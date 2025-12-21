from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KnownErrorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[KnownErrorMode]
    ALLOW_UNIMPLEMENTED: _ClassVar[KnownErrorMode]
    ALLOW_ERROR: _ClassVar[KnownErrorMode]
    ALLOW_ERROR_OR_WRONG_ANSWER: _ClassVar[KnownErrorMode]
    CRASHES_DO_NOT_RUN: _ClassVar[KnownErrorMode]
NONE: KnownErrorMode
ALLOW_UNIMPLEMENTED: KnownErrorMode
ALLOW_ERROR: KnownErrorMode
ALLOW_ERROR_OR_WRONG_ANSWER: KnownErrorMode
CRASHES_DO_NOT_RUN: KnownErrorMode

class KnownErrorEntry(_message.Message):
    __slots__ = ("mode", "reason", "label")
    MODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    mode: KnownErrorMode
    reason: str
    label: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mode: _Optional[_Union[KnownErrorMode, str]] = ..., reason: _Optional[str] = ..., label: _Optional[_Iterable[str]] = ...) -> None: ...

class KnownErrorFile(_message.Message):
    __slots__ = ("contact_email", "known_errors")
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    KNOWN_ERRORS_FIELD_NUMBER: _ClassVar[int]
    contact_email: _containers.RepeatedScalarFieldContainer[str]
    known_errors: _containers.RepeatedCompositeFieldContainer[KnownErrorEntry]
    def __init__(self, contact_email: _Optional[_Iterable[str]] = ..., known_errors: _Optional[_Iterable[_Union[KnownErrorEntry, _Mapping]]] = ...) -> None: ...
