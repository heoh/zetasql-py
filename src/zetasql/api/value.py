"""Value wrapper for ZetaSQL typed values.

Provides Java-style Value API wrapping the proto-based Value ProtoModel.
Mirrors Java's Value class for creating and manipulating typed SQL values.
"""

from typing import Optional, Any, List, Dict, Union
import zetasql.core.types as types
from zetasql.core.types import TypeKind


class Value:
    """Wrapper for ZetaSQL Value ProtoModel with Java-style API.
    
    Provides factory methods for creating typed values and accessor methods
    for retrieving typed data. Wraps the underlying Value ProtoModel from
    zetasql.core.types.
    
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
    
    def __init__(self, proto_value: types.Value, type_kind: Optional[TypeKind] = None):
        """Initialize Value wrapper from ProtoModel Value.
        
        Args:
            proto_value: Value ProtoModel from zetasql.core.types
            type_kind: Optional TypeKind for null values (since proto doesn't store type for nulls)
        """
        self._proto = proto_value
        self._type_kind = type_kind  # Only used for null values
        self._field_names: Optional[List[str]] = None  # For STRUCT field names
        self._element_metadata: Optional[List[Dict[str, Any]]] = None  # For ARRAY element metadata
    
    @property
    def type_kind(self) -> TypeKind:
        """Get the TypeKind of this value.
        
        Returns:
            TypeKind enum value
        """
        # If this is a null value, use stored type_kind
        if self._type_kind is not None:
            return self._type_kind
            
        # Infer type from which value field is set
        if self._proto.int64_value is not None:
            return TypeKind.TYPE_INT64
        elif self._proto.string_value is not None:
            return TypeKind.TYPE_STRING
        elif self._proto.bool_value is not None:
            return TypeKind.TYPE_BOOL
        elif self._proto.double_value is not None:
            return TypeKind.TYPE_DOUBLE
        elif self._proto.int32_value is not None:
            return TypeKind.TYPE_INT32
        elif self._proto.float_value is not None:
            return TypeKind.TYPE_FLOAT
        elif self._proto.date_value is not None:
            return TypeKind.TYPE_DATE
        elif self._proto.timestamp_value is not None:
            return TypeKind.TYPE_TIMESTAMP
        elif self._proto.array_value is not None:
            return TypeKind.TYPE_ARRAY
        elif self._proto.struct_value is not None:
            return TypeKind.TYPE_STRUCT
        # Add more type checks as needed
        return TypeKind.TYPE_UNKNOWN
    
    def is_null(self) -> bool:
        """Check if this value is NULL.
        
        Returns:
            True if value is NULL
        """
        # A value is null if all value fields are None
        return (self._proto.int32_value is None and
                self._proto.int64_value is None and
                self._proto.uint32_value is None and
                self._proto.uint64_value is None and
                self._proto.bool_value is None and
                self._proto.float_value is None and
                self._proto.double_value is None and
                self._proto.string_value is None and
                self._proto.bytes_value is None and
                self._proto.date_value is None and
                self._proto.timestamp_value is None and
                self._proto.array_value is None and
                self._proto.struct_value is None)
    
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
    
    def get_date(self) -> 'datetime.date':
        """Get DATE value.
        
        Returns:
            Python date
            
        Raises:
            ValueError: If type is not DATE or value is NULL
        """
        import datetime
        if self.type_kind != TypeKind.TYPE_DATE:
            raise ValueError(f"Type mismatch: expected DATE, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        # DATE is stored as days since epoch
        epoch = datetime.date(1970, 1, 1)
        return epoch + datetime.timedelta(days=self._proto.date_value)
    
    def get_timestamp(self) -> 'datetime.datetime':
        """Get TIMESTAMP value.
        
        Returns:
            Python datetime
            
        Raises:
            ValueError: If type is not TIMESTAMP or value is NULL
        """
        import datetime
        if self.type_kind != TypeKind.TYPE_TIMESTAMP:
            raise ValueError(f"Type mismatch: expected TIMESTAMP, got {self.type_kind}")
        if self.is_null():
            raise ValueError("Cannot get value from NULL")
        # Convert protobuf Timestamp to datetime
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
    
    def get_array_element(self, index: int) -> 'Value':
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
            if 'field_names' in metadata:
                elem_value._field_names = metadata['field_names']
        
        return elem_value
    
    def get_field(self, field_name: str) -> 'Value':
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
    def int64(value: int) -> 'Value':
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
    def string(value: str) -> 'Value':
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
    def bool(value: bool) -> 'Value':
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
    def double(value: float) -> 'Value':
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
    def int32(value: int) -> 'Value':
        """Create INT32 value.
        
        Args:
            value: Python int
            
        Returns:
            Value wrapper
        """
        proto = types.Value(int32_value=value)
        return Value(proto)
    
    @staticmethod
    def float_value(value: float) -> 'Value':
        """Create FLOAT value.
        
        Args:
            value: Python float
            
        Returns:
            Value wrapper
        """
        proto = types.Value(float_value=value)
        return Value(proto)
    
    @staticmethod
    def date(year: int, month: int, day: int) -> 'Value':
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
        import datetime
        # DATE is stored as days since epoch (1970-01-01)
        epoch = datetime.date(1970, 1, 1)
        target_date = datetime.date(year, month, day)
        days_since_epoch = (target_date - epoch).days
        proto = types.Value(date_value=days_since_epoch)
        return Value(proto)
    
    @staticmethod
    def timestamp(dt: 'datetime.datetime') -> 'Value':
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
        import datetime
        from google.protobuf.timestamp_pb2 import Timestamp
        
        # Convert datetime to protobuf Timestamp
        timestamp_proto = Timestamp()
        timestamp_proto.FromDatetime(dt)
        
        # Create types.Value with timestamp
        proto = types.Value(timestamp_value=timestamp_proto)
        return Value(proto)
    
    @staticmethod
    def null(type_kind: TypeKind) -> 'Value':
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
        # For null values, we create a Value with no value field set
        # Store the type_kind separately since proto doesn't store it for nulls
        proto = types.Value()
        return Value(proto, type_kind=type_kind)
    
    @staticmethod
    def array(elements: list['Value']) -> 'Value':
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
        # Extract proto Values from wrappers
        proto_elements = [elem.to_proto() for elem in elements]
        
        # Create Array with elements
        array_proto = types.Value.Array(element=proto_elements)
        
        # Create Value with array_value
        proto = types.Value(array_value=array_proto)
        
        # Store metadata for each element (like field_names for structs)
        value_obj = Value(proto)
        value_obj._element_metadata = []
        for elem in elements:
            metadata = {}
            if elem._field_names is not None:
                metadata['field_names'] = elem._field_names
            value_obj._element_metadata.append(metadata)
        
        return value_obj
    
    @staticmethod
    def struct(fields: dict[str, 'Value']) -> 'Value':
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
        # Note: Struct in proto only stores field values, not names
        # Field names would typically come from the Type definition
        # For now, we'll just store the values in order
        proto_fields = [value.to_proto() for value in fields.values()]
        
        # Create Struct with fields
        struct_proto = types.Value.Struct(field=proto_fields)
        
        # Create Value with struct_value
        proto = types.Value(struct_value=struct_proto)
        
        # Store field names for later retrieval
        value_obj = Value(proto)
        value_obj._field_names = list(fields.keys())
        return value_obj
    
    @staticmethod
    def from_proto(proto: types.Value) -> 'Value':
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
    
    def equals(self, other: 'Value') -> bool:
        """Check equality with another Value.
        
        Args:
            other: Another Value to compare
            
        Returns:
            True if values are equal
        """
        if not isinstance(other, Value):
            return False
        
        # Compare types
        if self.type_kind != other.type_kind:
            return False
        
        # Both NULL
        if self.is_null() and other.is_null():
            return True
        
        # One NULL, one not
        if self.is_null() != other.is_null():
            return False
        
        # Compare values based on type
        if self.type_kind == TypeKind.TYPE_INT64:
            return self.get_int64() == other.get_int64()
        elif self.type_kind == TypeKind.TYPE_STRING:
            return self.get_string() == other.get_string()
        elif self.type_kind == TypeKind.TYPE_BOOL:
            return self.get_bool() == other.get_bool()
        elif self.type_kind == TypeKind.TYPE_DOUBLE:
            return self.get_double() == other.get_double()
        elif self.type_kind == TypeKind.TYPE_INT32:
            return self.get_int32() == other.get_int32()
        elif self.type_kind == TypeKind.TYPE_FLOAT:
            return self.get_float() == other.get_float()
        elif self.type_kind == TypeKind.TYPE_DATE:
            return self.get_date() == other.get_date()
        elif self.type_kind == TypeKind.TYPE_TIMESTAMP:
            return self.get_timestamp() == other.get_timestamp()
        
        # For other types, compare proto directly
        return self._proto == other._proto
    
    def compare_to(self, other: 'Value') -> int:
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
        
        # Compare based on type
        if self.type_kind == TypeKind.TYPE_INT64:
            a, b = self.get_int64(), other.get_int64()
        elif self.type_kind == TypeKind.TYPE_INT32:
            a, b = self.get_int32(), other.get_int32()
        elif self.type_kind == TypeKind.TYPE_DOUBLE:
            a, b = self.get_double(), other.get_double()
        elif self.type_kind == TypeKind.TYPE_FLOAT:
            a, b = self.get_float(), other.get_float()
        elif self.type_kind == TypeKind.TYPE_STRING:
            a, b = self.get_string(), other.get_string()
        elif self.type_kind == TypeKind.TYPE_BOOL:
            a, b = self.get_bool(), other.get_bool()
        elif self.type_kind == TypeKind.TYPE_DATE:
            a, b = self.get_date(), other.get_date()
        elif self.type_kind == TypeKind.TYPE_TIMESTAMP:
            a, b = self.get_timestamp(), other.get_timestamp()
        else:
            raise ValueError(f"Comparison not supported for type {self.type_kind}")
        
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    
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
            # Escape single quotes
            escaped = self.get_string().replace("'", "''")
            return f"'{escaped}'"
        elif self.type_kind == TypeKind.TYPE_BOOL:
            return "TRUE" if self.get_bool() else "FALSE"
        elif self.type_kind == TypeKind.TYPE_INT64:
            return str(self.get_int64())
        elif self.type_kind == TypeKind.TYPE_INT32:
            return str(self.get_int32())
        elif self.type_kind == TypeKind.TYPE_DOUBLE:
            return str(self.get_double())
        elif self.type_kind == TypeKind.TYPE_FLOAT:
            return str(self.get_float())
        elif self.type_kind == TypeKind.TYPE_DATE:
            return f"DATE '{self.get_date().isoformat()}'"
        elif self.type_kind == TypeKind.TYPE_TIMESTAMP:
            return f"TIMESTAMP '{self.get_timestamp().isoformat()}'"
        
        return str(self)
    
    def __str__(self) -> str:
        """String representation of the value.
        
        Returns:
            String representation matching SQL literals
        """
        if self.is_null():
            return "NULL"
        
        if self.type_kind == TypeKind.TYPE_STRING:
            return f'"{self.get_string()}"'
        elif self.type_kind == TypeKind.TYPE_BOOL:
            return "true" if self.get_bool() else "false"
        elif self.type_kind == TypeKind.TYPE_INT64:
            return str(self.get_int64())
        elif self.type_kind == TypeKind.TYPE_INT32:
            return str(self.get_int32())
        elif self.type_kind == TypeKind.TYPE_DOUBLE:
            return str(self.get_double())
        elif self.type_kind == TypeKind.TYPE_FLOAT:
            return str(self.get_float())
        elif self.type_kind == TypeKind.TYPE_DATE:
            return str(self.get_date())
        elif self.type_kind == TypeKind.TYPE_TIMESTAMP:
            return str(self.get_timestamp())
        
        return f"Value({self.type_kind})"
    
    def __repr__(self) -> str:
        """Developer representation."""
        return f"Value({self._proto})"
    
    def get_type(self) -> 'types.Type':
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
    
    def coerce_to(self, target_type: TypeKind) -> 'Value':
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
            # Already the target type
            return self
        
        if self.is_null():
            # NULL values can be coerced to any type
            return Value.null(target_type)
        
        # INT64 coercions
        if self.type_kind == TypeKind.TYPE_INT64:
            if target_type == TypeKind.TYPE_STRING:
                return Value.string(str(self.get_int64()))
            elif target_type == TypeKind.TYPE_DOUBLE:
                return Value.double(float(self.get_int64()))
            elif target_type == TypeKind.TYPE_FLOAT:
                return Value.float_value(float(self.get_int64()))
        
        # INT32 coercions
        elif self.type_kind == TypeKind.TYPE_INT32:
            if target_type == TypeKind.TYPE_INT64:
                return Value.int64(self.get_int32())
            elif target_type == TypeKind.TYPE_STRING:
                return Value.string(str(self.get_int32()))
            elif target_type == TypeKind.TYPE_DOUBLE:
                return Value.double(float(self.get_int32()))
            elif target_type == TypeKind.TYPE_FLOAT:
                return Value.float_value(float(self.get_int32()))
        
        # DOUBLE coercions
        elif self.type_kind == TypeKind.TYPE_DOUBLE:
            if target_type == TypeKind.TYPE_STRING:
                return Value.string(str(self.get_double()))
        
        # FLOAT coercions
        elif self.type_kind == TypeKind.TYPE_FLOAT:
            if target_type == TypeKind.TYPE_DOUBLE:
                return Value.double(self.get_float())
            elif target_type == TypeKind.TYPE_STRING:
                return Value.string(str(self.get_float()))
        
        # BOOL coercions
        elif self.type_kind == TypeKind.TYPE_BOOL:
            if target_type == TypeKind.TYPE_STRING:
                return Value.string("true" if self.get_bool() else "false")
            elif target_type == TypeKind.TYPE_INT64:
                return Value.int64(1 if self.get_bool() else 0)
        
        # STRING coercions (limited)
        elif self.type_kind == TypeKind.TYPE_STRING:
            # String can be coerced to STRING (no-op)
            pass
        
        # DATE coercions
        elif self.type_kind == TypeKind.TYPE_DATE:
            if target_type == TypeKind.TYPE_STRING:
                return Value.string(self.get_date().isoformat())
        
        # TIMESTAMP coercions
        elif self.type_kind == TypeKind.TYPE_TIMESTAMP:
            if target_type == TypeKind.TYPE_STRING:
                return Value.string(self.get_timestamp().isoformat())
        
        raise ValueError(f"Cannot coerce {self.type_kind} to {target_type}")
    
    def cast_to(self, target_type: TypeKind) -> 'Value':
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
            s = self.get_string()
            try:
                if target_type == TypeKind.TYPE_INT64:
                    return Value.int64(int(s))
                elif target_type == TypeKind.TYPE_INT32:
                    return Value.int32(int(s))
                elif target_type == TypeKind.TYPE_DOUBLE:
                    return Value.double(float(s))
                elif target_type == TypeKind.TYPE_FLOAT:
                    return Value.float_value(float(s))
                elif target_type == TypeKind.TYPE_BOOL:
                    # Parse boolean strings
                    if s.lower() in ('true', 't', '1', 'yes'):
                        return Value.bool(True)
                    elif s.lower() in ('false', 'f', '0', 'no'):
                        return Value.bool(False)
                    else:
                        raise ValueError(f"Cannot parse '{s}' as BOOL")
            except (ValueError, OverflowError) as e:
                raise ValueError(f"Cannot cast STRING '{s}' to {target_type}: {e}")
        
        # Numeric casts
        elif self.type_kind in (TypeKind.TYPE_INT64, TypeKind.TYPE_INT32, 
                                 TypeKind.TYPE_DOUBLE, TypeKind.TYPE_FLOAT):
            if self.type_kind == TypeKind.TYPE_INT64:
                val = self.get_int64()
            elif self.type_kind == TypeKind.TYPE_INT32:
                val = self.get_int32()
            elif self.type_kind == TypeKind.TYPE_DOUBLE:
                val = self.get_double()
            else:  # FLOAT
                val = self.get_float()
            
            try:
                if target_type == TypeKind.TYPE_INT64:
                    return Value.int64(int(val))
                elif target_type == TypeKind.TYPE_INT32:
                    return Value.int32(int(val))
                elif target_type == TypeKind.TYPE_DOUBLE:
                    return Value.double(float(val))
                elif target_type == TypeKind.TYPE_FLOAT:
                    return Value.float_value(float(val))
                elif target_type == TypeKind.TYPE_STRING:
                    return Value.string(str(val))
                elif target_type == TypeKind.TYPE_BOOL:
                    return Value.bool(val != 0)
            except (ValueError, OverflowError) as e:
                raise ValueError(f"Cannot cast {self.type_kind} to {target_type}: {e}")
        
        # Try coercion as fallback
        try:
            return self.coerce_to(target_type)
        except ValueError:
            raise ValueError(f"Cannot cast {self.type_kind} to {target_type}")
