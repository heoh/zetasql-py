"""
Tests for ASTNodeVisitor

Tests the visitor pattern for traversing ASTNode hierarchies with:
- Dynamic visit_{type} method dispatch using MRO
- descend() for child node traversal
- Caching optimization for field metadata
"""

from zetasql.api.ast_visitor import ASTNodeVisitor
from zetasql.types.proto_model import ASTBinaryExpression, ASTExpression, ASTNode, ASTPathExpression


class TestASTNodeVisitorBasics:
    """Test basic visitor functionality."""

    def test_default_visit_called_when_no_specific_visitor(self):
        """Test that default_visit is called when no visit_{type} method exists."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        # Create a simple AST node
        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        assert len(visited) == 1
        assert visited[0] == ("default", "ASTPathExpression")

    def test_specific_visit_method_called(self):
        """Test that visit_{type} method is called when it exists."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
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

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTExpression(self, node: ASTExpression) -> None:
                visited.append(("expression", type(node).__name__))

            def visit_ASTNode(self, node: ASTNode) -> None:
                visited.append(("node", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        # ASTPathExpression inherits from ASTExpression inherits from ASTNode
        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should call visit_ASTExpression (more specific than visit_ASTNode)
        assert len(visited) == 1
        assert visited[0] == ("expression", "ASTPathExpression")

    def test_mro_dispatch_falls_back_to_parent_class(self):
        """Test that MRO dispatch falls back to parent class visitor."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTNode(self, node: ASTNode) -> None:
                visited.append(("node", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        node = ASTPathExpression()
        visitor = TestVisitor()
        visitor.visit(node)

        # Should fall back to visit_ASTNode
        assert len(visited) == 1
        assert visited[0] == ("node", "ASTPathExpression")


class TestASTNodeVisitorDescend:
    """Test descend() functionality for child traversal."""

    def test_descend_not_called_children_not_visited(self):
        """Test that children are not visited if descend() is not called."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                # Intentionally NOT calling descend()

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        # Create binary expression with child nodes
        lhs = ASTPathExpression()
        rhs = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=lhs, rhs=rhs)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Only parent should be visited, not children
        assert len(visited) == 1
        assert visited[0] == ("binary", "ASTBinaryExpression")

    def test_descend_called_children_visited(self):
        """Test that children are visited when descend() is called."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                self.descend(node)  # Visit children

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

            def default_visit(self, node: ASTNode) -> None:
                visited.append(("default", type(node).__name__))

        lhs = ASTPathExpression()
        rhs = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=lhs, rhs=rhs)

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

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node):
                visited.append(type(node).__name__)
                self.descend(node)

        # Binary expression with no children
        binary = ASTBinaryExpression()
        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit parent, no errors
        assert len(visited) == 1
        assert visited[0] == "ASTBinaryExpression"


class TestASTNodeVisitorCaching:
    """Test field metadata caching optimization."""

    def test_field_metadata_cached_across_visits(self):
        """Test that field metadata is cached and reused."""
        visit_count = 0

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node: ASTNode) -> None:
                nonlocal visit_count
                visit_count += 1
                self.descend(node)

        lhs = ASTPathExpression()
        rhs = ASTPathExpression()
        binary1 = ASTBinaryExpression(lhs=lhs, rhs=rhs)
        binary2 = ASTBinaryExpression(lhs=lhs, rhs=rhs)

        visitor = TestVisitor()
        visitor.visit(binary1)

        # Cache should be populated
        assert len(visitor._field_cache) > 0
        cache_size_after_first = len(visitor._field_cache)

        visitor.visit(binary2)

        # Cache should not grow (same types visited)
        assert len(visitor._field_cache) == cache_size_after_first


class TestASTNodeVisitorOnlyMessageFields:
    """Test that only is_message=True fields are traversed."""

    def test_only_protomodel_children_visited(self):
        """Test that only ProtoModel fields (is_message=True) are visited."""
        visited_types = []

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node: ASTNode) -> None:
                visited_types.append(type(node).__name__)
                self.descend(node)

        lhs = ASTPathExpression()
        rhs = ASTPathExpression()
        # BinaryExpression has op (enum), is_not (bool), lhs, rhs (ProtoModel)
        binary = ASTBinaryExpression(
            lhs=lhs,
            rhs=rhs,
            op=1,  # Some enum value
            is_not=False,
        )

        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit ProtoModel nodes, not primitives/enums
        assert "ASTBinaryExpression" in visited_types
        assert "ASTPathExpression" in visited_types
        # Enum and bool should not appear as separate visits
        assert len([t for t in visited_types if "Expression" in t or "Node" in t]) == len(visited_types)


class TestASTNodeVisitorComplexTraversal:
    """Test complex tree traversal scenarios."""

    def test_nested_tree_traversal(self):
        """Test traversal of nested tree structure."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def default_visit(self, node: ASTNode) -> None:
                visited.append(type(node).__name__)
                self.descend(node)

        # Build nested structure: (a + b) + c
        a = ASTPathExpression()
        b = ASTPathExpression()
        ab = ASTBinaryExpression(lhs=a, rhs=b)
        c = ASTPathExpression()
        root = ASTBinaryExpression(lhs=ab, rhs=c)

        visitor = TestVisitor()
        visitor.visit(root)

        # Should visit all nodes in depth-first order
        assert len(visited) == 5
        assert visited[0] == "ASTBinaryExpression"  # root
        assert visited[1] == "ASTBinaryExpression"  # ab
        assert visited[2] == "ASTPathExpression"  # a
        assert visited[3] == "ASTPathExpression"  # b
        assert visited[4] == "ASTPathExpression"  # c

    def test_selective_descend(self):
        """Test selective descending based on node type."""
        visited = []

        class TestVisitor(ASTNodeVisitor):
            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                visited.append(("binary", type(node).__name__))
                # Only descend into left side
                if node.lhs:
                    self.visit(node.lhs)
                # Don't visit right side

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                visited.append(("path", type(node).__name__))

        a = ASTPathExpression()
        b = ASTPathExpression()
        binary = ASTBinaryExpression(lhs=a, rhs=b)

        visitor = TestVisitor()
        visitor.visit(binary)

        # Should only visit root and left child
        assert len(visited) == 2
        assert visited[0] == ("binary", "ASTBinaryExpression")
        assert visited[1] == ("path", "ASTPathExpression")
