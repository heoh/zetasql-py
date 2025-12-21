from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    __TypeKind__switch_must_have_a_default__: _ClassVar[TypeKind]
    TYPE_UNKNOWN: _ClassVar[TypeKind]
    TYPE_INT32: _ClassVar[TypeKind]
    TYPE_INT64: _ClassVar[TypeKind]
    TYPE_UINT32: _ClassVar[TypeKind]
    TYPE_UINT64: _ClassVar[TypeKind]
    TYPE_BOOL: _ClassVar[TypeKind]
    TYPE_FLOAT: _ClassVar[TypeKind]
    TYPE_DOUBLE: _ClassVar[TypeKind]
    TYPE_STRING: _ClassVar[TypeKind]
    TYPE_BYTES: _ClassVar[TypeKind]
    TYPE_DATE: _ClassVar[TypeKind]
    TYPE_TIMESTAMP: _ClassVar[TypeKind]
    TYPE_ENUM: _ClassVar[TypeKind]
    TYPE_ARRAY: _ClassVar[TypeKind]
    TYPE_STRUCT: _ClassVar[TypeKind]
    TYPE_PROTO: _ClassVar[TypeKind]
    TYPE_TIME: _ClassVar[TypeKind]
    TYPE_DATETIME: _ClassVar[TypeKind]
    TYPE_GEOGRAPHY: _ClassVar[TypeKind]
    TYPE_NUMERIC: _ClassVar[TypeKind]
    TYPE_BIGNUMERIC: _ClassVar[TypeKind]
    TYPE_EXTENDED: _ClassVar[TypeKind]
    TYPE_JSON: _ClassVar[TypeKind]
    TYPE_INTERVAL: _ClassVar[TypeKind]
    TYPE_TOKENLIST: _ClassVar[TypeKind]
    TYPE_RANGE: _ClassVar[TypeKind]
    TYPE_GRAPH_ELEMENT: _ClassVar[TypeKind]
    TYPE_GRAPH_PATH: _ClassVar[TypeKind]
    TYPE_MAP: _ClassVar[TypeKind]
    TYPE_UUID: _ClassVar[TypeKind]
    TYPE_MEASURE: _ClassVar[TypeKind]
    TYPE_ROW: _ClassVar[TypeKind]
__TypeKind__switch_must_have_a_default__: TypeKind
TYPE_UNKNOWN: TypeKind
TYPE_INT32: TypeKind
TYPE_INT64: TypeKind
TYPE_UINT32: TypeKind
TYPE_UINT64: TypeKind
TYPE_BOOL: TypeKind
TYPE_FLOAT: TypeKind
TYPE_DOUBLE: TypeKind
TYPE_STRING: TypeKind
TYPE_BYTES: TypeKind
TYPE_DATE: TypeKind
TYPE_TIMESTAMP: TypeKind
TYPE_ENUM: TypeKind
TYPE_ARRAY: TypeKind
TYPE_STRUCT: TypeKind
TYPE_PROTO: TypeKind
TYPE_TIME: TypeKind
TYPE_DATETIME: TypeKind
TYPE_GEOGRAPHY: TypeKind
TYPE_NUMERIC: TypeKind
TYPE_BIGNUMERIC: TypeKind
TYPE_EXTENDED: TypeKind
TYPE_JSON: TypeKind
TYPE_INTERVAL: TypeKind
TYPE_TOKENLIST: TypeKind
TYPE_RANGE: TypeKind
TYPE_GRAPH_ELEMENT: TypeKind
TYPE_GRAPH_PATH: TypeKind
TYPE_MAP: TypeKind
TYPE_UUID: TypeKind
TYPE_MEASURE: TypeKind
TYPE_ROW: TypeKind
OPAQUE_ENUM_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
opaque_enum_type_options: _descriptor.FieldDescriptor
OPAQUE_ENUM_VALUE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
opaque_enum_value_options: _descriptor.FieldDescriptor

class TypeProto(_message.Message):
    __slots__ = ("type_kind", "array_type", "struct_type", "proto_type", "enum_type", "range_type", "graph_element_type", "graph_path_type", "map_type", "measure_type", "file_descriptor_set", "extended_type_name")
    Extensions: _python_message._ExtensionDict
    TYPE_KIND_FIELD_NUMBER: _ClassVar[int]
    ARRAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTO_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_PATH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEASURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    type_kind: TypeKind
    array_type: ArrayTypeProto
    struct_type: StructTypeProto
    proto_type: ProtoTypeProto
    enum_type: EnumTypeProto
    range_type: RangeTypeProto
    graph_element_type: GraphElementTypeProto
    graph_path_type: GraphPathTypeProto
    map_type: MapTypeProto
    measure_type: MeasureTypeProto
    file_descriptor_set: _containers.RepeatedCompositeFieldContainer[_descriptor_pb2.FileDescriptorSet]
    extended_type_name: str
    def __init__(self, type_kind: _Optional[_Union[TypeKind, str]] = ..., array_type: _Optional[_Union[ArrayTypeProto, _Mapping]] = ..., struct_type: _Optional[_Union[StructTypeProto, _Mapping]] = ..., proto_type: _Optional[_Union[ProtoTypeProto, _Mapping]] = ..., enum_type: _Optional[_Union[EnumTypeProto, _Mapping]] = ..., range_type: _Optional[_Union[RangeTypeProto, _Mapping]] = ..., graph_element_type: _Optional[_Union[GraphElementTypeProto, _Mapping]] = ..., graph_path_type: _Optional[_Union[GraphPathTypeProto, _Mapping]] = ..., map_type: _Optional[_Union[MapTypeProto, _Mapping]] = ..., measure_type: _Optional[_Union[MeasureTypeProto, _Mapping]] = ..., file_descriptor_set: _Optional[_Iterable[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]]] = ..., extended_type_name: _Optional[str] = ...) -> None: ...

