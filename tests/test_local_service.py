"""
Test ZetaSqlLocalService class

Tests for the high-level local service wrapper using ProtoModel API.
"""

import pytest
from zetasql.local_service import ZetaSqlLocalService
from zetasql.types import proto_models
from zetasql.types.type_kind import TypeKind
from zetasql.builders import TableBuilder, CatalogBuilder
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2


@pytest.fixture(scope="session")
def service():
    """Create a ZetaSqlLocalService instance (reused across all tests)."""
    return ZetaSqlLocalService()


@pytest.fixture(scope="session")
def analyzer_options():
    """Create analyzer options with all language features enabled."""
    # Create language options with all features
    language_options = proto_models.LanguageOptions()
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    
    # Enable all released language features
    for feature in dir(public_options_pb2):
        if feature.startswith('FEATURE_'):
            if feature == 'FEATURE_SPANNER_LEGACY_DDL':
                continue
            try:
                feature_value = getattr(public_options_pb2, feature)
                if isinstance(feature_value, int) and feature_value > 0:
                    language_options.enabled_language_features.append(feature_value)
            except:
                pass
    
    # Create analyzer options with language options
    opts = proto_models.AnalyzerOptions(language_options=language_options)
    return opts


@pytest.fixture
def simple_catalog(analyzer_options):
    """Create a simple catalog with test table and builtin functions enabled."""
    # Create test table using TableBuilder
    table = (TableBuilder("TestTable")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("value", TypeKind.TYPE_DOUBLE)
        .build())
    
    # Create builtin function options
    builtin_opts = proto_models.ZetaSQLBuiltinFunctionOptions(
        language_options=analyzer_options.language_options
    )
    
    # Create catalog using CatalogBuilder
    catalog = (CatalogBuilder("test")
        .add_table(table)
        .with_builtin_functions(builtin_opts)
        .build())
    
    return catalog


class TestParsing:
    """Test Parse RPC method."""
    
    def test_parse_simple_select(self, service):
        """Test parsing a simple SELECT statement."""
        response = service.parse(sql_statement="SELECT 1 AS one")
        
        assert isinstance(response, proto_models.ParseResponse)
        assert response.parsed_statement is not None
    
    def test_parse_complex_query(self, service):
        """Test parsing a complex query."""
        sql = "SELECT a, b FROM table1 WHERE a > 10 ORDER BY b LIMIT 5"
        response = service.parse(sql_statement=sql)
        
        assert isinstance(response, proto_models.ParseResponse)
        assert response.parsed_statement is not None
    
    def test_parse_join(self, service):
        """Test parsing a query with JOIN."""
        sql = "SELECT t1.id, t2.name FROM table1 t1 JOIN table2 t2 ON t1.id = t2.id"
        response = service.parse(sql_statement=sql)
        
        assert isinstance(response, proto_models.ParseResponse)
        assert response.parsed_statement is not None
    
    def test_parse_with_cte(self, service):
        """Test parsing a query with CTE."""
        sql = """
        WITH cte AS (
            SELECT id, name FROM table1
        )
        SELECT * FROM cte WHERE id > 10
        """
        response = service.parse(sql_statement=sql)
        
        assert isinstance(response, proto_models.ParseResponse)
        assert response.parsed_statement is not None


