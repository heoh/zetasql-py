"""
Tests for ResolvedNodeVisitor

Demonstrates ResolvedNodeVisitor usage with ResolvedNode hierarchies.
For core visitor mechanism tests, see test_tree_visitor.py.
For integration tests with Parser/Analyzer, see test_visitors_integration.py.
"""

from zetasql.api.resolved_visitor import ResolvedNodeVisitor
from zetasql.types.proto_model import ResolvedExpr, ResolvedLiteral, ResolvedNode, ResolvedQueryStmt


class TestResolvedNodeVisitorUsage:
    """Test ResolvedNodeVisitor with actual Resolved nodes."""

    def test_visit_resolved_node_with_specific_method(self):
        """Test visitor with Resolved-specific node types."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedExpr(self, node: ResolvedExpr) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # ResolvedLiteral is a subclass of ResolvedExpr
        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        assert "ResolvedLiteral" in visited

    def test_traverse_resolved_tree(self):
        """Test traversing a resolved tree structure."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Simple resolved node
        query = ResolvedQueryStmt()
        visitor = TestVisitor()
        visitor.visit(query)

        assert "ResolvedQueryStmt" in visited

    def test_collect_specific_resolved_nodes(self):
        """Test collecting specific node types from resolved tree."""

        class LiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                self.literals = []

            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                self.literals.append(node)
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        visitor = LiteralCollector()
        lit1 = ResolvedLiteral()
        lit2 = ResolvedLiteral()

        visitor.visit(lit1)
        visitor.visit(lit2)

        assert len(visitor.literals) == 2
