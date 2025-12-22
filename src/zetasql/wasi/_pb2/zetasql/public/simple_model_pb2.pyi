from zetasql.wasi._pb2.zetasql.public import simple_table_pb2 as _simple_table_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleModelProto(_message.Message):
    __slots__ = ("id", "name", "input", "output")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    input: _containers.RepeatedCompositeFieldContainer[_simple_table_pb2.SimpleColumnProto]
    output: _containers.RepeatedCompositeFieldContainer[_simple_table_pb2.SimpleColumnProto]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., input: _Optional[_Iterable[_Union[_simple_table_pb2.SimpleColumnProto, _Mapping]]] = ..., output: _Optional[_Iterable[_Union[_simple_table_pb2.SimpleColumnProto, _Mapping]]] = ...) -> None: ...
