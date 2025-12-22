from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BitwiseAggEnums(_message.Message):
    __slots__ = ()
    class BitwiseAggMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BITWISE_AGG_MODE_INVALID: _ClassVar[BitwiseAggEnums.BitwiseAggMode]
        STRICT: _ClassVar[BitwiseAggEnums.BitwiseAggMode]
        PAD: _ClassVar[BitwiseAggEnums.BitwiseAggMode]
    BITWISE_AGG_MODE_INVALID: BitwiseAggEnums.BitwiseAggMode
    STRICT: BitwiseAggEnums.BitwiseAggMode
    PAD: BitwiseAggEnums.BitwiseAggMode
    def __init__(self) -> None: ...
