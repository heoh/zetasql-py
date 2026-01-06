"""TableBuilder - Fluent API for building SimpleTable ProtoModel objects."""

from typing_extensions import Self

from zetasql.types import SimpleColumn, SimpleTable, Type, TypeKind

from ._helpers import convert_to_type


class TableBuilder:
    """Builder for SimpleTable ProtoModel objects.

    Args:
        name: Table name
        serialization_id: Optional table ID
    """

    def __init__(self, name: str, serialization_id: int | None = None):
        self._table = SimpleTable(name=name, serialization_id=serialization_id, column=[])

    def add_column(self, name: str, type_or_kind: Type | TypeKind | int) -> Self:
        """Add a column to the table."""
        column_type = convert_to_type(type_or_kind)
        column = SimpleColumn(name=name, type=column_type, is_writable_column=True)
        self._table.column.append(column)
        return self

    def with_serialization_id(self, serialization_id: int) -> Self:
        """Set serialization ID."""
        self._table.serialization_id = serialization_id
        return self

    def as_value_table(self) -> Self:
        """Mark table as a value table."""
        self._table.is_value_table = True
        return self

    def build(self) -> SimpleTable:
        """Build and return the SimpleTable ProtoModel."""
        return self._table


__all__ = ["TableBuilder"]
