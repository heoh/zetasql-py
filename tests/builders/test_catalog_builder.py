"""
CatalogBuilder tests - fluent API for building SimpleCatalog objects
"""

import pytest
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import SimpleCatalog, ZetaSQLBuiltinFunctionOptions, LanguageOptions, TypeKind, TypeFactory


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
            .add_column("name", TypeKind.TYPE_STRING)
            .build())
        
        catalog = (CatalogBuilder("my_db")
            .add_table(table)
            .build())
        
        assert catalog.name == "my_db"
        assert len(catalog.table) == 1
        assert catalog.table[0].name == "users"
        assert len(catalog.table[0].column) == 2
    
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
        # Verify order is preserved
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
    
    def test_catalog_with_maximum_features(self):
        """Test catalog with maximum language features enabled."""
        builtin_opts = ZetaSQLBuiltinFunctionOptions(
            language_options=LanguageOptions.maximum_features()
        )
        
        catalog = (CatalogBuilder("db")
            .with_builtin_functions(builtin_opts)
            .build())
        
        assert catalog.builtin_function_options is not None
        # Should have many enabled features
        enabled_features = catalog.builtin_function_options.language_options.enabled_language_features
        assert len(enabled_features) > 0
    
    def test_catalog_method_chaining(self):
        """Test that all catalog builder methods support chaining."""
        t1 = TableBuilder("t1").add_column("id", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("t2").add_column("id", TypeKind.TYPE_INT64).build()
        t3 = TableBuilder("t3").add_column("id", TypeKind.TYPE_INT64).build()
        
        builtin_opts = ZetaSQLBuiltinFunctionOptions(
            language_options=LanguageOptions()
        )
        
        catalog = (CatalogBuilder("chained")
            .add_table(t1)
            .add_table(t2)
            .add_table(t3)
            .with_builtin_functions(builtin_opts)
            .build())
        
        assert catalog.name == "chained"
        assert len(catalog.table) == 3
        assert catalog.builtin_function_options is not None
    
    def test_catalog_protomodel_instance(self):
        """Test that built catalog is a ProtoModel instance."""
        table = TableBuilder("test").add_column("id", TypeKind.TYPE_INT64).build()
        catalog = CatalogBuilder("db").add_table(table).build()
        
        # Should be a SimpleCatalog ProtoModel
        assert isinstance(catalog, SimpleCatalog)
        assert hasattr(catalog, 'to_proto')  # Has ProtoModel methods
        assert hasattr(catalog, 'from_proto')
        assert catalog.name == "db"
        assert len(catalog.table) == 1


class TestCatalogBuilderIntegration:
    """Test CatalogBuilder with complex scenarios."""
    
    def test_complete_catalog_setup(self):
        """Test a complete real-world catalog setup."""
        # Build tables with serialization IDs
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
        # Verify serialization IDs are preserved
        assert catalog.table[0].serialization_id == 1
        assert catalog.table[1].serialization_id == 2
        assert catalog.table[2].serialization_id == 3
        # Verify column counts
        assert len(catalog.table[0].column) == 3
        assert len(catalog.table[1].column) == 3
        assert len(catalog.table[2].column) == 4
    
    def test_catalog_with_complex_types(self):
        """Test catalog with tables containing complex types."""
        # Create complex types
        tags_array = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        metadata_struct = TypeFactory.create_struct_type([
            ("created_at", TypeFactory.create_simple_type(TypeKind.TYPE_TIMESTAMP)),
            ("updated_at", TypeFactory.create_simple_type(TypeKind.TYPE_TIMESTAMP)),
            ("version", TypeFactory.create_simple_type(TypeKind.TYPE_INT64))
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
        # Verify complex type columns
        assert catalog.table[0].column[1].type.type_kind == TypeKind.TYPE_ARRAY
        assert catalog.table[0].column[2].type.type_kind == TypeKind.TYPE_STRUCT
        # Verify struct has 3 fields
        assert len(catalog.table[0].column[2].type.struct_type.field) == 3
    
    def test_multiple_catalogs_independent(self):
        """Test that multiple catalog builder instances are independent."""
        t1 = TableBuilder("table1").add_column("a", TypeKind.TYPE_INT64).build()
        t2 = TableBuilder("table2").add_column("b", TypeKind.TYPE_STRING).build()
        
        catalog1 = CatalogBuilder("catalog1").add_table(t1).build()
        catalog2 = CatalogBuilder("catalog2").add_table(t2).build()
        
        # Should be different catalogs
        assert catalog1.name != catalog2.name
        assert len(catalog1.table) == 1
        assert len(catalog2.table) == 1
        assert catalog1.table[0].name != catalog2.table[0].name
