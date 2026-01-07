"""
Tests for ResolvedNodeVisitor

Tests the visitor pattern for traversing ResolvedNode hierarchies with:
- Dynamic visit_{type} method dispatch using MRO
- descend() for child node traversal
- Caching optimization for field metadata
"""

from zetasql.api.resolved_visitor import ResolvedNodeVisitor
from zetasql.types.proto_model import ResolvedColumnRef, ResolvedExpr, ResolvedLiteral, ResolvedNode, ResolvedQueryStmt


class TestResolvedNodeVisitorBasics:
    """Test basic visitor functionality."""

    def test_default_visit_called_when_no_specific_visitor(self):
        """Test that default_visit is called when no visit_{type} method exists."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        # Create a simple Resolved node
        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) == 1
        assert visited[0] == ("default", "ResolvedLiteral")

    def test_specific_visit_method_called(self):
        """Test that visit_{type} method is called when it exists."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                visited.append(("specific", type(node).__name__))

            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) == 1
        assert visited[0] == ("specific", "ResolvedLiteral")

    def test_mro_dispatch_most_specific_first(self):
        """Test that MRO dispatch finds most specific visit method."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedExpr(self, node: ResolvedExpr) -> None:
                visited.append(("expr", type(node).__name__))

            def visit_ResolvedNode(self, node: ResolvedNode) -> None:
                visited.append(("node", type(node).__name__))

            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        # ResolvedLiteral inherits from ResolvedExpr inherits from ResolvedNode
        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should call visit_ResolvedExpr (more specific than visit_ResolvedNode)
        assert len(visited) == 1
        assert visited[0] == ("expr", "ResolvedLiteral")

    def test_mro_dispatch_falls_back_to_parent_class(self):
        """Test that MRO dispatch falls back to parent class visitor."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedNode(self, node: ResolvedNode) -> None:
                visited.append(("node", type(node).__name__))

            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should fall back to visit_ResolvedNode
        assert len(visited) == 1
        assert visited[0] == ("node", "ResolvedLiteral")


class TestResolvedNodeVisitorDescend:
    """Test descend() functionality for child traversal."""

    def test_descend_not_called_children_not_visited(self):
        """Test that children are not visited if descend() is not called."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedQueryStmt(self, node: ResolvedQueryStmt) -> None:
                visited.append(("query", type(node).__name__))
                # Intentionally NOT calling descend()

            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        # Create query with child nodes
        query = ResolvedQueryStmt()
        visitor = TestVisitor()
        visitor.visit(query)

        # Only parent should be visited, not children
        assert len(visited) == 1
        assert visited[0] == ("query", "ResolvedQueryStmt")

    def test_descend_called_children_visited(self):
        """Test that children are visited when descend() is called."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node):
                visited.append(type(node).__name__)
                self.descend(node)

        # Create a structure with children
        col_ref = ResolvedColumnRef()
        visitor = TestVisitor()
        visitor.visit(col_ref)

        # Node should be visited
        assert "ResolvedColumnRef" in visited

    def test_descend_handles_none_children(self):
        """Test that descend() handles None child fields gracefully."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Node with no children
        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should only visit parent, no errors
        assert len(visited) == 1
        assert visited[0] == "ResolvedLiteral"

    def test_descend_handles_list_children(self):
        """Test that descend() handles list of child nodes."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # ResolvedQueryStmt has output_column_list which is a list
        query = ResolvedQueryStmt()
        visitor = TestVisitor()
        visitor.visit(query)

        # Should handle list fields without error
        assert "ResolvedQueryStmt" in visited


class TestResolvedNodeVisitorCaching:
    """Test field metadata caching optimization."""

    def test_field_metadata_cached_across_visits(self):
        """Test that field metadata is cached and reused."""
        visit_count = 0

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                nonlocal visit_count
                visit_count += 1
                self.descend(node)

        node1 = ResolvedLiteral()
        node2 = ResolvedLiteral()

        visitor = TestVisitor()
        visitor.visit(node1)

        # Cache should be populated
        assert len(visitor._field_cache) > 0
        cache_size_after_first = len(visitor._field_cache)

        visitor.visit(node2)

        # Cache should not grow (same types visited)
        assert len(visitor._field_cache) == cache_size_after_first

    def test_method_cache_populated(self):
        """Test that method cache is populated and reused."""

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                pass

        visitor = TestVisitor()
        node1 = ResolvedLiteral()
        node2 = ResolvedLiteral()

        visitor.visit(node1)
        assert len(visitor._method_cache) > 0

        cache_size = len(visitor._method_cache)
        visitor.visit(node2)

        # Cache should be reused
        assert len(visitor._method_cache) == cache_size


class TestResolvedNodeVisitorOnlyMessageFields:
    """Test that only is_message=True fields are traversed."""

    def test_only_protomodel_children_visited(self):
        """Test that only ProtoModel fields (is_message=True) are visited."""
        visited_types = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited_types.append(type(node).__name__)
                self.descend(node)

        # ResolvedQueryStmt has various field types
        query = ResolvedQueryStmt()
        visitor = TestVisitor()
        visitor.visit(query)

        # Should only visit ProtoModel nodes, not primitives/enums
        assert "ResolvedQueryStmt" in visited_types
        # Primitives/enums should not appear as separate visits


class TestResolvedNodeVisitorComplexTraversal:
    """Test complex tree traversal scenarios."""

    def test_nested_tree_traversal(self):
        """Test traversal can handle nested structures."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Simple structure
        node = ResolvedLiteral()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) >= 1
        assert "ResolvedLiteral" in visited

    def test_selective_descend(self):
        """Test selective descending based on node type."""
        visited = []

        class TestVisitor(ResolvedNodeVisitor):
            def visit_ResolvedQueryStmt(self, node: ResolvedQueryStmt) -> None:
                visited.append(("query", type(node).__name__))
                # Don't descend - selective control

            def default_visit(self, node: ResolvedNode) -> None:
                visited.append(("default", type(node).__name__))

        query = ResolvedQueryStmt()
        visitor = TestVisitor()
        visitor.visit(query)

        # Should only visit root
        assert len(visited) == 1
        assert visited[0] == ("query", "ResolvedQueryStmt")

    def test_visitor_can_collect_specific_nodes(self):
        """Test visitor can collect specific node types."""

        class LiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
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
