from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from zetasql.wasi._pb2.zetasql.parser import parse_tree_pb2 as _parse_tree_pb2
from zetasql.wasi._pb2.zetasql.proto import function_pb2 as _function_pb2
from zetasql.wasi._pb2.zetasql.proto import options_pb2 as _options_pb2
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2 as _simple_catalog_pb2
from zetasql.wasi._pb2.zetasql.public import formatter_options_pb2 as _formatter_options_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as _options_pb2_1
from zetasql.wasi._pb2.zetasql.public import parse_resume_location_pb2 as _parse_resume_location_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2 as _simple_table_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.public import value_pb2 as _value_pb2
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2 as _resolved_ast_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescriptorPoolListProto(_message.Message):
    __slots__ = ("definitions",)
    class Builtin(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Definition(_message.Message):
        __slots__ = ("file_descriptor_set", "registered_id", "builtin")
        FILE_DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_ID_FIELD_NUMBER: _ClassVar[int]
        BUILTIN_FIELD_NUMBER: _ClassVar[int]
        file_descriptor_set: _descriptor_pb2.FileDescriptorSet
        registered_id: int
        builtin: DescriptorPoolListProto.Builtin
        def __init__(self, file_descriptor_set: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ..., registered_id: _Optional[int] = ..., builtin: _Optional[_Union[DescriptorPoolListProto.Builtin, _Mapping]] = ...) -> None: ...
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.RepeatedCompositeFieldContainer[DescriptorPoolListProto.Definition]
    def __init__(self, definitions: _Optional[_Iterable[_Union[DescriptorPoolListProto.Definition, _Mapping]]] = ...) -> None: ...

class DescriptorPoolIdList(_message.Message):
    __slots__ = ("registered_ids",)
    REGISTERED_IDS_FIELD_NUMBER: _ClassVar[int]
    registered_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, registered_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class PrepareRequest(_message.Message):
    __slots__ = ("sql", "options", "descriptor_pool_list", "simple_catalog", "registered_catalog_id")
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _options_pb2.AnalyzerOptionsProto
    descriptor_pool_list: DescriptorPoolListProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    registered_catalog_id: int
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ...) -> None: ...

class PreparedState(_message.Message):
    __slots__ = ("prepared_expression_id", "output_type", "referenced_columns", "referenced_parameters", "positional_parameter_count", "descriptor_pool_id_list")
    PREPARED_EXPRESSION_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_PARAMETER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    prepared_expression_id: int
    output_type: _type_pb2.TypeProto
    referenced_columns: _containers.RepeatedScalarFieldContainer[str]
    referenced_parameters: _containers.RepeatedScalarFieldContainer[str]
    positional_parameter_count: int
    descriptor_pool_id_list: DescriptorPoolIdList
    def __init__(self, prepared_expression_id: _Optional[int] = ..., output_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., referenced_columns: _Optional[_Iterable[str]] = ..., referenced_parameters: _Optional[_Iterable[str]] = ..., positional_parameter_count: _Optional[int] = ..., descriptor_pool_id_list: _Optional[_Union[DescriptorPoolIdList, _Mapping]] = ...) -> None: ...

class PrepareResponse(_message.Message):
    __slots__ = ("prepared",)
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    prepared: PreparedState
    def __init__(self, prepared: _Optional[_Union[PreparedState, _Mapping]] = ...) -> None: ...

class EvaluateRequest(_message.Message):
    __slots__ = ("sql", "columns", "params", "descriptor_pool_list", "prepared_expression_id", "options")
    class Parameter(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: _value_pb2.ValueProto
        def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    PREPARED_EXPRESSION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    sql: str
    columns: _containers.RepeatedCompositeFieldContainer[EvaluateRequest.Parameter]
    params: _containers.RepeatedCompositeFieldContainer[EvaluateRequest.Parameter]
    descriptor_pool_list: DescriptorPoolListProto
    prepared_expression_id: int
    options: _options_pb2.AnalyzerOptionsProto
    def __init__(self, sql: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[EvaluateRequest.Parameter, _Mapping]]] = ..., params: _Optional[_Iterable[_Union[EvaluateRequest.Parameter, _Mapping]]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., prepared_expression_id: _Optional[int] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ...) -> None: ...

