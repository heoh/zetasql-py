"""
Integration tests for analysis workflows.

Tests complete end-to-end scenarios for SQL analysis.
"""

import pytest
from zetasql.api.analyzer import Analyzer
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import ResolvedQueryStmt, ResolvedExpr, TypeKind, TypeFactory


@pytest.fixture
def ecommerce_catalog(builtin_function_options):
    """Create realistic e-commerce catalog for testing."""
    customers = (TableBuilder("customers")
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("email", TypeKind.TYPE_STRING)
        .add_column("created_at", TypeKind.TYPE_TIMESTAMP)
        .build())
    
    orders = (TableBuilder("orders")
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("order_date", TypeKind.TYPE_DATE)
        .add_column("status", TypeKind.TYPE_STRING)
        .add_column("total_amount", TypeKind.TYPE_DOUBLE)
        .build())
    
    order_items = (TableBuilder("order_items")
        .add_column("order_item_id", TypeKind.TYPE_INT64)
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("quantity", TypeKind.TYPE_INT64)
        .add_column("unit_price", TypeKind.TYPE_DOUBLE)
        .build())
    
    products = (TableBuilder("products")
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("category", TypeKind.TYPE_STRING)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .add_column("in_stock", TypeKind.TYPE_BOOL)
        .build())
    
    return (CatalogBuilder("ecommerce")
        .add_table(customers)
        .add_table(orders)
        .add_table(order_items)
        .add_table(products)
        .with_builtin_functions(builtin_function_options)
        .build())


