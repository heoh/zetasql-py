from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RoundingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUNDING_MODE_UNSPECIFIED: _ClassVar[RoundingMode]
    ROUND_HALF_AWAY_FROM_ZERO: _ClassVar[RoundingMode]
    ROUND_HALF_EVEN: _ClassVar[RoundingMode]
ROUNDING_MODE_UNSPECIFIED: RoundingMode
ROUND_HALF_AWAY_FROM_ZERO: RoundingMode
ROUND_HALF_EVEN: RoundingMode
