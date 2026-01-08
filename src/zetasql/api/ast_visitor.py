"""
ASTNode Visitor Pattern

Provides a visitor class for traversing ASTNode hierarchies with:
- Dynamic visit_{type} method dispatch using MRO (most specific first)
- descend() for controlled child node traversal
- Caching optimization for field metadata and method dispatch
"""

from zetasql.api.tree_visitor import TreeVisitor
from zetasql.types.proto_model import ASTNode


class ASTNodeVisitor(TreeVisitor[ASTNode]):
    """
    Base class for visiting ASTNode trees.

    Subclasses can override visit_{NodeType} methods to handle specific node types.
    The visitor will automatically dispatch to the most specific method available
    based on the node's MRO (Method Resolution Order).

    Example:
        >>> class MyVisitor(ASTNodeVisitor):
        ...     def visit_ASTExpression(self, node: ASTExpression) -> None:
        ...         print(f"Visiting expression: {type(node).__name__}")
        ...         self.descend(node)  # Visit children
        ...
        ...     def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
        ...         print(f"Binary: {node.op}")
        ...         # Don't call descend() to stop here
        ...
        ...     def default_visit(self, node: ASTNode) -> None:
        ...         print(f"Default: {type(node).__name__}")
        ...         self.descend(node)

    Usage:
        >>> visitor = MyVisitor()
        >>> visitor.visit(ast_root)
    """

    pass
