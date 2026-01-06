"""
ConstantBuilder - Fluent API for building SimpleConstant ProtoModel objects

This module provides a Java-style builder pattern for constructing constants,
making catalog constant creation much cleaner than manual protobuf manipulation.

Constants in ZetaSQL represent named typed values (like DECLARE variables in scripts).
They store name and type, but typically not values.

Examples:
    >>> from zetasql.api.builders import ConstantBuilder
    >>> from zetasql.types import TypeKind
    >>>
    >>> # Simple constant
    >>> max_limit = (ConstantBuilder("MAX_LIMIT")
    ...     .set_type(TypeKind.TYPE_INT64)
    ...     .build())
    >>>
    >>> # String constant
    >>> default_name = (ConstantBuilder("DEFAULT_NAME")
    ...     .set_type(TypeKind.TYPE_STRING)
    ...     .build())
    >>>
    >>> # Complex type constant
    >>> from zetasql.api import TypeFactory
    >>>
    >>> tags_const = (ConstantBuilder("DEFAULT_TAGS")
    ...     .set_type(TypeFactory.create_array_type(
    ...         TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
    ...     ))
    ...     .build())
"""

from typing_extensions import Self

from zetasql.api.type_factory import TypeFactory
from zetasql.types import SimpleConstant, Type, TypeKind


class ConstantBuilder:
    """Builder for SimpleConstant ProtoModel objects.

    Provides method chaining for fluent constant construction. The builder
    creates ProtoModel objects that can be used directly with SimpleCatalog.

    Constants are used for DECLARE variables in scripts and represent
    named typed values in the catalog.

    Args:
        name: Constant name

    Examples:
        >>> # Basic constant
        >>> const = (ConstantBuilder("MY_CONSTANT")
        ...     .set_type(TypeKind.TYPE_INT64)
        ...     .build())
        >>>
        >>> # Qualified name constant
        >>> const = (ConstantBuilder("pkg.MY_CONST")
        ...     .set_type(TypeKind.TYPE_STRING)
        ...     .build())
    """

    def __init__(self, name: str):
        """Initialize ConstantBuilder.

        Args:
            name: Constant name. Can be simple ("MAX_LIMIT") or qualified ("pkg.MAX_LIMIT")
        """
        # Split name into name_path (following Function pattern)
        name_path = name.split(".") if "." in name else [name]

        self._constant = SimpleConstant(
            name_path=name_path,
            type=None,
            value=None,  # Typically constants don't have values in catalog
        )

    def set_type(self, type_or_kind: Type | TypeKind | int) -> Self:
        """Set the type of the constant.

        Args:
            type_or_kind: Type object or TypeKind enum value

        Returns:
            Self for method chaining

        Examples:
            >>> # Simple type
            >>> builder.set_type(TypeKind.TYPE_INT64)
            >>>
            >>> # Complex type
            >>> array_type = TypeFactory.create_array_type(
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            ... )
            >>> builder.set_type(array_type)
        """
        # Convert TypeKind to Type if needed (following TableBuilder pattern)
        if isinstance(type_or_kind, (TypeKind, int)):
            const_type = TypeFactory.create_simple_type(type_or_kind)
        else:
            const_type = type_or_kind

        self._constant.type = const_type
        return self

    def build(self) -> SimpleConstant:
        """Build and return the SimpleConstant ProtoModel.

        Returns:
            SimpleConstant ProtoModel ready for use with SimpleCatalog
        """
        return self._constant
