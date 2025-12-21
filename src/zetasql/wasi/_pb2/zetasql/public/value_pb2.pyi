import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueProto(_message.Message):
    __slots__ = ("int32_value", "int64_value", "uint32_value", "uint64_value", "bool_value", "float_value", "double_value", "string_value", "bytes_value", "date_value", "enum_value", "array_value", "struct_value", "proto_value", "timestamp_value", "timestamp_pico_value", "timestamp_picos_value", "datetime_value", "time_value", "geography_value", "numeric_value", "bignumeric_value", "json_value", "interval_value", "tokenlist_value", "range_value", "uuid_value", "map_value", "__ValueProto__switch_must_have_a_default")
    class Array(_message.Message):
        __slots__ = ("element",)
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        element: _containers.RepeatedCompositeFieldContainer[ValueProto]
        def __init__(self, element: _Optional[_Iterable[_Union[ValueProto, _Mapping]]] = ...) -> None: ...
    class Struct(_message.Message):
        __slots__ = ("field",)
        FIELD_FIELD_NUMBER: _ClassVar[int]
        field: _containers.RepeatedCompositeFieldContainer[ValueProto]
        def __init__(self, field: _Optional[_Iterable[_Union[ValueProto, _Mapping]]] = ...) -> None: ...
    class Datetime(_message.Message):
        __slots__ = ("bit_field_datetime_seconds", "nanos")
        BIT_FIELD_DATETIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
        NANOS_FIELD_NUMBER: _ClassVar[int]
        bit_field_datetime_seconds: int
        nanos: int
        def __init__(self, bit_field_datetime_seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...
    class Range(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: ValueProto
        end: ValueProto
        def __init__(self, start: _Optional[_Union[ValueProto, _Mapping]] = ..., end: _Optional[_Union[ValueProto, _Mapping]] = ...) -> None: ...
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: ValueProto
        value: ValueProto
        def __init__(self, key: _Optional[_Union[ValueProto, _Mapping]] = ..., value: _Optional[_Union[ValueProto, _Mapping]] = ...) -> None: ...
    class Map(_message.Message):
        __slots__ = ("entry",)
        ENTRY_FIELD_NUMBER: _ClassVar[int]
        entry: _containers.RepeatedCompositeFieldContainer[ValueProto.MapEntry]
        def __init__(self, entry: _Optional[_Iterable[_Union[ValueProto.MapEntry, _Mapping]]] = ...) -> None: ...
    class TimestampPicos(_message.Message):
        __slots__ = ("seconds", "picos")
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        PICOS_FIELD_NUMBER: _ClassVar[int]
        seconds: int
        picos: int
        def __init__(self, seconds: _Optional[int] = ..., picos: _Optional[int] = ...) -> None: ...
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PROTO_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_PICO_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_PICOS_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    GEOGRAPHY_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    BIGNUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    JSON_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOKENLIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    UUID_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    __VALUEPROTO__SWITCH_MUST_HAVE_A_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    int32_value: int
    int64_value: int
    uint32_value: int
    uint64_value: int
    bool_value: bool
    float_value: float
    double_value: float
    string_value: str
    bytes_value: bytes
    date_value: int
    enum_value: int
    array_value: ValueProto.Array
    struct_value: ValueProto.Struct
    proto_value: bytes
    timestamp_value: _timestamp_pb2.Timestamp
    timestamp_pico_value: bytes
    timestamp_picos_value: ValueProto.TimestampPicos
    datetime_value: ValueProto.Datetime
    time_value: int
    geography_value: bytes
    numeric_value: bytes
    bignumeric_value: bytes
    json_value: str
    interval_value: bytes
    tokenlist_value: bytes
    range_value: ValueProto.Range
    uuid_value: bytes
    map_value: ValueProto.Map
    __ValueProto__switch_must_have_a_default: bool
    def __init__(self, int32_value: _Optional[int] = ..., int64_value: _Optional[int] = ..., uint32_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., bool_value: bool = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ..., date_value: _Optional[int] = ..., enum_value: _Optional[int] = ..., array_value: _Optional[_Union[ValueProto.Array, _Mapping]] = ..., struct_value: _Optional[_Union[ValueProto.Struct, _Mapping]] = ..., proto_value: _Optional[bytes] = ..., timestamp_value: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., timestamp_pico_value: _Optional[bytes] = ..., timestamp_picos_value: _Optional[_Union[ValueProto.TimestampPicos, _Mapping]] = ..., datetime_value: _Optional[_Union[ValueProto.Datetime, _Mapping]] = ..., time_value: _Optional[int] = ..., geography_value: _Optional[bytes] = ..., numeric_value: _Optional[bytes] = ..., bignumeric_value: _Optional[bytes] = ..., json_value: _Optional[str] = ..., interval_value: _Optional[bytes] = ..., tokenlist_value: _Optional[bytes] = ..., range_value: _Optional[_Union[ValueProto.Range, _Mapping]] = ..., uuid_value: _Optional[bytes] = ..., map_value: _Optional[_Union[ValueProto.Map, _Mapping]] = ..., __ValueProto__switch_must_have_a_default: bool = ...) -> None: ...