class EvaluateResponse(_message.Message):
    __slots__ = ("value", "prepared")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    value: _value_pb2.ValueProto
    prepared: PreparedState
    def __init__(self, value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ..., prepared: _Optional[_Union[PreparedState, _Mapping]] = ...) -> None: ...

class EvaluateRequestBatch(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: _containers.RepeatedCompositeFieldContainer[EvaluateRequest]
    def __init__(self, request: _Optional[_Iterable[_Union[EvaluateRequest, _Mapping]]] = ...) -> None: ...

class EvaluateResponseBatch(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[EvaluateResponse]
    def __init__(self, response: _Optional[_Iterable[_Union[EvaluateResponse, _Mapping]]] = ...) -> None: ...

class UnprepareRequest(_message.Message):
    __slots__ = ("prepared_expression_id",)
    PREPARED_EXPRESSION_ID_FIELD_NUMBER: _ClassVar[int]
    prepared_expression_id: int
    def __init__(self, prepared_expression_id: _Optional[int] = ...) -> None: ...

class PrepareQueryRequest(_message.Message):
    __slots__ = ("sql", "options", "descriptor_pool_list", "simple_catalog", "registered_catalog_id", "table_content")
    class TableContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TableContent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TableContent, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _options_pb2.AnalyzerOptionsProto
    descriptor_pool_list: DescriptorPoolListProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    registered_catalog_id: int
    table_content: _containers.MessageMap[str, TableContent]
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., table_content: _Optional[_Mapping[str, TableContent]] = ...) -> None: ...

class PreparedQueryState(_message.Message):
    __slots__ = ("prepared_query_id", "referenced_parameters", "positional_parameter_count", "columns", "descriptor_pool_id_list")
    PREPARED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_PARAMETER_COUNT_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    prepared_query_id: int
    referenced_parameters: _containers.RepeatedScalarFieldContainer[str]
    positional_parameter_count: int
    columns: _containers.RepeatedCompositeFieldContainer[_simple_table_pb2.SimpleColumnProto]
    descriptor_pool_id_list: DescriptorPoolIdList
    def __init__(self, prepared_query_id: _Optional[int] = ..., referenced_parameters: _Optional[_Iterable[str]] = ..., positional_parameter_count: _Optional[int] = ..., columns: _Optional[_Iterable[_Union[_simple_table_pb2.SimpleColumnProto, _Mapping]]] = ..., descriptor_pool_id_list: _Optional[_Union[DescriptorPoolIdList, _Mapping]] = ...) -> None: ...

class PrepareQueryResponse(_message.Message):
    __slots__ = ("prepared",)
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    prepared: PreparedQueryState
    def __init__(self, prepared: _Optional[_Union[PreparedQueryState, _Mapping]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _value_pb2.ValueProto
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ...) -> None: ...

class UnprepareQueryRequest(_message.Message):
    __slots__ = ("prepared_query_id",)
    PREPARED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    prepared_query_id: int
    def __init__(self, prepared_query_id: _Optional[int] = ...) -> None: ...

class EvaluateQueryRequest(_message.Message):
    __slots__ = ("sql", "options", "descriptor_pool_list", "simple_catalog", "registered_catalog_id", "prepared_query_id", "table_content", "params")
    class TableContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TableContent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TableContent, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    PREPARED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _options_pb2.AnalyzerOptionsProto
    descriptor_pool_list: DescriptorPoolListProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    registered_catalog_id: int
    prepared_query_id: int
    table_content: _containers.MessageMap[str, TableContent]
    params: _containers.RepeatedCompositeFieldContainer[Parameter]
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., prepared_query_id: _Optional[int] = ..., table_content: _Optional[_Mapping[str, TableContent]] = ..., params: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ...) -> None: ...

class EvaluateQueryResponse(_message.Message):
    __slots__ = ("content", "prepared")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    content: TableContent
    prepared: PreparedQueryState
    def __init__(self, content: _Optional[_Union[TableContent, _Mapping]] = ..., prepared: _Optional[_Union[PreparedQueryState, _Mapping]] = ...) -> None: ...

class EvaluateQueryBatchRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: _containers.RepeatedCompositeFieldContainer[EvaluateQueryRequest]
    def __init__(self, request: _Optional[_Iterable[_Union[EvaluateQueryRequest, _Mapping]]] = ...) -> None: ...

class EvaluateQueryBatchResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[EvaluateQueryResponse]
    def __init__(self, response: _Optional[_Iterable[_Union[EvaluateQueryResponse, _Mapping]]] = ...) -> None: ...

class PrepareModifyRequest(_message.Message):
    __slots__ = ("sql", "options", "descriptor_pool_list", "simple_catalog", "registered_catalog_id", "table_content")
    class TableContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TableContent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TableContent, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _options_pb2.AnalyzerOptionsProto
    descriptor_pool_list: DescriptorPoolListProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    registered_catalog_id: int
    table_content: _containers.MessageMap[str, TableContent]
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., table_content: _Optional[_Mapping[str, TableContent]] = ...) -> None: ...

