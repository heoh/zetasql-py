from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArrayFindEnums(_message.Message):
    __slots__ = ()
    class ArrayFindMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARRAY_FIND_MODE_INVALID: _ClassVar[ArrayFindEnums.ArrayFindMode]
        FIRST: _ClassVar[ArrayFindEnums.ArrayFindMode]
        LAST: _ClassVar[ArrayFindEnums.ArrayFindMode]
    ARRAY_FIND_MODE_INVALID: ArrayFindEnums.ArrayFindMode
    FIRST: ArrayFindEnums.ArrayFindMode
    LAST: ArrayFindEnums.ArrayFindMode
    def __init__(self) -> None: ...
