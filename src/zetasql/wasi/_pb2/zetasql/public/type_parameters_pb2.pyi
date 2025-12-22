from zetasql.wasi._pb2.zetasql.public import simple_value_pb2 as _simple_value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypeParametersProto(_message.Message):
    __slots__ = ("string_type_parameters", "numeric_type_parameters", "extended_type_parameters", "timestamp_type_parameters", "child_list")
    STRING_TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CHILD_LIST_FIELD_NUMBER: _ClassVar[int]
    string_type_parameters: StringTypeParametersProto
    numeric_type_parameters: NumericTypeParametersProto
    extended_type_parameters: ExtendedTypeParametersProto
    timestamp_type_parameters: TimestampTypeParametersProto
    child_list: _containers.RepeatedCompositeFieldContainer[TypeParametersProto]
    def __init__(self, string_type_parameters: _Optional[_Union[StringTypeParametersProto, _Mapping]] = ..., numeric_type_parameters: _Optional[_Union[NumericTypeParametersProto, _Mapping]] = ..., extended_type_parameters: _Optional[_Union[ExtendedTypeParametersProto, _Mapping]] = ..., timestamp_type_parameters: _Optional[_Union[TimestampTypeParametersProto, _Mapping]] = ..., child_list: _Optional[_Iterable[_Union[TypeParametersProto, _Mapping]]] = ...) -> None: ...

class StringTypeParametersProto(_message.Message):
    __slots__ = ("max_length", "is_max_length")
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IS_MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    max_length: int
    is_max_length: bool
    def __init__(self, max_length: _Optional[int] = ..., is_max_length: bool = ...) -> None: ...

class TimestampTypeParametersProto(_message.Message):
    __slots__ = ("precision",)
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    precision: int
    def __init__(self, precision: _Optional[int] = ...) -> None: ...

class NumericTypeParametersProto(_message.Message):
    __slots__ = ("precision", "is_max_precision", "scale")
    Extensions: _python_message._ExtensionDict
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    IS_MAX_PRECISION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    precision: int
    is_max_precision: bool
    scale: int
    def __init__(self, precision: _Optional[int] = ..., is_max_precision: bool = ..., scale: _Optional[int] = ...) -> None: ...

class ExtendedTypeParametersProto(_message.Message):
    __slots__ = ("parameters",)
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[_simple_value_pb2.SimpleValueProto]
    def __init__(self, parameters: _Optional[_Iterable[_Union[_simple_value_pb2.SimpleValueProto, _Mapping]]] = ...) -> None: ...
