"""
ResolvedNode Visitor Pattern

Provides a visitor class for traversing ResolvedNode hierarchies with:
- Dynamic visit_{type} method dispatch using MRO (most specific first)
- descend() for controlled child node traversal
- Caching optimization for field metadata and method dispatch
"""

from zetasql.api.tree_visitor import TreeVisitor
from zetasql.types.proto_model import ResolvedNode


class ResolvedNodeVisitor(TreeVisitor[ResolvedNode]):
    """
    Base class for visiting ResolvedNode trees.

    Subclasses can override visit_{NodeType} methods to handle specific node types.
    The visitor will automatically dispatch to the most specific method available
    based on the node's MRO (Method Resolution Order).

    Example:
        >>> class MyVisitor(ResolvedNodeVisitor):
        ...     def visit_ResolvedExpr(self, node: ResolvedExpr) -> None:
        ...         print(f"Visiting expression: {type(node).__name__}")
        ...         self.descend(node)  # Visit children
        ...
        ...     def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
        ...         print(f"Literal value: {node.value}")
        ...         # Don't call descend() to stop here
        ...
        ...     def default_visit(self, node: ResolvedNode) -> None:
        ...         print(f"Default: {type(node).__name__}")
        ...         self.descend(node)

    Usage:
        >>> visitor = MyVisitor()
        >>> visitor.visit(resolved_root)
    """

    pass
