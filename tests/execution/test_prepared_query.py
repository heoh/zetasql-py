"""Tests for PreparedQuery wrapper class."""

import pytest
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.api.prepared_query import PreparedQuery, PreparedQueryBuilder
from zetasql.core.exceptions import ZetaSQLError, IllegalStateError, InvalidArgumentError
from zetasql.types import AnalyzerOptions, LanguageOptions
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import TypeKind
from zetasql.extensions.table_content import create_table_content


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


@pytest.fixture
def table_content():
    """Create sample table content."""
    data = [
        [1, 101, 99.99],
        [2, 102, 149.99],
        [3, 101, 199.99],
    ]
    return {"Orders": create_table_content(data)}


class TestPreparedQuery:
    """Tests for PreparedQuery class."""
    
    def test_basic_prepare_and_execute(self, service, analyzer_options, catalog, table_content):
        """Test basic query preparation and execution."""
        sql = "SELECT order_id, amount FROM Orders WHERE amount > 100"
        
        # Prepare query
        response = service.prepare_query(
            sql=sql,
            options=analyzer_options,
            simple_catalog=catalog,
            table_content=table_content
        )
        
        query = PreparedQuery(
            service=service,
            prepared_id=response.prepared.prepared_query_id,
            columns=response.prepared.columns
        )
        
        try:
            # Execute query
            result = query.execute()
            assert result is not None
            assert result.content is not None
            
            # Verify columns
            assert len(query.columns) == 2
        finally:
            query.close()
    
    def test_context_manager_cleanup(self, service, analyzer_options, catalog, table_content):
        """Test that context manager properly cleans up resources."""
        sql = "SELECT * FROM Orders"
        
        response = service.prepare_query(
            sql=sql,
            options=analyzer_options,
            simple_catalog=catalog,
            table_content=table_content
        )
        
        prepared_id = response.prepared.prepared_query_id
        
        with PreparedQuery(service, prepared_id, response.prepared.columns) as query:
            result = query.execute()
            assert result is not None
            assert query._closed is False
        
        # After exiting context, query should be closed
        assert query._closed is True
    
    def test_execute_after_close_raises_error(self, service, analyzer_options, catalog, table_content):
        """Test that executing closed query raises error."""
        sql = "SELECT * FROM Orders"
        
        response = service.prepare_query(
            sql=sql,
            options=analyzer_options,
            simple_catalog=catalog,
            table_content=table_content
        )
        
        query = PreparedQuery(service, response.prepared.prepared_query_id, response.prepared.columns)
        query.close()
        
        with pytest.raises(IllegalStateError, match="already closed"):
            query.execute()
    
    def test_multiple_close_is_safe(self, service, analyzer_options, catalog, table_content):
        """Test that calling close() multiple times is safe."""
        sql = "SELECT * FROM Orders"
        
        response = service.prepare_query(
            sql=sql,
            options=analyzer_options,
            simple_catalog=catalog,
            table_content=table_content
        )
        
        query = PreparedQuery(service, response.prepared.prepared_query_id, response.prepared.columns)
        
        # Close multiple times should not raise error
        query.close()
        query.close()
        query.close()
        
        assert query._closed is True
    
    def test_properties(self, service, analyzer_options, catalog, table_content):
        """Test PreparedQuery properties."""
        sql = "SELECT order_id, customer_id FROM Orders"
        
        response = service.prepare_query(
            sql=sql,
            options=analyzer_options,
            simple_catalog=catalog,
            table_content=table_content
        )
        
        query = PreparedQuery(service, response.prepared.prepared_query_id, response.prepared.columns)
        
        try:
            # Test properties
            assert query.prepared_query_id == response.prepared.prepared_query_id
            assert query.columns == response.prepared.columns
            assert len(query.columns) == 2
        finally:
            query.close()


class TestPreparedQueryBuilder:
    """Tests for PreparedQueryBuilder class."""
    
    def test_builder_basic_usage(self, analyzer_options, catalog, table_content):
        """Test basic builder usage."""
        sql = "SELECT * FROM Orders"
        
        with PreparedQuery.builder() \
                .set_sql(sql) \
                .set_analyzer_options(analyzer_options) \
                .set_catalog(catalog) \
                .set_table_content(table_content) \
                .prepare() as query:
            
            result = query.execute()
            assert result is not None
    
    def test_builder_missing_sql_raises_error(self, analyzer_options, catalog):
        """Test that builder validates required SQL parameter."""
        with pytest.raises(InvalidArgumentError, match="SQL must be set"):
            PreparedQueryBuilder() \
                .set_analyzer_options(analyzer_options) \
                .set_catalog(catalog) \
                .prepare()
    
    def test_builder_catalog_conflict_raises_error(self, analyzer_options, catalog):
        """Test that builder detects catalog parameter conflicts."""
        with pytest.raises(InvalidArgumentError, match="Cannot provide both"):
            PreparedQueryBuilder() \
                .set_sql("SELECT 1") \
                .set_analyzer_options(analyzer_options) \
                .set_catalog(catalog) \
                .set_registered_catalog_id(123) \
                .prepare()
    
    def test_builder_table_content_with_registered_catalog_raises_error(
        self, analyzer_options, table_content
    ):
        """Test that builder detects table_content with registered catalog."""
        with pytest.raises(InvalidArgumentError, match="Cannot use table_content with registered catalog"):
            PreparedQueryBuilder() \
                .set_sql("SELECT 1") \
                .set_analyzer_options(analyzer_options) \
                .set_registered_catalog_id(123) \
                .set_table_content(table_content) \
                .prepare()
    
    def test_builder_method_chaining(self, analyzer_options, catalog, table_content):
        """Test that all builder methods support chaining."""
        builder = PreparedQueryBuilder()
        
        # All methods should return self for chaining
        result = builder.set_sql("SELECT 1")
        assert result is builder
        
        result = builder.set_analyzer_options(analyzer_options)
        assert result is builder
        
        result = builder.set_catalog(catalog)
        assert result is builder
        
        result = builder.set_table_content(table_content)
        assert result is builder
    
    def test_builder_static_factory(self):
        """Test static builder() factory method."""
        builder = PreparedQuery.builder()
        assert isinstance(builder, PreparedQueryBuilder)
    
    def test_builder_with_custom_service(self, analyzer_options, catalog, table_content):
        """Test builder with custom service instance."""
        service = ZetaSqlLocalService()  # Create new instance
        
        sql = "SELECT * FROM Orders"
        
        with PreparedQuery.builder() \
                .set_sql(sql) \
                .set_analyzer_options(analyzer_options) \
                .set_catalog(catalog) \
                .set_table_content(table_content) \
                .set_service(service) \
                .prepare() as query:
            
            result = query.execute()
            assert result is not None
