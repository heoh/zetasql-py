from zetasql.wasi._pb2.zetasql.proto import function_pb2 as _function_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2 as _options_pb2
from zetasql.wasi._pb2.zetasql.proto import simple_property_graph_pb2 as _simple_property_graph_pb2
from zetasql.wasi._pb2.zetasql.public import simple_connection_pb2 as _simple_connection_pb2
from zetasql.wasi._pb2.zetasql.public import simple_constant_pb2 as _simple_constant_pb2
from zetasql.wasi._pb2.zetasql.public import simple_model_pb2 as _simple_model_pb2
from zetasql.wasi._pb2.zetasql.public import simple_sequence_pb2 as _simple_sequence_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2 as _simple_table_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleCatalogProto(_message.Message):
    __slots__ = ("name", "table", "named_type", "catalog", "builtin_function_options", "custom_function", "custom_tvf", "file_descriptor_set_index", "procedure", "constant", "property_graph", "connection", "model", "sequence")
    class NamedTypeProto(_message.Message):
        __slots__ = ("name", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: _type_pb2.TypeProto
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    NAMED_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    BUILTIN_FUNCTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TVF_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_GRAPH_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    table: _containers.RepeatedCompositeFieldContainer[_simple_table_pb2.SimpleTableProto]
    named_type: _containers.RepeatedCompositeFieldContainer[SimpleCatalogProto.NamedTypeProto]
    catalog: _containers.RepeatedCompositeFieldContainer[SimpleCatalogProto]
    builtin_function_options: _options_pb2.ZetaSQLBuiltinFunctionOptionsProto
    custom_function: _containers.RepeatedCompositeFieldContainer[_function_pb2.FunctionProto]
    custom_tvf: _containers.RepeatedCompositeFieldContainer[_function_pb2.TableValuedFunctionProto]
    file_descriptor_set_index: int
    procedure: _containers.RepeatedCompositeFieldContainer[_function_pb2.ProcedureProto]
    constant: _containers.RepeatedCompositeFieldContainer[_simple_constant_pb2.SimpleConstantProto]
    property_graph: _containers.RepeatedCompositeFieldContainer[_simple_property_graph_pb2.SimplePropertyGraphProto]
    connection: _containers.RepeatedCompositeFieldContainer[_simple_connection_pb2.SimpleConnectionProto]
    model: _containers.RepeatedCompositeFieldContainer[_simple_model_pb2.SimpleModelProto]
    sequence: _containers.RepeatedCompositeFieldContainer[_simple_sequence_pb2.SimpleSequenceProto]
    def __init__(self, name: _Optional[str] = ..., table: _Optional[_Iterable[_Union[_simple_table_pb2.SimpleTableProto, _Mapping]]] = ..., named_type: _Optional[_Iterable[_Union[SimpleCatalogProto.NamedTypeProto, _Mapping]]] = ..., catalog: _Optional[_Iterable[_Union[SimpleCatalogProto, _Mapping]]] = ..., builtin_function_options: _Optional[_Union[_options_pb2.ZetaSQLBuiltinFunctionOptionsProto, _Mapping]] = ..., custom_function: _Optional[_Iterable[_Union[_function_pb2.FunctionProto, _Mapping]]] = ..., custom_tvf: _Optional[_Iterable[_Union[_function_pb2.TableValuedFunctionProto, _Mapping]]] = ..., file_descriptor_set_index: _Optional[int] = ..., procedure: _Optional[_Iterable[_Union[_function_pb2.ProcedureProto, _Mapping]]] = ..., constant: _Optional[_Iterable[_Union[_simple_constant_pb2.SimpleConstantProto, _Mapping]]] = ..., property_graph: _Optional[_Iterable[_Union[_simple_property_graph_pb2.SimplePropertyGraphProto, _Mapping]]] = ..., connection: _Optional[_Iterable[_Union[_simple_connection_pb2.SimpleConnectionProto, _Mapping]]] = ..., model: _Optional[_Iterable[_Union[_simple_model_pb2.SimpleModelProto, _Mapping]]] = ..., sequence: _Optional[_Iterable[_Union[_simple_sequence_pb2.SimpleSequenceProto, _Mapping]]] = ...) -> None: ...