class TestAnalysis:
    """Test Analyze RPC method."""
    
    def test_analyze_simple_query(self, service, simple_catalog, analyzer_options):
        """Test analyzing a simple query."""
        response = service.analyze(
            sql_statement="SELECT 1 AS one",
            simple_catalog=simple_catalog,
            options=analyzer_options
        )
        
        assert isinstance(response, proto_models.AnalyzeResponse)
        assert response.resolved_statement is not None
    
    def test_analyze_table_query(self, service, simple_catalog, analyzer_options):
        """Test analyzing a query against a table."""
        response = service.analyze(
            sql_statement="SELECT id, name FROM TestTable",
            simple_catalog=simple_catalog,
            options=analyzer_options
        )
        
        assert isinstance(response, proto_models.AnalyzeResponse)
        assert response.resolved_statement is not None
    
    def test_analyze_with_where(self, service, simple_catalog, analyzer_options):
        """Test analyzing a query with WHERE clause."""
        response = service.analyze(
            sql_statement="SELECT id, name FROM TestTable WHERE id > 10",
            simple_catalog=simple_catalog,
            options=analyzer_options
        )
        
        assert isinstance(response, proto_models.AnalyzeResponse)
        assert response.resolved_statement is not None
    
    def test_analyze_with_aggregation(self, service, simple_catalog, analyzer_options):
        """Test analyzing a query with aggregation."""
        response = service.analyze(
            sql_statement="SELECT COUNT(*) as count FROM TestTable",
            simple_catalog=simple_catalog,
            options=analyzer_options
        )
        
        assert isinstance(response, proto_models.AnalyzeResponse)
        assert response.resolved_statement is not None


class TestFormatting:
    """Test FormatSql and LenientFormatSql methods."""
    
    def test_format_simple_query(self, service):
        """Test formatting a simple query."""
        sql = "select   1    as   one"
        response = service.format_sql(sql=sql)
        
        assert isinstance(response, proto_models.FormatSqlResponse)
        assert response.sql is not None
        assert response.sql.strip()  # Should return formatted SQL
        assert "SELECT" in response.sql  # Should normalize keywords
    
    def test_format_complex_query(self, service):
        """Test formatting a complex query."""
        sql = "select a,b,c from table1 where a>10 and b<20 order by c"
        response = service.format_sql(sql=sql)
        
        assert isinstance(response, proto_models.FormatSqlResponse)
        assert response.sql.strip()
        assert "SELECT" in response.sql
        assert "FROM" in response.sql
        assert "WHERE" in response.sql
    
    def test_lenient_format_sql(self, service):
        """Test lenient formatting (more forgiving)."""
        sql = "SELECT 1 AS one"
        response = service.lenient_format_sql(sql=sql)
        
        assert isinstance(response, proto_models.FormatSqlResponse)
        assert response.sql.strip()


class TestExpressions:
    """Test PrepareExpression, EvaluateExpression methods."""
    
    def test_prepare_simple_expression(self, service, analyzer_options, simple_catalog):
        """Test preparing a simple expression."""
        response = service.prepare(
            sql="1 + 2", 
            options=analyzer_options,
            simple_catalog=simple_catalog
        )
        
        assert isinstance(response, proto_models.PrepareResponse)
        assert response.prepared is not None
        assert response.prepared.prepared_expression_id >= 0
        assert response.prepared.output_type is not None


class TestQueries:
    """Test PrepareQuery, EvaluateQuery, UnprepareQuery methods."""
    
    def test_prepare_simple_query(self, service, simple_catalog):
        """Test preparing a simple query."""
        response = service.prepare_query(
            sql="SELECT 1 AS one",
            simple_catalog=simple_catalog
        )
        
        assert isinstance(response, proto_models.PrepareQueryResponse)
        assert response.prepared is not None
        assert response.prepared.prepared_query_id >= 0
        assert len(response.prepared.columns) > 0
    
    def test_prepare_table_query(self, service, simple_catalog):
        """Test preparing a query against a table."""
        response = service.prepare_query(
            sql="SELECT id, name FROM TestTable",
            simple_catalog=simple_catalog
        )
        
        assert isinstance(response, proto_models.PrepareQueryResponse)
        assert response.prepared is not None
        assert response.prepared.prepared_query_id >= 0
        assert len(response.prepared.columns) == 2
        # Access columns using list methods, they return ProtoModel objects
        columns = response.prepared.columns
        assert columns[0].name == "id"
        assert columns[1].name == "name"
    
    def test_unprepare_query(self, service, simple_catalog):
        """Test unpreparing a query."""
        # First prepare
        response = service.prepare_query(
            sql="SELECT 1 AS one",
            simple_catalog=simple_catalog
        )
        prepared_id = response.prepared.prepared_query_id
        
        # Then unprepare (should not raise error)
        service.unprepare_query(prepared_query_id=prepared_id)


