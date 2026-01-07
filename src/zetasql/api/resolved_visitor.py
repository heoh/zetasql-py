"""
ResolvedNode Visitor Pattern

Provides a base visitor class for traversing ResolvedNode hierarchies with:
- Dynamic visit_{type} method dispatch using MRO (most specific first)
- descend() for controlled child node traversal
- Caching optimization for field metadata and method dispatch
"""

from collections.abc import Callable
from dataclasses import fields
from typing import Any

from zetasql.types.proto_model import ProtoModel, ResolvedNode


class ResolvedNodeVisitor:
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

    def __init__(self):
        """Initialize visitor with empty caches."""
        # Cache for field metadata: {node_type: [(field_name, is_repeated), ...]}
        self._field_cache: dict[type, list[tuple]] = {}

        # Cache for method dispatch: {node_type: method_callable}
        self._method_cache: dict[type, Callable] = {}

    def visit(self, node: ResolvedNode) -> Any:
        """
        Visit a node by dispatching to the most specific visit_{type} method.

        Searches through the node's MRO to find the most specific visitor method.
        Falls back to default_visit if no specific method is found.

        Args:
            node: The ResolvedNode to visit

        Returns:
            The return value of the visitor method
        """
        if node is None:
            return None

        node_type = type(node)

        # Check method cache first
        if node_type in self._method_cache:
            method = self._method_cache[node_type]
            return method(node)

        # Find the most specific visitor method using MRO
        method = self._find_visitor_method(node_type)

        # Cache the method for future visits
        self._method_cache[node_type] = method

        return method(node)

    def _find_visitor_method(self, node_type: type) -> Callable:
        """
        Find the most specific visitor method for a node type.

        Walks the MRO from most specific to least specific, looking for
        visit_{ClassName} methods. Stops at ProtoModel base class.

        Args:
            node_type: The type of node to find a visitor for

        Returns:
            The visitor method callable (or default_visit if none found)
        """
        # Walk MRO from most specific to most general
        for cls in node_type.__mro__:
            # Stop at ProtoModel - don't go beyond our type hierarchy
            if cls is ProtoModel:
                break

            method_name = f"visit_{cls.__name__}"
            if hasattr(self, method_name):
                return getattr(self, method_name)

        # No specific visitor found, use default
        return self.default_visit

    def default_visit(self, node: ResolvedNode) -> Any:
        """
        Default visitor method called when no specific visit_{type} exists.

        By default, automatically descends into child nodes. Override this to
        provide custom default behavior. If you override this, remember to call
        self.descend(node) if you want to continue traversing children.

        Args:
            node: The ResolvedNode being visited

        Returns:
            None by default
        """
        self.descend(node)

    def descend(self, node: ResolvedNode) -> None:
        """
        Visit all child nodes of the given node.

        Only visits fields that are ProtoModel instances (is_message=True).
        Handles both single nodes and lists of nodes.

        Call this method in your visit_{type} methods to traverse child nodes.
        If you don't call this, the traversal stops at the current node.

        Args:
            node: The ResolvedNode whose children should be visited
        """
        if node is None:
            return

        node_type = type(node)

        # Check cache first
        if node_type not in self._field_cache:
            self._field_cache[node_type] = self._get_message_fields(node_type)

        message_fields = self._field_cache[node_type]

        # Visit each child node
        for field_name, is_repeated in message_fields:
            value = getattr(node, field_name, None)

            if value is None:
                continue

            if is_repeated:
                # Handle list of child nodes
                for item in value:
                    if isinstance(item, ProtoModel):
                        self.visit(item)
            else:
                # Handle single child node
                if isinstance(value, ProtoModel):
                    self.visit(value)

    def _get_message_fields(self, node_type: type) -> list[tuple]:
        """
        Extract fields that are ProtoModel children (is_message=True).

        Args:
            node_type: The type of node to analyze

        Returns:
            List of (field_name, is_repeated) tuples for ProtoModel fields
        """
        message_fields = []

        # Get the _PROTO_FIELD_MAP from the node class
        if not hasattr(node_type, "_PROTO_FIELD_MAP"):
            return message_fields

        field_map = node_type._PROTO_FIELD_MAP

        # Get all dataclass fields
        for field in fields(node_type):
            field_name = field.name

            # Skip private fields
            if field_name.startswith("_"):
                continue

            # Check if this field is a message (ProtoModel child)
            if field_name in field_map:
                field_meta = field_map[field_name]
                if field_meta.get("is_message", False):
                    is_repeated = field_meta.get("is_repeated", False)
                    message_fields.append((field_name, is_repeated))

        return message_fields
