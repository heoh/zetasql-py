"""Value wrapper for ZetaSQL typed values.

Provides Java-style Value API wrapping the proto-based Value ProtoModel.
Mirrors Java's Value class for creating and manipulating typed SQL values.
"""

import datetime
from typing import Any

from google.protobuf.timestamp_pb2 import Timestamp

from zetasql import types
from zetasql.types import TypeKind


class Value:
    """Wrapper for ZetaSQL Value ProtoModel with Java-style API.

    Provides factory methods for creating typed values and accessor methods
    for retrieving typed data. Wraps the underlying Value ProtoModel from
    zetasql.types.

    Example:
        >>> # Create values
        >>> v1 = Value.int64(42)
        >>> v2 = Value.string("hello")
        >>> v3 = Value.null(TypeKind.TYPE_INT64)
        >>>
        >>> # Access values
        >>> assert v1.get_int64() == 42
        >>> assert v2.get_string() == "hello"
        >>> assert v3.is_null()
    """

    def __init__(self, proto_value: types.Value, type_kind: TypeKind | None = None):
        """Initialize Value wrapper from ProtoModel Value.

        Args:
            proto_value: Value ProtoModel from zetasql.types
            type_kind: Optional TypeKind for null values (since proto doesn't store type for nulls)
        """
        self._proto = proto_value
        self._type_kind = type_kind  # Only used for null values
        self._field_names: list[str] | None = None  # For STRUCT field names
        self._element_metadata: list[dict[str, Any]] | None = None  # For ARRAY element metadata

    @property
    def type_kind(self) -> TypeKind:
        """Get the TypeKind of this value.

        Returns:
            TypeKind enum value
        """
        if self._type_kind is not None:
            return self._type_kind

        # Map proto field names to TypeKind values
        field_to_type = {
            "int64_value": TypeKind.TYPE_INT64,
            "string_value": TypeKind.TYPE_STRING,
            "bool_value": TypeKind.TYPE_BOOL,
            "double_value": TypeKind.TYPE_DOUBLE,
            "int32_value": TypeKind.TYPE_INT32,
            "float_value": TypeKind.TYPE_FLOAT,
            "date_value": TypeKind.TYPE_DATE,
            "timestamp_value": TypeKind.TYPE_TIMESTAMP,
            "array_value": TypeKind.TYPE_ARRAY,
            "struct_value": TypeKind.TYPE_STRUCT,
        }

        for field_name, type_kind in field_to_type.items():
            if getattr(self._proto, field_name) is not None:
                return type_kind

        return TypeKind.TYPE_UNKNOWN

    def is_null(self) -> bool:
        """Check if this value is NULL.

        Returns:
            True if value is NULL
        """
        return all(
            getattr(self._proto, field) is None
            for field in [
                "int32_value",
                "int64_value",
                "uint32_value",
                "uint64_value",
                "bool_value",
                "float_value",
                "double_value",
                "string_value",
                "bytes_value",
                "date_value",
                "timestamp_value",
                "array_value",
                "struct_value",
            ]
        )

    def get_int64(self) -> int:
        """Get INT64 value.

        Returns:
            Python int

        Raises:
            ValueError: If type is not INT64 or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_INT64:
            raise ValueError(f"Type mismatch: expected INT64, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.int64_value

    def get_string(self) -> str:
        """Get STRING value.

        Returns:
            Python str

        Raises:
            ValueError: If type is not STRING or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_STRING:
            raise ValueError(f"Type mismatch: expected STRING, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.string_value

    def get_bool(self) -> bool:
        """Get BOOL value.

        Returns:
            Python bool

        Raises:
            ValueError: If type is not BOOL or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_BOOL:
            raise ValueError(f"Type mismatch: expected BOOL, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.bool_value

    def get_double(self) -> float:
        """Get DOUBLE value.

        Returns:
            Python float

        Raises:
            ValueError: If type is not DOUBLE or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_DOUBLE:
            raise ValueError(f"Type mismatch: expected DOUBLE, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.double_value

    def get_int32(self) -> int:
        """Get INT32 value.

        Returns:
            Python int

        Raises:
            ValueError: If type is not INT32 or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_INT32:
            raise ValueError(f"Type mismatch: expected INT32, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.int32_value

    def get_float(self) -> float:
        """Get FLOAT value.

        Returns:
            Python float

        Raises:
            ValueError: If type is not FLOAT or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_FLOAT:
            raise ValueError(f"Type mismatch: expected FLOAT, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.float_value

    def get_date(self) -> "datetime.date":
        """Get DATE value.

        Returns:
            Python date

        Raises:
            ValueError: If type is not DATE or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_DATE:
            raise ValueError(f"Type mismatch: expected DATE, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        epoch = datetime.date(1970, 1, 1)
        return epoch + datetime.timedelta(days=self._proto.date_value)

    def get_timestamp(self) -> "datetime.datetime":
        """Get TIMESTAMP value.

        Returns:
            Python datetime

        Raises:
            ValueError: If type is not TIMESTAMP or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_TIMESTAMP:
            raise ValueError(f"Type mismatch: expected TIMESTAMP, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return self._proto.timestamp_value.ToDatetime()

    def get_array_size(self) -> int:
        """Get size of ARRAY value.

        Returns:
            Number of elements in array

        Raises:
            ValueError: If type is not ARRAY or value is NULL
        """
        if self.type_kind != TypeKind.TYPE_ARRAY:
            raise ValueError(f"Type mismatch: expected ARRAY, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        return len(self._proto.array_value.element)

    def get_array_element(self, index: int) -> "Value":
        """Get element from ARRAY value.

        Args:
            index: Element index (0-based)

        Returns:
            Value at the given index

        Raises:
            ValueError: If type is not ARRAY or value is NULL
            IndexError: If index out of range
        """
        if self.type_kind != TypeKind.TYPE_ARRAY:
            raise ValueError(f"Type mismatch: expected ARRAY, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        if index < 0 or index >= len(self._proto.array_value.element):
            raise IndexError(f"Array index {index} out of range")

        # Create Value from proto element
        elem_value = Value(self._proto.array_value.element[index])

        # Restore metadata if available
        if self._element_metadata and index < len(self._element_metadata):
            metadata = self._element_metadata[index]
            if "field_names" in metadata:
                elem_value._field_names = metadata["field_names"]

        return elem_value

    def get_field(self, field_name: str) -> "Value":
        """Get field from STRUCT value by name.

        Args:
            field_name: Name of the field

        Returns:
            Value of the field

        Raises:
            ValueError: If type is not STRUCT or value is NULL
            KeyError: If field not found
        """
        if self.type_kind != TypeKind.TYPE_STRUCT:
            raise ValueError(f"Type mismatch: expected STRUCT, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        if self._field_names is None:
            raise ValueError("STRUCT field names not available")
        if field_name not in self._field_names:
            raise KeyError(f"Field '{field_name}' not found in STRUCT")

        index = self._field_names.index(field_name)
        return Value(self._proto.struct_value.field[index])

    # Factory methods for creating values

    @staticmethod
    def int64(value: int) -> "Value":
        """Create INT64 value.

        Args:
            value: Python int

        Returns:
            Value wrapper

        Example:
            >>> v = Value.int64(42)
            >>> assert v.get_int64() == 42
        """
        proto = types.Value(int64_value=value)
        return Value(proto)

    @staticmethod
    def string(value: str) -> "Value":
        """Create STRING value.

        Args:
            value: Python str

        Returns:
            Value wrapper

        Example:
            >>> v = Value.string("hello")
            >>> assert v.get_string() == "hello"
        """
        proto = types.Value(string_value=value)
        return Value(proto)

    @staticmethod
    def bool(value: bool) -> "Value":
        """Create BOOL value.

        Args:
            value: Python bool

        Returns:
            Value wrapper

        Example:
            >>> v = Value.bool(True)
            >>> assert v.get_bool() is True
        """
        proto = types.Value(bool_value=value)
        return Value(proto)

    @staticmethod
    def double(value: float) -> "Value":
        """Create DOUBLE value.

        Args:
            value: Python float

        Returns:
            Value wrapper

        Example:
            >>> v = Value.double(3.14)
            >>> assert abs(v.get_double() - 3.14) < 0.001
        """
        proto = types.Value(double_value=value)
        return Value(proto)

    @staticmethod
    def int32(value: int) -> "Value":
        """Create INT32 value.

        Args:
            value: Python int

        Returns:
            Value wrapper
        """
        proto = types.Value(int32_value=value)
        return Value(proto)

    @staticmethod
    def float_value(value: float) -> "Value":
        """Create FLOAT value.

        Args:
            value: Python float

        Returns:
            Value wrapper
        """
        proto = types.Value(float_value=value)
        return Value(proto)

    @staticmethod
    def date(year: int, month: int, day: int) -> "Value":
        """Create DATE value.

        Args:
            year: Year
            month: Month (1-12)
            day: Day (1-31)

        Returns:
            Value wrapper

        Example:
            >>> v = Value.date(2024, 1, 15)
            >>> assert v.get_date().year == 2024
        """
        epoch = datetime.date(1970, 1, 1)
        target_date = datetime.date(year, month, day)
        days_since_epoch = (target_date - epoch).days
        proto = types.Value(date_value=days_since_epoch)
        return Value(proto)

    @staticmethod
    def timestamp(dt: "datetime.datetime") -> "Value":
        """Create TIMESTAMP value.

        Args:
            dt: Python datetime

        Returns:
            Value wrapper

        Example:
            >>> import datetime
            >>> dt = datetime.datetime(2024, 1, 15, 10, 30, 45)
            >>> v = Value.timestamp(dt)
            >>> assert v.get_timestamp() == dt
        """
        timestamp_proto = Timestamp()
        timestamp_proto.FromDatetime(dt)
        proto = types.Value(timestamp_value=timestamp_proto)
        return Value(proto)

    @staticmethod
    def null(type_kind: TypeKind) -> "Value":
        """Create NULL value of specified type.

        Args:
            type_kind: TypeKind for the NULL value

        Returns:
            Value wrapper representing NULL

        Example:
            >>> v = Value.null(TypeKind.TYPE_INT64)
            >>> assert v.is_null()
            >>> assert v.type_kind == TypeKind.TYPE_INT64
        """
        proto = types.Value()
        return Value(proto, type_kind=type_kind)

    @staticmethod
    def array(elements: list["Value"]) -> "Value":
        """Create ARRAY value.

        Args:
            elements: List of Value elements

        Returns:
            Value wrapper representing ARRAY

        Example:
            >>> elements = [Value.int64(1), Value.int64(2), Value.int64(3)]
            >>> arr = Value.array(elements)
            >>> arr.get_array_size() == 3
        """
        proto_elements = [elem.to_proto() for elem in elements]
        array_proto = types.Value.Array(element=proto_elements)
        proto = types.Value(array_value=array_proto)

        value_obj = Value(proto)
        value_obj._element_metadata = [
            {"field_names": elem._field_names} if elem._field_names is not None else {} for elem in elements
        ]
        return value_obj

    @staticmethod
    def struct(fields: dict[str, "Value"]) -> "Value":
        """Create STRUCT value.

        Args:
            fields: Dictionary mapping field names to Values

        Returns:
            Value wrapper representing STRUCT

        Example:
            >>> s = Value.struct({
            ...     "name": Value.string("Alice"),
            ...     "age": Value.int64(30)
            ... })
            >>> s.get_field("name").get_string() == "Alice"
        """
        proto_fields = [value.to_proto() for value in fields.values()]
        struct_proto = types.Value.Struct(field=proto_fields)
        proto = types.Value(struct_value=struct_proto)

        value_obj = Value(proto)
        value_obj._field_names = list(fields.keys())
        return value_obj

    @staticmethod
    def from_proto(proto: types.Value) -> "Value":
        """Create Value wrapper from ProtoModel Value.

        Args:
            proto: Value ProtoModel

        Returns:
            Value wrapper
        """
        return Value(proto)

    def to_proto(self) -> types.Value:
        """Get underlying ProtoModel Value.

        Returns:
            Value ProtoModel
        """
        return self._proto

    def equals(self, other: "Value") -> bool:
        """Check equality with another Value.

        Args:
            other: Another Value to compare

        Returns:
            True if values are equal
        """
        if not isinstance(other, Value):
            return False

        if self.type_kind != other.type_kind:
            return False

        if self.is_null() and other.is_null():
            return True

        if self.is_null() != other.is_null():
            return False

        type_to_getter = {
            TypeKind.TYPE_INT64: lambda v: v.get_int64(),
            TypeKind.TYPE_STRING: lambda v: v.get_string(),
            TypeKind.TYPE_BOOL: lambda v: v.get_bool(),
            TypeKind.TYPE_DOUBLE: lambda v: v.get_double(),
            TypeKind.TYPE_INT32: lambda v: v.get_int32(),
            TypeKind.TYPE_FLOAT: lambda v: v.get_float(),
            TypeKind.TYPE_DATE: lambda v: v.get_date(),
            TypeKind.TYPE_TIMESTAMP: lambda v: v.get_timestamp(),
        }

        getter = type_to_getter.get(self.type_kind)
        if getter:
            return getter(self) == getter(other)

        return self._proto == other._proto

    def compare_to(self, other: "Value") -> int:
        """Compare this value to another.

        Args:
            other: Another Value to compare

        Returns:
            -1 if self < other, 0 if equal, 1 if self > other

        Raises:
            ValueError: If types don't match or values are NULL
        """
        if not isinstance(other, Value):
            raise ValueError("Can only compare with another Value")

        if self.type_kind != other.type_kind:
            raise ValueError(f"Cannot compare different types: {self.type_kind} vs {other.type_kind}")

        if self.is_null() or other.is_null():
            raise ValueError("Cannot compare NULL values")

        type_to_getter = {
            TypeKind.TYPE_INT64: lambda v: v.get_int64(),
            TypeKind.TYPE_INT32: lambda v: v.get_int32(),
            TypeKind.TYPE_DOUBLE: lambda v: v.get_double(),
            TypeKind.TYPE_FLOAT: lambda v: v.get_float(),
            TypeKind.TYPE_STRING: lambda v: v.get_string(),
            TypeKind.TYPE_BOOL: lambda v: v.get_bool(),
            TypeKind.TYPE_DATE: lambda v: v.get_date(),
            TypeKind.TYPE_TIMESTAMP: lambda v: v.get_timestamp(),
        }

        getter = type_to_getter.get(self.type_kind)
        if not getter:
            raise ValueError(f"Comparison not supported for type {self.type_kind}")

        a, b = getter(self), getter(other)
        return -1 if a < b else (1 if a > b else 0)

    def to_sql_literal(self) -> str:
        """Convert value to SQL literal string.

        Returns:
            SQL literal representation

        Example:
            >>> Value.int64(42).to_sql_literal()
            '42'
            >>> Value.string("hello").to_sql_literal()
            "'hello'"
        """
        if self.is_null():
            return "NULL"

        if self.type_kind == TypeKind.TYPE_STRING:
            escaped = self.get_string().replace("'", "''")
            return f"'{escaped}'"

        type_to_sql = {
            TypeKind.TYPE_BOOL: lambda: "TRUE" if self.get_bool() else "FALSE",
            TypeKind.TYPE_INT64: lambda: str(self.get_int64()),
            TypeKind.TYPE_INT32: lambda: str(self.get_int32()),
            TypeKind.TYPE_DOUBLE: lambda: str(self.get_double()),
            TypeKind.TYPE_FLOAT: lambda: str(self.get_float()),
            TypeKind.TYPE_DATE: lambda: f"DATE '{self.get_date().isoformat()}'",
            TypeKind.TYPE_TIMESTAMP: lambda: f"TIMESTAMP '{self.get_timestamp().isoformat()}'",
        }

        converter = type_to_sql.get(self.type_kind)
        return converter() if converter else str(self)

    def __str__(self) -> str:
        """String representation of the value.

        Returns:
            String representation matching SQL literals
        """
        if self.is_null():
            return "NULL"

        type_to_str = {
            TypeKind.TYPE_STRING: lambda: f'"{self.get_string()}"',
            TypeKind.TYPE_BOOL: lambda: "true" if self.get_bool() else "false",
            TypeKind.TYPE_INT64: lambda: str(self.get_int64()),
            TypeKind.TYPE_INT32: lambda: str(self.get_int32()),
            TypeKind.TYPE_DOUBLE: lambda: str(self.get_double()),
            TypeKind.TYPE_FLOAT: lambda: str(self.get_float()),
            TypeKind.TYPE_DATE: lambda: str(self.get_date()),
            TypeKind.TYPE_TIMESTAMP: lambda: str(self.get_timestamp()),
        }

        converter = type_to_str.get(self.type_kind)
        return converter() if converter else f"Value({self.type_kind})"

    def __repr__(self) -> str:
        """Developer representation."""
        return f"Value({self._proto})"

    def get_type(self) -> "types.Type":
        """Get the Type of this value.

        Mirrors Java's Value.getType() method for type introspection.

        Returns:
            Type object representing this value's type

        Example:
            >>> v = Value.int64(42)
            >>> t = v.get_type()
            >>> assert t.type_kind == TypeKind.TYPE_INT64
        """
        return types.Type(type_kind=self.type_kind)

    def __iter__(self):
        """Iterate over ARRAY elements.

        Yields:
            Value: Each element in the array

        Raises:
            ValueError: If type is not ARRAY
        """
        if self.type_kind != TypeKind.TYPE_ARRAY:
            raise ValueError(f"Cannot iterate over non-ARRAY type: {self.type_kind}")

        for i in range(self.get_array_size()):
            yield self.get_array_element(i)

    def coerce_to(self, target_type: TypeKind) -> "Value":
        """Coerce value to a different type.

        Type coercion attempts to convert a value to another compatible type
        following SQL coercion rules (e.g., INT64 -> STRING, INT32 -> INT64).

        Args:
            target_type: Target TypeKind to coerce to

        Returns:
            New Value with coerced type

        Raises:
            ValueError: If coercion is not supported

        Example:
            >>> v = Value.int64(42)
            >>> s = v.coerce_to(TypeKind.TYPE_STRING)
            >>> s.get_string() == "42"
        """
        if self.type_kind == target_type:
            return self

        if self.is_null():
            return Value.null(target_type)

        # Define coercion rules as nested dict: source_type -> target_type -> converter
        coercion_rules = {
            TypeKind.TYPE_INT64: {
                TypeKind.TYPE_STRING: lambda: Value.string(str(self.get_int64())),
                TypeKind.TYPE_DOUBLE: lambda: Value.double(float(self.get_int64())),
                TypeKind.TYPE_FLOAT: lambda: Value.float_value(float(self.get_int64())),
            },
            TypeKind.TYPE_INT32: {
                TypeKind.TYPE_INT64: lambda: Value.int64(self.get_int32()),
                TypeKind.TYPE_STRING: lambda: Value.string(str(self.get_int32())),
                TypeKind.TYPE_DOUBLE: lambda: Value.double(float(self.get_int32())),
                TypeKind.TYPE_FLOAT: lambda: Value.float_value(float(self.get_int32())),
            },
            TypeKind.TYPE_DOUBLE: {
                TypeKind.TYPE_STRING: lambda: Value.string(str(self.get_double())),
            },
            TypeKind.TYPE_FLOAT: {
                TypeKind.TYPE_DOUBLE: lambda: Value.double(self.get_float()),
                TypeKind.TYPE_STRING: lambda: Value.string(str(self.get_float())),
            },
            TypeKind.TYPE_BOOL: {
                TypeKind.TYPE_STRING: lambda: Value.string("true" if self.get_bool() else "false"),
                TypeKind.TYPE_INT64: lambda: Value.int64(1 if self.get_bool() else 0),
            },
            TypeKind.TYPE_DATE: {
                TypeKind.TYPE_STRING: lambda: Value.string(self.get_date().isoformat()),
            },
            TypeKind.TYPE_TIMESTAMP: {
                TypeKind.TYPE_STRING: lambda: Value.string(self.get_timestamp().isoformat()),
            },
        }

        converter = coercion_rules.get(self.type_kind, {}).get(target_type)
        if converter:
            return converter()

        raise ValueError(f"Cannot coerce {self.type_kind} to {target_type}")

    def cast_to(self, target_type: TypeKind) -> "Value":
        """Cast value to a different type with explicit conversion.

        Type casting is more aggressive than coercion and may fail at runtime
        if the conversion is invalid (e.g., "abc" -> INT64).

        Args:
            target_type: Target TypeKind to cast to

        Returns:
            New Value with cast type

        Raises:
            ValueError: If cast fails or is not supported

        Example:
            >>> v = Value.string("123")
            >>> i = v.cast_to(TypeKind.TYPE_INT64)
            >>> i.get_int64() == 123
        """
        if self.type_kind == target_type:
            return self

        if self.is_null():
            return Value.null(target_type)

        # STRING casts (parse from string)
        if self.type_kind == TypeKind.TYPE_STRING:
            return self._cast_from_string(target_type)

        # Numeric casts
        if self.type_kind in (TypeKind.TYPE_INT64, TypeKind.TYPE_INT32, TypeKind.TYPE_DOUBLE, TypeKind.TYPE_FLOAT):
            return self._cast_from_numeric(target_type)

        # Try coercion as fallback
        try:
            return self.coerce_to(target_type)
        except ValueError as e:
            raise ValueError(f"Cannot cast {self.type_kind} to {target_type}") from e

    def _cast_from_string(self, target_type: TypeKind) -> "Value":
        """Cast STRING value to target type."""
        s = self.get_string()

        cast_functions = {
            TypeKind.TYPE_INT64: lambda: Value.int64(int(s)),
            TypeKind.TYPE_INT32: lambda: Value.int32(int(s)),
            TypeKind.TYPE_DOUBLE: lambda: Value.double(float(s)),
            TypeKind.TYPE_FLOAT: lambda: Value.float_value(float(s)),
            TypeKind.TYPE_BOOL: self._parse_bool_from_string,
        }

        caster = cast_functions.get(target_type)
        if not caster:
            raise ValueError(f"Cannot cast STRING to {target_type}")

        try:
            return caster()
        except (ValueError, OverflowError) as e:
            raise ValueError(f"Cannot cast STRING '{s}' to {target_type}: {e}") from e

    def _parse_bool_from_string(self) -> "Value":
        """Parse boolean value from string."""
        s = self.get_string().lower()
        if s in ("true", "t", "1", "yes"):
            return Value.bool(True)
        if s in ("false", "f", "0", "no"):
            return Value.bool(False)
        raise ValueError(f"Cannot parse '{s}' as BOOL")

    def _cast_from_numeric(self, target_type: TypeKind) -> "Value":
        """Cast numeric value to target type."""
        # Get numeric value based on source type
        value_getters = {
            TypeKind.TYPE_INT64: self.get_int64,
            TypeKind.TYPE_INT32: self.get_int32,
            TypeKind.TYPE_DOUBLE: self.get_double,
            TypeKind.TYPE_FLOAT: self.get_float,
        }

        val = value_getters[self.type_kind]()

        cast_functions = {
            TypeKind.TYPE_INT64: lambda: Value.int64(int(val)),
            TypeKind.TYPE_INT32: lambda: Value.int32(int(val)),
            TypeKind.TYPE_DOUBLE: lambda: Value.double(float(val)),
            TypeKind.TYPE_FLOAT: lambda: Value.float_value(float(val)),
            TypeKind.TYPE_STRING: lambda: Value.string(str(val)),
            TypeKind.TYPE_BOOL: lambda: Value.bool(val != 0),
        }

        caster = cast_functions.get(target_type)
        if not caster:
            raise ValueError(f"Cannot cast {self.type_kind} to {target_type}")

        try:
            return caster()
        except (ValueError, OverflowError) as e:
            raise ValueError(f"Cannot cast {self.type_kind} to {target_type}: {e}") from e
