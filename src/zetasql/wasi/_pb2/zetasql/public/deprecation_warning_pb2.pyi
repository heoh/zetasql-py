from zetasql.wasi._pb2.zetasql.public import error_location_pb2 as _error_location_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeprecationWarning(_message.Message):
    __slots__ = ("kind",)
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        __Kind__switch_must_have_a_default__: _ClassVar[DeprecationWarning.Kind]
        UNKNOWN: _ClassVar[DeprecationWarning.Kind]
        DEPRECATED_FUNCTION: _ClassVar[DeprecationWarning.Kind]
        DEPRECATED_FUNCTION_SIGNATURE: _ClassVar[DeprecationWarning.Kind]
        PROTO3_FIELD_PRESENCE: _ClassVar[DeprecationWarning.Kind]
        QUERY_TOO_COMPLEX: _ClassVar[DeprecationWarning.Kind]
        DEPRECATED_ANONYMIZATION_OPTION_KAPPA: _ClassVar[DeprecationWarning.Kind]
        PIVOT_OR_UNPIVOT_ON_ARRAY_SCAN: _ClassVar[DeprecationWarning.Kind]
        TABLE_SYNTAX_ARGUMENT_RESOLUTION_ORDER: _ClassVar[DeprecationWarning.Kind]
        PIPE_WINDOW: _ClassVar[DeprecationWarning.Kind]
        RESERVED_KEYWORD: _ClassVar[DeprecationWarning.Kind]
        LEGACY_FUNCTION_OPTIONS_PLACEMENT: _ClassVar[DeprecationWarning.Kind]
        LATERAL_COLUMN_REFERENCE: _ClassVar[DeprecationWarning.Kind]
    __Kind__switch_must_have_a_default__: DeprecationWarning.Kind
    UNKNOWN: DeprecationWarning.Kind
    DEPRECATED_FUNCTION: DeprecationWarning.Kind
    DEPRECATED_FUNCTION_SIGNATURE: DeprecationWarning.Kind
    PROTO3_FIELD_PRESENCE: DeprecationWarning.Kind
    QUERY_TOO_COMPLEX: DeprecationWarning.Kind
    DEPRECATED_ANONYMIZATION_OPTION_KAPPA: DeprecationWarning.Kind
    PIVOT_OR_UNPIVOT_ON_ARRAY_SCAN: DeprecationWarning.Kind
    TABLE_SYNTAX_ARGUMENT_RESOLUTION_ORDER: DeprecationWarning.Kind
    PIPE_WINDOW: DeprecationWarning.Kind
    RESERVED_KEYWORD: DeprecationWarning.Kind
    LEGACY_FUNCTION_OPTIONS_PLACEMENT: DeprecationWarning.Kind
    LATERAL_COLUMN_REFERENCE: DeprecationWarning.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    kind: DeprecationWarning.Kind
    def __init__(self, kind: _Optional[_Union[DeprecationWarning.Kind, str]] = ...) -> None: ...

class FreestandingDeprecationWarning(_message.Message):
    __slots__ = ("message", "caret_string", "error_location", "deprecation_warning")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CARET_STRING_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_WARNING_FIELD_NUMBER: _ClassVar[int]
    message: str
    caret_string: str
    error_location: _error_location_pb2.ErrorLocation
    deprecation_warning: DeprecationWarning
    def __init__(self, message: _Optional[str] = ..., caret_string: _Optional[str] = ..., error_location: _Optional[_Union[_error_location_pb2.ErrorLocation, _Mapping]] = ..., deprecation_warning: _Optional[_Union[DeprecationWarning, _Mapping]] = ...) -> None: ...
