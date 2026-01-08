"""
Tests for ASTNodeVisitor

Demonstrates ASTNodeVisitor usage with ASTNode hierarchies.
For core visitor mechanism tests, see test_tree_visitor.py.
For integration tests with Parser/Analyzer, see test_visitors_integration.py.
"""

from zetasql.api.ast_visitor import ASTNodeVisitor
from zetasql.types.proto_model import ASTBinaryExpression, ASTExpression, ASTNode, ASTPathExpression


class TestASTNodeVisitorUsage:
    """Test ASTNodeVisitor with actual AST nodes."""

    def test_visit_ast_node_with_specific_method(self):
        """Test visitor with AST-specific node types."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTExpression(self, node: ASTExpression) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # ASTPathExpression is a subclass of ASTExpression
        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        assert "ASTPathExpression" in visited

    def test_traverse_ast_tree(self):
        """Test traversing an AST tree structure."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Build AST structure
        lhs = ASTPathExpression()
        rhs = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=lhs, rhs=rhs)

        visitor = TestVisitor()
        visitor.visit(binary)

        assert "ASTBinaryExpression" in visited
        assert visited.count("ASTPathExpression") == 2
