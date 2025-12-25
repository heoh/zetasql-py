"""
Tests for Builders (TableBuilder and CatalogBuilder)

Tests the fluent builder API for creating tables and catalogs.
"""

import pytest
from zetasql.builders import TableBuilder, CatalogBuilder
from zetasql.types import TypeKind
from zetasql.types.type_factory import TypeFactory
from zetasql.types.proto_models import SimpleTable, SimpleCatalog, ZetaSQLBuiltinFunctionOptions, LanguageOptions


class TestTableBuilder:
    """Test TableBuilder functionality."""
    
    def test_simple_table_creation(self):
        """Test creating a simple table with basic columns."""
        table = (TableBuilder("users")
            .add_column("id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .add_column("email", TypeKind.TYPE_STRING)
            .build())
        
        assert isinstance(table, SimpleTable)
        assert table.name == "users"
        assert len(table.column) == 3
        
        # Check columns
        assert table.column[0].name == "id"
        assert table.column[0].type.type_kind == TypeKind.TYPE_INT64
        assert table.column[1].name == "name"
        assert table.column[1].type.type_kind == TypeKind.TYPE_STRING
        assert table.column[2].name == "email"
        assert table.column[2].type.type_kind == TypeKind.TYPE_STRING
    
    def test_table_with_serialization_id(self):
        """Test table with explicit serialization ID."""
        table = (TableBuilder("products", serialization_id=42)
            .add_column("product_id", TypeKind.TYPE_INT64)
            .build())
        
        assert table.serialization_id == 42
    
    def test_table_auto_serialization_id(self):
        """Test that serialization IDs are auto-generated."""
        table1 = TableBuilder("table1").build()
        table2 = TableBuilder("table2").build()
        
        # IDs should be different
        assert table1.serialization_id != table2.serialization_id
        assert table1.serialization_id > 0
        assert table2.serialization_id > 0
    
    def test_table_with_complex_type(self):
        """Test adding column with complex Type object."""
        array_type = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        table = (TableBuilder("items")
            .add_column("item_id", TypeKind.TYPE_INT64)
            .add_column("tags", array_type)
            .build())
        
        assert len(table.column) == 2
        assert table.column[1].type.type_kind == TypeKind.TYPE_ARRAY
    
    def test_table_with_struct_column(self):
        """Test adding struct type column."""
        address_type = TypeFactory.create_struct_type([
            ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("zipcode", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
        ])
        
        table = (TableBuilder("customers")
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .add_column("address", address_type)
            .build())
        
        assert table.column[1].type.type_kind == TypeKind.TYPE_STRUCT
        assert len(table.column[1].type.struct_type.field) == 3
    
    def test_value_table(self):
        """Test creating a value table."""
        table = (TableBuilder("value_table")
            .add_column("value", TypeKind.TYPE_STRING)
            .as_value_table()
            .build())
        
        assert table.is_value_table is True
    
    def test_method_chaining(self):
        """Test that all builder methods support chaining."""
        table = (TableBuilder("chained")
            .add_column("col1", TypeKind.TYPE_INT64)
            .add_column("col2", TypeKind.TYPE_STRING)
            .with_serialization_id(100)
            .build())
        
        assert table.name == "chained"
        assert table.serialization_id == 100
        assert len(table.column) == 2
    
    def test_table_protomodel_instance(self):
        """Test that built table is a ProtoModel instance."""
        table = (TableBuilder("test")
            .add_column("id", TypeKind.TYPE_INT64)
            .build())
        
        # Should be a SimpleTable ProtoModel
        assert isinstance(table, SimpleTable)
        assert hasattr(table, 'to_proto')  # Has ProtoModel methods
        assert table.name == "test"
        assert len(table.column) == 1


class TestCatalogBuilder:
    """Test CatalogBuilder functionality."""
    
    def test_empty_catalog(self):
        """Test creating an empty catalog."""
        catalog = CatalogBuilder("empty").build()
        
        assert isinstance(catalog, SimpleCatalog)
        assert catalog.name == "empty"
        assert len(catalog.table) == 0
    
    def test_catalog_with_single_table(self):
        """Test catalog with one table."""
        table = (TableBuilder("users")
            .add_column("id", TypeKind.TYPE_INT64)
            .build())
        
        catalog = (CatalogBuilder("my_db")
            .add_table(table)
            .build())
        
        assert catalog.name == "my_db"
        assert len(catalog.table) == 1
        assert catalog.table[0].name == "users"
    
    def test_catalog_with_multiple_tables(self):
        """Test catalog with multiple tables."""
        orders = (TableBuilder("orders")
            .add_column("order_id", TypeKind.TYPE_INT64)
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .build())
        
        products = (TableBuilder("products")
            .add_column("product_id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .build())
        
        customers = (TableBuilder("customers")
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .build())
        
        catalog = (CatalogBuilder("shop")
            .add_table(orders)
            .add_table(products)
            .add_table(customers)
            .build())
        
        assert len(catalog.table) == 3
        assert catalog.table[0].name == "orders"
        assert catalog.table[1].name == "products"
        assert catalog.table[2].name == "customers"
    
    def test_catalog_with_builtin_functions(self):
        """Test adding builtin function options."""
        table = (TableBuilder("test")
            .add_column("id", TypeKind.TYPE_INT64)
            .build())
        
        lang_opts = LanguageOptions()
        builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)
        
        catalog = (CatalogBuilder("db")
            .add_table(table)
            .with_builtin_functions(builtin_opts)
            .build())
        
        assert catalog.builtin_function_options is not None
        assert catalog.builtin_function_options.language_options is not None
    
    def test_catalog_method_chaining(self):
        """Test that all catalog builder methods support chaining."""
        t1 = TableBuilder("t1").add_column("id", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("t2").add_column("id", TypeKind.TYPE_INT64).build()
        
        catalog = (CatalogBuilder("chained")
            .add_table(t1)
            .add_table(t2)
            .build())
        
        assert catalog.name == "chained"
        assert len(catalog.table) == 2
    
    def test_catalog_protomodel_instance(self):
        """Test that built catalog is a ProtoModel instance."""
        table = TableBuilder("test").add_column("id", TypeKind.TYPE_INT64).build()
        catalog = CatalogBuilder("db").add_table(table).build()
        
        # Should be a SimpleCatalog ProtoModel
        assert isinstance(catalog, SimpleCatalog)
        assert hasattr(catalog, 'to_proto')  # Has ProtoModel methods
        assert catalog.name == "db"
        assert len(catalog.table) == 1


class TestBuilderIntegration:
    """Test builders working together."""
    
    def test_complete_catalog_setup(self):
        """Test a complete real-world catalog setup."""
        # Build tables
        customers = (TableBuilder("Customers", serialization_id=1)
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .add_column("email", TypeKind.TYPE_STRING)
            .build())
        
        products = (TableBuilder("Products", serialization_id=2)
            .add_column("product_id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .add_column("price", TypeKind.TYPE_DOUBLE)
            .build())
        
        orders = (TableBuilder("Orders", serialization_id=3)
            .add_column("order_id", TypeKind.TYPE_INT64)
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .add_column("product_id", TypeKind.TYPE_INT64)
            .add_column("quantity", TypeKind.TYPE_INT64)
            .build())
        
        # Build catalog
        catalog = (CatalogBuilder("shop")
            .add_table(customers)
            .add_table(products)
            .add_table(orders)
            .build())
        
        assert len(catalog.table) == 3
        assert catalog.table[0].serialization_id == 1
        assert catalog.table[1].serialization_id == 2
        assert catalog.table[2].serialization_id == 3
    
    def test_catalog_with_complex_types(self):
        """Test catalog with tables containing complex types."""
        # Create complex types
        tags_array = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        metadata_struct = TypeFactory.create_struct_type([
            ("created_at", TypeFactory.create_simple_type(TypeKind.TYPE_TIMESTAMP)),
            ("updated_at", TypeFactory.create_simple_type(TypeKind.TYPE_TIMESTAMP))
        ])
        
        # Build table with complex types
        items = (TableBuilder("items")
            .add_column("id", TypeKind.TYPE_INT64)
            .add_column("tags", tags_array)
            .add_column("metadata", metadata_struct)
            .build())
        
        # Build catalog
        catalog = CatalogBuilder("complex").add_table(items).build()
        
        assert len(catalog.table[0].column) == 3
        assert catalog.table[0].column[1].type.type_kind == TypeKind.TYPE_ARRAY
        assert catalog.table[0].column[2].type.type_kind == TypeKind.TYPE_STRUCT
