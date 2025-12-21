from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ParseResumeLocationProto(_message.Message):
    __slots__ = ("filename", "input", "byte_position", "allow_resume")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    BYTE_POSITION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RESUME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    input: str
    byte_position: int
    allow_resume: bool
    def __init__(self, filename: _Optional[str] = ..., input: _Optional[str] = ..., byte_position: _Optional[int] = ..., allow_resume: bool = ...) -> None: ...
