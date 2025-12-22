from zetasql.wasi._pb2.zetasql.public import error_location_pb2 as _error_location_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalErrorLocation(_message.Message):
    __slots__ = ("byte_offset", "filename", "error_source")
    BYTE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    byte_offset: int
    filename: str
    error_source: _containers.RepeatedCompositeFieldContainer[_error_location_pb2.ErrorSource]
    def __init__(self, byte_offset: _Optional[int] = ..., filename: _Optional[str] = ..., error_source: _Optional[_Iterable[_Union[_error_location_pb2.ErrorSource, _Mapping]]] = ...) -> None: ...
