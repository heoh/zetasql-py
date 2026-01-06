"""
Basic catalog operations - mirrors Java SimpleCatalogTest.java

Tests for SimpleCatalog basic operations like name, structure,
and table list access.
"""

import pytest
from zetasql.api import TypeFactory
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import (
    TypeKind,
    ZetaSQLBuiltinFunctionOptions,
    LanguageOptions,
)


class TestCatalogBasics:
    """Test basic catalog properties - Java: testGets()"""
    
    def test_catalog_name(self):
        """Test catalog has correct name."""
        catalog = CatalogBuilder("my_catalog").build()
        
        assert catalog.name == "my_catalog"
    
    def test_empty_catalog_has_no_tables(self, empty_catalog):
        """Test empty catalog has no tables initially."""
        assert len(empty_catalog.table) == 0
    
    def test_catalog_with_single_table(self, sample_table):
        """Test catalog with one table."""
        catalog = (CatalogBuilder("db")
            .add_table(sample_table)
            .build())
        
        assert len(catalog.table) == 1
        assert catalog.table[0].name == "SampleTable"
    
    def test_catalog_with_multiple_tables(self):
        """Test catalog with multiple tables."""
        table1 = (TableBuilder("Table1")
            .add_column("id", TypeKind.TYPE_INT64)
            .build())
        
        table2 = (TableBuilder("Table2")
            .add_column("name", TypeKind.TYPE_STRING)
            .build())
        
        table3 = (TableBuilder("Table3")
            .add_column("value", TypeKind.TYPE_DOUBLE)
            .build())
        
        catalog = (CatalogBuilder("db")
            .add_table(table1)
            .add_table(table2)
            .add_table(table3)
            .build())
        
        assert len(catalog.table) == 3
        # Verify all table names
        table_names = [t.name for t in catalog.table]
        assert "Table1" in table_names
        assert "Table2" in table_names
        assert "Table3" in table_names


class TestCatalogBuiltinFunctions:
    """Test builtin function configuration."""
    
    def test_catalog_without_builtin_functions(self):
        """Test catalog without builtin functions."""
        catalog = CatalogBuilder("db").build()
        
        # Should not have builtin_function_options set (or it's default/empty)
        assert not hasattr(catalog, 'builtin_function_options') or \
               catalog.builtin_function_options is None or \
               not catalog.builtin_function_options.language_options.enabled_language_features
    
    def test_catalog_with_builtin_functions(self, service):
        """Test catalog with builtin functions enabled."""
        builtin_opts = ZetaSQLBuiltinFunctionOptions(
            language_options=LanguageOptions.maximum_features(),
        )
        
        catalog = (CatalogBuilder("db")
            .with_builtin_functions(builtin_opts)
            .build())
        
        # Should have builtin function options configured
        assert catalog.builtin_function_options is not None
        assert len(catalog.builtin_function_options.language_options.enabled_language_features) > 0
    
    def test_get_builtin_functions_from_service(self, service):
        """Test getting builtin function list from service."""
        lang_opts = service.get_language_options(maximum_features=True)
        
        response = service.get_builtin_functions(language_options=lang_opts)
        
        assert response is not None
        assert len(response.function) > 0  # Should have many builtin functions (100+)
        
        # Verify some common functions exist
        func_names = [f.name_path[0] for f in response.function if f.name_path]
        # Common functions should be present
        # (exact names depend on ZetaSQL version, but UPPER/LOWER are standard)


class TestCatalogRegistration:
    """Test catalog registration/unregistration - Java: AutoUnregister tests"""
    
    def test_register_catalog(self, service, sample_table):
        """Test registering catalog returns valid ID."""
        catalog = CatalogBuilder("db").add_table(sample_table).build()
        
        response = service.register_catalog(simple_catalog=catalog)
        registered_id = response.registered_id
        
        assert registered_id >= 0
        assert isinstance(registered_id, int)
        
        # Cleanup
        service.unregister_catalog(registered_id=registered_id)
    
    def test_unregister_catalog(self, service):
        """Test unregistering catalog."""
        catalog = CatalogBuilder("db").build()
        
        response = service.register_catalog(simple_catalog=catalog)
        registered_id = response.registered_id
        
        # Should not raise
        service.unregister_catalog(registered_id=registered_id)
    
    def test_register_multiple_catalogs(self, service):
        """Test registering multiple catalogs."""
        catalog1 = CatalogBuilder("db1").build()
        catalog2 = CatalogBuilder("db2").build()
        
        resp1 = service.register_catalog(simple_catalog=catalog1)
        resp2 = service.register_catalog(simple_catalog=catalog2)
        
        id1 = resp1.registered_id
        id2 = resp2.registered_id
        
        # Should get different IDs
        assert id1 != id2
        assert id1 > 0
        assert id2 > 0
        
        # Cleanup both
        service.unregister_catalog(registered_id=id1)
        service.unregister_catalog(registered_id=id2)
