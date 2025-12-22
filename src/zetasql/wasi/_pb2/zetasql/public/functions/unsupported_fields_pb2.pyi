from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class UnsupportedFieldsEnum(_message.Message):
    __slots__ = ()
    class UnsupportedFields(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSUPPORTED_FIELDS_INVALID: _ClassVar[UnsupportedFieldsEnum.UnsupportedFields]
        FAIL: _ClassVar[UnsupportedFieldsEnum.UnsupportedFields]
        IGNORE: _ClassVar[UnsupportedFieldsEnum.UnsupportedFields]
        PLACEHOLDER: _ClassVar[UnsupportedFieldsEnum.UnsupportedFields]
    UNSUPPORTED_FIELDS_INVALID: UnsupportedFieldsEnum.UnsupportedFields
    FAIL: UnsupportedFieldsEnum.UnsupportedFields
    IGNORE: UnsupportedFieldsEnum.UnsupportedFields
    PLACEHOLDER: UnsupportedFieldsEnum.UnsupportedFields
    def __init__(self) -> None: ...
