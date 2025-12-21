from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchResultProto(_message.Message):
    __slots__ = ("match", "rep_count")
    MATCH_FIELD_NUMBER: _ClassVar[int]
    REP_COUNT_FIELD_NUMBER: _ClassVar[int]
    match: _containers.RepeatedScalarFieldContainer[str]
    rep_count: int
    def __init__(self, match: _Optional[_Iterable[str]] = ..., rep_count: _Optional[int] = ...) -> None: ...

class MatchPartitionResultProto(_message.Message):
    __slots__ = ("add_row", "finalize")
    ADD_ROW_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    add_row: _containers.RepeatedCompositeFieldContainer[MatchResultProto]
    finalize: MatchResultProto
    def __init__(self, add_row: _Optional[_Iterable[_Union[MatchResultProto, _Mapping]]] = ..., finalize: _Optional[_Union[MatchResultProto, _Mapping]] = ...) -> None: ...
