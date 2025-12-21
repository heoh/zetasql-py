from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleSequenceProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...
