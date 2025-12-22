from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArrayZipEnums(_message.Message):
    __slots__ = ()
    class ArrayZipMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARRAY_ZIP_MODE_INVALID: _ClassVar[ArrayZipEnums.ArrayZipMode]
        PAD: _ClassVar[ArrayZipEnums.ArrayZipMode]
        TRUNCATE: _ClassVar[ArrayZipEnums.ArrayZipMode]
        STRICT: _ClassVar[ArrayZipEnums.ArrayZipMode]
    ARRAY_ZIP_MODE_INVALID: ArrayZipEnums.ArrayZipMode
    PAD: ArrayZipEnums.ArrayZipMode
    TRUNCATE: ArrayZipEnums.ArrayZipMode
    STRICT: ArrayZipEnums.ArrayZipMode
    def __init__(self) -> None: ...