class TestCompleteAnalysisWorkflow:
    """Test complete workflow: Build catalog → Analyze → Build SQL back."""
    
    def test_simple_query_roundtrip(self, options, ecommerce_catalog):
        """Test analyzing and rebuilding simple query."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        original_sql = "SELECT customer_id, name, email FROM customers WHERE customer_id > 100"
        
        # Step 1: Analyze
        stmt = analyzer.analyze_statement(original_sql)
        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        
        # Verify output columns
        assert len(stmt.output_column_list) == 3
        col_names = [col.name for col in stmt.output_column_list]
        assert "customer_id" in col_names
        assert "name" in col_names
        assert "email" in col_names
        
        # Step 2: Build SQL back
        rebuilt_sql = Analyzer.build_statement(stmt, ecommerce_catalog)
        assert rebuilt_sql is not None
        assert isinstance(rebuilt_sql, str)
        
        # Step 3: Re-analyze rebuilt SQL (should succeed)
        stmt2 = analyzer.analyze_statement(rebuilt_sql)
        assert stmt2 is not None
        assert isinstance(stmt2, ResolvedQueryStmt)
    
    def test_complex_join_analysis(self, options, ecommerce_catalog):
        """Test analyzing complex multi-table join with aggregations."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        sql = """
            SELECT 
                c.customer_id,
                c.name,
                COUNT(o.order_id) as order_count,
                SUM(o.total_amount) as lifetime_value,
                AVG(o.total_amount) as avg_order_value
            FROM customers c
            LEFT JOIN orders o ON c.customer_id = o.customer_id
            WHERE o.status = 'completed' OR o.status IS NULL
            GROUP BY c.customer_id, c.name
            HAVING SUM(o.total_amount) > 1000
            ORDER BY lifetime_value DESC
            LIMIT 10
        """
        
        stmt = analyzer.analyze_statement(sql)
        
        # Verify it's a query statement
        assert isinstance(stmt, ResolvedQueryStmt)
        
        # Verify output columns (5 columns in SELECT)
        assert len(stmt.output_column_list) == 5
        
        # Verify has aggregation (GROUP BY)
        assert hasattr(stmt, 'query')
        
        # Can be rebuilt
        rebuilt_sql = Analyzer.build_statement(stmt, ecommerce_catalog)
        assert len(rebuilt_sql) > 0
    
    def test_cte_analysis(self, options, ecommerce_catalog):
        """Test analyzing query with Common Table Expressions (CTEs)."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        sql = """
            WITH high_value_customers AS (
                SELECT customer_id, SUM(total_amount) as total
                FROM orders
                WHERE status = 'completed'
                GROUP BY customer_id
                HAVING SUM(total_amount) > 5000
            ),
            customer_products AS (
                SELECT 
                    o.customer_id,
                    p.category,
                    COUNT(DISTINCT p.product_id) as product_count
                FROM orders o
                JOIN order_items oi ON o.order_id = oi.order_id
                JOIN products p ON oi.product_id = p.product_id
                GROUP BY o.customer_id, p.category
            )
            SELECT 
                c.name,
                hvc.total as lifetime_value,
                cp.category as favorite_category
            FROM high_value_customers hvc
            JOIN customers c ON hvc.customer_id = c.customer_id
            JOIN customer_products cp ON c.customer_id = cp.customer_id
        """
        
        stmt = analyzer.analyze_statement(sql)
        
        # Should successfully analyze CTE query
        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        
        # Should have 3 output columns
        assert len(stmt.output_column_list) == 3
    
    @pytest.mark.skip(reason="WASM server hangs on scalar subquery in WHERE clause - known limitation")
    def test_subquery_analysis(self, options, ecommerce_catalog):
        """Test analyzing query with correlated subquery.
        
        NOTE: This test hangs indefinitely in the WASM server when analyzing
        scalar subqueries in WHERE clauses. This appears to be a limitation
        of the current ZetaSQL WASM implementation.
        
        Verified behaviors:
        - ✅ Simple queries work
        - ✅ Subqueries in SELECT work
        - ❌ Subqueries in WHERE hang (both correlated and non-correlated)
        """
        analyzer = Analyzer(options, ecommerce_catalog)
        
        sql = """
            SELECT *
            FROM products p
            WHERE p.price > (
                SELECT AVG(oi.unit_price)
                FROM order_items oi
                WHERE oi.product_id = p.product_id
            )
        """
        
        stmt = analyzer.analyze_statement(sql)
        
        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)


class TestComplexTypeAnalysis:
    """Test analyzing queries with complex types (arrays, structs)."""
    
    def test_array_operations(self, options, builtin_function_options):
        """Test analyzing queries with array operations."""
        # Create table with array column
        table = (TableBuilder("events")
            .add_column("event_id", TypeKind.TYPE_INT64)
            .add_column("tags", TypeFactory.create_array_type(
                TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            ))
            .build())
        
        catalog = (CatalogBuilder("db")
            .add_table(table)
            .with_builtin_functions(builtin_function_options)
            .build())
        
        analyzer = Analyzer(options, catalog)
        
        # UNNEST array
        sql = """
            SELECT event_id, tag
            FROM events, UNNEST(tags) as tag
            WHERE tag = 'important'
        """
        
        stmt = analyzer.analyze_statement(sql)
        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        
        # Should have 2 output columns
        assert len(stmt.output_column_list) == 2
    
    def test_struct_operations(self, options, builtin_function_options):
        """Test analyzing queries with struct operations."""
        # Create table with struct column
        address_type = TypeFactory.create_struct_type([
            ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("zipcode", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
        ])
        
        table = (TableBuilder("users")
            .add_column("user_id", TypeKind.TYPE_INT64)
            .add_column("address", address_type)
            .build())
        
        catalog = (CatalogBuilder("db")
            .add_table(table)
            .with_builtin_functions(builtin_function_options)
            .build())
        
        analyzer = Analyzer(options, catalog)
        
        # Access struct fields
        sql = """
            SELECT 
                user_id,
                address.city,
                address.zipcode
            FROM users
            WHERE address.city = 'New York'
        """
        
        stmt = analyzer.analyze_statement(sql)
        assert stmt is not None
        assert isinstance(stmt, ResolvedQueryStmt)
        
        # Should have 3 output columns
        assert len(stmt.output_column_list) == 3


class TestErrorScenarios:
    """Test error handling in analysis workflows."""
    
    def test_syntax_error_handling(self, options, ecommerce_catalog):
        """Test graceful handling of syntax errors."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        # Invalid SQL with syntax error
        invalid_sql = "SELECT * FORM customers"  # typo: FORM instead of FROM
        
        with pytest.raises(Exception) as exc_info:
            analyzer.analyze_statement(invalid_sql)
        
        # Error should be raised (exact message depends on ZetaSQL)
        assert exc_info.value is not None
    
    def test_unknown_table_error(self, options, ecommerce_catalog):
        """Test handling unknown table reference."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        sql = "SELECT * FROM unknown_table_12345"
        
        with pytest.raises(Exception) as exc_info:
            analyzer.analyze_statement(sql)
        
        # Should raise error about unknown table
        assert exc_info.value is not None
    
    def test_unknown_column_error(self, options, ecommerce_catalog):
        """Test handling unknown column reference."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        sql = "SELECT unknown_column_xyz FROM customers"
        
        with pytest.raises(Exception) as exc_info:
            analyzer.analyze_statement(sql)
        
        # Should raise error about unknown column
        assert exc_info.value is not None
    
    def test_type_mismatch_error(self, options, ecommerce_catalog):
        """Test handling type mismatch errors."""
        analyzer = Analyzer(options, ecommerce_catalog)
        
        # Try to compare incompatible types
        sql = "SELECT * FROM customers WHERE customer_id = 'not_a_number'"
        
        with pytest.raises(Exception) as exc_info:
            analyzer.analyze_statement(sql)
        
        # Should raise error (INT64 compared with STRING)
        assert exc_info.value is not None