class ArrayTypeProto(_message.Message):
    __slots__ = ("element_type",)
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    element_type: TypeProto
    def __init__(self, element_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...

class StructFieldProto(_message.Message):
    __slots__ = ("field_name", "field_type")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    field_type: TypeProto
    def __init__(self, field_name: _Optional[str] = ..., field_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...

class StructTypeProto(_message.Message):
    __slots__ = ("field",)
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: _containers.RepeatedCompositeFieldContainer[StructFieldProto]
    def __init__(self, field: _Optional[_Iterable[_Union[StructFieldProto, _Mapping]]] = ...) -> None: ...

class MapTypeProto(_message.Message):
    __slots__ = ("key_type", "value_type")
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    key_type: TypeProto
    value_type: TypeProto
    def __init__(self, key_type: _Optional[_Union[TypeProto, _Mapping]] = ..., value_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...

class ProtoTypeProto(_message.Message):
    __slots__ = ("proto_name", "proto_file_name", "file_descriptor_set_index", "catalog_name_path")
    PROTO_NAME_FIELD_NUMBER: _ClassVar[int]
    PROTO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    CATALOG_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    proto_name: str
    proto_file_name: str
    file_descriptor_set_index: int
    catalog_name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, proto_name: _Optional[str] = ..., proto_file_name: _Optional[str] = ..., file_descriptor_set_index: _Optional[int] = ..., catalog_name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class EnumTypeProto(_message.Message):
    __slots__ = ("enum_name", "enum_file_name", "file_descriptor_set_index", "catalog_name_path", "is_opaque")
    ENUM_NAME_FIELD_NUMBER: _ClassVar[int]
    ENUM_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    CATALOG_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_OPAQUE_FIELD_NUMBER: _ClassVar[int]
    enum_name: str
    enum_file_name: str
    file_descriptor_set_index: int
    catalog_name_path: _containers.RepeatedScalarFieldContainer[str]
    is_opaque: bool
    def __init__(self, enum_name: _Optional[str] = ..., enum_file_name: _Optional[str] = ..., file_descriptor_set_index: _Optional[int] = ..., catalog_name_path: _Optional[_Iterable[str]] = ..., is_opaque: bool = ...) -> None: ...

class RangeTypeProto(_message.Message):
    __slots__ = ("element_type",)
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    element_type: TypeProto
    def __init__(self, element_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...

class OpaqueEnumTypeOptions(_message.Message):
    __slots__ = ("sql_opaque_enum_name",)
    SQL_OPAQUE_ENUM_NAME_FIELD_NUMBER: _ClassVar[int]
    sql_opaque_enum_name: str
    def __init__(self, sql_opaque_enum_name: _Optional[str] = ...) -> None: ...

class OpaqueEnumValueOptions(_message.Message):
    __slots__ = ("invalid_enum_value",)
    INVALID_ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    invalid_enum_value: bool
    def __init__(self, invalid_enum_value: bool = ...) -> None: ...

class GraphElementTypeProto(_message.Message):
    __slots__ = ("kind", "property_type", "graph_reference", "is_dynamic")
    class ElementKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_INVALID: _ClassVar[GraphElementTypeProto.ElementKind]
        KIND_NODE: _ClassVar[GraphElementTypeProto.ElementKind]
        KIND_EDGE: _ClassVar[GraphElementTypeProto.ElementKind]
    KIND_INVALID: GraphElementTypeProto.ElementKind
    KIND_NODE: GraphElementTypeProto.ElementKind
    KIND_EDGE: GraphElementTypeProto.ElementKind
    class PropertyTypeProto(_message.Message):
        __slots__ = ("name", "value_type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value_type: TypeProto
        def __init__(self, name: _Optional[str] = ..., value_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    kind: GraphElementTypeProto.ElementKind
    property_type: _containers.RepeatedCompositeFieldContainer[GraphElementTypeProto.PropertyTypeProto]
    graph_reference: _containers.RepeatedScalarFieldContainer[str]
    is_dynamic: bool
    def __init__(self, kind: _Optional[_Union[GraphElementTypeProto.ElementKind, str]] = ..., property_type: _Optional[_Iterable[_Union[GraphElementTypeProto.PropertyTypeProto, _Mapping]]] = ..., graph_reference: _Optional[_Iterable[str]] = ..., is_dynamic: bool = ...) -> None: ...

class GraphPathTypeProto(_message.Message):
    __slots__ = ("node_type", "edge_type")
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_type: GraphElementTypeProto
    edge_type: GraphElementTypeProto
    def __init__(self, node_type: _Optional[_Union[GraphElementTypeProto, _Mapping]] = ..., edge_type: _Optional[_Union[GraphElementTypeProto, _Mapping]] = ...) -> None: ...

class MeasureTypeProto(_message.Message):
    __slots__ = ("result_type",)
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    result_type: TypeProto
    def __init__(self, result_type: _Optional[_Union[TypeProto, _Mapping]] = ...) -> None: ...
