from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RangeSessionizeEnums(_message.Message):
    __slots__ = ()
    class RangeSessionizeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RANGE_SESSIONIZE_MODE_INVALID: _ClassVar[RangeSessionizeEnums.RangeSessionizeMode]
        OVERLAPS: _ClassVar[RangeSessionizeEnums.RangeSessionizeMode]
        MEETS: _ClassVar[RangeSessionizeEnums.RangeSessionizeMode]
    RANGE_SESSIONIZE_MODE_INVALID: RangeSessionizeEnums.RangeSessionizeMode
    OVERLAPS: RangeSessionizeEnums.RangeSessionizeMode
    MEETS: RangeSessionizeEnums.RangeSessionizeMode
    def __init__(self) -> None: ...