class PreparedModifyState(_message.Message):
    __slots__ = ("prepared_modify_id", "referenced_parameters", "positional_parameter_count", "descriptor_pool_id_list")
    PREPARED_MODIFY_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_PARAMETER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    prepared_modify_id: int
    referenced_parameters: _containers.RepeatedScalarFieldContainer[str]
    positional_parameter_count: int
    descriptor_pool_id_list: DescriptorPoolIdList
    def __init__(self, prepared_modify_id: _Optional[int] = ..., referenced_parameters: _Optional[_Iterable[str]] = ..., positional_parameter_count: _Optional[int] = ..., descriptor_pool_id_list: _Optional[_Union[DescriptorPoolIdList, _Mapping]] = ...) -> None: ...

class PrepareModifyResponse(_message.Message):
    __slots__ = ("prepared",)
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    prepared: PreparedModifyState
    def __init__(self, prepared: _Optional[_Union[PreparedModifyState, _Mapping]] = ...) -> None: ...

class UnprepareModifyRequest(_message.Message):
    __slots__ = ("prepared_modify_id",)
    PREPARED_MODIFY_ID_FIELD_NUMBER: _ClassVar[int]
    prepared_modify_id: int
    def __init__(self, prepared_modify_id: _Optional[int] = ...) -> None: ...

class EvaluateModifyRequest(_message.Message):
    __slots__ = ("sql", "options", "descriptor_pool_list", "simple_catalog", "registered_catalog_id", "prepared_modify_id", "table_content", "params")
    class TableContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TableContent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TableContent, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    PREPARED_MODIFY_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _options_pb2.AnalyzerOptionsProto
    descriptor_pool_list: DescriptorPoolListProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    registered_catalog_id: int
    prepared_modify_id: int
    table_content: _containers.MessageMap[str, TableContent]
    params: _containers.RepeatedCompositeFieldContainer[Parameter]
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., prepared_modify_id: _Optional[int] = ..., table_content: _Optional[_Mapping[str, TableContent]] = ..., params: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ...) -> None: ...

class EvaluateModifyResponse(_message.Message):
    __slots__ = ("table_name", "content", "prepared")
    class Row(_message.Message):
        __slots__ = ("operation", "cell", "old_primary_key")
        class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[EvaluateModifyResponse.Row.Operation]
            INSERT: _ClassVar[EvaluateModifyResponse.Row.Operation]
            DELETE: _ClassVar[EvaluateModifyResponse.Row.Operation]
            UPDATE: _ClassVar[EvaluateModifyResponse.Row.Operation]
        UNKNOWN: EvaluateModifyResponse.Row.Operation
        INSERT: EvaluateModifyResponse.Row.Operation
        DELETE: EvaluateModifyResponse.Row.Operation
        UPDATE: EvaluateModifyResponse.Row.Operation
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        CELL_FIELD_NUMBER: _ClassVar[int]
        OLD_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        operation: EvaluateModifyResponse.Row.Operation
        cell: _containers.RepeatedCompositeFieldContainer[_value_pb2.ValueProto]
        old_primary_key: _containers.RepeatedCompositeFieldContainer[_value_pb2.ValueProto]
        def __init__(self, operation: _Optional[_Union[EvaluateModifyResponse.Row.Operation, str]] = ..., cell: _Optional[_Iterable[_Union[_value_pb2.ValueProto, _Mapping]]] = ..., old_primary_key: _Optional[_Iterable[_Union[_value_pb2.ValueProto, _Mapping]]] = ...) -> None: ...
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PREPARED_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    content: _containers.RepeatedCompositeFieldContainer[EvaluateModifyResponse.Row]
    prepared: PreparedModifyState
    def __init__(self, table_name: _Optional[str] = ..., content: _Optional[_Iterable[_Union[EvaluateModifyResponse.Row, _Mapping]]] = ..., prepared: _Optional[_Union[PreparedModifyState, _Mapping]] = ...) -> None: ...

class EvaluateModifyBatchRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: _containers.RepeatedCompositeFieldContainer[EvaluateModifyRequest]
    def __init__(self, request: _Optional[_Iterable[_Union[EvaluateModifyRequest, _Mapping]]] = ...) -> None: ...

class EvaluateModifyBatchResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _containers.RepeatedCompositeFieldContainer[EvaluateModifyResponse]
    def __init__(self, response: _Optional[_Iterable[_Union[EvaluateModifyResponse, _Mapping]]] = ...) -> None: ...

class TableFromProtoRequest(_message.Message):
    __slots__ = ("proto", "file_descriptor_set")
    PROTO_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    proto: _type_pb2.ProtoTypeProto
    file_descriptor_set: _descriptor_pb2.FileDescriptorSet
    def __init__(self, proto: _Optional[_Union[_type_pb2.ProtoTypeProto, _Mapping]] = ..., file_descriptor_set: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ...) -> None: ...

class AnalyzeRequest(_message.Message):
    __slots__ = ("options", "simple_catalog", "descriptor_pool_list", "registered_catalog_id", "sql_statement", "parse_resume_location", "sql_expression")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    SQL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PARSE_RESUME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SQL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    options: _options_pb2.AnalyzerOptionsProto
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    descriptor_pool_list: DescriptorPoolListProto
    registered_catalog_id: int
    sql_statement: str
    parse_resume_location: _parse_resume_location_pb2.ParseResumeLocationProto
    sql_expression: str
    def __init__(self, options: _Optional[_Union[_options_pb2.AnalyzerOptionsProto, _Mapping]] = ..., simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., sql_statement: _Optional[str] = ..., parse_resume_location: _Optional[_Union[_parse_resume_location_pb2.ParseResumeLocationProto, _Mapping]] = ..., sql_expression: _Optional[str] = ...) -> None: ...

class AnalyzeResponse(_message.Message):
    __slots__ = ("resolved_statement", "resolved_expression", "resume_byte_position")
    RESOLVED_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    RESUME_BYTE_POSITION_FIELD_NUMBER: _ClassVar[int]
    resolved_statement: _resolved_ast_pb2.AnyResolvedStatementProto
    resolved_expression: _resolved_ast_pb2.AnyResolvedExprProto
    resume_byte_position: int
    def __init__(self, resolved_statement: _Optional[_Union[_resolved_ast_pb2.AnyResolvedStatementProto, _Mapping]] = ..., resolved_expression: _Optional[_Union[_resolved_ast_pb2.AnyResolvedExprProto, _Mapping]] = ..., resume_byte_position: _Optional[int] = ...) -> None: ...

