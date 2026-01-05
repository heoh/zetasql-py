"""Level 4 테스트: ParentColumnFinder

컬럼의 terminal(최종 소스) 컬럼을 추적하는 테스트입니다.
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
        .add_column("status", TypeKind.TYPE_STRING)
        .build()
    )

    products = (
        TableBuilder("products")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .build()
    )

    return (
        CatalogBuilder("test")
        .add_table(users)
        .add_table(orders)
        .add_table(products)
        .build()
    )


@pytest.fixture
def analyzer(simple_catalog):
    """테스트용 Analyzer"""
    from zetasql.api import Analyzer

    return Analyzer(catalog=simple_catalog)


def get_output_column_and_stmt(analyzer, sql: str, column_index: int = 0):
    """SQL에서 출력 컬럼과 statement 가져오기"""
    stmt = analyzer.analyze_statement(sql)

    # QueryStmt의 output_column_list에서 컬럼 가져오기
    if hasattr(stmt, "output_column_list"):
        output_cols = stmt.output_column_list
        if column_index < len(output_cols):
            return output_cols[column_index].column, stmt
    return None, stmt


class TestDirectColumnSelection:
    """직접 컬럼 선택 테스트"""

    def test_simple_select(self, analyzer):
        """단순 SELECT: 직접 컬럼 매핑"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(analyzer, "SELECT name FROM users")

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert len(parents) == 1
        assert "name" in parent_names

    def test_select_with_alias(self, analyzer):
        """별칭 사용: 소스 컬럼 추적"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(
            analyzer, "SELECT name AS user_name FROM users"
        )

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert len(parents) == 1
        assert "name" in parent_names

    def test_select_multiple_columns(self, analyzer):
        """여러 컬럼 선택: 각각 독립 추적"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        # 첫 번째 컬럼 (name)
        col1, stmt = get_output_column_and_stmt(
            analyzer, "SELECT name, email FROM users", column_index=0
        )
        parents1 = ParentColumnFinder.find_parents_for_column(stmt, col1)

        # 두 번째 컬럼 (email)
        col2, _ = get_output_column_and_stmt(
            analyzer, "SELECT name, email FROM users", column_index=1
        )
        parents2 = ParentColumnFinder.find_parents_for_column(stmt, col2)

        assert {p.name for p in parents1} == {"name"}
        assert {p.name for p in parents2} == {"email"}


class TestExpressionTracking:
    """표현식 추적 테스트"""

    def test_function_expression(self, analyzer):
        """함수 표현식: UPPER(col)"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(
            analyzer, "SELECT UPPER(name) AS upper_name FROM users"
        )

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert len(parents) == 1
        assert "name" in parent_names

    def test_nested_expression(self, analyzer):
        """중첩 표현식: UPPER(CONCAT(col1, col2))"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(
            analyzer, "SELECT UPPER(CONCAT(name, email)) AS combined FROM users"
        )

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert len(parents) == 2
        assert "name" in parent_names
        assert "email" in parent_names

    def test_arithmetic_expression(self, analyzer):
        """산술 표현식: col1 + col2"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(
            analyzer, "SELECT amount + 10 AS adjusted FROM orders"
        )

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert len(parents) == 1
        assert "amount" in parent_names


class TestJoinTracking:
    """JOIN 추적 테스트"""

    def test_simple_join(self, analyzer):
        """단순 JOIN: 양쪽 테이블 컬럼 추적"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT u.name, o.amount 
        FROM users u 
        JOIN orders o ON u.id = o.user_id
        """

        # 첫 번째 컬럼 (u.name)
        col1, stmt = get_output_column_and_stmt(analyzer, sql, column_index=0)
        parents1 = ParentColumnFinder.find_parents_for_column(stmt, col1)

        # 두 번째 컬럼 (o.amount)
        col2, _ = get_output_column_and_stmt(analyzer, sql, column_index=1)
        parents2 = ParentColumnFinder.find_parents_for_column(stmt, col2)

        assert {p.name for p in parents1} == {"name"}
        assert {p.name for p in parents2} == {"amount"}

    def test_join_with_expression(self, analyzer):
        """JOIN + 표현식"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT CONCAT(u.name, ' - ', o.status) AS combined
        FROM users u 
        JOIN orders o ON u.id = o.user_id
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert "name" in parent_names
        assert "status" in parent_names


