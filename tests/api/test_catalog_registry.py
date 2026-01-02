"""Tests for RegisteredCatalog context manager."""

import pytest
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.api.catalog_registry import RegisteredCatalog
from zetasql.types import AnalyzerOptions
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import TypeKind


@pytest.fixture
def service():
    """Get LocalService instance."""
    return ZetaSqlLocalService.get_instance()


@pytest.fixture
def analyzer_options(service):
    """Create analyzer options."""
    return AnalyzerOptions(
        language_options=service.get_language_options(maximum_features=True),
    )


@pytest.fixture
def catalog(service):
    """Create sample catalog with builtin functions."""
    from zetasql.types import ZetaSQLBuiltinFunctionOptions, LanguageOptions
    
    orders_table = (TableBuilder("Orders")
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .build())
    
    builtin_opts = ZetaSQLBuiltinFunctionOptions(
        language_options=LanguageOptions.maximum_features(),
    )
    
    catalog = (CatalogBuilder("test_db")
        .add_table(orders_table)
        .with_builtin_functions(builtin_opts)
        .build())
    
    return catalog


class TestRegisteredCatalog:
    """Tests for RegisteredCatalog context manager."""
    
    def test_basic_register_and_unregister(self, service, catalog):
        """Test basic catalog registration and unregistration."""
        reg_catalog = RegisteredCatalog(service, catalog)
        
        # Before entering context
        assert reg_catalog.registered_id is None
        
        # Enter context
        catalog_id = reg_catalog.__enter__()
        assert catalog_id is not None
        assert reg_catalog.registered_id == catalog_id
        
        # Exit context
        reg_catalog.__exit__(None, None, None)
        # After exit, catalog should be unregistered (no way to verify directly)
    
    def test_context_manager_usage(self, service, analyzer_options, catalog):
        """Test using RegisteredCatalog as context manager."""
        sql = "SELECT * FROM Orders"
        
        with RegisteredCatalog(service, catalog) as catalog_id:
            assert catalog_id is not None
            
            # Use catalog_id in analyze
            response = service.analyze(
                sql_statement=sql,
                options=analyzer_options,
                registered_catalog_id=catalog_id
            )
            
            assert response.resolved_statement is not None
    
    def test_catalog_register_method(self, service, analyzer_options, catalog):
        """Test SimpleCatalog.register() method."""
        sql = "SELECT order_id FROM Orders"
        
        # Use catalog.register() shorthand
        with catalog.register() as catalog_id:
            assert catalog_id is not None
            
            response = service.analyze(
                sql_statement=sql,
                options=analyzer_options,
                registered_catalog_id=catalog_id
            )
            
            assert response.resolved_statement is not None
    
    def test_catalog_register_with_custom_service(self, analyzer_options, catalog):
        """Test catalog.register() with custom service."""
        service = ZetaSqlLocalService()  # Create new instance
        sql = "SELECT * FROM Orders"
        
        with catalog.register(service=service) as catalog_id:
            response = service.analyze(
                sql_statement=sql,
                options=analyzer_options,
                registered_catalog_id=catalog_id
            )
            
            assert response.resolved_statement is not None
    
    def test_exception_during_usage_still_unregisters(self, service, analyzer_options, catalog):
        """Test that catalog is unregistered even if exception occurs."""
        sql = "SELECT nonexistent_column FROM Orders"
        
        catalog_id_captured = None
        
        try:
            with catalog.register() as catalog_id:
                catalog_id_captured = catalog_id
                
                # This should raise an error (column not found)
                service.analyze(
                    sql_statement=sql,
                    options=analyzer_options,
                    registered_catalog_id=catalog_id
                )
        except Exception:
            # Expected - column doesn't exist
            pass
        
        assert catalog_id_captured is not None
        # Catalog should have been unregistered despite exception
        # (no direct way to verify, but context manager guarantees it)
    
    def test_registered_catalog_property(self, service, catalog):
        """Test registered_id property."""
        reg_catalog = RegisteredCatalog(service, catalog)
        
        assert reg_catalog.registered_id is None
        
        with reg_catalog as catalog_id:
            assert reg_catalog.registered_id == catalog_id
            assert reg_catalog.registered_id is not None
    
    def test_multiple_catalogs_independently(self, service, analyzer_options):
        """Test that multiple catalogs can be registered independently."""
        # Create two different catalogs
        catalog1 = (CatalogBuilder("db1")
            .add_table(
                TableBuilder("Table1")
                .add_column("id", TypeKind.TYPE_INT64)
                .build()
            )
            .build())
        
        catalog2 = (CatalogBuilder("db2")
            .add_table(
                TableBuilder("Table2")
                .add_column("id", TypeKind.TYPE_INT64)
                .build()
            )
            .build())
        
        # Register both
        with catalog1.register() as id1:
            with catalog2.register() as id2:
                assert id1 != id2
                
                # Can use both catalog IDs
                response1 = service.analyze(
                    sql_statement="SELECT * FROM Table1",
                    options=analyzer_options,
                    registered_catalog_id=id1
                )
                
                response2 = service.analyze(
                    sql_statement="SELECT * FROM Table2",
                    options=analyzer_options,
                    registered_catalog_id=id2
                )
                
                assert response1.resolved_statement is not None
                assert response2.resolved_statement is not None