class BuildSqlRequest(_message.Message):
    __slots__ = ("simple_catalog", "descriptor_pool_list", "registered_catalog_id", "resolved_statement", "resolved_expression")
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    descriptor_pool_list: DescriptorPoolListProto
    registered_catalog_id: int
    resolved_statement: _resolved_ast_pb2.AnyResolvedStatementProto
    resolved_expression: _resolved_ast_pb2.AnyResolvedExprProto
    def __init__(self, simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., registered_catalog_id: _Optional[int] = ..., resolved_statement: _Optional[_Union[_resolved_ast_pb2.AnyResolvedStatementProto, _Mapping]] = ..., resolved_expression: _Optional[_Union[_resolved_ast_pb2.AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class BuildSqlResponse(_message.Message):
    __slots__ = ("sql",)
    SQL_FIELD_NUMBER: _ClassVar[int]
    sql: str
    def __init__(self, sql: _Optional[str] = ...) -> None: ...

class ExtractTableNamesFromStatementRequest(_message.Message):
    __slots__ = ("sql_statement", "options", "allow_script")
    SQL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    sql_statement: str
    options: _options_pb2.LanguageOptionsProto
    allow_script: bool
    def __init__(self, sql_statement: _Optional[str] = ..., options: _Optional[_Union[_options_pb2.LanguageOptionsProto, _Mapping]] = ..., allow_script: bool = ...) -> None: ...

class ExtractTableNamesFromStatementResponse(_message.Message):
    __slots__ = ("table_name",)
    class TableName(_message.Message):
        __slots__ = ("table_name_segment",)
        TABLE_NAME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
        table_name_segment: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, table_name_segment: _Optional[_Iterable[str]] = ...) -> None: ...
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: _containers.RepeatedCompositeFieldContainer[ExtractTableNamesFromStatementResponse.TableName]
    def __init__(self, table_name: _Optional[_Iterable[_Union[ExtractTableNamesFromStatementResponse.TableName, _Mapping]]] = ...) -> None: ...

class ExtractTableNamesFromNextStatementRequest(_message.Message):
    __slots__ = ("parse_resume_location", "options")
    PARSE_RESUME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    parse_resume_location: _parse_resume_location_pb2.ParseResumeLocationProto
    options: _options_pb2.LanguageOptionsProto
    def __init__(self, parse_resume_location: _Optional[_Union[_parse_resume_location_pb2.ParseResumeLocationProto, _Mapping]] = ..., options: _Optional[_Union[_options_pb2.LanguageOptionsProto, _Mapping]] = ...) -> None: ...

class ExtractTableNamesFromNextStatementResponse(_message.Message):
    __slots__ = ("table_name", "resume_byte_position")
    class TableName(_message.Message):
        __slots__ = ("table_name_segment",)
        TABLE_NAME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
        table_name_segment: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, table_name_segment: _Optional[_Iterable[str]] = ...) -> None: ...
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESUME_BYTE_POSITION_FIELD_NUMBER: _ClassVar[int]
    table_name: _containers.RepeatedCompositeFieldContainer[ExtractTableNamesFromNextStatementResponse.TableName]
    resume_byte_position: int
    def __init__(self, table_name: _Optional[_Iterable[_Union[ExtractTableNamesFromNextStatementResponse.TableName, _Mapping]]] = ..., resume_byte_position: _Optional[int] = ...) -> None: ...

class FormatSqlRequest(_message.Message):
    __slots__ = ("sql", "options", "byte_ranges")
    SQL_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BYTE_RANGES_FIELD_NUMBER: _ClassVar[int]
    sql: str
    options: _formatter_options_pb2.FormatterOptionsProto
    byte_ranges: _containers.RepeatedCompositeFieldContainer[_formatter_options_pb2.FormatterRangeProto]
    def __init__(self, sql: _Optional[str] = ..., options: _Optional[_Union[_formatter_options_pb2.FormatterOptionsProto, _Mapping]] = ..., byte_ranges: _Optional[_Iterable[_Union[_formatter_options_pb2.FormatterRangeProto, _Mapping]]] = ...) -> None: ...

class FormatSqlResponse(_message.Message):
    __slots__ = ("sql",)
    SQL_FIELD_NUMBER: _ClassVar[int]
    sql: str
    def __init__(self, sql: _Optional[str] = ...) -> None: ...

class RegisterCatalogRequest(_message.Message):
    __slots__ = ("simple_catalog", "descriptor_pool_list", "table_content")
    class TableContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TableContent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TableContent, _Mapping]] = ...) -> None: ...
    SIMPLE_CATALOG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_LIST_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    simple_catalog: _simple_catalog_pb2.SimpleCatalogProto
    descriptor_pool_list: DescriptorPoolListProto
    table_content: _containers.MessageMap[str, TableContent]
    def __init__(self, simple_catalog: _Optional[_Union[_simple_catalog_pb2.SimpleCatalogProto, _Mapping]] = ..., descriptor_pool_list: _Optional[_Union[DescriptorPoolListProto, _Mapping]] = ..., table_content: _Optional[_Mapping[str, TableContent]] = ...) -> None: ...

