from zetasql.wasi._pb2.zetasql.public import annotation_pb2 as _annotation_pb2
from zetasql.wasi._pb2.zetasql.public import constness_level_pb2 as _constness_level_pb2
from zetasql.wasi._pb2.zetasql.public import deprecation_warning_pb2 as _deprecation_warning_pb2
from zetasql.wasi._pb2.zetasql.public import function_pb2 as _function_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as _options_pb2
from zetasql.wasi._pb2.zetasql.public import parse_location_range_pb2 as _parse_location_range_pb2
from zetasql.wasi._pb2.zetasql.public import parse_resume_location_pb2 as _parse_resume_location_pb2
from zetasql.wasi._pb2.zetasql.public import simple_table_pb2 as _simple_table_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.public import value_pb2 as _value_pb2
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_enums_pb2 as _resolved_ast_enums_pb2
from zetasql.wasi._pb2.zetasql.resolved_ast import serialization_pb2 as _serialization_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TVFRelationColumnProto(_message.Message):
    __slots__ = ("name", "type", "is_pseudo_column", "annotation_map", "name_parse_location_range", "type_parse_location_range")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PSEUDO_COLUMN_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_MAP_FIELD_NUMBER: _ClassVar[int]
    NAME_PARSE_LOCATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARSE_LOCATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _type_pb2.TypeProto
    is_pseudo_column: bool
    annotation_map: _annotation_pb2.AnnotationMapProto
    name_parse_location_range: _parse_location_range_pb2.ParseLocationRangeProto
    type_parse_location_range: _parse_location_range_pb2.ParseLocationRangeProto
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., is_pseudo_column: bool = ..., annotation_map: _Optional[_Union[_annotation_pb2.AnnotationMapProto, _Mapping]] = ..., name_parse_location_range: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ..., type_parse_location_range: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ...) -> None: ...

class TVFRelationProto(_message.Message):
    __slots__ = ("column", "is_value_table")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    column: _containers.RepeatedCompositeFieldContainer[TVFRelationColumnProto]
    is_value_table: bool
    def __init__(self, column: _Optional[_Iterable[_Union[TVFRelationColumnProto, _Mapping]]] = ..., is_value_table: bool = ...) -> None: ...

class TVFModelProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class TVFConnectionProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class TVFDescriptorProto(_message.Message):
    __slots__ = ("column_name",)
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    column_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, column_name: _Optional[_Iterable[str]] = ...) -> None: ...