class TestSubqueryTracking:
    """서브쿼리 추적 테스트"""

    def test_simple_subquery(self, analyzer):
        """단순 서브쿼리: 내부 컬럼 추적"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT subq.user_name
        FROM (
            SELECT name AS user_name FROM users
        ) AS subq
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        # 최종 소스는 users.name
        assert "name" in parent_names

    def test_nested_subquery(self, analyzer):
        """중첩 서브쿼리"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT outer_q.final_name
        FROM (
            SELECT inner_q.mid_name AS final_name
            FROM (
                SELECT name AS mid_name FROM users
            ) AS inner_q
        ) AS outer_q
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        # 최종 소스는 users.name
        assert "name" in parent_names

    def test_subquery_with_expression(self, analyzer):
        """서브쿼리 내 표현식"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT subq.upper_name
        FROM (
            SELECT UPPER(name) AS upper_name FROM users
        ) AS subq
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert "name" in parent_names


class TestWithClause:
    """WITH 절 (CTE) 추적 테스트"""

    def test_simple_cte(self, analyzer):
        """단순 CTE"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        WITH user_cte AS (
            SELECT name, email FROM users
        )
        SELECT name FROM user_cte
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert "name" in parent_names

    def test_cte_with_expression(self, analyzer):
        """CTE 내 표현식"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        WITH processed AS (
            SELECT UPPER(name) AS upper_name FROM users
        )
        SELECT upper_name FROM processed
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        assert "name" in parent_names

    def test_multiple_cte_references(self, analyzer):
        """CTE 여러 번 참조"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        WITH user_cte AS (
            SELECT id, name FROM users
        )
        SELECT a.name AS name1, b.name AS name2
        FROM user_cte a
        JOIN user_cte b ON a.id = b.id
        """

        col1, stmt = get_output_column_and_stmt(analyzer, sql, column_index=0)
        parents1 = ParentColumnFinder.find_parents_for_column(stmt, col1)

        col2, _ = get_output_column_and_stmt(analyzer, sql, column_index=1)
        parents2 = ParentColumnFinder.find_parents_for_column(stmt, col2)

        # 둘 다 users.name을 소스로 해야 함
        assert "name" in {p.name for p in parents1}
        assert "name" in {p.name for p in parents2}


class TestUnionOperations:
    """UNION 연산 추적 테스트"""

    def test_simple_union(self, analyzer):
        """UNION: 양쪽 소스 추적"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT name FROM users
        UNION ALL
        SELECT name FROM products
        """

        col, stmt = get_output_column_and_stmt(analyzer, sql)
        parents = ParentColumnFinder.find_parents_for_column(stmt, col)
        parent_names = {p.name for p in parents}

        # UNION의 결과는 양쪽 소스 모두 포함
        assert "name" in parent_names
        # 양쪽 테이블에서 오므로 2개 이상
        assert len(parents) >= 2


class TestGroupBy:
    """GROUP BY 추적 테스트"""

    def test_grouped_column(self, analyzer):
        """GROUP BY 컬럼"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        sql = """
        SELECT status, SUM(amount) AS total
        FROM orders
        GROUP BY status
        """

        # status 컬럼
        col1, stmt = get_output_column_and_stmt(analyzer, sql, column_index=0)
        parents1 = ParentColumnFinder.find_parents_for_column(stmt, col1)

        # total 컬럼
        col2, _ = get_output_column_and_stmt(analyzer, sql, column_index=1)
        parents2 = ParentColumnFinder.find_parents_for_column(stmt, col2)

        assert "status" in {p.name for p in parents1}
        assert "amount" in {p.name for p in parents2}


class TestTableNameTracking:
    """테이블 이름 추적 테스트"""

    def test_table_name_in_parent(self, analyzer):
        """부모 컬럼에 테이블 이름 포함"""
        from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

        col, stmt = get_output_column_and_stmt(analyzer, "SELECT name FROM users")

        parents = ParentColumnFinder.find_parents_for_column(stmt, col)

        assert len(parents) == 1
        # table_name 속성이 있어야 함
        assert hasattr(parents[0], "table_name")
        # 테이블 이름이 포함되어야 함
        assert "users" in parents[0].table_name.lower()
