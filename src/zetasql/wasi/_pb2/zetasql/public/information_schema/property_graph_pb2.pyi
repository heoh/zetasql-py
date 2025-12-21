from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropertyGraphProto(_message.Message):
    __slots__ = ("catalog", "schema", "name", "node_tables", "edge_tables", "labels", "property_declarations")
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLES_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    schema: str
    name: str
    node_tables: _containers.RepeatedCompositeFieldContainer[GraphElementTableProto]
    edge_tables: _containers.RepeatedCompositeFieldContainer[GraphElementTableProto]
    labels: _containers.RepeatedCompositeFieldContainer[GraphElementLabelProto]
    property_declarations: _containers.RepeatedCompositeFieldContainer[GraphPropertyDeclarationProto]
    def __init__(self, catalog: _Optional[str] = ..., schema: _Optional[str] = ..., name: _Optional[str] = ..., node_tables: _Optional[_Iterable[_Union[GraphElementTableProto, _Mapping]]] = ..., edge_tables: _Optional[_Iterable[_Union[GraphElementTableProto, _Mapping]]] = ..., labels: _Optional[_Iterable[_Union[GraphElementLabelProto, _Mapping]]] = ..., property_declarations: _Optional[_Iterable[_Union[GraphPropertyDeclarationProto, _Mapping]]] = ...) -> None: ...

class GraphElementTableProto(_message.Message):
    __slots__ = ("name", "kind", "base_catalog_name", "base_schema_name", "base_table_name", "key_columns", "label_names", "property_definitions", "dynamic_label_expr", "dynamic_property_expr", "source_node_table", "destination_node_table")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[GraphElementTableProto.Kind]
        NODE: _ClassVar[GraphElementTableProto.Kind]
        EDGE: _ClassVar[GraphElementTableProto.Kind]
    KIND_UNSPECIFIED: GraphElementTableProto.Kind
    NODE: GraphElementTableProto.Kind
    EDGE: GraphElementTableProto.Kind
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    BASE_CATALOG_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    LABEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LABEL_EXPR_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PROPERTY_EXPR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NODE_TABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: GraphElementTableProto.Kind
    base_catalog_name: str
    base_schema_name: str
    base_table_name: str
    key_columns: _containers.RepeatedScalarFieldContainer[str]
    label_names: _containers.RepeatedScalarFieldContainer[str]
    property_definitions: _containers.RepeatedCompositeFieldContainer[GraphPropertyDefinitionProto]
    dynamic_label_expr: str
    dynamic_property_expr: str
    source_node_table: GraphNodeTableReferenceProto
    destination_node_table: GraphNodeTableReferenceProto
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[_Union[GraphElementTableProto.Kind, str]] = ..., base_catalog_name: _Optional[str] = ..., base_schema_name: _Optional[str] = ..., base_table_name: _Optional[str] = ..., key_columns: _Optional[_Iterable[str]] = ..., label_names: _Optional[_Iterable[str]] = ..., property_definitions: _Optional[_Iterable[_Union[GraphPropertyDefinitionProto, _Mapping]]] = ..., dynamic_label_expr: _Optional[str] = ..., dynamic_property_expr: _Optional[str] = ..., source_node_table: _Optional[_Union[GraphNodeTableReferenceProto, _Mapping]] = ..., destination_node_table: _Optional[_Union[GraphNodeTableReferenceProto, _Mapping]] = ...) -> None: ...

class GraphNodeTableReferenceProto(_message.Message):
    __slots__ = ("node_table_name", "edge_table_columns", "node_table_columns")
    NODE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    node_table_name: str
    edge_table_columns: _containers.RepeatedScalarFieldContainer[str]
    node_table_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node_table_name: _Optional[str] = ..., edge_table_columns: _Optional[_Iterable[str]] = ..., node_table_columns: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphElementLabelProto(_message.Message):
    __slots__ = ("name", "property_declaration_names")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATION_NAMES_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_declaration_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., property_declaration_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GraphPropertyDeclarationProto(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class GraphPropertyDefinitionProto(_message.Message):
    __slots__ = ("property_declaration_name", "value_expression_sql")
    PROPERTY_DECLARATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_EXPRESSION_SQL_FIELD_NUMBER: _ClassVar[int]
    property_declaration_name: str
    value_expression_sql: str
    def __init__(self, property_declaration_name: _Optional[str] = ..., value_expression_sql: _Optional[str] = ...) -> None: ...