class TestCatalog:
    """Test RegisterCatalog and UnregisterCatalog methods."""
    
    def test_register_catalog(self, service, simple_catalog):
        """Test registering a catalog."""
        response = service.register_catalog(simple_catalog=simple_catalog)
        
        assert isinstance(response, proto_models.RegisterResponse)
        assert response.registered_id >= 0
    
    def test_register_and_use_catalog(self, service, simple_catalog):
        """Test registering and using a catalog."""
        # Register
        register_response = service.register_catalog(simple_catalog=simple_catalog)
        catalog_id = register_response.registered_id
        
        # Use registered catalog
        query_response = service.prepare_query(
            sql="SELECT id FROM TestTable",
            registered_catalog_id=catalog_id
        )
        
        assert isinstance(query_response, proto_models.PrepareQueryResponse)
        assert query_response.prepared.prepared_query_id >= 0
    
    def test_unregister_catalog(self, service, simple_catalog):
        """Test unregistering a catalog."""
        # Register
        register_response = service.register_catalog(simple_catalog=simple_catalog)
        catalog_id = register_response.registered_id
        
        # Unregister (should not raise error)
        service.unregister_catalog(registered_id=catalog_id)


class TestTableExtraction:
    """Test ExtractTableNames methods."""
    
    def test_extract_table_names_simple(self, service):
        """Test extracting table names from a simple query."""
        response = service.extract_table_names_from_statement(
            sql_statement="SELECT * FROM table1"
        )
        
        assert isinstance(response, proto_models.ExtractTableNamesFromStatementResponse)
        assert len(response.table_name) == 1
        assert response.table_name[0].table_name_segment[0] == "table1"
    
    def test_extract_table_names_join(self, service):
        """Test extracting table names from a JOIN query."""
        response = service.extract_table_names_from_statement(
            sql_statement="SELECT * FROM table1 JOIN table2 ON table1.id = table2.id"
        )
        
        assert isinstance(response, proto_models.ExtractTableNamesFromStatementResponse)
        assert len(response.table_name) == 2
        table_names = [t.table_name_segment[0] for t in response.table_name]
        assert "table1" in table_names
        assert "table2" in table_names
    
    def test_extract_table_names_multiple_statements(self, service):
        """Test extracting table names from multiple statements."""
        sql = "SELECT * FROM table1; SELECT * FROM table2"
        
        # First statement
        parse_resume = proto_models.ParseResumeLocation(
            input=sql,
            byte_position=0
        )
        
        response = service.extract_table_names_from_next_statement(
            parse_resume_location=parse_resume
        )
        
        assert isinstance(response, proto_models.ExtractTableNamesFromNextStatementResponse)
        assert len(response.table_name) == 1
        assert response.table_name[0].table_name_segment[0] == "table1"
        assert response.resume_byte_position > 0


class TestBuiltinFunctions:
    """Test GetBuiltinFunctions method."""
    
    def test_get_builtin_functions(self, service):
        """Test getting builtin functions."""
        response = service.get_builtin_functions()
        
        assert isinstance(response, proto_models.GetBuiltinFunctionsResponse)
        # Should return some functions
        assert len(response.function) > 0


class TestOptions:
    """Test GetLanguageOptions and GetAnalyzerOptions methods."""
    
    def test_get_language_options(self, service):
        """Test getting language options."""
        response = service.get_language_options()
        
        # Should return language options ProtoModel
        assert isinstance(response, proto_models.LanguageOptions)
    
    def test_get_analyzer_options(self, service):
        """Test getting analyzer options."""
        response = service.get_analyzer_options()
        
        # Should return analyzer options ProtoModel
        assert isinstance(response, proto_models.AnalyzerOptions)
