from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorLocation(_message.Message):
    __slots__ = ("line", "column", "filename", "input_start_line_offset", "input_start_column_offset", "error_source")
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_START_LINE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INPUT_START_COLUMN_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ERROR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    line: int
    column: int
    filename: str
    input_start_line_offset: int
    input_start_column_offset: int
    error_source: _containers.RepeatedCompositeFieldContainer[ErrorSource]
    def __init__(self, line: _Optional[int] = ..., column: _Optional[int] = ..., filename: _Optional[str] = ..., input_start_line_offset: _Optional[int] = ..., input_start_column_offset: _Optional[int] = ..., error_source: _Optional[_Iterable[_Union[ErrorSource, _Mapping]]] = ...) -> None: ...

class ErrorSource(_message.Message):
    __slots__ = ("error_message", "error_message_caret_string", "error_location")
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_CARET_STRING_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOCATION_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    error_message_caret_string: str
    error_location: ErrorLocation
    def __init__(self, error_message: _Optional[str] = ..., error_message_caret_string: _Optional[str] = ..., error_location: _Optional[_Union[ErrorLocation, _Mapping]] = ...) -> None: ...
