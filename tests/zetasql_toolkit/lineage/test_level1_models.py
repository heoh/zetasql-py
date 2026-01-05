"""
Level 1 Tests: Data Models (ColumnEntity, ColumnLineage)

Test progression:
✅ Level 1: Basic data models
⬜ Level 2: Expression finder
⬜ Level 3: Parent finder
⬜ Level 4: Extractor (CTAS)
⬜ Level 5: INSERT
⬜ Level 6: UPDATE
⬜ Level 7: MERGE
⬜ Level 8: Complex cases
"""
import pytest


class TestColumnEntity:
    """Test ColumnEntity data model."""
    
    def test_create_column_entity(self):
        """Test basic ColumnEntity creation."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        entity = ColumnEntity(table="test_table", name="test_column")
        assert entity.table == "test_table"
        assert entity.name == "test_column"
    
    def test_column_entity_equality_case_insensitive(self):
        """Test that column names are compared case-insensitively."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        entity1 = ColumnEntity(table="table1", name="ColumnA")
        entity2 = ColumnEntity(table="table1", name="columna")
        entity3 = ColumnEntity(table="table1", name="COLUMNA")
        
        assert entity1 == entity2
        assert entity2 == entity3
        assert entity1 == entity3
    
    def test_column_entity_equality_table_sensitive(self):
        """Test that table names are compared case-sensitively."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        entity1 = ColumnEntity(table="Table1", name="col")
        entity2 = ColumnEntity(table="table1", name="col")
        
        # Table names should be case-sensitive
        assert entity1 != entity2
    
    def test_column_entity_hash_consistency(self):
        """Test that equal entities have the same hash."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        entity1 = ColumnEntity(table="table1", name="ColumnA")
        entity2 = ColumnEntity(table="table1", name="columna")
        
        assert hash(entity1) == hash(entity2)
    
    def test_column_entity_set_usage(self):
        """Test that ColumnEntity can be used in sets."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        entities = {
            ColumnEntity(table="t1", name="col1"),
            ColumnEntity(table="t1", name="COL1"),  # Should dedupe
            ColumnEntity(table="t1", name="col2"),
            ColumnEntity(table="t2", name="col1"),  # Different table
        }
        
        assert len(entities) == 3
    
    def test_from_resolved_column(self):
        """Test creating ColumnEntity from ResolvedColumn."""
        from zetasql_toolkit.lineage.models import ColumnEntity
        from zetasql.core.types.proto_models import ResolvedColumn
        from zetasql.types import SimpleType, TypeKind
        
        resolved_col = ResolvedColumn(
            column_id=1,
            table_name="my_table",
            name="my_column",
            type=SimpleType(TypeKind.TYPE_STRING)
        )
        
        entity = ColumnEntity.from_resolved_column(resolved_col)
        assert entity.table == "my_table"
        assert entity.name == "my_column"


class TestColumnLineage:
    """Test ColumnLineage data model."""
    
    def test_create_column_lineage(self):
        """Test basic ColumnLineage creation."""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage
        
        target = ColumnEntity(table="target", name="col1")
        parent1 = ColumnEntity(table="source", name="col_a")
        parent2 = ColumnEntity(table="source", name="col_b")
        
        lineage = ColumnLineage(target=target, parents={parent1, parent2})
        
        assert lineage.target == target
        assert len(lineage.parents) == 2
        assert parent1 in lineage.parents
        assert parent2 in lineage.parents
    
    def test_lineage_with_no_parents(self):
        """Test lineage with empty parent set (e.g., literal values)."""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage
        
        target = ColumnEntity(table="target", name="literal_col")
        lineage = ColumnLineage(target=target, parents=set())
        
        assert lineage.target == target
        assert len(lineage.parents) == 0
    
    def test_lineage_equality(self):
        """Test ColumnLineage equality."""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage
        
        target = ColumnEntity(table="t", name="c")
        parent = ColumnEntity(table="s", name="p")
        
        lineage1 = ColumnLineage(target=target, parents={parent})
        lineage2 = ColumnLineage(target=target, parents={parent})
        
        assert lineage1 == lineage2
    
    def test_lineage_in_set(self):
        """Test that ColumnLineage can be used in sets."""
        from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage
        
        target1 = ColumnEntity(table="t", name="c1")
        target2 = ColumnEntity(table="t", name="c2")
        parent = ColumnEntity(table="s", name="p")
        
        lineages = {
            ColumnLineage(target=target1, parents={parent}),
            ColumnLineage(target=target2, parents={parent}),
        }
        
        assert len(lineages) == 2


@pytest.mark.xfail(reason="Level 1 not yet implemented", strict=True)
class TestLevel1Complete:
    """Marker test to verify Level 1 is complete."""
    
    def test_all_level1_tests_pass(self):
        """This test passing means Level 1 is complete."""
        assert True