class TableContent(_message.Message):
    __slots__ = ("table_data",)
    TABLE_DATA_FIELD_NUMBER: _ClassVar[int]
    table_data: TableData
    def __init__(self, table_data: _Optional[_Union[TableData, _Mapping]] = ...) -> None: ...

class TableData(_message.Message):
    __slots__ = ("row",)
    class Row(_message.Message):
        __slots__ = ("cell",)
        CELL_FIELD_NUMBER: _ClassVar[int]
        cell: _containers.RepeatedCompositeFieldContainer[_value_pb2.ValueProto]
        def __init__(self, cell: _Optional[_Iterable[_Union[_value_pb2.ValueProto, _Mapping]]] = ...) -> None: ...
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _containers.RepeatedCompositeFieldContainer[TableData.Row]
    def __init__(self, row: _Optional[_Iterable[_Union[TableData.Row, _Mapping]]] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("registered_id", "descriptor_pool_id_list")
    REGISTERED_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_POOL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    registered_id: int
    descriptor_pool_id_list: DescriptorPoolIdList
    def __init__(self, registered_id: _Optional[int] = ..., descriptor_pool_id_list: _Optional[_Union[DescriptorPoolIdList, _Mapping]] = ...) -> None: ...

class UnregisterRequest(_message.Message):
    __slots__ = ("registered_id",)
    REGISTERED_ID_FIELD_NUMBER: _ClassVar[int]
    registered_id: int
    def __init__(self, registered_id: _Optional[int] = ...) -> None: ...

class GetBuiltinFunctionsResponse(_message.Message):
    __slots__ = ("function", "types", "table_valued_function")
    class TypesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _type_pb2.TypeProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    TABLE_VALUED_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    function: _containers.RepeatedCompositeFieldContainer[_function_pb2.FunctionProto]
    types: _containers.MessageMap[str, _type_pb2.TypeProto]
    table_valued_function: _containers.RepeatedCompositeFieldContainer[_function_pb2.TableValuedFunctionProto]
    def __init__(self, function: _Optional[_Iterable[_Union[_function_pb2.FunctionProto, _Mapping]]] = ..., types: _Optional[_Mapping[str, _type_pb2.TypeProto]] = ..., table_valued_function: _Optional[_Iterable[_Union[_function_pb2.TableValuedFunctionProto, _Mapping]]] = ...) -> None: ...

class LanguageOptionsRequest(_message.Message):
    __slots__ = ("maximum_features", "language_version")
    MAXIMUM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    maximum_features: bool
    language_version: _options_pb2_1.LanguageVersion
    def __init__(self, maximum_features: bool = ..., language_version: _Optional[_Union[_options_pb2_1.LanguageVersion, str]] = ...) -> None: ...

class AnalyzerOptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ParseRequest(_message.Message):
    __slots__ = ("sql_statement", "parse_resume_location", "options", "allow_script")
    SQL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PARSE_RESUME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    sql_statement: str
    parse_resume_location: _parse_resume_location_pb2.ParseResumeLocationProto
    options: _options_pb2.LanguageOptionsProto
    allow_script: bool
    def __init__(self, sql_statement: _Optional[str] = ..., parse_resume_location: _Optional[_Union[_parse_resume_location_pb2.ParseResumeLocationProto, _Mapping]] = ..., options: _Optional[_Union[_options_pb2.LanguageOptionsProto, _Mapping]] = ..., allow_script: bool = ...) -> None: ...

class ParseResponse(_message.Message):
    __slots__ = ("parsed_statement", "parsed_script", "resume_byte_position")
    PARSED_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PARSED_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    RESUME_BYTE_POSITION_FIELD_NUMBER: _ClassVar[int]
    parsed_statement: _parse_tree_pb2.AnyASTStatementProto
    parsed_script: _parse_tree_pb2.ASTScriptProto
    resume_byte_position: int
    def __init__(self, parsed_statement: _Optional[_Union[_parse_tree_pb2.AnyASTStatementProto, _Mapping]] = ..., parsed_script: _Optional[_Union[_parse_tree_pb2.ASTScriptProto, _Mapping]] = ..., resume_byte_position: _Optional[int] = ...) -> None: ...
