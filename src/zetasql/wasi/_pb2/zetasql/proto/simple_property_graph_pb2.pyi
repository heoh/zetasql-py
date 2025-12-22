from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimplePropertyGraphProto(_message.Message):
    __slots__ = ("name", "name_path", "node_tables", "edge_tables", "labels", "property_declarations")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLES_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    name_path: _containers.RepeatedScalarFieldContainer[str]
    node_tables: _containers.RepeatedCompositeFieldContainer[SimpleGraphElementTableProto]
    edge_tables: _containers.RepeatedCompositeFieldContainer[SimpleGraphElementTableProto]
    labels: _containers.RepeatedCompositeFieldContainer[SimpleGraphElementLabelProto]
    property_declarations: _containers.RepeatedCompositeFieldContainer[SimpleGraphPropertyDeclarationProto]
    def __init__(self, name: _Optional[str] = ..., name_path: _Optional[_Iterable[str]] = ..., node_tables: _Optional[_Iterable[_Union[SimpleGraphElementTableProto, _Mapping]]] = ..., edge_tables: _Optional[_Iterable[_Union[SimpleGraphElementTableProto, _Mapping]]] = ..., labels: _Optional[_Iterable[_Union[SimpleGraphElementLabelProto, _Mapping]]] = ..., property_declarations: _Optional[_Iterable[_Union[SimpleGraphPropertyDeclarationProto, _Mapping]]] = ...) -> None: ...

class SimpleGraphElementTableProto(_message.Message):
    __slots__ = ("name", "property_graph_name_path", "kind", "input_table_name", "key_columns", "label_names", "property_definitions", "source_node_table", "dest_node_table", "dynamic_properties", "dynamic_label")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[SimpleGraphElementTableProto.Kind]
        NODE: _ClassVar[SimpleGraphElementTableProto.Kind]
        EDGE: _ClassVar[SimpleGraphElementTableProto.Kind]
    KIND_UNSPECIFIED: SimpleGraphElementTableProto.Kind
    NODE: SimpleGraphElementTableProto.Kind
    EDGE: SimpleGraphElementTableProto.Kind
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_GRAPH_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    INPUT_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    LABEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DEST_NODE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LABEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_graph_name_path: _containers.RepeatedScalarFieldContainer[str]
    kind: SimpleGraphElementTableProto.Kind
    input_table_name: str
    key_columns: _containers.RepeatedScalarFieldContainer[int]
    label_names: _containers.RepeatedScalarFieldContainer[str]
    property_definitions: _containers.RepeatedCompositeFieldContainer[SimpleGraphPropertyDefinitionProto]
    source_node_table: SimpleGraphNodeTableReferenceProto
    dest_node_table: SimpleGraphNodeTableReferenceProto
    dynamic_properties: SimpleGraphElementDynamicPropertiesProto
    dynamic_label: SimpleGraphElementDynamicLabelProto
    def __init__(self, name: _Optional[str] = ..., property_graph_name_path: _Optional[_Iterable[str]] = ..., kind: _Optional[_Union[SimpleGraphElementTableProto.Kind, str]] = ..., input_table_name: _Optional[str] = ..., key_columns: _Optional[_Iterable[int]] = ..., label_names: _Optional[_Iterable[str]] = ..., property_definitions: _Optional[_Iterable[_Union[SimpleGraphPropertyDefinitionProto, _Mapping]]] = ..., source_node_table: _Optional[_Union[SimpleGraphNodeTableReferenceProto, _Mapping]] = ..., dest_node_table: _Optional[_Union[SimpleGraphNodeTableReferenceProto, _Mapping]] = ..., dynamic_properties: _Optional[_Union[SimpleGraphElementDynamicPropertiesProto, _Mapping]] = ..., dynamic_label: _Optional[_Union[SimpleGraphElementDynamicLabelProto, _Mapping]] = ...) -> None: ...

class SimpleGraphElementLabelProto(_message.Message):
    __slots__ = ("name", "property_graph_name_path", "property_declaration_names")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_GRAPH_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATION_NAMES_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_graph_name_path: _containers.RepeatedScalarFieldContainer[str]
    property_declaration_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., property_graph_name_path: _Optional[_Iterable[str]] = ..., property_declaration_names: _Optional[_Iterable[str]] = ...) -> None: ...

class SimpleGraphNodeTableReferenceProto(_message.Message):
    __slots__ = ("node_table_name", "edge_table_columns", "node_table_columns")
    NODE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    node_table_name: str
    edge_table_columns: _containers.RepeatedScalarFieldContainer[int]
    node_table_columns: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, node_table_name: _Optional[str] = ..., edge_table_columns: _Optional[_Iterable[int]] = ..., node_table_columns: _Optional[_Iterable[int]] = ...) -> None: ...

class SimpleGraphPropertyDeclarationProto(_message.Message):
    __slots__ = ("name", "property_graph_name_path", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_GRAPH_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_graph_name_path: _containers.RepeatedScalarFieldContainer[str]
    type: _type_pb2.TypeProto
    def __init__(self, name: _Optional[str] = ..., property_graph_name_path: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...

class SimpleGraphPropertyDefinitionProto(_message.Message):
    __slots__ = ("property_declaration_name", "value_expression_sql")
    PROPERTY_DECLARATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_EXPRESSION_SQL_FIELD_NUMBER: _ClassVar[int]
    property_declaration_name: str
    value_expression_sql: str
    def __init__(self, property_declaration_name: _Optional[str] = ..., value_expression_sql: _Optional[str] = ...) -> None: ...

class SimpleGraphElementDynamicPropertiesProto(_message.Message):
    __slots__ = ("properties_expression",)
    PROPERTIES_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    properties_expression: str
    def __init__(self, properties_expression: _Optional[str] = ...) -> None: ...

class SimpleGraphElementDynamicLabelProto(_message.Message):
    __slots__ = ("label_expression",)
    LABEL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    label_expression: str
    def __init__(self, label_expression: _Optional[str] = ...) -> None: ...
