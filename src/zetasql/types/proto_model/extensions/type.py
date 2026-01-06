"""
Type System Extensions - Domain logic for ZetaSQL types

This module extends the auto-generated Type ProtoModel with domain-specific
helper methods, providing a Java-compatible API for type checking and manipulation.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from zetasql.types.proto_model.generated import (
    Type as _GeneratedType,
)
from zetasql.types.proto_model.generated import (
    TypeKind,
)

if TYPE_CHECKING:
    from zetasql.types.proto_model import ArrayType, MapType, RangeType, StructType


@dataclass
class Type(_GeneratedType):
    """
    Enhanced Type with domain-specific helper methods.

    This class extends the auto-generated Type ProtoModel with Java-compatible
    helper methods for type checking, type narrowing, and formatting.

    All fields are inherited from the generated Type class. This class only
    adds methods and overrides the type hint for type_kind field.

    Examples:
        >>> from zetasql.types import Type, TypeKind
        >>> t = Type(type_kind=TypeKind.TYPE_INT64)
        >>> t.is_int64()
        True
        >>> t.is_numerical()
        True
        >>> t.type_name()
        'INT64'

        >>> # Array type
        >>> arr = Type(type_kind=TypeKind.TYPE_ARRAY)
        >>> arr.is_array()
        True
    """

    # Override type hint for better IDE support (value still compatible with int)
    type_kind: TypeKind = TypeKind.TYPE_UNKNOWN

    # ========== Type Checking Methods (Java API parity) ==========

    def is_int32(self) -> bool:
        """Returns true if type is INT32."""
        return self.type_kind == TypeKind.TYPE_INT32

    def is_int64(self) -> bool:
        """Returns true if type is INT64."""
        return self.type_kind == TypeKind.TYPE_INT64

    def is_uint32(self) -> bool:
        """Returns true if type is UINT32."""
        return self.type_kind == TypeKind.TYPE_UINT32

    def is_uint64(self) -> bool:
        """Returns true if type is UINT64."""
        return self.type_kind == TypeKind.TYPE_UINT64

    def is_bool(self) -> bool:
        """Returns true if type is BOOL."""
        return self.type_kind == TypeKind.TYPE_BOOL

    def is_float(self) -> bool:
        """Returns true if type is FLOAT."""
        return self.type_kind == TypeKind.TYPE_FLOAT

    def is_double(self) -> bool:
        """Returns true if type is DOUBLE."""
        return self.type_kind == TypeKind.TYPE_DOUBLE

    def is_string(self) -> bool:
        """Returns true if type is STRING."""
        return self.type_kind == TypeKind.TYPE_STRING

    def is_bytes(self) -> bool:
        """Returns true if type is BYTES."""
        return self.type_kind == TypeKind.TYPE_BYTES

    def is_date(self) -> bool:
        """Returns true if type is DATE."""
        return self.type_kind == TypeKind.TYPE_DATE

    def is_timestamp(self) -> bool:
        """Returns true if type is TIMESTAMP."""
        return self.type_kind == TypeKind.TYPE_TIMESTAMP

    def is_time(self) -> bool:
        """Returns true if type is TIME."""
        return self.type_kind == TypeKind.TYPE_TIME

    def is_datetime(self) -> bool:
        """Returns true if type is DATETIME."""
        return self.type_kind == TypeKind.TYPE_DATETIME

    def is_interval(self) -> bool:
        """Returns true if type is INTERVAL."""
        return self.type_kind == TypeKind.TYPE_INTERVAL

    def is_geography(self) -> bool:
        """Returns true if type is GEOGRAPHY."""
        return self.type_kind == TypeKind.TYPE_GEOGRAPHY

    def is_numeric(self) -> bool:
        """Returns true if type is NUMERIC."""
        return self.type_kind == TypeKind.TYPE_NUMERIC

    def is_bignumeric(self) -> bool:
        """Returns true if type is BIGNUMERIC."""
        return self.type_kind == TypeKind.TYPE_BIGNUMERIC

    def is_json(self) -> bool:
        """Returns true if type is JSON."""
        return self.type_kind == TypeKind.TYPE_JSON

    def is_enum(self) -> bool:
        """Returns true if type is ENUM."""
        return self.type_kind == TypeKind.TYPE_ENUM

    def is_array(self) -> bool:
        """Returns true if type is ARRAY."""
        return self.type_kind == TypeKind.TYPE_ARRAY

    def is_struct(self) -> bool:
        """Returns true if type is STRUCT."""
        return self.type_kind == TypeKind.TYPE_STRUCT

    def is_proto(self) -> bool:
        """Returns true if type is PROTO."""
        return self.type_kind == TypeKind.TYPE_PROTO

    def is_range(self) -> bool:
        """Returns true if type is RANGE."""
        return self.type_kind == TypeKind.TYPE_RANGE

    def is_map(self) -> bool:
        """Returns true if type is MAP."""
        return self.type_kind == TypeKind.TYPE_MAP

    def is_uuid(self) -> bool:
        """Returns true if type is UUID."""
        return self.type_kind == TypeKind.TYPE_UUID

    def is_graph_element(self) -> bool:
        """Returns true if type is GRAPH_ELEMENT."""
        return self.type_kind == TypeKind.TYPE_GRAPH_ELEMENT

    def is_graph_path(self) -> bool:
        """Returns true if type is GRAPH_PATH."""
        return self.type_kind == TypeKind.TYPE_GRAPH_PATH

    def is_measure(self) -> bool:
        """Returns true if type is MEASURE."""
        return self.type_kind == TypeKind.TYPE_MEASURE

    # ========== Type Category Methods ==========

    def is_integer(self) -> bool:
        """Returns true for any integer type (signed or unsigned)."""
        return TypeKind(self.type_kind).is_integer()

    def is_signed_integer(self) -> bool:
        """Returns true for signed integer types (INT32, INT64)."""
        return TypeKind(self.type_kind).is_signed_integer()

    def is_unsigned_integer(self) -> bool:
        """Returns true for unsigned integer types (UINT32, UINT64)."""
        return TypeKind(self.type_kind).is_unsigned_integer()

    def is_floating_point(self) -> bool:
        """Returns true for floating point types (FLOAT, DOUBLE)."""
        return TypeKind(self.type_kind).is_floating_point()

    def is_numerical(self) -> bool:
        """Returns true for any numeric type (integer, float, numeric, bignumeric)."""
        return TypeKind(self.type_kind).is_numerical()

    def is_temporal(self) -> bool:
        """Returns true for date/time types."""
        return TypeKind(self.type_kind).is_temporal()

    def is_simple(self) -> bool:
        """Returns true if this is a simple (non-composite) type."""
        return TypeKind(self.type_kind).is_simple()

    def is_composite(self) -> bool:
        """Returns true for composite types (array, struct, map, etc)."""
        return TypeKind(self.type_kind).is_composite()

    # ========== Type Narrowing Methods (Java asArray(), asStruct() pattern) ==========

    def as_array(self) -> Optional["ArrayType"]:
        """
        Returns ArrayType if this is an array type, else None.

        This follows the Java API pattern for safe type narrowing.

        Example:
            >>> if t.is_array():
            ...     arr = t.as_array()
            ...     elem_type = arr.element_type
        """
        return self.array_type if self.is_array() else None

    def as_struct(self) -> Optional["StructType"]:
        """
        Returns StructType if this is a struct type, else None.

        Example:
            >>> if t.is_struct():
            ...     st = t.as_struct()
            ...     for field in st.field:
            ...         print(field.field_name)
        """
        return self.struct_type if self.is_struct() else None

    def as_map(self) -> Optional["MapType"]:
        """Returns MapType if this is a map type, else None."""
        return self.map_type if self.is_map() else None

    def as_range(self) -> Optional["RangeType"]:
        """Returns RangeType if this is a range type, else None."""
        return self.range_type if self.is_range() else None

    # ========== Type Formatting ==========

    def type_name(self) -> str:
        """
        Returns human-readable type name.

        Returns:
            Type name string like 'INT64', 'ARRAY<STRING>', 'STRUCT<...>', etc.

        Example:
            >>> Type(type_kind=TypeKind.TYPE_INT64).type_name()
            'INT64'
            >>> # Array type returns 'ARRAY<element_type>'
        """
        # Composite types with nested elements
        if self.is_array() and self.array_type:
            elem_name = self.array_type.element_type.type_name() if self.array_type.element_type else "?"
            return f"ARRAY<{elem_name}>"

        if self.is_struct():
            return "STRUCT<...>"

        if self.is_map() and self.map_type:
            key_name = self.map_type.key_type.type_name() if self.map_type.key_type else "?"
            val_name = self.map_type.value_type.type_name() if self.map_type.value_type else "?"
            return f"MAP<{key_name}, {val_name}>"

        if self.is_range() and self.range_type:
            elem_name = self.range_type.element_type.type_name() if self.range_type.element_type else "?"
            return f"RANGE<{elem_name}>"

        # Simple type - use enum name without TYPE_ prefix
        kind = TypeKind(self.type_kind)
        try:
            return kind.name.removeprefix("TYPE_")
        except (ValueError, AttributeError):
            return f"UNKNOWN({self.type_kind})"

    def __str__(self) -> str:
        """Returns type name for string representation."""
        return self.type_name()

    def __repr__(self) -> str:
        """Returns detailed representation."""
        return f"Type(type_kind={self.type_kind.name if isinstance(self.type_kind, TypeKind) else self.type_kind})"


__all__ = ["Type"]
