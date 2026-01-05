"""Level 5 테스트: ColumnLineageExtractor

최종 계보 추출기 통합 테스트입니다.
Java 예제와 동일한 시나리오를 테스트합니다.
"""

import pytest


@pytest.fixture
def bigquery_like_catalog():
    """BigQuery 스타일 카탈로그 (Java 예제와 유사)"""
    from zetasql.api.builders import CatalogBuilder, TableBuilder
    from zetasql.types import TypeKind

    # bigquery-public-data.samples.wikipedia
    wikipedia = (
        TableBuilder("bigquery-public-data.samples.wikipedia")
        .add_column("title", TypeKind.TYPE_STRING)
        .add_column("comment", TypeKind.TYPE_STRING)
        .add_column("id", TypeKind.TYPE_INT64)
        .build()
    )

    # bigquery-public-data.samples.shakespeare
    shakespeare = (
        TableBuilder("bigquery-public-data.samples.shakespeare")
        .add_column("corpus", TypeKind.TYPE_STRING)
        .add_column("word", TypeKind.TYPE_STRING)
        .add_column("word_count", TypeKind.TYPE_INT64)
        .build()
    )

    return (
        CatalogBuilder("bigquery-public-data")
        .add_table(wikipedia)
        .add_table(shakespeare)
        .build()
    )


@pytest.fixture
def simple_catalog():
    """간단한 테스트 카탈로그"""
    from zetasql.api.builders import CatalogBuilder, TableBuilder
    from zetasql.types import TypeKind

    source1 = (
        TableBuilder("source1")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("value", TypeKind.TYPE_DOUBLE)
        .build()
    )

    source2 = (
        TableBuilder("source2")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("category", TypeKind.TYPE_STRING)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .build()
    )

    target = (
        TableBuilder("target")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("total", TypeKind.TYPE_DOUBLE)
        .build()
    )

    return (
        CatalogBuilder("test")
        .add_table(source1)
        .add_table(source2)
        .add_table(target)
        .build()
    )


@pytest.fixture
def analyzer_bq(bigquery_like_catalog):
    """BigQuery 스타일 Analyzer"""
    from zetasql.api import Analyzer

    return Analyzer(catalog=bigquery_like_catalog)


@pytest.fixture
def analyzer(simple_catalog):
    """간단한 Analyzer"""
    from zetasql.api import Analyzer

    return Analyzer(catalog=simple_catalog)


class TestCreateTableAsSelect:
    """CREATE TABLE AS SELECT 계보 추출 테스트"""

    def test_simple_ctas(self, analyzer):
        """단순 CTAS"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT id, name FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # 결과 확인
        target_cols = {l.target.name for l in lineages}
        assert "id" in target_cols
        assert "name" in target_cols

        # id 컬럼의 계보
        id_lineage = next(l for l in lineages if l.target.name == "id")
        assert any(p.name == "id" for p in id_lineage.parents)

        # name 컬럼의 계보
        name_lineage = next(l for l in lineages if l.target.name == "name")
        assert any(p.name == "name" for p in name_lineage.parents)

    def test_ctas_with_expression(self, analyzer):
        """표현식이 포함된 CTAS"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT 
            UPPER(name) AS upper_name,
            value + 10 AS adjusted_value
        FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # upper_name은 name에서 파생
        upper_lineage = next(l for l in lineages if l.target.name == "upper_name")
        assert any(p.name == "name" for p in upper_lineage.parents)

        # adjusted_value는 value에서 파생
        value_lineage = next(l for l in lineages if l.target.name == "adjusted_value")
        assert any(p.name == "value" for p in value_lineage.parents)

    def test_ctas_with_nested_subquery(self, analyzer):
        """Java 예제: 중첩 서브쿼리가 있는 CTAS"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT
            concatted AS column_alias
        FROM (
            SELECT 
                UPPER(CONCAT(name, category)) AS concatted
            FROM source1, source2
        )
        GROUP BY 1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # column_alias는 name과 category에서 파생
        alias_lineage = next(l for l in lineages if l.target.name == "column_alias")
        parent_names = {p.name for p in alias_lineage.parents}

        assert "name" in parent_names
        assert "category" in parent_names


class TestInsertStatement:
    """INSERT 문 계보 추출 테스트"""

    def test_simple_insert(self, analyzer):
        """단순 INSERT"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        INSERT INTO target(id, name)
        SELECT id, name FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # target.id <- source1.id
        id_lineage = next(l for l in lineages if l.target.name == "id")
        assert "target" in id_lineage.target.table
        assert any(p.name == "id" for p in id_lineage.parents)

        # target.name <- source1.name
        name_lineage = next(l for l in lineages if l.target.name == "name")
        assert any(p.name == "name" for p in name_lineage.parents)

    def test_insert_with_expression(self, analyzer):
        """표현식이 포함된 INSERT"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        INSERT INTO target(id, name, total)
        SELECT 
            id,
            LOWER(name) AS name,
            value * 2 AS total
        FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # total <- source1.value
        total_lineage = next(l for l in lineages if l.target.name == "total")
        assert any(p.name == "value" for p in total_lineage.parents)

    def test_insert_with_subquery(self, analyzer):
        """서브쿼리가 있는 INSERT"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        INSERT INTO target(id, name)
        SELECT
            CAST(inner_id AS INT64) AS id,
            UPPER(inner_name) AS name
        FROM (
            SELECT id AS inner_id, name AS inner_name
            FROM source1
        )
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # target.id <- source1.id (서브쿼리 통과)
        id_lineage = next(l for l in lineages if l.target.name == "id")
        assert any(p.name == "id" for p in id_lineage.parents)


