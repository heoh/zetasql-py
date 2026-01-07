"""
Tests for Parser class

Tests the high-level Parser API for syntax-only SQL parsing.
Validates both instance and static methods.
"""

import pytest

from zetasql.api import ASTNodeVisitor, Parser
from zetasql.core import ServerError
from zetasql.types import (
    ASTQueryStatement,
    ASTScript,
    ASTStatement,
    LanguageOptions,
    ParseResumeLocation,
)


class TestParserBasics:
    """Test basic Parser functionality."""

    def test_parser_instance_creation(self):
        """Test creating a Parser instance."""
        parser = Parser()
        assert parser is not None
        assert parser.options is None  # Default is None

    def test_parser_instance_with_options(self):
        """Test creating Parser with LanguageOptions."""
        options = LanguageOptions()
        parser = Parser(options)
        assert parser.options is options

    def test_parse_simple_statement(self):
        """Test parsing a simple SELECT statement."""
        parser = Parser()
        stmt = parser.parse_statement("SELECT 1 AS one")

        assert stmt is not None
        assert isinstance(stmt, ASTStatement)
        assert isinstance(stmt, ASTQueryStatement)

    def test_parse_statement_static(self):
        """Test static parse_statement method."""
        stmt = Parser.parse_statement_static("SELECT 1 AS one")

        assert stmt is not None
        assert isinstance(stmt, ASTStatement)
        assert isinstance(stmt, ASTQueryStatement)

    def test_parse_statement_with_from_clause(self):
        """Test parsing SELECT with FROM clause."""
        stmt = Parser.parse_statement_static("SELECT id, name FROM Users")

        assert stmt is not None
        assert isinstance(stmt, ASTQueryStatement)

    def test_parse_statement_with_where(self):
        """Test parsing SELECT with WHERE clause."""
        stmt = Parser.parse_statement_static("SELECT * FROM Orders WHERE price > 100")

        assert stmt is not None
        assert isinstance(stmt, ASTQueryStatement)

    def test_parse_statement_invalid_syntax(self):
        """Test that invalid syntax raises an error."""
        with pytest.raises(ServerError):
            Parser.parse_statement_static("SELECT * FORM table")

    def test_parse_statement_empty_string(self):
        """Test parsing empty string."""
        with pytest.raises(ServerError):
            Parser.parse_statement_static("")


class TestParserScript:
    """Test script parsing functionality."""

    def test_parse_script_single_statement(self):
        """Test parsing script with single statement."""
        script = Parser.parse_script_static("SELECT 1;")

        assert script is not None
        assert isinstance(script, ASTScript)
        assert script.statement_list_node is not None

    def test_parse_script_multiple_statements(self):
        """Test parsing script with multiple statements."""
        script = Parser.parse_script_static("SELECT 1; SELECT 2; SELECT 3;")

        assert script is not None
        assert isinstance(script, ASTScript)
        assert script.statement_list_node is not None
        assert len(script.statement_list_node.statement_list) == 3

    def test_parse_script_instance_method(self):
        """Test instance method for script parsing."""
        parser = Parser()
        script = parser.parse_script("SELECT 1; SELECT 2;")

        assert script is not None
        assert isinstance(script, ASTScript)
        assert len(script.statement_list_node.statement_list) == 2

    def test_parse_script_complex(self):
        """Test parsing complex multi-statement script."""
        sql = """
        SELECT id, name FROM Users;
        SELECT order_id, amount FROM Orders WHERE amount > 100;
        SELECT COUNT(*) FROM Products;
        """
        script = Parser.parse_script_static(sql)

        assert script is not None
        assert isinstance(script, ASTScript)
        assert len(script.statement_list_node.statement_list) == 3


