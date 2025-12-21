from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleValueProto(_message.Message):
    __slots__ = ("int64_value", "string_value", "bool_value", "double_value", "bytes_value", "__SimpleValueProto__switch_must_have_a_default")
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    __SIMPLEVALUEPROTO__SWITCH_MUST_HAVE_A_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    string_value: str
    bool_value: bool
    double_value: float
    bytes_value: bytes
    __SimpleValueProto__switch_must_have_a_default: bool
    def __init__(self, int64_value: _Optional[int] = ..., string_value: _Optional[str] = ..., bool_value: bool = ..., double_value: _Optional[float] = ..., bytes_value: _Optional[bytes] = ..., __SimpleValueProto__switch_must_have_a_default: bool = ...) -> None: ...
