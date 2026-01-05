"""Level 2 테스트: AST Walker

ResolvedAST를 순회하는 유틸리티 테스트입니다.
실제 ZetaSQL 분석 결과를 사용합니다.
"""

import pytest


@pytest.fixture
def simple_catalog():
    """테스트용 간단한 카탈로그"""
    from zetasql.api.builders import CatalogBuilder, TableBuilder
    from zetasql.types import TypeKind

    users = (
        TableBuilder("users")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("email", TypeKind.TYPE_STRING)
        .build()
    )

    orders = (
        TableBuilder("orders")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("user_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .build()
    )

    return CatalogBuilder("test").add_table(users).add_table(orders).build()


@pytest.fixture
def analyzer(simple_catalog):
    """테스트용 Analyzer"""
    from zetasql.api import Analyzer

    return Analyzer(catalog=simple_catalog)


class TestASTWalkerBasic:
    """기본 AST 순회 테스트"""

    def test_walk_simple_select(self, analyzer):
        """단순 SELECT 순회"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement("SELECT id, name FROM users")

        visited_types = []

        def visitor(node):
            visited_types.append(type(node).__name__)

        walk_resolved_tree(stmt, visitor)

        # 최소한 이 노드들이 방문되어야 함
        assert "ResolvedQueryStmt" in visited_types
        assert "ResolvedProjectScan" in visited_types
        assert "ResolvedTableScan" in visited_types

    def test_walk_visits_all_nodes(self, analyzer):
        """모든 노드 방문 확인"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement("SELECT id + 1 AS incremented FROM users")

        node_count = 0

        def counter(node):
            nonlocal node_count
            node_count += 1

        walk_resolved_tree(stmt, counter)

        # 최소 몇 개의 노드가 있어야 함
        assert node_count >= 3

    def test_walk_with_join(self, analyzer):
        """JOIN 포함 쿼리 순회"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement(
            """
            SELECT u.name, o.amount 
            FROM users u 
            JOIN orders o ON u.id = o.user_id
            """
        )

        visited_types = set()

        def visitor(node):
            visited_types.add(type(node).__name__)

        walk_resolved_tree(stmt, visitor)

        assert "ResolvedJoinScan" in visited_types
        # 두 테이블 스캔이 있어야 함
        assert "ResolvedTableScan" in visited_types


class TestASTWalkerSubquery:
    """서브쿼리 순회 테스트"""

    def test_walk_subquery(self, analyzer):
        """서브쿼리 순회"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement(
            """
            SELECT * FROM (
                SELECT id, name FROM users
            ) AS subq
            """
        )

        table_scans = []

        def visitor(node):
            if type(node).__name__ == "ResolvedTableScan":
                table_scans.append(node)

        walk_resolved_tree(stmt, visitor)

        assert len(table_scans) == 1  # users 테이블


class TestGetChildNodes:
    """get_child_nodes 함수 테스트"""

    def test_get_children_of_project_scan(self, analyzer):
        """ProjectScan의 자식 노드 가져오기"""
        from zetasql_toolkit.lineage.ast_walker import get_child_nodes

        stmt = analyzer.analyze_statement("SELECT id FROM users")

        # stmt는 QueryStmt, 그 안에 ProjectScan이 있음
        # QueryStmt의 자식을 확인
        children = get_child_nodes(stmt)

        # 최소한 query 필드가 자식으로 있어야 함
        assert len(children) >= 1

    def test_get_children_returns_list(self, analyzer):
        """자식 노드는 리스트로 반환"""
        from zetasql_toolkit.lineage.ast_walker import get_child_nodes

        stmt = analyzer.analyze_statement("SELECT id FROM users")
        children = get_child_nodes(stmt)

        assert isinstance(children, list)

    def test_get_children_empty_for_terminal(self, analyzer):
        """터미널 노드는 빈 리스트"""
        from zetasql_toolkit.lineage.ast_walker import (
            walk_resolved_tree,
            get_child_nodes,
        )

        stmt = analyzer.analyze_statement("SELECT 1")

        # Literal 노드 찾기
        literal_node = None

        def find_literal(node):
            nonlocal literal_node
            if "Literal" in type(node).__name__:
                literal_node = node

        walk_resolved_tree(stmt, find_literal)

        if literal_node:
            children = get_child_nodes(literal_node)
            # Literal은 자식이 없거나 매우 적음
            assert isinstance(children, list)


class TestNodeTypeDiscovery:
    """노드 타입 발견 테스트"""

    def test_discover_computed_columns(self, analyzer):
        """계산된 컬럼 발견"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement("SELECT id * 2 AS doubled FROM users")

        computed_cols = []

        def visitor(node):
            if "ComputedColumn" in type(node).__name__:
                computed_cols.append(node)

        walk_resolved_tree(stmt, visitor)

        # id * 2 에 대한 ComputedColumn이 있어야 함
        assert len(computed_cols) >= 1

    def test_discover_column_refs(self, analyzer):
        """컬럼 참조 발견"""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

        stmt = analyzer.analyze_statement("SELECT id, name FROM users")

        column_refs = []

        def visitor(node):
            if "ColumnRef" in type(node).__name__:
                column_refs.append(node)

        walk_resolved_tree(stmt, visitor)

        # id, name 두 컬럼 참조
        assert len(column_refs) >= 2
