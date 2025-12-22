from zetasql.wasi._pb2.zetasql.public import builtin_function_pb2 as _builtin_function_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as _options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2 as _type_pb2
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_node_kind_pb2 as _resolved_node_kind_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZetaSQLBuiltinFunctionOptionsProto(_message.Message):
    __slots__ = ("language_options", "include_function_ids", "exclude_function_ids", "enabled_rewrites_map_entry")
    LANGUAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FUNCTION_IDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FUNCTION_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_REWRITES_MAP_ENTRY_FIELD_NUMBER: _ClassVar[int]
    language_options: LanguageOptionsProto
    include_function_ids: _containers.RepeatedScalarFieldContainer[_builtin_function_pb2.FunctionSignatureId]
    exclude_function_ids: _containers.RepeatedScalarFieldContainer[_builtin_function_pb2.FunctionSignatureId]
    enabled_rewrites_map_entry: _containers.RepeatedCompositeFieldContainer[EnabledRewriteProto]
    def __init__(self, language_options: _Optional[_Union[LanguageOptionsProto, _Mapping]] = ..., include_function_ids: _Optional[_Iterable[_Union[_builtin_function_pb2.FunctionSignatureId, str]]] = ..., exclude_function_ids: _Optional[_Iterable[_Union[_builtin_function_pb2.FunctionSignatureId, str]]] = ..., enabled_rewrites_map_entry: _Optional[_Iterable[_Union[EnabledRewriteProto, _Mapping]]] = ...) -> None: ...

class EnabledRewriteProto(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: _builtin_function_pb2.FunctionSignatureId
    value: bool
    def __init__(self, key: _Optional[_Union[_builtin_function_pb2.FunctionSignatureId, str]] = ..., value: bool = ...) -> None: ...

class LanguageOptionsProto(_message.Message):
    __slots__ = ("name_resolution_mode", "product_mode", "error_on_deprecated_syntax", "enabled_language_features", "supported_statement_kinds", "supported_generic_entity_types", "reserved_keywords", "supported_generic_sub_entity_types")
    NAME_RESOLUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_MODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_ON_DEPRECATED_SYNTAX_FIELD_NUMBER: _ClassVar[int]
    ENABLED_LANGUAGE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_STATEMENT_KINDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_GENERIC_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESERVED_KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_GENERIC_SUB_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    name_resolution_mode: _options_pb2.NameResolutionMode
    product_mode: _options_pb2.ProductMode
    error_on_deprecated_syntax: bool
    enabled_language_features: _containers.RepeatedScalarFieldContainer[_options_pb2.LanguageFeature]
    supported_statement_kinds: _containers.RepeatedScalarFieldContainer[_resolved_node_kind_pb2.ResolvedNodeKind]
    supported_generic_entity_types: _containers.RepeatedScalarFieldContainer[str]
    reserved_keywords: _containers.RepeatedScalarFieldContainer[str]
    supported_generic_sub_entity_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name_resolution_mode: _Optional[_Union[_options_pb2.NameResolutionMode, str]] = ..., product_mode: _Optional[_Union[_options_pb2.ProductMode, str]] = ..., error_on_deprecated_syntax: bool = ..., enabled_language_features: _Optional[_Iterable[_Union[_options_pb2.LanguageFeature, str]]] = ..., supported_statement_kinds: _Optional[_Iterable[_Union[_resolved_node_kind_pb2.ResolvedNodeKind, str]]] = ..., supported_generic_entity_types: _Optional[_Iterable[str]] = ..., reserved_keywords: _Optional[_Iterable[str]] = ..., supported_generic_sub_entity_types: _Optional[_Iterable[str]] = ...) -> None: ...