class TVFGraphProto(_message.Message):
    __slots__ = ("name", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    full_name: str
    def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class FunctionArgumentTypeOptionsProto(_message.Message):
    __slots__ = ("cardinality", "must_be_constant", "must_be_non_null", "is_not_aggregate", "must_support_equality", "must_support_ordering", "min_value", "max_value", "extra_relation_input_columns_allowed", "relation_input_schema", "argument_name", "argument_name_parse_location", "argument_type_parse_location", "procedure_argument_mode", "argument_name_is_mandatory", "descriptor_resolution_table_offset", "default_value", "default_value_type", "argument_collation_mode", "uses_array_element_for_collation", "must_support_grouping", "array_element_must_support_equality", "array_element_must_support_ordering", "array_element_must_support_grouping", "named_argument_kind", "argument_alias_kind", "must_be_constant_expression", "constness_level")
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    MUST_BE_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    MUST_BE_NON_NULL_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    MUST_SUPPORT_EQUALITY_FIELD_NUMBER: _ClassVar[int]
    MUST_SUPPORT_ORDERING_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_RELATION_INPUT_COLUMNS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    RELATION_INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_PARSE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_TYPE_PARSE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_ARGUMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_IS_MANDATORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_RESOLUTION_TABLE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_COLLATION_MODE_FIELD_NUMBER: _ClassVar[int]
    USES_ARRAY_ELEMENT_FOR_COLLATION_FIELD_NUMBER: _ClassVar[int]
    MUST_SUPPORT_GROUPING_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_MUST_SUPPORT_EQUALITY_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_MUST_SUPPORT_ORDERING_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_MUST_SUPPORT_GROUPING_FIELD_NUMBER: _ClassVar[int]
    NAMED_ARGUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_ALIAS_KIND_FIELD_NUMBER: _ClassVar[int]
    MUST_BE_CONSTANT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    CONSTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    cardinality: _function_pb2.FunctionEnums.ArgumentCardinality
    must_be_constant: bool
    must_be_non_null: bool
    is_not_aggregate: bool
    must_support_equality: bool
    must_support_ordering: bool
    min_value: int
    max_value: int
    extra_relation_input_columns_allowed: bool
    relation_input_schema: TVFRelationProto
    argument_name: str
    argument_name_parse_location: _parse_location_range_pb2.ParseLocationRangeProto
    argument_type_parse_location: _parse_location_range_pb2.ParseLocationRangeProto
    procedure_argument_mode: _function_pb2.FunctionEnums.ProcedureArgumentMode
    argument_name_is_mandatory: bool
    descriptor_resolution_table_offset: int
    default_value: _value_pb2.ValueProto
    default_value_type: _type_pb2.TypeProto
    argument_collation_mode: _function_pb2.FunctionEnums.ArgumentCollationMode
    uses_array_element_for_collation: bool
    must_support_grouping: bool
    array_element_must_support_equality: bool
    array_element_must_support_ordering: bool
    array_element_must_support_grouping: bool
    named_argument_kind: _function_pb2.FunctionEnums.NamedArgumentKind
    argument_alias_kind: _function_pb2.FunctionEnums.ArgumentAliasKind
    must_be_constant_expression: bool
    constness_level: _constness_level_pb2.ConstnessLevelProto.Level
    def __init__(self, cardinality: _Optional[_Union[_function_pb2.FunctionEnums.ArgumentCardinality, str]] = ..., must_be_constant: bool = ..., must_be_non_null: bool = ..., is_not_aggregate: bool = ..., must_support_equality: bool = ..., must_support_ordering: bool = ..., min_value: _Optional[int] = ..., max_value: _Optional[int] = ..., extra_relation_input_columns_allowed: bool = ..., relation_input_schema: _Optional[_Union[TVFRelationProto, _Mapping]] = ..., argument_name: _Optional[str] = ..., argument_name_parse_location: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ..., argument_type_parse_location: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ..., procedure_argument_mode: _Optional[_Union[_function_pb2.FunctionEnums.ProcedureArgumentMode, str]] = ..., argument_name_is_mandatory: bool = ..., descriptor_resolution_table_offset: _Optional[int] = ..., default_value: _Optional[_Union[_value_pb2.ValueProto, _Mapping]] = ..., default_value_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., argument_collation_mode: _Optional[_Union[_function_pb2.FunctionEnums.ArgumentCollationMode, str]] = ..., uses_array_element_for_collation: bool = ..., must_support_grouping: bool = ..., array_element_must_support_equality: bool = ..., array_element_must_support_ordering: bool = ..., array_element_must_support_grouping: bool = ..., named_argument_kind: _Optional[_Union[_function_pb2.FunctionEnums.NamedArgumentKind, str]] = ..., argument_alias_kind: _Optional[_Union[_function_pb2.FunctionEnums.ArgumentAliasKind, str]] = ..., must_be_constant_expression: bool = ..., constness_level: _Optional[_Union[_constness_level_pb2.ConstnessLevelProto.Level, str]] = ...) -> None: ...

class ArgumentTypeLambdaProto(_message.Message):
    __slots__ = ("argument", "body")
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    argument: _containers.RepeatedCompositeFieldContainer[FunctionArgumentTypeProto]
    body: FunctionArgumentTypeProto
    def __init__(self, argument: _Optional[_Iterable[_Union[FunctionArgumentTypeProto, _Mapping]]] = ..., body: _Optional[_Union[FunctionArgumentTypeProto, _Mapping]] = ...) -> None: ...

class FunctionArgumentTypeProto(_message.Message):
    __slots__ = ("kind", "type", "num_occurrences", "options")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LAMBDA_FIELD_NUMBER: _ClassVar[int]
    kind: _function_pb2.SignatureArgumentKind
    type: _type_pb2.TypeProto
    num_occurrences: int
    options: FunctionArgumentTypeOptionsProto
    def __init__(self, kind: _Optional[_Union[_function_pb2.SignatureArgumentKind, str]] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., num_occurrences: _Optional[int] = ..., options: _Optional[_Union[FunctionArgumentTypeOptionsProto, _Mapping]] = ..., **kwargs) -> None: ...

class FunctionSignatureRewriteOptionsProto(_message.Message):
    __slots__ = ("enabled", "rewriter", "sql", "allow_table_references", "allowed_function_groups")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REWRITER_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TABLE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FUNCTION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    rewriter: _options_pb2.ResolvedASTRewrite
    sql: str
    allow_table_references: bool
    allowed_function_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled: bool = ..., rewriter: _Optional[_Union[_options_pb2.ResolvedASTRewrite, str]] = ..., sql: _Optional[str] = ..., allow_table_references: bool = ..., allowed_function_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class FunctionSignatureOptionsProto(_message.Message):
    __slots__ = ("is_deprecated", "additional_deprecation_warning", "required_language_feature", "is_aliased_signature", "propagates_collation", "uses_operation_collation", "rejects_collation", "rewrite_options")
    IS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DEPRECATION_WARNING_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_LANGUAGE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    IS_ALIASED_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PROPAGATES_COLLATION_FIELD_NUMBER: _ClassVar[int]
    USES_OPERATION_COLLATION_FIELD_NUMBER: _ClassVar[int]
    REJECTS_COLLATION_FIELD_NUMBER: _ClassVar[int]
    REWRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    is_deprecated: bool
    additional_deprecation_warning: _containers.RepeatedCompositeFieldContainer[_deprecation_warning_pb2.FreestandingDeprecationWarning]
    required_language_feature: _containers.RepeatedScalarFieldContainer[_options_pb2.LanguageFeature]
    is_aliased_signature: bool
    propagates_collation: bool
    uses_operation_collation: bool
    rejects_collation: bool
    rewrite_options: FunctionSignatureRewriteOptionsProto
    def __init__(self, is_deprecated: bool = ..., additional_deprecation_warning: _Optional[_Iterable[_Union[_deprecation_warning_pb2.FreestandingDeprecationWarning, _Mapping]]] = ..., required_language_feature: _Optional[_Iterable[_Union[_options_pb2.LanguageFeature, str]]] = ..., is_aliased_signature: bool = ..., propagates_collation: bool = ..., uses_operation_collation: bool = ..., rejects_collation: bool = ..., rewrite_options: _Optional[_Union[FunctionSignatureRewriteOptionsProto, _Mapping]] = ...) -> None: ...

class FunctionSignatureProto(_message.Message):
    __slots__ = ("argument", "return_type", "context_id", "options")
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    argument: _containers.RepeatedCompositeFieldContainer[FunctionArgumentTypeProto]
    return_type: FunctionArgumentTypeProto
    context_id: int
    options: FunctionSignatureOptionsProto
    def __init__(self, argument: _Optional[_Iterable[_Union[FunctionArgumentTypeProto, _Mapping]]] = ..., return_type: _Optional[_Union[FunctionArgumentTypeProto, _Mapping]] = ..., context_id: _Optional[int] = ..., options: _Optional[_Union[FunctionSignatureOptionsProto, _Mapping]] = ...) -> None: ...

class FunctionOptionsProto(_message.Message):
    __slots__ = ("supports_over_clause", "window_ordering_support", "supports_window_framing", "arguments_are_coercible", "is_deprecated", "alias_name", "sql_name", "allow_external_usage", "volatility", "supports_order_by", "required_language_feature", "supports_limit", "supports_null_handling_modifier", "supports_safe_error_mode", "supports_having_modifier", "supports_clamped_between_modifier", "uses_upper_case_sql_name", "may_suppress_side_effects", "module_name_from_import")
    SUPPORTS_OVER_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_ORDERING_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_WINDOW_FRAMING_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_ARE_COERCIBLE_FIELD_NUMBER: _ClassVar[int]
    IS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXTERNAL_USAGE_FIELD_NUMBER: _ClassVar[int]
    VOLATILITY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_LANGUAGE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_NULL_HANDLING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_SAFE_ERROR_MODE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_HAVING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLAMPED_BETWEEN_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    USES_UPPER_CASE_SQL_NAME_FIELD_NUMBER: _ClassVar[int]
    MAY_SUPPRESS_SIDE_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FROM_IMPORT_FIELD_NUMBER: _ClassVar[int]
    supports_over_clause: bool
    window_ordering_support: _function_pb2.FunctionEnums.WindowOrderSupport
    supports_window_framing: bool
    arguments_are_coercible: bool
    is_deprecated: bool
    alias_name: str
    sql_name: str
    allow_external_usage: bool
    volatility: _function_pb2.FunctionEnums.Volatility
    supports_order_by: bool
    required_language_feature: _containers.RepeatedScalarFieldContainer[_options_pb2.LanguageFeature]
    supports_limit: bool
    supports_null_handling_modifier: bool
    supports_safe_error_mode: bool
    supports_having_modifier: bool
    supports_clamped_between_modifier: bool
    uses_upper_case_sql_name: bool
    may_suppress_side_effects: bool
    module_name_from_import: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, supports_over_clause: bool = ..., window_ordering_support: _Optional[_Union[_function_pb2.FunctionEnums.WindowOrderSupport, str]] = ..., supports_window_framing: bool = ..., arguments_are_coercible: bool = ..., is_deprecated: bool = ..., alias_name: _Optional[str] = ..., sql_name: _Optional[str] = ..., allow_external_usage: bool = ..., volatility: _Optional[_Union[_function_pb2.FunctionEnums.Volatility, str]] = ..., supports_order_by: bool = ..., required_language_feature: _Optional[_Iterable[_Union[_options_pb2.LanguageFeature, str]]] = ..., supports_limit: bool = ..., supports_null_handling_modifier: bool = ..., supports_safe_error_mode: bool = ..., supports_having_modifier: bool = ..., supports_clamped_between_modifier: bool = ..., uses_upper_case_sql_name: bool = ..., may_suppress_side_effects: bool = ..., module_name_from_import: _Optional[_Iterable[str]] = ...) -> None: ...

