from zetasql.wasi._pb2.zetasql.public import annotation_pb2 as _annotation_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleAnonymizationInfoProto(_message.Message):
    __slots__ = ("userid_column_name",)
    USERID_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    userid_column_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, userid_column_name: _Optional[_Iterable[str]] = ...) -> None: ...

class SimpleTableProto(_message.Message):
    __slots__ = ("name", "serialization_id", "is_value_table", "column", "primary_key_column_index", "row_identity_column_index", "name_in_catalog", "allow_anonymous_column_name", "allow_duplicate_column_names", "anonymization_info", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_COLUMN_INDEX_FIELD_NUMBER: _ClassVar[int]
    ROW_IDENTITY_COLUMN_INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_IN_CATALOG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ANONYMOUS_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DUPLICATE_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    ANONYMIZATION_INFO_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    serialization_id: int
    is_value_table: bool
    column: _containers.RepeatedCompositeFieldContainer[SimpleColumnProto]
    primary_key_column_index: _containers.RepeatedScalarFieldContainer[int]
    row_identity_column_index: _containers.RepeatedScalarFieldContainer[int]
    name_in_catalog: str
    allow_anonymous_column_name: bool
    allow_duplicate_column_names: bool
    anonymization_info: SimpleAnonymizationInfoProto
    full_name: str
    def __init__(self, name: _Optional[str] = ..., serialization_id: _Optional[int] = ..., is_value_table: bool = ..., column: _Optional[_Iterable[_Union[SimpleColumnProto, _Mapping]]] = ..., primary_key_column_index: _Optional[_Iterable[int]] = ..., row_identity_column_index: _Optional[_Iterable[int]] = ..., name_in_catalog: _Optional[str] = ..., allow_anonymous_column_name: bool = ..., allow_duplicate_column_names: bool = ..., anonymization_info: _Optional[_Union[SimpleAnonymizationInfoProto, _Mapping]] = ..., full_name: _Optional[str] = ...) -> None: ...

class ExpressionAttributeProto(_message.Message):
    __slots__ = ("expression_string", "expression_kind", "row_identity_column_index")
    class ExpressionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ExpressionAttributeProto.ExpressionKind]
        GENERATED: _ClassVar[ExpressionAttributeProto.ExpressionKind]
        MEASURE_EXPRESSION: _ClassVar[ExpressionAttributeProto.ExpressionKind]
    DEFAULT: ExpressionAttributeProto.ExpressionKind
    GENERATED: ExpressionAttributeProto.ExpressionKind
    MEASURE_EXPRESSION: ExpressionAttributeProto.ExpressionKind
    EXPRESSION_STRING_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_KIND_FIELD_NUMBER: _ClassVar[int]
    ROW_IDENTITY_COLUMN_INDEX_FIELD_NUMBER: _ClassVar[int]
    expression_string: str
    expression_kind: ExpressionAttributeProto.ExpressionKind
    row_identity_column_index: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, expression_string: _Optional[str] = ..., expression_kind: _Optional[_Union[ExpressionAttributeProto.ExpressionKind, str]] = ..., row_identity_column_index: _Optional[_Iterable[int]] = ...) -> None: ...

class SimpleColumnProto(_message.Message):
    __slots__ = ("name", "type", "is_pseudo_column", "is_writable_column", "can_update_unwritable_to_default", "annotation_map", "has_default_value", "column_expression")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PSEUDO_COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_WRITABLE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    CAN_UPDATE_UNWRITABLE_TO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_MAP_FIELD_NUMBER: _ClassVar[int]
    HAS_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _type_pb2.TypeProto
    is_pseudo_column: bool
    is_writable_column: bool
    can_update_unwritable_to_default: bool
    annotation_map: _annotation_pb2.AnnotationMapProto
    has_default_value: bool
    column_expression: ExpressionAttributeProto
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., is_pseudo_column: bool = ..., is_writable_column: bool = ..., can_update_unwritable_to_default: bool = ..., annotation_map: _Optional[_Union[_annotation_pb2.AnnotationMapProto, _Mapping]] = ..., has_default_value: bool = ..., column_expression: _Optional[_Union[ExpressionAttributeProto, _Mapping]] = ...) -> None: ...
