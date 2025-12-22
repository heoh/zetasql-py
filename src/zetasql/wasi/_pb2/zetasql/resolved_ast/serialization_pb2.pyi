from zetasql.wasi._pb2.zetasql.public import annotation_pb2 as _annotation_pb2
from zetasql.wasi._pb2.zetasql.public import parse_location_range_pb2 as _parse_location_range_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.public import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResolvedColumnProto(_message.Message):
    __slots__ = ("column_id", "table_name", "name", "type", "annotation_map")
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_MAP_FIELD_NUMBER: _ClassVar[int]
    column_id: int
    table_name: str
    name: str
    type: _type_pb2.TypeProto
    annotation_map: _annotation_pb2.AnnotationMapProto
    def __init__(self, column_id: _Optional[int] = ..., table_name: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., annotation_map: _Optional[_Union[_annotation_pb2.AnnotationMapProto, _Mapping]] = ...) -> None: ...

class ValueWithTypeProto(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _type_pb2.TypeProto
    value: _value_pb2.ValueProto
    def __init__(self, type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ...) -> None: ...

class TableRefProto(_message.Message):
    __slots__ = ("name", "serialization_id", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    serialization_id: int
    full_name: str
    def __init__(self, name: _Optional[str] = ..., serialization_id: _Optional[int] = ..., full_name: _Optional[str] = ...) -> None: ...

class ModelRefProto(_message.Message):
    __slots__ = ("name", "serialization_id", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    serialization_id: int
    full_name: str
    def __init__(self, name: _Optional[str] = ..., serialization_id: _Optional[int] = ..., full_name: _Optional[str] = ...) -> None: ...

class ConnectionRefProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class SequenceRefProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class ConstantRefProto(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FunctionRefProto(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TableValuedFunctionRefProto(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResolvedNodeProto(_message.Message):
    __slots__ = ("parse_location_range",)
    PARSE_LOCATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    parse_location_range: _parse_location_range_pb2.ParseLocationRangeProto
    def __init__(self, parse_location_range: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ...) -> None: ...

class FieldDescriptorRefProto(_message.Message):
    __slots__ = ("containing_proto", "number")
    CONTAINING_PROTO_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    containing_proto: _type_pb2.ProtoTypeProto
    number: int
    def __init__(self, containing_proto: _Optional[_Union[_type_pb2.ProtoTypeProto, _Mapping]] = ..., number: _Optional[int] = ...) -> None: ...

class OneofDescriptorRefProto(_message.Message):
    __slots__ = ("containing_proto", "index")
    CONTAINING_PROTO_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    containing_proto: _type_pb2.ProtoTypeProto
    index: int
    def __init__(self, containing_proto: _Optional[_Union[_type_pb2.ProtoTypeProto, _Mapping]] = ..., index: _Optional[int] = ...) -> None: ...

class ProcedureRefProto(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResolvedCollationProto(_message.Message):
    __slots__ = ("collation_name", "child_list")
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CHILD_LIST_FIELD_NUMBER: _ClassVar[int]
    collation_name: str
    child_list: _containers.RepeatedCompositeFieldContainer[ResolvedCollationProto]
    def __init__(self, collation_name: _Optional[str] = ..., child_list: _Optional[_Iterable[_Union[ResolvedCollationProto, _Mapping]]] = ...) -> None: ...

class ColumnRefProto(_message.Message):
    __slots__ = ("table_ref", "name")
    TABLE_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    table_ref: TableRefProto
    name: str
    def __init__(self, table_ref: _Optional[_Union[TableRefProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class PropertyGraphRefProto(_message.Message):
    __slots__ = ("full_name",)
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    full_name: str
    def __init__(self, full_name: _Optional[str] = ...) -> None: ...

class GraphPropertyDeclarationRefProto(_message.Message):
    __slots__ = ("property_graph", "name")
    PROPERTY_GRAPH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    property_graph: PropertyGraphRefProto
    name: str
    def __init__(self, property_graph: _Optional[_Union[PropertyGraphRefProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class GraphElementLabelRefProto(_message.Message):
    __slots__ = ("property_graph", "name")
    PROPERTY_GRAPH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    property_graph: PropertyGraphRefProto
    name: str
    def __init__(self, property_graph: _Optional[_Union[PropertyGraphRefProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class GraphElementTableRefProto(_message.Message):
    __slots__ = ("property_graph", "name")
    PROPERTY_GRAPH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    property_graph: PropertyGraphRefProto
    name: str
    def __init__(self, property_graph: _Optional[_Union[PropertyGraphRefProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