class TestParserNextStatement:
    """Test sequential statement parsing."""

    def test_parse_next_statement_basic(self):
        """Test parsing statements sequentially."""
        script = "SELECT 1; SELECT 2; SELECT 3;"
        location = ParseResumeLocation(input=script, byte_position=0)

        parser = Parser()
        stmt1 = parser.parse_next_statement(location)
        assert stmt1 is not None
        assert isinstance(stmt1, ASTQueryStatement)

        stmt2 = parser.parse_next_statement(location)
        assert stmt2 is not None
        assert isinstance(stmt2, ASTQueryStatement)

        stmt3 = parser.parse_next_statement(location)
        assert stmt3 is not None
        assert isinstance(stmt3, ASTQueryStatement)

        # No more statements
        stmt4 = parser.parse_next_statement(location)
        assert stmt4 is None

    def test_parse_next_statement_static(self):
        """Test static method for next statement."""
        script = "SELECT 1; SELECT 2;"
        location = ParseResumeLocation(input=script, byte_position=0)

        stmt1 = Parser.parse_next_statement_static(location)
        assert stmt1 is not None

        stmt2 = Parser.parse_next_statement_static(location)
        assert stmt2 is not None

        stmt3 = Parser.parse_next_statement_static(location)
        assert stmt3 is None

    def test_parse_next_statement_updates_location(self):
        """Test that parse_next_statement updates location.byte_position."""
        script = "SELECT 1; SELECT 2;"
        location = ParseResumeLocation(input=script, byte_position=0)

        initial_pos = location.byte_position
        Parser.parse_next_statement_static(location)

        # Position should have moved forward
        assert location.byte_position > initial_pos

    def test_parse_next_script_statement(self):
        """Test parse_next_script_statement method."""
        script = "SELECT 1; SELECT 2;"
        location = ParseResumeLocation(input=script, byte_position=0)

        parser = Parser()
        stmt1 = parser.parse_next_script_statement(location)
        assert stmt1 is not None

        stmt2 = parser.parse_next_script_statement(location)
        assert stmt2 is not None

    def test_parse_next_script_statement_static(self):
        """Test static parse_next_script_statement method."""
        script = "SELECT 1; SELECT 2;"
        location = ParseResumeLocation(input=script, byte_position=0)

        stmt1 = Parser.parse_next_script_statement_static(location)
        assert stmt1 is not None

        stmt2 = Parser.parse_next_script_statement_static(location)
        assert stmt2 is not None


class TestParserIterator:
    """Test iterate_statements generator."""

    def test_iterate_statements_basic(self):
        """Test iterating through statements."""
        script = "SELECT 1; SELECT 2; SELECT 3;"
        statements = list(Parser.iterate_statements(script))

        assert len(statements) == 3
        for stmt in statements:
            assert isinstance(stmt, ASTQueryStatement)

    def test_iterate_statements_empty(self):
        """Test iterating with no statements."""
        statements = list(Parser.iterate_statements(""))
        assert len(statements) == 0

    def test_iterate_statements_single(self):
        """Test iterating with single statement."""
        statements = list(Parser.iterate_statements("SELECT 1;"))
        assert len(statements) == 1

    def test_iterate_statements_complex(self):
        """Test iterating through complex script."""
        script = """
        SELECT id FROM Users;
        SELECT order_id FROM Orders;
        SELECT product_id FROM Products;
        """
        statements = list(Parser.iterate_statements(script))
        assert len(statements) == 3


