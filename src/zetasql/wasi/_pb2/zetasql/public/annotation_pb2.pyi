from zetasql.wasi._pb2.zetasql.public import simple_value_pb2 as _simple_value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnnotationProto(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: _simple_value_pb2.SimpleValueProto
    def __init__(self, id: _Optional[int] = ..., value: _Optional[_Union[_simple_value_pb2.SimpleValueProto, _Mapping]] = ...) -> None: ...

class AnnotationMapProto(_message.Message):
    __slots__ = ("is_null", "annotations", "array_element", "struct_fields")
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    annotations: _containers.RepeatedCompositeFieldContainer[AnnotationProto]
    array_element: AnnotationMapProto
    struct_fields: _containers.RepeatedCompositeFieldContainer[AnnotationMapProto]
    def __init__(self, is_null: bool = ..., annotations: _Optional[_Iterable[_Union[AnnotationProto, _Mapping]]] = ..., array_element: _Optional[_Union[AnnotationMapProto, _Mapping]] = ..., struct_fields: _Optional[_Iterable[_Union[AnnotationMapProto, _Mapping]]] = ...) -> None: ...
