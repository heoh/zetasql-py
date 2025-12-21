from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Column(_message.Message):
    __slots__ = ("table_alias", "column_name", "type", "is_value_table_column")
    TABLE_ALIAS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    table_alias: str
    column_name: str
    type: str
    is_value_table_column: bool
    def __init__(self, table_alias: _Optional[str] = ..., column_name: _Optional[str] = ..., type: _Optional[str] = ..., is_value_table_column: bool = ...) -> None: ...

class TableAlias(_message.Message):
    __slots__ = ("name", "column_name", "pseudo_column_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    PSEUDO_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    column_name: _containers.RepeatedScalarFieldContainer[str]
    pseudo_column_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., column_name: _Optional[_Iterable[str]] = ..., pseudo_column_name: _Optional[_Iterable[str]] = ...) -> None: ...

class ResultTable(_message.Message):
    __slots__ = ("column", "pseudo_column", "table_alias", "common_table_expression", "is_value_table", "is_ordered")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    PSEUDO_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TABLE_ALIAS_FIELD_NUMBER: _ClassVar[int]
    COMMON_TABLE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    IS_ORDERED_FIELD_NUMBER: _ClassVar[int]
    column: _containers.RepeatedCompositeFieldContainer[Column]
    pseudo_column: _containers.RepeatedCompositeFieldContainer[Column]
    table_alias: _containers.RepeatedCompositeFieldContainer[TableAlias]
    common_table_expression: _containers.RepeatedCompositeFieldContainer[TableAlias]
    is_value_table: bool
    is_ordered: bool
    def __init__(self, column: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., pseudo_column: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., table_alias: _Optional[_Iterable[_Union[TableAlias, _Mapping]]] = ..., common_table_expression: _Optional[_Iterable[_Union[TableAlias, _Mapping]]] = ..., is_value_table: bool = ..., is_ordered: bool = ...) -> None: ...
