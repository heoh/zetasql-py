from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluatorTableIteratorProto(_message.Message):
    __slots__ = ("location_byte_offset", "next_row_count")
    LOCATION_BYTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NEXT_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    location_byte_offset: int
    next_row_count: int
    def __init__(self, location_byte_offset: _Optional[int] = ..., next_row_count: _Optional[int] = ...) -> None: ...
