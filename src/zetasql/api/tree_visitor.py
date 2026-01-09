"""
TreeVisitor - Generic Visitor Pattern for ProtoModel Trees

Provides a generic base visitor class for traversing ProtoModel hierarchies with:
- Dynamic visit_{type} method dispatch using MRO (most specific first)
- descend() for controlled child node traversal
- Class-level caching optimization for field metadata and method dispatch
"""

from typing import Any, ClassVar, Generic, TypeVar

from zetasql.types.proto_model import ProtoModel

# Type variable bound to ProtoModel for generic visitor
T = TypeVar("T", bound=ProtoModel)


class TreeVisitor(Generic[T]):
    """
    Generic base class for visiting ProtoModel trees.

    Subclasses can override visit_{NodeType} methods to handle specific node types.
    The visitor will automatically dispatch to the most specific method available
    based on the node's MRO (Method Resolution Order).

    Type Parameter:
        T: The ProtoModel subclass this visitor operates on (e.g., ASTNode, ResolvedNode)

    Example:
        >>> class MyVisitor(TreeVisitor[ASTNode]):
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
        >>> visitor.visit(tree_root)
    """

    # Class-level caches shared across instances of the same visitor class
    # Each subclass gets its own cache dictionaries
    _field_cache: ClassVar[dict[type, list[tuple]]] = {}
    _method_cache: ClassVar[dict[type, str]] = {}  # Stores method names, not callables

    def __init_subclass__(cls, **kwargs):
        """Initialize separate caches for each subclass."""
        super().__init_subclass__(**kwargs)
        # Each subclass gets its own cache dictionaries
        cls._field_cache = {}
        cls._method_cache = {}

    def visit(self, node: T) -> Any:
        """
        Visit a node by dispatching to the most specific visit_{type} method.

        Searches through the node's MRO to find the most specific visitor method.
        Falls back to default_visit if no specific method is found.

        Args:
            node: The ProtoModel node to visit

        Returns:
            The return value of the visitor method
        """
        if node is None:
            return None

        node_type = type(node)

        # Check method cache first
        if node_type in self.__class__._method_cache:
            method_name = self.__class__._method_cache[node_type]
            method = getattr(self, method_name)
            return method(node)

        # Find the most specific visitor method using MRO
        method_name = self._find_visitor_method_name(node_type)

        # Cache the method name for future visits
        self.__class__._method_cache[node_type] = method_name

        method = getattr(self, method_name)
        return method(node)

    def _find_visitor_method_name(self, node_type: type) -> str:
        """
        Find the most specific visitor method name for a node type.

        Walks the MRO from most specific to least specific, looking for
        visit_{ClassName} methods. Stops at ProtoModel base class.

        Args:
            node_type: The type of node to find a visitor for

        Returns:
            The visitor method name (or 'default_visit' if none found)
        """
        # Walk MRO from most specific to most general
        for cls in node_type.__mro__:
            # Stop at ProtoModel - don't go beyond our type hierarchy
            if cls is ProtoModel:
                break

            method_name = f"visit_{cls.__name__}"
            if hasattr(self, method_name):
                return method_name

        # No specific visitor found, use default
        return "default_visit"

    def default_visit(self, node: T) -> Any:
        """
        Default visitor method called when no specific visit_{type} exists.

        By default, automatically descends into child nodes. Override this to
        provide custom default behavior. If you override this, remember to call
        self.descend(node) if you want to continue traversing children.

        Args:
            node: The ProtoModel node being visited

        Returns:
            None by default
        """
        self.descend(node)

    def descend(self, node: T) -> None:
        """
        Visit all child nodes of the given node.

        Only visits fields that are ProtoModel instances (is_message=True).
        Handles both single nodes and lists of nodes.

        Call this method in your visit_{type} methods to traverse child nodes.
        If you don't call this, the traversal stops at the current node.

        Args:
            node: The ProtoModel node whose children should be visited
        """
        if node is None:
            return

        node_type = type(node)

        # Check cache first
        if node_type not in self.__class__._field_cache:
            self.__class__._field_cache[node_type] = self._get_message_fields(node_type)

        message_fields = self.__class__._field_cache[node_type]

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

        # Build a combined field map from the entire inheritance chain
        combined_field_map = {}
        for cls in reversed(node_type.__mro__):
            # Skip ProtoModel itself and classes before it (object, etc.)
            if not issubclass(cls, ProtoModel) or cls is ProtoModel:
                continue

            # Merge this class's field map (child overrides parent)
            if hasattr(cls, "_PROTO_FIELD_MAP"):
                combined_field_map.update(cls._PROTO_FIELD_MAP)

        # Extract message fields from combined_field_map
        for field_name, field_meta in combined_field_map.items():
            # Skip private fields
            if field_name.startswith("_"):
                continue

            # Check if this field is a message (ProtoModel child)
            if field_meta.get("is_message", False):
                is_repeated = field_meta.get("is_repeated", False)
                message_fields.append((field_name, is_repeated))

        return message_fields
