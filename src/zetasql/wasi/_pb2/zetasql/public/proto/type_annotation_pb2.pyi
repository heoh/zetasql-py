from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
FORMAT_FIELD_NUMBER: _ClassVar[int]
format: _descriptor.FieldDescriptor
TYPE_FIELD_NUMBER: _ClassVar[int]
type: _descriptor.FieldDescriptor
ENCODING_FIELD_NUMBER: _ClassVar[int]
encoding: _descriptor.FieldDescriptor
USE_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
use_defaults: _descriptor.FieldDescriptor
USE_FIELD_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
use_field_defaults: _descriptor.FieldDescriptor

class FieldFormat(_message.Message):
    __slots__ = ()
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_FORMAT: _ClassVar[FieldFormat.Format]
        DATE: _ClassVar[FieldFormat.Format]
        TIMESTAMP_SECONDS: _ClassVar[FieldFormat.Format]
        TIMESTAMP_MILLIS: _ClassVar[FieldFormat.Format]
        TIMESTAMP_MICROS: _ClassVar[FieldFormat.Format]
        TIMESTAMP_NANOS: _ClassVar[FieldFormat.Format]
        TIMESTAMP_PICOS: _ClassVar[FieldFormat.Format]
        TIMESTAMP: _ClassVar[FieldFormat.Format]
        DATE_DECIMAL: _ClassVar[FieldFormat.Format]
        TIME_MICROS: _ClassVar[FieldFormat.Format]
        DATETIME_MICROS: _ClassVar[FieldFormat.Format]
        ST_GEOGRAPHY_ENCODED: _ClassVar[FieldFormat.Format]
        NUMERIC: _ClassVar[FieldFormat.Format]
        BIGNUMERIC: _ClassVar[FieldFormat.Format]
        JSON: _ClassVar[FieldFormat.Format]
        INTERVAL: _ClassVar[FieldFormat.Format]
        TOKENLIST: _ClassVar[FieldFormat.Format]
        RANGE_DATES_ENCODED: _ClassVar[FieldFormat.Format]
        RANGE_DATETIMES_ENCODED: _ClassVar[FieldFormat.Format]
        RANGE_TIMESTAMPS_ENCODED: _ClassVar[FieldFormat.Format]
        UUID: _ClassVar[FieldFormat.Format]
        __FieldFormat_Type__switch_must_have_a_default__: _ClassVar[FieldFormat.Format]
    DEFAULT_FORMAT: FieldFormat.Format
    DATE: FieldFormat.Format
    TIMESTAMP_SECONDS: FieldFormat.Format
    TIMESTAMP_MILLIS: FieldFormat.Format
    TIMESTAMP_MICROS: FieldFormat.Format
    TIMESTAMP_NANOS: FieldFormat.Format
    TIMESTAMP_PICOS: FieldFormat.Format
    TIMESTAMP: FieldFormat.Format
    DATE_DECIMAL: FieldFormat.Format
    TIME_MICROS: FieldFormat.Format
    DATETIME_MICROS: FieldFormat.Format
    ST_GEOGRAPHY_ENCODED: FieldFormat.Format
    NUMERIC: FieldFormat.Format
    BIGNUMERIC: FieldFormat.Format
    JSON: FieldFormat.Format
    INTERVAL: FieldFormat.Format
    TOKENLIST: FieldFormat.Format
    RANGE_DATES_ENCODED: FieldFormat.Format
    RANGE_DATETIMES_ENCODED: FieldFormat.Format
    RANGE_TIMESTAMPS_ENCODED: FieldFormat.Format
    UUID: FieldFormat.Format
    __FieldFormat_Type__switch_must_have_a_default__: FieldFormat.Format
    def __init__(self) -> None: ...

class DeprecatedEncoding(_message.Message):
    __slots__ = ()
    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_ENCODING: _ClassVar[DeprecatedEncoding.Encoding]
        DATE_DECIMAL: _ClassVar[DeprecatedEncoding.Encoding]
        DATE_PACKED32: _ClassVar[DeprecatedEncoding.Encoding]
        __FieldFormat_Encoding__switch_must_have_a_default__: _ClassVar[DeprecatedEncoding.Encoding]
    DEFAULT_ENCODING: DeprecatedEncoding.Encoding
    DATE_DECIMAL: DeprecatedEncoding.Encoding
    DATE_PACKED32: DeprecatedEncoding.Encoding
    __FieldFormat_Encoding__switch_must_have_a_default__: DeprecatedEncoding.Encoding
    def __init__(self) -> None: ...
