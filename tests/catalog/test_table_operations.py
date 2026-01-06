"""
Table operations on SimpleCatalog - mirrors Java SimpleCatalogTest.java (table sections)

Tests for adding tables to catalogs and retrieving them.
"""

import pytest
from zetasql.api import TypeFactory
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import TypeKind


class TestCatalogTableAdd:
    """Test adding tables to catalog - Java: testAdds() for tables"""
    
    def test_add_table_via_builder(self):
        """Test adding table via CatalogBuilder."""
        table = (TableBuilder("Orders")
            .add_column("order_id", TypeKind.TYPE_INT64)
            .add_column("amount", TypeKind.TYPE_DOUBLE)
            .build())
        
        catalog = (CatalogBuilder("db")
            .add_table(table)
            .build())
        
        assert len(catalog.table) == 1
        assert catalog.table[0].name == "Orders"
        assert len(catalog.table[0].column) == 2
    
    def test_add_multiple_tables(self):
        """Test adding multiple tables."""
        t1 = TableBuilder("T1").add_column("c1", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("T2").add_column("c2", TypeKind.TYPE_STRING).build()
        t3 = TableBuilder("T3").add_column("c3", TypeKind.TYPE_BOOL).build()
        
        catalog = (CatalogBuilder("db")
            .add_table(t1)
            .add_table(t2)
            .add_table(t3)
            .build())
        
        assert len(catalog.table) == 3
        
        # Verify tables are in order
        assert catalog.table[0].name == "T1"
        assert catalog.table[1].name == "T2"
        assert catalog.table[2].name == "T3"
    
    def test_add_table_with_complex_types(self):
        """Test adding table with array and struct columns."""
        # Array column
        array_type = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        # Struct column
        struct_type = TypeFactory.create_struct_type([
            ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
        ])
        
        table = (TableBuilder("ComplexTable")
            .add_column("id", TypeKind.TYPE_INT64)
            .add_column("tags", array_type)
            .add_column("address", struct_type)
            .build())
        
        catalog = CatalogBuilder("db").add_table(table).build()
        
        assert len(catalog.table) == 1
        assert len(catalog.table[0].column) == 3
        
        # Verify complex types
        cols = catalog.table[0].column
        assert cols[1].type.type_kind == TypeKind.TYPE_ARRAY
        assert cols[2].type.type_kind == TypeKind.TYPE_STRUCT


class TestCatalogTableRetrieval:
    """Test retrieving tables from catalog."""
    
    def test_access_table_by_index(self):
        """Test accessing table via proto list."""
        table = TableBuilder("MyTable").add_column("id", TypeKind.TYPE_INT64).build()
        catalog = CatalogBuilder("db").add_table(table).build()
        
        # Direct proto access
        retrieved = catalog.table[0]
        assert retrieved.name == "MyTable"
        assert len(retrieved.column) == 1
    
    def test_get_table_list_method(self):
        """Test SimpleCatalog.get_table_list().
        
        Expected API (Java):
            ImmutableList<SimpleTable> SimpleCatalog.getTableList()
        """
        t1 = TableBuilder("T1").add_column("c1", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("T2").add_column("c2", TypeKind.TYPE_STRING).build()
        
        catalog = (CatalogBuilder("db")
            .add_table(t1)
            .add_table(t2)
            .build())
        
        # Expected API
        tables = catalog.get_table_list()
        
        assert isinstance(tables, list)
        assert len(tables) == 2
        assert tables[0].name == "T1"
        assert tables[1].name == "T2"
    
    def test_get_table_by_name(self):
        """Test SimpleCatalog.get_table(name).
        
        Expected API (Java):
            SimpleTable SimpleCatalog.getTable(String name)
        """
        table = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        catalog = CatalogBuilder("db").add_table(table).build()
        
        # Expected API
        retrieved = catalog.get_table("Orders")
        
        assert retrieved is not None
        assert retrieved.name == "Orders"
    
    def test_get_table_case_insensitive(self):
        """Test table lookup is case-insensitive - Java behavior.
        
        Java: catalog.getTable("T1") == catalog.getTable("t1") == catalog.getTable("T1")
        """
        table = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        catalog = CatalogBuilder("db").add_table(table).build()
        
        # Expected: all should return same table
        assert catalog.get_table("Orders") is not None
        assert catalog.get_table("ORDERS") is not None
        assert catalog.get_table("orders") is not None
        
        # All should refer to same logical table
        assert catalog.get_table("Orders").name == catalog.get_table("ORDERS").name
    
    def test_get_table_name_list(self):
        """Test SimpleCatalog.getTableNameList().
        
        Expected API (Java):
            ImmutableList<String> SimpleCatalog.getTableNameList()
        """
        t1 = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("Products").add_column("id", TypeKind.TYPE_INT64).build()
        
        catalog = (CatalogBuilder("db")
            .add_table(t1)
            .add_table(t2)
            .build())
        
        # Expected API
        names = catalog.get_table_name_list()
        
        assert isinstance(names, list)
        assert len(names) == 2
        # Java returns lowercase names
        assert "orders" in names or "Orders" in names
        assert "products" in names or "Products" in names


class TestCatalogTableErrors:
    """Test error handling for table operations."""
    
    def test_add_duplicate_table_raises_error(self):
        """Test that adding duplicate table raises error.
        
        Java behavior: throws IllegalArgumentException
        """
        table1 = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        
        catalog_builder = CatalogBuilder("db").add_table(table1)
        
        # Attempting to add table with same name should raise
        table2 = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        
        with pytest.raises(ValueError):
            catalog_builder.add_table(table2)
    
    def test_add_table_case_insensitive_duplicate(self):
        """Test duplicate detection is case-insensitive.
        
        Java behavior: "Orders" and "ORDERS" are considered duplicates
        """
        table1 = TableBuilder("Orders").add_column("id", TypeKind.TYPE_INT64).build()
        table2 = TableBuilder("ORDERS").add_column("id", TypeKind.TYPE_INT64).build()
        
        catalog_builder = CatalogBuilder("db").add_table(table1)
        
        # Should raise error (case-insensitive)
        with pytest.raises(ValueError):
            catalog_builder.add_table(table2)
    
    def test_get_nonexistent_table_returns_none(self):
        """Test getting non-existent table returns None.
        
        Java behavior: returns null for non-existent table
        """
        catalog = CatalogBuilder("db").build()
        
        # Expected: returns None (not raise)
        result = catalog.get_table("NonExistentTable")
        assert result is None
