"""Level 1 테스트: 데이터 모델 (ColumnEntity, ColumnLineage)

이 테스트는 다른 레벨 구현 없이 독립적으로 실행 가능합니다.
"""

import pytest
from dataclasses import FrozenInstanceError


class TestColumnEntity:
    """ColumnEntity 데이터 모델 테스트"""

    def test_create_column_entity(self):
        """기본 생성 테스트"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="my_table", name="my_column")

        assert entity.table == "my_table"
        assert entity.name == "my_column"

    def test_equality_same_case(self):
        """동일 케이스 동등성 테스트"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity1 = ColumnEntity(table="table1", name="col1")
        entity2 = ColumnEntity(table="table1", name="col1")

        assert entity1 == entity2

    def test_equality_case_insensitive_column_name(self):
        """컬럼 이름은 대소문자 무시 비교"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity1 = ColumnEntity(table="table1", name="Column1")
        entity2 = ColumnEntity(table="table1", name="column1")

        assert entity1 == entity2

    def test_equality_case_sensitive_table_name(self):
        """테이블 이름은 대소문자 구분"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity1 = ColumnEntity(table="Table1", name="col1")
        entity2 = ColumnEntity(table="table1", name="col1")

        # 테이블 이름은 대소문자 구분 (BigQuery 등 일부 시스템)
        # 참고: Java 구현에서는 테이블도 equals로 직접 비교
        assert entity1 != entity2

    def test_hash_consistency(self):
        """해시 일관성 테스트 (Set/Dict에서 사용)"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity1 = ColumnEntity(table="table1", name="Col1")
        entity2 = ColumnEntity(table="table1", name="col1")

        # 동등한 객체는 동일한 해시값
        assert hash(entity1) == hash(entity2)

        # Set에서 중복 제거 확인
        entities = {entity1, entity2}
        assert len(entities) == 1

    def test_qualified_name(self):
        """정규화된 이름 (table.column)"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="project.dataset.table", name="column1")

        assert entity.table == "project.dataset.table"
        assert entity.name == "column1"
        # 선택적: __str__ 구현 시
        # assert str(entity) == "project.dataset.table.column1"

    def test_from_resolved_column(self):
        """ResolvedColumn에서 ColumnEntity 생성"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        # Mock ResolvedColumn 객체 생성
        class MockResolvedColumn:
            def __init__(self, table_name: str, name: str):
                self.table_name = table_name
                self.name = name

        resolved_col = MockResolvedColumn("source_table", "source_column")
        entity = ColumnEntity.from_resolved_column(resolved_col)

        assert entity.table == "source_table"
        assert entity.name == "source_column"

    def test_immutable(self):
        """불변성 테스트 (frozen dataclass)"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="table1", name="col1")

        with pytest.raises((FrozenInstanceError, AttributeError)):
            entity.table = "modified"


class TestColumnLineage:
    """ColumnLineage 데이터 모델 테스트"""

    def test_create_column_lineage(self):
        """기본 생성 테스트"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target = ColumnEntity(table="target_table", name="target_col")
        parent1 = ColumnEntity(table="source1", name="col1")
        parent2 = ColumnEntity(table="source2", name="col2")

        lineage = ColumnLineage(target=target, parents=frozenset([parent1, parent2]))

        assert lineage.target == target
        assert len(lineage.parents) == 2
        assert parent1 in lineage.parents
        assert parent2 in lineage.parents

    def test_empty_parents(self):
        """부모 없는 계보 (리터럴 값 등)"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target = ColumnEntity(table="target", name="constant_col")
        lineage = ColumnLineage(target=target, parents=frozenset())

        assert lineage.target == target
        assert len(lineage.parents) == 0

    def test_lineage_hashable(self):
        """Set에서 사용 가능 테스트"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target = ColumnEntity(table="target", name="col")
        parent = ColumnEntity(table="source", name="col")

        lineage1 = ColumnLineage(target=target, parents=frozenset([parent]))
        lineage2 = ColumnLineage(target=target, parents=frozenset([parent]))

        # Set에 추가 가능
        lineages = {lineage1, lineage2}
        assert len(lineages) == 1

    def test_lineage_equality(self):
        """계보 동등성 테스트"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target = ColumnEntity(table="target", name="col")
        parent1 = ColumnEntity(table="source", name="col1")
        parent2 = ColumnEntity(table="source", name="col2")

        lineage1 = ColumnLineage(target=target, parents=frozenset([parent1, parent2]))
        lineage2 = ColumnLineage(target=target, parents=frozenset([parent2, parent1]))

        # frozenset은 순서 무관
        assert lineage1 == lineage2

    def test_different_target_not_equal(self):
        """다른 타겟은 다른 계보"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target1 = ColumnEntity(table="target", name="col1")
        target2 = ColumnEntity(table="target", name="col2")
        parent = ColumnEntity(table="source", name="col")

        lineage1 = ColumnLineage(target=target1, parents=frozenset([parent]))
        lineage2 = ColumnLineage(target=target2, parents=frozenset([parent]))

        assert lineage1 != lineage2

    def test_repr_readable(self):
        """읽기 좋은 문자열 표현"""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

        target = ColumnEntity(table="target", name="result")
        parent = ColumnEntity(table="source", name="input")

        lineage = ColumnLineage(target=target, parents=frozenset([parent]))

        repr_str = repr(lineage)
        assert "target" in repr_str
        assert "result" in repr_str


class TestColumnEntityEdgeCases:
    """경계 조건 테스트"""

    def test_empty_table_name(self):
        """빈 테이블 이름 (익명 소스)"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        # ZetaSQL에서 익명 테이블/서브쿼리는 빈 이름 가능
        entity = ColumnEntity(table="", name="col")
        assert entity.table == ""
        assert entity.name == "col"

    def test_struct_field_name(self):
        """STRUCT 필드 이름 (점 포함)"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="table1", name="struct_col.field1.nested")
        assert entity.name == "struct_col.field1.nested"

    def test_special_characters_in_name(self):
        """특수 문자가 포함된 컬럼 이름"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="table", name="column with spaces")
        assert entity.name == "column with spaces"

    def test_unicode_names(self):
        """유니코드 이름"""
        from zetasql_toolkit.lineage.models import ColumnEntity

        entity = ColumnEntity(table="테이블", name="컬럼")
        assert entity.table == "테이블"
        assert entity.name == "컬럼"
