from zetasql.wasi._pb2.zetasql.public import error_location_pb2 as _error_location_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FixRange(_message.Message):
    __slots__ = ("start", "length")
    START_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    start: _error_location_pb2.ErrorLocation
    length: int
    def __init__(self, start: _Optional[_Union[_error_location_pb2.ErrorLocation, _Mapping]] = ..., length: _Optional[int] = ...) -> None: ...

class TextEdit(_message.Message):
    __slots__ = ("range", "new_text")
    RANGE_FIELD_NUMBER: _ClassVar[int]
    NEW_TEXT_FIELD_NUMBER: _ClassVar[int]
    range: FixRange
    new_text: str
    def __init__(self, range: _Optional[_Union[FixRange, _Mapping]] = ..., new_text: _Optional[str] = ...) -> None: ...

class Edits(_message.Message):
    __slots__ = ("text_edits",)
    TEXT_EDITS_FIELD_NUMBER: _ClassVar[int]
    text_edits: _containers.RepeatedCompositeFieldContainer[TextEdit]
    def __init__(self, text_edits: _Optional[_Iterable[_Union[TextEdit, _Mapping]]] = ...) -> None: ...

class Fix(_message.Message):
    __slots__ = ("title", "edits")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EDITS_FIELD_NUMBER: _ClassVar[int]
    title: str
    edits: Edits
    def __init__(self, title: _Optional[str] = ..., edits: _Optional[_Union[Edits, _Mapping]] = ...) -> None: ...

class ErrorFixSuggestions(_message.Message):
    __slots__ = ("fix_suggestions",)
    FIX_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    fix_suggestions: _containers.RepeatedCompositeFieldContainer[Fix]
    def __init__(self, fix_suggestions: _Optional[_Iterable[_Union[Fix, _Mapping]]] = ...) -> None: ...
