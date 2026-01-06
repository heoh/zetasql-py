"""
TableBuilder - Fluent API for building SimpleTable ProtoModel objects

This module provides a Java-style builder pattern for constructing tables,
making catalog creation much cleaner than manual protobuf manipulation.

Examples:
    >>> from zetasql.builders import TableBuilder
    >>> from zetasql.types import TypeKind
    >>>
    >>> # Simple table with basic columns
    >>> orders = (TableBuilder("orders")
    ...     .add_column("order_id", TypeKind.TYPE_INT64)
    ...     .add_column("customer_id", TypeKind.TYPE_INT64)
    ...     .add_column("amount", TypeKind.TYPE_DOUBLE)
    ...     .build())
    >>>
    >>> # Table with complex types
    >>> from zetasql.api import TypeFactory
    >>>
    >>> users = (TableBuilder("users")
    ...     .add_column("id", TypeKind.TYPE_INT64)
    ...     .add_column("tags", TypeFactory.create_array_type(
    ...         TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
    ...     ))
    ...     .build())
"""

from typing_extensions import Self

from zetasql.api.type_factory import TypeFactory
from zetasql.types import SimpleColumn, SimpleTable, Type, TypeKind


class TableBuilder:
    """Builder for SimpleTable ProtoModel objects.

    Provides method chaining for fluent table construction. The builder
    creates ProtoModel objects that can be used directly with LocalService
    or CatalogBuilder.

    Args:
        name: Table name
        serialization_id: Optional table ID (auto-generated if not provided)

    Examples:
        >>> # Basic usage
        >>> table = (TableBuilder("products")
        ...     .add_column("product_id", TypeKind.TYPE_INT64)
        ...     .add_column("name", TypeKind.TYPE_STRING)
        ...     .add_column("price", TypeKind.TYPE_DOUBLE)
        ...     .build())
        >>>
        >>> # With serialization ID
        >>> table = (TableBuilder("orders", serialization_id=1)
        ...     .add_column("order_id", TypeKind.TYPE_INT64)
        ...     .build())
        >>>
        >>> # Using Type objects directly
        >>> str_array = TypeFactory.create_array_type(
        ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        ... )
        >>> table = (TableBuilder("items")
        ...     .add_column("tags", str_array)
        ...     .build())
    """

    def __init__(self, name: str, serialization_id: int | None = None):
        """Initialize TableBuilder.

        Args:
            name: Table name
            serialization_id: Optional table ID. If not provided, backend will assign one.
        """
        self._table = SimpleTable(name=name, serialization_id=serialization_id, column=[])

    def add_column(self, name: str, type_or_kind: Type | TypeKind | int) -> Self:
        """Add a column to the table.

        Accepts either a TypeKind enum (for simple types) or a Type ProtoModel
        (for complex types). Method chaining is supported.

        Args:
            name: Column name
            type_or_kind: Either TypeKind enum/int or Type ProtoModel

        Returns:
            Self for method chaining

        Examples:
            >>> # Simple type with TypeKind
            >>> builder.add_column("id", TypeKind.TYPE_INT64)
            >>>
            >>> # Complex type with Type object
            >>> array_type = TypeFactory.create_array_type(
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            ... )
            >>> builder.add_column("tags", array_type)
        """
        # Convert TypeKind to Type if needed
        if isinstance(type_or_kind, (TypeKind, int)):
            column_type = TypeFactory.create_simple_type(type_or_kind)
        else:
            column_type = type_or_kind

        # Create column
        column = SimpleColumn(name=name, type=column_type, is_writable_column=True)

        # Add to table's column list
        self._table.column.append(column)

        return self

    def with_serialization_id(self, serialization_id: int) -> Self:
        """Set serialization ID.

        Args:
            serialization_id: Table ID

        Returns:
            Self for method chaining
        """
        self._table.serialization_id = serialization_id
        return self

    def as_value_table(self) -> Self:
        """Mark table as a value table.

        Returns:
            Self for method chaining
        """
        self._table.is_value_table = True
        return self

    def build(self) -> SimpleTable:
        """Build and return the SimpleTable ProtoModel.

        Returns:
            SimpleTable ProtoModel ready to use with LocalService or CatalogBuilder

        Examples:
            >>> table = TableBuilder("users").add_column("id", TypeKind.TYPE_INT64).build()
            >>> # Use with CatalogBuilder
            >>> catalog = CatalogBuilder("my_catalog").add_table(table).build()
        """
        return self._table


__all__ = ["TableBuilder"]
