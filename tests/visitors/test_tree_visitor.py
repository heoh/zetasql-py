"""
Tests for TreeVisitor

Tests the generic visitor pattern for traversing ProtoModel hierarchies with:
- Dynamic visit_{type} method dispatch using MRO
- descend() for child node traversal
- Class-level caching optimization for field metadata and method dispatch
"""

from zetasql.api.tree_visitor import TreeVisitor
from zetasql.types.proto_model import (
    ASTBinaryExpression,
    ASTExpression,
    ASTFunctionCall,
    ASTNode,
    ASTPathExpression,
)


class TestTreeVisitorBasics:
    """Test basic visitor functionality."""

    def test_default_visit_called_when_no_specific_visitor(self):
        """Test that default_visit is called when no visit_{type} method exists."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) == 1
        assert visited[0] == ("default", "ASTPathExpression")

    def test_specific_visit_method_called(self):
        """Test that visit_{type} method is called when it exists."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("specific", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) == 1
        assert visited[0] == ("specific", "ASTPathExpression")

    def test_mro_dispatch_most_specific_first(self):
        """Test that MRO dispatch finds most specific visit method."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTExpression(self, node: ASTExpression) -> None:
                visited.append(("expression", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        # ASTPathExpression inherits from ASTExpression
        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should call visit_ASTExpression (parent class visitor)
        assert len(visited) == 1
        assert visited[0] == ("expression", "ASTPathExpression")

    def test_mro_dispatch_prefers_specific_over_parent(self):
        """Test that specific visit method is preferred over parent class visitor."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

            def visit_ASTExpression(self, node: ASTExpression) -> None:
                visited.append(("expression", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should prefer visit_ASTPathExpression over visit_ASTExpression
        assert len(visited) == 1
        assert visited[0] == ("path", "ASTPathExpression")

    def test_visit_none_returns_none(self):
        """Test that visiting None returns None without error."""

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                pass

        visitor = TestVisitor()
        result = visitor.visit(None)
        assert result is None


class TestTreeVisitorDescend:
    """Test descend() functionality for child traversal."""

    def test_descend_not_called_children_not_visited(self):
        """Test that children are not visited if descend() is not called."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                # Intentionally NOT calling descend()

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        # Create parent with children
        left = ASTPathExpression()
        right = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=left, rhs=right)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Only parent should be visited, not children
        assert len(visited) == 1
        assert visited[0] == ("binary", "ASTBinaryExpression")

    def test_descend_called_children_visited(self):
        """Test that children are visited when descend() is called."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                self.descend(node)  # Visit children

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        left = ASTPathExpression()
        right = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=left, rhs=right)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Parent and both children should be visited
        assert len(visited) == 3
        assert visited[0] == ("binary", "ASTBinaryExpression")
        assert visited[1] == ("path", "ASTPathExpression")
        assert visited[2] == ("path", "ASTPathExpression")

    def test_descend_handles_none_children(self):
        """Test that descend() handles None child fields gracefully."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Binary expression with no children
        binary = ASTBinaryExpression()
        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit parent, no errors
        assert len(visited) == 1
        assert visited[0] == "ASTBinaryExpression"

    def test_descend_handles_list_children(self):
        """Test that descend() handles list of child nodes."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # FunctionCall with multiple arguments (list)
        arg1 = ASTPathExpression()
        arg2 = ASTPathExpression()
        arg3 = ASTPathExpression()
        func = ASTFunctionCall(arguments=[arg1, arg2, arg3])

        visitor = TestVisitor()
        visitor.visit(func)

        # Should visit function and all arguments
        assert len(visited) == 4
        assert visited[0] == "ASTFunctionCall"
        assert visited[1] == "ASTPathExpression"
        assert visited[2] == "ASTPathExpression"
        assert visited[3] == "ASTPathExpression"

    def test_descend_none_node_does_nothing(self):
        """Test that descend(None) does nothing."""

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                pass

        visitor = TestVisitor()
        # Should not raise error
        visitor.descend(None)


class TestTreeVisitorCaching:
    """Test class-level caching optimization."""

    def test_field_metadata_cached_across_visits(self):
        """Test that field metadata is cached and reused."""

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        visitor = TestVisitor()

        # First visit should populate cache
        node1 = ASTPathExpression()
        visitor.visit(node1)

        assert len(TestVisitor._field_cache) > 0
        cache_size_after_first = len(TestVisitor._field_cache)

        # Second visit of same type should reuse cache
        node2 = ASTPathExpression()
        visitor.visit(node2)

        assert len(TestVisitor._field_cache) == cache_size_after_first

    def test_method_cache_populated_and_reused(self):
        """Test that method cache is populated and reused."""

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                pass

        visitor = TestVisitor()

        # First visit should populate method cache
        node1 = ASTPathExpression()
        visitor.visit(node1)

        assert len(TestVisitor._method_cache) > 0
        cache_size = len(TestVisitor._method_cache)

        # Second visit should reuse cached method
        node2 = ASTPathExpression()
        visitor.visit(node2)

        assert len(TestVisitor._method_cache) == cache_size

    def test_cache_shared_across_visitor_instances(self):
        """Test that cache is shared across different visitor instances."""

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        visitor1 = TestVisitor()
        visitor2 = TestVisitor()

        # First visitor populates cache
        node = ASTPathExpression()
        visitor1.visit(node)

        initial_cache_size = len(TestVisitor._field_cache)
        assert initial_cache_size > 0

        # Second visitor should see same cache
        visitor2.visit(node)
        assert len(TestVisitor._field_cache) == initial_cache_size


class TestTreeVisitorFieldFiltering:
    """Test that only is_message=True fields are traversed."""

    def test_only_protomodel_children_visited(self):
        """Test that only ProtoModel fields (is_message=True) are visited."""
        visited_types = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                visited_types.append(type(node).__name__)
                self.descend(node)

        left = ASTPathExpression()
        right = ASTPathExpression()
        # BinaryExpression has op (enum), is_not (bool), lhs, rhs (ProtoModel)
        binary = ASTBinaryExpression(lhs=left, rhs=right, op=1, is_not=False)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit ProtoModel nodes, not primitive value
        assert visited_types == ["ASTBinaryExpression", "ASTPathExpression", "ASTPathExpression"]
        assert len(visited_types) == 3


class TestTreeVisitorComplexTraversal:
    """Test complex tree traversal scenarios."""

    def test_nested_tree_traversal(self):
        """Test traversal of deeply nested tree structure."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Build nested structure: ((a + b) + (c + d))
        a = ASTPathExpression()
        b = ASTPathExpression()
        ab = ASTBinaryExpression(lhs=a, rhs=b)

        c = ASTPathExpression()
        d = ASTPathExpression()
        cd = ASTBinaryExpression(lhs=c, rhs=d)

        root = ASTBinaryExpression(lhs=ab, rhs=cd)

        visitor = TestVisitor()
        visitor.visit(root)

        # Should visit all nodes in depth-first order
        assert len(visited) == 7
        assert visited[0] == "ASTBinaryExpression"  # root
        assert visited[1] == "ASTBinaryExpression"  # ab
        assert visited[2] == "ASTPathExpression"  # a
        assert visited[3] == "ASTPathExpression"  # b
        assert visited[4] == "ASTBinaryExpression"  # cd
        assert visited[5] == "ASTPathExpression"  # c
        assert visited[6] == "ASTPathExpression"  # d

    def test_selective_descend(self):
        """Test selective descending based on node type."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                # Only descend into left side
                if node.lhs:
                    self.visit(node.lhs)
                # Don't visit right side

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

        left = ASTPathExpression()
        right = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=left, rhs=right)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit root and left child
        assert len(visited) == 2
        assert visited[0] == ("binary", "ASTBinaryExpression")
        assert visited[1] == ("path", "ASTPathExpression")

    def test_visitor_can_collect_specific_nodes(self):
        """Test visitor can collect specific node types."""

        class PathCollector(TreeVisitor[ASTNode]):
            def __init__(self):
                self.paths = []

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                self.paths.append(node)

            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        a = ASTPathExpression()
        b = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=a, rhs=b)

        visitor = PathCollector()
        visitor.visit(binary)

        assert len(visitor.paths) == 2

    def test_default_visit_automatically_descends(self):
        """Test that default_visit() automatically descends by default."""
        visited = []

        class TestVisitor(TreeVisitor[ASTNode]):
            # Override only to track visits, rely on default descend behavior
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                super().default_visit(node)  # Calls descend

        left = ASTPathExpression()
        right = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=left, rhs=right)

        visitor = TestVisitor()
        visitor.visit(binary)

        # All nodes should be visited via default descend
        assert len(visited) == 3
        assert "ASTBinaryExpression" in visited
        assert visited.count("ASTPathExpression") == 2
