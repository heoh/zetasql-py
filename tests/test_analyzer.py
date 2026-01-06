"""
Tests for Analyzer API - mirrors Java AnalyzerTest.java

Tests all static and instance methods of the Analyzer class,
following Java ZetaSQL API patterns.
"""

import pytest

from zetasql.api import Analyzer, CatalogBuilder, TableBuilder
from zetasql.core.exceptions import ZetaSQLError
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.types import (
    AnalyzerOptions,
    LanguageOptions,
    ParseResumeLocation,
    ResolvedFunctionCall,
    ResolvedLiteral,
    ResolvedQueryStmt,
    TypeKind,
    ZetaSQLBuiltinFunctionOptions,
)


@pytest.fixture
def service():
    """Get LocalService singleton."""
    return ZetaSqlLocalService.get_instance()


@pytest.fixture
def options(service):
    """Create analyzer options with maximum features."""
    return AnalyzerOptions(
        language_options=service.get_language_options(maximum_features=True),
    )


@pytest.fixture
def catalog():
    """Create sample catalog - mirrors Java test setup."""
    orders = (
        TableBuilder("Orders")
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .add_column("status", TypeKind.TYPE_STRING)
        .build()
    )

    products = (
        TableBuilder("Products")
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .add_column("category", TypeKind.TYPE_STRING)
        .build()
    )

    customers = (
        TableBuilder("Customers")
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("email", TypeKind.TYPE_STRING)
        .build()
    )

    builtin_opts = ZetaSQLBuiltinFunctionOptions(
        language_options=LanguageOptions.maximum_features(),
    )

    return (
        CatalogBuilder("test_catalog")
        .add_table(orders)
        .add_table(products)
        .add_table(customers)
        .with_builtin_functions(builtin_opts)
        .build()
    )


class TestAnalyzerStatementAnalysis:
    """Test statement analysis - Java: testAnalyzeStatement*"""

    def test_analyze_statement_empty_catalog(self, options):
        """Test analyzing simple SELECT without tables - Java: testAnalyzeStatementEmptyCatalog"""
        empty_catalog = CatalogBuilder("empty").build()

        analyzer = Analyzer(options, empty_catalog)
        stmt = analyzer.analyze_statement("SELECT 1")

        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)

    def test_analyze_statement_with_table(self, options, catalog):
        """Test analyzing statement with table reference."""
        analyzer = Analyzer(options, catalog)

        stmt = analyzer.analyze_statement("SELECT * FROM Orders")

        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        # Verify it's a query statement with output columns
        assert hasattr(stmt, "query")

    def test_analyze_statement_returns_columns(self, options, catalog):
        """Test that analyzed statement has output column information."""
        analyzer = Analyzer(options, catalog)

        stmt = analyzer.analyze_statement("SELECT order_id, amount FROM Orders")

        assert isinstance(stmt, ResolvedQueryStmt)
        # ResolvedQueryStmt should have output_column_list
        assert hasattr(stmt, "output_column_list")
        assert len(stmt.output_column_list) == 2
        # Verify column names
        col_names = [col.name for col in stmt.output_column_list]
        assert "order_id" in col_names
        assert "amount" in col_names

    def test_analyze_statement_with_join(self, options, catalog):
        """Test analyzing multi-table join."""
        analyzer = Analyzer(options, catalog)

        sql = """
            SELECT o.order_id, c.name, o.amount
            FROM Orders o
            JOIN Customers c ON o.customer_id = c.customer_id
            WHERE o.amount > 100
        """

        stmt = analyzer.analyze_statement(sql)

        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        # Should have 3 output columns
        assert len(stmt.output_column_list) == 3

    def test_analyze_statement_static_method(self, options, catalog):
        """Test static analyzeStatement method - Java: Analyzer.analyzeStatement()"""
        sql = "SELECT * FROM Products WHERE price > 50.0"

        stmt = Analyzer.analyze_statement_static(sql, options, catalog)

        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)

    def test_analyze_invalid_sql_raises_error(self, options, catalog):
        """Test that invalid SQL raises appropriate error."""
        analyzer = Analyzer(options, catalog)

        with pytest.raises(ZetaSQLError):
            analyzer.analyze_statement("SELECT * FORM Orders")  # typo: FORM

    def test_analyze_unknown_table_raises_error(self, options, catalog):
        """Test that unknown table raises error."""
        analyzer = Analyzer(options, catalog)

        with pytest.raises(ZetaSQLError):  # ZetaSQLError with "not found" message
            analyzer.analyze_statement("SELECT * FROM UnknownTable")


