from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT_TABLE_TYPE: _ClassVar[TableType]
    SQL_TABLE: _ClassVar[TableType]
    VALUE_TABLE: _ClassVar[TableType]
DEFAULT_TABLE_TYPE: TableType
SQL_TABLE: TableType
VALUE_TABLE: TableType
STRUCT_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
struct_field_name: _descriptor.FieldDescriptor
IS_RAW_PROTO_FIELD_NUMBER: _ClassVar[int]
is_raw_proto: _descriptor.FieldDescriptor
IS_HIDDEN_COLUMN_FIELD_NUMBER: _ClassVar[int]
is_hidden_column: _descriptor.FieldDescriptor
IS_MEASURE_FIELD_NUMBER: _ClassVar[int]
is_measure: _descriptor.FieldDescriptor
IS_WRAPPER_FIELD_NUMBER: _ClassVar[int]
is_wrapper: _descriptor.FieldDescriptor
IS_STRUCT_FIELD_NUMBER: _ClassVar[int]
is_struct: _descriptor.FieldDescriptor
TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
table_type: _descriptor.FieldDescriptor

class WireFormatAnnotationEmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
