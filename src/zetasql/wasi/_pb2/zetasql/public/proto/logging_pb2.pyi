import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionStats(_message.Message):
    __slots__ = ("wall_time", "cpu_time", "stack_available_bytes", "stack_peak_used_bytes")
    class ParserVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARSER_UNSPECIFIED: _ClassVar[ExecutionStats.ParserVariant]
        PARSER_BISON: _ClassVar[ExecutionStats.ParserVariant]
        PARSER_TEXTMAPPER: _ClassVar[ExecutionStats.ParserVariant]
    PARSER_UNSPECIFIED: ExecutionStats.ParserVariant
    PARSER_BISON: ExecutionStats.ParserVariant
    PARSER_TEXTMAPPER: ExecutionStats.ParserVariant
    WALL_TIME_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_FIELD_NUMBER: _ClassVar[int]
    STACK_AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STACK_PEAK_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    wall_time: _duration_pb2.Duration
    cpu_time: _duration_pb2.Duration
    stack_available_bytes: int
    stack_peak_used_bytes: int
    def __init__(self, wall_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., cpu_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., stack_available_bytes: _Optional[int] = ..., stack_peak_used_bytes: _Optional[int] = ...) -> None: ...

class AnalyzerLogEntry(_message.Message):
    __slots__ = ("num_lexical_tokens", "overall_execution_stats", "execution_stats_by_op")
    class LoggedOperationCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_LOGGED_OPERATION_CATEGORY: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
        PARSER: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
        RESOLVER: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
        REWRITER: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
        CATALOG_RESOLVER: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
        VALIDATOR: _ClassVar[AnalyzerLogEntry.LoggedOperationCategory]
    UNKNOWN_LOGGED_OPERATION_CATEGORY: AnalyzerLogEntry.LoggedOperationCategory
    PARSER: AnalyzerLogEntry.LoggedOperationCategory
    RESOLVER: AnalyzerLogEntry.LoggedOperationCategory
    REWRITER: AnalyzerLogEntry.LoggedOperationCategory
    CATALOG_RESOLVER: AnalyzerLogEntry.LoggedOperationCategory
    VALIDATOR: AnalyzerLogEntry.LoggedOperationCategory
    class ExecutionStatsByOpEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: AnalyzerLogEntry.LoggedOperationCategory
        value: ExecutionStats
        def __init__(self, key: _Optional[_Union[AnalyzerLogEntry.LoggedOperationCategory, str]] = ..., value: _Optional[_Union[ExecutionStats, _Mapping]] = ...) -> None: ...
    NUM_LEXICAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OVERALL_EXECUTION_STATS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATS_BY_OP_FIELD_NUMBER: _ClassVar[int]
    num_lexical_tokens: int
    overall_execution_stats: ExecutionStats
    execution_stats_by_op: _containers.RepeatedCompositeFieldContainer[AnalyzerLogEntry.ExecutionStatsByOpEntry]
    def __init__(self, num_lexical_tokens: _Optional[int] = ..., overall_execution_stats: _Optional[_Union[ExecutionStats, _Mapping]] = ..., execution_stats_by_op: _Optional[_Iterable[_Union[AnalyzerLogEntry.ExecutionStatsByOpEntry, _Mapping]]] = ...) -> None: ...
