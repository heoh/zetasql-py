from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ParseLocationRangeProto(_message.Message):
    __slots__ = ("filename", "start", "end")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    filename: str
    start: int
    end: int
    def __init__(self, filename: _Optional[str] = ..., start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
