"""
TypeKind Enum - Type-safe wrapper for ZetaSQL TypeKind

This module provides a Pythonic IntEnum wrapper around the protobuf TypeKind enum,
maintaining full backward compatibility while adding type safety and helper methods.
"""

from enum import IntEnum
from zetasql.wasi._pb2.zetasql.public import type_pb2


class TypeKind(IntEnum):
    """
    Type-safe wrapper for ZetaSQL TypeKind constants.
    
    This enum provides IDE autocomplete, type checking, and helper methods
    while maintaining full backward compatibility with proto TypeKind integers.
    
    Examples:
        >>> TypeKind.TYPE_INT64
        <TypeKind.TYPE_INT64: 2>
        >>> TypeKind.TYPE_INT64 == 2
        True
        >>> TypeKind.TYPE_INT64.is_integer()
        True
    """
    
    # Map directly to proto values
    TYPE_UNKNOWN = type_pb2.TYPE_UNKNOWN  # 0
    TYPE_INT32 = type_pb2.TYPE_INT32  # 1
    TYPE_INT64 = type_pb2.TYPE_INT64  # 2
    TYPE_UINT32 = type_pb2.TYPE_UINT32  # 3
    TYPE_UINT64 = type_pb2.TYPE_UINT64  # 4
    TYPE_BOOL = type_pb2.TYPE_BOOL  # 5
    TYPE_FLOAT = type_pb2.TYPE_FLOAT  # 6
    TYPE_DOUBLE = type_pb2.TYPE_DOUBLE  # 7
    TYPE_STRING = type_pb2.TYPE_STRING  # 8
    TYPE_BYTES = type_pb2.TYPE_BYTES  # 9
    TYPE_DATE = type_pb2.TYPE_DATE  # 10
    TYPE_ENUM = type_pb2.TYPE_ENUM  # 15
    TYPE_ARRAY = type_pb2.TYPE_ARRAY  # 16
    TYPE_STRUCT = type_pb2.TYPE_STRUCT  # 17
    TYPE_PROTO = type_pb2.TYPE_PROTO  # 18
    TYPE_TIMESTAMP = type_pb2.TYPE_TIMESTAMP  # 19
    TYPE_TIME = type_pb2.TYPE_TIME  # 20
    TYPE_DATETIME = type_pb2.TYPE_DATETIME  # 21
    TYPE_GEOGRAPHY = type_pb2.TYPE_GEOGRAPHY  # 22
    TYPE_NUMERIC = type_pb2.TYPE_NUMERIC  # 23
    TYPE_BIGNUMERIC = type_pb2.TYPE_BIGNUMERIC  # 24
    TYPE_EXTENDED = type_pb2.TYPE_EXTENDED  # 25
    TYPE_JSON = type_pb2.TYPE_JSON  # 26
    TYPE_INTERVAL = type_pb2.TYPE_INTERVAL  # 27
    TYPE_TOKENLIST = type_pb2.TYPE_TOKENLIST  # 28
    TYPE_RANGE = type_pb2.TYPE_RANGE  # 29
    TYPE_GRAPH_ELEMENT = type_pb2.TYPE_GRAPH_ELEMENT  # 30
    TYPE_MAP = type_pb2.TYPE_MAP  # 31
    TYPE_UUID = type_pb2.TYPE_UUID  # 32
    TYPE_GRAPH_PATH = type_pb2.TYPE_GRAPH_PATH  # 33
    TYPE_MEASURE = type_pb2.TYPE_MEASURE  # 34
    TYPE_ROW = type_pb2.TYPE_ROW  # 36
    
    def is_simple(self) -> bool:
        """Returns true if this is a simple (non-composite) type."""
        return self not in (
            TypeKind.TYPE_ARRAY,
            TypeKind.TYPE_STRUCT,
            TypeKind.TYPE_PROTO,
            TypeKind.TYPE_ENUM,
            TypeKind.TYPE_RANGE,
            TypeKind.TYPE_MAP,
            TypeKind.TYPE_GRAPH_ELEMENT,
            TypeKind.TYPE_GRAPH_PATH,
            TypeKind.TYPE_MEASURE,
        )
    
    def is_integer(self) -> bool:
        """Returns true for any integer type (signed or unsigned)."""
        return self in (
            TypeKind.TYPE_INT32,
            TypeKind.TYPE_INT64,
            TypeKind.TYPE_UINT32,
            TypeKind.TYPE_UINT64,
        )
    
    def is_signed_integer(self) -> bool:
        """Returns true for signed integer types."""
        return self in (TypeKind.TYPE_INT32, TypeKind.TYPE_INT64)
    
    def is_unsigned_integer(self) -> bool:
        """Returns true for unsigned integer types."""
        return self in (TypeKind.TYPE_UINT32, TypeKind.TYPE_UINT64)
    
    def is_floating_point(self) -> bool:
        """Returns true for floating point types."""
        return self in (TypeKind.TYPE_FLOAT, TypeKind.TYPE_DOUBLE)
    
    def is_numerical(self) -> bool:
        """Returns true for any numeric type (integer, float, or decimal)."""
        return self.is_integer() or self.is_floating_point() or \
               self in (TypeKind.TYPE_NUMERIC, TypeKind.TYPE_BIGNUMERIC)
    
    def is_temporal(self) -> bool:
        """Returns true for date/time types."""
        return self in (
            TypeKind.TYPE_DATE,
            TypeKind.TYPE_TIME,
            TypeKind.TYPE_DATETIME,
            TypeKind.TYPE_TIMESTAMP,
            TypeKind.TYPE_INTERVAL,
        )
    
    def is_composite(self) -> bool:
        """Returns true for composite types (array, struct, map, etc)."""
        return not self.is_simple()
    
    @classmethod
    def from_proto(cls, value: int) -> 'TypeKind':
        """Convert proto TypeKind integer to TypeKind enum.
        
        Args:
            value: Integer value from proto TypeKind
            
        Returns:
            TypeKind enum member
            
        Example:
            >>> TypeKind.from_proto(2)
            <TypeKind.TYPE_INT64: 2>
        """
        return cls(value)
    
    def to_proto(self) -> int:
        """Convert TypeKind enum to proto integer.
        
        Returns:
            Integer value compatible with proto TypeKind
            
        Example:
            >>> TypeKind.TYPE_INT64.to_proto()
            2
        """
        return self.value


__all__ = ['TypeKind']