class FunctionProto(_message.Message):
    __slots__ = ("name_path", "group", "mode", "signature", "options", "parse_resume_location", "templated_sql_function_argument_name", "sql_security", "statement_context")
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARSE_RESUME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATED_SQL_FUNCTION_ARGUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name_path: _containers.RepeatedScalarFieldContainer[str]
    group: str
    mode: _function_pb2.FunctionEnums.Mode
    signature: _containers.RepeatedCompositeFieldContainer[FunctionSignatureProto]
    options: FunctionOptionsProto
    parse_resume_location: _parse_resume_location_pb2.ParseResumeLocationProto
    templated_sql_function_argument_name: _containers.RepeatedScalarFieldContainer[str]
    sql_security: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity
    statement_context: _options_pb2.StatementContext
    def __init__(self, name_path: _Optional[_Iterable[str]] = ..., group: _Optional[str] = ..., mode: _Optional[_Union[_function_pb2.FunctionEnums.Mode, str]] = ..., signature: _Optional[_Iterable[_Union[FunctionSignatureProto, _Mapping]]] = ..., options: _Optional[_Union[FunctionOptionsProto, _Mapping]] = ..., parse_resume_location: _Optional[_Union[_parse_resume_location_pb2.ParseResumeLocationProto, _Mapping]] = ..., templated_sql_function_argument_name: _Optional[_Iterable[str]] = ..., sql_security: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity, str]] = ..., statement_context: _Optional[_Union[_options_pb2.StatementContext, str]] = ...) -> None: ...

class ResolvedFunctionCallInfoProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TableValuedFunctionOptionsProto(_message.Message):
    __slots__ = ("uses_upper_case_sql_name", "required_language_feature")
    USES_UPPER_CASE_SQL_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_LANGUAGE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    uses_upper_case_sql_name: bool
    required_language_feature: _containers.RepeatedScalarFieldContainer[_options_pb2.LanguageFeature]
    def __init__(self, uses_upper_case_sql_name: bool = ..., required_language_feature: _Optional[_Iterable[_Union[_options_pb2.LanguageFeature, str]]] = ...) -> None: ...

class TableValuedFunctionProto(_message.Message):
    __slots__ = ("name_path", "signature", "signatures", "options", "type", "volatility", "parse_resume_location", "argument_name", "custom_context", "anonymization_info", "statement_context", "group")
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLATILITY_FIELD_NUMBER: _ClassVar[int]
    PARSE_RESUME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ANONYMIZATION_INFO_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    name_path: _containers.RepeatedScalarFieldContainer[str]
    signature: FunctionSignatureProto
    signatures: _containers.RepeatedCompositeFieldContainer[FunctionSignatureProto]
    options: TableValuedFunctionOptionsProto
    type: _function_pb2.FunctionEnums.TableValuedFunctionType
    volatility: _function_pb2.FunctionEnums.Volatility
    parse_resume_location: _parse_resume_location_pb2.ParseResumeLocationProto
    argument_name: _containers.RepeatedScalarFieldContainer[str]
    custom_context: str
    anonymization_info: _simple_table_pb2.SimpleAnonymizationInfoProto
    statement_context: _options_pb2.StatementContext
    group: str
    def __init__(self, name_path: _Optional[_Iterable[str]] = ..., signature: _Optional[_Union[FunctionSignatureProto, _Mapping]] = ..., signatures: _Optional[_Iterable[_Union[FunctionSignatureProto, _Mapping]]] = ..., options: _Optional[_Union[TableValuedFunctionOptionsProto, _Mapping]] = ..., type: _Optional[_Union[_function_pb2.FunctionEnums.TableValuedFunctionType, str]] = ..., volatility: _Optional[_Union[_function_pb2.FunctionEnums.Volatility, str]] = ..., parse_resume_location: _Optional[_Union[_parse_resume_location_pb2.ParseResumeLocationProto, _Mapping]] = ..., argument_name: _Optional[_Iterable[str]] = ..., custom_context: _Optional[str] = ..., anonymization_info: _Optional[_Union[_simple_table_pb2.SimpleAnonymizationInfoProto, _Mapping]] = ..., statement_context: _Optional[_Union[_options_pb2.StatementContext, str]] = ..., group: _Optional[str] = ...) -> None: ...