class AllowedHintsAndOptionsProto(_message.Message):
    __slots__ = ("disallow_unknown_options", "disallow_unknown_hints_with_qualifier", "hint", "option", "anonymization_option", "differential_privacy_option", "disallow_duplicate_option_names")
    class HintProto(_message.Message):
        __slots__ = ("qualifier", "name", "type", "allow_unqualified")
        QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_UNQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        qualifier: str
        name: str
        type: _type_pb2.TypeProto
        allow_unqualified: bool
        def __init__(self, qualifier: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., allow_unqualified: bool = ...) -> None: ...
    class OptionProto(_message.Message):
        __slots__ = ("name", "type", "resolving_kind", "allow_alter_array")
        class ResolvingKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONSTANT_OR_EMPTY_NAME_SCOPE_IDENTIFIER: _ClassVar[AllowedHintsAndOptionsProto.OptionProto.ResolvingKind]
            FROM_NAME_SCOPE_IDENTIFIER: _ClassVar[AllowedHintsAndOptionsProto.OptionProto.ResolvingKind]
        CONSTANT_OR_EMPTY_NAME_SCOPE_IDENTIFIER: AllowedHintsAndOptionsProto.OptionProto.ResolvingKind
        FROM_NAME_SCOPE_IDENTIFIER: AllowedHintsAndOptionsProto.OptionProto.ResolvingKind
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOLVING_KIND_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ALTER_ARRAY_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: _type_pb2.TypeProto
        resolving_kind: AllowedHintsAndOptionsProto.OptionProto.ResolvingKind
        allow_alter_array: bool
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., resolving_kind: _Optional[_Union[AllowedHintsAndOptionsProto.OptionProto.ResolvingKind, str]] = ..., allow_alter_array: bool = ...) -> None: ...
    DISALLOW_UNKNOWN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_UNKNOWN_HINTS_WITH_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    OPTION_FIELD_NUMBER: _ClassVar[int]
    ANONYMIZATION_OPTION_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_PRIVACY_OPTION_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_DUPLICATE_OPTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    disallow_unknown_options: bool
    disallow_unknown_hints_with_qualifier: _containers.RepeatedScalarFieldContainer[str]
    hint: _containers.RepeatedCompositeFieldContainer[AllowedHintsAndOptionsProto.HintProto]
    option: _containers.RepeatedCompositeFieldContainer[AllowedHintsAndOptionsProto.OptionProto]
    anonymization_option: _containers.RepeatedCompositeFieldContainer[AllowedHintsAndOptionsProto.OptionProto]
    differential_privacy_option: _containers.RepeatedCompositeFieldContainer[AllowedHintsAndOptionsProto.OptionProto]
    disallow_duplicate_option_names: bool
    def __init__(self, disallow_unknown_options: bool = ..., disallow_unknown_hints_with_qualifier: _Optional[_Iterable[str]] = ..., hint: _Optional[_Iterable[_Union[AllowedHintsAndOptionsProto.HintProto, _Mapping]]] = ..., option: _Optional[_Iterable[_Union[AllowedHintsAndOptionsProto.OptionProto, _Mapping]]] = ..., anonymization_option: _Optional[_Iterable[_Union[AllowedHintsAndOptionsProto.OptionProto, _Mapping]]] = ..., differential_privacy_option: _Optional[_Iterable[_Union[AllowedHintsAndOptionsProto.OptionProto, _Mapping]]] = ..., disallow_duplicate_option_names: bool = ...) -> None: ...

