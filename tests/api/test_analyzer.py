"""Tests for Analyzer helper class."""

import pytest
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.api.analyzer import Analyzer
from zetasql.types import AnalyzerOptions, proto_models
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
        .add_column("status", TypeKind.TYPE_STRING)
        .build())
    
    products_table = (TableBuilder("Products")
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .build())
    
    builtin_opts = ZetaSQLBuiltinFunctionOptions(
        language_options=LanguageOptions.maximum_features(),
    )
    
    catalog = (CatalogBuilder("test_db")
        .add_table(orders_table)
        .add_table(products_table)
        .with_builtin_functions(builtin_opts)
        .build())
    
    return catalog


class TestAnalyzerInstance:
    """Tests for Analyzer instance methods."""
    
    def test_init(self, analyzer_options, catalog):
        """Test Analyzer initialization."""
        analyzer = Analyzer(analyzer_options, catalog)
        
        assert analyzer.options == analyzer_options
        assert analyzer.catalog == catalog
        assert analyzer.service is not None
    
    def test_analyze_statement(self, analyzer_options, catalog):
        """Test instance analyze_statement method."""
        analyzer = Analyzer(analyzer_options, catalog)
        
        sql = "SELECT order_id, amount FROM Orders WHERE amount > 100"
        stmt = analyzer.analyze_statement(sql)
        
        assert stmt is not None
        assert isinstance(stmt, proto_models.ResolvedStatement)
    
    def test_analyze_expression(self, analyzer_options, catalog):
        """Test instance analyze_expression method."""
        analyzer = Analyzer(analyzer_options, catalog)
        
        expression = "1 + 2"
        expr = analyzer.analyze_expression(expression)
        
        assert expr is not None
        assert isinstance(expr, proto_models.ResolvedExpr)
    
    def test_multiple_analyses(self, analyzer_options, catalog):
        """Test analyzer can be reused for multiple analyses."""
        analyzer = Analyzer(analyzer_options, catalog)
        
        stmt1 = analyzer.analyze_statement("SELECT * FROM Orders")
        stmt2 = analyzer.analyze_statement("SELECT * FROM Products")
        expr1 = analyzer.analyze_expression("10 + 20")
        
        assert stmt1 is not None
        assert stmt2 is not None
        assert expr1 is not None


class TestAnalyzerStatic:
    """Tests for Analyzer static methods."""
    
    def test_analyze_statement_static(self, analyzer_options, catalog):
        """Test static analyze_statement method."""
        sql = "SELECT * FROM Orders"
        
        stmt = Analyzer.analyze_statement_static(sql, analyzer_options, catalog)
        
        assert stmt is not None
        assert isinstance(stmt, proto_models.ResolvedStatement)
    
    def test_analyze_expression_static(self, analyzer_options, catalog):
        """Test static analyze_expression method."""
        expression = "100 + 50"
        
        expr = Analyzer.analyze_expression_static(expression, analyzer_options, catalog)
        
        assert expr is not None
        assert isinstance(expr, proto_models.ResolvedExpr)
    
    def test_build_statement(self, analyzer_options, catalog):
        """Test static build_statement method (unanalyze)."""
        original_sql = "SELECT order_id, amount FROM Orders WHERE amount > 100"
        
        # Analyze first
        stmt = Analyzer.analyze_statement_static(original_sql, analyzer_options, catalog)
        
        # Build SQL back
        rebuilt_sql = Analyzer.build_statement(stmt, catalog)
        
        assert rebuilt_sql is not None
        assert isinstance(rebuilt_sql, str)
        assert len(rebuilt_sql) > 0
    
    def test_extract_table_names(self):
        """Test static extract_table_names method."""
        sql = "SELECT * FROM Orders JOIN Products ON Orders.product_id = Products.product_id"
        
        tables = Analyzer.extract_table_names(sql)
        
        assert tables is not None
        assert isinstance(tables, list)
        assert len(tables) == 2
        
        # Extract actual table names from TableName objects
        table_names = ['.'.join(t.table_name_segment) for t in tables]
        assert "Orders" in table_names
        assert "Products" in table_names
    
    def test_extract_table_names_single_table(self):
        """Test extract_table_names with single table."""
        sql = "SELECT * FROM Orders WHERE amount > 100"
        
        tables = Analyzer.extract_table_names(sql)
        
        assert len(tables) == 1
        table_names = ['.'.join(t.table_name_segment) for t in tables]
        assert "Orders" in table_names


class TestAnalyzerCustomService:
    """Test Analyzer with custom service instance."""
    
    def test_custom_service_instance(self, analyzer_options, catalog):
        """Test Analyzer with custom service."""
        service = ZetaSqlLocalService()  # Create new instance
        analyzer = Analyzer(analyzer_options, catalog, service)
        
        assert analyzer.service is service
        
        stmt = analyzer.analyze_statement("SELECT * FROM Orders")
        assert stmt is not None


class TestAnalyzerWithoutCatalog:
    """Test Analyzer without catalog (for expressions or simple queries)."""
    
    def test_analyze_expression_without_catalog(self, service, analyzer_options):
        """Test analyzing simple expression."""
        from zetasql.types import ZetaSQLBuiltinFunctionOptions, LanguageOptions
        from zetasql.api.builders import CatalogBuilder
        
        builtin_opts = ZetaSQLBuiltinFunctionOptions(
            language_options=LanguageOptions.maximum_features(),
        )
        empty_catalog = (CatalogBuilder("empty")
            .with_builtin_functions(builtin_opts)
            .build())
        
        analyzer = Analyzer(analyzer_options, empty_catalog)
        expr = analyzer.analyze_expression("1 + 2")
        
        assert expr is not None
    
    def test_analyze_statement_without_catalog_fails(self, analyzer_options):
        """Test that analyzing statement with table reference fails without catalog."""
        analyzer = Analyzer(analyzer_options, catalog=None)
        
        # This should fail - needs catalog for table resolution
        with pytest.raises(Exception):  # ZetaSQLError or similar
            analyzer.analyze_statement("SELECT * FROM Orders")