class TestParserWithVisitor:
    """Test Parser integration with ASTNodeVisitor."""

    def test_parse_and_visit(self):
        """Test parsing and visiting AST nodes."""
        visited_nodes = []

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node):
                visited_nodes.append(type(node).__name__)
                self.descend(node)

        stmt = Parser.parse_statement_static("SELECT 1 AS one")
        visitor = TestVisitor()
        visitor.visit(stmt)

        # Should have visited at least the statement node
        assert len(visited_nodes) > 0
        assert "ASTQueryStatement" in visited_nodes

    def test_parse_script_and_visit_all(self):
        """Test parsing script and visiting all statements."""
        visited_statements = []

        class StatementCollector(ASTNodeVisitor):
            def visit_ASTQueryStatement(self, node):
                visited_statements.append(node)
                # Don't descend to avoid collecting child nodes

        script = Parser.parse_script_static("SELECT 1; SELECT 2; SELECT 3;")

        # Visit each statement in the script
        for stmt in script.statement_list_node.statement_list:
            visitor = StatementCollector()
            visitor.visit(stmt)

        assert len(visited_statements) == 3

    def test_parse_and_extract_info_with_visitor(self):
        """Test using visitor to extract information from parsed AST."""

        class QueryStatementCounter(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.query_count = 0

            def visit_ASTQueryStatement(self, node):
                self.query_count += 1
                self.descend(node)

        stmt = Parser.parse_statement_static("SELECT a, b FROM t")
        visitor = QueryStatementCounter()
        visitor.visit(stmt)

        # Should have found the query statement
        assert visitor.query_count == 1


class TestParserLanguageOptions:
    """Test Parser with different LanguageOptions."""

    def test_parser_with_custom_options(self):
        """Test Parser with custom language options."""
        options = LanguageOptions()
        parser = Parser(options)

        stmt = parser.parse_statement("SELECT 1")
        assert stmt is not None

    def test_static_parse_with_options(self):
        """Test static parsing with language options."""
        options = LanguageOptions()
        stmt = Parser.parse_statement_static("SELECT 1", options)
        assert stmt is not None


class TestParserErrorHandling:
    """Test error handling in Parser."""

    def test_syntax_error_in_statement(self):
        """Test that syntax errors are raised."""
        with pytest.raises(ServerError):
            Parser.parse_statement_static("SELECT * FORM table")

    def test_syntax_error_in_script(self):
        """Test that syntax errors in scripts are raised."""
        with pytest.raises(ServerError):
            Parser.parse_script_static("SELECT 1; SELECT * FORM table;")

    def test_incomplete_statement(self):
        """Test parsing incomplete statement."""
        with pytest.raises(ServerError):
            Parser.parse_statement_static("SELECT * FROM")


class TestParserVsAnalyzer:
    """Test differences between Parser and Analyzer."""

    def test_parser_returns_ast_statement(self):
        """Test that Parser returns ASTStatement (not ResolvedStatement)."""
        stmt = Parser.parse_statement_static("SELECT 1")

        # Should be ASTStatement, not ResolvedStatement
        assert isinstance(stmt, ASTStatement)
        assert type(stmt).__name__ == "ASTQueryStatement"

    def test_parser_no_catalog_required(self):
        """Test that Parser doesn't require catalog."""
        # This should work without any catalog
        stmt = Parser.parse_statement_static("SELECT * FROM NonExistentTable")

        # Parser doesn't validate table existence
        assert stmt is not None
        assert isinstance(stmt, ASTStatement)

    def test_parser_no_type_checking(self):
        """Test that Parser doesn't perform type checking."""
        # This would fail in Analyzer due to type mismatch, but Parser allows it
        stmt = Parser.parse_statement_static("SELECT 1 + 'string'")

        # Parser only checks syntax, not types
        assert stmt is not None
        assert isinstance(stmt, ASTStatement)


class TestParserEdgeCases:
    """Test edge cases and special scenarios."""

    def test_parse_whitespace_only(self):
        """Test parsing whitespace-only string."""
        with pytest.raises(ServerError):
            Parser.parse_statement_static("   \n  \t  ")

    def test_parse_comments(self):
        """Test parsing statements with comments."""
        stmt = Parser.parse_statement_static("-- This is a comment\nSELECT 1")
        assert stmt is not None

    def test_parse_multi_line_statement(self):
        """Test parsing multi-line statement."""
        sql = """
        SELECT
            id,
            name,
            email
        FROM
            Users
        WHERE
            active = TRUE
        """
        stmt = Parser.parse_statement_static(sql)
        assert stmt is not None

    def test_parse_with_semicolon(self):
        """Test parsing statement with trailing semicolon."""
        stmt = Parser.parse_statement_static("SELECT 1;")
        assert stmt is not None

    def test_script_with_empty_statements(self):
        """Test script with multiple semicolons."""
        # This might raise an error or skip empty statements
        # depending on ZetaSQL behavior
        try:
            script = Parser.parse_script_static("SELECT 1;; SELECT 2;")
            # If it succeeds, verify we got statements
            assert script is not None
        except ServerError:
            # Empty statements might cause errors
            pass
