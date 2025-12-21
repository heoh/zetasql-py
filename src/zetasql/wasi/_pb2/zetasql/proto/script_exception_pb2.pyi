from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptException(_message.Message):
    __slots__ = ("message", "internal")
    Extensions: _python_message._ExtensionDict
    class StackTraceFrame(_message.Message):
        __slots__ = ("line", "column", "filename", "location")
        LINE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        line: int
        column: int
        filename: str
        location: str
        def __init__(self, line: _Optional[int] = ..., column: _Optional[int] = ..., filename: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...
    class Internal(_message.Message):
        __slots__ = ("statement_text", "stack_trace")
        STATEMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
        STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
        statement_text: str
        stack_trace: _containers.RepeatedCompositeFieldContainer[ScriptException.StackTraceFrame]
        def __init__(self, statement_text: _Optional[str] = ..., stack_trace: _Optional[_Iterable[_Union[ScriptException.StackTraceFrame, _Mapping]]] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    message: str
    internal: ScriptException.Internal
    def __init__(self, message: _Optional[str] = ..., internal: _Optional[_Union[ScriptException.Internal, _Mapping]] = ...) -> None: ...