class TestAnalyzerExpressionAnalysis:
    """Test expression analysis - Java: testAnalyzeExpression*"""

    def test_analyze_expression_literal(self, options, catalog):
        """Test analyzing literal expression."""
        analyzer = Analyzer(options, catalog)

        expr = analyzer.analyze_expression("42")

        assert expr is not None
        assert isinstance(expr, ResolvedLiteral), f"Expected ResolvedLiteral but got {type(expr).__name__}"
        # Verify it has a value
        assert expr.value is not None

    def test_analyze_expression_arithmetic(self, options, catalog):
        """Test analyzing arithmetic expression."""
        analyzer = Analyzer(options, catalog)

        expr = analyzer.analyze_expression("10 + 20 * 3")

        assert expr is not None
        # Arithmetic operations become function calls
        assert isinstance(expr, ResolvedFunctionCall), f"Expected ResolvedFunctionCall but got {type(expr).__name__}"

    def test_analyze_expression_with_function(self, options, catalog):
        """Test analyzing expression with builtin function."""
        analyzer = Analyzer(options, catalog)

        expr = analyzer.analyze_expression("UPPER('hello')")

        assert expr is not None
        assert isinstance(expr, ResolvedFunctionCall), f"Expected ResolvedFunctionCall but got {type(expr).__name__}"
        assert expr.function is not None

    def test_analyze_expression_static_method(self, options, catalog):
        """Test static analyzeExpression method."""
        expr = Analyzer.analyze_expression_static("1 + 1", options, catalog)

        assert expr is not None


class TestAnalyzerBuildSQL:
    """Test building SQL from resolved AST - Java: testBuildStatement/Expression"""

    def test_build_statement(self, options, catalog):
        """Test buildStatement - resolved AST back to SQL."""
        original_sql = "SELECT order_id, amount FROM Orders WHERE amount > 100"

        # Analyze
        stmt = Analyzer.analyze_statement_static(original_sql, options, catalog)

        # Build back
        rebuilt_sql = Analyzer.build_statement(stmt, catalog)

        assert rebuilt_sql is not None
        assert isinstance(rebuilt_sql, str)
        assert len(rebuilt_sql) > 0
        # Should contain key elements (exact format may differ)
        assert "SELECT" in rebuilt_sql.upper()
        assert "Orders" in rebuilt_sql or "orders" in rebuilt_sql

    def test_build_expression(self, options, catalog):
        """Test buildExpression - resolved expr back to SQL."""
        original_expr = "10 + 20"

        # Analyze
        expr = Analyzer.analyze_expression_static(original_expr, options, catalog)

        # Build back
        rebuilt_expr = Analyzer.build_expression(expr, catalog)

        assert rebuilt_expr is not None
        assert isinstance(rebuilt_expr, str)

    def test_roundtrip_complex_query(self, options, catalog):
        """Test analyze -> build roundtrip preserves semantics."""
        original_sql = """
            SELECT 
                o.order_id,
                SUM(o.amount) as total_amount,
                COUNT(*) as order_count
            FROM Orders o
            WHERE o.status = 'completed'
            GROUP BY o.order_id
            HAVING SUM(o.amount) > 1000
        """

        stmt = Analyzer.analyze_statement_static(original_sql, options, catalog)
        rebuilt_sql = Analyzer.build_statement(stmt, catalog)

        # Re-analyze rebuilt SQL - should succeed without errors
        stmt2 = Analyzer.analyze_statement_static(rebuilt_sql, options, catalog)
        assert stmt2 is not None
        assert isinstance(stmt2, ResolvedQueryStmt)