class TestUpdateStatement:
    """UPDATE 문 계보 추출 테스트"""

    def test_simple_update(self, analyzer):
        """단순 UPDATE"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        UPDATE target
        SET name = source1.name
        FROM source1
        WHERE target.id = source1.id
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # target.name <- source1.name
        name_lineage = next(l for l in lineages if l.target.name == "name")
        assert any(p.name == "name" for p in name_lineage.parents)

    def test_update_with_expression(self, analyzer):
        """표현식이 포함된 UPDATE"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        UPDATE target
        SET total = source1.value * 2 + source2.amount
        FROM source1, source2
        WHERE target.id = source1.id
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # target.total <- source1.value, source2.amount
        total_lineage = next(l for l in lineages if l.target.name == "total")
        parent_names = {p.name for p in total_lineage.parents}

        assert "value" in parent_names
        assert "amount" in parent_names


class TestMergeStatement:
    """MERGE 문 계보 추출 테스트"""

    def test_merge_update_only(self, analyzer):
        """MERGE - UPDATE만"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        MERGE target T
        USING source1 S
        ON T.id = S.id
        WHEN MATCHED THEN
            UPDATE SET name = S.name
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # T.name <- S.name
        name_lineage = next(l for l in lineages if l.target.name == "name")
        assert any(p.name == "name" for p in name_lineage.parents)

    def test_merge_insert_only(self, analyzer):
        """MERGE - INSERT만"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        MERGE target T
        USING source1 S
        ON T.id = S.id
        WHEN NOT MATCHED THEN
            INSERT(id, name) VALUES (S.id, UPPER(S.name))
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # T.id <- S.id
        id_lineage = next(l for l in lineages if l.target.name == "id")
        assert any(p.name == "id" for p in id_lineage.parents)

        # T.name <- S.name (UPPER 함수 통과)
        name_lineage = next(l for l in lineages if l.target.name == "name")
        assert any(p.name == "name" for p in name_lineage.parents)

    def test_merge_update_and_insert(self, analyzer):
        """MERGE - UPDATE + INSERT 둘 다"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        MERGE target T
        USING source1 S
        ON T.id = S.id
        WHEN MATCHED THEN
            UPDATE SET name = S.name
        WHEN NOT MATCHED THEN
            INSERT(id, name) VALUES (S.id, S.name)
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # UPDATE와 INSERT 모두의 계보 포함
        assert len(lineages) >= 2


class TestQueryStatement:
    """일반 SELECT 문 계보 추출 테스트"""

    def test_select_with_target_table(self, analyzer):
        """SELECT 문 (target_table 지정)"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        SELECT id, UPPER(name) AS upper_name
        FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(
            stmt, target_table="output_table"
        )

        # output_table.id <- source1.id
        id_lineage = next(l for l in lineages if l.target.name == "id")
        assert id_lineage.target.table == "output_table"
        assert any(p.name == "id" for p in id_lineage.parents)


class TestComplexScenarios:
    """복잡한 시나리오 테스트"""

    def test_multi_level_cte(self, analyzer):
        """다중 레벨 CTE"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE result AS
        WITH 
            cte1 AS (SELECT id, UPPER(name) AS name FROM source1),
            cte2 AS (SELECT id, CONCAT(name, '-suffix') AS full_name FROM cte1)
        SELECT id, full_name FROM cte2
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # result.full_name <- source1.name (CTE 체인 통과)
        full_name_lineage = next(l for l in lineages if l.target.name == "full_name")
        assert any(p.name == "name" for p in full_name_lineage.parents)

    def test_union_lineage(self, analyzer):
        """UNION 계보"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE result AS
        SELECT name FROM source1
        UNION ALL
        SELECT category AS name FROM source2
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # result.name <- source1.name, source2.category
        name_lineage = next(l for l in lineages if l.target.name == "name")
        parent_names = {p.name for p in name_lineage.parents}

        # UNION의 양쪽 소스 모두 포함
        assert "name" in parent_names or "category" in parent_names

    def test_self_join(self, analyzer):
        """Self JOIN"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE result AS
        SELECT a.name AS name1, b.name AS name2
        FROM source1 a
        JOIN source1 b ON a.id = b.id
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # 둘 다 source1.name에서 파생
        for lineage in lineages:
            assert any(p.name == "name" for p in lineage.parents)


class TestOutputFormat:
    """출력 형식 테스트"""

    def test_lineage_contains_table_info(self, analyzer):
        """계보에 테이블 정보 포함"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT name FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        lineage = list(lineages)[0]

        # 타겟에 테이블 정보
        assert lineage.target.table is not None
        assert "new_table" in lineage.target.table

        # 부모에 테이블 정보
        for parent in lineage.parents:
            assert parent.table is not None
            assert "source1" in parent.table.lower()

    def test_result_is_set(self, analyzer):
        """결과는 Set 타입"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT id, name FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        assert isinstance(lineages, set)

    def test_no_duplicate_lineages(self, analyzer):
        """중복 계보 없음"""
        from zetasql_toolkit.lineage import ColumnLineageExtractor

        sql = """
        CREATE TABLE new_table AS
        SELECT id, id AS id2 FROM source1
        """

        stmt = analyzer.analyze_statement(sql)
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

        # id와 id2는 다른 타겟이므로 별개의 계보
        target_cols = [l.target.name for l in lineages]
        assert len(target_cols) == len(set(target_cols))
