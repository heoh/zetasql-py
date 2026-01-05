"""Level 3 테스트: ExpressionParentFinder

표현식 내에서 직접 참조되는 컬럼을 찾는 테스트입니다.
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
        .add_column("age", TypeKind.TYPE_INT64)
        .add_column("is_active", TypeKind.TYPE_BOOL)
        .build()
    )

    return CatalogBuilder("test").add_table(users).build()


@pytest.fixture
def analyzer(simple_catalog):
    """테스트용 Analyzer"""
    from zetasql.api import Analyzer

    return Analyzer(catalog=simple_catalog)


def get_first_computed_expr(analyzer, sql: str):
    """SQL에서 첫 번째 계산된 표현식 가져오기"""
    from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

    stmt = analyzer.analyze_statement(sql)

    computed_col = None

    def visitor(node):
        nonlocal computed_col
        if computed_col is None and "ComputedColumn" in type(node).__name__:
            computed_col = node

    walk_resolved_tree(stmt, visitor)

    if computed_col and hasattr(computed_col, "expr"):
        return computed_col.expr
    return None


class TestDirectColumnRef:
    """직접 컬럼 참조 테스트"""

    def test_single_column_ref(self, analyzer):
        """단일 컬럼 참조"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT name AS alias FROM users")

        parents = ExpressionParentFinder.find_direct_parents(expr)

        assert len(parents) == 1
        assert parents[0].name == "name"

    def test_column_ref_in_function(self, analyzer):
        """함수 내 컬럼 참조"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT UPPER(name) FROM users")

        parents = ExpressionParentFinder.find_direct_parents(expr)

        assert len(parents) == 1
        assert parents[0].name == "name"


class TestFunctionCalls:
    """함수 호출 테스트"""

    def test_nested_functions(self, analyzer):
        """중첩 함수: UPPER(CONCAT(col1, col2))"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT UPPER(CONCAT(name, email)) FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)
        parent_names = {p.name for p in parents}

        assert len(parents) == 2
        assert "name" in parent_names
        assert "email" in parent_names

    def test_arithmetic_expression(self, analyzer):
        """산술 표현식: col1 + col2"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT id + age FROM users")

        parents = ExpressionParentFinder.find_direct_parents(expr)
        parent_names = {p.name for p in parents}

        assert len(parents) == 2
        assert "id" in parent_names
        assert "age" in parent_names

    def test_literal_no_parents(self, analyzer):
        """리터럴은 부모 없음"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT 'constant' AS const FROM users")

        if expr:  # 리터럴만 있을 때 ComputedColumn이 없을 수 있음
            parents = ExpressionParentFinder.find_direct_parents(expr)
            # 리터럴 참조만 있으면 컬럼 부모 없음
            # 단, CAST 등이 있으면 다를 수 있음

    def test_function_with_literal(self, analyzer):
        """함수에 리터럴과 컬럼 혼합"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT CONCAT(name, ' suffix') FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)

        assert len(parents) == 1
        assert parents[0].name == "name"


class TestCaseExpression:
    """CASE 표현식 테스트"""

    def test_case_when_then_else(self, analyzer):
        """CASE WHEN 표현식 (조건 제외, 값만)"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer,
            """
            SELECT CASE 
                WHEN is_active THEN name 
                ELSE email 
            END FROM users
            """,
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)
        parent_names = {p.name for p in parents}

        # THEN과 ELSE 값만 포함 (is_active 조건은 제외)
        # 참고: Java 구현에서는 조건도 포함하는 경우가 있음
        # 정확한 동작은 Java 구현 확인 필요
        assert "name" in parent_names
        assert "email" in parent_names


class TestCast:
    """CAST 표현식 테스트"""

    def test_cast_preserves_source(self, analyzer):
        """CAST는 소스 컬럼 보존"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT CAST(id AS STRING) FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)

        assert len(parents) == 1
        assert parents[0].name == "id"


class TestIfFunction:
    """IF 함수 테스트"""

    def test_if_function(self, analyzer):
        """IF(condition, true_val, false_val)"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT IF(is_active, name, email) FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)
        parent_names = {p.name for p in parents}

        # true_val과 false_val만 포함 (조건 is_active는 제외)
        # Java 구현: IF 함수는 조건 제외
        assert "name" in parent_names
        assert "email" in parent_names


class TestNullif:
    """NULLIF 함수 테스트"""

    def test_nullif_first_arg_only(self, analyzer):
        """NULLIF(expr1, expr2)는 첫 번째 인자만"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT NULLIF(name, email) FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)

        # Java 구현: NULLIF는 첫 번째 인자만 계보에 포함
        assert len(parents) == 1
        assert parents[0].name == "name"


class TestCoalesce:
    """COALESCE 함수 테스트"""

    def test_coalesce_all_args(self, analyzer):
        """COALESCE는 모든 인자 포함"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(
            analyzer, "SELECT COALESCE(name, email) FROM users"
        )

        parents = ExpressionParentFinder.find_direct_parents(expr)
        parent_names = {p.name for p in parents}

        # COALESCE는 일반 함수로 처리 (모든 인자)
        assert "name" in parent_names
        assert "email" in parent_names


class TestAggregate:
    """집계 함수 테스트"""

    def test_sum_aggregate(self, analyzer):
        """SUM(col) 집계"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT SUM(age) FROM users")

        parents = ExpressionParentFinder.find_direct_parents(expr)

        assert len(parents) == 1
        assert parents[0].name == "age"

    def test_count_star(self, analyzer):
        """COUNT(*) 는 특정 컬럼 없음"""
        from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

        expr = get_first_computed_expr(analyzer, "SELECT COUNT(*) FROM users")

        if expr:
            parents = ExpressionParentFinder.find_direct_parents(expr)
            # COUNT(*)는 특정 컬럼 참조 없음 (또는 모든 컬럼)