class TVFArgumentProto(_message.Message):
    __slots__ = ("scalar_argument", "relation_argument", "model_argument", "connection_argument", "descriptor_argument", "graph_argument")
    SCALAR_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    RELATION_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    scalar_argument: _serialization_pb2.ValueWithTypeProto
    relation_argument: TVFRelationProto
    model_argument: TVFModelProto
    connection_argument: TVFConnectionProto
    descriptor_argument: TVFDescriptorProto
    graph_argument: TVFGraphProto
    def __init__(self, scalar_argument: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., relation_argument: _Optional[_Union[TVFRelationProto, _Mapping]] = ..., model_argument: _Optional[_Union[TVFModelProto, _Mapping]] = ..., connection_argument: _Optional[_Union[TVFConnectionProto, _Mapping]] = ..., descriptor_argument: _Optional[_Union[TVFDescriptorProto, _Mapping]] = ..., graph_argument: _Optional[_Union[TVFGraphProto, _Mapping]] = ...) -> None: ...

class TVFSignatureOptionsProto(_message.Message):
    __slots__ = ("additional_deprecation_warning",)
    ADDITIONAL_DEPRECATION_WARNING_FIELD_NUMBER: _ClassVar[int]
    additional_deprecation_warning: _containers.RepeatedCompositeFieldContainer[_deprecation_warning_pb2.FreestandingDeprecationWarning]
    def __init__(self, additional_deprecation_warning: _Optional[_Iterable[_Union[_deprecation_warning_pb2.FreestandingDeprecationWarning, _Mapping]]] = ...) -> None: ...

class TVFSignatureProto(_message.Message):
    __slots__ = ("argument", "options", "output_schema", "output_table_schema")
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    argument: _containers.RepeatedCompositeFieldContainer[TVFArgumentProto]
    options: TVFSignatureOptionsProto
    output_schema: TVFRelationProto
    output_table_schema: _serialization_pb2.TableRefProto
    def __init__(self, argument: _Optional[_Iterable[_Union[TVFArgumentProto, _Mapping]]] = ..., options: _Optional[_Union[TVFSignatureOptionsProto, _Mapping]] = ..., output_schema: _Optional[_Union[TVFRelationProto, _Mapping]] = ..., output_table_schema: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ...) -> None: ...

class ProcedureProto(_message.Message):
    __slots__ = ("name_path", "signature")
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    name_path: _containers.RepeatedScalarFieldContainer[str]
    signature: FunctionSignatureProto
    def __init__(self, name_path: _Optional[_Iterable[str]] = ..., signature: _Optional[_Union[FunctionSignatureProto, _Mapping]] = ...) -> None: ...