class TestAnalyzerExtractTableNames:
    """Test table name extraction - Java: testExtractTableNames*"""

    def test_extract_table_names_single_table(self):
        """Test extracting table names from simple SELECT."""
        sql = "SELECT * FROM Orders"

        tables = Analyzer.extract_table_names(sql)

        assert tables is not None
        assert len(tables) == 1
        # Verify table name structure
        assert len(tables[0].table_name_segment) >= 1
        assert tables[0].table_name_segment[-1] == "Orders"

    def test_extract_table_names_multiple_tables(self):
        """Test extracting from JOIN query."""
        sql = """
            SELECT * 
            FROM Orders 
            JOIN Products ON Orders.product_id = Products.product_id
            JOIN Customers ON Orders.customer_id = Customers.customer_id
        """

        tables = Analyzer.extract_table_names(sql)

        assert len(tables) == 3
        # Extract table names from path segments
        table_names = [t.table_name_segment[-1] for t in tables]
        assert "Orders" in table_names
        assert "Products" in table_names
        assert "Customers" in table_names

    def test_extract_table_names_qualified_paths(self):
        """Test extracting qualified table names (db.schema.table)."""
        sql = "SELECT * FROM mydb.myschema.Orders"

        tables = Analyzer.extract_table_names(sql)

        assert len(tables) == 1
        # Should preserve full path
        segments = list(tables[0].table_name_segment)
        assert len(segments) == 3
        assert segments == ["mydb", "myschema", "Orders"]

    def test_extract_table_names_with_subquery(self):
        """Test extracting from query with subquery."""
        sql = """
            SELECT * FROM (
                SELECT * FROM Orders WHERE amount > 100
            ) AS filtered_orders
            JOIN Products ON filtered_orders.product_id = Products.product_id
        """

        tables = Analyzer.extract_table_names(sql)

        # Should find Orders and Products
        assert len(tables) >= 2
        table_names = [t.table_name_segment[-1] for t in tables]
        assert "Orders" in table_names
        assert "Products" in table_names

    def test_extract_table_names_from_script(self):
        """Test extractTableNamesFromScript - Java: extractTableNamesFromScript()"""
        script = """
            SELECT * FROM Orders;
            SELECT * FROM Products;
            SELECT * FROM Customers;
        """

        tables = Analyzer.extract_table_names_from_script(script)

        # Should find all tables across all statements
        assert len(tables) >= 3
        table_names = [t.table_name_segment[-1] for t in tables]
        assert "Orders" in table_names
        assert "Products" in table_names
        assert "Customers" in table_names


class TestAnalyzerMultiStatement:
    """Test multi-statement analysis - Java: testAnalyzeNextStatement*"""

    def test_analyze_next_statement(self, options, catalog):
        """Test parsing multiple statements with ParseResumeLocation."""
        script = "SELECT * FROM Orders; SELECT * FROM Products; SELECT * FROM Customers;"

        location = ParseResumeLocation(input=script, byte_position=0)

        # Initial position should be 0
        assert location.byte_position == 0

        # First statement
        stmt1 = Analyzer.analyze_next_statement_static(location, options, catalog)
        assert stmt1 is not None
        assert isinstance(stmt1, ResolvedQueryStmt)

    def test_analyze_next_statement_instance_method(self, options, catalog):
        """Test instance method for analyzeNextStatement."""
        script = "SELECT 1; SELECT 2;"

        analyzer = Analyzer(options, catalog)
        location = ParseResumeLocation(input=script, byte_position=0)

        stmt1 = analyzer.analyze_next_statement(location)
        stmt2 = analyzer.analyze_next_statement(location)

        assert stmt1 is not None
        assert stmt2 is not None
        # Both should be valid query statements
        assert isinstance(stmt1, ResolvedQueryStmt)
        assert isinstance(stmt2, ResolvedQueryStmt)

    def test_parse_resume_location_byte_position(self, options, catalog):
        """Test that byte position advances correctly - mirrors Java test."""
        script = "SELECT * FROM Orders; SELECT * FROM Products;"
        location = ParseResumeLocation(input=script, byte_position=0)

        initial_pos = location.byte_position
        assert initial_pos == 0

        Analyzer.analyze_next_statement_static(location, options, catalog)
        pos_after_first = location.byte_position
        assert pos_after_first > initial_pos
        # Should be around the position of first semicolon + 1
        assert pos_after_first >= len("SELECT * FROM Orders;")

        Analyzer.analyze_next_statement_static(location, options, catalog)
        pos_after_second = location.byte_position
        assert pos_after_second > pos_after_first
        # Should be at or near end of script
        assert pos_after_second >= len(script) - 5  # Allow for trailing whitespace


