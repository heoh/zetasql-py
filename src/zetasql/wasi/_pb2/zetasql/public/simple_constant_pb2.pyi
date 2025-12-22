from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.public import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleConstantProto(_message.Message):
    __slots__ = ("name_path", "type", "value")
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name_path: _containers.RepeatedScalarFieldContainer[str]
    type: _type_pb2.TypeProto
    value: _value_pb2.ValueProto
    def __init__(self, name_path: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ...) -> None: ...