class AnalyzerOptionsProto(_message.Message):
    __slots__ = ("language_options", "query_parameters", "positional_query_parameters", "expression_columns", "in_scope_expression_column", "ddl_pseudo_columns", "error_message_mode", "default_timezone", "create_new_column_for_each_projected_output", "prune_unused_columns", "allow_undeclared_parameters", "parameter_mode", "allowed_hints_and_options", "statement_context", "preserve_column_aliases", "system_variables", "target_column_types", "enabled_rewrites", "parse_location_record_type", "preserve_unnecessary_cast", "default_anon_function_report_format", "default_anon_kappa_value", "rewrite_options", "replace_table_not_found_error_with_tvf_error_if_applicable", "log_impact_of_lateral_column_references")
    class QueryParameterProto(_message.Message):
        __slots__ = ("name", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: _type_pb2.TypeProto
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...
    class SystemVariableProto(_message.Message):
        __slots__ = ("name_path", "type")
        NAME_PATH_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name_path: _containers.RepeatedScalarFieldContainer[str]
        type: _type_pb2.TypeProto
        def __init__(self, name_path: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...
    LANGUAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    IN_SCOPE_EXPRESSION_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DDL_PSEUDO_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_COLUMN_FOR_EACH_PROJECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PRUNE_UNUSED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UNDECLARED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MODE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_HINTS_AND_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_COLUMN_ALIASES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_TYPES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_REWRITES_FIELD_NUMBER: _ClassVar[int]
    PARSE_LOCATION_RECORD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_UNNECESSARY_CAST_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ANON_FUNCTION_REPORT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ANON_KAPPA_VALUE_FIELD_NUMBER: _ClassVar[int]
    REWRITE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_TABLE_NOT_FOUND_ERROR_WITH_TVF_ERROR_IF_APPLICABLE_FIELD_NUMBER: _ClassVar[int]
    LOG_IMPACT_OF_LATERAL_COLUMN_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    language_options: LanguageOptionsProto
    query_parameters: _containers.RepeatedCompositeFieldContainer[AnalyzerOptionsProto.QueryParameterProto]
    positional_query_parameters: _containers.RepeatedCompositeFieldContainer[_type_pb2.TypeProto]
    expression_columns: _containers.RepeatedCompositeFieldContainer[AnalyzerOptionsProto.QueryParameterProto]
    in_scope_expression_column: AnalyzerOptionsProto.QueryParameterProto
    ddl_pseudo_columns: _containers.RepeatedCompositeFieldContainer[AnalyzerOptionsProto.QueryParameterProto]
    error_message_mode: _options_pb2.ErrorMessageMode
    default_timezone: str
    create_new_column_for_each_projected_output: bool
    prune_unused_columns: bool
    allow_undeclared_parameters: bool
    parameter_mode: _options_pb2.ParameterMode
    allowed_hints_and_options: AllowedHintsAndOptionsProto
    statement_context: _options_pb2.StatementContext
    preserve_column_aliases: bool
    system_variables: _containers.RepeatedCompositeFieldContainer[AnalyzerOptionsProto.SystemVariableProto]
    target_column_types: _containers.RepeatedCompositeFieldContainer[_type_pb2.TypeProto]
    enabled_rewrites: _containers.RepeatedScalarFieldContainer[_options_pb2.ResolvedASTRewrite]
    parse_location_record_type: _options_pb2.ParseLocationRecordType
    preserve_unnecessary_cast: bool
    default_anon_function_report_format: str
    default_anon_kappa_value: int
    rewrite_options: _options_pb2.RewriteOptions
    replace_table_not_found_error_with_tvf_error_if_applicable: bool
    log_impact_of_lateral_column_references: bool
    def __init__(self, language_options: _Optional[_Union[LanguageOptionsProto, _Mapping]] = ..., query_parameters: _Optional[_Iterable[_Union[AnalyzerOptionsProto.QueryParameterProto, _Mapping]]] = ..., positional_query_parameters: _Optional[_Iterable[_Union[_type_pb2.TypeProto, _Mapping]]] = ..., expression_columns: _Optional[_Iterable[_Union[AnalyzerOptionsProto.QueryParameterProto, _Mapping]]] = ..., in_scope_expression_column: _Optional[_Union[AnalyzerOptionsProto.QueryParameterProto, _Mapping]] = ..., ddl_pseudo_columns: _Optional[_Iterable[_Union[AnalyzerOptionsProto.QueryParameterProto, _Mapping]]] = ..., error_message_mode: _Optional[_Union[_options_pb2.ErrorMessageMode, str]] = ..., default_timezone: _Optional[str] = ..., create_new_column_for_each_projected_output: bool = ..., prune_unused_columns: bool = ..., allow_undeclared_parameters: bool = ..., parameter_mode: _Optional[_Union[_options_pb2.ParameterMode, str]] = ..., allowed_hints_and_options: _Optional[_Union[AllowedHintsAndOptionsProto, _Mapping]] = ..., statement_context: _Optional[_Union[_options_pb2.StatementContext, str]] = ..., preserve_column_aliases: bool = ..., system_variables: _Optional[_Iterable[_Union[AnalyzerOptionsProto.SystemVariableProto, _Mapping]]] = ..., target_column_types: _Optional[_Iterable[_Union[_type_pb2.TypeProto, _Mapping]]] = ..., enabled_rewrites: _Optional[_Iterable[_Union[_options_pb2.ResolvedASTRewrite, str]]] = ..., parse_location_record_type: _Optional[_Union[_options_pb2.ParseLocationRecordType, str]] = ..., preserve_unnecessary_cast: bool = ..., default_anon_function_report_format: _Optional[str] = ..., default_anon_kappa_value: _Optional[int] = ..., rewrite_options: _Optional[_Union[_options_pb2.RewriteOptions, _Mapping]] = ..., replace_table_not_found_error_with_tvf_error_if_applicable: bool = ..., log_impact_of_lateral_column_references: bool = ...) -> None: ...
