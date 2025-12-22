from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.public import type_parameters_pb2 as _type_parameters_pb2
from zetasql.wasi._pb2.zetasql.public import value_pb2 as _value_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Variable(_message.Message):
    __slots__ = ("name", "type", "value", "type_params")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _type_pb2.TypeProto
    value: _value_pb2.ValueProto
    type_params: _type_parameters_pb2.TypeParametersProto
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ..., type_params: _Optional[_Union[_type_parameters_pb2.TypeParametersProto, _Mapping]] = ...) -> None: ...
