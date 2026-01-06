"""
Tests for script analysis - multi-statement SQL scripts.

Mirrors Java ScriptAnalyzer functionality for analyzing SQL scripts
with multiple statements.
"""

import pytest

from zetasql.api import Analyzer, CatalogBuilder, StatementType, TableBuilder, get_statement_type
from zetasql.types import (
    ParseResumeLocation,
    ResolvedNodeKind,
    ResolvedQueryStmt,
    TypeKind,
)


@pytest.fixture
def script_catalog(builtin_function_options):
    """Create catalog for script testing."""
    orders = (
        TableBuilder("Orders")
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .build()
    )

    products = (
        TableBuilder("Products")
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .build()
    )

    return (
        CatalogBuilder("script_db")
        .add_table(orders)
        .add_table(products)
        .with_builtin_functions(builtin_function_options)
        .build()
    )


class TestScriptAnalysis:
    """Test analyzing multi-statement SQL scripts - Java: ScriptAnalyzer tests"""

    def test_analyze_script_basic(self, options, script_catalog):
        """Test analyzing script with multiple statements - Java: analyzeScript()"""
        script = """
            SELECT * FROM Orders WHERE amount > 100;
            SELECT * FROM Products WHERE price < 50;
            SELECT COUNT(*) FROM Orders;
        """

        location = ParseResumeLocation(input=script, byte_position=0)
        statements = []

        while location.byte_position < len(script):
            try:
                stmt = Analyzer.analyze_next_statement_static(location, options, script_catalog)
                if stmt is None:
                    break
                statements.append(stmt)
            except Exception:
                break

        assert len(statements) == 3
        assert all(isinstance(s, ResolvedQueryStmt) for s in statements)

    def test_script_iterator(self, options, script_catalog):
        """Test iterating through script statements - Java: ScriptIterator

        Expected API:
            for stmt in Analyzer.iterate_script(script, options, catalog):
                # Process each statement
        """
        script = """
            SELECT 1;
            SELECT 2;
            SELECT 3;
        """

        statements = list(Analyzer.iterate_script(script, options, script_catalog))

        assert len(statements) == 3
        assert all(isinstance(s, ResolvedQueryStmt) for s in statements)

    def test_script_with_errors(self, options, script_catalog):
        """Test handling errors in multi-statement scripts - Java: error handling

        Expected: Should identify which statement failed and at what position
        """
        script = """
            SELECT * FROM Orders;
            SELECT * FROM NonExistentTable;
            SELECT * FROM Products;
        """

        location = ParseResumeLocation(input=script, byte_position=0)

        # First statement should succeed
        stmt1 = Analyzer.analyze_next_statement_static(location, options, script_catalog)
        assert stmt1 is not None

        # Second statement should raise error
        with pytest.raises(Exception) as exc_info:
            Analyzer.analyze_next_statement_static(location, options, script_catalog)

        # Error should contain position information
        assert "NonExistentTable" in str(exc_info.value)

    def test_extract_script_metadata(self, options, script_catalog):
        """Test extracting metadata from entire script - Java: extractTableNamesFromScript()

        Expected API:
            metadata = Analyzer.extract_script_metadata(script)
            # metadata.tables, metadata.functions, metadata.statement_count
        """
        script = """
            SELECT * FROM Orders WHERE amount > 100;
            SELECT p.name, o.amount 
            FROM Products p 
            JOIN Orders o ON p.product_id = o.customer_id;
        """

        metadata = Analyzer.extract_script_metadata(script)

        assert "Orders" in metadata.tables
        assert "Products" in metadata.tables
        assert metadata.statement_count == 2

    def test_detect_statement_types(self, options, script_catalog):
        """Test detecting statement types in script - Java: StatementType

        Expected: Distinguish between SELECT, INSERT, UPDATE, DELETE, DDL, etc.
        """
        # Enable DDL/DML statement support
        options.language_options.supported_statement_kinds.extend(
            [
                ResolvedNodeKind.RESOLVED_CREATE_TABLE_STMT,
                ResolvedNodeKind.RESOLVED_INSERT_STMT,
            ]
        )

        script = """
            SELECT * FROM Orders;
            CREATE TABLE temp (id INT64);
            INSERT INTO Orders (order_id, customer_id, amount) VALUES (1, 2, 100.0);
        """

        location = ParseResumeLocation(input=script, byte_position=0)
        types = []

        while location.byte_position < len(script):
            stmt = Analyzer.analyze_next_statement_static(location, options, script_catalog)
            if stmt is None:
                break
            # Use get_statement_type helper function
            types.append(get_statement_type(stmt))

        # Should have all three statement types
        assert len(types) == 3
        assert StatementType.QUERY in types  # SELECT
        assert StatementType.DDL in types  # CREATE TABLE
        assert StatementType.DML in types  # INSERT


class TestScriptValidation:
    """Test script validation without full analysis - Java: validation APIs"""

    def test_validate_script_syntax(self):
        """Test syntax validation without catalog - Java: validateScript()

        Expected API:
            result = Analyzer.validate_script_syntax(script)
            # Returns: is_valid, errors[]
        """
        valid_script = """
            SELECT * FROM table1;
            SELECT * FROM table2;
        """

        result = Analyzer.validate_script_syntax(valid_script)
        assert result.is_valid is True
        assert len(result.errors) == 0

        invalid_script = """
            SELECT * FORM table1;  -- typo
            SELECT FROM;            -- incomplete
        """

        result = Analyzer.validate_script_syntax(invalid_script)
        assert result.is_valid is False
        assert len(result.errors) > 0

    def test_find_statement_boundaries(self):
        """Test finding statement boundaries in script - Java: statement parsing

        Expected API:
            boundaries = Analyzer.find_statement_boundaries(script)
            # Returns: [(start_pos, end_pos), ...]
        """
        script = """
            SELECT 1;
            SELECT 2;
            SELECT 3;
        """

        boundaries = Analyzer.find_statement_boundaries(script)

        assert len(boundaries) == 3
        for start, end in boundaries:
            assert 0 <= start < end <= len(script)


class TestScriptFormatting:
    """Test formatting multi-statement scripts - Java: formatting APIs"""

    def test_format_script(self):
        """Test formatting entire script - Java: formatScript()

        Expected API:
            formatted = Analyzer.format_script(script)
        """
        ugly_script = "SELECT * FROM Orders;SELECT * FROM Products;"

        formatted = Analyzer.format_script(ugly_script)

        assert "SELECT" in formatted
        assert "\n" in formatted
        assert formatted != ugly_script

    def test_lenient_format_script(self):
        """Test lenient formatting (partial errors OK) - Java: lenientFormatScript()

        Expected API:
            formatted = Analyzer.lenient_format_script(script)
        """
        script_with_error = """
            SELECT * FROM Orders;
            SELECT * FORM Products;  -- typo, should still format rest
        """

        formatted = Analyzer.lenient_format_script(script_with_error)

        # Should format what it can
        assert formatted is not None
        assert len(formatted) > 0
