from zetasql.wasi._pb2.zetasql.proto import internal_error_location_pb2 as _internal_error_location_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InternalFixRange(_message.Message):
    __slots__ = ("start", "length")
    START_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    start: _internal_error_location_pb2.InternalErrorLocation
    length: int
    def __init__(self, start: _Optional[_Union[_internal_error_location_pb2.InternalErrorLocation, _Mapping]] = ..., length: _Optional[int] = ...) -> None: ...

class InternalTextEdit(_message.Message):
    __slots__ = ("range", "new_text")
    RANGE_FIELD_NUMBER: _ClassVar[int]
    NEW_TEXT_FIELD_NUMBER: _ClassVar[int]
    range: InternalFixRange
    new_text: str
    def __init__(self, range: _Optional[_Union[InternalFixRange, _Mapping]] = ..., new_text: _Optional[str] = ...) -> None: ...

class InternalEdits(_message.Message):
    __slots__ = ("text_edits",)
    TEXT_EDITS_FIELD_NUMBER: _ClassVar[int]
    text_edits: _containers.RepeatedCompositeFieldContainer[InternalTextEdit]
    def __init__(self, text_edits: _Optional[_Iterable[_Union[InternalTextEdit, _Mapping]]] = ...) -> None: ...

class InternalFix(_message.Message):
    __slots__ = ("title", "edits")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EDITS_FIELD_NUMBER: _ClassVar[int]
    title: str
    edits: InternalEdits
    def __init__(self, title: _Optional[str] = ..., edits: _Optional[_Union[InternalEdits, _Mapping]] = ...) -> None: ...

class InternalErrorFixSuggestions(_message.Message):
    __slots__ = ("fix_suggestions",)
    FIX_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    fix_suggestions: _containers.RepeatedCompositeFieldContainer[InternalFix]
    def __init__(self, fix_suggestions: _Optional[_Iterable[_Union[InternalFix, _Mapping]]] = ...) -> None: ...