class TestAnalyzerWithRegisteredCatalog:
    """Test analyzer with registered catalogs"""

    def test_analyze_with_registered_catalog(self, options, catalog, service):
        """Test analyzing with pre-registered catalog."""
        # Register catalog
        response = service.register_catalog(simple_catalog=catalog)
        registered_id = response.registered_id

        try:
            assert registered_id >= 0
            assert isinstance(registered_id, int)

            # Analyze using registered catalog
            analyzer = Analyzer(options, catalog)
            stmt = analyzer.analyze_statement("SELECT * FROM Orders")

            assert stmt is not None
            assert isinstance(stmt, ResolvedQueryStmt)
        finally:
            # Cleanup
            service.unregister_catalog(registered_id=registered_id)

    def test_analyze_next_statement_with_registered_catalog(self, options, catalog, service):
        """Test multi-statement with registered catalog - mirrors Java test."""
        script = "SELECT * FROM Orders; SELECT * FROM Products;"

        response = service.register_catalog(simple_catalog=catalog)
        registered_id = response.registered_id

        try:
            location = ParseResumeLocation(input=script, byte_position=0)

            stmt1 = Analyzer.analyze_next_statement_static(location, options, catalog)
            stmt2 = Analyzer.analyze_next_statement_static(location, options, catalog)

            assert stmt1 is not None
            assert stmt2 is not None
        finally:
            service.unregister_catalog(registered_id=registered_id)


class TestAnalyzerEdgeCases:
    """Test edge cases and error scenarios."""

    def test_empty_sql_raises_error(self, options, catalog):
        """Test that empty SQL raises error."""
        analyzer = Analyzer(options, catalog)

        with pytest.raises(ZetaSQLError):
            analyzer.analyze_statement("")

    def test_analyze_with_null_catalog(self, options):
        """Test analyzer with None catalog."""
        analyzer = Analyzer(options, catalog=None)

        # Simple literal expressions work without catalog
        expr = analyzer.analyze_expression("42")
        assert expr is not None
        assert isinstance(expr, ResolvedLiteral)

        # Statement with table reference should fail without catalog
        with pytest.raises(ZetaSQLError):
            analyzer.analyze_statement("SELECT * FROM Orders")

    def test_concurrent_analysis(self, options, catalog):
        """Test that analyzer can handle multiple sequential operations."""
        analyzer = Analyzer(options, catalog)

        # Multiple analyses in sequence should work
        for i in range(5):
            stmt = analyzer.analyze_statement(f"SELECT {i}")
            assert stmt is not None

    def test_reuse_analyzer_instance(self, options, catalog):
        """Test reusing analyzer instance for different queries."""
        analyzer = Analyzer(options, catalog)

        # First query
        stmt1 = analyzer.analyze_statement("SELECT * FROM Orders")
        assert stmt1 is not None

        # Second query with different table
        stmt2 = analyzer.analyze_statement("SELECT * FROM Products")
        assert stmt2 is not None

        # Expression
        expr = analyzer.analyze_expression("42 + 8")
        assert expr is not None

        # Third query
        stmt3 = analyzer.analyze_statement("SELECT * FROM Customers")
        assert stmt3 is not None
