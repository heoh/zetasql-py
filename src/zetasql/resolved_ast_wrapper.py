"""
ZetaSQL ResolvedAST Python Wrappers

Auto-generated wrapper classes for convenient proto field access.
DO NOT EDIT MANUALLY - regenerate with scripts/generate_wrappers.py

Usage:
    from zetasql.resolved_ast_wrapper import ResolvedLiteral
    
    proto = resolved_ast_pb2.ResolvedLiteralProto()
    wrapper = ResolvedLiteral(proto)
    
    # Convenient access with IDE autocompletion
    print(wrapper.value)  # Instead of proto.value
    print(wrapper.type)   # Instead of proto.parent.type
"""

from __future__ import annotations
from functools import cached_property
from typing import Optional, List, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
    from zetasql.wasi._pb2.zetasql.resolved_ast import serialization_pb2


class ASTNode:
    """Generated wrapper for ASTNodeProto"""

    def __init__(self, proto: 'ASTNodeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parse_location_range



class AllowedHintsAndOptions:
    """Generated wrapper for AllowedHintsAndOptionsProto"""

    def __init__(self, proto: 'AllowedHintsAndOptionsProto'):
        self._proto = proto

    @cached_property
    def disallow_unknown_options(self) -> Optional[bool]:
        """Field disallow_unknown_options"""
        return self._proto.disallow_unknown_options

    @cached_property
    def disallow_unknown_hints_with_qualifier(self) -> List[str]:
        """Field disallow_unknown_hints_with_qualifier"""
        return self._proto.disallow_unknown_hints_with_qualifier

    @cached_property
    def hint(self) -> List['HintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def option(self) -> List['OptionProto']:
        """Field option"""
        return self._proto.option

    @cached_property
    def anonymization_option(self) -> List['OptionProto']:
        """Field anonymization_option"""
        return self._proto.anonymization_option

    @cached_property
    def differential_privacy_option(self) -> List['OptionProto']:
        """Field differential_privacy_option"""
        return self._proto.differential_privacy_option

    @cached_property
    def disallow_duplicate_option_names(self) -> Optional[bool]:
        """Field disallow_duplicate_option_names"""
        return self._proto.disallow_duplicate_option_names



class AnalyzerOptions:
    """Generated wrapper for AnalyzerOptionsProto"""

    def __init__(self, proto: 'AnalyzerOptionsProto'):
        self._proto = proto

    @cached_property
    def language_options(self) -> Optional['LanguageOptionsProto']:
        """Field language_options"""
        return self._proto.language_options

    @cached_property
    def query_parameters(self) -> List['QueryParameterProto']:
        """Field query_parameters"""
        return self._proto.query_parameters

    @cached_property
    def positional_query_parameters(self) -> List['TypeProto']:
        """Field positional_query_parameters"""
        return self._proto.positional_query_parameters

    @cached_property
    def expression_columns(self) -> List['QueryParameterProto']:
        """Field expression_columns"""
        return self._proto.expression_columns

    @cached_property
    def in_scope_expression_column(self) -> Optional['QueryParameterProto']:
        """Field in_scope_expression_column"""
        return self._proto.in_scope_expression_column

    @cached_property
    def ddl_pseudo_columns(self) -> List['QueryParameterProto']:
        """Field ddl_pseudo_columns"""
        return self._proto.ddl_pseudo_columns

    @cached_property
    def error_message_mode(self) -> Optional[int]:
        """Field error_message_mode"""
        return self._proto.error_message_mode

    @cached_property
    def default_timezone(self) -> Optional[str]:
        """Field default_timezone"""
        return self._proto.default_timezone

    @cached_property
    def create_new_column_for_each_projected_output(self) -> Optional[bool]:
        """Field create_new_column_for_each_projected_output"""
        return self._proto.create_new_column_for_each_projected_output

    @cached_property
    def prune_unused_columns(self) -> Optional[bool]:
        """Field prune_unused_columns"""
        return self._proto.prune_unused_columns

    @cached_property
    def allow_undeclared_parameters(self) -> Optional[bool]:
        """Field allow_undeclared_parameters"""
        return self._proto.allow_undeclared_parameters

    @cached_property
    def parameter_mode(self) -> Optional[int]:
        """Field parameter_mode"""
        return self._proto.parameter_mode

    @cached_property
    def allowed_hints_and_options(self) -> Optional['AllowedHintsAndOptionsProto']:
        """Field allowed_hints_and_options"""
        return self._proto.allowed_hints_and_options

    @cached_property
    def statement_context(self) -> Optional[int]:
        """Field statement_context"""
        return self._proto.statement_context

    @cached_property
    def preserve_column_aliases(self) -> Optional[bool]:
        """Field preserve_column_aliases"""
        return self._proto.preserve_column_aliases

    @cached_property
    def system_variables(self) -> List['SystemVariableProto']:
        """Field system_variables"""
        return self._proto.system_variables

    @cached_property
    def target_column_types(self) -> List['TypeProto']:
        """Field target_column_types"""
        return self._proto.target_column_types

    @cached_property
    def enabled_rewrites(self) -> List[int]:
        """Field enabled_rewrites"""
        return self._proto.enabled_rewrites

    @cached_property
    def parse_location_record_type(self) -> Optional[int]:
        """Field parse_location_record_type"""
        return self._proto.parse_location_record_type

    @cached_property
    def preserve_unnecessary_cast(self) -> Optional[bool]:
        """Field preserve_unnecessary_cast"""
        return self._proto.preserve_unnecessary_cast

    @cached_property
    def default_anon_function_report_format(self) -> Optional[str]:
        """Field default_anon_function_report_format"""
        return self._proto.default_anon_function_report_format

    @cached_property
    def default_anon_kappa_value(self) -> Optional[int]:
        """Field default_anon_kappa_value"""
        return self._proto.default_anon_kappa_value

    @cached_property
    def rewrite_options(self) -> Optional['RewriteOptions']:
        """Field rewrite_options"""
        return self._proto.rewrite_options

    @cached_property
    def replace_table_not_found_error_with_tvf_error_if_applicable(self) -> Optional[bool]:
        """Field replace_table_not_found_error_with_tvf_error_if_applicable"""
        return self._proto.replace_table_not_found_error_with_tvf_error_if_applicable

    @cached_property
    def log_impact_of_lateral_column_references(self) -> Optional[bool]:
        """Field log_impact_of_lateral_column_references"""
        return self._proto.log_impact_of_lateral_column_references



class AnnotationMap:
    """Generated wrapper for AnnotationMapProto"""

    def __init__(self, proto: 'AnnotationMapProto'):
        self._proto = proto

    @cached_property
    def is_null(self) -> Optional[bool]:
        """Field is_null"""
        return self._proto.is_null

    @cached_property
    def annotations(self) -> List['AnnotationProto']:
        """Field annotations"""
        return self._proto.annotations

    @cached_property
    def array_element(self) -> Optional['AnnotationMapProto']:
        """Field array_element"""
        return self._proto.array_element

    @cached_property
    def struct_fields(self) -> List['AnnotationMapProto']:
        """Field struct_fields"""
        return self._proto.struct_fields



class Annotation:
    """Generated wrapper for AnnotationProto"""

    def __init__(self, proto: 'AnnotationProto'):
        self._proto = proto

    @cached_property
    def id(self) -> Optional[int]:
        """Field id"""
        return self._proto.id

    @cached_property
    def value(self) -> Optional['SimpleValueProto']:
        """Field value"""
        return self._proto.value



class ArgumentTypeLambda:
    """Generated wrapper for ArgumentTypeLambdaProto"""

    def __init__(self, proto: 'ArgumentTypeLambdaProto'):
        self._proto = proto

    @cached_property
    def argument(self) -> List['FunctionArgumentTypeProto']:
        """Field argument"""
        return self._proto.argument

    @cached_property
    def body(self) -> Optional['FunctionArgumentTypeProto']:
        """Field body"""
        return self._proto.body



class ArrayType:
    """Generated wrapper for ArrayTypeProto"""

    def __init__(self, proto: 'ArrayTypeProto'):
        self._proto = proto

    @cached_property
    def element_type(self) -> Optional['TypeProto']:
        """Field element_type"""
        return self._proto.element_type



class Collation:
    """Generated wrapper for CollationProto"""

    def __init__(self, proto: 'CollationProto'):
        self._proto = proto

    @cached_property
    def collation_name(self) -> Optional[str]:
        """Field collation_name"""
        return self._proto.collation_name

    @cached_property
    def child_list(self) -> List['CollationProto']:
        """Field child_list"""
        return self._proto.child_list



class ColumnRef:
    """Generated wrapper for ColumnRefProto"""

    def __init__(self, proto: 'ColumnRefProto'):
        self._proto = proto

    @cached_property
    def table_ref(self) -> Optional['TableRefProto']:
        """Field table_ref"""
        return self._proto.table_ref

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class CompiledPattern:
    """Generated wrapper for CompiledPatternProto"""

    def __init__(self, proto: 'CompiledPatternProto'):
        self._proto = proto

    @cached_property
    def state_machine(self) -> Optional['StateMachineProto']:
        """Field state_machine"""
        return self._proto.state_machine



class ConnectionRef:
    """Generated wrapper for ConnectionRefProto"""

    def __init__(self, proto: 'ConnectionRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class ConstantRef:
    """Generated wrapper for ConstantRefProto"""

    def __init__(self, proto: 'ConstantRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class ConstnessLevel:
    """Generated wrapper for ConstnessLevelProto"""

    def __init__(self, proto: 'ConstnessLevelProto'):
        self._proto = proto


class DescriptorPoolList:
    """Generated wrapper for DescriptorPoolListProto"""

    def __init__(self, proto: 'DescriptorPoolListProto'):
        self._proto = proto

    @cached_property
    def definitions(self) -> List['Definition']:
        """Field definitions"""
        return self._proto.definitions



class EnabledRewrite:
    """Generated wrapper for EnabledRewriteProto"""

    def __init__(self, proto: 'EnabledRewriteProto'):
        self._proto = proto

    @cached_property
    def key(self) -> Optional[int]:
        """Field key"""
        return self._proto.key

    @cached_property
    def value(self) -> Optional[bool]:
        """Field value"""
        return self._proto.value



class EnumType:
    """Generated wrapper for EnumTypeProto"""

    def __init__(self, proto: 'EnumTypeProto'):
        self._proto = proto

    @cached_property
    def enum_name(self) -> Optional[str]:
        """Field enum_name"""
        return self._proto.enum_name

    @cached_property
    def enum_file_name(self) -> Optional[str]:
        """Field enum_file_name"""
        return self._proto.enum_file_name

    @cached_property
    def file_descriptor_set_index(self) -> Optional[int]:
        """Field file_descriptor_set_index"""
        return self._proto.file_descriptor_set_index

    @cached_property
    def catalog_name_path(self) -> List[str]:
        """Field catalog_name_path"""
        return self._proto.catalog_name_path

    @cached_property
    def is_opaque(self) -> Optional[bool]:
        """Field is_opaque"""
        return self._proto.is_opaque



class EvaluatorTableIterator:
    """Generated wrapper for EvaluatorTableIteratorProto"""

    def __init__(self, proto: 'EvaluatorTableIteratorProto'):
        self._proto = proto

    @cached_property
    def location_byte_offset(self) -> Optional[int]:
        """Field location_byte_offset"""
        return self._proto.location_byte_offset

    @cached_property
    def next_row_count(self) -> Optional[int]:
        """Field next_row_count"""
        return self._proto.next_row_count



class ExpressionAttribute:
    """Generated wrapper for ExpressionAttributeProto"""

    def __init__(self, proto: 'ExpressionAttributeProto'):
        self._proto = proto

    @cached_property
    def expression_string(self) -> Optional[str]:
        """Field expression_string"""
        return self._proto.expression_string

    @cached_property
    def expression_kind(self) -> Optional[int]:
        """Field expression_kind"""
        return self._proto.expression_kind

    @cached_property
    def row_identity_column_index(self) -> List[int]:
        """Field row_identity_column_index"""
        return self._proto.row_identity_column_index



class ExtendedTypeParameters:
    """Generated wrapper for ExtendedTypeParametersProto"""

    def __init__(self, proto: 'ExtendedTypeParametersProto'):
        self._proto = proto

    @cached_property
    def parameters(self) -> List['SimpleValueProto']:
        """Field parameters"""
        return self._proto.parameters



class FeatureLabelDictionary:
    """Generated wrapper for FeatureLabelDictionaryProto"""

    def __init__(self, proto: 'FeatureLabelDictionaryProto'):
        self._proto = proto

    @cached_property
    def label_mapping(self) -> List['LabelMappingEntry']:
        """Field label_mapping"""
        return self._proto.label_mapping

    @cached_property
    def encoded_labels(self) -> List['EncodedLabelsEntry']:
        """Field encoded_labels"""
        return self._proto.encoded_labels



class FieldDescriptorRef:
    """Generated wrapper for FieldDescriptorRefProto"""

    def __init__(self, proto: 'FieldDescriptorRefProto'):
        self._proto = proto

    @cached_property
    def containing_proto(self) -> Optional['ProtoTypeProto']:
        """Field containing_proto"""
        return self._proto.containing_proto

    @cached_property
    def number(self) -> Optional[int]:
        """Field number"""
        return self._proto.number



class FormatterOptions:
    """Generated wrapper for FormatterOptionsProto"""

    def __init__(self, proto: 'FormatterOptionsProto'):
        self._proto = proto

    @cached_property
    def new_line_type(self) -> Optional[str]:
        """Field new_line_type"""
        return self._proto.new_line_type

    @cached_property
    def line_length_limit(self) -> Optional[int]:
        """Field line_length_limit"""
        return self._proto.line_length_limit

    @cached_property
    def indentation_spaces(self) -> Optional[int]:
        """Field indentation_spaces"""
        return self._proto.indentation_spaces

    @cached_property
    def allow_invalid_tokens(self) -> Optional[bool]:
        """Field allow_invalid_tokens"""
        return self._proto.allow_invalid_tokens

    @cached_property
    def capitalize_keywords(self) -> Optional[bool]:
        """Field capitalize_keywords"""
        return self._proto.capitalize_keywords

    @cached_property
    def preserve_line_breaks(self) -> Optional[bool]:
        """Field preserve_line_breaks"""
        return self._proto.preserve_line_breaks

    @cached_property
    def expand_format_ranges(self) -> Optional[bool]:
        """Field expand_format_ranges"""
        return self._proto.expand_format_ranges

    @cached_property
    def enforce_single_quotes(self) -> Optional[bool]:
        """Field enforce_single_quotes"""
        return self._proto.enforce_single_quotes

    @cached_property
    def capitalize_functions(self) -> Optional[bool]:
        """Field capitalize_functions"""
        return self._proto.capitalize_functions

    @cached_property
    def format_structured_strings(self) -> Optional[bool]:
        """Field format_structured_strings"""
        return self._proto.format_structured_strings

    @cached_property
    def format_comments(self) -> Optional[bool]:
        """Field format_comments"""
        return self._proto.format_comments



class FormatterRange:
    """Generated wrapper for FormatterRangeProto"""

    def __init__(self, proto: 'FormatterRangeProto'):
        self._proto = proto

    @cached_property
    def start(self) -> Optional[int]:
        """Field start"""
        return self._proto.start

    @cached_property
    def end(self) -> Optional[int]:
        """Field end"""
        return self._proto.end



class FunctionArgumentTypeOptions:
    """Generated wrapper for FunctionArgumentTypeOptionsProto"""

    def __init__(self, proto: 'FunctionArgumentTypeOptionsProto'):
        self._proto = proto

    @cached_property
    def cardinality(self) -> Optional[int]:
        """Field cardinality"""
        return self._proto.cardinality

    @cached_property
    def must_be_constant(self) -> Optional[bool]:
        """Field must_be_constant"""
        return self._proto.must_be_constant

    @cached_property
    def must_be_non_null(self) -> Optional[bool]:
        """Field must_be_non_null"""
        return self._proto.must_be_non_null

    @cached_property
    def is_not_aggregate(self) -> Optional[bool]:
        """Field is_not_aggregate"""
        return self._proto.is_not_aggregate

    @cached_property
    def must_support_equality(self) -> Optional[bool]:
        """Field must_support_equality"""
        return self._proto.must_support_equality

    @cached_property
    def must_support_ordering(self) -> Optional[bool]:
        """Field must_support_ordering"""
        return self._proto.must_support_ordering

    @cached_property
    def min_value(self) -> Optional[int]:
        """Field min_value"""
        return self._proto.min_value

    @cached_property
    def max_value(self) -> Optional[int]:
        """Field max_value"""
        return self._proto.max_value

    @cached_property
    def extra_relation_input_columns_allowed(self) -> Optional[bool]:
        """Field extra_relation_input_columns_allowed"""
        return self._proto.extra_relation_input_columns_allowed

    @cached_property
    def relation_input_schema(self) -> Optional['TVFRelationProto']:
        """Field relation_input_schema"""
        return self._proto.relation_input_schema

    @cached_property
    def argument_name(self) -> Optional[str]:
        """Field argument_name"""
        return self._proto.argument_name

    @cached_property
    def argument_name_parse_location(self) -> Optional['ParseLocationRangeProto']:
        """Field argument_name_parse_location"""
        return self._proto.argument_name_parse_location

    @cached_property
    def argument_type_parse_location(self) -> Optional['ParseLocationRangeProto']:
        """Field argument_type_parse_location"""
        return self._proto.argument_type_parse_location

    @cached_property
    def procedure_argument_mode(self) -> Optional[int]:
        """Field procedure_argument_mode"""
        return self._proto.procedure_argument_mode

    @cached_property
    def argument_name_is_mandatory(self) -> Optional[bool]:
        """Field argument_name_is_mandatory"""
        return self._proto.argument_name_is_mandatory

    @cached_property
    def descriptor_resolution_table_offset(self) -> Optional[int]:
        """Field descriptor_resolution_table_offset"""
        return self._proto.descriptor_resolution_table_offset

    @cached_property
    def default_value(self) -> Optional['ValueProto']:
        """Field default_value"""
        return self._proto.default_value

    @cached_property
    def default_value_type(self) -> Optional['TypeProto']:
        """Field default_value_type"""
        return self._proto.default_value_type

    @cached_property
    def argument_collation_mode(self) -> Optional[int]:
        """Field argument_collation_mode"""
        return self._proto.argument_collation_mode

    @cached_property
    def uses_array_element_for_collation(self) -> Optional[bool]:
        """Field uses_array_element_for_collation"""
        return self._proto.uses_array_element_for_collation

    @cached_property
    def must_support_grouping(self) -> Optional[bool]:
        """Field must_support_grouping"""
        return self._proto.must_support_grouping

    @cached_property
    def array_element_must_support_equality(self) -> Optional[bool]:
        """Field array_element_must_support_equality"""
        return self._proto.array_element_must_support_equality

    @cached_property
    def array_element_must_support_ordering(self) -> Optional[bool]:
        """Field array_element_must_support_ordering"""
        return self._proto.array_element_must_support_ordering

    @cached_property
    def array_element_must_support_grouping(self) -> Optional[bool]:
        """Field array_element_must_support_grouping"""
        return self._proto.array_element_must_support_grouping

    @cached_property
    def named_argument_kind(self) -> Optional[int]:
        """Field named_argument_kind"""
        return self._proto.named_argument_kind

    @cached_property
    def argument_alias_kind(self) -> Optional[int]:
        """Field argument_alias_kind"""
        return self._proto.argument_alias_kind

    @cached_property
    def must_be_constant_expression(self) -> Optional[bool]:
        """Field must_be_constant_expression"""
        return self._proto.must_be_constant_expression

    @cached_property
    def constness_level(self) -> Optional[int]:
        """Field constness_level"""
        return self._proto.constness_level



class FunctionArgumentType:
    """Generated wrapper for FunctionArgumentTypeProto"""

    def __init__(self, proto: 'FunctionArgumentTypeProto'):
        self._proto = proto

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def num_occurrences(self) -> Optional[int]:
        """Field num_occurrences"""
        return self._proto.num_occurrences

    @cached_property
    def options(self) -> Optional['FunctionArgumentTypeOptionsProto']:
        """Field options"""
        return self._proto.options

    @cached_property
    def lambda_(self) -> Optional['ArgumentTypeLambdaProto']:
        """Field lambda (escaped from reserved keyword 'lambda')"""
        return getattr(self._proto, 'lambda')



class FunctionOptions:
    """Generated wrapper for FunctionOptionsProto"""

    def __init__(self, proto: 'FunctionOptionsProto'):
        self._proto = proto

    @cached_property
    def supports_over_clause(self) -> Optional[bool]:
        """Field supports_over_clause"""
        return self._proto.supports_over_clause

    @cached_property
    def window_ordering_support(self) -> Optional[int]:
        """Field window_ordering_support"""
        return self._proto.window_ordering_support

    @cached_property
    def supports_window_framing(self) -> Optional[bool]:
        """Field supports_window_framing"""
        return self._proto.supports_window_framing

    @cached_property
    def arguments_are_coercible(self) -> Optional[bool]:
        """Field arguments_are_coercible"""
        return self._proto.arguments_are_coercible

    @cached_property
    def is_deprecated(self) -> Optional[bool]:
        """Field is_deprecated"""
        return self._proto.is_deprecated

    @cached_property
    def alias_name(self) -> Optional[str]:
        """Field alias_name"""
        return self._proto.alias_name

    @cached_property
    def sql_name(self) -> Optional[str]:
        """Field sql_name"""
        return self._proto.sql_name

    @cached_property
    def allow_external_usage(self) -> Optional[bool]:
        """Field allow_external_usage"""
        return self._proto.allow_external_usage

    @cached_property
    def volatility(self) -> Optional[int]:
        """Field volatility"""
        return self._proto.volatility

    @cached_property
    def supports_order_by(self) -> Optional[bool]:
        """Field supports_order_by"""
        return self._proto.supports_order_by

    @cached_property
    def required_language_feature(self) -> List[int]:
        """Field required_language_feature"""
        return self._proto.required_language_feature

    @cached_property
    def supports_limit(self) -> Optional[bool]:
        """Field supports_limit"""
        return self._proto.supports_limit

    @cached_property
    def supports_null_handling_modifier(self) -> Optional[bool]:
        """Field supports_null_handling_modifier"""
        return self._proto.supports_null_handling_modifier

    @cached_property
    def supports_safe_error_mode(self) -> Optional[bool]:
        """Field supports_safe_error_mode"""
        return self._proto.supports_safe_error_mode

    @cached_property
    def supports_having_modifier(self) -> Optional[bool]:
        """Field supports_having_modifier"""
        return self._proto.supports_having_modifier

    @cached_property
    def supports_clamped_between_modifier(self) -> Optional[bool]:
        """Field supports_clamped_between_modifier"""
        return self._proto.supports_clamped_between_modifier

    @cached_property
    def uses_upper_case_sql_name(self) -> Optional[bool]:
        """Field uses_upper_case_sql_name"""
        return self._proto.uses_upper_case_sql_name

    @cached_property
    def may_suppress_side_effects(self) -> Optional[bool]:
        """Field may_suppress_side_effects"""
        return self._proto.may_suppress_side_effects

    @cached_property
    def module_name_from_import(self) -> List[str]:
        """Field module_name_from_import"""
        return self._proto.module_name_from_import



class Function:
    """Generated wrapper for FunctionProto"""

    def __init__(self, proto: 'FunctionProto'):
        self._proto = proto

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def group(self) -> Optional[str]:
        """Field group"""
        return self._proto.group

    @cached_property
    def mode(self) -> Optional[int]:
        """Field mode"""
        return self._proto.mode

    @cached_property
    def signature(self) -> List['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def options(self) -> Optional['FunctionOptionsProto']:
        """Field options"""
        return self._proto.options

    @cached_property
    def parse_resume_location(self) -> Optional['ParseResumeLocationProto']:
        """Field parse_resume_location"""
        return self._proto.parse_resume_location

    @cached_property
    def templated_sql_function_argument_name(self) -> List[str]:
        """Field templated_sql_function_argument_name"""
        return self._proto.templated_sql_function_argument_name

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security

    @cached_property
    def statement_context(self) -> Optional[int]:
        """Field statement_context"""
        return self._proto.statement_context



class FunctionRef:
    """Generated wrapper for FunctionRefProto"""

    def __init__(self, proto: 'FunctionRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class FunctionSignatureOptions:
    """Generated wrapper for FunctionSignatureOptionsProto"""

    def __init__(self, proto: 'FunctionSignatureOptionsProto'):
        self._proto = proto

    @cached_property
    def is_deprecated(self) -> Optional[bool]:
        """Field is_deprecated"""
        return self._proto.is_deprecated

    @cached_property
    def additional_deprecation_warning(self) -> List['FreestandingDeprecationWarning']:
        """Field additional_deprecation_warning"""
        return self._proto.additional_deprecation_warning

    @cached_property
    def required_language_feature(self) -> List[int]:
        """Field required_language_feature"""
        return self._proto.required_language_feature

    @cached_property
    def is_aliased_signature(self) -> Optional[bool]:
        """Field is_aliased_signature"""
        return self._proto.is_aliased_signature

    @cached_property
    def propagates_collation(self) -> Optional[bool]:
        """Field propagates_collation"""
        return self._proto.propagates_collation

    @cached_property
    def uses_operation_collation(self) -> Optional[bool]:
        """Field uses_operation_collation"""
        return self._proto.uses_operation_collation

    @cached_property
    def rejects_collation(self) -> Optional[bool]:
        """Field rejects_collation"""
        return self._proto.rejects_collation

    @cached_property
    def rewrite_options(self) -> Optional['FunctionSignatureRewriteOptionsProto']:
        """Field rewrite_options"""
        return self._proto.rewrite_options



class FunctionSignature:
    """Generated wrapper for FunctionSignatureProto"""

    def __init__(self, proto: 'FunctionSignatureProto'):
        self._proto = proto

    @cached_property
    def argument(self) -> List['FunctionArgumentTypeProto']:
        """Field argument"""
        return self._proto.argument

    @cached_property
    def return_type(self) -> Optional['FunctionArgumentTypeProto']:
        """Field return_type"""
        return self._proto.return_type

    @cached_property
    def context_id(self) -> Optional[int]:
        """Field context_id"""
        return self._proto.context_id

    @cached_property
    def options(self) -> Optional['FunctionSignatureOptionsProto']:
        """Field options"""
        return self._proto.options



class FunctionSignatureRewriteOptions:
    """Generated wrapper for FunctionSignatureRewriteOptionsProto"""

    def __init__(self, proto: 'FunctionSignatureRewriteOptionsProto'):
        self._proto = proto

    @cached_property
    def enabled(self) -> Optional[bool]:
        """Field enabled"""
        return self._proto.enabled

    @cached_property
    def rewriter(self) -> Optional[int]:
        """Field rewriter"""
        return self._proto.rewriter

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.sql

    @cached_property
    def allow_table_references(self) -> Optional[bool]:
        """Field allow_table_references"""
        return self._proto.allow_table_references

    @cached_property
    def allowed_function_groups(self) -> List[str]:
        """Field allowed_function_groups"""
        return self._proto.allowed_function_groups



class GraphElementLabel:
    """Generated wrapper for GraphElementLabelProto"""

    def __init__(self, proto: 'GraphElementLabelProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def property_declaration_names(self) -> List[str]:
        """Field property_declaration_names"""
        return self._proto.property_declaration_names



class GraphElementLabelRef:
    """Generated wrapper for GraphElementLabelRefProto"""

    def __init__(self, proto: 'GraphElementLabelRefProto'):
        self._proto = proto

    @cached_property
    def property_graph(self) -> Optional['PropertyGraphRefProto']:
        """Field property_graph"""
        return self._proto.property_graph

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class GraphElementTable:
    """Generated wrapper for GraphElementTableProto"""

    def __init__(self, proto: 'GraphElementTableProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind

    @cached_property
    def base_catalog_name(self) -> Optional[str]:
        """Field base_catalog_name"""
        return self._proto.base_catalog_name

    @cached_property
    def base_schema_name(self) -> Optional[str]:
        """Field base_schema_name"""
        return self._proto.base_schema_name

    @cached_property
    def base_table_name(self) -> Optional[str]:
        """Field base_table_name"""
        return self._proto.base_table_name

    @cached_property
    def key_columns(self) -> List[str]:
        """Field key_columns"""
        return self._proto.key_columns

    @cached_property
    def label_names(self) -> List[str]:
        """Field label_names"""
        return self._proto.label_names

    @cached_property
    def property_definitions(self) -> List['GraphPropertyDefinitionProto']:
        """Field property_definitions"""
        return self._proto.property_definitions

    @cached_property
    def dynamic_label_expr(self) -> Optional[str]:
        """Field dynamic_label_expr"""
        return self._proto.dynamic_label_expr

    @cached_property
    def dynamic_property_expr(self) -> Optional[str]:
        """Field dynamic_property_expr"""
        return self._proto.dynamic_property_expr

    @cached_property
    def source_node_table(self) -> Optional['GraphNodeTableReferenceProto']:
        """Field source_node_table"""
        return self._proto.source_node_table

    @cached_property
    def destination_node_table(self) -> Optional['GraphNodeTableReferenceProto']:
        """Field destination_node_table"""
        return self._proto.destination_node_table



class GraphElementTableRef:
    """Generated wrapper for GraphElementTableRefProto"""

    def __init__(self, proto: 'GraphElementTableRefProto'):
        self._proto = proto

    @cached_property
    def property_graph(self) -> Optional['PropertyGraphRefProto']:
        """Field property_graph"""
        return self._proto.property_graph

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class GraphElementType:
    """Generated wrapper for GraphElementTypeProto"""

    def __init__(self, proto: 'GraphElementTypeProto'):
        self._proto = proto

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind

    @cached_property
    def property_type(self) -> List['PropertyTypeProto']:
        """Field property_type"""
        return self._proto.property_type

    @cached_property
    def graph_reference(self) -> List[str]:
        """Field graph_reference"""
        return self._proto.graph_reference

    @cached_property
    def is_dynamic(self) -> Optional[bool]:
        """Field is_dynamic"""
        return self._proto.is_dynamic



class GraphNodeTableReference:
    """Generated wrapper for GraphNodeTableReferenceProto"""

    def __init__(self, proto: 'GraphNodeTableReferenceProto'):
        self._proto = proto

    @cached_property
    def node_table_name(self) -> Optional[str]:
        """Field node_table_name"""
        return self._proto.node_table_name

    @cached_property
    def edge_table_columns(self) -> List[str]:
        """Field edge_table_columns"""
        return self._proto.edge_table_columns

    @cached_property
    def node_table_columns(self) -> List[str]:
        """Field node_table_columns"""
        return self._proto.node_table_columns



class GraphPathType:
    """Generated wrapper for GraphPathTypeProto"""

    def __init__(self, proto: 'GraphPathTypeProto'):
        self._proto = proto

    @cached_property
    def node_type(self) -> Optional['GraphElementTypeProto']:
        """Field node_type"""
        return self._proto.node_type

    @cached_property
    def edge_type(self) -> Optional['GraphElementTypeProto']:
        """Field edge_type"""
        return self._proto.edge_type



class GraphPropertyDeclaration:
    """Generated wrapper for GraphPropertyDeclarationProto"""

    def __init__(self, proto: 'GraphPropertyDeclarationProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional[str]:
        """Field type"""
        return self._proto.type



class GraphPropertyDeclarationRef:
    """Generated wrapper for GraphPropertyDeclarationRefProto"""

    def __init__(self, proto: 'GraphPropertyDeclarationRefProto'):
        self._proto = proto

    @cached_property
    def property_graph(self) -> Optional['PropertyGraphRefProto']:
        """Field property_graph"""
        return self._proto.property_graph

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class GraphPropertyDefinition:
    """Generated wrapper for GraphPropertyDefinitionProto"""

    def __init__(self, proto: 'GraphPropertyDefinitionProto'):
        self._proto = proto

    @cached_property
    def property_declaration_name(self) -> Optional[str]:
        """Field property_declaration_name"""
        return self._proto.property_declaration_name

    @cached_property
    def value_expression_sql(self) -> Optional[str]:
        """Field value_expression_sql"""
        return self._proto.value_expression_sql



class LanguageOptions:
    """Generated wrapper for LanguageOptionsProto"""

    def __init__(self, proto: 'LanguageOptionsProto'):
        self._proto = proto

    @cached_property
    def name_resolution_mode(self) -> Optional[int]:
        """Field name_resolution_mode"""
        return self._proto.name_resolution_mode

    @cached_property
    def product_mode(self) -> Optional[int]:
        """Field product_mode"""
        return self._proto.product_mode

    @cached_property
    def error_on_deprecated_syntax(self) -> Optional[bool]:
        """Field error_on_deprecated_syntax"""
        return self._proto.error_on_deprecated_syntax

    @cached_property
    def enabled_language_features(self) -> List[int]:
        """Field enabled_language_features"""
        return self._proto.enabled_language_features

    @cached_property
    def supported_statement_kinds(self) -> List[int]:
        """Field supported_statement_kinds"""
        return self._proto.supported_statement_kinds

    @cached_property
    def supported_generic_entity_types(self) -> List[str]:
        """Field supported_generic_entity_types"""
        return self._proto.supported_generic_entity_types

    @cached_property
    def reserved_keywords(self) -> List[str]:
        """Field reserved_keywords"""
        return self._proto.reserved_keywords

    @cached_property
    def supported_generic_sub_entity_types(self) -> List[str]:
        """Field supported_generic_sub_entity_types"""
        return self._proto.supported_generic_sub_entity_types



class MapType:
    """Generated wrapper for MapTypeProto"""

    def __init__(self, proto: 'MapTypeProto'):
        self._proto = proto

    @cached_property
    def key_type(self) -> Optional['TypeProto']:
        """Field key_type"""
        return self._proto.key_type

    @cached_property
    def value_type(self) -> Optional['TypeProto']:
        """Field value_type"""
        return self._proto.value_type



class MatchPartitionResult:
    """Generated wrapper for MatchPartitionResultProto"""

    def __init__(self, proto: 'MatchPartitionResultProto'):
        self._proto = proto

    @cached_property
    def add_row(self) -> List['MatchResultProto']:
        """Field add_row"""
        return self._proto.add_row

    @cached_property
    def finalize(self) -> Optional['MatchResultProto']:
        """Field finalize"""
        return self._proto.finalize



class MatchResult:
    """Generated wrapper for MatchResultProto"""

    def __init__(self, proto: 'MatchResultProto'):
        self._proto = proto

    @cached_property
    def match(self) -> List[str]:
        """Field match"""
        return self._proto.match

    @cached_property
    def rep_count(self) -> Optional[int]:
        """Field rep_count"""
        return self._proto.rep_count



class MeasureType:
    """Generated wrapper for MeasureTypeProto"""

    def __init__(self, proto: 'MeasureTypeProto'):
        self._proto = proto

    @cached_property
    def result_type(self) -> Optional['TypeProto']:
        """Field result_type"""
        return self._proto.result_type



class ModelRef:
    """Generated wrapper for ModelRefProto"""

    def __init__(self, proto: 'ModelRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def serialization_id(self) -> Optional[int]:
        """Field serialization_id"""
        return self._proto.serialization_id

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class NumericTypeParameters:
    """Generated wrapper for NumericTypeParametersProto"""

    def __init__(self, proto: 'NumericTypeParametersProto'):
        self._proto = proto

    @cached_property
    def precision(self) -> Optional[int]:
        """Field precision"""
        return self._proto.precision

    @cached_property
    def is_max_precision(self) -> Optional[bool]:
        """Field is_max_precision"""
        return self._proto.is_max_precision

    @cached_property
    def scale(self) -> Optional[int]:
        """Field scale"""
        return self._proto.scale



class OneofDescriptorRef:
    """Generated wrapper for OneofDescriptorRefProto"""

    def __init__(self, proto: 'OneofDescriptorRefProto'):
        self._proto = proto

    @cached_property
    def containing_proto(self) -> Optional['ProtoTypeProto']:
        """Field containing_proto"""
        return self._proto.containing_proto

    @cached_property
    def index(self) -> Optional[int]:
        """Field index"""
        return self._proto.index



class ParseLocationRange:
    """Generated wrapper for ParseLocationRangeProto"""

    def __init__(self, proto: 'ParseLocationRangeProto'):
        self._proto = proto

    @cached_property
    def filename(self) -> Optional[str]:
        """Field filename"""
        return self._proto.filename

    @cached_property
    def start(self) -> Optional[int]:
        """Field start"""
        return self._proto.start

    @cached_property
    def end(self) -> Optional[int]:
        """Field end"""
        return self._proto.end



class ParseResumeLocation:
    """Generated wrapper for ParseResumeLocationProto"""

    def __init__(self, proto: 'ParseResumeLocationProto'):
        self._proto = proto

    @cached_property
    def filename(self) -> Optional[str]:
        """Field filename"""
        return self._proto.filename

    @cached_property
    def input(self) -> Optional[str]:
        """Field input"""
        return self._proto.input

    @cached_property
    def byte_position(self) -> Optional[int]:
        """Field byte_position"""
        return self._proto.byte_position

    @cached_property
    def allow_resume(self) -> Optional[bool]:
        """Field allow_resume"""
        return self._proto.allow_resume



class PlaceholderDescriptor:
    """Generated wrapper for PlaceholderDescriptorProto"""

    def __init__(self, proto: 'PlaceholderDescriptorProto'):
        self._proto = proto

    @cached_property
    def is_placeholder(self) -> Optional[bool]:
        """Field is_placeholder"""
        return self._proto.is_placeholder



class Procedure:
    """Generated wrapper for ProcedureProto"""

    def __init__(self, proto: 'ProcedureProto'):
        self._proto = proto

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature



class ProcedureRef:
    """Generated wrapper for ProcedureRefProto"""

    def __init__(self, proto: 'ProcedureRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class PropertyGraph:
    """Generated wrapper for PropertyGraphProto"""

    def __init__(self, proto: 'PropertyGraphProto'):
        self._proto = proto

    @cached_property
    def catalog(self) -> Optional[str]:
        """Field catalog"""
        return self._proto.catalog

    @cached_property
    def schema(self) -> Optional[str]:
        """Field schema"""
        return self._proto.schema

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def node_tables(self) -> List['GraphElementTableProto']:
        """Field node_tables"""
        return self._proto.node_tables

    @cached_property
    def edge_tables(self) -> List['GraphElementTableProto']:
        """Field edge_tables"""
        return self._proto.edge_tables

    @cached_property
    def labels(self) -> List['GraphElementLabelProto']:
        """Field labels"""
        return self._proto.labels

    @cached_property
    def property_declarations(self) -> List['GraphPropertyDeclarationProto']:
        """Field property_declarations"""
        return self._proto.property_declarations



class PropertyGraphRef:
    """Generated wrapper for PropertyGraphRefProto"""

    def __init__(self, proto: 'PropertyGraphRefProto'):
        self._proto = proto

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class Type:
    """Generated wrapper for ProtoTypeProto"""

    def __init__(self, proto: 'ProtoTypeProto'):
        self._proto = proto

    @cached_property
    def proto_name(self) -> Optional[str]:
        """Field proto_name"""
        return self._proto.proto_name

    @cached_property
    def proto_file_name(self) -> Optional[str]:
        """Field proto_file_name"""
        return self._proto.proto_file_name

    @cached_property
    def file_descriptor_set_index(self) -> Optional[int]:
        """Field file_descriptor_set_index"""
        return self._proto.file_descriptor_set_index

    @cached_property
    def catalog_name_path(self) -> List[str]:
        """Field catalog_name_path"""
        return self._proto.catalog_name_path



class RangeType:
    """Generated wrapper for RangeTypeProto"""

    def __init__(self, proto: 'RangeTypeProto'):
        self._proto = proto

    @cached_property
    def element_type(self) -> Optional['TypeProto']:
        """Field element_type"""
        return self._proto.element_type



class ResolvedCollation:
    """Generated wrapper for ResolvedCollationProto"""

    def __init__(self, proto: 'ResolvedCollationProto'):
        self._proto = proto

    @cached_property
    def collation_name(self) -> Optional[str]:
        """Field collation_name"""
        return self._proto.collation_name

    @cached_property
    def child_list(self) -> List['ResolvedCollationProto']:
        """Field child_list"""
        return self._proto.child_list



class ResolvedColumn:
    """Generated wrapper for ResolvedColumnProto"""

    def __init__(self, proto: 'ResolvedColumnProto'):
        self._proto = proto

    @cached_property
    def column_id(self) -> Optional[int]:
        """Field column_id"""
        return self._proto.column_id

    @cached_property
    def table_name(self) -> Optional[str]:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field annotation_map"""
        return self._proto.annotation_map



class ResolvedFunctionCallInfo:
    """Generated wrapper for ResolvedFunctionCallInfoProto"""

    def __init__(self, proto: 'ResolvedFunctionCallInfoProto'):
        self._proto = proto


class ResolvedNode:
    """Generated wrapper for ResolvedNodeProto"""

    def __init__(self, proto: 'ResolvedNodeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parse_location_range



class ScriptExecutorState:
    """Generated wrapper for ScriptExecutorStateProto"""

    def __init__(self, proto: 'ScriptExecutorStateProto'):
        self._proto = proto

    @cached_property
    def callstack(self) -> List['StackFrame']:
        """Field callstack"""
        return self._proto.callstack

    @cached_property
    def pending_exceptions(self) -> List['ScriptException']:
        """Field pending_exceptions"""
        return self._proto.pending_exceptions

    @cached_property
    def triggered_features(self) -> List[int]:
        """Field triggered_features"""
        return self._proto.triggered_features

    @cached_property
    def timezone(self) -> Optional[str]:
        """Field timezone"""
        return self._proto.timezone

    @cached_property
    def case_stmt_true_branch_index(self) -> Optional[int]:
        """Field case_stmt_true_branch_index"""
        return self._proto.case_stmt_true_branch_index

    @cached_property
    def case_stmt_current_branch_index(self) -> Optional[int]:
        """Field case_stmt_current_branch_index"""
        return self._proto.case_stmt_current_branch_index

    @cached_property
    def sql_feature_usage(self) -> Optional['ScriptFeatureUsage']:
        """Field sql_feature_usage"""
        return self._proto.sql_feature_usage



class SequenceRef:
    """Generated wrapper for SequenceRefProto"""

    def __init__(self, proto: 'SequenceRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class SimpleAnonymizationInfo:
    """Generated wrapper for SimpleAnonymizationInfoProto"""

    def __init__(self, proto: 'SimpleAnonymizationInfoProto'):
        self._proto = proto

    @cached_property
    def userid_column_name(self) -> List[str]:
        """Field userid_column_name"""
        return self._proto.userid_column_name



class SimpleCatalog:
    """Generated wrapper for SimpleCatalogProto"""

    def __init__(self, proto: 'SimpleCatalogProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def table(self) -> List['SimpleTableProto']:
        """Field table"""
        return self._proto.table

    @cached_property
    def named_type(self) -> List['NamedTypeProto']:
        """Field named_type"""
        return self._proto.named_type

    @cached_property
    def catalog(self) -> List['SimpleCatalogProto']:
        """Field catalog"""
        return self._proto.catalog

    @cached_property
    def builtin_function_options(self) -> Optional['ZetaSQLBuiltinFunctionOptionsProto']:
        """Field builtin_function_options"""
        return self._proto.builtin_function_options

    @cached_property
    def custom_function(self) -> List['FunctionProto']:
        """Field custom_function"""
        return self._proto.custom_function

    @cached_property
    def custom_tvf(self) -> List['TableValuedFunctionProto']:
        """Field custom_tvf"""
        return self._proto.custom_tvf

    @cached_property
    def file_descriptor_set_index(self) -> Optional[int]:
        """Field file_descriptor_set_index"""
        return self._proto.file_descriptor_set_index

    @cached_property
    def procedure(self) -> List['ProcedureProto']:
        """Field procedure"""
        return self._proto.procedure

    @cached_property
    def constant(self) -> List['SimpleConstantProto']:
        """Field constant"""
        return self._proto.constant

    @cached_property
    def property_graph(self) -> List['SimplePropertyGraphProto']:
        """Field property_graph"""
        return self._proto.property_graph

    @cached_property
    def connection(self) -> List['SimpleConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def model(self) -> List['SimpleModelProto']:
        """Field model"""
        return self._proto.model

    @cached_property
    def sequence(self) -> List['SimpleSequenceProto']:
        """Field sequence"""
        return self._proto.sequence



class SimpleColumn:
    """Generated wrapper for SimpleColumnProto"""

    def __init__(self, proto: 'SimpleColumnProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def is_pseudo_column(self) -> Optional[bool]:
        """Field is_pseudo_column"""
        return self._proto.is_pseudo_column

    @cached_property
    def is_writable_column(self) -> Optional[bool]:
        """Field is_writable_column"""
        return self._proto.is_writable_column

    @cached_property
    def can_update_unwritable_to_default(self) -> Optional[bool]:
        """Field can_update_unwritable_to_default"""
        return self._proto.can_update_unwritable_to_default

    @cached_property
    def annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field annotation_map"""
        return self._proto.annotation_map

    @cached_property
    def has_default_value(self) -> Optional[bool]:
        """Field has_default_value"""
        return self._proto.has_default_value

    @cached_property
    def column_expression(self) -> Optional['ExpressionAttributeProto']:
        """Field column_expression"""
        return self._proto.column_expression



class SimpleConnection:
    """Generated wrapper for SimpleConnectionProto"""

    def __init__(self, proto: 'SimpleConnectionProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class SimpleConstant:
    """Generated wrapper for SimpleConstantProto"""

    def __init__(self, proto: 'SimpleConstantProto'):
        self._proto = proto

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def value(self) -> Optional['ValueProto']:
        """Field value"""
        return self._proto.value



class SimpleGraphElementDynamicLabel:
    """Generated wrapper for SimpleGraphElementDynamicLabelProto"""

    def __init__(self, proto: 'SimpleGraphElementDynamicLabelProto'):
        self._proto = proto

    @cached_property
    def label_expression(self) -> Optional[str]:
        """Field label_expression"""
        return self._proto.label_expression



class SimpleGraphElementDynamicProperties:
    """Generated wrapper for SimpleGraphElementDynamicPropertiesProto"""

    def __init__(self, proto: 'SimpleGraphElementDynamicPropertiesProto'):
        self._proto = proto

    @cached_property
    def properties_expression(self) -> Optional[str]:
        """Field properties_expression"""
        return self._proto.properties_expression



class SimpleGraphElementLabel:
    """Generated wrapper for SimpleGraphElementLabelProto"""

    def __init__(self, proto: 'SimpleGraphElementLabelProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def property_graph_name_path(self) -> List[str]:
        """Field property_graph_name_path"""
        return self._proto.property_graph_name_path

    @cached_property
    def property_declaration_names(self) -> List[str]:
        """Field property_declaration_names"""
        return self._proto.property_declaration_names



class SimpleGraphElementTable:
    """Generated wrapper for SimpleGraphElementTableProto"""

    def __init__(self, proto: 'SimpleGraphElementTableProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def property_graph_name_path(self) -> List[str]:
        """Field property_graph_name_path"""
        return self._proto.property_graph_name_path

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind

    @cached_property
    def input_table_name(self) -> Optional[str]:
        """Field input_table_name"""
        return self._proto.input_table_name

    @cached_property
    def key_columns(self) -> List[int]:
        """Field key_columns"""
        return self._proto.key_columns

    @cached_property
    def label_names(self) -> List[str]:
        """Field label_names"""
        return self._proto.label_names

    @cached_property
    def property_definitions(self) -> List['SimpleGraphPropertyDefinitionProto']:
        """Field property_definitions"""
        return self._proto.property_definitions

    @cached_property
    def source_node_table(self) -> Optional['SimpleGraphNodeTableReferenceProto']:
        """Field source_node_table"""
        return self._proto.source_node_table

    @cached_property
    def dest_node_table(self) -> Optional['SimpleGraphNodeTableReferenceProto']:
        """Field dest_node_table"""
        return self._proto.dest_node_table

    @cached_property
    def dynamic_properties(self) -> Optional['SimpleGraphElementDynamicPropertiesProto']:
        """Field dynamic_properties"""
        return self._proto.dynamic_properties

    @cached_property
    def dynamic_label(self) -> Optional['SimpleGraphElementDynamicLabelProto']:
        """Field dynamic_label"""
        return self._proto.dynamic_label



class SimpleGraphNodeTableReference:
    """Generated wrapper for SimpleGraphNodeTableReferenceProto"""

    def __init__(self, proto: 'SimpleGraphNodeTableReferenceProto'):
        self._proto = proto

    @cached_property
    def node_table_name(self) -> Optional[str]:
        """Field node_table_name"""
        return self._proto.node_table_name

    @cached_property
    def edge_table_columns(self) -> List[int]:
        """Field edge_table_columns"""
        return self._proto.edge_table_columns

    @cached_property
    def node_table_columns(self) -> List[int]:
        """Field node_table_columns"""
        return self._proto.node_table_columns



class SimpleGraphPropertyDeclaration:
    """Generated wrapper for SimpleGraphPropertyDeclarationProto"""

    def __init__(self, proto: 'SimpleGraphPropertyDeclarationProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def property_graph_name_path(self) -> List[str]:
        """Field property_graph_name_path"""
        return self._proto.property_graph_name_path

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type



class SimpleGraphPropertyDefinition:
    """Generated wrapper for SimpleGraphPropertyDefinitionProto"""

    def __init__(self, proto: 'SimpleGraphPropertyDefinitionProto'):
        self._proto = proto

    @cached_property
    def property_declaration_name(self) -> Optional[str]:
        """Field property_declaration_name"""
        return self._proto.property_declaration_name

    @cached_property
    def value_expression_sql(self) -> Optional[str]:
        """Field value_expression_sql"""
        return self._proto.value_expression_sql



class SimpleModel:
    """Generated wrapper for SimpleModelProto"""

    def __init__(self, proto: 'SimpleModelProto'):
        self._proto = proto

    @cached_property
    def id(self) -> Optional[int]:
        """Field id"""
        return self._proto.id

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def input(self) -> List['SimpleColumnProto']:
        """Field input"""
        return self._proto.input

    @cached_property
    def output(self) -> List['SimpleColumnProto']:
        """Field output"""
        return self._proto.output



class SimplePropertyGraph:
    """Generated wrapper for SimplePropertyGraphProto"""

    def __init__(self, proto: 'SimplePropertyGraphProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def node_tables(self) -> List['SimpleGraphElementTableProto']:
        """Field node_tables"""
        return self._proto.node_tables

    @cached_property
    def edge_tables(self) -> List['SimpleGraphElementTableProto']:
        """Field edge_tables"""
        return self._proto.edge_tables

    @cached_property
    def labels(self) -> List['SimpleGraphElementLabelProto']:
        """Field labels"""
        return self._proto.labels

    @cached_property
    def property_declarations(self) -> List['SimpleGraphPropertyDeclarationProto']:
        """Field property_declarations"""
        return self._proto.property_declarations



class SimpleSequence:
    """Generated wrapper for SimpleSequenceProto"""

    def __init__(self, proto: 'SimpleSequenceProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class SimpleTable:
    """Generated wrapper for SimpleTableProto"""

    def __init__(self, proto: 'SimpleTableProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def serialization_id(self) -> Optional[int]:
        """Field serialization_id"""
        return self._proto.serialization_id

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def column(self) -> List['SimpleColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def primary_key_column_index(self) -> List[int]:
        """Field primary_key_column_index"""
        return self._proto.primary_key_column_index

    @cached_property
    def row_identity_column_index(self) -> List[int]:
        """Field row_identity_column_index"""
        return self._proto.row_identity_column_index

    @cached_property
    def name_in_catalog(self) -> Optional[str]:
        """Field name_in_catalog"""
        return self._proto.name_in_catalog

    @cached_property
    def allow_anonymous_column_name(self) -> Optional[bool]:
        """Field allow_anonymous_column_name"""
        return self._proto.allow_anonymous_column_name

    @cached_property
    def allow_duplicate_column_names(self) -> Optional[bool]:
        """Field allow_duplicate_column_names"""
        return self._proto.allow_duplicate_column_names

    @cached_property
    def anonymization_info(self) -> Optional['SimpleAnonymizationInfoProto']:
        """Field anonymization_info"""
        return self._proto.anonymization_info

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class SimpleTokenList:
    """Generated wrapper for SimpleTokenListProto"""

    def __init__(self, proto: 'SimpleTokenListProto'):
        self._proto = proto

    @cached_property
    def text_token(self) -> List['TextTokenProto']:
        """Field text_token"""
        return self._proto.text_token



class SimpleValue:
    """Generated wrapper for SimpleValueProto"""

    def __init__(self, proto: 'SimpleValueProto'):
        self._proto = proto

    @cached_property
    def int64_value(self) -> Optional[int]:
        """Field int64_value"""
        return self._proto.int64_value

    @cached_property
    def string_value(self) -> Optional[str]:
        """Field string_value"""
        return self._proto.string_value

    @cached_property
    def bool_value(self) -> Optional[bool]:
        """Field bool_value"""
        return self._proto.bool_value

    @cached_property
    def double_value(self) -> Optional[float]:
        """Field double_value"""
        return self._proto.double_value

    @cached_property
    def bytes_value(self) -> Optional[bytes]:
        """Field bytes_value"""
        return self._proto.bytes_value

    @cached_property
    def __SimpleValueProto__switch_must_have_a_default(self) -> Optional[bool]:
        """Field __SimpleValueProto__switch_must_have_a_default"""
        return self._proto.__SimpleValueProto__switch_must_have_a_default



class StateMachine:
    """Generated wrapper for StateMachineProto"""

    def __init__(self, proto: 'StateMachineProto'):
        self._proto = proto

    @cached_property
    def nfa(self) -> Optional['CompiledNFAProto']:
        """Field nfa"""
        return self._proto.nfa

    @cached_property
    def after_match_skip_mode(self) -> Optional[int]:
        """Field after_match_skip_mode"""
        return self._proto.after_match_skip_mode

    @cached_property
    def longest_match_mode(self) -> Optional[bool]:
        """Field longest_match_mode"""
        return self._proto.longest_match_mode



class StringTypeParameters:
    """Generated wrapper for StringTypeParametersProto"""

    def __init__(self, proto: 'StringTypeParametersProto'):
        self._proto = proto

    @cached_property
    def max_length(self) -> Optional[int]:
        """Field max_length"""
        return self._proto.max_length

    @cached_property
    def is_max_length(self) -> Optional[bool]:
        """Field is_max_length"""
        return self._proto.is_max_length



class StructField:
    """Generated wrapper for StructFieldProto"""

    def __init__(self, proto: 'StructFieldProto'):
        self._proto = proto

    @cached_property
    def field_name(self) -> Optional[str]:
        """Field field_name"""
        return self._proto.field_name

    @cached_property
    def field_type(self) -> Optional['TypeProto']:
        """Field field_type"""
        return self._proto.field_type



class StructType:
    """Generated wrapper for StructTypeProto"""

    def __init__(self, proto: 'StructTypeProto'):
        self._proto = proto

    @cached_property
    def field(self) -> List['StructFieldProto']:
        """Field field"""
        return self._proto.field



class TVFArgument:
    """Generated wrapper for TVFArgumentProto"""

    def __init__(self, proto: 'TVFArgumentProto'):
        self._proto = proto

    @cached_property
    def scalar_argument(self) -> Optional['ValueWithTypeProto']:
        """Field scalar_argument"""
        return self._proto.scalar_argument

    @cached_property
    def relation_argument(self) -> Optional['TVFRelationProto']:
        """Field relation_argument"""
        return self._proto.relation_argument

    @cached_property
    def model_argument(self) -> Optional['TVFModelProto']:
        """Field model_argument"""
        return self._proto.model_argument

    @cached_property
    def connection_argument(self) -> Optional['TVFConnectionProto']:
        """Field connection_argument"""
        return self._proto.connection_argument

    @cached_property
    def descriptor_argument(self) -> Optional['TVFDescriptorProto']:
        """Field descriptor_argument"""
        return self._proto.descriptor_argument

    @cached_property
    def graph_argument(self) -> Optional['TVFGraphProto']:
        """Field graph_argument"""
        return self._proto.graph_argument



class TVFConnection:
    """Generated wrapper for TVFConnectionProto"""

    def __init__(self, proto: 'TVFConnectionProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class TVFDescriptor:
    """Generated wrapper for TVFDescriptorProto"""

    def __init__(self, proto: 'TVFDescriptorProto'):
        self._proto = proto

    @cached_property
    def column_name(self) -> List[str]:
        """Field column_name"""
        return self._proto.column_name



class TVFGraph:
    """Generated wrapper for TVFGraphProto"""

    def __init__(self, proto: 'TVFGraphProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class TVFModel:
    """Generated wrapper for TVFModelProto"""

    def __init__(self, proto: 'TVFModelProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class TVFRelationColumn:
    """Generated wrapper for TVFRelationColumnProto"""

    def __init__(self, proto: 'TVFRelationColumnProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def is_pseudo_column(self) -> Optional[bool]:
        """Field is_pseudo_column"""
        return self._proto.is_pseudo_column

    @cached_property
    def annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field annotation_map"""
        return self._proto.annotation_map

    @cached_property
    def name_parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field name_parse_location_range"""
        return self._proto.name_parse_location_range

    @cached_property
    def type_parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field type_parse_location_range"""
        return self._proto.type_parse_location_range



class TVFRelation:
    """Generated wrapper for TVFRelationProto"""

    def __init__(self, proto: 'TVFRelationProto'):
        self._proto = proto

    @cached_property
    def column(self) -> List['TVFRelationColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table



class TVFSignatureOptions:
    """Generated wrapper for TVFSignatureOptionsProto"""

    def __init__(self, proto: 'TVFSignatureOptionsProto'):
        self._proto = proto

    @cached_property
    def additional_deprecation_warning(self) -> List['FreestandingDeprecationWarning']:
        """Field additional_deprecation_warning"""
        return self._proto.additional_deprecation_warning



class TVFSignature:
    """Generated wrapper for TVFSignatureProto"""

    def __init__(self, proto: 'TVFSignatureProto'):
        self._proto = proto

    @cached_property
    def argument(self) -> List['TVFArgumentProto']:
        """Field argument"""
        return self._proto.argument

    @cached_property
    def options(self) -> Optional['TVFSignatureOptionsProto']:
        """Field options"""
        return self._proto.options

    @cached_property
    def output_schema(self) -> Optional['TVFRelationProto']:
        """Field output_schema"""
        return self._proto.output_schema

    @cached_property
    def output_table_schema(self) -> Optional['TableRefProto']:
        """Field output_table_schema"""
        return self._proto.output_table_schema



class TableRef:
    """Generated wrapper for TableRefProto"""

    def __init__(self, proto: 'TableRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def serialization_id(self) -> Optional[int]:
        """Field serialization_id"""
        return self._proto.serialization_id

    @cached_property
    def full_name(self) -> Optional[str]:
        """Field full_name"""
        return self._proto.full_name



class TableValuedFunctionOptions:
    """Generated wrapper for TableValuedFunctionOptionsProto"""

    def __init__(self, proto: 'TableValuedFunctionOptionsProto'):
        self._proto = proto

    @cached_property
    def uses_upper_case_sql_name(self) -> Optional[bool]:
        """Field uses_upper_case_sql_name"""
        return self._proto.uses_upper_case_sql_name

    @cached_property
    def required_language_feature(self) -> List[int]:
        """Field required_language_feature"""
        return self._proto.required_language_feature



class TableValuedFunction:
    """Generated wrapper for TableValuedFunctionProto"""

    def __init__(self, proto: 'TableValuedFunctionProto'):
        self._proto = proto

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def signatures(self) -> List['FunctionSignatureProto']:
        """Field signatures"""
        return self._proto.signatures

    @cached_property
    def options(self) -> Optional['TableValuedFunctionOptionsProto']:
        """Field options"""
        return self._proto.options

    @cached_property
    def type(self) -> Optional[int]:
        """Field type"""
        return self._proto.type

    @cached_property
    def volatility(self) -> Optional[int]:
        """Field volatility"""
        return self._proto.volatility

    @cached_property
    def parse_resume_location(self) -> Optional['ParseResumeLocationProto']:
        """Field parse_resume_location"""
        return self._proto.parse_resume_location

    @cached_property
    def argument_name(self) -> List[str]:
        """Field argument_name"""
        return self._proto.argument_name

    @cached_property
    def custom_context(self) -> Optional[str]:
        """Field custom_context"""
        return self._proto.custom_context

    @cached_property
    def anonymization_info(self) -> Optional['SimpleAnonymizationInfoProto']:
        """Field anonymization_info"""
        return self._proto.anonymization_info

    @cached_property
    def statement_context(self) -> Optional[int]:
        """Field statement_context"""
        return self._proto.statement_context

    @cached_property
    def group(self) -> Optional[str]:
        """Field group"""
        return self._proto.group



class TableValuedFunctionRef:
    """Generated wrapper for TableValuedFunctionRefProto"""

    def __init__(self, proto: 'TableValuedFunctionRefProto'):
        self._proto = proto

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class TextToken:
    """Generated wrapper for TextTokenProto"""

    def __init__(self, proto: 'TextTokenProto'):
        self._proto = proto

    @cached_property
    def text(self) -> Optional[str]:
        """Field text"""
        return self._proto.text

    @cached_property
    def attribute(self) -> Optional[int]:
        """Field attribute"""
        return self._proto.attribute

    @cached_property
    def index_token(self) -> List['TokenProto']:
        """Field index_token"""
        return self._proto.index_token



class TimestampTypeParameters:
    """Generated wrapper for TimestampTypeParametersProto"""

    def __init__(self, proto: 'TimestampTypeParametersProto'):
        self._proto = proto

    @cached_property
    def precision(self) -> Optional[int]:
        """Field precision"""
        return self._proto.precision



class Token:
    """Generated wrapper for TokenProto"""

    def __init__(self, proto: 'TokenProto'):
        self._proto = proto

    @cached_property
    def text(self) -> Optional[str]:
        """Field text"""
        return self._proto.text

    @cached_property
    def attribute(self) -> Optional[int]:
        """Field attribute"""
        return self._proto.attribute



class TypeModifiers:
    """Generated wrapper for TypeModifiersProto"""

    def __init__(self, proto: 'TypeModifiersProto'):
        self._proto = proto

    @cached_property
    def type_parameters(self) -> Optional['TypeParametersProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collation(self) -> Optional['CollationProto']:
        """Field collation"""
        return self._proto.collation



class TypeParameters:
    """Generated wrapper for TypeParametersProto"""

    def __init__(self, proto: 'TypeParametersProto'):
        self._proto = proto

    @cached_property
    def string_type_parameters(self) -> Optional['StringTypeParametersProto']:
        """Field string_type_parameters"""
        return self._proto.string_type_parameters

    @cached_property
    def numeric_type_parameters(self) -> Optional['NumericTypeParametersProto']:
        """Field numeric_type_parameters"""
        return self._proto.numeric_type_parameters

    @cached_property
    def extended_type_parameters(self) -> Optional['ExtendedTypeParametersProto']:
        """Field extended_type_parameters"""
        return self._proto.extended_type_parameters

    @cached_property
    def timestamp_type_parameters(self) -> Optional['TimestampTypeParametersProto']:
        """Field timestamp_type_parameters"""
        return self._proto.timestamp_type_parameters

    @cached_property
    def child_list(self) -> List['TypeParametersProto']:
        """Field child_list"""
        return self._proto.child_list



class Type:
    """Generated wrapper for TypeProto"""

    def __init__(self, proto: 'TypeProto'):
        self._proto = proto

    @cached_property
    def type_kind(self) -> Optional[int]:
        """Field type_kind"""
        return self._proto.type_kind

    @cached_property
    def array_type(self) -> Optional['ArrayTypeProto']:
        """Field array_type"""
        return self._proto.array_type

    @cached_property
    def struct_type(self) -> Optional['StructTypeProto']:
        """Field struct_type"""
        return self._proto.struct_type

    @cached_property
    def proto_type(self) -> Optional['ProtoTypeProto']:
        """Field proto_type"""
        return self._proto.proto_type

    @cached_property
    def enum_type(self) -> Optional['EnumTypeProto']:
        """Field enum_type"""
        return self._proto.enum_type

    @cached_property
    def range_type(self) -> Optional['RangeTypeProto']:
        """Field range_type"""
        return self._proto.range_type

    @cached_property
    def graph_element_type(self) -> Optional['GraphElementTypeProto']:
        """Field graph_element_type"""
        return self._proto.graph_element_type

    @cached_property
    def graph_path_type(self) -> Optional['GraphPathTypeProto']:
        """Field graph_path_type"""
        return self._proto.graph_path_type

    @cached_property
    def map_type(self) -> Optional['MapTypeProto']:
        """Field map_type"""
        return self._proto.map_type

    @cached_property
    def measure_type(self) -> Optional['MeasureTypeProto']:
        """Field measure_type"""
        return self._proto.measure_type

    @cached_property
    def file_descriptor_set(self) -> List['FileDescriptorSet']:
        """Field file_descriptor_set"""
        return self._proto.file_descriptor_set

    @cached_property
    def extended_type_name(self) -> Optional[str]:
        """Field extended_type_name"""
        return self._proto.extended_type_name



class Value:
    """Generated wrapper for ValueProto"""

    def __init__(self, proto: 'ValueProto'):
        self._proto = proto

    @cached_property
    def int32_value(self) -> Optional[int]:
        """Field int32_value"""
        return self._proto.int32_value

    @cached_property
    def int64_value(self) -> Optional[int]:
        """Field int64_value"""
        return self._proto.int64_value

    @cached_property
    def uint32_value(self) -> Optional[int]:
        """Field uint32_value"""
        return self._proto.uint32_value

    @cached_property
    def uint64_value(self) -> Optional[int]:
        """Field uint64_value"""
        return self._proto.uint64_value

    @cached_property
    def bool_value(self) -> Optional[bool]:
        """Field bool_value"""
        return self._proto.bool_value

    @cached_property
    def float_value(self) -> Optional[float]:
        """Field float_value"""
        return self._proto.float_value

    @cached_property
    def double_value(self) -> Optional[float]:
        """Field double_value"""
        return self._proto.double_value

    @cached_property
    def string_value(self) -> Optional[str]:
        """Field string_value"""
        return self._proto.string_value

    @cached_property
    def bytes_value(self) -> Optional[bytes]:
        """Field bytes_value"""
        return self._proto.bytes_value

    @cached_property
    def date_value(self) -> Optional[int]:
        """Field date_value"""
        return self._proto.date_value

    @cached_property
    def enum_value(self) -> Optional[int]:
        """Field enum_value"""
        return self._proto.enum_value

    @cached_property
    def array_value(self) -> Optional['Array']:
        """Field array_value"""
        return self._proto.array_value

    @cached_property
    def struct_value(self) -> Optional['Struct']:
        """Field struct_value"""
        return self._proto.struct_value

    @cached_property
    def proto_value(self) -> Optional[bytes]:
        """Field proto_value"""
        return self._proto.proto_value

    @cached_property
    def timestamp_value(self) -> Optional['Timestamp']:
        """Field timestamp_value"""
        return self._proto.timestamp_value

    @cached_property
    def timestamp_pico_value(self) -> Optional[bytes]:
        """Field timestamp_pico_value"""
        return self._proto.timestamp_pico_value

    @cached_property
    def timestamp_picos_value(self) -> Optional['TimestampPicos']:
        """Field timestamp_picos_value"""
        return self._proto.timestamp_picos_value

    @cached_property
    def datetime_value(self) -> Optional['Datetime']:
        """Field datetime_value"""
        return self._proto.datetime_value

    @cached_property
    def time_value(self) -> Optional[int]:
        """Field time_value"""
        return self._proto.time_value

    @cached_property
    def geography_value(self) -> Optional[bytes]:
        """Field geography_value"""
        return self._proto.geography_value

    @cached_property
    def numeric_value(self) -> Optional[bytes]:
        """Field numeric_value"""
        return self._proto.numeric_value

    @cached_property
    def bignumeric_value(self) -> Optional[bytes]:
        """Field bignumeric_value"""
        return self._proto.bignumeric_value

    @cached_property
    def json_value(self) -> Optional[str]:
        """Field json_value"""
        return self._proto.json_value

    @cached_property
    def interval_value(self) -> Optional[bytes]:
        """Field interval_value"""
        return self._proto.interval_value

    @cached_property
    def tokenlist_value(self) -> Optional[bytes]:
        """Field tokenlist_value"""
        return self._proto.tokenlist_value

    @cached_property
    def range_value(self) -> Optional['Range']:
        """Field range_value"""
        return self._proto.range_value

    @cached_property
    def uuid_value(self) -> Optional[bytes]:
        """Field uuid_value"""
        return self._proto.uuid_value

    @cached_property
    def map_value(self) -> Optional['Map']:
        """Field map_value"""
        return self._proto.map_value

    @cached_property
    def __ValueProto__switch_must_have_a_default(self) -> Optional[bool]:
        """Field __ValueProto__switch_must_have_a_default"""
        return self._proto.__ValueProto__switch_must_have_a_default



class ValueWithType:
    """Generated wrapper for ValueWithTypeProto"""

    def __init__(self, proto: 'ValueWithTypeProto'):
        self._proto = proto

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def value(self) -> Optional['ValueProto']:
        """Field value"""
        return self._proto.value



class ZetaSQLBuiltinFunctionOptions:
    """Generated wrapper for ZetaSQLBuiltinFunctionOptionsProto"""

    def __init__(self, proto: 'ZetaSQLBuiltinFunctionOptionsProto'):
        self._proto = proto

    @cached_property
    def language_options(self) -> Optional['LanguageOptionsProto']:
        """Field language_options"""
        return self._proto.language_options

    @cached_property
    def include_function_ids(self) -> List[int]:
        """Field include_function_ids"""
        return self._proto.include_function_ids

    @cached_property
    def exclude_function_ids(self) -> List[int]:
        """Field exclude_function_ids"""
        return self._proto.exclude_function_ids

    @cached_property
    def enabled_rewrites_map_entry(self) -> List['EnabledRewriteProto']:
        """Field enabled_rewrites_map_entry"""
        return self._proto.enabled_rewrites_map_entry



class ASTAfterMatchSkipClause(ASTNode):
    """Generated wrapper for ASTAfterMatchSkipClauseProto"""

    def __init__(self, proto: 'ASTAfterMatchSkipClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def target_type(self) -> Optional[int]:
        """Field target_type"""
        return self._proto.target_type



class ASTAlias(ASTNode):
    """Generated wrapper for ASTAliasProto"""

    def __init__(self, proto: 'ASTAliasProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier



class ASTAliasedQueryList(ASTNode):
    """Generated wrapper for ASTAliasedQueryListProto"""

    def __init__(self, proto: 'ASTAliasedQueryListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def aliased_query_list(self) -> List['ASTAliasedQueryProto']:
        """Field aliased_query_list"""
        return self._proto.aliased_query_list



class ASTAliasedQueryModifiers(ASTNode):
    """Generated wrapper for ASTAliasedQueryModifiersProto"""

    def __init__(self, proto: 'ASTAliasedQueryModifiersProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def recursion_depth_modifier(self) -> Optional['ASTRecursionDepthModifierProto']:
        """Field recursion_depth_modifier"""
        return self._proto.recursion_depth_modifier



class ASTAliasedQuery(ASTNode):
    """Generated wrapper for ASTAliasedQueryProto"""

    def __init__(self, proto: 'ASTAliasedQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional['ASTIdentifierProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def modifiers(self) -> Optional['ASTAliasedQueryModifiersProto']:
        """Field modifiers"""
        return self._proto.modifiers



class ASTAlterActionList(ASTNode):
    """Generated wrapper for ASTAlterActionListProto"""

    def __init__(self, proto: 'ASTAlterActionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def actions(self) -> List['AnyASTAlterActionProto']:
        """Field actions"""
        return self._proto.actions



class ASTAlterAction(ASTNode):
    """Generated wrapper for ASTAlterActionProto"""

    def __init__(self, proto: 'ASTAlterActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTAnySomeAllOp(ASTNode):
    """Generated wrapper for ASTAnySomeAllOpProto"""

    def __init__(self, proto: 'ASTAnySomeAllOpProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def op(self) -> Optional[int]:
        """Field op"""
        return self._proto.op



class ASTAssertRowsModified(ASTNode):
    """Generated wrapper for ASTAssertRowsModifiedProto"""

    def __init__(self, proto: 'ASTAssertRowsModifiedProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def num_rows(self) -> Optional['AnyASTExpressionProto']:
        """Field num_rows"""
        return self._proto.num_rows



class ASTAuxLoadDataFromFilesOptionsList(ASTNode):
    """Generated wrapper for ASTAuxLoadDataFromFilesOptionsListProto"""

    def __init__(self, proto: 'ASTAuxLoadDataFromFilesOptionsListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTAuxLoadDataPartitionsClause(ASTNode):
    """Generated wrapper for ASTAuxLoadDataPartitionsClauseProto"""

    def __init__(self, proto: 'ASTAuxLoadDataPartitionsClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def partition_filter(self) -> Optional['AnyASTExpressionProto']:
        """Field partition_filter"""
        return self._proto.partition_filter

    @cached_property
    def is_overwrite(self) -> Optional[bool]:
        """Field is_overwrite"""
        return self._proto.is_overwrite



class ASTBracedConstructorField(ASTNode):
    """Generated wrapper for ASTBracedConstructorFieldProto"""

    def __init__(self, proto: 'ASTBracedConstructorFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['ASTBracedConstructorFieldValueProto']:
        """Field value"""
        return self._proto.value

    @cached_property
    def comma_separated(self) -> Optional[bool]:
        """Field comma_separated"""
        return self._proto.comma_separated

    @cached_property
    def braced_constructor_lhs(self) -> Optional['ASTBracedConstructorLhsProto']:
        """Field braced_constructor_lhs"""
        return self._proto.braced_constructor_lhs



class ASTBracedConstructorFieldValue(ASTNode):
    """Generated wrapper for ASTBracedConstructorFieldValueProto"""

    def __init__(self, proto: 'ASTBracedConstructorFieldValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def colon_prefixed(self) -> Optional[bool]:
        """Field colon_prefixed"""
        return self._proto.colon_prefixed



class ASTChainedBaseExpr(ASTNode):
    """Generated wrapper for ASTChainedBaseExprProto"""

    def __init__(self, proto: 'ASTChainedBaseExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr



class ASTClampedBetweenModifier(ASTNode):
    """Generated wrapper for ASTClampedBetweenModifierProto"""

    def __init__(self, proto: 'ASTClampedBetweenModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def low(self) -> Optional['AnyASTExpressionProto']:
        """Field low"""
        return self._proto.low

    @cached_property
    def high(self) -> Optional['AnyASTExpressionProto']:
        """Field high"""
        return self._proto.high



class ASTCloneDataSourceList(ASTNode):
    """Generated wrapper for ASTCloneDataSourceListProto"""

    def __init__(self, proto: 'ASTCloneDataSourceListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def data_sources(self) -> List['ASTCloneDataSourceProto']:
        """Field data_sources"""
        return self._proto.data_sources



class ASTClusterBy(ASTNode):
    """Generated wrapper for ASTClusterByProto"""

    def __init__(self, proto: 'ASTClusterByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def clustering_expressions(self) -> List['AnyASTExpressionProto']:
        """Field clustering_expressions"""
        return self._proto.clustering_expressions



class ASTCollate(ASTNode):
    """Generated wrapper for ASTCollateProto"""

    def __init__(self, proto: 'ASTCollateProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def collation_name(self) -> Optional['AnyASTExpressionProto']:
        """Field collation_name"""
        return self._proto.collation_name



class ASTColumnAttributeList(ASTNode):
    """Generated wrapper for ASTColumnAttributeListProto"""

    def __init__(self, proto: 'ASTColumnAttributeListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def values(self) -> List['AnyASTColumnAttributeProto']:
        """Field values"""
        return self._proto.values



class ASTColumnAttribute(ASTNode):
    """Generated wrapper for ASTColumnAttributeProto"""

    def __init__(self, proto: 'ASTColumnAttributeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTColumnList(ASTNode):
    """Generated wrapper for ASTColumnListProto"""

    def __init__(self, proto: 'ASTColumnListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifiers(self) -> List['ASTIdentifierProto']:
        """Field identifiers"""
        return self._proto.identifiers



class ASTColumnPosition(ASTNode):
    """Generated wrapper for ASTColumnPositionProto"""

    def __init__(self, proto: 'ASTColumnPositionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def type(self) -> Optional[int]:
        """Field type"""
        return self._proto.type



class ASTColumnSchema(ASTNode):
    """Generated wrapper for ASTColumnSchemaProto"""

    def __init__(self, proto: 'ASTColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTColumnWithOptionsList(ASTNode):
    """Generated wrapper for ASTColumnWithOptionsListProto"""

    def __init__(self, proto: 'ASTColumnWithOptionsListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def column_with_options(self) -> List['ASTColumnWithOptionsProto']:
        """Field column_with_options"""
        return self._proto.column_with_options



class ASTColumnWithOptions(ASTNode):
    """Generated wrapper for ASTColumnWithOptionsProto"""

    def __init__(self, proto: 'ASTColumnWithOptionsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTConnectionClause(ASTNode):
    """Generated wrapper for ASTConnectionClauseProto"""

    def __init__(self, proto: 'ASTConnectionClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def connection_path(self) -> Optional['AnyASTExpressionProto']:
        """Field connection_path"""
        return self._proto.connection_path



class ASTCube(ASTNode):
    """Generated wrapper for ASTCubeProto"""

    def __init__(self, proto: 'ASTCubeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expressions(self) -> List['AnyASTExpressionProto']:
        """Field expressions"""
        return self._proto.expressions



class ASTDescriptorColumnList(ASTNode):
    """Generated wrapper for ASTDescriptorColumnListProto"""

    def __init__(self, proto: 'ASTDescriptorColumnListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def descriptor_column_list(self) -> List['ASTDescriptorColumnProto']:
        """Field descriptor_column_list"""
        return self._proto.descriptor_column_list



class ASTDescriptorColumn(ASTNode):
    """Generated wrapper for ASTDescriptorColumnProto"""

    def __init__(self, proto: 'ASTDescriptorColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTDescriptor(ASTNode):
    """Generated wrapper for ASTDescriptorProto"""

    def __init__(self, proto: 'ASTDescriptorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def columns(self) -> Optional['ASTDescriptorColumnListProto']:
        """Field columns"""
        return self._proto.columns



class ASTElseifClauseList(ASTNode):
    """Generated wrapper for ASTElseifClauseListProto"""

    def __init__(self, proto: 'ASTElseifClauseListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def elseif_clauses(self) -> List['ASTElseifClauseProto']:
        """Field elseif_clauses"""
        return self._proto.elseif_clauses



class ASTElseifClause(ASTNode):
    """Generated wrapper for ASTElseifClauseProto"""

    def __init__(self, proto: 'ASTElseifClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.body



class ASTExceptionHandlerList(ASTNode):
    """Generated wrapper for ASTExceptionHandlerListProto"""

    def __init__(self, proto: 'ASTExceptionHandlerListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def exception_handler_list(self) -> List['ASTExceptionHandlerProto']:
        """Field exception_handler_list"""
        return self._proto.exception_handler_list



class ASTExceptionHandler(ASTNode):
    """Generated wrapper for ASTExceptionHandlerProto"""

    def __init__(self, proto: 'ASTExceptionHandlerProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def statement_list(self) -> Optional['ASTStatementListProto']:
        """Field statement_list"""
        return self._proto.statement_list



class ASTExecuteIntoClause(ASTNode):
    """Generated wrapper for ASTExecuteIntoClauseProto"""

    def __init__(self, proto: 'ASTExecuteIntoClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifiers(self) -> Optional['ASTIdentifierListProto']:
        """Field identifiers"""
        return self._proto.identifiers



class ASTExecuteUsingArgument(ASTNode):
    """Generated wrapper for ASTExecuteUsingArgumentProto"""

    def __init__(self, proto: 'ASTExecuteUsingArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTExecuteUsingClause(ASTNode):
    """Generated wrapper for ASTExecuteUsingClauseProto"""

    def __init__(self, proto: 'ASTExecuteUsingClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def arguments(self) -> List['ASTExecuteUsingArgumentProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTExpression(ASTNode):
    """Generated wrapper for ASTExpressionProto"""

    def __init__(self, proto: 'ASTExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized



class ASTExpressionWithOptAlias(ASTNode):
    """Generated wrapper for ASTExpressionWithOptAliasProto"""

    def __init__(self, proto: 'ASTExpressionWithOptAliasProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def optional_alias(self) -> Optional['ASTAliasProto']:
        """Field optional_alias"""
        return self._proto.optional_alias



class ASTFilterFieldsArg(ASTNode):
    """Generated wrapper for ASTFilterFieldsArgProto"""

    def __init__(self, proto: 'ASTFilterFieldsArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def path_expression(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field path_expression"""
        return self._proto.path_expression

    @cached_property
    def filter_type(self) -> Optional[int]:
        """Field filter_type"""
        return self._proto.filter_type



class ASTForSystemTime(ASTNode):
    """Generated wrapper for ASTForSystemTimeProto"""

    def __init__(self, proto: 'ASTForSystemTimeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTForeignKeyActions(ASTNode):
    """Generated wrapper for ASTForeignKeyActionsProto"""

    def __init__(self, proto: 'ASTForeignKeyActionsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def update_action(self) -> Optional[int]:
        """Field update_action"""
        return self._proto.update_action

    @cached_property
    def delete_action(self) -> Optional[int]:
        """Field delete_action"""
        return self._proto.delete_action



class ASTForeignKeyReference(ASTNode):
    """Generated wrapper for ASTForeignKeyReferenceProto"""

    def __init__(self, proto: 'ASTForeignKeyReferenceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def column_list(self) -> Optional['ASTColumnListProto']:
        """Field column_list"""
        return self._proto.column_list

    @cached_property
    def actions(self) -> Optional['ASTForeignKeyActionsProto']:
        """Field actions"""
        return self._proto.actions

    @cached_property
    def match(self) -> Optional[int]:
        """Field match"""
        return self._proto.match

    @cached_property
    def enforced(self) -> Optional[bool]:
        """Field enforced"""
        return self._proto.enforced



class ASTFormatClause(ASTNode):
    """Generated wrapper for ASTFormatClauseProto"""

    def __init__(self, proto: 'ASTFormatClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def format(self) -> Optional['AnyASTExpressionProto']:
        """Field format"""
        return self._proto.format

    @cached_property
    def time_zone_expr(self) -> Optional['AnyASTExpressionProto']:
        """Field time_zone_expr"""
        return self._proto.time_zone_expr



class ASTFromClause(ASTNode):
    """Generated wrapper for ASTFromClauseProto"""

    def __init__(self, proto: 'ASTFromClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_expression(self) -> Optional['AnyASTTableExpressionProto']:
        """Field table_expression"""
        return self._proto.table_expression



class ASTFunctionDeclaration(ASTNode):
    """Generated wrapper for ASTFunctionDeclarationProto"""

    def __init__(self, proto: 'ASTFunctionDeclarationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def parameters(self) -> Optional['ASTFunctionParametersProto']:
        """Field parameters"""
        return self._proto.parameters



class ASTFunctionParameter(ASTNode):
    """Generated wrapper for ASTFunctionParameterProto"""

    def __init__(self, proto: 'ASTFunctionParameterProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['AnyASTTypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def templated_parameter_type(self) -> Optional['ASTTemplatedParameterTypeProto']:
        """Field templated_parameter_type"""
        return self._proto.templated_parameter_type

    @cached_property
    def tvf_schema(self) -> Optional['ASTTVFSchemaProto']:
        """Field tvf_schema"""
        return self._proto.tvf_schema

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def default_value(self) -> Optional['AnyASTExpressionProto']:
        """Field default_value"""
        return self._proto.default_value

    @cached_property
    def procedure_parameter_mode(self) -> Optional[int]:
        """Field procedure_parameter_mode"""
        return self._proto.procedure_parameter_mode

    @cached_property
    def is_not_aggregate(self) -> Optional[bool]:
        """Field is_not_aggregate"""
        return self._proto.is_not_aggregate



class ASTFunctionParameters(ASTNode):
    """Generated wrapper for ASTFunctionParametersProto"""

    def __init__(self, proto: 'ASTFunctionParametersProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parameter_entries(self) -> List['ASTFunctionParameterProto']:
        """Field parameter_entries"""
        return self._proto.parameter_entries



class ASTFunctionTypeArgList(ASTNode):
    """Generated wrapper for ASTFunctionTypeArgListProto"""

    def __init__(self, proto: 'ASTFunctionTypeArgListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def args(self) -> List['AnyASTTypeProto']:
        """Field args"""
        return self._proto.args



class ASTGeneratedColumnInfo(ASTNode):
    """Generated wrapper for ASTGeneratedColumnInfoProto"""

    def __init__(self, proto: 'ASTGeneratedColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def stored_mode(self) -> Optional[int]:
        """Field stored_mode"""
        return self._proto.stored_mode

    @cached_property
    def generated_mode(self) -> Optional[int]:
        """Field generated_mode"""
        return self._proto.generated_mode

    @cached_property
    def identity_column_info(self) -> Optional['ASTIdentityColumnInfoProto']:
        """Field identity_column_info"""
        return self._proto.identity_column_info



class ASTGqlLetVariableDefinitionList(ASTNode):
    """Generated wrapper for ASTGqlLetVariableDefinitionListProto"""

    def __init__(self, proto: 'ASTGqlLetVariableDefinitionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def variable_definitions(self) -> List['ASTGqlLetVariableDefinitionProto']:
        """Field variable_definitions"""
        return self._proto.variable_definitions



class ASTGqlLetVariableDefinition(ASTNode):
    """Generated wrapper for ASTGqlLetVariableDefinitionProto"""

    def __init__(self, proto: 'ASTGqlLetVariableDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTGqlOperator(ASTNode):
    """Generated wrapper for ASTGqlOperatorProto"""

    def __init__(self, proto: 'ASTGqlOperatorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTGqlPageLimit(ASTNode):
    """Generated wrapper for ASTGqlPageLimitProto"""

    def __init__(self, proto: 'ASTGqlPageLimitProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def limit(self) -> Optional['AnyASTExpressionProto']:
        """Field limit"""
        return self._proto.limit



class ASTGqlPageOffset(ASTNode):
    """Generated wrapper for ASTGqlPageOffsetProto"""

    def __init__(self, proto: 'ASTGqlPageOffsetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def offset(self) -> Optional['AnyASTExpressionProto']:
        """Field offset"""
        return self._proto.offset



class ASTGqlPage(ASTNode):
    """Generated wrapper for ASTGqlPageProto"""

    def __init__(self, proto: 'ASTGqlPageProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def offset(self) -> Optional['ASTGqlPageOffsetProto']:
        """Field offset"""
        return self._proto.offset

    @cached_property
    def limit(self) -> Optional['ASTGqlPageLimitProto']:
        """Field limit"""
        return self._proto.limit



class ASTGranteeList(ASTNode):
    """Generated wrapper for ASTGranteeListProto"""

    def __init__(self, proto: 'ASTGranteeListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def grantee_list(self) -> List['AnyASTExpressionProto']:
        """Field grantee_list"""
        return self._proto.grantee_list



class ASTGraphDerivedPropertyList(ASTNode):
    """Generated wrapper for ASTGraphDerivedPropertyListProto"""

    def __init__(self, proto: 'ASTGraphDerivedPropertyListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def properties(self) -> List['ASTGraphDerivedPropertyProto']:
        """Field properties"""
        return self._proto.properties



class ASTGraphDerivedProperty(ASTNode):
    """Generated wrapper for ASTGraphDerivedPropertyProto"""

    def __init__(self, proto: 'ASTGraphDerivedPropertyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTGraphDynamicLabel(ASTNode):
    """Generated wrapper for ASTGraphDynamicLabelProto"""

    def __init__(self, proto: 'ASTGraphDynamicLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['AnyASTExpressionProto']:
        """Field label"""
        return self._proto.label



class ASTGraphDynamicProperties(ASTNode):
    """Generated wrapper for ASTGraphDynamicPropertiesProto"""

    def __init__(self, proto: 'ASTGraphDynamicPropertiesProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def properties(self) -> Optional['AnyASTExpressionProto']:
        """Field properties"""
        return self._proto.properties



class ASTGraphElementLabelAndPropertiesList(ASTNode):
    """Generated wrapper for ASTGraphElementLabelAndPropertiesListProto"""

    def __init__(self, proto: 'ASTGraphElementLabelAndPropertiesListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def label_properties_list(self) -> List['ASTGraphElementLabelAndPropertiesProto']:
        """Field label_properties_list"""
        return self._proto.label_properties_list



class ASTGraphElementLabelAndProperties(ASTNode):
    """Generated wrapper for ASTGraphElementLabelAndPropertiesProto"""

    def __init__(self, proto: 'ASTGraphElementLabelAndPropertiesProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def label_name(self) -> Optional['ASTIdentifierProto']:
        """Field label_name"""
        return self._proto.label_name

    @cached_property
    def properties(self) -> Optional['ASTGraphPropertiesProto']:
        """Field properties"""
        return self._proto.properties

    @cached_property
    def label_options_list(self) -> Optional['ASTOptionsListProto']:
        """Field label_options_list"""
        return self._proto.label_options_list



class ASTGraphElementPatternFiller(ASTNode):
    """Generated wrapper for ASTGraphElementPatternFillerProto"""

    def __init__(self, proto: 'ASTGraphElementPatternFillerProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def variable_name(self) -> Optional['ASTIdentifierProto']:
        """Field variable_name"""
        return self._proto.variable_name

    @cached_property
    def label_filter(self) -> Optional['ASTGraphLabelFilterProto']:
        """Field label_filter"""
        return self._proto.label_filter

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause

    @cached_property
    def property_specification(self) -> Optional['ASTGraphPropertySpecificationProto']:
        """Field property_specification"""
        return self._proto.property_specification

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def edge_cost(self) -> Optional['AnyASTExpressionProto']:
        """Field edge_cost"""
        return self._proto.edge_cost



class ASTGraphElementTableList(ASTNode):
    """Generated wrapper for ASTGraphElementTableListProto"""

    def __init__(self, proto: 'ASTGraphElementTableListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def element_tables(self) -> List['ASTGraphElementTableProto']:
        """Field element_tables"""
        return self._proto.element_tables



class ASTGraphElementTable(ASTNode):
    """Generated wrapper for ASTGraphElementTableProto"""

    def __init__(self, proto: 'ASTGraphElementTableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def key_list(self) -> Optional['ASTColumnListProto']:
        """Field key_list"""
        return self._proto.key_list

    @cached_property
    def source_node_reference(self) -> Optional['ASTGraphNodeTableReferenceProto']:
        """Field source_node_reference"""
        return self._proto.source_node_reference

    @cached_property
    def dest_node_reference(self) -> Optional['ASTGraphNodeTableReferenceProto']:
        """Field dest_node_reference"""
        return self._proto.dest_node_reference

    @cached_property
    def label_properties_list(self) -> Optional['ASTGraphElementLabelAndPropertiesListProto']:
        """Field label_properties_list"""
        return self._proto.label_properties_list

    @cached_property
    def dynamic_label(self) -> Optional['ASTGraphDynamicLabelProto']:
        """Field dynamic_label"""
        return self._proto.dynamic_label

    @cached_property
    def dynamic_properties(self) -> Optional['ASTGraphDynamicPropertiesProto']:
        """Field dynamic_properties"""
        return self._proto.dynamic_properties



class ASTGraphLabelExpression(ASTNode):
    """Generated wrapper for ASTGraphLabelExpressionProto"""

    def __init__(self, proto: 'ASTGraphLabelExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized



class ASTGraphLabelFilter(ASTNode):
    """Generated wrapper for ASTGraphLabelFilterProto"""

    def __init__(self, proto: 'ASTGraphLabelFilterProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def label_expression(self) -> Optional['AnyASTGraphLabelExpressionProto']:
        """Field label_expression"""
        return self._proto.label_expression



class ASTGraphLhsHint(ASTNode):
    """Generated wrapper for ASTGraphLhsHintProto"""

    def __init__(self, proto: 'ASTGraphLhsHintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint



class ASTGraphNodeTableReference(ASTNode):
    """Generated wrapper for ASTGraphNodeTableReferenceProto"""

    def __init__(self, proto: 'ASTGraphNodeTableReferenceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def node_table_identifier(self) -> Optional['ASTIdentifierProto']:
        """Field node_table_identifier"""
        return self._proto.node_table_identifier

    @cached_property
    def edge_table_columns(self) -> Optional['ASTColumnListProto']:
        """Field edge_table_columns"""
        return self._proto.edge_table_columns

    @cached_property
    def node_table_columns(self) -> Optional['ASTColumnListProto']:
        """Field node_table_columns"""
        return self._proto.node_table_columns

    @cached_property
    def node_reference_type(self) -> Optional[int]:
        """Field node_reference_type"""
        return self._proto.node_reference_type



class ASTGraphPathBase(ASTNode):
    """Generated wrapper for ASTGraphPathBaseProto"""

    def __init__(self, proto: 'ASTGraphPathBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.quantifier



class ASTGraphPathMode(ASTNode):
    """Generated wrapper for ASTGraphPathModeProto"""

    def __init__(self, proto: 'ASTGraphPathModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def path_mode(self) -> Optional[int]:
        """Field path_mode"""
        return self._proto.path_mode



class ASTGraphPathSearchPrefixCount(ASTNode):
    """Generated wrapper for ASTGraphPathSearchPrefixCountProto"""

    def __init__(self, proto: 'ASTGraphPathSearchPrefixCountProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def path_count(self) -> Optional['AnyASTExpressionProto']:
        """Field path_count"""
        return self._proto.path_count



class ASTGraphPathSearchPrefix(ASTNode):
    """Generated wrapper for ASTGraphPathSearchPrefixProto"""

    def __init__(self, proto: 'ASTGraphPathSearchPrefixProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def type(self) -> Optional[int]:
        """Field type"""
        return self._proto.type

    @cached_property
    def path_count(self) -> Optional['ASTGraphPathSearchPrefixCountProto']:
        """Field path_count"""
        return self._proto.path_count



class ASTGraphPattern(ASTNode):
    """Generated wrapper for ASTGraphPatternProto"""

    def __init__(self, proto: 'ASTGraphPatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def paths(self) -> List['ASTGraphPathPatternProto']:
        """Field paths"""
        return self._proto.paths

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause



class ASTGraphProperties(ASTNode):
    """Generated wrapper for ASTGraphPropertiesProto"""

    def __init__(self, proto: 'ASTGraphPropertiesProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def no_properties(self) -> Optional[bool]:
        """Field no_properties"""
        return self._proto.no_properties

    @cached_property
    def derived_property_list(self) -> Optional['ASTGraphDerivedPropertyListProto']:
        """Field derived_property_list"""
        return self._proto.derived_property_list

    @cached_property
    def all_except_columns(self) -> Optional['ASTColumnListProto']:
        """Field all_except_columns"""
        return self._proto.all_except_columns



class ASTGraphPropertyNameAndValue(ASTNode):
    """Generated wrapper for ASTGraphPropertyNameAndValueProto"""

    def __init__(self, proto: 'ASTGraphPropertyNameAndValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def property_name(self) -> Optional['ASTIdentifierProto']:
        """Field property_name"""
        return self._proto.property_name

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTGraphPropertySpecification(ASTNode):
    """Generated wrapper for ASTGraphPropertySpecificationProto"""

    def __init__(self, proto: 'ASTGraphPropertySpecificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def property_name_and_value(self) -> List['ASTGraphPropertyNameAndValueProto']:
        """Field property_name_and_value"""
        return self._proto.property_name_and_value



class ASTGraphRhsHint(ASTNode):
    """Generated wrapper for ASTGraphRhsHintProto"""

    def __init__(self, proto: 'ASTGraphRhsHintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint



class ASTGroupByAll(ASTNode):
    """Generated wrapper for ASTGroupByAllProto"""

    def __init__(self, proto: 'ASTGroupByAllProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTGroupBy(ASTNode):
    """Generated wrapper for ASTGroupByProto"""

    def __init__(self, proto: 'ASTGroupByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def all(self) -> Optional['ASTGroupByAllProto']:
        """Field all"""
        return self._proto.all

    @cached_property
    def grouping_items(self) -> List['ASTGroupingItemProto']:
        """Field grouping_items"""
        return self._proto.grouping_items

    @cached_property
    def and_order_by(self) -> Optional[bool]:
        """Field and_order_by"""
        return self._proto.and_order_by



class ASTGroupingItemOrder(ASTNode):
    """Generated wrapper for ASTGroupingItemOrderProto"""

    def __init__(self, proto: 'ASTGroupingItemOrderProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def ordering_spec(self) -> Optional[int]:
        """Field ordering_spec"""
        return self._proto.ordering_spec

    @cached_property
    def null_order(self) -> Optional['ASTNullOrderProto']:
        """Field null_order"""
        return self._proto.null_order



class ASTGroupingItem(ASTNode):
    """Generated wrapper for ASTGroupingItemProto"""

    def __init__(self, proto: 'ASTGroupingItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def rollup(self) -> Optional['ASTRollupProto']:
        """Field rollup"""
        return self._proto.rollup

    @cached_property
    def cube(self) -> Optional['ASTCubeProto']:
        """Field cube"""
        return self._proto.cube

    @cached_property
    def grouping_set_list(self) -> Optional['ASTGroupingSetListProto']:
        """Field grouping_set_list"""
        return self._proto.grouping_set_list

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def grouping_item_order(self) -> Optional['ASTGroupingItemOrderProto']:
        """Field grouping_item_order"""
        return self._proto.grouping_item_order



class ASTGroupingSetList(ASTNode):
    """Generated wrapper for ASTGroupingSetListProto"""

    def __init__(self, proto: 'ASTGroupingSetListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def grouping_sets(self) -> List['ASTGroupingSetProto']:
        """Field grouping_sets"""
        return self._proto.grouping_sets



class ASTGroupingSet(ASTNode):
    """Generated wrapper for ASTGroupingSetProto"""

    def __init__(self, proto: 'ASTGroupingSetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def rollup(self) -> Optional['ASTRollupProto']:
        """Field rollup"""
        return self._proto.rollup

    @cached_property
    def cube(self) -> Optional['ASTCubeProto']:
        """Field cube"""
        return self._proto.cube



class ASTHavingModifier(ASTNode):
    """Generated wrapper for ASTHavingModifierProto"""

    def __init__(self, proto: 'ASTHavingModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def modifier_kind(self) -> Optional[int]:
        """Field modifier_kind"""
        return self._proto.modifier_kind



class ASTHaving(ASTNode):
    """Generated wrapper for ASTHavingProto"""

    def __init__(self, proto: 'ASTHavingProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTHintEntry(ASTNode):
    """Generated wrapper for ASTHintEntryProto"""

    def __init__(self, proto: 'ASTHintEntryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def qualifier(self) -> Optional['ASTIdentifierProto']:
        """Field qualifier"""
        return self._proto.qualifier

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTHint(ASTNode):
    """Generated wrapper for ASTHintProto"""

    def __init__(self, proto: 'ASTHintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def num_shards_hint(self) -> Optional['ASTIntLiteralProto']:
        """Field num_shards_hint"""
        return self._proto.num_shards_hint

    @cached_property
    def hint_entries(self) -> List['ASTHintEntryProto']:
        """Field hint_entries"""
        return self._proto.hint_entries



class ASTIdentifierList(ASTNode):
    """Generated wrapper for ASTIdentifierListProto"""

    def __init__(self, proto: 'ASTIdentifierListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier_list(self) -> List['ASTIdentifierProto']:
        """Field identifier_list"""
        return self._proto.identifier_list



class ASTIdentityColumnIncrementBy(ASTNode):
    """Generated wrapper for ASTIdentityColumnIncrementByProto"""

    def __init__(self, proto: 'ASTIdentityColumnIncrementByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTIdentityColumnInfo(ASTNode):
    """Generated wrapper for ASTIdentityColumnInfoProto"""

    def __init__(self, proto: 'ASTIdentityColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def start_with_value(self) -> Optional['ASTIdentityColumnStartWithProto']:
        """Field start_with_value"""
        return self._proto.start_with_value

    @cached_property
    def increment_by_value(self) -> Optional['ASTIdentityColumnIncrementByProto']:
        """Field increment_by_value"""
        return self._proto.increment_by_value

    @cached_property
    def max_value(self) -> Optional['ASTIdentityColumnMaxValueProto']:
        """Field max_value"""
        return self._proto.max_value

    @cached_property
    def min_value(self) -> Optional['ASTIdentityColumnMinValueProto']:
        """Field min_value"""
        return self._proto.min_value

    @cached_property
    def cycling_enabled(self) -> Optional[bool]:
        """Field cycling_enabled"""
        return self._proto.cycling_enabled



class ASTIdentityColumnMaxValue(ASTNode):
    """Generated wrapper for ASTIdentityColumnMaxValueProto"""

    def __init__(self, proto: 'ASTIdentityColumnMaxValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTIdentityColumnMinValue(ASTNode):
    """Generated wrapper for ASTIdentityColumnMinValueProto"""

    def __init__(self, proto: 'ASTIdentityColumnMinValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTIdentityColumnStartWith(ASTNode):
    """Generated wrapper for ASTIdentityColumnStartWithProto"""

    def __init__(self, proto: 'ASTIdentityColumnStartWithProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTInList(ASTNode):
    """Generated wrapper for ASTInListProto"""

    def __init__(self, proto: 'ASTInListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def list(self) -> List['AnyASTExpressionProto']:
        """Field list"""
        return self._proto.list



class ASTIndexItemList(ASTNode):
    """Generated wrapper for ASTIndexItemListProto"""

    def __init__(self, proto: 'ASTIndexItemListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def ordering_expressions(self) -> List['ASTOrderingExpressionProto']:
        """Field ordering_expressions"""
        return self._proto.ordering_expressions



class ASTIndexStoringExpressionList(ASTNode):
    """Generated wrapper for ASTIndexStoringExpressionListProto"""

    def __init__(self, proto: 'ASTIndexStoringExpressionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expressions(self) -> List['AnyASTExpressionProto']:
        """Field expressions"""
        return self._proto.expressions



class ASTIndexUnnestExpressionList(ASTNode):
    """Generated wrapper for ASTIndexUnnestExpressionListProto"""

    def __init__(self, proto: 'ASTIndexUnnestExpressionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def unnest_expressions(self) -> List['ASTUnnestExpressionWithOptAliasAndOffsetProto']:
        """Field unnest_expressions"""
        return self._proto.unnest_expressions



class ASTInputOutputClause(ASTNode):
    """Generated wrapper for ASTInputOutputClauseProto"""

    def __init__(self, proto: 'ASTInputOutputClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def input(self) -> Optional['ASTTableElementListProto']:
        """Field input"""
        return self._proto.input

    @cached_property
    def output(self) -> Optional['ASTTableElementListProto']:
        """Field output"""
        return self._proto.output



class ASTInsertValuesRowList(ASTNode):
    """Generated wrapper for ASTInsertValuesRowListProto"""

    def __init__(self, proto: 'ASTInsertValuesRowListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def rows(self) -> List['ASTInsertValuesRowProto']:
        """Field rows"""
        return self._proto.rows



class ASTInsertValuesRow(ASTNode):
    """Generated wrapper for ASTInsertValuesRowProto"""

    def __init__(self, proto: 'ASTInsertValuesRowProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def values(self) -> List['AnyASTExpressionProto']:
        """Field values"""
        return self._proto.values



class ASTIntoAlias(ASTNode):
    """Generated wrapper for ASTIntoAliasProto"""

    def __init__(self, proto: 'ASTIntoAliasProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier



class ASTLabel(ASTNode):
    """Generated wrapper for ASTLabelProto"""

    def __init__(self, proto: 'ASTLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTLimitAll(ASTNode):
    """Generated wrapper for ASTLimitAllProto"""

    def __init__(self, proto: 'ASTLimitAllProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTLimitOffset(ASTNode):
    """Generated wrapper for ASTLimitOffsetProto"""

    def __init__(self, proto: 'ASTLimitOffsetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def limit(self) -> Optional['ASTLimitProto']:
        """Field limit"""
        return self._proto.limit

    @cached_property
    def offset(self) -> Optional['AnyASTExpressionProto']:
        """Field offset"""
        return self._proto.offset



class ASTLimit(ASTNode):
    """Generated wrapper for ASTLimitProto"""

    def __init__(self, proto: 'ASTLimitProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def all(self) -> Optional['ASTLimitAllProto']:
        """Field all"""
        return self._proto.all

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTLocation(ASTNode):
    """Generated wrapper for ASTLocationProto"""

    def __init__(self, proto: 'ASTLocationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTLockMode(ASTNode):
    """Generated wrapper for ASTLockModeProto"""

    def __init__(self, proto: 'ASTLockModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def strength(self) -> Optional[int]:
        """Field strength"""
        return self._proto.strength



class ASTMergeAction(ASTNode):
    """Generated wrapper for ASTMergeActionProto"""

    def __init__(self, proto: 'ASTMergeActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def insert_column_list(self) -> Optional['ASTColumnListProto']:
        """Field insert_column_list"""
        return self._proto.insert_column_list

    @cached_property
    def insert_row(self) -> Optional['ASTInsertValuesRowProto']:
        """Field insert_row"""
        return self._proto.insert_row

    @cached_property
    def update_item_list(self) -> Optional['ASTUpdateItemListProto']:
        """Field update_item_list"""
        return self._proto.update_item_list

    @cached_property
    def action_type(self) -> Optional[int]:
        """Field action_type"""
        return self._proto.action_type



class ASTMergeWhenClauseList(ASTNode):
    """Generated wrapper for ASTMergeWhenClauseListProto"""

    def __init__(self, proto: 'ASTMergeWhenClauseListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def clause_list(self) -> List['ASTMergeWhenClauseProto']:
        """Field clause_list"""
        return self._proto.clause_list



class ASTMergeWhenClause(ASTNode):
    """Generated wrapper for ASTMergeWhenClauseProto"""

    def __init__(self, proto: 'ASTMergeWhenClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def search_condition(self) -> Optional['AnyASTExpressionProto']:
        """Field search_condition"""
        return self._proto.search_condition

    @cached_property
    def action(self) -> Optional['ASTMergeActionProto']:
        """Field action"""
        return self._proto.action

    @cached_property
    def match_type(self) -> Optional[int]:
        """Field match_type"""
        return self._proto.match_type



class ASTModelClause(ASTNode):
    """Generated wrapper for ASTModelClauseProto"""

    def __init__(self, proto: 'ASTModelClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def model_path(self) -> Optional['ASTPathExpressionProto']:
        """Field model_path"""
        return self._proto.model_path



class ASTNewConstructorArg(ASTNode):
    """Generated wrapper for ASTNewConstructorArgProto"""

    def __init__(self, proto: 'ASTNewConstructorArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def optional_identifier(self) -> Optional['ASTIdentifierProto']:
        """Field optional_identifier"""
        return self._proto.optional_identifier

    @cached_property
    def optional_path_expression(self) -> Optional['ASTPathExpressionProto']:
        """Field optional_path_expression"""
        return self._proto.optional_path_expression



class ASTNullOrder(ASTNode):
    """Generated wrapper for ASTNullOrderProto"""

    def __init__(self, proto: 'ASTNullOrderProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def nulls_first(self) -> Optional[bool]:
        """Field nulls_first"""
        return self._proto.nulls_first



class ASTOnClause(ASTNode):
    """Generated wrapper for ASTOnClauseProto"""

    def __init__(self, proto: 'ASTOnClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTOnConflictClause(ASTNode):
    """Generated wrapper for ASTOnConflictClauseProto"""

    def __init__(self, proto: 'ASTOnConflictClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def conflict_action(self) -> Optional[int]:
        """Field conflict_action"""
        return self._proto.conflict_action

    @cached_property
    def conflict_target(self) -> Optional['ASTColumnListProto']:
        """Field conflict_target"""
        return self._proto.conflict_target

    @cached_property
    def unique_constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field unique_constraint_name"""
        return self._proto.unique_constraint_name

    @cached_property
    def update_item_list(self) -> Optional['ASTUpdateItemListProto']:
        """Field update_item_list"""
        return self._proto.update_item_list

    @cached_property
    def update_where_clause(self) -> Optional['AnyASTExpressionProto']:
        """Field update_where_clause"""
        return self._proto.update_where_clause



class ASTOnOrUsingClauseList(ASTNode):
    """Generated wrapper for ASTOnOrUsingClauseListProto"""

    def __init__(self, proto: 'ASTOnOrUsingClauseListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def on_or_using_clause_list(self) -> List['ASTNodeProto']:
        """Field on_or_using_clause_list"""
        return self._proto.on_or_using_clause_list



class ASTOptionsEntry(ASTNode):
    """Generated wrapper for ASTOptionsEntryProto"""

    def __init__(self, proto: 'ASTOptionsEntryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value

    @cached_property
    def assignment_op(self) -> Optional[int]:
        """Field assignment_op"""
        return self._proto.assignment_op



class ASTOptionsList(ASTNode):
    """Generated wrapper for ASTOptionsListProto"""

    def __init__(self, proto: 'ASTOptionsListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def options_entries(self) -> List['ASTOptionsEntryProto']:
        """Field options_entries"""
        return self._proto.options_entries



class ASTOrderBy(ASTNode):
    """Generated wrapper for ASTOrderByProto"""

    def __init__(self, proto: 'ASTOrderByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def ordering_expressions(self) -> List['ASTOrderingExpressionProto']:
        """Field ordering_expressions"""
        return self._proto.ordering_expressions



class ASTOrderingExpression(ASTNode):
    """Generated wrapper for ASTOrderingExpressionProto"""

    def __init__(self, proto: 'ASTOrderingExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate

    @cached_property
    def null_order(self) -> Optional['ASTNullOrderProto']:
        """Field null_order"""
        return self._proto.null_order

    @cached_property
    def ordering_spec(self) -> Optional[int]:
        """Field ordering_spec"""
        return self._proto.ordering_spec

    @cached_property
    def option_list(self) -> Optional['ASTOptionsListProto']:
        """Field option_list"""
        return self._proto.option_list



class ASTPartitionBy(ASTNode):
    """Generated wrapper for ASTPartitionByProto"""

    def __init__(self, proto: 'ASTPartitionByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def partitioning_expressions(self) -> List['AnyASTExpressionProto']:
        """Field partitioning_expressions"""
        return self._proto.partitioning_expressions



class ASTPathExpressionList(ASTNode):
    """Generated wrapper for ASTPathExpressionListProto"""

    def __init__(self, proto: 'ASTPathExpressionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def path_expression_list(self) -> List['ASTPathExpressionProto']:
        """Field path_expression_list"""
        return self._proto.path_expression_list



class ASTPipeOperator(ASTNode):
    """Generated wrapper for ASTPipeOperatorProto"""

    def __init__(self, proto: 'ASTPipeOperatorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTPipeSetItem(ASTNode):
    """Generated wrapper for ASTPipeSetItemProto"""

    def __init__(self, proto: 'ASTPipeSetItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ASTIdentifierProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTPivotExpressionList(ASTNode):
    """Generated wrapper for ASTPivotExpressionListProto"""

    def __init__(self, proto: 'ASTPivotExpressionListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expressions(self) -> List['ASTPivotExpressionProto']:
        """Field expressions"""
        return self._proto.expressions



class ASTPivotExpression(ASTNode):
    """Generated wrapper for ASTPivotExpressionProto"""

    def __init__(self, proto: 'ASTPivotExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTPivotValueList(ASTNode):
    """Generated wrapper for ASTPivotValueListProto"""

    def __init__(self, proto: 'ASTPivotValueListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def values(self) -> List['ASTPivotValueProto']:
        """Field values"""
        return self._proto.values



class ASTPivotValue(ASTNode):
    """Generated wrapper for ASTPivotValueProto"""

    def __init__(self, proto: 'ASTPivotValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTPostfixTableOperator(ASTNode):
    """Generated wrapper for ASTPostfixTableOperatorProto"""

    def __init__(self, proto: 'ASTPostfixTableOperatorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTPrimaryKeyElementList(ASTNode):
    """Generated wrapper for ASTPrimaryKeyElementListProto"""

    def __init__(self, proto: 'ASTPrimaryKeyElementListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def elements(self) -> List['ASTPrimaryKeyElementProto']:
        """Field elements"""
        return self._proto.elements



class ASTPrimaryKeyElement(ASTNode):
    """Generated wrapper for ASTPrimaryKeyElementProto"""

    def __init__(self, proto: 'ASTPrimaryKeyElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ASTIdentifierProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def ordering_spec(self) -> Optional[int]:
        """Field ordering_spec"""
        return self._proto.ordering_spec

    @cached_property
    def null_order(self) -> Optional['ASTNullOrderProto']:
        """Field null_order"""
        return self._proto.null_order



class ASTPrivilege(ASTNode):
    """Generated wrapper for ASTPrivilegeProto"""

    def __init__(self, proto: 'ASTPrivilegeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def privilege_action(self) -> Optional['ASTIdentifierProto']:
        """Field privilege_action"""
        return self._proto.privilege_action

    @cached_property
    def paths(self) -> Optional['ASTPathExpressionListProto']:
        """Field paths"""
        return self._proto.paths



class ASTPrivileges(ASTNode):
    """Generated wrapper for ASTPrivilegesProto"""

    def __init__(self, proto: 'ASTPrivilegesProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def privileges(self) -> List['ASTPrivilegeProto']:
        """Field privileges"""
        return self._proto.privileges



class ASTQualify(ASTNode):
    """Generated wrapper for ASTQualifyProto"""

    def __init__(self, proto: 'ASTQualifyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTQuantifierBound(ASTNode):
    """Generated wrapper for ASTQuantifierBoundProto"""

    def __init__(self, proto: 'ASTQuantifierBoundProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def bound(self) -> Optional['AnyASTExpressionProto']:
        """Field bound"""
        return self._proto.bound



class ASTQuantifier(ASTNode):
    """Generated wrapper for ASTQuantifierProto"""

    def __init__(self, proto: 'ASTQuantifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def is_reluctant(self) -> Optional[bool]:
        """Field is_reluctant"""
        return self._proto.is_reluctant



class ASTQueryExpression(ASTNode):
    """Generated wrapper for ASTQueryExpressionProto"""

    def __init__(self, proto: 'ASTQueryExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized



class ASTRecursionDepthModifier(ASTNode):
    """Generated wrapper for ASTRecursionDepthModifierProto"""

    def __init__(self, proto: 'ASTRecursionDepthModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def lower_bound(self) -> Optional['ASTIntOrUnboundedProto']:
        """Field lower_bound"""
        return self._proto.lower_bound

    @cached_property
    def upper_bound(self) -> Optional['ASTIntOrUnboundedProto']:
        """Field upper_bound"""
        return self._proto.upper_bound



class ASTRepeatableClause(ASTNode):
    """Generated wrapper for ASTRepeatableClauseProto"""

    def __init__(self, proto: 'ASTRepeatableClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def argument(self) -> Optional['AnyASTExpressionProto']:
        """Field argument"""
        return self._proto.argument



class ASTReplaceFieldsArg(ASTNode):
    """Generated wrapper for ASTReplaceFieldsArgProto"""

    def __init__(self, proto: 'ASTReplaceFieldsArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def path_expression(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field path_expression"""
        return self._proto.path_expression



class ASTReturningClause(ASTNode):
    """Generated wrapper for ASTReturningClauseProto"""

    def __init__(self, proto: 'ASTReturningClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def select_list(self) -> Optional['ASTSelectListProto']:
        """Field select_list"""
        return self._proto.select_list

    @cached_property
    def action_alias(self) -> Optional['ASTAliasProto']:
        """Field action_alias"""
        return self._proto.action_alias



class ASTRollup(ASTNode):
    """Generated wrapper for ASTRollupProto"""

    def __init__(self, proto: 'ASTRollupProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expressions(self) -> List['AnyASTExpressionProto']:
        """Field expressions"""
        return self._proto.expressions



class ASTRowPatternExpression(ASTNode):
    """Generated wrapper for ASTRowPatternExpressionProto"""

    def __init__(self, proto: 'ASTRowPatternExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized



class ASTSampleSize(ASTNode):
    """Generated wrapper for ASTSampleSizeProto"""

    def __init__(self, proto: 'ASTSampleSizeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def size(self) -> Optional['AnyASTExpressionProto']:
        """Field size"""
        return self._proto.size

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def unit(self) -> Optional[int]:
        """Field unit"""
        return self._proto.unit



class ASTSampleSuffix(ASTNode):
    """Generated wrapper for ASTSampleSuffixProto"""

    def __init__(self, proto: 'ASTSampleSuffixProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def weight(self) -> Optional['ASTWithWeightProto']:
        """Field weight"""
        return self._proto.weight

    @cached_property
    def repeat(self) -> Optional['ASTRepeatableClauseProto']:
        """Field repeat"""
        return self._proto.repeat



class ASTScript(ASTNode):
    """Generated wrapper for ASTScriptProto"""

    def __init__(self, proto: 'ASTScriptProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def statement_list_node(self) -> Optional['ASTStatementListProto']:
        """Field statement_list_node"""
        return self._proto.statement_list_node



class ASTSelectAs(ASTNode):
    """Generated wrapper for ASTSelectAsProto"""

    def __init__(self, proto: 'ASTSelectAsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def type_name(self) -> Optional['ASTPathExpressionProto']:
        """Field type_name"""
        return self._proto.type_name

    @cached_property
    def as_mode(self) -> Optional[int]:
        """Field as_mode"""
        return self._proto.as_mode



class ASTSelectColumn(ASTNode):
    """Generated wrapper for ASTSelectColumnProto"""

    def __init__(self, proto: 'ASTSelectColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def grouping_item_order(self) -> Optional['ASTGroupingItemOrderProto']:
        """Field grouping_item_order"""
        return self._proto.grouping_item_order



class ASTSelectList(ASTNode):
    """Generated wrapper for ASTSelectListProto"""

    def __init__(self, proto: 'ASTSelectListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def columns(self) -> List['ASTSelectColumnProto']:
        """Field columns"""
        return self._proto.columns



class ASTSelectWith(ASTNode):
    """Generated wrapper for ASTSelectWithProto"""

    def __init__(self, proto: 'ASTSelectWithProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def options(self) -> Optional['ASTOptionsListProto']:
        """Field options"""
        return self._proto.options



class ASTSetOperationAllOrDistinct(ASTNode):
    """Generated wrapper for ASTSetOperationAllOrDistinctProto"""

    def __init__(self, proto: 'ASTSetOperationAllOrDistinctProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional[int]:
        """Field value"""
        return self._proto.value



class ASTSetOperationColumnMatchMode(ASTNode):
    """Generated wrapper for ASTSetOperationColumnMatchModeProto"""

    def __init__(self, proto: 'ASTSetOperationColumnMatchModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional[int]:
        """Field value"""
        return self._proto.value



class ASTSetOperationColumnPropagationMode(ASTNode):
    """Generated wrapper for ASTSetOperationColumnPropagationModeProto"""

    def __init__(self, proto: 'ASTSetOperationColumnPropagationModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional[int]:
        """Field value"""
        return self._proto.value



class ASTSetOperationMetadataList(ASTNode):
    """Generated wrapper for ASTSetOperationMetadataListProto"""

    def __init__(self, proto: 'ASTSetOperationMetadataListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def set_operation_metadata_list(self) -> List['ASTSetOperationMetadataProto']:
        """Field set_operation_metadata_list"""
        return self._proto.set_operation_metadata_list



class ASTSetOperationMetadata(ASTNode):
    """Generated wrapper for ASTSetOperationMetadataProto"""

    def __init__(self, proto: 'ASTSetOperationMetadataProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def op_type(self) -> Optional['ASTSetOperationTypeProto']:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def all_or_distinct(self) -> Optional['ASTSetOperationAllOrDistinctProto']:
        """Field all_or_distinct"""
        return self._proto.all_or_distinct

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def column_match_mode(self) -> Optional['ASTSetOperationColumnMatchModeProto']:
        """Field column_match_mode"""
        return self._proto.column_match_mode

    @cached_property
    def column_propagation_mode(self) -> Optional['ASTSetOperationColumnPropagationModeProto']:
        """Field column_propagation_mode"""
        return self._proto.column_propagation_mode

    @cached_property
    def corresponding_by_column_list(self) -> Optional['ASTColumnListProto']:
        """Field corresponding_by_column_list"""
        return self._proto.corresponding_by_column_list



class ASTSetOperationType(ASTNode):
    """Generated wrapper for ASTSetOperationTypeProto"""

    def __init__(self, proto: 'ASTSetOperationTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def value(self) -> Optional[int]:
        """Field value"""
        return self._proto.value



class ASTSpannerInterleaveClause(ASTNode):
    """Generated wrapper for ASTSpannerInterleaveClauseProto"""

    def __init__(self, proto: 'ASTSpannerInterleaveClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def type(self) -> Optional[int]:
        """Field type"""
        return self._proto.type

    @cached_property
    def action(self) -> Optional[int]:
        """Field action"""
        return self._proto.action



class ASTSpannerTableOptions(ASTNode):
    """Generated wrapper for ASTSpannerTableOptionsProto"""

    def __init__(self, proto: 'ASTSpannerTableOptionsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def primary_key(self) -> Optional['ASTPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.primary_key

    @cached_property
    def interleave_clause(self) -> Optional['ASTSpannerInterleaveClauseProto']:
        """Field interleave_clause"""
        return self._proto.interleave_clause



class ASTSqlFunctionBody(ASTNode):
    """Generated wrapper for ASTSqlFunctionBodyProto"""

    def __init__(self, proto: 'ASTSqlFunctionBodyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTStarExceptList(ASTNode):
    """Generated wrapper for ASTStarExceptListProto"""

    def __init__(self, proto: 'ASTStarExceptListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def identifiers(self) -> List['ASTIdentifierProto']:
        """Field identifiers"""
        return self._proto.identifiers



class ASTStarModifiers(ASTNode):
    """Generated wrapper for ASTStarModifiersProto"""

    def __init__(self, proto: 'ASTStarModifiersProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def except_list(self) -> Optional['ASTStarExceptListProto']:
        """Field except_list"""
        return self._proto.except_list

    @cached_property
    def replace_items(self) -> List['ASTStarReplaceItemProto']:
        """Field replace_items"""
        return self._proto.replace_items



class ASTStarReplaceItem(ASTNode):
    """Generated wrapper for ASTStarReplaceItemProto"""

    def __init__(self, proto: 'ASTStarReplaceItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTIdentifierProto']:
        """Field alias"""
        return self._proto.alias



class ASTStatementList(ASTNode):
    """Generated wrapper for ASTStatementListProto"""

    def __init__(self, proto: 'ASTStatementListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def statement_list(self) -> List['AnyASTStatementProto']:
        """Field statement_list"""
        return self._proto.statement_list

    @cached_property
    def variable_declarations_allowed(self) -> Optional[bool]:
        """Field variable_declarations_allowed"""
        return self._proto.variable_declarations_allowed



class ASTStatement(ASTNode):
    """Generated wrapper for ASTStatementProto"""

    def __init__(self, proto: 'ASTStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTStructColumnField(ASTNode):
    """Generated wrapper for ASTStructColumnFieldProto"""

    def __init__(self, proto: 'ASTStructColumnFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field schema"""
        return self._proto.schema



class ASTStructConstructorArg(ASTNode):
    """Generated wrapper for ASTStructConstructorArgProto"""

    def __init__(self, proto: 'ASTStructConstructorArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTStructField(ASTNode):
    """Generated wrapper for ASTStructFieldProto"""

    def __init__(self, proto: 'ASTStructFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['AnyASTTypeProto']:
        """Field type"""
        return self._proto.type



class ASTSubpipeline(ASTNode):
    """Generated wrapper for ASTSubpipelineProto"""

    def __init__(self, proto: 'ASTSubpipelineProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def pipe_operator_list(self) -> List['AnyASTPipeOperatorProto']:
        """Field pipe_operator_list"""
        return self._proto.pipe_operator_list

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized



class ASTTVFArgument(ASTNode):
    """Generated wrapper for ASTTVFArgumentProto"""

    def __init__(self, proto: 'ASTTVFArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def table_clause(self) -> Optional['ASTTableClauseProto']:
        """Field table_clause"""
        return self._proto.table_clause

    @cached_property
    def model_clause(self) -> Optional['ASTModelClauseProto']:
        """Field model_clause"""
        return self._proto.model_clause

    @cached_property
    def connection_clause(self) -> Optional['ASTConnectionClauseProto']:
        """Field connection_clause"""
        return self._proto.connection_clause

    @cached_property
    def desc(self) -> Optional['ASTDescriptorProto']:
        """Field desc"""
        return self._proto.desc



class ASTTVFSchemaColumn(ASTNode):
    """Generated wrapper for ASTTVFSchemaColumnProto"""

    def __init__(self, proto: 'ASTTVFSchemaColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['AnyASTTypeProto']:
        """Field type"""
        return self._proto.type



class ASTTVFSchema(ASTNode):
    """Generated wrapper for ASTTVFSchemaProto"""

    def __init__(self, proto: 'ASTTVFSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def columns(self) -> List['ASTTVFSchemaColumnProto']:
        """Field columns"""
        return self._proto.columns



class ASTTableAndColumnInfoList(ASTNode):
    """Generated wrapper for ASTTableAndColumnInfoListProto"""

    def __init__(self, proto: 'ASTTableAndColumnInfoListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_and_column_info_entries(self) -> List['ASTTableAndColumnInfoProto']:
        """Field table_and_column_info_entries"""
        return self._proto.table_and_column_info_entries



class ASTTableAndColumnInfo(ASTNode):
    """Generated wrapper for ASTTableAndColumnInfoProto"""

    def __init__(self, proto: 'ASTTableAndColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def column_list(self) -> Optional['ASTColumnListProto']:
        """Field column_list"""
        return self._proto.column_list



class ASTTableElementList(ASTNode):
    """Generated wrapper for ASTTableElementListProto"""

    def __init__(self, proto: 'ASTTableElementListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def elements(self) -> List['AnyASTTableElementProto']:
        """Field elements"""
        return self._proto.elements



class ASTTableElement(ASTNode):
    """Generated wrapper for ASTTableElementProto"""

    def __init__(self, proto: 'ASTTableElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTTableExpression(ASTNode):
    """Generated wrapper for ASTTableExpressionProto"""

    def __init__(self, proto: 'ASTTableExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.postfix_operators



class ASTTemplatedParameterType(ASTNode):
    """Generated wrapper for ASTTemplatedParameterTypeProto"""

    def __init__(self, proto: 'ASTTemplatedParameterTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind



class ASTTransactionModeList(ASTNode):
    """Generated wrapper for ASTTransactionModeListProto"""

    def __init__(self, proto: 'ASTTransactionModeListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def elements(self) -> List['AnyASTTransactionModeProto']:
        """Field elements"""
        return self._proto.elements



class ASTTransactionMode(ASTNode):
    """Generated wrapper for ASTTransactionModeProto"""

    def __init__(self, proto: 'ASTTransactionModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTTransformClause(ASTNode):
    """Generated wrapper for ASTTransformClauseProto"""

    def __init__(self, proto: 'ASTTransformClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def select_list(self) -> Optional['ASTSelectListProto']:
        """Field select_list"""
        return self._proto.select_list



class ASTTtlClause(ASTNode):
    """Generated wrapper for ASTTtlClauseProto"""

    def __init__(self, proto: 'ASTTtlClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTTypeParameterList(ASTNode):
    """Generated wrapper for ASTTypeParameterListProto"""

    def __init__(self, proto: 'ASTTypeParameterListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def parameters(self) -> List['AnyASTLeafProto']:
        """Field parameters"""
        return self._proto.parameters



class ASTType(ASTNode):
    """Generated wrapper for ASTTypeProto"""

    def __init__(self, proto: 'ASTTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ASTUnnestExpression(ASTNode):
    """Generated wrapper for ASTUnnestExpressionProto"""

    def __init__(self, proto: 'ASTUnnestExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expressions(self) -> List['ASTExpressionWithOptAliasProto']:
        """Field expressions"""
        return self._proto.expressions

    @cached_property
    def array_zip_mode(self) -> Optional['ASTNamedArgumentProto']:
        """Field array_zip_mode"""
        return self._proto.array_zip_mode



class ASTUnnestExpressionWithOptAliasAndOffset(ASTNode):
    """Generated wrapper for ASTUnnestExpressionWithOptAliasAndOffsetProto"""

    def __init__(self, proto: 'ASTUnnestExpressionWithOptAliasAndOffsetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def unnest_expression(self) -> Optional['ASTUnnestExpressionProto']:
        """Field unnest_expression"""
        return self._proto.unnest_expression

    @cached_property
    def optional_alias(self) -> Optional['ASTAliasProto']:
        """Field optional_alias"""
        return self._proto.optional_alias

    @cached_property
    def optional_with_offset(self) -> Optional['ASTWithOffsetProto']:
        """Field optional_with_offset"""
        return self._proto.optional_with_offset



class ASTUnpivotInItemLabel(ASTNode):
    """Generated wrapper for ASTUnpivotInItemLabelProto"""

    def __init__(self, proto: 'ASTUnpivotInItemLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def string_label(self) -> Optional['ASTStringLiteralProto']:
        """Field string_label"""
        return self._proto.string_label

    @cached_property
    def int_label(self) -> Optional['ASTIntLiteralProto']:
        """Field int_label"""
        return self._proto.int_label



class ASTUnpivotInItemList(ASTNode):
    """Generated wrapper for ASTUnpivotInItemListProto"""

    def __init__(self, proto: 'ASTUnpivotInItemListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def in_items(self) -> List['ASTUnpivotInItemProto']:
        """Field in_items"""
        return self._proto.in_items



class ASTUnpivotInItem(ASTNode):
    """Generated wrapper for ASTUnpivotInItemProto"""

    def __init__(self, proto: 'ASTUnpivotInItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def unpivot_columns(self) -> Optional['ASTPathExpressionListProto']:
        """Field unpivot_columns"""
        return self._proto.unpivot_columns

    @cached_property
    def alias(self) -> Optional['ASTUnpivotInItemLabelProto']:
        """Field alias"""
        return self._proto.alias



class ASTUntilClause(ASTNode):
    """Generated wrapper for ASTUntilClauseProto"""

    def __init__(self, proto: 'ASTUntilClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition



class ASTUpdateItemList(ASTNode):
    """Generated wrapper for ASTUpdateItemListProto"""

    def __init__(self, proto: 'ASTUpdateItemListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def update_items(self) -> List['ASTUpdateItemProto']:
        """Field update_items"""
        return self._proto.update_items



class ASTUpdateItem(ASTNode):
    """Generated wrapper for ASTUpdateItemProto"""

    def __init__(self, proto: 'ASTUpdateItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def set_value(self) -> Optional['ASTUpdateSetValueProto']:
        """Field set_value"""
        return self._proto.set_value

    @cached_property
    def insert_statement(self) -> Optional['ASTInsertStatementProto']:
        """Field insert_statement"""
        return self._proto.insert_statement

    @cached_property
    def delete_statement(self) -> Optional['ASTDeleteStatementProto']:
        """Field delete_statement"""
        return self._proto.delete_statement

    @cached_property
    def update_statement(self) -> Optional['ASTUpdateStatementProto']:
        """Field update_statement"""
        return self._proto.update_statement



class ASTUpdateSetValue(ASTNode):
    """Generated wrapper for ASTUpdateSetValueProto"""

    def __init__(self, proto: 'ASTUpdateSetValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field path"""
        return self._proto.path

    @cached_property
    def value(self) -> Optional['AnyASTExpressionProto']:
        """Field value"""
        return self._proto.value



class ASTUsingClause(ASTNode):
    """Generated wrapper for ASTUsingClauseProto"""

    def __init__(self, proto: 'ASTUsingClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def keys(self) -> List['ASTIdentifierProto']:
        """Field keys"""
        return self._proto.keys



class ASTWhenThenClauseList(ASTNode):
    """Generated wrapper for ASTWhenThenClauseListProto"""

    def __init__(self, proto: 'ASTWhenThenClauseListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def when_then_clauses(self) -> List['ASTWhenThenClauseProto']:
        """Field when_then_clauses"""
        return self._proto.when_then_clauses



class ASTWhenThenClause(ASTNode):
    """Generated wrapper for ASTWhenThenClauseProto"""

    def __init__(self, proto: 'ASTWhenThenClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.body



class ASTWhereClause(ASTNode):
    """Generated wrapper for ASTWhereClauseProto"""

    def __init__(self, proto: 'ASTWhereClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTWindowClause(ASTNode):
    """Generated wrapper for ASTWindowClauseProto"""

    def __init__(self, proto: 'ASTWindowClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def windows(self) -> List['ASTWindowDefinitionProto']:
        """Field windows"""
        return self._proto.windows



class ASTWindowDefinition(ASTNode):
    """Generated wrapper for ASTWindowDefinitionProto"""

    def __init__(self, proto: 'ASTWindowDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def window_spec(self) -> Optional['ASTWindowSpecificationProto']:
        """Field window_spec"""
        return self._proto.window_spec



class ASTWindowFrameExpr(ASTNode):
    """Generated wrapper for ASTWindowFrameExprProto"""

    def __init__(self, proto: 'ASTWindowFrameExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def boundary_type(self) -> Optional[int]:
        """Field boundary_type"""
        return self._proto.boundary_type



class ASTWindowFrame(ASTNode):
    """Generated wrapper for ASTWindowFrameProto"""

    def __init__(self, proto: 'ASTWindowFrameProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def start_expr(self) -> Optional['ASTWindowFrameExprProto']:
        """Field start_expr"""
        return self._proto.start_expr

    @cached_property
    def end_expr(self) -> Optional['ASTWindowFrameExprProto']:
        """Field end_expr"""
        return self._proto.end_expr

    @cached_property
    def frame_unit(self) -> Optional[int]:
        """Field frame_unit"""
        return self._proto.frame_unit



class ASTWindowSpecification(ASTNode):
    """Generated wrapper for ASTWindowSpecificationProto"""

    def __init__(self, proto: 'ASTWindowSpecificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def base_window_name(self) -> Optional['ASTIdentifierProto']:
        """Field base_window_name"""
        return self._proto.base_window_name

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def window_frame(self) -> Optional['ASTWindowFrameProto']:
        """Field window_frame"""
        return self._proto.window_frame



class ASTWithClause(ASTNode):
    """Generated wrapper for ASTWithClauseProto"""

    def __init__(self, proto: 'ASTWithClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def with_(self) -> List['ASTAliasedQueryProto']:
        """Field with (escaped from reserved keyword 'with')"""
        return getattr(self._proto, 'with')

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.recursive



class ASTWithConnectionClause(ASTNode):
    """Generated wrapper for ASTWithConnectionClauseProto"""

    def __init__(self, proto: 'ASTWithConnectionClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def connection_clause(self) -> Optional['ASTConnectionClauseProto']:
        """Field connection_clause"""
        return self._proto.connection_clause



class ASTWithOffset(ASTNode):
    """Generated wrapper for ASTWithOffsetProto"""

    def __init__(self, proto: 'ASTWithOffsetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTWithPartitionColumnsClause(ASTNode):
    """Generated wrapper for ASTWithPartitionColumnsClauseProto"""

    def __init__(self, proto: 'ASTWithPartitionColumnsClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def table_element_list(self) -> Optional['ASTTableElementListProto']:
        """Field table_element_list"""
        return self._proto.table_element_list



class ASTWithReportModifier(ASTNode):
    """Generated wrapper for ASTWithReportModifierProto"""

    def __init__(self, proto: 'ASTWithReportModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTWithWeight(ASTNode):
    """Generated wrapper for ASTWithWeightProto"""

    def __init__(self, proto: 'ASTWithWeightProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTYieldItemList(ASTNode):
    """Generated wrapper for ASTYieldItemListProto"""

    def __init__(self, proto: 'ASTYieldItemListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def yield_items(self) -> List['ASTExpressionWithOptAliasProto']:
        """Field yield_items"""
        return self._proto.yield_items



class ResolvedArgument(ResolvedNode):
    """Generated wrapper for ResolvedArgumentProto"""

    def __init__(self, proto: 'ResolvedArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range



class ResolvedExpr(ResolvedNode):
    """Generated wrapper for ResolvedExprProto"""

    def __init__(self, proto: 'ResolvedExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.type_annotation_map



class ResolvedScan(ResolvedNode):
    """Generated wrapper for ResolvedScanProto"""

    def __init__(self, proto: 'ResolvedScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.node_source



class ResolvedStatement(ResolvedNode):
    """Generated wrapper for ResolvedStatementProto"""

    def __init__(self, proto: 'ResolvedStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list



class ASTAbortBatchStatement(ASTStatement):
    """Generated wrapper for ASTAbortBatchStatementProto"""

    def __init__(self, proto: 'ASTAbortBatchStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTAddColumnAction(ASTAlterAction):
    """Generated wrapper for ASTAddColumnActionProto"""

    def __init__(self, proto: 'ASTAddColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_definition(self) -> Optional['ASTColumnDefinitionProto']:
        """Field column_definition"""
        return self._proto.column_definition

    @cached_property
    def column_position(self) -> Optional['ASTColumnPositionProto']:
        """Field column_position"""
        return self._proto.column_position

    @cached_property
    def fill_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field fill_expression"""
        return self._proto.fill_expression

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTAddColumnIdentifierAction(ASTAlterAction):
    """Generated wrapper for ASTAddColumnIdentifierActionProto"""

    def __init__(self, proto: 'ASTAddColumnIdentifierActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTAddConstraintAction(ASTAlterAction):
    """Generated wrapper for ASTAddConstraintActionProto"""

    def __init__(self, proto: 'ASTAddConstraintActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def constraint(self) -> Optional['AnyASTTableConstraintProto']:
        """Field constraint"""
        return self._proto.constraint

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTAddSubEntityAction(ASTAlterAction):
    """Generated wrapper for ASTAddSubEntityActionProto"""

    def __init__(self, proto: 'ASTAddSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['ASTIdentifierProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTAddToRestricteeListClause(ASTAlterAction):
    """Generated wrapper for ASTAddToRestricteeListClauseProto"""

    def __init__(self, proto: 'ASTAddToRestricteeListClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def restrictee_list(self) -> Optional['ASTGranteeListProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ASTAddTtlAction(ASTAlterAction):
    """Generated wrapper for ASTAddTtlActionProto"""

    def __init__(self, proto: 'ASTAddTtlActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTAliasedQueryExpression(ASTQueryExpression):
    """Generated wrapper for ASTAliasedQueryExpressionProto"""

    def __init__(self, proto: 'ASTAliasedQueryExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTAlterAllRowAccessPoliciesStatement(ASTStatement):
    """Generated wrapper for ASTAlterAllRowAccessPoliciesStatementProto"""

    def __init__(self, proto: 'ASTAlterAllRowAccessPoliciesStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def table_name_path(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name_path"""
        return self._proto.table_name_path

    @cached_property
    def alter_action(self) -> Optional['AnyASTAlterActionProto']:
        """Field alter_action"""
        return self._proto.alter_action



class ASTAlterColumnDropDefaultAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnDropDefaultActionProto"""

    def __init__(self, proto: 'ASTAlterColumnDropDefaultActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnDropGeneratedAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnDropGeneratedActionProto"""

    def __init__(self, proto: 'ASTAlterColumnDropGeneratedActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnDropNotNullAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnDropNotNullActionProto"""

    def __init__(self, proto: 'ASTAlterColumnDropNotNullActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnOptionsAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnOptionsActionProto"""

    def __init__(self, proto: 'ASTAlterColumnOptionsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnSetDefaultAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnSetDefaultActionProto"""

    def __init__(self, proto: 'ASTAlterColumnSetDefaultActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.default_expression

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnSetGeneratedAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnSetGeneratedActionProto"""

    def __init__(self, proto: 'ASTAlterColumnSetGeneratedActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.generated_column_info

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterColumnTypeAction(ASTAlterAction):
    """Generated wrapper for ASTAlterColumnTypeActionProto"""

    def __init__(self, proto: 'ASTAlterColumnTypeActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field schema"""
        return self._proto.schema

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterConstraintEnforcementAction(ASTAlterAction):
    """Generated wrapper for ASTAlterConstraintEnforcementActionProto"""

    def __init__(self, proto: 'ASTAlterConstraintEnforcementActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def is_enforced(self) -> Optional[bool]:
        """Field is_enforced"""
        return self._proto.is_enforced



class ASTAlterConstraintSetOptionsAction(ASTAlterAction):
    """Generated wrapper for ASTAlterConstraintSetOptionsActionProto"""

    def __init__(self, proto: 'ASTAlterConstraintSetOptionsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAlterSubEntityAction(ASTAlterAction):
    """Generated wrapper for ASTAlterSubEntityActionProto"""

    def __init__(self, proto: 'ASTAlterSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['ASTIdentifierProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def action(self) -> Optional['AnyASTAlterActionProto']:
        """Field action"""
        return self._proto.action

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTAnalyticFunctionCall(ASTExpression):
    """Generated wrapper for ASTAnalyticFunctionCallProto"""

    def __init__(self, proto: 'ASTAnalyticFunctionCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def function(self) -> Optional['ASTFunctionCallProto']:
        """Field function"""
        return self._proto.function

    @cached_property
    def window_spec(self) -> Optional['ASTWindowSpecificationProto']:
        """Field window_spec"""
        return self._proto.window_spec



class ASTAnalyzeStatement(ASTStatement):
    """Generated wrapper for ASTAnalyzeStatementProto"""

    def __init__(self, proto: 'ASTAnalyzeStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def table_and_column_info_list(self) -> Optional['ASTTableAndColumnInfoListProto']:
        """Field table_and_column_info_list"""
        return self._proto.table_and_column_info_list



class ASTAndExpr(ASTExpression):
    """Generated wrapper for ASTAndExprProto"""

    def __init__(self, proto: 'ASTAndExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def conjuncts(self) -> List['AnyASTExpressionProto']:
        """Field conjuncts"""
        return self._proto.conjuncts



class ASTArrayConstructor(ASTExpression):
    """Generated wrapper for ASTArrayConstructorProto"""

    def __init__(self, proto: 'ASTArrayConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def type(self) -> Optional['ASTArrayTypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def elements(self) -> List['AnyASTExpressionProto']:
        """Field elements"""
        return self._proto.elements



class ASTArrayType(ASTType):
    """Generated wrapper for ASTArrayTypeProto"""

    def __init__(self, proto: 'ASTArrayTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def element_type(self) -> Optional['AnyASTTypeProto']:
        """Field element_type"""
        return self._proto.element_type

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTAssertStatement(ASTStatement):
    """Generated wrapper for ASTAssertStatementProto"""

    def __init__(self, proto: 'ASTAssertStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def description(self) -> Optional['ASTStringLiteralProto']:
        """Field description"""
        return self._proto.description



class ASTBeginStatement(ASTStatement):
    """Generated wrapper for ASTBeginStatementProto"""

    def __init__(self, proto: 'ASTBeginStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def mode_list(self) -> Optional['ASTTransactionModeListProto']:
        """Field mode_list"""
        return self._proto.mode_list



class ASTBetweenExpression(ASTExpression):
    """Generated wrapper for ASTBetweenExpressionProto"""

    def __init__(self, proto: 'ASTBetweenExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def lhs(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def low(self) -> Optional['AnyASTExpressionProto']:
        """Field low"""
        return self._proto.low

    @cached_property
    def high(self) -> Optional['AnyASTExpressionProto']:
        """Field high"""
        return self._proto.high

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def between_location(self) -> Optional['ASTLocationProto']:
        """Field between_location"""
        return self._proto.between_location



class ASTBinaryExpression(ASTExpression):
    """Generated wrapper for ASTBinaryExpressionProto"""

    def __init__(self, proto: 'ASTBinaryExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def op(self) -> Optional[int]:
        """Field op"""
        return self._proto.op

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def lhs(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def rhs(self) -> Optional['AnyASTExpressionProto']:
        """Field rhs"""
        return self._proto.rhs



class ASTBitwiseShiftExpression(ASTExpression):
    """Generated wrapper for ASTBitwiseShiftExpressionProto"""

    def __init__(self, proto: 'ASTBitwiseShiftExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def lhs(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def rhs(self) -> Optional['AnyASTExpressionProto']:
        """Field rhs"""
        return self._proto.rhs

    @cached_property
    def is_left_shift(self) -> Optional[bool]:
        """Field is_left_shift"""
        return self._proto.is_left_shift

    @cached_property
    def operator_location(self) -> Optional['ASTLocationProto']:
        """Field operator_location"""
        return self._proto.operator_location



class ASTBoundedQuantifier(ASTQuantifier):
    """Generated wrapper for ASTBoundedQuantifierProto"""

    def __init__(self, proto: 'ASTBoundedQuantifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_reluctant(self) -> Optional[bool]:
        """Field is_reluctant"""
        return self._proto.parent.is_reluctant

    @cached_property
    def lower_bound(self) -> Optional['ASTQuantifierBoundProto']:
        """Field lower_bound"""
        return self._proto.lower_bound

    @cached_property
    def upper_bound(self) -> Optional['ASTQuantifierBoundProto']:
        """Field upper_bound"""
        return self._proto.upper_bound



class ASTBracedConstructorLhs(ASTExpression):
    """Generated wrapper for ASTBracedConstructorLhsProto"""

    def __init__(self, proto: 'ASTBracedConstructorLhsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def extended_path_expr(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field extended_path_expr"""
        return self._proto.extended_path_expr

    @cached_property
    def operation(self) -> Optional[int]:
        """Field operation"""
        return self._proto.operation



class ASTBracedConstructor(ASTExpression):
    """Generated wrapper for ASTBracedConstructorProto"""

    def __init__(self, proto: 'ASTBracedConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def fields(self) -> List['ASTBracedConstructorFieldProto']:
        """Field fields"""
        return self._proto.fields



class ASTBracedNewConstructor(ASTExpression):
    """Generated wrapper for ASTBracedNewConstructorProto"""

    def __init__(self, proto: 'ASTBracedNewConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def type_name(self) -> Optional['ASTSimpleTypeProto']:
        """Field type_name"""
        return self._proto.type_name

    @cached_property
    def braced_constructor(self) -> Optional['ASTBracedConstructorProto']:
        """Field braced_constructor"""
        return self._proto.braced_constructor



class ASTCallStatement(ASTStatement):
    """Generated wrapper for ASTCallStatementProto"""

    def __init__(self, proto: 'ASTCallStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def procedure_name(self) -> Optional['ASTPathExpressionProto']:
        """Field procedure_name"""
        return self._proto.procedure_name

    @cached_property
    def arguments(self) -> List['ASTTVFArgumentProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTCaseNoValueExpression(ASTExpression):
    """Generated wrapper for ASTCaseNoValueExpressionProto"""

    def __init__(self, proto: 'ASTCaseNoValueExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def arguments(self) -> List['AnyASTExpressionProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTCaseValueExpression(ASTExpression):
    """Generated wrapper for ASTCaseValueExpressionProto"""

    def __init__(self, proto: 'ASTCaseValueExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def arguments(self) -> List['AnyASTExpressionProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTCastExpression(ASTExpression):
    """Generated wrapper for ASTCastExpressionProto"""

    def __init__(self, proto: 'ASTCastExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def type(self) -> Optional['AnyASTTypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def format(self) -> Optional['ASTFormatClauseProto']:
        """Field format"""
        return self._proto.format

    @cached_property
    def is_safe_cast(self) -> Optional[bool]:
        """Field is_safe_cast"""
        return self._proto.is_safe_cast



class ASTCloneDataStatement(ASTStatement):
    """Generated wrapper for ASTCloneDataStatementProto"""

    def __init__(self, proto: 'ASTCloneDataStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def data_source_list(self) -> Optional['ASTCloneDataSourceListProto']:
        """Field data_source_list"""
        return self._proto.data_source_list



class ASTColumnDefinition(ASTTableElement):
    """Generated wrapper for ASTColumnDefinitionProto"""

    def __init__(self, proto: 'ASTColumnDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field schema"""
        return self._proto.schema



class ASTCommitStatement(ASTStatement):
    """Generated wrapper for ASTCommitStatementProto"""

    def __init__(self, proto: 'ASTCommitStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTConcatExpr(ASTExpression):
    """Generated wrapper for ASTConcatExprProto"""

    def __init__(self, proto: 'ASTConcatExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def operands(self) -> List['AnyASTExpressionProto']:
        """Field operands"""
        return self._proto.operands



class ASTCreateDatabaseStatement(ASTStatement):
    """Generated wrapper for ASTCreateDatabaseStatementProto"""

    def __init__(self, proto: 'ASTCreateDatabaseStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateLocalityGroupStatement(ASTStatement):
    """Generated wrapper for ASTCreateLocalityGroupStatementProto"""

    def __init__(self, proto: 'ASTCreateLocalityGroupStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTDateOrTimeLiteral(ASTExpression):
    """Generated wrapper for ASTDateOrTimeLiteralProto"""

    def __init__(self, proto: 'ASTDateOrTimeLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def string_literal(self) -> Optional['ASTStringLiteralProto']:
        """Field string_literal"""
        return self._proto.string_literal

    @cached_property
    def type_kind(self) -> Optional[int]:
        """Field type_kind"""
        return self._proto.type_kind



class ASTDdlStatement(ASTStatement):
    """Generated wrapper for ASTDdlStatementProto"""

    def __init__(self, proto: 'ASTDdlStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTDefaultLiteral(ASTExpression):
    """Generated wrapper for ASTDefaultLiteralProto"""

    def __init__(self, proto: 'ASTDefaultLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTDefineMacroStatement(ASTStatement):
    """Generated wrapper for ASTDefineMacroStatementProto"""

    def __init__(self, proto: 'ASTDefineMacroStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def body(self) -> Optional['ASTMacroBodyProto']:
        """Field body"""
        return self._proto.body



class ASTDefineTableStatement(ASTStatement):
    """Generated wrapper for ASTDefineTableStatementProto"""

    def __init__(self, proto: 'ASTDefineTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTDeleteStatement(ASTStatement):
    """Generated wrapper for ASTDeleteStatementProto"""

    def __init__(self, proto: 'ASTDeleteStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def offset(self) -> Optional['ASTWithOffsetProto']:
        """Field offset"""
        return self._proto.offset

    @cached_property
    def where(self) -> Optional['AnyASTExpressionProto']:
        """Field where"""
        return self._proto.where

    @cached_property
    def assert_rows_modified(self) -> Optional['ASTAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ASTReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint



class ASTDescribeStatement(ASTStatement):
    """Generated wrapper for ASTDescribeStatementProto"""

    def __init__(self, proto: 'ASTDescribeStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def optional_identifier(self) -> Optional['ASTIdentifierProto']:
        """Field optional_identifier"""
        return self._proto.optional_identifier

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def optional_from_name(self) -> Optional['ASTPathExpressionProto']:
        """Field optional_from_name"""
        return self._proto.optional_from_name



class ASTDotStar(ASTExpression):
    """Generated wrapper for ASTDotStarProto"""

    def __init__(self, proto: 'ASTDotStarProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr



class ASTDotStarWithModifiers(ASTExpression):
    """Generated wrapper for ASTDotStarWithModifiersProto"""

    def __init__(self, proto: 'ASTDotStarWithModifiersProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def modifiers(self) -> Optional['ASTStarModifiersProto']:
        """Field modifiers"""
        return self._proto.modifiers



class ASTDropAllRowAccessPoliciesStatement(ASTStatement):
    """Generated wrapper for ASTDropAllRowAccessPoliciesStatementProto"""

    def __init__(self, proto: 'ASTDropAllRowAccessPoliciesStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def has_access_keyword(self) -> Optional[bool]:
        """Field has_access_keyword"""
        return self._proto.has_access_keyword



class ASTDropColumnAction(ASTAlterAction):
    """Generated wrapper for ASTDropColumnActionProto"""

    def __init__(self, proto: 'ASTDropColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropConstraintAction(ASTAlterAction):
    """Generated wrapper for ASTDropConstraintActionProto"""

    def __init__(self, proto: 'ASTDropConstraintActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropPrimaryKeyAction(ASTAlterAction):
    """Generated wrapper for ASTDropPrimaryKeyActionProto"""

    def __init__(self, proto: 'ASTDropPrimaryKeyActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropSubEntityAction(ASTAlterAction):
    """Generated wrapper for ASTDropSubEntityActionProto"""

    def __init__(self, proto: 'ASTDropSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['ASTIdentifierProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropTtlAction(ASTAlterAction):
    """Generated wrapper for ASTDropTtlActionProto"""

    def __init__(self, proto: 'ASTDropTtlActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTElementTypeColumnSchema(ASTColumnSchema):
    """Generated wrapper for ASTElementTypeColumnSchemaProto"""

    def __init__(self, proto: 'ASTElementTypeColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def element_schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field element_schema"""
        return self._proto.element_schema



class ASTEmptyRowPattern(ASTRowPatternExpression):
    """Generated wrapper for ASTEmptyRowPatternProto"""

    def __init__(self, proto: 'ASTEmptyRowPatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTExecuteImmediateStatement(ASTStatement):
    """Generated wrapper for ASTExecuteImmediateStatementProto"""

    def __init__(self, proto: 'ASTExecuteImmediateStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def sql(self) -> Optional['AnyASTExpressionProto']:
        """Field sql"""
        return self._proto.sql

    @cached_property
    def into_clause(self) -> Optional['ASTExecuteIntoClauseProto']:
        """Field into_clause"""
        return self._proto.into_clause

    @cached_property
    def using_clause(self) -> Optional['ASTExecuteUsingClauseProto']:
        """Field using_clause"""
        return self._proto.using_clause



class ASTExplainStatement(ASTStatement):
    """Generated wrapper for ASTExplainStatementProto"""

    def __init__(self, proto: 'ASTExplainStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def statement(self) -> Optional['AnyASTStatementProto']:
        """Field statement"""
        return self._proto.statement



class ASTExportDataStatement(ASTStatement):
    """Generated wrapper for ASTExportDataStatementProto"""

    def __init__(self, proto: 'ASTExportDataStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query



class ASTExportMetadataStatement(ASTStatement):
    """Generated wrapper for ASTExportMetadataStatementProto"""

    def __init__(self, proto: 'ASTExportMetadataStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def schema_object_kind(self) -> Optional[int]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind

    @cached_property
    def name_path(self) -> Optional['ASTPathExpressionProto']:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTExportModelStatement(ASTStatement):
    """Generated wrapper for ASTExportModelStatementProto"""

    def __init__(self, proto: 'ASTExportModelStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def model_name_path(self) -> Optional['ASTPathExpressionProto']:
        """Field model_name_path"""
        return self._proto.model_name_path

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTExpressionSubquery(ASTExpression):
    """Generated wrapper for ASTExpressionSubqueryProto"""

    def __init__(self, proto: 'ASTExpressionSubqueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def modifier(self) -> Optional[int]:
        """Field modifier"""
        return self._proto.modifier



class ASTExpressionWithAlias(ASTExpression):
    """Generated wrapper for ASTExpressionWithAliasProto"""

    def __init__(self, proto: 'ASTExpressionWithAliasProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTExtractExpression(ASTExpression):
    """Generated wrapper for ASTExtractExpressionProto"""

    def __init__(self, proto: 'ASTExtractExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def lhs_expr(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs_expr"""
        return self._proto.lhs_expr

    @cached_property
    def rhs_expr(self) -> Optional['AnyASTExpressionProto']:
        """Field rhs_expr"""
        return self._proto.rhs_expr

    @cached_property
    def time_zone_expr(self) -> Optional['AnyASTExpressionProto']:
        """Field time_zone_expr"""
        return self._proto.time_zone_expr



class ASTFilterUsingClause(ASTAlterAction):
    """Generated wrapper for ASTFilterUsingClauseProto"""

    def __init__(self, proto: 'ASTFilterUsingClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def predicate(self) -> Optional['AnyASTExpressionProto']:
        """Field predicate"""
        return self._proto.predicate

    @cached_property
    def has_filter_keyword(self) -> Optional[bool]:
        """Field has_filter_keyword"""
        return self._proto.has_filter_keyword



class ASTFixedQuantifier(ASTQuantifier):
    """Generated wrapper for ASTFixedQuantifierProto"""

    def __init__(self, proto: 'ASTFixedQuantifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_reluctant(self) -> Optional[bool]:
        """Field is_reluctant"""
        return self._proto.parent.is_reluctant

    @cached_property
    def bound(self) -> Optional['AnyASTExpressionProto']:
        """Field bound"""
        return self._proto.bound



class ASTForeignKeyColumnAttribute(ASTColumnAttribute):
    """Generated wrapper for ASTForeignKeyColumnAttributeProto"""

    def __init__(self, proto: 'ASTForeignKeyColumnAttributeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def reference(self) -> Optional['ASTForeignKeyReferenceProto']:
        """Field reference"""
        return self._proto.reference



class ASTFromQuery(ASTQueryExpression):
    """Generated wrapper for ASTFromQueryProto"""

    def __init__(self, proto: 'ASTFromQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def from_clause(self) -> Optional['ASTFromClauseProto']:
        """Field from_clause"""
        return self._proto.from_clause



class ASTFunctionCall(ASTExpression):
    """Generated wrapper for ASTFunctionCallProto"""

    def __init__(self, proto: 'ASTFunctionCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def function(self) -> Optional['ASTPathExpressionProto']:
        """Field function"""
        return self._proto.function

    @cached_property
    def arguments(self) -> List['AnyASTExpressionProto']:
        """Field arguments"""
        return self._proto.arguments

    @cached_property
    def having_modifier(self) -> Optional['ASTHavingModifierProto']:
        """Field having_modifier"""
        return self._proto.having_modifier

    @cached_property
    def clamped_between_modifier(self) -> Optional['ASTClampedBetweenModifierProto']:
        """Field clamped_between_modifier"""
        return self._proto.clamped_between_modifier

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def limit_offset(self) -> Optional['ASTLimitOffsetProto']:
        """Field limit_offset"""
        return self._proto.limit_offset

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def null_handling_modifier(self) -> Optional[int]:
        """Field null_handling_modifier"""
        return self._proto.null_handling_modifier

    @cached_property
    def distinct(self) -> Optional[bool]:
        """Field distinct"""
        return self._proto.distinct

    @cached_property
    def is_current_date_time_without_parentheses(self) -> Optional[bool]:
        """Field is_current_date_time_without_parentheses"""
        return self._proto.is_current_date_time_without_parentheses

    @cached_property
    def with_report_modifier(self) -> Optional['ASTWithReportModifierProto']:
        """Field with_report_modifier"""
        return self._proto.with_report_modifier

    @cached_property
    def group_by(self) -> Optional['ASTGroupByProto']:
        """Field group_by"""
        return self._proto.group_by

    @cached_property
    def where_expr(self) -> Optional['ASTWhereClauseProto']:
        """Field where_expr"""
        return self._proto.where_expr

    @cached_property
    def having_expr(self) -> Optional['ASTHavingProto']:
        """Field having_expr"""
        return self._proto.having_expr

    @cached_property
    def is_chained_call(self) -> Optional[bool]:
        """Field is_chained_call"""
        return self._proto.is_chained_call



class ASTFunctionType(ASTType):
    """Generated wrapper for ASTFunctionTypeProto"""

    def __init__(self, proto: 'ASTFunctionTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def arg_list(self) -> Optional['ASTFunctionTypeArgListProto']:
        """Field arg_list"""
        return self._proto.arg_list

    @cached_property
    def return_type(self) -> Optional['AnyASTTypeProto']:
        """Field return_type"""
        return self._proto.return_type

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTGeneralizedPathExpression(ASTExpression):
    """Generated wrapper for ASTGeneralizedPathExpressionProto"""

    def __init__(self, proto: 'ASTGeneralizedPathExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTGqlCallBase(ASTGqlOperator):
    """Generated wrapper for ASTGqlCallBaseProto"""

    def __init__(self, proto: 'ASTGqlCallBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.optional

    @cached_property
    def is_partitioning(self) -> Optional[bool]:
        """Field is_partitioning"""
        return self._proto.is_partitioning

    @cached_property
    def name_capture_list(self) -> Optional['ASTIdentifierListProto']:
        """Field name_capture_list"""
        return self._proto.name_capture_list



class ASTGqlFilter(ASTGqlOperator):
    """Generated wrapper for ASTGqlFilterProto"""

    def __init__(self, proto: 'ASTGqlFilterProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['ASTWhereClauseProto']:
        """Field condition"""
        return self._proto.condition



class ASTGqlFor(ASTGqlOperator):
    """Generated wrapper for ASTGqlForProto"""

    def __init__(self, proto: 'ASTGqlForProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def with_offset(self) -> Optional['ASTWithOffsetProto']:
        """Field with_offset"""
        return self._proto.with_offset



class ASTGqlGraphPatternQuery(ASTQueryExpression):
    """Generated wrapper for ASTGqlGraphPatternQueryProto"""

    def __init__(self, proto: 'ASTGqlGraphPatternQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def graph_reference(self) -> Optional['ASTPathExpressionProto']:
        """Field graph_reference"""
        return self._proto.graph_reference

    @cached_property
    def graph_pattern(self) -> Optional['ASTGraphPatternProto']:
        """Field graph_pattern"""
        return self._proto.graph_pattern



class ASTGqlLet(ASTGqlOperator):
    """Generated wrapper for ASTGqlLetProto"""

    def __init__(self, proto: 'ASTGqlLetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def variable_definition_list(self) -> Optional['ASTGqlLetVariableDefinitionListProto']:
        """Field variable_definition_list"""
        return self._proto.variable_definition_list



class ASTGqlLinearOpsQuery(ASTQueryExpression):
    """Generated wrapper for ASTGqlLinearOpsQueryProto"""

    def __init__(self, proto: 'ASTGqlLinearOpsQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def graph_reference(self) -> Optional['ASTPathExpressionProto']:
        """Field graph_reference"""
        return self._proto.graph_reference

    @cached_property
    def linear_ops(self) -> Optional['ASTGqlOperatorListProto']:
        """Field linear_ops"""
        return self._proto.linear_ops



class ASTGqlMatch(ASTGqlOperator):
    """Generated wrapper for ASTGqlMatchProto"""

    def __init__(self, proto: 'ASTGqlMatchProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def graph_pattern(self) -> Optional['ASTGraphPatternProto']:
        """Field graph_pattern"""
        return self._proto.graph_pattern

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.optional

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint



class ASTGqlOperatorList(ASTGqlOperator):
    """Generated wrapper for ASTGqlOperatorListProto"""

    def __init__(self, proto: 'ASTGqlOperatorListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def operators(self) -> List['AnyASTGqlOperatorProto']:
        """Field operators"""
        return self._proto.operators



class ASTGqlOrderByAndPage(ASTGqlOperator):
    """Generated wrapper for ASTGqlOrderByAndPageProto"""

    def __init__(self, proto: 'ASTGqlOrderByAndPageProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def page(self) -> Optional['ASTGqlPageProto']:
        """Field page"""
        return self._proto.page



class ASTGqlQuery(ASTQueryExpression):
    """Generated wrapper for ASTGqlQueryProto"""

    def __init__(self, proto: 'ASTGqlQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def graph_table(self) -> Optional['ASTGraphTableQueryProto']:
        """Field graph_table"""
        return self._proto.graph_table



class ASTGqlReturn(ASTGqlOperator):
    """Generated wrapper for ASTGqlReturnProto"""

    def __init__(self, proto: 'ASTGqlReturnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select

    @cached_property
    def order_by_page(self) -> Optional['ASTGqlOrderByAndPageProto']:
        """Field order_by_page"""
        return self._proto.order_by_page



class ASTGqlSample(ASTGqlOperator):
    """Generated wrapper for ASTGqlSampleProto"""

    def __init__(self, proto: 'ASTGqlSampleProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def sample(self) -> Optional['ASTSampleClauseProto']:
        """Field sample"""
        return self._proto.sample



class ASTGqlSetOperation(ASTGqlOperator):
    """Generated wrapper for ASTGqlSetOperationProto"""

    def __init__(self, proto: 'ASTGqlSetOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def metadata(self) -> Optional['ASTSetOperationMetadataListProto']:
        """Field metadata"""
        return self._proto.metadata

    @cached_property
    def inputs(self) -> List['AnyASTGqlOperatorProto']:
        """Field inputs"""
        return self._proto.inputs



class ASTGqlWith(ASTGqlOperator):
    """Generated wrapper for ASTGqlWithProto"""

    def __init__(self, proto: 'ASTGqlWithProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select



class ASTGrantStatement(ASTStatement):
    """Generated wrapper for ASTGrantStatementProto"""

    def __init__(self, proto: 'ASTGrantStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def privileges(self) -> Optional['ASTPrivilegesProto']:
        """Field privileges"""
        return self._proto.privileges

    @cached_property
    def target_type_parts(self) -> List['ASTIdentifierProto']:
        """Field target_type_parts"""
        return self._proto.target_type_parts

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def grantee_list(self) -> Optional['ASTGranteeListProto']:
        """Field grantee_list"""
        return self._proto.grantee_list



class ASTGrantToClause(ASTAlterAction):
    """Generated wrapper for ASTGrantToClauseProto"""

    def __init__(self, proto: 'ASTGrantToClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def grantee_list(self) -> Optional['ASTGranteeListProto']:
        """Field grantee_list"""
        return self._proto.grantee_list

    @cached_property
    def has_grant_keyword_and_parens(self) -> Optional[bool]:
        """Field has_grant_keyword_and_parens"""
        return self._proto.has_grant_keyword_and_parens



class ASTGraphElementLabel(ASTGraphLabelExpression):
    """Generated wrapper for ASTGraphElementLabelProto"""

    def __init__(self, proto: 'ASTGraphElementLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTGraphElementPattern(ASTGraphPathBase):
    """Generated wrapper for ASTGraphElementPatternProto"""

    def __init__(self, proto: 'ASTGraphElementPatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.parent.quantifier

    @cached_property
    def filler(self) -> Optional['ASTGraphElementPatternFillerProto']:
        """Field filler"""
        return self._proto.filler



class ASTGraphIsLabeledPredicate(ASTExpression):
    """Generated wrapper for ASTGraphIsLabeledPredicateProto"""

    def __init__(self, proto: 'ASTGraphIsLabeledPredicateProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def operand(self) -> Optional['AnyASTExpressionProto']:
        """Field operand"""
        return self._proto.operand

    @cached_property
    def label_expression(self) -> Optional['AnyASTGraphLabelExpressionProto']:
        """Field label_expression"""
        return self._proto.label_expression



class ASTGraphLabelOperation(ASTGraphLabelExpression):
    """Generated wrapper for ASTGraphLabelOperationProto"""

    def __init__(self, proto: 'ASTGraphLabelOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def op_type(self) -> Optional[int]:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def inputs(self) -> List['AnyASTGraphLabelExpressionProto']:
        """Field inputs"""
        return self._proto.inputs



class ASTGraphPathPattern(ASTGraphPathBase):
    """Generated wrapper for ASTGraphPathPatternProto"""

    def __init__(self, proto: 'ASTGraphPathPatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.parent.quantifier

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause

    @cached_property
    def path_mode(self) -> Optional['ASTGraphPathModeProto']:
        """Field path_mode"""
        return self._proto.path_mode

    @cached_property
    def input_pattern_list(self) -> List['AnyASTGraphPathBaseProto']:
        """Field input_pattern_list"""
        return self._proto.input_pattern_list

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parenthesized

    @cached_property
    def search_prefix(self) -> Optional['ASTGraphPathSearchPrefixProto']:
        """Field search_prefix"""
        return self._proto.search_prefix

    @cached_property
    def path_name(self) -> Optional['ASTIdentifierProto']:
        """Field path_name"""
        return self._proto.path_name



class ASTGraphTableQuery(ASTTableExpression):
    """Generated wrapper for ASTGraphTableQueryProto"""

    def __init__(self, proto: 'ASTGraphTableQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def graph_reference(self) -> Optional['ASTPathExpressionProto']:
        """Field graph_reference"""
        return self._proto.graph_reference

    @cached_property
    def graph_op(self) -> Optional['AnyASTGqlOperatorProto']:
        """Field graph_op"""
        return self._proto.graph_op

    @cached_property
    def graph_table_shape(self) -> Optional['ASTSelectListProto']:
        """Field graph_table_shape"""
        return self._proto.graph_table_shape

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTGraphWildcardLabel(ASTGraphLabelExpression):
    """Generated wrapper for ASTGraphWildcardLabelProto"""

    def __init__(self, proto: 'ASTGraphWildcardLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTHiddenColumnAttribute(ASTColumnAttribute):
    """Generated wrapper for ASTHiddenColumnAttributeProto"""

    def __init__(self, proto: 'ASTHiddenColumnAttributeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTHintedStatement(ASTStatement):
    """Generated wrapper for ASTHintedStatementProto"""

    def __init__(self, proto: 'ASTHintedStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def statement(self) -> Optional['AnyASTStatementProto']:
        """Field statement"""
        return self._proto.statement



class ASTIdentifier(ASTExpression):
    """Generated wrapper for ASTIdentifierProto"""

    def __init__(self, proto: 'ASTIdentifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def id_string(self) -> Optional[str]:
        """Field id_string"""
        return self._proto.id_string

    @cached_property
    def is_quoted(self) -> Optional[bool]:
        """Field is_quoted"""
        return self._proto.is_quoted



class ASTImportStatement(ASTStatement):
    """Generated wrapper for ASTImportStatementProto"""

    def __init__(self, proto: 'ASTImportStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def string_value(self) -> Optional['ASTStringLiteralProto']:
        """Field string_value"""
        return self._proto.string_value

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def into_alias(self) -> Optional['ASTIntoAliasProto']:
        """Field into_alias"""
        return self._proto.into_alias

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def import_kind(self) -> Optional[int]:
        """Field import_kind"""
        return self._proto.import_kind



class ASTInExpression(ASTExpression):
    """Generated wrapper for ASTInExpressionProto"""

    def __init__(self, proto: 'ASTInExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def lhs(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def in_list(self) -> Optional['ASTInListProto']:
        """Field in_list"""
        return self._proto.in_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def unnest_expr(self) -> Optional['ASTUnnestExpressionProto']:
        """Field unnest_expr"""
        return self._proto.unnest_expr

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def in_location(self) -> Optional['ASTLocationProto']:
        """Field in_location"""
        return self._proto.in_location



class ASTInferredTypeColumnSchema(ASTColumnSchema):
    """Generated wrapper for ASTInferredTypeColumnSchemaProto"""

    def __init__(self, proto: 'ASTInferredTypeColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list



class ASTInputTableArgument(ASTExpression):
    """Generated wrapper for ASTInputTableArgumentProto"""

    def __init__(self, proto: 'ASTInputTableArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTInsertStatement(ASTStatement):
    """Generated wrapper for ASTInsertStatementProto"""

    def __init__(self, proto: 'ASTInsertStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def column_list(self) -> Optional['ASTColumnListProto']:
        """Field column_list"""
        return self._proto.column_list

    @cached_property
    def rows(self) -> Optional['ASTInsertValuesRowListProto']:
        """Field rows"""
        return self._proto.rows

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def assert_rows_modified(self) -> Optional['ASTAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ASTReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def deprecated_parse_progress(self) -> Optional[int]:
        """Field deprecated_parse_progress"""
        return self._proto.deprecated_parse_progress

    @cached_property
    def insert_mode(self) -> Optional[int]:
        """Field insert_mode"""
        return self._proto.insert_mode

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def on_conflict(self) -> Optional['ASTOnConflictClauseProto']:
        """Field on_conflict"""
        return self._proto.on_conflict



class ASTIntOrUnbounded(ASTExpression):
    """Generated wrapper for ASTIntOrUnboundedProto"""

    def __init__(self, proto: 'ASTIntOrUnboundedProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def bound(self) -> Optional['AnyASTExpressionProto']:
        """Field bound"""
        return self._proto.bound



class ASTIntervalExpr(ASTExpression):
    """Generated wrapper for ASTIntervalExprProto"""

    def __init__(self, proto: 'ASTIntervalExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def interval_value(self) -> Optional['AnyASTExpressionProto']:
        """Field interval_value"""
        return self._proto.interval_value

    @cached_property
    def date_part_name(self) -> Optional['ASTIdentifierProto']:
        """Field date_part_name"""
        return self._proto.date_part_name

    @cached_property
    def date_part_name_to(self) -> Optional['ASTIdentifierProto']:
        """Field date_part_name_to"""
        return self._proto.date_part_name_to



class ASTJoin(ASTTableExpression):
    """Generated wrapper for ASTJoinProto"""

    def __init__(self, proto: 'ASTJoinProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def lhs(self) -> Optional['AnyASTTableExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def rhs(self) -> Optional['AnyASTTableExpressionProto']:
        """Field rhs"""
        return self._proto.rhs

    @cached_property
    def on_clause(self) -> Optional['ASTOnClauseProto']:
        """Field on_clause"""
        return self._proto.on_clause

    @cached_property
    def using_clause(self) -> Optional['ASTUsingClauseProto']:
        """Field using_clause"""
        return self._proto.using_clause

    @cached_property
    def clause_list(self) -> Optional['ASTOnOrUsingClauseListProto']:
        """Field clause_list"""
        return self._proto.clause_list

    @cached_property
    def join_type(self) -> Optional[int]:
        """Field join_type"""
        return self._proto.join_type

    @cached_property
    def join_hint(self) -> Optional[int]:
        """Field join_hint"""
        return self._proto.join_hint

    @cached_property
    def natural(self) -> Optional[bool]:
        """Field natural"""
        return self._proto.natural

    @cached_property
    def unmatched_join_count(self) -> Optional[int]:
        """Field unmatched_join_count"""
        return self._proto.unmatched_join_count

    @cached_property
    def transformation_needed(self) -> Optional[bool]:
        """Field transformation_needed"""
        return self._proto.transformation_needed

    @cached_property
    def contains_comma_join(self) -> Optional[bool]:
        """Field contains_comma_join"""
        return self._proto.contains_comma_join

    @cached_property
    def join_location(self) -> Optional['ASTLocationProto']:
        """Field join_location"""
        return self._proto.join_location



class ASTLambda(ASTExpression):
    """Generated wrapper for ASTLambdaProto"""

    def __init__(self, proto: 'ASTLambdaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def argument_list(self) -> Optional['AnyASTExpressionProto']:
        """Field argument_list"""
        return self._proto.argument_list

    @cached_property
    def body(self) -> Optional['AnyASTExpressionProto']:
        """Field body"""
        return self._proto.body



class ASTLeaf(ASTExpression):
    """Generated wrapper for ASTLeafProto"""

    def __init__(self, proto: 'ASTLeafProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTLikeExpression(ASTExpression):
    """Generated wrapper for ASTLikeExpressionProto"""

    def __init__(self, proto: 'ASTLikeExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def lhs(self) -> Optional['AnyASTExpressionProto']:
        """Field lhs"""
        return self._proto.lhs

    @cached_property
    def op(self) -> Optional['ASTAnySomeAllOpProto']:
        """Field op"""
        return self._proto.op

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def in_list(self) -> Optional['ASTInListProto']:
        """Field in_list"""
        return self._proto.in_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def unnest_expr(self) -> Optional['ASTUnnestExpressionProto']:
        """Field unnest_expr"""
        return self._proto.unnest_expr

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def like_location(self) -> Optional['ASTLocationProto']:
        """Field like_location"""
        return self._proto.like_location



class ASTMapType(ASTType):
    """Generated wrapper for ASTMapTypeProto"""

    def __init__(self, proto: 'ASTMapTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def key_type(self) -> Optional['AnyASTTypeProto']:
        """Field key_type"""
        return self._proto.key_type

    @cached_property
    def value_type(self) -> Optional['AnyASTTypeProto']:
        """Field value_type"""
        return self._proto.value_type

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTMatchRecognizeClause(ASTPostfixTableOperator):
    """Generated wrapper for ASTMatchRecognizeClauseProto"""

    def __init__(self, proto: 'ASTMatchRecognizeClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def measures(self) -> Optional['ASTSelectListProto']:
        """Field measures"""
        return self._proto.measures

    @cached_property
    def after_match_skip_clause(self) -> Optional['ASTAfterMatchSkipClauseProto']:
        """Field after_match_skip_clause"""
        return self._proto.after_match_skip_clause

    @cached_property
    def pattern(self) -> Optional['AnyASTRowPatternExpressionProto']:
        """Field pattern"""
        return self._proto.pattern

    @cached_property
    def pattern_variable_definition_list(self) -> Optional['ASTSelectListProto']:
        """Field pattern_variable_definition_list"""
        return self._proto.pattern_variable_definition_list

    @cached_property
    def output_alias(self) -> Optional['ASTAliasProto']:
        """Field output_alias"""
        return self._proto.output_alias

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTMergeStatement(ASTStatement):
    """Generated wrapper for ASTMergeStatementProto"""

    def __init__(self, proto: 'ASTMergeStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def table_expression(self) -> Optional['AnyASTTableExpressionProto']:
        """Field table_expression"""
        return self._proto.table_expression

    @cached_property
    def merge_condition(self) -> Optional['AnyASTExpressionProto']:
        """Field merge_condition"""
        return self._proto.merge_condition

    @cached_property
    def when_clauses(self) -> Optional['ASTMergeWhenClauseListProto']:
        """Field when_clauses"""
        return self._proto.when_clauses



class ASTModuleStatement(ASTStatement):
    """Generated wrapper for ASTModuleStatementProto"""

    def __init__(self, proto: 'ASTModuleStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTNamedArgument(ASTExpression):
    """Generated wrapper for ASTNamedArgumentProto"""

    def __init__(self, proto: 'ASTNamedArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr



class ASTNewConstructor(ASTExpression):
    """Generated wrapper for ASTNewConstructorProto"""

    def __init__(self, proto: 'ASTNewConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def type_name(self) -> Optional['ASTSimpleTypeProto']:
        """Field type_name"""
        return self._proto.type_name

    @cached_property
    def arguments(self) -> List['ASTNewConstructorArgProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTNotNullColumnAttribute(ASTColumnAttribute):
    """Generated wrapper for ASTNotNullColumnAttributeProto"""

    def __init__(self, proto: 'ASTNotNullColumnAttributeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTOrExpr(ASTExpression):
    """Generated wrapper for ASTOrExprProto"""

    def __init__(self, proto: 'ASTOrExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def disjuncts(self) -> List['AnyASTExpressionProto']:
        """Field disjuncts"""
        return self._proto.disjuncts



class ASTParameterAssignment(ASTStatement):
    """Generated wrapper for ASTParameterAssignmentProto"""

    def __init__(self, proto: 'ASTParameterAssignmentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parameter(self) -> Optional['ASTParameterExprProto']:
        """Field parameter"""
        return self._proto.parameter

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTParameterExprBase(ASTExpression):
    """Generated wrapper for ASTParameterExprBaseProto"""

    def __init__(self, proto: 'ASTParameterExprBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized



class ASTParenthesizedJoin(ASTTableExpression):
    """Generated wrapper for ASTParenthesizedJoinProto"""

    def __init__(self, proto: 'ASTParenthesizedJoinProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def join(self) -> Optional['ASTJoinProto']:
        """Field join"""
        return self._proto.join



class ASTPipeAggregate(ASTPipeOperator):
    """Generated wrapper for ASTPipeAggregateProto"""

    def __init__(self, proto: 'ASTPipeAggregateProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select

    @cached_property
    def select_with(self) -> Optional['ASTSelectWithProto']:
        """Field select_with"""
        return self._proto.select_with



class ASTPipeAs(ASTPipeOperator):
    """Generated wrapper for ASTPipeAsProto"""

    def __init__(self, proto: 'ASTPipeAsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTPipeAssert(ASTPipeOperator):
    """Generated wrapper for ASTPipeAssertProto"""

    def __init__(self, proto: 'ASTPipeAssertProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def message_list(self) -> List['AnyASTExpressionProto']:
        """Field message_list"""
        return self._proto.message_list



class ASTPipeCall(ASTPipeOperator):
    """Generated wrapper for ASTPipeCallProto"""

    def __init__(self, proto: 'ASTPipeCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def tvf(self) -> Optional['ASTTVFProto']:
        """Field tvf"""
        return self._proto.tvf



class ASTPipeCreateTable(ASTPipeOperator):
    """Generated wrapper for ASTPipeCreateTableProto"""

    def __init__(self, proto: 'ASTPipeCreateTableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def create_table_statement(self) -> Optional['ASTCreateTableStatementProto']:
        """Field create_table_statement"""
        return self._proto.create_table_statement



class ASTPipeDescribe(ASTPipeOperator):
    """Generated wrapper for ASTPipeDescribeProto"""

    def __init__(self, proto: 'ASTPipeDescribeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTPipeDistinct(ASTPipeOperator):
    """Generated wrapper for ASTPipeDistinctProto"""

    def __init__(self, proto: 'ASTPipeDistinctProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTPipeDrop(ASTPipeOperator):
    """Generated wrapper for ASTPipeDropProto"""

    def __init__(self, proto: 'ASTPipeDropProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> Optional['ASTIdentifierListProto']:
        """Field column_list"""
        return self._proto.column_list



class ASTPipeExportData(ASTPipeOperator):
    """Generated wrapper for ASTPipeExportDataProto"""

    def __init__(self, proto: 'ASTPipeExportDataProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def export_data_statement(self) -> Optional['ASTExportDataStatementProto']:
        """Field export_data_statement"""
        return self._proto.export_data_statement



class ASTPipeExtend(ASTPipeOperator):
    """Generated wrapper for ASTPipeExtendProto"""

    def __init__(self, proto: 'ASTPipeExtendProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select



class ASTPipeFork(ASTPipeOperator):
    """Generated wrapper for ASTPipeForkProto"""

    def __init__(self, proto: 'ASTPipeForkProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def subpipeline_list(self) -> List['ASTSubpipelineProto']:
        """Field subpipeline_list"""
        return self._proto.subpipeline_list



class ASTPipeIfCase(ASTPipeOperator):
    """Generated wrapper for ASTPipeIfCaseProto"""

    def __init__(self, proto: 'ASTPipeIfCaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def subpipeline(self) -> Optional['ASTSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline



class ASTPipeIf(ASTPipeOperator):
    """Generated wrapper for ASTPipeIfProto"""

    def __init__(self, proto: 'ASTPipeIfProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def if_cases(self) -> List['ASTPipeIfCaseProto']:
        """Field if_cases"""
        return self._proto.if_cases

    @cached_property
    def else_subpipeline(self) -> Optional['ASTSubpipelineProto']:
        """Field else_subpipeline"""
        return self._proto.else_subpipeline



class ASTPipeInsert(ASTPipeOperator):
    """Generated wrapper for ASTPipeInsertProto"""

    def __init__(self, proto: 'ASTPipeInsertProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def insert_statement(self) -> Optional['ASTInsertStatementProto']:
        """Field insert_statement"""
        return self._proto.insert_statement



class ASTPipeJoinLhsPlaceholder(ASTTableExpression):
    """Generated wrapper for ASTPipeJoinLhsPlaceholderProto"""

    def __init__(self, proto: 'ASTPipeJoinLhsPlaceholderProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators



class ASTPipeJoin(ASTPipeOperator):
    """Generated wrapper for ASTPipeJoinProto"""

    def __init__(self, proto: 'ASTPipeJoinProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def join(self) -> Optional['ASTJoinProto']:
        """Field join"""
        return self._proto.join



class ASTPipeLimitOffset(ASTPipeOperator):
    """Generated wrapper for ASTPipeLimitOffsetProto"""

    def __init__(self, proto: 'ASTPipeLimitOffsetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def limit_offset(self) -> Optional['ASTLimitOffsetProto']:
        """Field limit_offset"""
        return self._proto.limit_offset



class ASTPipeLog(ASTPipeOperator):
    """Generated wrapper for ASTPipeLogProto"""

    def __init__(self, proto: 'ASTPipeLogProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def subpipeline(self) -> Optional['ASTSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline



class ASTPipeMatchRecognize(ASTPipeOperator):
    """Generated wrapper for ASTPipeMatchRecognizeProto"""

    def __init__(self, proto: 'ASTPipeMatchRecognizeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def match_recognize(self) -> Optional['ASTMatchRecognizeClauseProto']:
        """Field match_recognize"""
        return self._proto.match_recognize



class ASTPipeOrderBy(ASTPipeOperator):
    """Generated wrapper for ASTPipeOrderByProto"""

    def __init__(self, proto: 'ASTPipeOrderByProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by



class ASTPipePivot(ASTPipeOperator):
    """Generated wrapper for ASTPipePivotProto"""

    def __init__(self, proto: 'ASTPipePivotProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def pivot_clause(self) -> Optional['ASTPivotClauseProto']:
        """Field pivot_clause"""
        return self._proto.pivot_clause



class ASTPipeRecursiveUnion(ASTPipeOperator):
    """Generated wrapper for ASTPipeRecursiveUnionProto"""

    def __init__(self, proto: 'ASTPipeRecursiveUnionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def metadata(self) -> Optional['ASTSetOperationMetadataProto']:
        """Field metadata"""
        return self._proto.metadata

    @cached_property
    def recursion_depth_modifier(self) -> Optional['ASTRecursionDepthModifierProto']:
        """Field recursion_depth_modifier"""
        return self._proto.recursion_depth_modifier

    @cached_property
    def input_subpipeline(self) -> Optional['ASTSubpipelineProto']:
        """Field input_subpipeline"""
        return self._proto.input_subpipeline

    @cached_property
    def input_subquery(self) -> Optional['AnyASTQueryExpressionProto']:
        """Field input_subquery"""
        return self._proto.input_subquery

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias



class ASTPipeRenameItem(ASTPipeOperator):
    """Generated wrapper for ASTPipeRenameItemProto"""

    def __init__(self, proto: 'ASTPipeRenameItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def old_name(self) -> Optional['ASTIdentifierProto']:
        """Field old_name"""
        return self._proto.old_name

    @cached_property
    def new_name(self) -> Optional['ASTIdentifierProto']:
        """Field new_name"""
        return self._proto.new_name



class ASTPipeRename(ASTPipeOperator):
    """Generated wrapper for ASTPipeRenameProto"""

    def __init__(self, proto: 'ASTPipeRenameProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def rename_item_list(self) -> List['ASTPipeRenameItemProto']:
        """Field rename_item_list"""
        return self._proto.rename_item_list



class ASTPipeSelect(ASTPipeOperator):
    """Generated wrapper for ASTPipeSelectProto"""

    def __init__(self, proto: 'ASTPipeSelectProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select



class ASTPipeSetOperation(ASTPipeOperator):
    """Generated wrapper for ASTPipeSetOperationProto"""

    def __init__(self, proto: 'ASTPipeSetOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def metadata(self) -> Optional['ASTSetOperationMetadataProto']:
        """Field metadata"""
        return self._proto.metadata

    @cached_property
    def inputs(self) -> List['AnyASTQueryExpressionProto']:
        """Field inputs"""
        return self._proto.inputs



class ASTPipeSet(ASTPipeOperator):
    """Generated wrapper for ASTPipeSetProto"""

    def __init__(self, proto: 'ASTPipeSetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def set_item_list(self) -> List['ASTPipeSetItemProto']:
        """Field set_item_list"""
        return self._proto.set_item_list



class ASTPipeStaticDescribe(ASTPipeOperator):
    """Generated wrapper for ASTPipeStaticDescribeProto"""

    def __init__(self, proto: 'ASTPipeStaticDescribeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTPipeTablesample(ASTPipeOperator):
    """Generated wrapper for ASTPipeTablesampleProto"""

    def __init__(self, proto: 'ASTPipeTablesampleProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def sample(self) -> Optional['ASTSampleClauseProto']:
        """Field sample"""
        return self._proto.sample



class ASTPipeTee(ASTPipeOperator):
    """Generated wrapper for ASTPipeTeeProto"""

    def __init__(self, proto: 'ASTPipeTeeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def subpipeline_list(self) -> List['ASTSubpipelineProto']:
        """Field subpipeline_list"""
        return self._proto.subpipeline_list



class ASTPipeUnpivot(ASTPipeOperator):
    """Generated wrapper for ASTPipeUnpivotProto"""

    def __init__(self, proto: 'ASTPipeUnpivotProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def unpivot_clause(self) -> Optional['ASTUnpivotClauseProto']:
        """Field unpivot_clause"""
        return self._proto.unpivot_clause



class ASTPipeWhere(ASTPipeOperator):
    """Generated wrapper for ASTPipeWhereProto"""

    def __init__(self, proto: 'ASTPipeWhereProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def where(self) -> Optional['ASTWhereClauseProto']:
        """Field where"""
        return self._proto.where



class ASTPipeWindow(ASTPipeOperator):
    """Generated wrapper for ASTPipeWindowProto"""

    def __init__(self, proto: 'ASTPipeWindowProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def select(self) -> Optional['ASTSelectProto']:
        """Field select"""
        return self._proto.select



class ASTPipeWith(ASTPipeOperator):
    """Generated wrapper for ASTPipeWithProto"""

    def __init__(self, proto: 'ASTPipeWithProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def with_clause(self) -> Optional['ASTWithClauseProto']:
        """Field with_clause"""
        return self._proto.with_clause



class ASTPivotClause(ASTPostfixTableOperator):
    """Generated wrapper for ASTPivotClauseProto"""

    def __init__(self, proto: 'ASTPivotClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def pivot_expressions(self) -> Optional['ASTPivotExpressionListProto']:
        """Field pivot_expressions"""
        return self._proto.pivot_expressions

    @cached_property
    def for_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field for_expression"""
        return self._proto.for_expression

    @cached_property
    def pivot_values(self) -> Optional['ASTPivotValueListProto']:
        """Field pivot_values"""
        return self._proto.pivot_values

    @cached_property
    def output_alias(self) -> Optional['ASTAliasProto']:
        """Field output_alias"""
        return self._proto.output_alias



class ASTPrimaryKeyColumnAttribute(ASTColumnAttribute):
    """Generated wrapper for ASTPrimaryKeyColumnAttributeProto"""

    def __init__(self, proto: 'ASTPrimaryKeyColumnAttributeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def enforced(self) -> Optional[bool]:
        """Field enforced"""
        return self._proto.enforced



class ASTQuery(ASTQueryExpression):
    """Generated wrapper for ASTQueryProto"""

    def __init__(self, proto: 'ASTQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def with_clause(self) -> Optional['ASTWithClauseProto']:
        """Field with_clause"""
        return self._proto.with_clause

    @cached_property
    def query_expr(self) -> Optional['AnyASTQueryExpressionProto']:
        """Field query_expr"""
        return self._proto.query_expr

    @cached_property
    def order_by(self) -> Optional['ASTOrderByProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def limit_offset(self) -> Optional['ASTLimitOffsetProto']:
        """Field limit_offset"""
        return self._proto.limit_offset

    @cached_property
    def is_nested(self) -> Optional[bool]:
        """Field is_nested"""
        return self._proto.is_nested

    @cached_property
    def is_pivot_input(self) -> Optional[bool]:
        """Field is_pivot_input"""
        return self._proto.is_pivot_input

    @cached_property
    def pipe_operator_list(self) -> List['AnyASTPipeOperatorProto']:
        """Field pipe_operator_list"""
        return self._proto.pipe_operator_list

    @cached_property
    def lock_mode(self) -> Optional['ASTLockModeProto']:
        """Field lock_mode"""
        return self._proto.lock_mode



class ASTQueryStatement(ASTStatement):
    """Generated wrapper for ASTQueryStatementProto"""

    def __init__(self, proto: 'ASTQueryStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query



class ASTRangeLiteral(ASTExpression):
    """Generated wrapper for ASTRangeLiteralProto"""

    def __init__(self, proto: 'ASTRangeLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def type(self) -> Optional['ASTRangeTypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def range_value(self) -> Optional['ASTStringLiteralProto']:
        """Field range_value"""
        return self._proto.range_value



class ASTRangeType(ASTType):
    """Generated wrapper for ASTRangeTypeProto"""

    def __init__(self, proto: 'ASTRangeTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def element_type(self) -> Optional['AnyASTTypeProto']:
        """Field element_type"""
        return self._proto.element_type

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTRebuildAction(ASTAlterAction):
    """Generated wrapper for ASTRebuildActionProto"""

    def __init__(self, proto: 'ASTRebuildActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTRemoveFromRestricteeListClause(ASTAlterAction):
    """Generated wrapper for ASTRemoveFromRestricteeListClauseProto"""

    def __init__(self, proto: 'ASTRemoveFromRestricteeListClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def restrictee_list(self) -> Optional['ASTGranteeListProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ASTRenameColumnAction(ASTAlterAction):
    """Generated wrapper for ASTRenameColumnActionProto"""

    def __init__(self, proto: 'ASTRenameColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_name(self) -> Optional['ASTIdentifierProto']:
        """Field column_name"""
        return self._proto.column_name

    @cached_property
    def new_column_name(self) -> Optional['ASTIdentifierProto']:
        """Field new_column_name"""
        return self._proto.new_column_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTRenameStatement(ASTStatement):
    """Generated wrapper for ASTRenameStatementProto"""

    def __init__(self, proto: 'ASTRenameStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def old_name(self) -> Optional['ASTPathExpressionProto']:
        """Field old_name"""
        return self._proto.old_name

    @cached_property
    def new_name(self) -> Optional['ASTPathExpressionProto']:
        """Field new_name"""
        return self._proto.new_name



class ASTRenameToClause(ASTAlterAction):
    """Generated wrapper for ASTRenameToClauseProto"""

    def __init__(self, proto: 'ASTRenameToClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def new_name(self) -> Optional['ASTPathExpressionProto']:
        """Field new_name"""
        return self._proto.new_name



class ASTReplaceFieldsExpression(ASTExpression):
    """Generated wrapper for ASTReplaceFieldsExpressionProto"""

    def __init__(self, proto: 'ASTReplaceFieldsExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def arguments(self) -> List['ASTReplaceFieldsArgProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTReplaceTtlAction(ASTAlterAction):
    """Generated wrapper for ASTReplaceTtlActionProto"""

    def __init__(self, proto: 'ASTReplaceTtlActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTRestrictToClause(ASTAlterAction):
    """Generated wrapper for ASTRestrictToClauseProto"""

    def __init__(self, proto: 'ASTRestrictToClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def restrictee_list(self) -> Optional['ASTGranteeListProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ASTRevokeFromClause(ASTAlterAction):
    """Generated wrapper for ASTRevokeFromClauseProto"""

    def __init__(self, proto: 'ASTRevokeFromClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def revoke_from_list(self) -> Optional['ASTGranteeListProto']:
        """Field revoke_from_list"""
        return self._proto.revoke_from_list

    @cached_property
    def is_revoke_from_all(self) -> Optional[bool]:
        """Field is_revoke_from_all"""
        return self._proto.is_revoke_from_all



class ASTRevokeStatement(ASTStatement):
    """Generated wrapper for ASTRevokeStatementProto"""

    def __init__(self, proto: 'ASTRevokeStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def privileges(self) -> Optional['ASTPrivilegesProto']:
        """Field privileges"""
        return self._proto.privileges

    @cached_property
    def target_type_parts(self) -> List['ASTIdentifierProto']:
        """Field target_type_parts"""
        return self._proto.target_type_parts

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def grantee_list(self) -> Optional['ASTGranteeListProto']:
        """Field grantee_list"""
        return self._proto.grantee_list



class ASTRollbackStatement(ASTStatement):
    """Generated wrapper for ASTRollbackStatementProto"""

    def __init__(self, proto: 'ASTRollbackStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTRowPatternAnchor(ASTRowPatternExpression):
    """Generated wrapper for ASTRowPatternAnchorProto"""

    def __init__(self, proto: 'ASTRowPatternAnchorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def anchor(self) -> Optional[int]:
        """Field anchor"""
        return self._proto.anchor



class ASTRowPatternOperation(ASTRowPatternExpression):
    """Generated wrapper for ASTRowPatternOperationProto"""

    def __init__(self, proto: 'ASTRowPatternOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def op_type(self) -> Optional[int]:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def inputs(self) -> List['AnyASTRowPatternExpressionProto']:
        """Field inputs"""
        return self._proto.inputs



class ASTRowPatternQuantification(ASTRowPatternExpression):
    """Generated wrapper for ASTRowPatternQuantificationProto"""

    def __init__(self, proto: 'ASTRowPatternQuantificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def operand(self) -> Optional['AnyASTRowPatternExpressionProto']:
        """Field operand"""
        return self._proto.operand

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.quantifier



class ASTRowPatternVariable(ASTRowPatternExpression):
    """Generated wrapper for ASTRowPatternVariableProto"""

    def __init__(self, proto: 'ASTRowPatternVariableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTRunBatchStatement(ASTStatement):
    """Generated wrapper for ASTRunBatchStatementProto"""

    def __init__(self, proto: 'ASTRunBatchStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTRunStatement(ASTStatement):
    """Generated wrapper for ASTRunStatementProto"""

    def __init__(self, proto: 'ASTRunStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path_expression(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path_expression"""
        return self._proto.target_path_expression

    @cached_property
    def target_string_literal(self) -> Optional['ASTStringLiteralProto']:
        """Field target_string_literal"""
        return self._proto.target_string_literal

    @cached_property
    def arguments(self) -> List['ASTNamedArgumentProto']:
        """Field arguments"""
        return self._proto.arguments



class ASTSampleClause(ASTPostfixTableOperator):
    """Generated wrapper for ASTSampleClauseProto"""

    def __init__(self, proto: 'ASTSampleClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def sample_method(self) -> Optional['ASTIdentifierProto']:
        """Field sample_method"""
        return self._proto.sample_method

    @cached_property
    def sample_size(self) -> Optional['ASTSampleSizeProto']:
        """Field sample_size"""
        return self._proto.sample_size

    @cached_property
    def sample_suffix(self) -> Optional['ASTSampleSuffixProto']:
        """Field sample_suffix"""
        return self._proto.sample_suffix



class ASTScriptStatement(ASTStatement):
    """Generated wrapper for ASTScriptStatementProto"""

    def __init__(self, proto: 'ASTScriptStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTSelect(ASTQueryExpression):
    """Generated wrapper for ASTSelectProto"""

    def __init__(self, proto: 'ASTSelectProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def select_with(self) -> Optional['ASTSelectWithProto']:
        """Field select_with"""
        return self._proto.select_with

    @cached_property
    def distinct(self) -> Optional[bool]:
        """Field distinct"""
        return self._proto.distinct

    @cached_property
    def select_as(self) -> Optional['ASTSelectAsProto']:
        """Field select_as"""
        return self._proto.select_as

    @cached_property
    def select_list(self) -> Optional['ASTSelectListProto']:
        """Field select_list"""
        return self._proto.select_list

    @cached_property
    def from_clause(self) -> Optional['ASTFromClauseProto']:
        """Field from_clause"""
        return self._proto.from_clause

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause

    @cached_property
    def group_by(self) -> Optional['ASTGroupByProto']:
        """Field group_by"""
        return self._proto.group_by

    @cached_property
    def having(self) -> Optional['ASTHavingProto']:
        """Field having"""
        return self._proto.having

    @cached_property
    def qualify(self) -> Optional['ASTQualifyProto']:
        """Field qualify"""
        return self._proto.qualify

    @cached_property
    def window_clause(self) -> Optional['ASTWindowClauseProto']:
        """Field window_clause"""
        return self._proto.window_clause



class ASTSequenceArg(ASTExpression):
    """Generated wrapper for ASTSequenceArgProto"""

    def __init__(self, proto: 'ASTSequenceArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def sequence_path(self) -> Optional['ASTPathExpressionProto']:
        """Field sequence_path"""
        return self._proto.sequence_path



class ASTSetAsAction(ASTAlterAction):
    """Generated wrapper for ASTSetAsActionProto"""

    def __init__(self, proto: 'ASTSetAsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def json_body(self) -> Optional['ASTJSONLiteralProto']:
        """Field json_body"""
        return self._proto.json_body

    @cached_property
    def text_body(self) -> Optional['ASTStringLiteralProto']:
        """Field text_body"""
        return self._proto.text_body



class ASTSetCollateClause(ASTAlterAction):
    """Generated wrapper for ASTSetCollateClauseProto"""

    def __init__(self, proto: 'ASTSetCollateClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTSetOperation(ASTQueryExpression):
    """Generated wrapper for ASTSetOperationProto"""

    def __init__(self, proto: 'ASTSetOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def metadata(self) -> Optional['ASTSetOperationMetadataListProto']:
        """Field metadata"""
        return self._proto.metadata

    @cached_property
    def inputs(self) -> List['AnyASTQueryExpressionProto']:
        """Field inputs"""
        return self._proto.inputs



class ASTSetOptionsAction(ASTAlterAction):
    """Generated wrapper for ASTSetOptionsActionProto"""

    def __init__(self, proto: 'ASTSetOptionsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTSetTransactionStatement(ASTStatement):
    """Generated wrapper for ASTSetTransactionStatementProto"""

    def __init__(self, proto: 'ASTSetTransactionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def mode_list(self) -> Optional['ASTTransactionModeListProto']:
        """Field mode_list"""
        return self._proto.mode_list



class ASTShowStatement(ASTStatement):
    """Generated wrapper for ASTShowStatementProto"""

    def __init__(self, proto: 'ASTShowStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def identifier(self) -> Optional['ASTIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def optional_name(self) -> Optional['ASTPathExpressionProto']:
        """Field optional_name"""
        return self._proto.optional_name

    @cached_property
    def optional_like_string(self) -> Optional['ASTStringLiteralProto']:
        """Field optional_like_string"""
        return self._proto.optional_like_string



class ASTSimpleColumnSchema(ASTColumnSchema):
    """Generated wrapper for ASTSimpleColumnSchemaProto"""

    def __init__(self, proto: 'ASTSimpleColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def type_name(self) -> Optional['ASTPathExpressionProto']:
        """Field type_name"""
        return self._proto.type_name



class ASTSimpleType(ASTType):
    """Generated wrapper for ASTSimpleTypeProto"""

    def __init__(self, proto: 'ASTSimpleTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type_name(self) -> Optional['ASTPathExpressionProto']:
        """Field type_name"""
        return self._proto.type_name

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTSpannerAlterColumnAction(ASTAlterAction):
    """Generated wrapper for ASTSpannerAlterColumnActionProto"""

    def __init__(self, proto: 'ASTSpannerAlterColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_definition(self) -> Optional['ASTColumnDefinitionProto']:
        """Field column_definition"""
        return self._proto.column_definition



class ASTSpannerSetOnDeleteAction(ASTAlterAction):
    """Generated wrapper for ASTSpannerSetOnDeleteActionProto"""

    def __init__(self, proto: 'ASTSpannerSetOnDeleteActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def action(self) -> Optional[int]:
        """Field action"""
        return self._proto.action



class ASTStarWithModifiers(ASTExpression):
    """Generated wrapper for ASTStarWithModifiersProto"""

    def __init__(self, proto: 'ASTStarWithModifiersProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def modifiers(self) -> Optional['ASTStarModifiersProto']:
        """Field modifiers"""
        return self._proto.modifiers



class ASTStartBatchStatement(ASTStatement):
    """Generated wrapper for ASTStartBatchStatementProto"""

    def __init__(self, proto: 'ASTStartBatchStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def batch_type(self) -> Optional['ASTIdentifierProto']:
        """Field batch_type"""
        return self._proto.batch_type



class ASTStatementWithPipeOperators(ASTStatement):
    """Generated wrapper for ASTStatementWithPipeOperatorsProto"""

    def __init__(self, proto: 'ASTStatementWithPipeOperatorsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def statement(self) -> Optional['AnyASTStatementProto']:
        """Field statement"""
        return self._proto.statement

    @cached_property
    def pipe_operator_suffix(self) -> Optional['ASTSubpipelineStatementProto']:
        """Field pipe_operator_suffix"""
        return self._proto.pipe_operator_suffix



class ASTStructBracedConstructor(ASTExpression):
    """Generated wrapper for ASTStructBracedConstructorProto"""

    def __init__(self, proto: 'ASTStructBracedConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def type_name(self) -> Optional['AnyASTTypeProto']:
        """Field type_name"""
        return self._proto.type_name

    @cached_property
    def braced_constructor(self) -> Optional['ASTBracedConstructorProto']:
        """Field braced_constructor"""
        return self._proto.braced_constructor



class ASTStructColumnSchema(ASTColumnSchema):
    """Generated wrapper for ASTStructColumnSchemaProto"""

    def __init__(self, proto: 'ASTStructColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def struct_fields(self) -> List['ASTStructColumnFieldProto']:
        """Field struct_fields"""
        return self._proto.struct_fields



class ASTStructConstructorWithKeyword(ASTExpression):
    """Generated wrapper for ASTStructConstructorWithKeywordProto"""

    def __init__(self, proto: 'ASTStructConstructorWithKeywordProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def struct_type(self) -> Optional['ASTStructTypeProto']:
        """Field struct_type"""
        return self._proto.struct_type

    @cached_property
    def fields(self) -> List['ASTStructConstructorArgProto']:
        """Field fields"""
        return self._proto.fields



class ASTStructConstructorWithParens(ASTExpression):
    """Generated wrapper for ASTStructConstructorWithParensProto"""

    def __init__(self, proto: 'ASTStructConstructorWithParensProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def field_expressions(self) -> List['AnyASTExpressionProto']:
        """Field field_expressions"""
        return self._proto.field_expressions



class ASTStructType(ASTType):
    """Generated wrapper for ASTStructTypeProto"""

    def __init__(self, proto: 'ASTStructTypeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def struct_fields(self) -> List['ASTStructFieldProto']:
        """Field struct_fields"""
        return self._proto.struct_fields

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.type_parameters

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTSubpipelineStatement(ASTStatement):
    """Generated wrapper for ASTSubpipelineStatementProto"""

    def __init__(self, proto: 'ASTSubpipelineStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def subpipeline(self) -> Optional['ASTSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline



class ASTSymbolQuantifier(ASTQuantifier):
    """Generated wrapper for ASTSymbolQuantifierProto"""

    def __init__(self, proto: 'ASTSymbolQuantifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def is_reluctant(self) -> Optional[bool]:
        """Field is_reluctant"""
        return self._proto.parent.is_reluctant

    @cached_property
    def symbol(self) -> Optional[int]:
        """Field symbol"""
        return self._proto.symbol



class ASTSystemVariableAssignment(ASTStatement):
    """Generated wrapper for ASTSystemVariableAssignmentProto"""

    def __init__(self, proto: 'ASTSystemVariableAssignmentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def system_variable(self) -> Optional['ASTSystemVariableExprProto']:
        """Field system_variable"""
        return self._proto.system_variable

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTTVF(ASTTableExpression):
    """Generated wrapper for ASTTVFProto"""

    def __init__(self, proto: 'ASTTVFProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def argument_entries(self) -> List['ASTTVFArgumentProto']:
        """Field argument_entries"""
        return self._proto.argument_entries

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def is_lateral(self) -> Optional[bool]:
        """Field is_lateral"""
        return self._proto.is_lateral



class ASTTableClause(ASTQueryExpression):
    """Generated wrapper for ASTTableClauseProto"""

    def __init__(self, proto: 'ASTTableClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def table_path(self) -> Optional['ASTPathExpressionProto']:
        """Field table_path"""
        return self._proto.table_path

    @cached_property
    def tvf(self) -> Optional['ASTTVFProto']:
        """Field tvf"""
        return self._proto.tvf

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause



class ASTTableConstraint(ASTTableElement):
    """Generated wrapper for ASTTableConstraintProto"""

    def __init__(self, proto: 'ASTTableConstraintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ASTTableDataSource(ASTTableExpression):
    """Generated wrapper for ASTTableDataSourceProto"""

    def __init__(self, proto: 'ASTTableDataSourceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def path_expr(self) -> Optional['ASTPathExpressionProto']:
        """Field path_expr"""
        return self._proto.path_expr

    @cached_property
    def for_system_time(self) -> Optional['ASTForSystemTimeProto']:
        """Field for_system_time"""
        return self._proto.for_system_time

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.where_clause



class ASTTablePathExpression(ASTTableExpression):
    """Generated wrapper for ASTTablePathExpressionProto"""

    def __init__(self, proto: 'ASTTablePathExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def path_expr(self) -> Optional['ASTPathExpressionProto']:
        """Field path_expr"""
        return self._proto.path_expr

    @cached_property
    def unnest_expr(self) -> Optional['ASTUnnestExpressionProto']:
        """Field unnest_expr"""
        return self._proto.unnest_expr

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def with_offset(self) -> Optional['ASTWithOffsetProto']:
        """Field with_offset"""
        return self._proto.with_offset

    @cached_property
    def for_system_time(self) -> Optional['ASTForSystemTimeProto']:
        """Field for_system_time"""
        return self._proto.for_system_time



class ASTTableSubquery(ASTTableExpression):
    """Generated wrapper for ASTTableSubqueryProto"""

    def __init__(self, proto: 'ASTTableSubqueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.postfix_operators

    @cached_property
    def subquery(self) -> Optional['ASTQueryProto']:
        """Field subquery"""
        return self._proto.subquery

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def is_lateral(self) -> Optional[bool]:
        """Field is_lateral"""
        return self._proto.is_lateral



class ASTTransactionIsolationLevel(ASTTransactionMode):
    """Generated wrapper for ASTTransactionIsolationLevelProto"""

    def __init__(self, proto: 'ASTTransactionIsolationLevelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def identifier1(self) -> Optional['ASTIdentifierProto']:
        """Field identifier1"""
        return self._proto.identifier1

    @cached_property
    def identifier2(self) -> Optional['ASTIdentifierProto']:
        """Field identifier2"""
        return self._proto.identifier2



class ASTTransactionReadWriteMode(ASTTransactionMode):
    """Generated wrapper for ASTTransactionReadWriteModeProto"""

    def __init__(self, proto: 'ASTTransactionReadWriteModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def mode(self) -> Optional[int]:
        """Field mode"""
        return self._proto.mode



class ASTTruncateStatement(ASTStatement):
    """Generated wrapper for ASTTruncateStatementProto"""

    def __init__(self, proto: 'ASTTruncateStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def where(self) -> Optional['AnyASTExpressionProto']:
        """Field where"""
        return self._proto.where



class ASTUnaryExpression(ASTExpression):
    """Generated wrapper for ASTUnaryExpressionProto"""

    def __init__(self, proto: 'ASTUnaryExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def operand(self) -> Optional['AnyASTExpressionProto']:
        """Field operand"""
        return self._proto.operand

    @cached_property
    def op(self) -> Optional[int]:
        """Field op"""
        return self._proto.op



class ASTUnpivotClause(ASTPostfixTableOperator):
    """Generated wrapper for ASTUnpivotClauseProto"""

    def __init__(self, proto: 'ASTUnpivotClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def unpivot_output_value_columns(self) -> Optional['ASTPathExpressionListProto']:
        """Field unpivot_output_value_columns"""
        return self._proto.unpivot_output_value_columns

    @cached_property
    def unpivot_output_name_column(self) -> Optional['ASTPathExpressionProto']:
        """Field unpivot_output_name_column"""
        return self._proto.unpivot_output_name_column

    @cached_property
    def unpivot_in_items(self) -> Optional['ASTUnpivotInItemListProto']:
        """Field unpivot_in_items"""
        return self._proto.unpivot_in_items

    @cached_property
    def output_alias(self) -> Optional['ASTAliasProto']:
        """Field output_alias"""
        return self._proto.output_alias

    @cached_property
    def null_filter(self) -> Optional[int]:
        """Field null_filter"""
        return self._proto.null_filter



class ASTUpdateConstructor(ASTExpression):
    """Generated wrapper for ASTUpdateConstructorProto"""

    def __init__(self, proto: 'ASTUpdateConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def function(self) -> Optional['ASTFunctionCallProto']:
        """Field function"""
        return self._proto.function

    @cached_property
    def braced_constructor(self) -> Optional['ASTBracedConstructorProto']:
        """Field braced_constructor"""
        return self._proto.braced_constructor



class ASTUpdateStatement(ASTStatement):
    """Generated wrapper for ASTUpdateStatementProto"""

    def __init__(self, proto: 'ASTUpdateStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target_path(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def alias(self) -> Optional['ASTAliasProto']:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def offset(self) -> Optional['ASTWithOffsetProto']:
        """Field offset"""
        return self._proto.offset

    @cached_property
    def update_item_list(self) -> Optional['ASTUpdateItemListProto']:
        """Field update_item_list"""
        return self._proto.update_item_list

    @cached_property
    def from_clause(self) -> Optional['ASTFromClauseProto']:
        """Field from_clause"""
        return self._proto.from_clause

    @cached_property
    def where(self) -> Optional['AnyASTExpressionProto']:
        """Field where"""
        return self._proto.where

    @cached_property
    def assert_rows_modified(self) -> Optional['ASTAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ASTReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def hint(self) -> Optional['ASTHintProto']:
        """Field hint"""
        return self._proto.hint



class ASTWithExpression(ASTExpression):
    """Generated wrapper for ASTWithExpressionProto"""

    def __init__(self, proto: 'ASTWithExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parenthesized

    @cached_property
    def variables(self) -> Optional['ASTSelectListProto']:
        """Field variables"""
        return self._proto.variables

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ResolvedAbortBatchStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAbortBatchStmtProto"""

    def __init__(self, proto: 'ResolvedAbortBatchStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list



class ResolvedAggregateHavingModifier(ResolvedArgument):
    """Generated wrapper for ResolvedAggregateHavingModifierProto"""

    def __init__(self, proto: 'ResolvedAggregateHavingModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def kind(self) -> Optional[int]:
        """Field kind"""
        return self._proto.kind

    @cached_property
    def having_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field having_expr"""
        return self._proto.having_expr



class ResolvedAggregateScanBase(ResolvedScan):
    """Generated wrapper for ResolvedAggregateScanBaseProto"""

    def __init__(self, proto: 'ResolvedAggregateScanBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.group_by_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.collation_list

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.aggregate_list

    @cached_property
    def grouping_set_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field grouping_set_list"""
        return self._proto.grouping_set_list

    @cached_property
    def rollup_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field rollup_column_list"""
        return self._proto.rollup_column_list

    @cached_property
    def grouping_call_list(self) -> List['ResolvedGroupingCallProto']:
        """Field grouping_call_list"""
        return self._proto.grouping_call_list



class ResolvedAlterAction(ResolvedArgument):
    """Generated wrapper for ResolvedAlterActionProto"""

    def __init__(self, proto: 'ResolvedAlterActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedAlterObjectStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAlterObjectStmtProto"""

    def __init__(self, proto: 'ResolvedAlterObjectStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ResolvedAlterTableSetOptionsStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAlterTableSetOptionsStmtProto"""

    def __init__(self, proto: 'ResolvedAlterTableSetOptionsStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ResolvedAnalyticFunctionGroup(ResolvedArgument):
    """Generated wrapper for ResolvedAnalyticFunctionGroupProto"""

    def __init__(self, proto: 'ResolvedAnalyticFunctionGroupProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def partition_by(self) -> Optional['ResolvedWindowPartitioningProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def order_by(self) -> Optional['ResolvedWindowOrderingProto']:
        """Field order_by"""
        return self._proto.order_by

    @cached_property
    def analytic_function_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field analytic_function_list"""
        return self._proto.analytic_function_list



class ResolvedAnalyticScan(ResolvedScan):
    """Generated wrapper for ResolvedAnalyticScanProto"""

    def __init__(self, proto: 'ResolvedAnalyticScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def function_group_list(self) -> List['ResolvedAnalyticFunctionGroupProto']:
        """Field function_group_list"""
        return self._proto.function_group_list



class ResolvedAnalyzeStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAnalyzeStmtProto"""

    def __init__(self, proto: 'ResolvedAnalyzeStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def table_and_column_index_list(self) -> List['ResolvedTableAndColumnInfoProto']:
        """Field table_and_column_index_list"""
        return self._proto.table_and_column_index_list



class ResolvedArgumentDef(ResolvedArgument):
    """Generated wrapper for ResolvedArgumentDefProto"""

    def __init__(self, proto: 'ResolvedArgumentDefProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def argument_kind(self) -> Optional[int]:
        """Field argument_kind"""
        return self._proto.argument_kind



class ResolvedArgumentList(ResolvedArgument):
    """Generated wrapper for ResolvedArgumentListProto"""

    def __init__(self, proto: 'ResolvedArgumentListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def arg_list(self) -> List['ResolvedArgumentDefProto']:
        """Field arg_list"""
        return self._proto.arg_list



class ResolvedArgumentRef(ResolvedExpr):
    """Generated wrapper for ResolvedArgumentRefProto"""

    def __init__(self, proto: 'ResolvedArgumentRefProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def argument_kind(self) -> Optional[int]:
        """Field argument_kind"""
        return self._proto.argument_kind



class ResolvedArrayAggregate(ResolvedExpr):
    """Generated wrapper for ResolvedArrayAggregateProto"""

    def __init__(self, proto: 'ResolvedArrayAggregateProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def array(self) -> Optional['AnyResolvedExprProto']:
        """Field array"""
        return self._proto.array

    @cached_property
    def element_column(self) -> Optional['ResolvedColumnProto']:
        """Field element_column"""
        return self._proto.element_column

    @cached_property
    def pre_aggregate_computed_column_list(self) -> List['ResolvedComputedColumnProto']:
        """Field pre_aggregate_computed_column_list"""
        return self._proto.pre_aggregate_computed_column_list

    @cached_property
    def aggregate(self) -> Optional['ResolvedAggregateFunctionCallProto']:
        """Field aggregate"""
        return self._proto.aggregate



class ResolvedArrayScan(ResolvedScan):
    """Generated wrapper for ResolvedArrayScanProto"""

    def __init__(self, proto: 'ResolvedArrayScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def array_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field array_expr_list"""
        return self._proto.array_expr_list

    @cached_property
    def element_column_list(self) -> List['ResolvedColumnProto']:
        """Field element_column_list"""
        return self._proto.element_column_list

    @cached_property
    def array_offset_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field array_offset_column"""
        return self._proto.array_offset_column

    @cached_property
    def join_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field join_expr"""
        return self._proto.join_expr

    @cached_property
    def is_outer(self) -> Optional[bool]:
        """Field is_outer"""
        return self._proto.is_outer

    @cached_property
    def array_zip_mode(self) -> Optional['AnyResolvedExprProto']:
        """Field array_zip_mode"""
        return self._proto.array_zip_mode



class ResolvedAssertRowsModified(ResolvedArgument):
    """Generated wrapper for ResolvedAssertRowsModifiedProto"""

    def __init__(self, proto: 'ResolvedAssertRowsModifiedProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def rows(self) -> Optional['AnyResolvedExprProto']:
        """Field rows"""
        return self._proto.rows



class ResolvedAssertScan(ResolvedScan):
    """Generated wrapper for ResolvedAssertScanProto"""

    def __init__(self, proto: 'ResolvedAssertScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def condition(self) -> Optional['AnyResolvedExprProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def message(self) -> Optional['AnyResolvedExprProto']:
        """Field message"""
        return self._proto.message



class ResolvedAssertStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAssertStmtProto"""

    def __init__(self, proto: 'ResolvedAssertStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def description(self) -> Optional[str]:
        """Field description"""
        return self._proto.description



class ResolvedAssignmentStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAssignmentStmtProto"""

    def __init__(self, proto: 'ResolvedAssignmentStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def target(self) -> Optional['AnyResolvedExprProto']:
        """Field target"""
        return self._proto.target

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedAuxLoadDataPartitionFilter(ResolvedArgument):
    """Generated wrapper for ResolvedAuxLoadDataPartitionFilterProto"""

    def __init__(self, proto: 'ResolvedAuxLoadDataPartitionFilterProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def filter(self) -> Optional['AnyResolvedExprProto']:
        """Field filter"""
        return self._proto.filter

    @cached_property
    def is_overwrite(self) -> Optional[bool]:
        """Field is_overwrite"""
        return self._proto.is_overwrite



class ResolvedAuxLoadDataStmt(ResolvedStatement):
    """Generated wrapper for ResolvedAuxLoadDataStmtProto"""

    def __init__(self, proto: 'ResolvedAuxLoadDataStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def insertion_mode(self) -> Optional[int]:
        """Field insertion_mode"""
        return self._proto.insertion_mode

    @cached_property
    def is_temp_table(self) -> Optional[bool]:
        """Field is_temp_table"""
        return self._proto.is_temp_table

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def partition_filter(self) -> Optional['ResolvedAuxLoadDataPartitionFilterProto']:
        """Field partition_filter"""
        return self._proto.partition_filter

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.column_definition_list

    @cached_property
    def pseudo_column_list(self) -> List['ResolvedColumnProto']:
        """Field pseudo_column_list"""
        return self._proto.pseudo_column_list

    @cached_property
    def primary_key(self) -> Optional['ResolvedPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.primary_key

    @cached_property
    def foreign_key_list(self) -> List['ResolvedForeignKeyProto']:
        """Field foreign_key_list"""
        return self._proto.foreign_key_list

    @cached_property
    def check_constraint_list(self) -> List['ResolvedCheckConstraintProto']:
        """Field check_constraint_list"""
        return self._proto.check_constraint_list

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def cluster_by_list(self) -> List['AnyResolvedExprProto']:
        """Field cluster_by_list"""
        return self._proto.cluster_by_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def with_partition_columns(self) -> Optional['ResolvedWithPartitionColumnsProto']:
        """Field with_partition_columns"""
        return self._proto.with_partition_columns

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def from_files_option_list(self) -> List['ResolvedOptionProto']:
        """Field from_files_option_list"""
        return self._proto.from_files_option_list



class ResolvedBarrierScan(ResolvedScan):
    """Generated wrapper for ResolvedBarrierScanProto"""

    def __init__(self, proto: 'ResolvedBarrierScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan



class ResolvedBeginStmt(ResolvedStatement):
    """Generated wrapper for ResolvedBeginStmtProto"""

    def __init__(self, proto: 'ResolvedBeginStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def read_write_mode(self) -> Optional[int]:
        """Field read_write_mode"""
        return self._proto.read_write_mode

    @cached_property
    def isolation_level_list(self) -> List[str]:
        """Field isolation_level_list"""
        return self._proto.isolation_level_list



class ResolvedCallStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCallStmtProto"""

    def __init__(self, proto: 'ResolvedCallStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def procedure(self) -> Optional['ProcedureRefProto']:
        """Field procedure"""
        return self._proto.procedure

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.argument_list



class ResolvedCast(ResolvedExpr):
    """Generated wrapper for ResolvedCastProto"""

    def __init__(self, proto: 'ResolvedCastProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def return_null_on_error(self) -> Optional[bool]:
        """Field return_null_on_error"""
        return self._proto.return_null_on_error

    @cached_property
    def extended_cast(self) -> Optional['ResolvedExtendedCastProto']:
        """Field extended_cast"""
        return self._proto.extended_cast

    @cached_property
    def format(self) -> Optional['AnyResolvedExprProto']:
        """Field format"""
        return self._proto.format

    @cached_property
    def time_zone(self) -> Optional['AnyResolvedExprProto']:
        """Field time_zone"""
        return self._proto.time_zone

    @cached_property
    def type_modifiers(self) -> Optional['TypeModifiersProto']:
        """Field type_modifiers"""
        return self._proto.type_modifiers



class ResolvedCatalogColumnRef(ResolvedExpr):
    """Generated wrapper for ResolvedCatalogColumnRefProto"""

    def __init__(self, proto: 'ResolvedCatalogColumnRefProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def column(self) -> Optional['ColumnRefProto']:
        """Field column"""
        return self._proto.column



class ResolvedCloneDataStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCloneDataStmtProto"""

    def __init__(self, proto: 'ResolvedCloneDataStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def target_table(self) -> Optional['ResolvedTableScanProto']:
        """Field target_table"""
        return self._proto.target_table

    @cached_property
    def clone_from(self) -> Optional['AnyResolvedScanProto']:
        """Field clone_from"""
        return self._proto.clone_from



class ResolvedColumnAnnotations(ResolvedArgument):
    """Generated wrapper for ResolvedColumnAnnotationsProto"""

    def __init__(self, proto: 'ResolvedColumnAnnotationsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.collation_name

    @cached_property
    def not_null(self) -> Optional[bool]:
        """Field not_null"""
        return self._proto.not_null

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def child_list(self) -> List['ResolvedColumnAnnotationsProto']:
        """Field child_list"""
        return self._proto.child_list

    @cached_property
    def type_parameters(self) -> Optional['TypeParametersProto']:
        """Field type_parameters"""
        return self._proto.type_parameters



class ResolvedColumnDefaultValue(ResolvedArgument):
    """Generated wrapper for ResolvedColumnDefaultValueProto"""

    def __init__(self, proto: 'ResolvedColumnDefaultValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.sql



class ResolvedColumnDefinition(ResolvedArgument):
    """Generated wrapper for ResolvedColumnDefinitionProto"""

    def __init__(self, proto: 'ResolvedColumnDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def annotations(self) -> Optional['ResolvedColumnAnnotationsProto']:
        """Field annotations"""
        return self._proto.annotations

    @cached_property
    def is_hidden(self) -> Optional[bool]:
        """Field is_hidden"""
        return self._proto.is_hidden

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def generated_column_info(self) -> Optional['ResolvedGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.generated_column_info

    @cached_property
    def default_value(self) -> Optional['ResolvedColumnDefaultValueProto']:
        """Field default_value"""
        return self._proto.default_value



class ResolvedColumnHolder(ResolvedArgument):
    """Generated wrapper for ResolvedColumnHolderProto"""

    def __init__(self, proto: 'ResolvedColumnHolderProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column



class ResolvedColumnRef(ResolvedExpr):
    """Generated wrapper for ResolvedColumnRefProto"""

    def __init__(self, proto: 'ResolvedColumnRefProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def is_correlated(self) -> Optional[bool]:
        """Field is_correlated"""
        return self._proto.is_correlated



class ResolvedCommitStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCommitStmtProto"""

    def __init__(self, proto: 'ResolvedCommitStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list



class ResolvedComputedColumnBase(ResolvedArgument):
    """Generated wrapper for ResolvedComputedColumnBaseProto"""

    def __init__(self, proto: 'ResolvedComputedColumnBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedConnection(ResolvedArgument):
    """Generated wrapper for ResolvedConnectionProto"""

    def __init__(self, proto: 'ResolvedConnectionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def connection(self) -> Optional['ConnectionRefProto']:
        """Field connection"""
        return self._proto.connection



class ResolvedConstant(ResolvedExpr):
    """Generated wrapper for ResolvedConstantProto"""

    def __init__(self, proto: 'ResolvedConstantProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def constant(self) -> Optional['ConstantRefProto']:
        """Field constant"""
        return self._proto.constant



class ResolvedConstraint(ResolvedArgument):
    """Generated wrapper for ResolvedConstraintProto"""

    def __init__(self, proto: 'ResolvedConstraintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedCreateDatabaseStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCreateDatabaseStmtProto"""

    def __init__(self, proto: 'ResolvedCreateDatabaseStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateModelAliasedQuery(ResolvedArgument):
    """Generated wrapper for ResolvedCreateModelAliasedQueryProto"""

    def __init__(self, proto: 'ResolvedCreateModelAliasedQueryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list



class ResolvedCreateRowAccessPolicyStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCreateRowAccessPolicyStmtProto"""

    def __init__(self, proto: 'ResolvedCreateRowAccessPolicyStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.create_mode

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def target_name_path(self) -> List[str]:
        """Field target_name_path"""
        return self._proto.target_name_path

    @cached_property
    def grantee_list(self) -> List[str]:
        """Field grantee_list"""
        return self._proto.grantee_list

    @cached_property
    def grantee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field grantee_expr_list"""
        return self._proto.grantee_expr_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def predicate(self) -> Optional['AnyResolvedExprProto']:
        """Field predicate"""
        return self._proto.predicate

    @cached_property
    def predicate_str(self) -> Optional[str]:
        """Field predicate_str"""
        return self._proto.predicate_str



class ResolvedCreateStatement(ResolvedStatement):
    """Generated wrapper for ResolvedCreateStatementProto"""

    def __init__(self, proto: 'ResolvedCreateStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.create_mode



class ResolvedCreateWithEntryStmt(ResolvedStatement):
    """Generated wrapper for ResolvedCreateWithEntryStmtProto"""

    def __init__(self, proto: 'ResolvedCreateWithEntryStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def with_entry(self) -> Optional['ResolvedWithEntryProto']:
        """Field with_entry"""
        return self._proto.with_entry



class ResolvedDMLDefault(ResolvedExpr):
    """Generated wrapper for ResolvedDMLDefaultProto"""

    def __init__(self, proto: 'ResolvedDMLDefaultProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map



class ResolvedDMLValue(ResolvedArgument):
    """Generated wrapper for ResolvedDMLValueProto"""

    def __init__(self, proto: 'ResolvedDMLValueProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def value(self) -> Optional['AnyResolvedExprProto']:
        """Field value"""
        return self._proto.value



class ResolvedDefineTableStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDefineTableStmtProto"""

    def __init__(self, proto: 'ResolvedDefineTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedDeleteStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDeleteStmtProto"""

    def __init__(self, proto: 'ResolvedDeleteStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def assert_rows_modified(self) -> Optional['ResolvedAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ResolvedReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def column_access_list(self) -> List[int]:
        """Field column_access_list"""
        return self._proto.column_access_list

    @cached_property
    def array_offset_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field array_offset_column"""
        return self._proto.array_offset_column

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.where_expr



class ResolvedDescribeScan(ResolvedScan):
    """Generated wrapper for ResolvedDescribeScanProto"""

    def __init__(self, proto: 'ResolvedDescribeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def describe_expr(self) -> Optional['ResolvedComputedColumnProto']:
        """Field describe_expr"""
        return self._proto.describe_expr



class ResolvedDescribeStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDescribeStmtProto"""

    def __init__(self, proto: 'ResolvedDescribeStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def from_name_path(self) -> List[str]:
        """Field from_name_path"""
        return self._proto.from_name_path



class ResolvedDescriptor(ResolvedArgument):
    """Generated wrapper for ResolvedDescriptorProto"""

    def __init__(self, proto: 'ResolvedDescriptorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def descriptor_column_list(self) -> List['ResolvedColumnProto']:
        """Field descriptor_column_list"""
        return self._proto.descriptor_column_list

    @cached_property
    def descriptor_column_name_list(self) -> List[str]:
        """Field descriptor_column_name_list"""
        return self._proto.descriptor_column_name_list



class ResolvedDropFunctionStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropFunctionStmtProto"""

    def __init__(self, proto: 'ResolvedDropFunctionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def arguments(self) -> Optional['ResolvedArgumentListProto']:
        """Field arguments"""
        return self._proto.arguments

    @cached_property
    def signature(self) -> Optional['ResolvedFunctionSignatureHolderProto']:
        """Field signature"""
        return self._proto.signature



class ResolvedDropIndexStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropIndexStmtProto"""

    def __init__(self, proto: 'ResolvedDropIndexStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_name_path(self) -> List[str]:
        """Field table_name_path"""
        return self._proto.table_name_path

    @cached_property
    def index_type(self) -> Optional[int]:
        """Field index_type"""
        return self._proto.index_type



class ResolvedDropMaterializedViewStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropMaterializedViewStmtProto"""

    def __init__(self, proto: 'ResolvedDropMaterializedViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path



class ResolvedDropPrivilegeRestrictionStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropPrivilegeRestrictionStmtProto"""

    def __init__(self, proto: 'ResolvedDropPrivilegeRestrictionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def column_privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field column_privilege_list"""
        return self._proto.column_privilege_list



class ResolvedDropRowAccessPolicyStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropRowAccessPolicyStmtProto"""

    def __init__(self, proto: 'ResolvedDropRowAccessPolicyStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_drop_all(self) -> Optional[bool]:
        """Field is_drop_all"""
        return self._proto.is_drop_all

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def target_name_path(self) -> List[str]:
        """Field target_name_path"""
        return self._proto.target_name_path



class ResolvedDropSnapshotTableStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropSnapshotTableStmtProto"""

    def __init__(self, proto: 'ResolvedDropSnapshotTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path



class ResolvedDropStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropStmtProto"""

    def __init__(self, proto: 'ResolvedDropStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def drop_mode(self) -> Optional[int]:
        """Field drop_mode"""
        return self._proto.drop_mode



class ResolvedDropTableFunctionStmt(ResolvedStatement):
    """Generated wrapper for ResolvedDropTableFunctionStmtProto"""

    def __init__(self, proto: 'ResolvedDropTableFunctionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path



class ResolvedExecuteAsRoleScan(ResolvedScan):
    """Generated wrapper for ResolvedExecuteAsRoleScanProto"""

    def __init__(self, proto: 'ResolvedExecuteAsRoleScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def original_inlined_view(self) -> Optional['TableRefProto']:
        """Field original_inlined_view"""
        return self._proto.original_inlined_view

    @cached_property
    def original_inlined_tvf(self) -> Optional['TableValuedFunctionRefProto']:
        """Field original_inlined_tvf"""
        return self._proto.original_inlined_tvf



class ResolvedExecuteImmediateArgument(ResolvedArgument):
    """Generated wrapper for ResolvedExecuteImmediateArgumentProto"""

    def __init__(self, proto: 'ResolvedExecuteImmediateArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression



class ResolvedExecuteImmediateStmt(ResolvedStatement):
    """Generated wrapper for ResolvedExecuteImmediateStmtProto"""

    def __init__(self, proto: 'ResolvedExecuteImmediateStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def sql(self) -> Optional['AnyResolvedExprProto']:
        """Field sql"""
        return self._proto.sql

    @cached_property
    def into_identifier_list(self) -> List[str]:
        """Field into_identifier_list"""
        return self._proto.into_identifier_list

    @cached_property
    def using_argument_list(self) -> List['ResolvedExecuteImmediateArgumentProto']:
        """Field using_argument_list"""
        return self._proto.using_argument_list



class ResolvedExplainStmt(ResolvedStatement):
    """Generated wrapper for ResolvedExplainStmtProto"""

    def __init__(self, proto: 'ResolvedExplainStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def statement(self) -> Optional['AnyResolvedStatementProto']:
        """Field statement"""
        return self._proto.statement



class ResolvedExportDataStmt(ResolvedStatement):
    """Generated wrapper for ResolvedExportDataStmtProto"""

    def __init__(self, proto: 'ResolvedExportDataStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query



class ResolvedExportMetadataStmt(ResolvedStatement):
    """Generated wrapper for ResolvedExportMetadataStmtProto"""

    def __init__(self, proto: 'ResolvedExportMetadataStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def schema_object_kind(self) -> Optional[str]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedExportModelStmt(ResolvedStatement):
    """Generated wrapper for ResolvedExportModelStmtProto"""

    def __init__(self, proto: 'ResolvedExportModelStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def model_name_path(self) -> List[str]:
        """Field model_name_path"""
        return self._proto.model_name_path

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedExpressionColumn(ResolvedExpr):
    """Generated wrapper for ResolvedExpressionColumnProto"""

    def __init__(self, proto: 'ResolvedExpressionColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class ResolvedExtendedCastElement(ResolvedArgument):
    """Generated wrapper for ResolvedExtendedCastElementProto"""

    def __init__(self, proto: 'ResolvedExtendedCastElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def from_type(self) -> Optional['TypeProto']:
        """Field from_type"""
        return self._proto.from_type

    @cached_property
    def to_type(self) -> Optional['TypeProto']:
        """Field to_type"""
        return self._proto.to_type

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.function



class ResolvedExtendedCast(ResolvedArgument):
    """Generated wrapper for ResolvedExtendedCastProto"""

    def __init__(self, proto: 'ResolvedExtendedCastProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def element_list(self) -> List['ResolvedExtendedCastElementProto']:
        """Field element_list"""
        return self._proto.element_list



class ResolvedFilterFieldArg(ResolvedArgument):
    """Generated wrapper for ResolvedFilterFieldArgProto"""

    def __init__(self, proto: 'ResolvedFilterFieldArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def include(self) -> Optional[bool]:
        """Field include"""
        return self._proto.include

    @cached_property
    def field_descriptor_path(self) -> List['FieldDescriptorRefProto']:
        """Field field_descriptor_path"""
        return self._proto.field_descriptor_path



class ResolvedFilterField(ResolvedExpr):
    """Generated wrapper for ResolvedFilterFieldProto"""

    def __init__(self, proto: 'ResolvedFilterFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def filter_field_arg_list(self) -> List['ResolvedFilterFieldArgProto']:
        """Field filter_field_arg_list"""
        return self._proto.filter_field_arg_list

    @cached_property
    def reset_cleared_required_fields(self) -> Optional[bool]:
        """Field reset_cleared_required_fields"""
        return self._proto.reset_cleared_required_fields



class ResolvedFilterScan(ResolvedScan):
    """Generated wrapper for ResolvedFilterScanProto"""

    def __init__(self, proto: 'ResolvedFilterScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.filter_expr



class ResolvedFlatten(ResolvedExpr):
    """Generated wrapper for ResolvedFlattenProto"""

    def __init__(self, proto: 'ResolvedFlattenProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def get_field_list(self) -> List['AnyResolvedExprProto']:
        """Field get_field_list"""
        return self._proto.get_field_list



class ResolvedFlattenedArg(ResolvedExpr):
    """Generated wrapper for ResolvedFlattenedArgProto"""

    def __init__(self, proto: 'ResolvedFlattenedArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map



class ResolvedFunctionArgument(ResolvedArgument):
    """Generated wrapper for ResolvedFunctionArgumentProto"""

    def __init__(self, proto: 'ResolvedFunctionArgumentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def scan(self) -> Optional['AnyResolvedScanProto']:
        """Field scan"""
        return self._proto.scan

    @cached_property
    def model(self) -> Optional['ResolvedModelProto']:
        """Field model"""
        return self._proto.model

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def descriptor_arg(self) -> Optional['ResolvedDescriptorProto']:
        """Field descriptor_arg"""
        return self._proto.descriptor_arg

    @cached_property
    def argument_column_list(self) -> List['ResolvedColumnProto']:
        """Field argument_column_list"""
        return self._proto.argument_column_list

    @cached_property
    def inline_lambda(self) -> Optional['ResolvedInlineLambdaProto']:
        """Field inline_lambda"""
        return self._proto.inline_lambda

    @cached_property
    def sequence(self) -> Optional['ResolvedSequenceProto']:
        """Field sequence"""
        return self._proto.sequence

    @cached_property
    def graph(self) -> Optional['PropertyGraphRefProto']:
        """Field graph"""
        return self._proto.graph

    @cached_property
    def argument_alias(self) -> Optional[str]:
        """Field argument_alias"""
        return self._proto.argument_alias



class ResolvedFunctionCallBase(ResolvedExpr):
    """Generated wrapper for ResolvedFunctionCallBaseProto"""

    def __init__(self, proto: 'ResolvedFunctionCallBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.function

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.argument_list

    @cached_property
    def generic_argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field generic_argument_list"""
        return self._proto.generic_argument_list

    @cached_property
    def error_mode(self) -> Optional[int]:
        """Field error_mode"""
        return self._proto.error_mode

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.collation_list



class ResolvedFunctionSignatureHolder(ResolvedArgument):
    """Generated wrapper for ResolvedFunctionSignatureHolderProto"""

    def __init__(self, proto: 'ResolvedFunctionSignatureHolderProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature



class ResolvedGeneralizedQueryStmt(ResolvedStatement):
    """Generated wrapper for ResolvedGeneralizedQueryStmtProto"""

    def __init__(self, proto: 'ResolvedGeneralizedQueryStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def output_schema(self) -> Optional['ResolvedOutputSchemaProto']:
        """Field output_schema"""
        return self._proto.output_schema

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query



class ResolvedGeneralizedQuerySubpipeline(ResolvedArgument):
    """Generated wrapper for ResolvedGeneralizedQuerySubpipelineProto"""

    def __init__(self, proto: 'ResolvedGeneralizedQuerySubpipelineProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def subpipeline(self) -> Optional['ResolvedSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline

    @cached_property
    def output_schema(self) -> Optional['ResolvedOutputSchemaProto']:
        """Field output_schema"""
        return self._proto.output_schema



class ResolvedGeneratedColumnInfo(ResolvedArgument):
    """Generated wrapper for ResolvedGeneratedColumnInfoProto"""

    def __init__(self, proto: 'ResolvedGeneratedColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def stored_mode(self) -> Optional[int]:
        """Field stored_mode"""
        return self._proto.stored_mode

    @cached_property
    def generated_mode(self) -> Optional[int]:
        """Field generated_mode"""
        return self._proto.generated_mode

    @cached_property
    def identity_column_info(self) -> Optional['ResolvedIdentityColumnInfoProto']:
        """Field identity_column_info"""
        return self._proto.identity_column_info



class ResolvedGetJsonField(ResolvedExpr):
    """Generated wrapper for ResolvedGetJsonFieldProto"""

    def __init__(self, proto: 'ResolvedGetJsonFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def field_name(self) -> Optional[str]:
        """Field field_name"""
        return self._proto.field_name



class ResolvedGetField(ResolvedExpr):
    """Generated wrapper for ResolvedGetProtoFieldProto"""

    def __init__(self, proto: 'ResolvedGetProtoFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def field_descriptor(self) -> Optional['FieldDescriptorRefProto']:
        """Field field_descriptor"""
        return self._proto.field_descriptor

    @cached_property
    def default_value(self) -> Optional['ValueWithTypeProto']:
        """Field default_value"""
        return self._proto.default_value

    @cached_property
    def get_has_bit(self) -> Optional[bool]:
        """Field get_has_bit"""
        return self._proto.get_has_bit

    @cached_property
    def format(self) -> Optional[int]:
        """Field format"""
        return self._proto.format

    @cached_property
    def return_default_value_when_unset(self) -> Optional[bool]:
        """Field return_default_value_when_unset"""
        return self._proto.return_default_value_when_unset



class ResolvedGetOneof(ResolvedExpr):
    """Generated wrapper for ResolvedGetProtoOneofProto"""

    def __init__(self, proto: 'ResolvedGetProtoOneofProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def oneof_descriptor(self) -> Optional['OneofDescriptorRefProto']:
        """Field oneof_descriptor"""
        return self._proto.oneof_descriptor



class ResolvedGetRowField(ResolvedExpr):
    """Generated wrapper for ResolvedGetRowFieldProto"""

    def __init__(self, proto: 'ResolvedGetRowFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def column(self) -> Optional['ColumnRefProto']:
        """Field column"""
        return self._proto.column



class ResolvedGetStructField(ResolvedExpr):
    """Generated wrapper for ResolvedGetStructFieldProto"""

    def __init__(self, proto: 'ResolvedGetStructFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def field_idx(self) -> Optional[int]:
        """Field field_idx"""
        return self._proto.field_idx

    @cached_property
    def field_expr_is_positional(self) -> Optional[bool]:
        """Field field_expr_is_positional"""
        return self._proto.field_expr_is_positional



class ResolvedGrantOrRevokeStmt(ResolvedStatement):
    """Generated wrapper for ResolvedGrantOrRevokeStmtProto"""

    def __init__(self, proto: 'ResolvedGrantOrRevokeStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field privilege_list"""
        return self._proto.privilege_list

    @cached_property
    def object_type_list(self) -> List[str]:
        """Field object_type_list"""
        return self._proto.object_type_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def grantee_list(self) -> List[str]:
        """Field grantee_list"""
        return self._proto.grantee_list

    @cached_property
    def grantee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field grantee_expr_list"""
        return self._proto.grantee_expr_list



class ResolvedGraphCallScan(ResolvedScan):
    """Generated wrapper for ResolvedGraphCallScanProto"""

    def __init__(self, proto: 'ResolvedGraphCallScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.optional

    @cached_property
    def subquery(self) -> Optional['AnyResolvedScanProto']:
        """Field subquery"""
        return self._proto.subquery

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def parameter_list(self) -> List['ResolvedColumnRefProto']:
        """Field parameter_list"""
        return self._proto.parameter_list



class ResolvedGraphDynamicLabelSpecification(ResolvedArgument):
    """Generated wrapper for ResolvedGraphDynamicLabelSpecificationProto"""

    def __init__(self, proto: 'ResolvedGraphDynamicLabelSpecificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def label_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field label_expr"""
        return self._proto.label_expr



class ResolvedGraphDynamicPropertiesSpecification(ResolvedArgument):
    """Generated wrapper for ResolvedGraphDynamicPropertiesSpecificationProto"""

    def __init__(self, proto: 'ResolvedGraphDynamicPropertiesSpecificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def property_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field property_expr"""
        return self._proto.property_expr



class ResolvedGraphElementIdentifier(ResolvedArgument):
    """Generated wrapper for ResolvedGraphElementIdentifierProto"""

    def __init__(self, proto: 'ResolvedGraphElementIdentifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def element_table(self) -> Optional['GraphElementTableRefProto']:
        """Field element_table"""
        return self._proto.element_table

    @cached_property
    def key_list(self) -> List['AnyResolvedExprProto']:
        """Field key_list"""
        return self._proto.key_list

    @cached_property
    def source_node_identifier(self) -> Optional['ResolvedGraphElementIdentifierProto']:
        """Field source_node_identifier"""
        return self._proto.source_node_identifier

    @cached_property
    def dest_node_identifier(self) -> Optional['ResolvedGraphElementIdentifierProto']:
        """Field dest_node_identifier"""
        return self._proto.dest_node_identifier



class ResolvedGraphElementLabel(ResolvedArgument):
    """Generated wrapper for ResolvedGraphElementLabelProto"""

    def __init__(self, proto: 'ResolvedGraphElementLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def property_declaration_name_list(self) -> List[str]:
        """Field property_declaration_name_list"""
        return self._proto.property_declaration_name_list

    @cached_property
    def options_list(self) -> List['ResolvedOptionProto']:
        """Field options_list"""
        return self._proto.options_list



class ResolvedGraphElementProperty(ResolvedArgument):
    """Generated wrapper for ResolvedGraphElementPropertyProto"""

    def __init__(self, proto: 'ResolvedGraphElementPropertyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def declaration(self) -> Optional['GraphPropertyDeclarationRefProto']:
        """Field declaration"""
        return self._proto.declaration

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedGraphElementTable(ResolvedArgument):
    """Generated wrapper for ResolvedGraphElementTableProto"""

    def __init__(self, proto: 'ResolvedGraphElementTableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def key_list(self) -> List['AnyResolvedExprProto']:
        """Field key_list"""
        return self._proto.key_list

    @cached_property
    def source_node_reference(self) -> Optional['ResolvedGraphNodeTableReferenceProto']:
        """Field source_node_reference"""
        return self._proto.source_node_reference

    @cached_property
    def dest_node_reference(self) -> Optional['ResolvedGraphNodeTableReferenceProto']:
        """Field dest_node_reference"""
        return self._proto.dest_node_reference

    @cached_property
    def label_name_list(self) -> List[str]:
        """Field label_name_list"""
        return self._proto.label_name_list

    @cached_property
    def property_definition_list(self) -> List['ResolvedGraphPropertyDefinitionProto']:
        """Field property_definition_list"""
        return self._proto.property_definition_list

    @cached_property
    def dynamic_label(self) -> Optional['ResolvedGraphDynamicLabelSpecificationProto']:
        """Field dynamic_label"""
        return self._proto.dynamic_label

    @cached_property
    def dynamic_properties(self) -> Optional['ResolvedGraphDynamicPropertiesSpecificationProto']:
        """Field dynamic_properties"""
        return self._proto.dynamic_properties



class ResolvedGraphGetElementProperty(ResolvedExpr):
    """Generated wrapper for ResolvedGraphGetElementPropertyProto"""

    def __init__(self, proto: 'ResolvedGraphGetElementPropertyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def property(self) -> Optional['GraphPropertyDeclarationRefProto']:
        """Field property"""
        return self._proto.property

    @cached_property
    def property_name(self) -> Optional['AnyResolvedExprProto']:
        """Field property_name"""
        return self._proto.property_name



class ResolvedGraphIsLabeledPredicate(ResolvedExpr):
    """Generated wrapper for ResolvedGraphIsLabeledPredicateProto"""

    def __init__(self, proto: 'ResolvedGraphIsLabeledPredicateProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def is_not(self) -> Optional[bool]:
        """Field is_not"""
        return self._proto.is_not

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def label_expr(self) -> Optional['AnyResolvedGraphLabelExprProto']:
        """Field label_expr"""
        return self._proto.label_expr



class ResolvedGraphLabelExpr(ResolvedArgument):
    """Generated wrapper for ResolvedGraphLabelExprProto"""

    def __init__(self, proto: 'ResolvedGraphLabelExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedGraphMakeArrayVariable(ResolvedArgument):
    """Generated wrapper for ResolvedGraphMakeArrayVariableProto"""

    def __init__(self, proto: 'ResolvedGraphMakeArrayVariableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def element(self) -> Optional['ResolvedColumnProto']:
        """Field element"""
        return self._proto.element

    @cached_property
    def array(self) -> Optional['ResolvedColumnProto']:
        """Field array"""
        return self._proto.array



class ResolvedGraphMakeElement(ResolvedExpr):
    """Generated wrapper for ResolvedGraphMakeElementProto"""

    def __init__(self, proto: 'ResolvedGraphMakeElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def identifier(self) -> Optional['ResolvedGraphElementIdentifierProto']:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def property_list(self) -> List['ResolvedGraphElementPropertyProto']:
        """Field property_list"""
        return self._proto.property_list

    @cached_property
    def label_list(self) -> List['GraphElementLabelRefProto']:
        """Field label_list"""
        return self._proto.label_list

    @cached_property
    def dynamic_labels(self) -> Optional['AnyResolvedExprProto']:
        """Field dynamic_labels"""
        return self._proto.dynamic_labels

    @cached_property
    def dynamic_properties(self) -> Optional['AnyResolvedExprProto']:
        """Field dynamic_properties"""
        return self._proto.dynamic_properties



class ResolvedGraphNodeTableReference(ResolvedArgument):
    """Generated wrapper for ResolvedGraphNodeTableReferenceProto"""

    def __init__(self, proto: 'ResolvedGraphNodeTableReferenceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def node_table_identifier(self) -> Optional[str]:
        """Field node_table_identifier"""
        return self._proto.node_table_identifier

    @cached_property
    def edge_table_column_list(self) -> List['AnyResolvedExprProto']:
        """Field edge_table_column_list"""
        return self._proto.edge_table_column_list

    @cached_property
    def node_table_column_list(self) -> List['AnyResolvedExprProto']:
        """Field node_table_column_list"""
        return self._proto.node_table_column_list



class ResolvedGraphPathCost(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPathCostProto"""

    def __init__(self, proto: 'ResolvedGraphPathCostProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def cost_supertype(self) -> Optional['TypeProto']:
        """Field cost_supertype"""
        return self._proto.cost_supertype



class ResolvedGraphPathMode(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPathModeProto"""

    def __init__(self, proto: 'ResolvedGraphPathModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def path_mode(self) -> Optional[int]:
        """Field path_mode"""
        return self._proto.path_mode



class ResolvedGraphPathPatternQuantifier(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPathPatternQuantifierProto"""

    def __init__(self, proto: 'ResolvedGraphPathPatternQuantifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def lower_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field lower_bound"""
        return self._proto.lower_bound

    @cached_property
    def upper_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field upper_bound"""
        return self._proto.upper_bound



class ResolvedGraphPathScanBase(ResolvedScan):
    """Generated wrapper for ResolvedGraphPathScanBaseProto"""

    def __init__(self, proto: 'ResolvedGraphPathScanBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedGraphPathSearchPrefix(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPathSearchPrefixProto"""

    def __init__(self, proto: 'ResolvedGraphPathSearchPrefixProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional[int]:
        """Field type"""
        return self._proto.type

    @cached_property
    def path_count(self) -> Optional['AnyResolvedExprProto']:
        """Field path_count"""
        return self._proto.path_count



class ResolvedGraphPropertyDeclaration(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPropertyDeclarationProto"""

    def __init__(self, proto: 'ResolvedGraphPropertyDeclarationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.type



class ResolvedGraphPropertyDefinition(ResolvedArgument):
    """Generated wrapper for ResolvedGraphPropertyDefinitionProto"""

    def __init__(self, proto: 'ResolvedGraphPropertyDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.sql

    @cached_property
    def property_declaration_name(self) -> Optional[str]:
        """Field property_declaration_name"""
        return self._proto.property_declaration_name

    @cached_property
    def options_list(self) -> List['ResolvedOptionProto']:
        """Field options_list"""
        return self._proto.options_list



class ResolvedGraphRefScan(ResolvedScan):
    """Generated wrapper for ResolvedGraphRefScanProto"""

    def __init__(self, proto: 'ResolvedGraphRefScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedGraphScanBase(ResolvedScan):
    """Generated wrapper for ResolvedGraphScanBaseProto"""

    def __init__(self, proto: 'ResolvedGraphScanBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedGraphTableScan(ResolvedScan):
    """Generated wrapper for ResolvedGraphTableScanProto"""

    def __init__(self, proto: 'ResolvedGraphTableScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def property_graph(self) -> Optional['PropertyGraphRefProto']:
        """Field property_graph"""
        return self._proto.property_graph

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedGraphScanBaseProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def shape_expr_list(self) -> List['ResolvedComputedColumnProto']:
        """Field shape_expr_list"""
        return self._proto.shape_expr_list



class ResolvedGroupRowsScan(ResolvedScan):
    """Generated wrapper for ResolvedGroupRowsScanProto"""

    def __init__(self, proto: 'ResolvedGroupRowsScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_column_list(self) -> List['ResolvedComputedColumnProto']:
        """Field input_column_list"""
        return self._proto.input_column_list

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias



class ResolvedGroupingCall(ResolvedArgument):
    """Generated wrapper for ResolvedGroupingCallProto"""

    def __init__(self, proto: 'ResolvedGroupingCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def group_by_column(self) -> Optional['ResolvedColumnRefProto']:
        """Field group_by_column"""
        return self._proto.group_by_column

    @cached_property
    def output_column(self) -> Optional['ResolvedColumnProto']:
        """Field output_column"""
        return self._proto.output_column



class ResolvedGroupingSetBase(ResolvedArgument):
    """Generated wrapper for ResolvedGroupingSetBaseProto"""

    def __init__(self, proto: 'ResolvedGroupingSetBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedGroupingSetMultiColumn(ResolvedArgument):
    """Generated wrapper for ResolvedGroupingSetMultiColumnProto"""

    def __init__(self, proto: 'ResolvedGroupingSetMultiColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnRefProto']:
        """Field column_list"""
        return self._proto.column_list



class ResolvedIdentityColumnInfo(ResolvedArgument):
    """Generated wrapper for ResolvedIdentityColumnInfoProto"""

    def __init__(self, proto: 'ResolvedIdentityColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def start_with_value(self) -> Optional['ValueWithTypeProto']:
        """Field start_with_value"""
        return self._proto.start_with_value

    @cached_property
    def increment_by_value(self) -> Optional['ValueWithTypeProto']:
        """Field increment_by_value"""
        return self._proto.increment_by_value

    @cached_property
    def max_value(self) -> Optional['ValueWithTypeProto']:
        """Field max_value"""
        return self._proto.max_value

    @cached_property
    def min_value(self) -> Optional['ValueWithTypeProto']:
        """Field min_value"""
        return self._proto.min_value

    @cached_property
    def cycling_enabled(self) -> Optional[bool]:
        """Field cycling_enabled"""
        return self._proto.cycling_enabled



class ResolvedImportStmt(ResolvedStatement):
    """Generated wrapper for ResolvedImportStmtProto"""

    def __init__(self, proto: 'ResolvedImportStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def import_kind(self) -> Optional[int]:
        """Field import_kind"""
        return self._proto.import_kind

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def file_path(self) -> Optional[str]:
        """Field file_path"""
        return self._proto.file_path

    @cached_property
    def alias_path(self) -> List[str]:
        """Field alias_path"""
        return self._proto.alias_path

    @cached_property
    def into_alias_path(self) -> List[str]:
        """Field into_alias_path"""
        return self._proto.into_alias_path

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedIndexItem(ResolvedArgument):
    """Generated wrapper for ResolvedIndexItemProto"""

    def __init__(self, proto: 'ResolvedIndexItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_ref(self) -> Optional['ResolvedColumnRefProto']:
        """Field column_ref"""
        return self._proto.column_ref

    @cached_property
    def descending(self) -> Optional[bool]:
        """Field descending"""
        return self._proto.descending

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedInlineLambda(ResolvedArgument):
    """Generated wrapper for ResolvedInlineLambdaProto"""

    def __init__(self, proto: 'ResolvedInlineLambdaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def argument_list(self) -> List['ResolvedColumnProto']:
        """Field argument_list"""
        return self._proto.argument_list

    @cached_property
    def parameter_list(self) -> List['ResolvedColumnRefProto']:
        """Field parameter_list"""
        return self._proto.parameter_list

    @cached_property
    def body(self) -> Optional['AnyResolvedExprProto']:
        """Field body"""
        return self._proto.body



class ResolvedInsertRow(ResolvedArgument):
    """Generated wrapper for ResolvedInsertRowProto"""

    def __init__(self, proto: 'ResolvedInsertRowProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def value_list(self) -> List['ResolvedDMLValueProto']:
        """Field value_list"""
        return self._proto.value_list



class ResolvedInsertStmt(ResolvedStatement):
    """Generated wrapper for ResolvedInsertStmtProto"""

    def __init__(self, proto: 'ResolvedInsertStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def insert_mode(self) -> Optional[int]:
        """Field insert_mode"""
        return self._proto.insert_mode

    @cached_property
    def assert_rows_modified(self) -> Optional['ResolvedAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ResolvedReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def insert_column_list(self) -> List['ResolvedColumnProto']:
        """Field insert_column_list"""
        return self._proto.insert_column_list

    @cached_property
    def query_parameter_list(self) -> List['ResolvedColumnRefProto']:
        """Field query_parameter_list"""
        return self._proto.query_parameter_list

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def query_output_column_list(self) -> List['ResolvedColumnProto']:
        """Field query_output_column_list"""
        return self._proto.query_output_column_list

    @cached_property
    def row_list(self) -> List['ResolvedInsertRowProto']:
        """Field row_list"""
        return self._proto.row_list

    @cached_property
    def column_access_list(self) -> List[int]:
        """Field column_access_list"""
        return self._proto.column_access_list

    @cached_property
    def on_conflict_clause(self) -> Optional['ResolvedOnConflictClauseProto']:
        """Field on_conflict_clause"""
        return self._proto.on_conflict_clause

    @cached_property
    def topologically_sorted_generated_column_id_list(self) -> List[int]:
        """Field topologically_sorted_generated_column_id_list"""
        return self._proto.topologically_sorted_generated_column_id_list

    @cached_property
    def generated_column_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field generated_column_expr_list"""
        return self._proto.generated_column_expr_list



class ResolvedJoinScan(ResolvedScan):
    """Generated wrapper for ResolvedJoinScanProto"""

    def __init__(self, proto: 'ResolvedJoinScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def join_type(self) -> Optional[int]:
        """Field join_type"""
        return self._proto.join_type

    @cached_property
    def left_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field left_scan"""
        return self._proto.left_scan

    @cached_property
    def right_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field right_scan"""
        return self._proto.right_scan

    @cached_property
    def join_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field join_expr"""
        return self._proto.join_expr

    @cached_property
    def has_using(self) -> Optional[bool]:
        """Field has_using"""
        return self._proto.has_using

    @cached_property
    def is_lateral(self) -> Optional[bool]:
        """Field is_lateral"""
        return self._proto.is_lateral

    @cached_property
    def parameter_list(self) -> List['ResolvedColumnRefProto']:
        """Field parameter_list"""
        return self._proto.parameter_list



class ResolvedLimitOffsetScan(ResolvedScan):
    """Generated wrapper for ResolvedLimitOffsetScanProto"""

    def __init__(self, proto: 'ResolvedLimitOffsetScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def limit(self) -> Optional['AnyResolvedExprProto']:
        """Field limit"""
        return self._proto.limit

    @cached_property
    def offset(self) -> Optional['AnyResolvedExprProto']:
        """Field offset"""
        return self._proto.offset



class ResolvedLiteral(ResolvedExpr):
    """Generated wrapper for ResolvedLiteralProto"""

    def __init__(self, proto: 'ResolvedLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def value(self) -> Optional['ValueWithTypeProto']:
        """Field value"""
        return self._proto.value

    @cached_property
    def has_explicit_type(self) -> Optional[bool]:
        """Field has_explicit_type"""
        return self._proto.has_explicit_type

    @cached_property
    def float_literal_id(self) -> Optional[int]:
        """Field float_literal_id"""
        return self._proto.float_literal_id

    @cached_property
    def preserve_in_literal_remover(self) -> Optional[bool]:
        """Field preserve_in_literal_remover"""
        return self._proto.preserve_in_literal_remover



class ResolvedLockMode(ResolvedArgument):
    """Generated wrapper for ResolvedLockModeProto"""

    def __init__(self, proto: 'ResolvedLockModeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def strength(self) -> Optional[int]:
        """Field strength"""
        return self._proto.strength



class ResolvedLogScan(ResolvedScan):
    """Generated wrapper for ResolvedLogScanProto"""

    def __init__(self, proto: 'ResolvedLogScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def subpipeline(self) -> Optional['ResolvedSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline

    @cached_property
    def output_schema(self) -> Optional['ResolvedOutputSchemaProto']:
        """Field output_schema"""
        return self._proto.output_schema



class ResolvedMakeField(ResolvedArgument):
    """Generated wrapper for ResolvedMakeProtoFieldProto"""

    def __init__(self, proto: 'ResolvedMakeProtoFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def field_descriptor(self) -> Optional['FieldDescriptorRefProto']:
        """Field field_descriptor"""
        return self._proto.field_descriptor

    @cached_property
    def format(self) -> Optional[int]:
        """Field format"""
        return self._proto.format

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedMake(ResolvedExpr):
    """Generated wrapper for ResolvedMakeProtoProto"""

    def __init__(self, proto: 'ResolvedMakeProtoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def field_list(self) -> List['ResolvedMakeProtoFieldProto']:
        """Field field_list"""
        return self._proto.field_list



class ResolvedMakeStruct(ResolvedExpr):
    """Generated wrapper for ResolvedMakeStructProto"""

    def __init__(self, proto: 'ResolvedMakeStructProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def field_list(self) -> List['AnyResolvedExprProto']:
        """Field field_list"""
        return self._proto.field_list



class ResolvedMatchRecognizePatternExpr(ResolvedArgument):
    """Generated wrapper for ResolvedMatchRecognizePatternExprProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range



class ResolvedMatchRecognizeScan(ResolvedScan):
    """Generated wrapper for ResolvedMatchRecognizeScanProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def analytic_function_group_list(self) -> List['ResolvedAnalyticFunctionGroupProto']:
        """Field analytic_function_group_list"""
        return self._proto.analytic_function_group_list

    @cached_property
    def pattern_variable_definition_list(self) -> List['ResolvedMatchRecognizeVariableDefinitionProto']:
        """Field pattern_variable_definition_list"""
        return self._proto.pattern_variable_definition_list

    @cached_property
    def pattern(self) -> Optional['AnyResolvedMatchRecognizePatternExprProto']:
        """Field pattern"""
        return self._proto.pattern

    @cached_property
    def after_match_skip_mode(self) -> Optional[int]:
        """Field after_match_skip_mode"""
        return self._proto.after_match_skip_mode

    @cached_property
    def measure_group_list(self) -> List['ResolvedMeasureGroupProto']:
        """Field measure_group_list"""
        return self._proto.measure_group_list

    @cached_property
    def match_number_column(self) -> Optional['ResolvedColumnProto']:
        """Field match_number_column"""
        return self._proto.match_number_column

    @cached_property
    def match_row_number_column(self) -> Optional['ResolvedColumnProto']:
        """Field match_row_number_column"""
        return self._proto.match_row_number_column

    @cached_property
    def classifier_column(self) -> Optional['ResolvedColumnProto']:
        """Field classifier_column"""
        return self._proto.classifier_column



class ResolvedMatchRecognizeVariableDefinition(ResolvedArgument):
    """Generated wrapper for ResolvedMatchRecognizeVariableDefinitionProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizeVariableDefinitionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def predicate(self) -> Optional['AnyResolvedExprProto']:
        """Field predicate"""
        return self._proto.predicate



class ResolvedMeasureGroup(ResolvedArgument):
    """Generated wrapper for ResolvedMeasureGroupProto"""

    def __init__(self, proto: 'ResolvedMeasureGroupProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def pattern_variable_ref(self) -> Optional['ResolvedMatchRecognizePatternVariableRefProto']:
        """Field pattern_variable_ref"""
        return self._proto.pattern_variable_ref

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.aggregate_list



class ResolvedMergeStmt(ResolvedStatement):
    """Generated wrapper for ResolvedMergeStmtProto"""

    def __init__(self, proto: 'ResolvedMergeStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def column_access_list(self) -> List[int]:
        """Field column_access_list"""
        return self._proto.column_access_list

    @cached_property
    def from_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field from_scan"""
        return self._proto.from_scan

    @cached_property
    def merge_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field merge_expr"""
        return self._proto.merge_expr

    @cached_property
    def when_clause_list(self) -> List['ResolvedMergeWhenProto']:
        """Field when_clause_list"""
        return self._proto.when_clause_list



class ResolvedMergeWhen(ResolvedArgument):
    """Generated wrapper for ResolvedMergeWhenProto"""

    def __init__(self, proto: 'ResolvedMergeWhenProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def match_type(self) -> Optional[int]:
        """Field match_type"""
        return self._proto.match_type

    @cached_property
    def match_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field match_expr"""
        return self._proto.match_expr

    @cached_property
    def action_type(self) -> Optional[int]:
        """Field action_type"""
        return self._proto.action_type

    @cached_property
    def insert_column_list(self) -> List['ResolvedColumnProto']:
        """Field insert_column_list"""
        return self._proto.insert_column_list

    @cached_property
    def insert_row(self) -> Optional['ResolvedInsertRowProto']:
        """Field insert_row"""
        return self._proto.insert_row

    @cached_property
    def update_item_list(self) -> List['ResolvedUpdateItemProto']:
        """Field update_item_list"""
        return self._proto.update_item_list



class ResolvedModel(ResolvedArgument):
    """Generated wrapper for ResolvedModelProto"""

    def __init__(self, proto: 'ResolvedModelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def model(self) -> Optional['ModelRefProto']:
        """Field model"""
        return self._proto.model



class ResolvedModuleStmt(ResolvedStatement):
    """Generated wrapper for ResolvedModuleStmtProto"""

    def __init__(self, proto: 'ResolvedModuleStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedMultiStmt(ResolvedStatement):
    """Generated wrapper for ResolvedMultiStmtProto"""

    def __init__(self, proto: 'ResolvedMultiStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def statement_list(self) -> List['AnyResolvedStatementProto']:
        """Field statement_list"""
        return self._proto.statement_list



class ResolvedObjectUnit(ResolvedArgument):
    """Generated wrapper for ResolvedObjectUnitProto"""

    def __init__(self, proto: 'ResolvedObjectUnitProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path



class ResolvedOnConflictClause(ResolvedArgument):
    """Generated wrapper for ResolvedOnConflictClauseProto"""

    def __init__(self, proto: 'ResolvedOnConflictClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def conflict_action(self) -> Optional[int]:
        """Field conflict_action"""
        return self._proto.conflict_action

    @cached_property
    def conflict_target_column_list(self) -> List['ResolvedColumnProto']:
        """Field conflict_target_column_list"""
        return self._proto.conflict_target_column_list

    @cached_property
    def unique_constraint_name(self) -> Optional[str]:
        """Field unique_constraint_name"""
        return self._proto.unique_constraint_name

    @cached_property
    def insert_row_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field insert_row_scan"""
        return self._proto.insert_row_scan

    @cached_property
    def update_item_list(self) -> List['ResolvedUpdateItemProto']:
        """Field update_item_list"""
        return self._proto.update_item_list

    @cached_property
    def update_where_expression(self) -> Optional['AnyResolvedExprProto']:
        """Field update_where_expression"""
        return self._proto.update_where_expression



class ResolvedOption(ResolvedArgument):
    """Generated wrapper for ResolvedOptionProto"""

    def __init__(self, proto: 'ResolvedOptionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def qualifier(self) -> Optional[str]:
        """Field qualifier"""
        return self._proto.qualifier

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def value(self) -> Optional['AnyResolvedExprProto']:
        """Field value"""
        return self._proto.value

    @cached_property
    def assignment_op(self) -> Optional[int]:
        """Field assignment_op"""
        return self._proto.assignment_op



class ResolvedOrderByItem(ResolvedArgument):
    """Generated wrapper for ResolvedOrderByItemProto"""

    def __init__(self, proto: 'ResolvedOrderByItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_ref(self) -> Optional['ResolvedColumnRefProto']:
        """Field column_ref"""
        return self._proto.column_ref

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.collation_name

    @cached_property
    def is_descending(self) -> Optional[bool]:
        """Field is_descending"""
        return self._proto.is_descending

    @cached_property
    def null_order(self) -> Optional[int]:
        """Field null_order"""
        return self._proto.null_order

    @cached_property
    def collation(self) -> Optional['ResolvedCollationProto']:
        """Field collation"""
        return self._proto.collation



class ResolvedOrderByScan(ResolvedScan):
    """Generated wrapper for ResolvedOrderByScanProto"""

    def __init__(self, proto: 'ResolvedOrderByScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def order_by_item_list(self) -> List['ResolvedOrderByItemProto']:
        """Field order_by_item_list"""
        return self._proto.order_by_item_list



class ResolvedOutputColumn(ResolvedArgument):
    """Generated wrapper for ResolvedOutputColumnProto"""

    def __init__(self, proto: 'ResolvedOutputColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column



class ResolvedOutputSchema(ResolvedArgument):
    """Generated wrapper for ResolvedOutputSchemaProto"""

    def __init__(self, proto: 'ResolvedOutputSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table



class ResolvedParameter(ResolvedExpr):
    """Generated wrapper for ResolvedParameterProto"""

    def __init__(self, proto: 'ResolvedParameterProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def position(self) -> Optional[int]:
        """Field position"""
        return self._proto.position

    @cached_property
    def is_untyped(self) -> Optional[bool]:
        """Field is_untyped"""
        return self._proto.is_untyped



class ResolvedPipeCreateTableScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeCreateTableScanProto"""

    def __init__(self, proto: 'ResolvedPipeCreateTableScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def create_table_as_select_stmt(self) -> Optional['ResolvedCreateTableAsSelectStmtProto']:
        """Field create_table_as_select_stmt"""
        return self._proto.create_table_as_select_stmt



class ResolvedPipeExportDataScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeExportDataScanProto"""

    def __init__(self, proto: 'ResolvedPipeExportDataScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def export_data_stmt(self) -> Optional['ResolvedExportDataStmtProto']:
        """Field export_data_stmt"""
        return self._proto.export_data_stmt



class ResolvedPipeForkScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeForkScanProto"""

    def __init__(self, proto: 'ResolvedPipeForkScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def subpipeline_list(self) -> List['ResolvedGeneralizedQuerySubpipelineProto']:
        """Field subpipeline_list"""
        return self._proto.subpipeline_list



class ResolvedPipeIfCase(ResolvedArgument):
    """Generated wrapper for ResolvedPipeIfCaseProto"""

    def __init__(self, proto: 'ResolvedPipeIfCaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyResolvedExprProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def subpipeline_sql(self) -> Optional[str]:
        """Field subpipeline_sql"""
        return self._proto.subpipeline_sql

    @cached_property
    def subpipeline(self) -> Optional['ResolvedSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline



class ResolvedPipeIfScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeIfScanProto"""

    def __init__(self, proto: 'ResolvedPipeIfScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def selected_case(self) -> Optional[int]:
        """Field selected_case"""
        return self._proto.selected_case

    @cached_property
    def if_case_list(self) -> List['ResolvedPipeIfCaseProto']:
        """Field if_case_list"""
        return self._proto.if_case_list



class ResolvedPipeInsertScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeInsertScanProto"""

    def __init__(self, proto: 'ResolvedPipeInsertScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def insert_stmt(self) -> Optional['ResolvedInsertStmtProto']:
        """Field insert_stmt"""
        return self._proto.insert_stmt



class ResolvedPipeTeeScan(ResolvedScan):
    """Generated wrapper for ResolvedPipeTeeScanProto"""

    def __init__(self, proto: 'ResolvedPipeTeeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def subpipeline_list(self) -> List['ResolvedGeneralizedQuerySubpipelineProto']:
        """Field subpipeline_list"""
        return self._proto.subpipeline_list



class ResolvedPivotColumn(ResolvedArgument):
    """Generated wrapper for ResolvedPivotColumnProto"""

    def __init__(self, proto: 'ResolvedPivotColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def pivot_expr_index(self) -> Optional[int]:
        """Field pivot_expr_index"""
        return self._proto.pivot_expr_index

    @cached_property
    def pivot_value_index(self) -> Optional[int]:
        """Field pivot_value_index"""
        return self._proto.pivot_value_index



class ResolvedPivotScan(ResolvedScan):
    """Generated wrapper for ResolvedPivotScanProto"""

    def __init__(self, proto: 'ResolvedPivotScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.group_by_list

    @cached_property
    def pivot_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field pivot_expr_list"""
        return self._proto.pivot_expr_list

    @cached_property
    def for_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field for_expr"""
        return self._proto.for_expr

    @cached_property
    def pivot_value_list(self) -> List['AnyResolvedExprProto']:
        """Field pivot_value_list"""
        return self._proto.pivot_value_list

    @cached_property
    def pivot_column_list(self) -> List['ResolvedPivotColumnProto']:
        """Field pivot_column_list"""
        return self._proto.pivot_column_list



class ResolvedPrivilege(ResolvedArgument):
    """Generated wrapper for ResolvedPrivilegeProto"""

    def __init__(self, proto: 'ResolvedPrivilegeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def action_type(self) -> Optional[str]:
        """Field action_type"""
        return self._proto.action_type

    @cached_property
    def unit_list(self) -> List['ResolvedObjectUnitProto']:
        """Field unit_list"""
        return self._proto.unit_list



class ResolvedProjectScan(ResolvedScan):
    """Generated wrapper for ResolvedProjectScanProto"""

    def __init__(self, proto: 'ResolvedProjectScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def expr_list(self) -> List['ResolvedComputedColumnProto']:
        """Field expr_list"""
        return self._proto.expr_list

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan



class ResolvedQueryStmt(ResolvedStatement):
    """Generated wrapper for ResolvedQueryStmtProto"""

    def __init__(self, proto: 'ResolvedQueryStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query



class ResolvedRecursionDepthModifier(ResolvedArgument):
    """Generated wrapper for ResolvedRecursionDepthModifierProto"""

    def __init__(self, proto: 'ResolvedRecursionDepthModifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def lower_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field lower_bound"""
        return self._proto.lower_bound

    @cached_property
    def upper_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field upper_bound"""
        return self._proto.upper_bound

    @cached_property
    def recursion_depth_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field recursion_depth_column"""
        return self._proto.recursion_depth_column



class ResolvedRecursiveRefScan(ResolvedScan):
    """Generated wrapper for ResolvedRecursiveRefScanProto"""

    def __init__(self, proto: 'ResolvedRecursiveRefScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedRecursiveScan(ResolvedScan):
    """Generated wrapper for ResolvedRecursiveScanProto"""

    def __init__(self, proto: 'ResolvedRecursiveScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def op_type(self) -> Optional[int]:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def non_recursive_term(self) -> Optional['ResolvedSetOperationItemProto']:
        """Field non_recursive_term"""
        return self._proto.non_recursive_term

    @cached_property
    def recursive_term(self) -> Optional['ResolvedSetOperationItemProto']:
        """Field recursive_term"""
        return self._proto.recursive_term

    @cached_property
    def recursion_depth_modifier(self) -> Optional['ResolvedRecursionDepthModifierProto']:
        """Field recursion_depth_modifier"""
        return self._proto.recursion_depth_modifier



class ResolvedRelationArgumentScan(ResolvedScan):
    """Generated wrapper for ResolvedRelationArgumentScanProto"""

    def __init__(self, proto: 'ResolvedRelationArgumentScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table



class ResolvedRenameStmt(ResolvedStatement):
    """Generated wrapper for ResolvedRenameStmtProto"""

    def __init__(self, proto: 'ResolvedRenameStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def old_name_path(self) -> List[str]:
        """Field old_name_path"""
        return self._proto.old_name_path

    @cached_property
    def new_name_path(self) -> List[str]:
        """Field new_name_path"""
        return self._proto.new_name_path



class ResolvedReplaceFieldItem(ResolvedArgument):
    """Generated wrapper for ResolvedReplaceFieldItemProto"""

    def __init__(self, proto: 'ResolvedReplaceFieldItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def struct_index_path(self) -> List[int]:
        """Field struct_index_path"""
        return self._proto.struct_index_path

    @cached_property
    def proto_field_path(self) -> List['FieldDescriptorRefProto']:
        """Field proto_field_path"""
        return self._proto.proto_field_path



class ResolvedReplaceField(ResolvedExpr):
    """Generated wrapper for ResolvedReplaceFieldProto"""

    def __init__(self, proto: 'ResolvedReplaceFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def replace_field_item_list(self) -> List['ResolvedReplaceFieldItemProto']:
        """Field replace_field_item_list"""
        return self._proto.replace_field_item_list



class ResolvedReturningClause(ResolvedArgument):
    """Generated wrapper for ResolvedReturningClauseProto"""

    def __init__(self, proto: 'ResolvedReturningClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def action_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field action_column"""
        return self._proto.action_column

    @cached_property
    def expr_list(self) -> List['ResolvedComputedColumnProto']:
        """Field expr_list"""
        return self._proto.expr_list



class ResolvedRollbackStmt(ResolvedStatement):
    """Generated wrapper for ResolvedRollbackStmtProto"""

    def __init__(self, proto: 'ResolvedRollbackStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list



class ResolvedRunBatchStmt(ResolvedStatement):
    """Generated wrapper for ResolvedRunBatchStmtProto"""

    def __init__(self, proto: 'ResolvedRunBatchStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list



class ResolvedSampleScan(ResolvedScan):
    """Generated wrapper for ResolvedSampleScanProto"""

    def __init__(self, proto: 'ResolvedSampleScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def method(self) -> Optional[str]:
        """Field method"""
        return self._proto.method

    @cached_property
    def size(self) -> Optional['AnyResolvedExprProto']:
        """Field size"""
        return self._proto.size

    @cached_property
    def unit(self) -> Optional[int]:
        """Field unit"""
        return self._proto.unit

    @cached_property
    def repeatable_argument(self) -> Optional['AnyResolvedExprProto']:
        """Field repeatable_argument"""
        return self._proto.repeatable_argument

    @cached_property
    def weight_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field weight_column"""
        return self._proto.weight_column

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list



class ResolvedSequence(ResolvedArgument):
    """Generated wrapper for ResolvedSequenceProto"""

    def __init__(self, proto: 'ResolvedSequenceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def sequence(self) -> Optional['SequenceRefProto']:
        """Field sequence"""
        return self._proto.sequence



class ResolvedSetOperationItem(ResolvedArgument):
    """Generated wrapper for ResolvedSetOperationItemProto"""

    def __init__(self, proto: 'ResolvedSetOperationItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def scan(self) -> Optional['AnyResolvedScanProto']:
        """Field scan"""
        return self._proto.scan

    @cached_property
    def output_column_list(self) -> List['ResolvedColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list



class ResolvedSetOperationScan(ResolvedScan):
    """Generated wrapper for ResolvedSetOperationScanProto"""

    def __init__(self, proto: 'ResolvedSetOperationScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def op_type(self) -> Optional[int]:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def input_item_list(self) -> List['ResolvedSetOperationItemProto']:
        """Field input_item_list"""
        return self._proto.input_item_list

    @cached_property
    def column_match_mode(self) -> Optional[int]:
        """Field column_match_mode"""
        return self._proto.column_match_mode

    @cached_property
    def column_propagation_mode(self) -> Optional[int]:
        """Field column_propagation_mode"""
        return self._proto.column_propagation_mode



class ResolvedSetTransactionStmt(ResolvedStatement):
    """Generated wrapper for ResolvedSetTransactionStmtProto"""

    def __init__(self, proto: 'ResolvedSetTransactionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def read_write_mode(self) -> Optional[int]:
        """Field read_write_mode"""
        return self._proto.read_write_mode

    @cached_property
    def isolation_level_list(self) -> List[str]:
        """Field isolation_level_list"""
        return self._proto.isolation_level_list



class ResolvedShowStmt(ResolvedStatement):
    """Generated wrapper for ResolvedShowStmtProto"""

    def __init__(self, proto: 'ResolvedShowStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def identifier(self) -> Optional[str]:
        """Field identifier"""
        return self._proto.identifier

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def like_expr(self) -> Optional['ResolvedLiteralProto']:
        """Field like_expr"""
        return self._proto.like_expr



class ResolvedSingleRowScan(ResolvedScan):
    """Generated wrapper for ResolvedSingleRowScanProto"""

    def __init__(self, proto: 'ResolvedSingleRowScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedStartBatchStmt(ResolvedStatement):
    """Generated wrapper for ResolvedStartBatchStmtProto"""

    def __init__(self, proto: 'ResolvedStartBatchStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def batch_type(self) -> Optional[str]:
        """Field batch_type"""
        return self._proto.batch_type



class ResolvedStatementWithPipeOperatorsStmt(ResolvedStatement):
    """Generated wrapper for ResolvedStatementWithPipeOperatorsStmtProto"""

    def __init__(self, proto: 'ResolvedStatementWithPipeOperatorsStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def statement(self) -> Optional['AnyResolvedStatementProto']:
        """Field statement"""
        return self._proto.statement

    @cached_property
    def suffix_subpipeline_sql(self) -> Optional[str]:
        """Field suffix_subpipeline_sql"""
        return self._proto.suffix_subpipeline_sql



class ResolvedStaticDescribeScan(ResolvedScan):
    """Generated wrapper for ResolvedStaticDescribeScanProto"""

    def __init__(self, proto: 'ResolvedStaticDescribeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def describe_text(self) -> Optional[str]:
        """Field describe_text"""
        return self._proto.describe_text



class ResolvedSubpipelineInputScan(ResolvedScan):
    """Generated wrapper for ResolvedSubpipelineInputScanProto"""

    def __init__(self, proto: 'ResolvedSubpipelineInputScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedSubpipeline(ResolvedArgument):
    """Generated wrapper for ResolvedSubpipelineProto"""

    def __init__(self, proto: 'ResolvedSubpipelineProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def scan(self) -> Optional['AnyResolvedScanProto']:
        """Field scan"""
        return self._proto.scan



class ResolvedSubpipelineStmt(ResolvedStatement):
    """Generated wrapper for ResolvedSubpipelineStmtProto"""

    def __init__(self, proto: 'ResolvedSubpipelineStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def subpipeline(self) -> Optional['ResolvedSubpipelineProto']:
        """Field subpipeline"""
        return self._proto.subpipeline

    @cached_property
    def output_schema(self) -> Optional['ResolvedOutputSchemaProto']:
        """Field output_schema"""
        return self._proto.output_schema



class ResolvedSubqueryExpr(ResolvedExpr):
    """Generated wrapper for ResolvedSubqueryExprProto"""

    def __init__(self, proto: 'ResolvedSubqueryExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def subquery_type(self) -> Optional[int]:
        """Field subquery_type"""
        return self._proto.subquery_type

    @cached_property
    def parameter_list(self) -> List['ResolvedColumnRefProto']:
        """Field parameter_list"""
        return self._proto.parameter_list

    @cached_property
    def in_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field in_expr"""
        return self._proto.in_expr

    @cached_property
    def in_collation(self) -> Optional['ResolvedCollationProto']:
        """Field in_collation"""
        return self._proto.in_collation

    @cached_property
    def subquery(self) -> Optional['AnyResolvedScanProto']:
        """Field subquery"""
        return self._proto.subquery

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list



class ResolvedSystemVariable(ResolvedExpr):
    """Generated wrapper for ResolvedSystemVariableProto"""

    def __init__(self, proto: 'ResolvedSystemVariableProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path



class ResolvedTVFScan(ResolvedScan):
    """Generated wrapper for ResolvedTVFScanProto"""

    def __init__(self, proto: 'ResolvedTVFScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def tvf(self) -> Optional['TableValuedFunctionRefProto']:
        """Field tvf"""
        return self._proto.tvf

    @cached_property
    def signature(self) -> Optional['TVFSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field argument_list"""
        return self._proto.argument_list

    @cached_property
    def column_index_list(self) -> List[int]:
        """Field column_index_list"""
        return self._proto.column_index_list

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def function_call_signature(self) -> Optional['FunctionSignatureProto']:
        """Field function_call_signature"""
        return self._proto.function_call_signature



class ResolvedTableAndColumnInfo(ResolvedArgument):
    """Generated wrapper for ResolvedTableAndColumnInfoProto"""

    def __init__(self, proto: 'ResolvedTableAndColumnInfoProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def table(self) -> Optional['TableRefProto']:
        """Field table"""
        return self._proto.table

    @cached_property
    def column_index_list(self) -> List[int]:
        """Field column_index_list"""
        return self._proto.column_index_list



class ResolvedTableScan(ResolvedScan):
    """Generated wrapper for ResolvedTableScanProto"""

    def __init__(self, proto: 'ResolvedTableScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def table(self) -> Optional['TableRefProto']:
        """Field table"""
        return self._proto.table

    @cached_property
    def for_system_time_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field for_system_time_expr"""
        return self._proto.for_system_time_expr

    @cached_property
    def column_index_list(self) -> List[int]:
        """Field column_index_list"""
        return self._proto.column_index_list

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def lock_mode(self) -> Optional['ResolvedLockModeProto']:
        """Field lock_mode"""
        return self._proto.lock_mode

    @cached_property
    def read_as_row_type(self) -> Optional[bool]:
        """Field read_as_row_type"""
        return self._proto.read_as_row_type

    @cached_property
    def table_column_list(self) -> List['ColumnRefProto']:
        """Field table_column_list"""
        return self._proto.table_column_list



class ResolvedTruncateStmt(ResolvedStatement):
    """Generated wrapper for ResolvedTruncateStmtProto"""

    def __init__(self, proto: 'ResolvedTruncateStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.where_expr



class ResolvedUndropStmt(ResolvedStatement):
    """Generated wrapper for ResolvedUndropStmtProto"""

    def __init__(self, proto: 'ResolvedUndropStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def schema_object_kind(self) -> Optional[str]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def for_system_time_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field for_system_time_expr"""
        return self._proto.for_system_time_expr

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedUnnestItem(ResolvedArgument):
    """Generated wrapper for ResolvedUnnestItemProto"""

    def __init__(self, proto: 'ResolvedUnnestItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def array_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field array_expr"""
        return self._proto.array_expr

    @cached_property
    def element_column(self) -> Optional['ResolvedColumnProto']:
        """Field element_column"""
        return self._proto.element_column

    @cached_property
    def array_offset_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field array_offset_column"""
        return self._proto.array_offset_column



class ResolvedUnpivotArg(ResolvedArgument):
    """Generated wrapper for ResolvedUnpivotArgProto"""

    def __init__(self, proto: 'ResolvedUnpivotArgProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnRefProto']:
        """Field column_list"""
        return self._proto.column_list



class ResolvedUnpivotScan(ResolvedScan):
    """Generated wrapper for ResolvedUnpivotScanProto"""

    def __init__(self, proto: 'ResolvedUnpivotScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def value_column_list(self) -> List['ResolvedColumnProto']:
        """Field value_column_list"""
        return self._proto.value_column_list

    @cached_property
    def label_column(self) -> Optional['ResolvedColumnProto']:
        """Field label_column"""
        return self._proto.label_column

    @cached_property
    def label_list(self) -> List['ResolvedLiteralProto']:
        """Field label_list"""
        return self._proto.label_list

    @cached_property
    def unpivot_arg_list(self) -> List['ResolvedUnpivotArgProto']:
        """Field unpivot_arg_list"""
        return self._proto.unpivot_arg_list

    @cached_property
    def projected_input_column_list(self) -> List['ResolvedComputedColumnProto']:
        """Field projected_input_column_list"""
        return self._proto.projected_input_column_list

    @cached_property
    def include_nulls(self) -> Optional[bool]:
        """Field include_nulls"""
        return self._proto.include_nulls



class ResolvedUnsetArgumentScan(ResolvedScan):
    """Generated wrapper for ResolvedUnsetArgumentScanProto"""

    def __init__(self, proto: 'ResolvedUnsetArgumentScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source



class ResolvedUpdateConstructor(ResolvedExpr):
    """Generated wrapper for ResolvedUpdateConstructorProto"""

    def __init__(self, proto: 'ResolvedUpdateConstructorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def alias(self) -> Optional[str]:
        """Field alias"""
        return self._proto.alias

    @cached_property
    def update_field_item_list(self) -> List['ResolvedUpdateFieldItemProto']:
        """Field update_field_item_list"""
        return self._proto.update_field_item_list



class ResolvedUpdateFieldItem(ResolvedArgument):
    """Generated wrapper for ResolvedUpdateFieldItemProto"""

    def __init__(self, proto: 'ResolvedUpdateFieldItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def proto_field_path(self) -> List['FieldDescriptorRefProto']:
        """Field proto_field_path"""
        return self._proto.proto_field_path

    @cached_property
    def operation(self) -> Optional[int]:
        """Field operation"""
        return self._proto.operation



class ResolvedUpdateItemElement(ResolvedArgument):
    """Generated wrapper for ResolvedUpdateItemElementProto"""

    def __init__(self, proto: 'ResolvedUpdateItemElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def subscript(self) -> Optional['AnyResolvedExprProto']:
        """Field subscript"""
        return self._proto.subscript

    @cached_property
    def update_item(self) -> Optional['ResolvedUpdateItemProto']:
        """Field update_item"""
        return self._proto.update_item



class ResolvedUpdateItem(ResolvedArgument):
    """Generated wrapper for ResolvedUpdateItemProto"""

    def __init__(self, proto: 'ResolvedUpdateItemProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def target(self) -> Optional['AnyResolvedExprProto']:
        """Field target"""
        return self._proto.target

    @cached_property
    def set_value(self) -> Optional['ResolvedDMLValueProto']:
        """Field set_value"""
        return self._proto.set_value

    @cached_property
    def element_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field element_column"""
        return self._proto.element_column

    @cached_property
    def update_item_element_list(self) -> List['ResolvedUpdateItemElementProto']:
        """Field update_item_element_list"""
        return self._proto.update_item_element_list

    @cached_property
    def delete_list(self) -> List['ResolvedDeleteStmtProto']:
        """Field delete_list"""
        return self._proto.delete_list

    @cached_property
    def update_list(self) -> List['ResolvedUpdateStmtProto']:
        """Field update_list"""
        return self._proto.update_list

    @cached_property
    def insert_list(self) -> List['ResolvedInsertStmtProto']:
        """Field insert_list"""
        return self._proto.insert_list



class ResolvedUpdateStmt(ResolvedStatement):
    """Generated wrapper for ResolvedUpdateStmtProto"""

    def __init__(self, proto: 'ResolvedUpdateStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def column_access_list(self) -> List[int]:
        """Field column_access_list"""
        return self._proto.column_access_list

    @cached_property
    def assert_rows_modified(self) -> Optional['ResolvedAssertRowsModifiedProto']:
        """Field assert_rows_modified"""
        return self._proto.assert_rows_modified

    @cached_property
    def returning(self) -> Optional['ResolvedReturningClauseProto']:
        """Field returning"""
        return self._proto.returning

    @cached_property
    def array_offset_column(self) -> Optional['ResolvedColumnHolderProto']:
        """Field array_offset_column"""
        return self._proto.array_offset_column

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.where_expr

    @cached_property
    def update_item_list(self) -> List['ResolvedUpdateItemProto']:
        """Field update_item_list"""
        return self._proto.update_item_list

    @cached_property
    def from_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field from_scan"""
        return self._proto.from_scan

    @cached_property
    def topologically_sorted_generated_column_id_list(self) -> List[int]:
        """Field topologically_sorted_generated_column_id_list"""
        return self._proto.topologically_sorted_generated_column_id_list

    @cached_property
    def generated_column_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field generated_column_expr_list"""
        return self._proto.generated_column_expr_list



class ResolvedWindowFrameExpr(ResolvedArgument):
    """Generated wrapper for ResolvedWindowFrameExprProto"""

    def __init__(self, proto: 'ResolvedWindowFrameExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def boundary_type(self) -> Optional[int]:
        """Field boundary_type"""
        return self._proto.boundary_type

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression



class ResolvedWindowFrame(ResolvedArgument):
    """Generated wrapper for ResolvedWindowFrameProto"""

    def __init__(self, proto: 'ResolvedWindowFrameProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def frame_unit(self) -> Optional[int]:
        """Field frame_unit"""
        return self._proto.frame_unit

    @cached_property
    def start_expr(self) -> Optional['ResolvedWindowFrameExprProto']:
        """Field start_expr"""
        return self._proto.start_expr

    @cached_property
    def end_expr(self) -> Optional['ResolvedWindowFrameExprProto']:
        """Field end_expr"""
        return self._proto.end_expr



class ResolvedWindowOrdering(ResolvedArgument):
    """Generated wrapper for ResolvedWindowOrderingProto"""

    def __init__(self, proto: 'ResolvedWindowOrderingProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def order_by_item_list(self) -> List['ResolvedOrderByItemProto']:
        """Field order_by_item_list"""
        return self._proto.order_by_item_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list



class ResolvedWindowPartitioning(ResolvedArgument):
    """Generated wrapper for ResolvedWindowPartitioningProto"""

    def __init__(self, proto: 'ResolvedWindowPartitioningProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def partition_by_list(self) -> List['ResolvedColumnRefProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.collation_list



class ResolvedWithEntry(ResolvedArgument):
    """Generated wrapper for ResolvedWithEntryProto"""

    def __init__(self, proto: 'ResolvedWithEntryProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def with_query_name(self) -> Optional[str]:
        """Field with_query_name"""
        return self._proto.with_query_name

    @cached_property
    def with_subquery(self) -> Optional['AnyResolvedScanProto']:
        """Field with_subquery"""
        return self._proto.with_subquery



class ResolvedWithExpr(ResolvedExpr):
    """Generated wrapper for ResolvedWithExprProto"""

    def __init__(self, proto: 'ResolvedWithExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.type_annotation_map

    @cached_property
    def assignment_list(self) -> List['ResolvedComputedColumnProto']:
        """Field assignment_list"""
        return self._proto.assignment_list

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedWithPartitionColumns(ResolvedArgument):
    """Generated wrapper for ResolvedWithPartitionColumnsProto"""

    def __init__(self, proto: 'ResolvedWithPartitionColumnsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.column_definition_list



class ResolvedWithRefScan(ResolvedScan):
    """Generated wrapper for ResolvedWithRefScanProto"""

    def __init__(self, proto: 'ResolvedWithRefScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def with_query_name(self) -> Optional[str]:
        """Field with_query_name"""
        return self._proto.with_query_name



class ResolvedWithScan(ResolvedScan):
    """Generated wrapper for ResolvedWithScanProto"""

    def __init__(self, proto: 'ResolvedWithScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.node_source

    @cached_property
    def with_entry_list(self) -> List['ResolvedWithEntryProto']:
        """Field with_entry_list"""
        return self._proto.with_entry_list

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.recursive



class ASTAlterStatementBase(ASTDdlStatement):
    """Generated wrapper for ASTAlterStatementBaseProto"""

    def __init__(self, proto: 'ASTAlterStatementBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTArrayColumnSchema(ASTElementTypeColumnSchema):
    """Generated wrapper for ASTArrayColumnSchemaProto"""

    def __init__(self, proto: 'ASTArrayColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.parent.options_list

    @cached_property
    def element_schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field element_schema"""
        return self._proto.parent.element_schema



class ASTArrayElement(ASTGeneralizedPathExpression):
    """Generated wrapper for ASTArrayElementProto"""

    def __init__(self, proto: 'ASTArrayElementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def array(self) -> Optional['AnyASTExpressionProto']:
        """Field array"""
        return self._proto.array

    @cached_property
    def position(self) -> Optional['AnyASTExpressionProto']:
        """Field position"""
        return self._proto.position

    @cached_property
    def open_bracket_location(self) -> Optional['ASTLocationProto']:
        """Field open_bracket_location"""
        return self._proto.open_bracket_location



class ASTAssignmentFromStruct(ASTScriptStatement):
    """Generated wrapper for ASTAssignmentFromStructProto"""

    def __init__(self, proto: 'ASTAssignmentFromStructProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def variables(self) -> Optional['ASTIdentifierListProto']:
        """Field variables"""
        return self._proto.variables

    @cached_property
    def struct_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field struct_expression"""
        return self._proto.struct_expression



class ASTBeginEndBlock(ASTScriptStatement):
    """Generated wrapper for ASTBeginEndBlockProto"""

    def __init__(self, proto: 'ASTBeginEndBlockProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.label

    @cached_property
    def statement_list_node(self) -> Optional['ASTStatementListProto']:
        """Field statement_list_node"""
        return self._proto.statement_list_node

    @cached_property
    def handler_list(self) -> Optional['ASTExceptionHandlerListProto']:
        """Field handler_list"""
        return self._proto.handler_list



class ASTBigNumericLiteral(ASTLeaf):
    """Generated wrapper for ASTBigNumericLiteralProto"""

    def __init__(self, proto: 'ASTBigNumericLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def string_literal(self) -> Optional['ASTStringLiteralProto']:
        """Field string_literal"""
        return self._proto.string_literal



class ASTBreakContinueStatement(ASTScriptStatement):
    """Generated wrapper for ASTBreakContinueStatementProto"""

    def __init__(self, proto: 'ASTBreakContinueStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.label



class ASTBytesLiteral(ASTLeaf):
    """Generated wrapper for ASTBytesLiteralProto"""

    def __init__(self, proto: 'ASTBytesLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def components(self) -> List['ASTBytesLiteralComponentProto']:
        """Field components"""
        return self._proto.components

    @cached_property
    def bytes_value(self) -> Optional[str]:
        """Field bytes_value"""
        return self._proto.bytes_value



class ASTCaseStatement(ASTScriptStatement):
    """Generated wrapper for ASTCaseStatementProto"""

    def __init__(self, proto: 'ASTCaseStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def when_then_clauses(self) -> Optional['ASTWhenThenClauseListProto']:
        """Field when_then_clauses"""
        return self._proto.when_then_clauses

    @cached_property
    def else_list(self) -> Optional['ASTStatementListProto']:
        """Field else_list"""
        return self._proto.else_list



class ASTCheckConstraint(ASTTableConstraint):
    """Generated wrapper for ASTCheckConstraintProto"""

    def __init__(self, proto: 'ASTCheckConstraintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def is_enforced(self) -> Optional[bool]:
        """Field is_enforced"""
        return self._proto.is_enforced



class ASTCloneDataSource(ASTTableDataSource):
    """Generated wrapper for ASTCloneDataSourceProto"""

    def __init__(self, proto: 'ASTCloneDataSourceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.parent.postfix_operators

    @cached_property
    def path_expr(self) -> Optional['ASTPathExpressionProto']:
        """Field path_expr"""
        return self._proto.parent.path_expr

    @cached_property
    def for_system_time(self) -> Optional['ASTForSystemTimeProto']:
        """Field for_system_time"""
        return self._proto.parent.for_system_time

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.parent.where_clause



class ASTCopyDataSource(ASTTableDataSource):
    """Generated wrapper for ASTCopyDataSourceProto"""

    def __init__(self, proto: 'ASTCopyDataSourceProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def postfix_operators(self) -> List['AnyASTPostfixTableOperatorProto']:
        """Field postfix_operators"""
        return self._proto.parent.parent.postfix_operators

    @cached_property
    def path_expr(self) -> Optional['ASTPathExpressionProto']:
        """Field path_expr"""
        return self._proto.parent.path_expr

    @cached_property
    def for_system_time(self) -> Optional['ASTForSystemTimeProto']:
        """Field for_system_time"""
        return self._proto.parent.for_system_time

    @cached_property
    def where_clause(self) -> Optional['ASTWhereClauseProto']:
        """Field where_clause"""
        return self._proto.parent.where_clause



class ASTCreateStatement(ASTDdlStatement):
    """Generated wrapper for ASTCreateStatementProto"""

    def __init__(self, proto: 'ASTCreateStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ASTDotGeneralizedField(ASTGeneralizedPathExpression):
    """Generated wrapper for ASTDotGeneralizedFieldProto"""

    def __init__(self, proto: 'ASTDotGeneralizedFieldProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.path



class ASTDotIdentifier(ASTGeneralizedPathExpression):
    """Generated wrapper for ASTDotIdentifierProto"""

    def __init__(self, proto: 'ASTDotIdentifierProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTDropEntityStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropEntityStatementProto"""

    def __init__(self, proto: 'ASTDropEntityStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def entity_type(self) -> Optional['ASTIdentifierProto']:
        """Field entity_type"""
        return self._proto.entity_type

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropFunctionStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropFunctionStatementProto"""

    def __init__(self, proto: 'ASTDropFunctionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def parameters(self) -> Optional['ASTFunctionParametersProto']:
        """Field parameters"""
        return self._proto.parameters

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropIndexStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropIndexStatementProto"""

    def __init__(self, proto: 'ASTDropIndexStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropMaterializedViewStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropMaterializedViewStatementProto"""

    def __init__(self, proto: 'ASTDropMaterializedViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropPrivilegeRestrictionStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropPrivilegeRestrictionStatementProto"""

    def __init__(self, proto: 'ASTDropPrivilegeRestrictionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def privileges(self) -> Optional['ASTPrivilegesProto']:
        """Field privileges"""
        return self._proto.privileges

    @cached_property
    def object_type(self) -> Optional['ASTIdentifierProto']:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def name_path(self) -> Optional['ASTPathExpressionProto']:
        """Field name_path"""
        return self._proto.name_path



class ASTDropRowAccessPolicyStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropRowAccessPolicyStatementProto"""

    def __init__(self, proto: 'ASTDropRowAccessPolicyStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropSnapshotTableStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropSnapshotTableStatementProto"""

    def __init__(self, proto: 'ASTDropSnapshotTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTDropStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropStatementProto"""

    def __init__(self, proto: 'ASTDropStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def drop_mode(self) -> Optional[int]:
        """Field drop_mode"""
        return self._proto.drop_mode

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def schema_object_kind(self) -> Optional[int]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind



class ASTDropTableFunctionStatement(ASTDdlStatement):
    """Generated wrapper for ASTDropTableFunctionStatementProto"""

    def __init__(self, proto: 'ASTDropTableFunctionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ASTExtendedPathExpression(ASTGeneralizedPathExpression):
    """Generated wrapper for ASTExtendedPathExpressionProto"""

    def __init__(self, proto: 'ASTExtendedPathExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def parenthesized_path(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field parenthesized_path"""
        return self._proto.parenthesized_path

    @cached_property
    def generalized_path_expression(self) -> Optional['AnyASTGeneralizedPathExpressionProto']:
        """Field generalized_path_expression"""
        return self._proto.generalized_path_expression



class ASTForeignKey(ASTTableConstraint):
    """Generated wrapper for ASTForeignKeyProto"""

    def __init__(self, proto: 'ASTForeignKeyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> Optional['ASTColumnListProto']:
        """Field column_list"""
        return self._proto.column_list

    @cached_property
    def reference(self) -> Optional['ASTForeignKeyReferenceProto']:
        """Field reference"""
        return self._proto.reference

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name



class ASTGqlInlineSubqueryCall(ASTGqlCallBase):
    """Generated wrapper for ASTGqlInlineSubqueryCallProto"""

    def __init__(self, proto: 'ASTGqlInlineSubqueryCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.parent.optional

    @cached_property
    def is_partitioning(self) -> Optional[bool]:
        """Field is_partitioning"""
        return self._proto.parent.is_partitioning

    @cached_property
    def name_capture_list(self) -> Optional['ASTIdentifierListProto']:
        """Field name_capture_list"""
        return self._proto.parent.name_capture_list

    @cached_property
    def subquery(self) -> Optional['ASTQueryProto']:
        """Field subquery"""
        return self._proto.subquery



class ASTGqlNamedCall(ASTGqlCallBase):
    """Generated wrapper for ASTGqlNamedCallProto"""

    def __init__(self, proto: 'ASTGqlNamedCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.parent.optional

    @cached_property
    def is_partitioning(self) -> Optional[bool]:
        """Field is_partitioning"""
        return self._proto.parent.is_partitioning

    @cached_property
    def name_capture_list(self) -> Optional['ASTIdentifierListProto']:
        """Field name_capture_list"""
        return self._proto.parent.name_capture_list

    @cached_property
    def tvf_call(self) -> Optional['ASTTVFProto']:
        """Field tvf_call"""
        return self._proto.tvf_call

    @cached_property
    def yield_clause(self) -> Optional['ASTYieldItemListProto']:
        """Field yield_clause"""
        return self._proto.yield_clause



class ASTGraphEdgePattern(ASTGraphElementPattern):
    """Generated wrapper for ASTGraphEdgePatternProto"""

    def __init__(self, proto: 'ASTGraphEdgePatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.parent.parent.quantifier

    @cached_property
    def filler(self) -> Optional['ASTGraphElementPatternFillerProto']:
        """Field filler"""
        return self._proto.parent.filler

    @cached_property
    def orientation(self) -> Optional[int]:
        """Field orientation"""
        return self._proto.orientation

    @cached_property
    def lhs_hint(self) -> Optional['ASTGraphLhsHintProto']:
        """Field lhs_hint"""
        return self._proto.lhs_hint

    @cached_property
    def rhs_hint(self) -> Optional['ASTGraphRhsHintProto']:
        """Field rhs_hint"""
        return self._proto.rhs_hint



class ASTGraphNodePattern(ASTGraphElementPattern):
    """Generated wrapper for ASTGraphNodePatternProto"""

    def __init__(self, proto: 'ASTGraphNodePatternProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def quantifier(self) -> Optional['AnyASTQuantifierProto']:
        """Field quantifier"""
        return self._proto.parent.parent.quantifier

    @cached_property
    def filler(self) -> Optional['ASTGraphElementPatternFillerProto']:
        """Field filler"""
        return self._proto.parent.filler



class ASTIfStatement(ASTScriptStatement):
    """Generated wrapper for ASTIfStatementProto"""

    def __init__(self, proto: 'ASTIfStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition

    @cached_property
    def then_list(self) -> Optional['ASTStatementListProto']:
        """Field then_list"""
        return self._proto.then_list

    @cached_property
    def elseif_clauses(self) -> Optional['ASTElseifClauseListProto']:
        """Field elseif_clauses"""
        return self._proto.elseif_clauses

    @cached_property
    def else_list(self) -> Optional['ASTStatementListProto']:
        """Field else_list"""
        return self._proto.else_list



class ASTJSONLiteral(ASTLeaf):
    """Generated wrapper for ASTJSONLiteralProto"""

    def __init__(self, proto: 'ASTJSONLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def string_literal(self) -> Optional['ASTStringLiteralProto']:
        """Field string_literal"""
        return self._proto.string_literal



class ASTLoopStatement(ASTScriptStatement):
    """Generated wrapper for ASTLoopStatementProto"""

    def __init__(self, proto: 'ASTLoopStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.label

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.body



class ASTNumericLiteral(ASTLeaf):
    """Generated wrapper for ASTNumericLiteralProto"""

    def __init__(self, proto: 'ASTNumericLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def string_literal(self) -> Optional['ASTStringLiteralProto']:
        """Field string_literal"""
        return self._proto.string_literal



class ASTParameterExpr(ASTParameterExprBase):
    """Generated wrapper for ASTParameterExprProto"""

    def __init__(self, proto: 'ASTParameterExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def position(self) -> Optional[int]:
        """Field position"""
        return self._proto.position



class ASTPathExpression(ASTGeneralizedPathExpression):
    """Generated wrapper for ASTPathExpressionProto"""

    def __init__(self, proto: 'ASTPathExpressionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def names(self) -> List['ASTIdentifierProto']:
        """Field names"""
        return self._proto.names



class ASTPrimaryKey(ASTTableConstraint):
    """Generated wrapper for ASTPrimaryKeyProto"""

    def __init__(self, proto: 'ASTPrimaryKeyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def element_list(self) -> Optional['ASTPrimaryKeyElementListProto']:
        """Field element_list"""
        return self._proto.element_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def constraint_name(self) -> Optional['ASTIdentifierProto']:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def enforced(self) -> Optional[bool]:
        """Field enforced"""
        return self._proto.enforced



class ASTPrintableLeaf(ASTLeaf):
    """Generated wrapper for ASTPrintableLeafProto"""

    def __init__(self, proto: 'ASTPrintableLeafProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.image



class ASTRaiseStatement(ASTScriptStatement):
    """Generated wrapper for ASTRaiseStatementProto"""

    def __init__(self, proto: 'ASTRaiseStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def message(self) -> Optional['AnyASTExpressionProto']:
        """Field message"""
        return self._proto.message



class ASTRangeColumnSchema(ASTElementTypeColumnSchema):
    """Generated wrapper for ASTRangeColumnSchemaProto"""

    def __init__(self, proto: 'ASTRangeColumnSchemaProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def type_parameters(self) -> Optional['ASTTypeParameterListProto']:
        """Field type_parameters"""
        return self._proto.parent.parent.type_parameters

    @cached_property
    def generated_column_info(self) -> Optional['ASTGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.parent.parent.generated_column_info

    @cached_property
    def default_expression(self) -> Optional['AnyASTExpressionProto']:
        """Field default_expression"""
        return self._proto.parent.parent.default_expression

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.parent.collate

    @cached_property
    def attributes(self) -> Optional['ASTColumnAttributeListProto']:
        """Field attributes"""
        return self._proto.parent.parent.attributes

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.parent.options_list

    @cached_property
    def element_schema(self) -> Optional['AnyASTColumnSchemaProto']:
        """Field element_schema"""
        return self._proto.parent.element_schema



class ASTReturnStatement(ASTScriptStatement):
    """Generated wrapper for ASTReturnStatementProto"""

    def __init__(self, proto: 'ASTReturnStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range



class ASTSingleAssignment(ASTScriptStatement):
    """Generated wrapper for ASTSingleAssignmentProto"""

    def __init__(self, proto: 'ASTSingleAssignmentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def variable(self) -> Optional['ASTIdentifierProto']:
        """Field variable"""
        return self._proto.variable

    @cached_property
    def expression(self) -> Optional['AnyASTExpressionProto']:
        """Field expression"""
        return self._proto.expression



class ASTStringLiteral(ASTLeaf):
    """Generated wrapper for ASTStringLiteralProto"""

    def __init__(self, proto: 'ASTStringLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def components(self) -> List['ASTStringLiteralComponentProto']:
        """Field components"""
        return self._proto.components

    @cached_property
    def string_value(self) -> Optional[str]:
        """Field string_value"""
        return self._proto.string_value



class ASTSystemVariableExpr(ASTParameterExprBase):
    """Generated wrapper for ASTSystemVariableExprProto"""

    def __init__(self, proto: 'ASTSystemVariableExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parenthesized

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.path



class ASTUndropStatement(ASTDdlStatement):
    """Generated wrapper for ASTUndropStatementProto"""

    def __init__(self, proto: 'ASTUndropStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def schema_object_kind(self) -> Optional[int]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def for_system_time(self) -> Optional['ASTForSystemTimeProto']:
        """Field for_system_time"""
        return self._proto.for_system_time

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTVariableDeclaration(ASTScriptStatement):
    """Generated wrapper for ASTVariableDeclarationProto"""

    def __init__(self, proto: 'ASTVariableDeclarationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def variable_list(self) -> Optional['ASTIdentifierListProto']:
        """Field variable_list"""
        return self._proto.variable_list

    @cached_property
    def type(self) -> Optional['AnyASTTypeProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def default_value(self) -> Optional['AnyASTExpressionProto']:
        """Field default_value"""
        return self._proto.default_value



class ResolvedAddColumnAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAddColumnActionProto"""

    def __init__(self, proto: 'ResolvedAddColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def column_definition(self) -> Optional['ResolvedColumnDefinitionProto']:
        """Field column_definition"""
        return self._proto.column_definition



class ResolvedAddColumnIdentifierAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAddColumnIdentifierActionProto"""

    def __init__(self, proto: 'ResolvedAddColumnIdentifierActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> List['ResolvedOptionProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ResolvedAddConstraintAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAddConstraintActionProto"""

    def __init__(self, proto: 'ResolvedAddConstraintActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def constraint(self) -> Optional['AnyResolvedConstraintProto']:
        """Field constraint"""
        return self._proto.constraint

    @cached_property
    def table(self) -> Optional['TableRefProto']:
        """Field table"""
        return self._proto.table



class ResolvedAddSubEntityAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAddSubEntityActionProto"""

    def __init__(self, proto: 'ResolvedAddSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def entity_type(self) -> Optional[str]:
        """Field entity_type"""
        return self._proto.entity_type

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> List['ResolvedOptionProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists



class ResolvedAddToRestricteeListAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAddToRestricteeListActionProto"""

    def __init__(self, proto: 'ResolvedAddToRestricteeListActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.is_if_not_exists

    @cached_property
    def restrictee_list(self) -> List['AnyResolvedExprProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ResolvedAggregateScan(ResolvedAggregateScanBase):
    """Generated wrapper for ResolvedAggregateScanProto"""

    def __init__(self, proto: 'ResolvedAggregateScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.parent.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.parent.group_by_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.parent.aggregate_list

    @cached_property
    def grouping_set_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field grouping_set_list"""
        return self._proto.parent.grouping_set_list

    @cached_property
    def rollup_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field rollup_column_list"""
        return self._proto.parent.rollup_column_list

    @cached_property
    def grouping_call_list(self) -> List['ResolvedGroupingCallProto']:
        """Field grouping_call_list"""
        return self._proto.parent.grouping_call_list



class ResolvedAggregationThresholdAggregateScan(ResolvedAggregateScanBase):
    """Generated wrapper for ResolvedAggregationThresholdAggregateScanProto"""

    def __init__(self, proto: 'ResolvedAggregationThresholdAggregateScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.parent.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.parent.group_by_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.parent.aggregate_list

    @cached_property
    def grouping_set_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field grouping_set_list"""
        return self._proto.parent.grouping_set_list

    @cached_property
    def rollup_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field rollup_column_list"""
        return self._proto.parent.rollup_column_list

    @cached_property
    def grouping_call_list(self) -> List['ResolvedGroupingCallProto']:
        """Field grouping_call_list"""
        return self._proto.parent.grouping_call_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedAlterAllRowAccessPoliciesStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterAllRowAccessPoliciesStmtProto"""

    def __init__(self, proto: 'ResolvedAlterAllRowAccessPoliciesStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan



class ResolvedAlterApproxViewStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterApproxViewStmtProto"""

    def __init__(self, proto: 'ResolvedAlterApproxViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterColumnAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAlterColumnActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.column



class ResolvedAlterConnectionStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterConnectionStmtProto"""

    def __init__(self, proto: 'ResolvedAlterConnectionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterDatabaseStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterDatabaseStmtProto"""

    def __init__(self, proto: 'ResolvedAlterDatabaseStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterEntityStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterEntityStmtProto"""

    def __init__(self, proto: 'ResolvedAlterEntityStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def entity_type(self) -> Optional[str]:
        """Field entity_type"""
        return self._proto.entity_type



class ResolvedAlterExternalSchemaStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterExternalSchemaStmtProto"""

    def __init__(self, proto: 'ResolvedAlterExternalSchemaStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterIndexStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterIndexStmtProto"""

    def __init__(self, proto: 'ResolvedAlterIndexStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def table_name_path(self) -> List[str]:
        """Field table_name_path"""
        return self._proto.table_name_path

    @cached_property
    def index_type(self) -> Optional[int]:
        """Field index_type"""
        return self._proto.index_type

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan



class ResolvedAlterMaterializedViewStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterMaterializedViewStmtProto"""

    def __init__(self, proto: 'ResolvedAlterMaterializedViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterModelStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterModelStmtProto"""

    def __init__(self, proto: 'ResolvedAlterModelStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterPrivilegeRestrictionStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterPrivilegeRestrictionStmtProto"""

    def __init__(self, proto: 'ResolvedAlterPrivilegeRestrictionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column_privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field column_privilege_list"""
        return self._proto.column_privilege_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type



class ResolvedAlterRowAccessPolicyStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterRowAccessPolicyStmtProto"""

    def __init__(self, proto: 'ResolvedAlterRowAccessPolicyStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan



class ResolvedAlterSchemaStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterSchemaStmtProto"""

    def __init__(self, proto: 'ResolvedAlterSchemaStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterSequenceStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterSequenceStmtProto"""

    def __init__(self, proto: 'ResolvedAlterSequenceStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterSubEntityAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedAlterSubEntityActionProto"""

    def __init__(self, proto: 'ResolvedAlterSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def entity_type(self) -> Optional[str]:
        """Field entity_type"""
        return self._proto.entity_type

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def alter_action(self) -> Optional['AnyResolvedAlterActionProto']:
        """Field alter_action"""
        return self._proto.alter_action

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ResolvedAlterTableStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterTableStmtProto"""

    def __init__(self, proto: 'ResolvedAlterTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAlterViewStmt(ResolvedAlterObjectStmt):
    """Generated wrapper for ResolvedAlterViewStmtProto"""

    def __init__(self, proto: 'ResolvedAlterViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def alter_action_list(self) -> List['AnyResolvedAlterActionProto']:
        """Field alter_action_list"""
        return self._proto.parent.alter_action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ResolvedAnonymizedAggregateScan(ResolvedAggregateScanBase):
    """Generated wrapper for ResolvedAnonymizedAggregateScanProto"""

    def __init__(self, proto: 'ResolvedAnonymizedAggregateScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.parent.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.parent.group_by_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.parent.aggregate_list

    @cached_property
    def grouping_set_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field grouping_set_list"""
        return self._proto.parent.grouping_set_list

    @cached_property
    def rollup_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field rollup_column_list"""
        return self._proto.parent.rollup_column_list

    @cached_property
    def grouping_call_list(self) -> List['ResolvedGroupingCallProto']:
        """Field grouping_call_list"""
        return self._proto.parent.grouping_call_list

    @cached_property
    def k_threshold_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field k_threshold_expr"""
        return self._proto.k_threshold_expr

    @cached_property
    def anonymization_option_list(self) -> List['ResolvedOptionProto']:
        """Field anonymization_option_list"""
        return self._proto.anonymization_option_list



class ResolvedCheckConstraint(ResolvedConstraint):
    """Generated wrapper for ResolvedCheckConstraintProto"""

    def __init__(self, proto: 'ResolvedCheckConstraintProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional[str]:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def expression(self) -> Optional['AnyResolvedExprProto']:
        """Field expression"""
        return self._proto.expression

    @cached_property
    def enforced(self) -> Optional[bool]:
        """Field enforced"""
        return self._proto.enforced

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedComputedColumnImpl(ResolvedComputedColumnBase):
    """Generated wrapper for ResolvedComputedColumnImplProto"""

    def __init__(self, proto: 'ResolvedComputedColumnImplProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range



class ResolvedCreateConnectionStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateConnectionStmtProto"""

    def __init__(self, proto: 'ResolvedCreateConnectionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateConstantStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateConstantStmtProto"""

    def __init__(self, proto: 'ResolvedCreateConstantStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedCreateEntityStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateEntityStmtProto"""

    def __init__(self, proto: 'ResolvedCreateEntityStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def entity_type(self) -> Optional[str]:
        """Field entity_type"""
        return self._proto.entity_type

    @cached_property
    def entity_body_json(self) -> Optional[str]:
        """Field entity_body_json"""
        return self._proto.entity_body_json

    @cached_property
    def entity_body_text(self) -> Optional[str]:
        """Field entity_body_text"""
        return self._proto.entity_body_text

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateFunctionStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateFunctionStmtProto"""

    def __init__(self, proto: 'ResolvedCreateFunctionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def has_explicit_return_type(self) -> Optional[bool]:
        """Field has_explicit_return_type"""
        return self._proto.has_explicit_return_type

    @cached_property
    def return_type(self) -> Optional['TypeProto']:
        """Field return_type"""
        return self._proto.return_type

    @cached_property
    def argument_name_list(self) -> List[str]:
        """Field argument_name_list"""
        return self._proto.argument_name_list

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def is_aggregate(self) -> Optional[bool]:
        """Field is_aggregate"""
        return self._proto.is_aggregate

    @cached_property
    def language(self) -> Optional[str]:
        """Field language"""
        return self._proto.language

    @cached_property
    def code(self) -> Optional[str]:
        """Field code"""
        return self._proto.code

    @cached_property
    def aggregate_expression_list(self) -> List['ResolvedComputedColumnProto']:
        """Field aggregate_expression_list"""
        return self._proto.aggregate_expression_list

    @cached_property
    def function_expression(self) -> Optional['AnyResolvedExprProto']:
        """Field function_expression"""
        return self._proto.function_expression

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security

    @cached_property
    def determinism_level(self) -> Optional[int]:
        """Field determinism_level"""
        return self._proto.determinism_level

    @cached_property
    def is_remote(self) -> Optional[bool]:
        """Field is_remote"""
        return self._proto.is_remote

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection



class ResolvedCreateIndexStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateIndexStmtProto"""

    def __init__(self, proto: 'ResolvedCreateIndexStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def table_name_path(self) -> List[str]:
        """Field table_name_path"""
        return self._proto.table_name_path

    @cached_property
    def table_scan(self) -> Optional['ResolvedTableScanProto']:
        """Field table_scan"""
        return self._proto.table_scan

    @cached_property
    def is_unique(self) -> Optional[bool]:
        """Field is_unique"""
        return self._proto.is_unique

    @cached_property
    def is_search(self) -> Optional[bool]:
        """Field is_search"""
        return self._proto.is_search

    @cached_property
    def is_vector(self) -> Optional[bool]:
        """Field is_vector"""
        return self._proto.is_vector

    @cached_property
    def index_all_columns(self) -> Optional[bool]:
        """Field index_all_columns"""
        return self._proto.index_all_columns

    @cached_property
    def index_item_list(self) -> List['ResolvedIndexItemProto']:
        """Field index_item_list"""
        return self._proto.index_item_list

    @cached_property
    def storing_expression_list(self) -> List['AnyResolvedExprProto']:
        """Field storing_expression_list"""
        return self._proto.storing_expression_list

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def computed_columns_list(self) -> List['ResolvedComputedColumnProto']:
        """Field computed_columns_list"""
        return self._proto.computed_columns_list

    @cached_property
    def unnest_expressions_list(self) -> List['ResolvedUnnestItemProto']:
        """Field unnest_expressions_list"""
        return self._proto.unnest_expressions_list



class ResolvedCreateModelStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateModelStmtProto"""

    def __init__(self, proto: 'ResolvedCreateModelStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def aliased_query_list(self) -> List['ResolvedCreateModelAliasedQueryProto']:
        """Field aliased_query_list"""
        return self._proto.aliased_query_list

    @cached_property
    def transform_input_column_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field transform_input_column_list"""
        return self._proto.transform_input_column_list

    @cached_property
    def transform_list(self) -> List['ResolvedComputedColumnProto']:
        """Field transform_list"""
        return self._proto.transform_list

    @cached_property
    def transform_output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field transform_output_column_list"""
        return self._proto.transform_output_column_list

    @cached_property
    def transform_analytic_function_group_list(self) -> List['ResolvedAnalyticFunctionGroupProto']:
        """Field transform_analytic_function_group_list"""
        return self._proto.transform_analytic_function_group_list

    @cached_property
    def input_column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field input_column_definition_list"""
        return self._proto.input_column_definition_list

    @cached_property
    def output_column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field output_column_definition_list"""
        return self._proto.output_column_definition_list

    @cached_property
    def is_remote(self) -> Optional[bool]:
        """Field is_remote"""
        return self._proto.is_remote

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection



class ResolvedCreatePrivilegeRestrictionStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreatePrivilegeRestrictionStmtProto"""

    def __init__(self, proto: 'ResolvedCreatePrivilegeRestrictionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def column_privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field column_privilege_list"""
        return self._proto.column_privilege_list

    @cached_property
    def object_type(self) -> Optional[str]:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def restrictee_list(self) -> List['AnyResolvedExprProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ResolvedCreateProcedureStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateProcedureStmtProto"""

    def __init__(self, proto: 'ResolvedCreateProcedureStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def argument_name_list(self) -> List[str]:
        """Field argument_name_list"""
        return self._proto.argument_name_list

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def procedure_body(self) -> Optional[str]:
        """Field procedure_body"""
        return self._proto.procedure_body

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection

    @cached_property
    def language(self) -> Optional[str]:
        """Field language"""
        return self._proto.language

    @cached_property
    def code(self) -> Optional[str]:
        """Field code"""
        return self._proto.code

    @cached_property
    def external_security(self) -> Optional[int]:
        """Field external_security"""
        return self._proto.external_security



class ResolvedCreatePropertyGraphStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreatePropertyGraphStmtProto"""

    def __init__(self, proto: 'ResolvedCreatePropertyGraphStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def node_table_list(self) -> List['ResolvedGraphElementTableProto']:
        """Field node_table_list"""
        return self._proto.node_table_list

    @cached_property
    def edge_table_list(self) -> List['ResolvedGraphElementTableProto']:
        """Field edge_table_list"""
        return self._proto.edge_table_list

    @cached_property
    def label_list(self) -> List['ResolvedGraphElementLabelProto']:
        """Field label_list"""
        return self._proto.label_list

    @cached_property
    def property_declaration_list(self) -> List['ResolvedGraphPropertyDeclarationProto']:
        """Field property_declaration_list"""
        return self._proto.property_declaration_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateSchemaStmtBase(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateSchemaStmtBaseProto"""

    def __init__(self, proto: 'ResolvedCreateSchemaStmtBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateSequenceStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateSequenceStmtProto"""

    def __init__(self, proto: 'ResolvedCreateSequenceStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateSnapshotTableStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateSnapshotTableStmtProto"""

    def __init__(self, proto: 'ResolvedCreateSnapshotTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def clone_from(self) -> Optional['AnyResolvedScanProto']:
        """Field clone_from"""
        return self._proto.clone_from

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedCreateTableFunctionStmt(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateTableFunctionStmtProto"""

    def __init__(self, proto: 'ResolvedCreateTableFunctionStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def argument_name_list(self) -> List[str]:
        """Field argument_name_list"""
        return self._proto.argument_name_list

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.signature

    @cached_property
    def has_explicit_return_schema(self) -> Optional[bool]:
        """Field has_explicit_return_schema"""
        return self._proto.has_explicit_return_schema

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def language(self) -> Optional[str]:
        """Field language"""
        return self._proto.language

    @cached_property
    def code(self) -> Optional[str]:
        """Field code"""
        return self._proto.code

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security



class ResolvedCreateTableStmtBase(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateTableStmtBaseProto"""

    def __init__(self, proto: 'ResolvedCreateTableStmtBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.column_definition_list

    @cached_property
    def pseudo_column_list(self) -> List['ResolvedColumnProto']:
        """Field pseudo_column_list"""
        return self._proto.pseudo_column_list

    @cached_property
    def primary_key(self) -> Optional['ResolvedPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.primary_key

    @cached_property
    def foreign_key_list(self) -> List['ResolvedForeignKeyProto']:
        """Field foreign_key_list"""
        return self._proto.foreign_key_list

    @cached_property
    def check_constraint_list(self) -> List['ResolvedCheckConstraintProto']:
        """Field check_constraint_list"""
        return self._proto.check_constraint_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def like_table(self) -> Optional['TableRefProto']:
        """Field like_table"""
        return self._proto.like_table

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.collation_name

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection



class ResolvedCreateViewBase(ResolvedCreateStatement):
    """Generated wrapper for ResolvedCreateViewBaseProto"""

    def __init__(self, proto: 'ResolvedCreateViewBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def has_explicit_columns(self) -> Optional[bool]:
        """Field has_explicit_columns"""
        return self._proto.has_explicit_columns

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.sql

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.is_value_table

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.recursive

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.column_definition_list



class ResolvedCube(ResolvedGroupingSetBase):
    """Generated wrapper for ResolvedCubeProto"""

    def __init__(self, proto: 'ResolvedCubeProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def cube_column_list(self) -> List['ResolvedGroupingSetMultiColumnProto']:
        """Field cube_column_list"""
        return self._proto.cube_column_list



class ResolvedDifferentialPrivacyAggregateScan(ResolvedAggregateScanBase):
    """Generated wrapper for ResolvedDifferentialPrivacyAggregateScanProto"""

    def __init__(self, proto: 'ResolvedDifferentialPrivacyAggregateScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.parent.input_scan

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.parent.group_by_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field aggregate_list"""
        return self._proto.parent.aggregate_list

    @cached_property
    def grouping_set_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field grouping_set_list"""
        return self._proto.parent.grouping_set_list

    @cached_property
    def rollup_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field rollup_column_list"""
        return self._proto.parent.rollup_column_list

    @cached_property
    def grouping_call_list(self) -> List['ResolvedGroupingCallProto']:
        """Field grouping_call_list"""
        return self._proto.parent.grouping_call_list

    @cached_property
    def group_selection_threshold_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field group_selection_threshold_expr"""
        return self._proto.group_selection_threshold_expr

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedDropColumnAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedDropColumnActionProto"""

    def __init__(self, proto: 'ResolvedDropColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class ResolvedDropConstraintAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedDropConstraintActionProto"""

    def __init__(self, proto: 'ResolvedDropConstraintActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class ResolvedDropPrimaryKeyAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedDropPrimaryKeyActionProto"""

    def __init__(self, proto: 'ResolvedDropPrimaryKeyActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ResolvedDropSubEntityAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedDropSubEntityActionProto"""

    def __init__(self, proto: 'ResolvedDropSubEntityActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def entity_type(self) -> Optional[str]:
        """Field entity_type"""
        return self._proto.entity_type

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists



class ResolvedFilterUsingAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedFilterUsingActionProto"""

    def __init__(self, proto: 'ResolvedFilterUsingActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def predicate(self) -> Optional['AnyResolvedExprProto']:
        """Field predicate"""
        return self._proto.predicate

    @cached_property
    def predicate_str(self) -> Optional[str]:
        """Field predicate_str"""
        return self._proto.predicate_str



class ResolvedForeignKey(ResolvedConstraint):
    """Generated wrapper for ResolvedForeignKeyProto"""

    def __init__(self, proto: 'ResolvedForeignKeyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def constraint_name(self) -> Optional[str]:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def referencing_column_offset_list(self) -> List[int]:
        """Field referencing_column_offset_list"""
        return self._proto.referencing_column_offset_list

    @cached_property
    def referenced_table(self) -> Optional['TableRefProto']:
        """Field referenced_table"""
        return self._proto.referenced_table

    @cached_property
    def referenced_column_offset_list(self) -> List[int]:
        """Field referenced_column_offset_list"""
        return self._proto.referenced_column_offset_list

    @cached_property
    def match_mode(self) -> Optional[int]:
        """Field match_mode"""
        return self._proto.match_mode

    @cached_property
    def update_action(self) -> Optional[int]:
        """Field update_action"""
        return self._proto.update_action

    @cached_property
    def delete_action(self) -> Optional[int]:
        """Field delete_action"""
        return self._proto.delete_action

    @cached_property
    def enforced(self) -> Optional[bool]:
        """Field enforced"""
        return self._proto.enforced

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def referencing_column_list(self) -> List[str]:
        """Field referencing_column_list"""
        return self._proto.referencing_column_list



class ResolvedFunctionCall(ResolvedFunctionCallBase):
    """Generated wrapper for ResolvedFunctionCallProto"""

    def __init__(self, proto: 'ResolvedFunctionCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.parent.type_annotation_map

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.parent.function

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.parent.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.parent.argument_list

    @cached_property
    def generic_argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field generic_argument_list"""
        return self._proto.parent.generic_argument_list

    @cached_property
    def error_mode(self) -> Optional[int]:
        """Field error_mode"""
        return self._proto.parent.error_mode

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def function_call_info(self) -> Optional['ResolvedFunctionCallInfoProto']:
        """Field function_call_info"""
        return self._proto.function_call_info



class ResolvedGrantStmt(ResolvedGrantOrRevokeStmt):
    """Generated wrapper for ResolvedGrantStmtProto"""

    def __init__(self, proto: 'ResolvedGrantStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field privilege_list"""
        return self._proto.parent.privilege_list

    @cached_property
    def object_type_list(self) -> List[str]:
        """Field object_type_list"""
        return self._proto.parent.object_type_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def grantee_list(self) -> List[str]:
        """Field grantee_list"""
        return self._proto.parent.grantee_list

    @cached_property
    def grantee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field grantee_expr_list"""
        return self._proto.parent.grantee_expr_list



class ResolvedGrantToAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedGrantToActionProto"""

    def __init__(self, proto: 'ResolvedGrantToActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def grantee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field grantee_expr_list"""
        return self._proto.grantee_expr_list



class ResolvedGraphElementScan(ResolvedGraphPathScanBase):
    """Generated wrapper for ResolvedGraphElementScanProto"""

    def __init__(self, proto: 'ResolvedGraphElementScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.filter_expr

    @cached_property
    def label_expr(self) -> Optional['AnyResolvedGraphLabelExprProto']:
        """Field label_expr"""
        return self._proto.label_expr

    @cached_property
    def target_element_table_list(self) -> List['GraphElementTableRefProto']:
        """Field target_element_table_list"""
        return self._proto.target_element_table_list



class ResolvedGraphLabelNaryExpr(ResolvedGraphLabelExpr):
    """Generated wrapper for ResolvedGraphLabelNaryExprProto"""

    def __init__(self, proto: 'ResolvedGraphLabelNaryExprProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def op(self) -> Optional[int]:
        """Field op"""
        return self._proto.op

    @cached_property
    def operand_list(self) -> List['AnyResolvedGraphLabelExprProto']:
        """Field operand_list"""
        return self._proto.operand_list



class ResolvedGraphLabel(ResolvedGraphLabelExpr):
    """Generated wrapper for ResolvedGraphLabelProto"""

    def __init__(self, proto: 'ResolvedGraphLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['GraphElementLabelRefProto']:
        """Field label"""
        return self._proto.label

    @cached_property
    def label_name(self) -> Optional['AnyResolvedExprProto']:
        """Field label_name"""
        return self._proto.label_name



class ResolvedGraphLinearScan(ResolvedGraphScanBase):
    """Generated wrapper for ResolvedGraphLinearScanProto"""

    def __init__(self, proto: 'ResolvedGraphLinearScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def scan_list(self) -> List['AnyResolvedScanProto']:
        """Field scan_list"""
        return self._proto.scan_list



class ResolvedGraphPathScan(ResolvedGraphPathScanBase):
    """Generated wrapper for ResolvedGraphPathScanProto"""

    def __init__(self, proto: 'ResolvedGraphPathScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan_list(self) -> List['AnyResolvedGraphPathScanBaseProto']:
        """Field input_scan_list"""
        return self._proto.input_scan_list

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.filter_expr

    @cached_property
    def path(self) -> Optional['ResolvedColumnHolderProto']:
        """Field path"""
        return self._proto.path

    @cached_property
    def head(self) -> Optional['ResolvedColumnProto']:
        """Field head"""
        return self._proto.head

    @cached_property
    def tail(self) -> Optional['ResolvedColumnProto']:
        """Field tail"""
        return self._proto.tail

    @cached_property
    def path_hint_list(self) -> List['ResolvedOptionProto']:
        """Field path_hint_list"""
        return self._proto.path_hint_list

    @cached_property
    def quantifier(self) -> Optional['ResolvedGraphPathPatternQuantifierProto']:
        """Field quantifier"""
        return self._proto.quantifier

    @cached_property
    def group_variable_list(self) -> List['ResolvedGraphMakeArrayVariableProto']:
        """Field group_variable_list"""
        return self._proto.group_variable_list

    @cached_property
    def path_mode(self) -> Optional['ResolvedGraphPathModeProto']:
        """Field path_mode"""
        return self._proto.path_mode

    @cached_property
    def search_prefix(self) -> Optional['ResolvedGraphPathSearchPrefixProto']:
        """Field search_prefix"""
        return self._proto.search_prefix

    @cached_property
    def path_cost(self) -> Optional['ResolvedGraphPathCostProto']:
        """Field path_cost"""
        return self._proto.path_cost



class ResolvedGraphScan(ResolvedGraphScanBase):
    """Generated wrapper for ResolvedGraphScanProto"""

    def __init__(self, proto: 'ResolvedGraphScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.node_source

    @cached_property
    def input_scan_list(self) -> List['ResolvedGraphPathScanProto']:
        """Field input_scan_list"""
        return self._proto.input_scan_list

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.filter_expr

    @cached_property
    def input_scan(self) -> Optional['AnyResolvedScanProto']:
        """Field input_scan"""
        return self._proto.input_scan

    @cached_property
    def optional(self) -> Optional[bool]:
        """Field optional"""
        return self._proto.optional



class ResolvedGraphWildCardLabel(ResolvedGraphLabelExpr):
    """Generated wrapper for ResolvedGraphWildCardLabelProto"""

    def __init__(self, proto: 'ResolvedGraphWildCardLabelProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range



class ResolvedGroupingSetList(ResolvedGroupingSetBase):
    """Generated wrapper for ResolvedGroupingSetListProto"""

    def __init__(self, proto: 'ResolvedGroupingSetListProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def elem_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field elem_list"""
        return self._proto.elem_list



class ResolvedGroupingSetProduct(ResolvedGroupingSetBase):
    """Generated wrapper for ResolvedGroupingSetProductProto"""

    def __init__(self, proto: 'ResolvedGroupingSetProductProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def input_list(self) -> List['AnyResolvedGroupingSetBaseProto']:
        """Field input_list"""
        return self._proto.input_list



class ResolvedGroupingSet(ResolvedGroupingSetBase):
    """Generated wrapper for ResolvedGroupingSetProto"""

    def __init__(self, proto: 'ResolvedGroupingSetProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def group_by_column_list(self) -> List['ResolvedColumnRefProto']:
        """Field group_by_column_list"""
        return self._proto.group_by_column_list



class ResolvedMatchRecognizePatternAnchor(ResolvedMatchRecognizePatternExpr):
    """Generated wrapper for ResolvedMatchRecognizePatternAnchorProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternAnchorProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def mode(self) -> Optional[int]:
        """Field mode"""
        return self._proto.mode



class ResolvedMatchRecognizePatternEmpty(ResolvedMatchRecognizePatternExpr):
    """Generated wrapper for ResolvedMatchRecognizePatternEmptyProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternEmptyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range



class ResolvedMatchRecognizePatternOperation(ResolvedMatchRecognizePatternExpr):
    """Generated wrapper for ResolvedMatchRecognizePatternOperationProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternOperationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def op_type(self) -> Optional[int]:
        """Field op_type"""
        return self._proto.op_type

    @cached_property
    def operand_list(self) -> List['AnyResolvedMatchRecognizePatternExprProto']:
        """Field operand_list"""
        return self._proto.operand_list



class ResolvedMatchRecognizePatternQuantification(ResolvedMatchRecognizePatternExpr):
    """Generated wrapper for ResolvedMatchRecognizePatternQuantificationProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternQuantificationProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def operand(self) -> Optional['AnyResolvedMatchRecognizePatternExprProto']:
        """Field operand"""
        return self._proto.operand

    @cached_property
    def lower_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field lower_bound"""
        return self._proto.lower_bound

    @cached_property
    def upper_bound(self) -> Optional['AnyResolvedExprProto']:
        """Field upper_bound"""
        return self._proto.upper_bound

    @cached_property
    def is_reluctant(self) -> Optional[bool]:
        """Field is_reluctant"""
        return self._proto.is_reluctant



class ResolvedMatchRecognizePatternVariableRef(ResolvedMatchRecognizePatternExpr):
    """Generated wrapper for ResolvedMatchRecognizePatternVariableRefProto"""

    def __init__(self, proto: 'ResolvedMatchRecognizePatternVariableRefProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name



class ResolvedNonScalarFunctionCallBase(ResolvedFunctionCallBase):
    """Generated wrapper for ResolvedNonScalarFunctionCallBaseProto"""

    def __init__(self, proto: 'ResolvedNonScalarFunctionCallBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.parent.type_annotation_map

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.parent.function

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.parent.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.parent.argument_list

    @cached_property
    def generic_argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field generic_argument_list"""
        return self._proto.parent.generic_argument_list

    @cached_property
    def error_mode(self) -> Optional[int]:
        """Field error_mode"""
        return self._proto.parent.error_mode

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.collation_list

    @cached_property
    def distinct(self) -> Optional[bool]:
        """Field distinct"""
        return self._proto.distinct

    @cached_property
    def null_handling_modifier(self) -> Optional[int]:
        """Field null_handling_modifier"""
        return self._proto.null_handling_modifier

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.where_expr



class ResolvedPrimaryKey(ResolvedConstraint):
    """Generated wrapper for ResolvedPrimaryKeyProto"""

    def __init__(self, proto: 'ResolvedPrimaryKeyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def column_offset_list(self) -> List[int]:
        """Field column_offset_list"""
        return self._proto.column_offset_list

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list

    @cached_property
    def unenforced(self) -> Optional[bool]:
        """Field unenforced"""
        return self._proto.unenforced

    @cached_property
    def constraint_name(self) -> Optional[str]:
        """Field constraint_name"""
        return self._proto.constraint_name

    @cached_property
    def column_name_list(self) -> List[str]:
        """Field column_name_list"""
        return self._proto.column_name_list



class ResolvedRebuildAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRebuildActionProto"""

    def __init__(self, proto: 'ResolvedRebuildActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range



class ResolvedRemoveFromRestricteeListAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRemoveFromRestricteeListActionProto"""

    def __init__(self, proto: 'ResolvedRemoveFromRestricteeListActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def restrictee_list(self) -> List['AnyResolvedExprProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ResolvedRenameColumnAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRenameColumnActionProto"""

    def __init__(self, proto: 'ResolvedRenameColumnActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.is_if_exists

    @cached_property
    def name(self) -> Optional[str]:
        """Field name"""
        return self._proto.name

    @cached_property
    def new_name(self) -> Optional[str]:
        """Field new_name"""
        return self._proto.new_name



class ResolvedRenameToAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRenameToActionProto"""

    def __init__(self, proto: 'ResolvedRenameToActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def new_path(self) -> List[str]:
        """Field new_path"""
        return self._proto.new_path



class ResolvedRestrictToAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRestrictToActionProto"""

    def __init__(self, proto: 'ResolvedRestrictToActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def restrictee_list(self) -> List['AnyResolvedExprProto']:
        """Field restrictee_list"""
        return self._proto.restrictee_list



class ResolvedRevokeFromAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedRevokeFromActionProto"""

    def __init__(self, proto: 'ResolvedRevokeFromActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def revokee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field revokee_expr_list"""
        return self._proto.revokee_expr_list

    @cached_property
    def is_revoke_from_all(self) -> Optional[bool]:
        """Field is_revoke_from_all"""
        return self._proto.is_revoke_from_all



class ResolvedRevokeStmt(ResolvedGrantOrRevokeStmt):
    """Generated wrapper for ResolvedRevokeStmtProto"""

    def __init__(self, proto: 'ResolvedRevokeStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def privilege_list(self) -> List['ResolvedPrivilegeProto']:
        """Field privilege_list"""
        return self._proto.parent.privilege_list

    @cached_property
    def object_type_list(self) -> List[str]:
        """Field object_type_list"""
        return self._proto.parent.object_type_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.name_path

    @cached_property
    def grantee_list(self) -> List[str]:
        """Field grantee_list"""
        return self._proto.parent.grantee_list

    @cached_property
    def grantee_expr_list(self) -> List['AnyResolvedExprProto']:
        """Field grantee_expr_list"""
        return self._proto.parent.grantee_expr_list



class ResolvedRollup(ResolvedGroupingSetBase):
    """Generated wrapper for ResolvedRollupProto"""

    def __init__(self, proto: 'ResolvedRollupProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def rollup_column_list(self) -> List['ResolvedGroupingSetMultiColumnProto']:
        """Field rollup_column_list"""
        return self._proto.rollup_column_list



class ResolvedSetAsAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedSetAsActionProto"""

    def __init__(self, proto: 'ResolvedSetAsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def entity_body_json(self) -> Optional[str]:
        """Field entity_body_json"""
        return self._proto.entity_body_json

    @cached_property
    def entity_body_text(self) -> Optional[str]:
        """Field entity_body_text"""
        return self._proto.entity_body_text



class ResolvedSetCollateClause(ResolvedAlterAction):
    """Generated wrapper for ResolvedSetCollateClauseProto"""

    def __init__(self, proto: 'ResolvedSetCollateClauseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.collation_name



class ResolvedSetOptionsAction(ResolvedAlterAction):
    """Generated wrapper for ResolvedSetOptionsActionProto"""

    def __init__(self, proto: 'ResolvedSetOptionsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parse_location_range

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ASTAlterApproxViewStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterApproxViewStatementProto"""

    def __init__(self, proto: 'ASTAlterApproxViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterConnectionStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterConnectionStatementProto"""

    def __init__(self, proto: 'ASTAlterConnectionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterDatabaseStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterDatabaseStatementProto"""

    def __init__(self, proto: 'ASTAlterDatabaseStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterEntityStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterEntityStatementProto"""

    def __init__(self, proto: 'ASTAlterEntityStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def type(self) -> Optional['ASTIdentifierProto']:
        """Field type"""
        return self._proto.type



class ASTAlterExternalSchemaStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterExternalSchemaStatementProto"""

    def __init__(self, proto: 'ASTAlterExternalSchemaStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterIndexStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterIndexStatementProto"""

    def __init__(self, proto: 'ASTAlterIndexStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def index_type(self) -> Optional[int]:
        """Field index_type"""
        return self._proto.index_type



class ASTAlterMaterializedViewStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterMaterializedViewStatementProto"""

    def __init__(self, proto: 'ASTAlterMaterializedViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterModelStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterModelStatementProto"""

    def __init__(self, proto: 'ASTAlterModelStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterPrivilegeRestrictionStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterPrivilegeRestrictionStatementProto"""

    def __init__(self, proto: 'ASTAlterPrivilegeRestrictionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def privileges(self) -> Optional['ASTPrivilegesProto']:
        """Field privileges"""
        return self._proto.privileges

    @cached_property
    def object_type(self) -> Optional['ASTIdentifierProto']:
        """Field object_type"""
        return self._proto.object_type



class ASTAlterRowAccessPolicyStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterRowAccessPolicyStatementProto"""

    def __init__(self, proto: 'ASTAlterRowAccessPolicyStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def name(self) -> Optional['ASTIdentifierProto']:
        """Field name"""
        return self._proto.name



class ASTAlterSchemaStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterSchemaStatementProto"""

    def __init__(self, proto: 'ASTAlterSchemaStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterSequenceStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterSequenceStatementProto"""

    def __init__(self, proto: 'ASTAlterSequenceStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterTableStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterTableStatementProto"""

    def __init__(self, proto: 'ASTAlterTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTAlterViewStatement(ASTAlterStatementBase):
    """Generated wrapper for ASTAlterViewStatementProto"""

    def __init__(self, proto: 'ASTAlterViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def path(self) -> Optional['ASTPathExpressionProto']:
        """Field path"""
        return self._proto.parent.path

    @cached_property
    def action_list(self) -> Optional['ASTAlterActionListProto']:
        """Field action_list"""
        return self._proto.parent.action_list

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTBooleanLiteral(ASTPrintableLeaf):
    """Generated wrapper for ASTBooleanLiteralProto"""

    def __init__(self, proto: 'ASTBooleanLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image

    @cached_property
    def value(self) -> Optional[bool]:
        """Field value"""
        return self._proto.value



class ASTBreakStatement(ASTBreakContinueStatement):
    """Generated wrapper for ASTBreakStatementProto"""

    def __init__(self, proto: 'ASTBreakStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.parent.label

    @cached_property
    def keyword(self) -> Optional[int]:
        """Field keyword"""
        return self._proto.keyword



class ASTBytesLiteralComponent(ASTPrintableLeaf):
    """Generated wrapper for ASTBytesLiteralComponentProto"""

    def __init__(self, proto: 'ASTBytesLiteralComponentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTContinueStatement(ASTBreakContinueStatement):
    """Generated wrapper for ASTContinueStatementProto"""

    def __init__(self, proto: 'ASTContinueStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.parent.label

    @cached_property
    def keyword(self) -> Optional[int]:
        """Field keyword"""
        return self._proto.keyword



class ASTCreateConnectionStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateConnectionStatementProto"""

    def __init__(self, proto: 'ASTCreateConnectionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateConstantStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateConstantStatementProto"""

    def __init__(self, proto: 'ASTCreateConstantStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def expr(self) -> Optional['AnyASTExpressionProto']:
        """Field expr"""
        return self._proto.expr



class ASTCreateEntityStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateEntityStatementProto"""

    def __init__(self, proto: 'ASTCreateEntityStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def type(self) -> Optional['ASTIdentifierProto']:
        """Field type"""
        return self._proto.type

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def json_body(self) -> Optional['ASTJSONLiteralProto']:
        """Field json_body"""
        return self._proto.json_body

    @cached_property
    def text_body(self) -> Optional['ASTStringLiteralProto']:
        """Field text_body"""
        return self._proto.text_body



class ASTCreateFunctionStmtBase(ASTCreateStatement):
    """Generated wrapper for ASTCreateFunctionStmtBaseProto"""

    def __init__(self, proto: 'ASTCreateFunctionStmtBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def function_declaration(self) -> Optional['ASTFunctionDeclarationProto']:
        """Field function_declaration"""
        return self._proto.function_declaration

    @cached_property
    def language(self) -> Optional['ASTIdentifierProto']:
        """Field language"""
        return self._proto.language

    @cached_property
    def code(self) -> Optional['ASTStringLiteralProto']:
        """Field code"""
        return self._proto.code

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def determinism_level(self) -> Optional[int]:
        """Field determinism_level"""
        return self._proto.determinism_level

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security



class ASTCreateIndexStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateIndexStatementProto"""

    def __init__(self, proto: 'ASTCreateIndexStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.table_name

    @cached_property
    def optional_table_alias(self) -> Optional['ASTAliasProto']:
        """Field optional_table_alias"""
        return self._proto.optional_table_alias

    @cached_property
    def optional_index_unnest_expression_list(self) -> Optional['ASTIndexUnnestExpressionListProto']:
        """Field optional_index_unnest_expression_list"""
        return self._proto.optional_index_unnest_expression_list

    @cached_property
    def index_item_list(self) -> Optional['ASTIndexItemListProto']:
        """Field index_item_list"""
        return self._proto.index_item_list

    @cached_property
    def optional_index_storing_expressions(self) -> Optional['ASTIndexStoringExpressionListProto']:
        """Field optional_index_storing_expressions"""
        return self._proto.optional_index_storing_expressions

    @cached_property
    def optional_partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field optional_partition_by"""
        return self._proto.optional_partition_by

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def is_unique(self) -> Optional[bool]:
        """Field is_unique"""
        return self._proto.is_unique

    @cached_property
    def is_search(self) -> Optional[bool]:
        """Field is_search"""
        return self._proto.is_search

    @cached_property
    def spanner_interleave_clause(self) -> Optional['ASTSpannerInterleaveClauseProto']:
        """Field spanner_interleave_clause"""
        return self._proto.spanner_interleave_clause

    @cached_property
    def spanner_is_null_filtered(self) -> Optional[bool]:
        """Field spanner_is_null_filtered"""
        return self._proto.spanner_is_null_filtered

    @cached_property
    def is_vector(self) -> Optional[bool]:
        """Field is_vector"""
        return self._proto.is_vector



class ASTCreateModelStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateModelStatementProto"""

    def __init__(self, proto: 'ASTCreateModelStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def transform_clause(self) -> Optional['ASTTransformClauseProto']:
        """Field transform_clause"""
        return self._proto.transform_clause

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def input_output_clause(self) -> Optional['ASTInputOutputClauseProto']:
        """Field input_output_clause"""
        return self._proto.input_output_clause

    @cached_property
    def is_remote(self) -> Optional[bool]:
        """Field is_remote"""
        return self._proto.is_remote

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause

    @cached_property
    def aliased_query_list(self) -> Optional['ASTAliasedQueryListProto']:
        """Field aliased_query_list"""
        return self._proto.aliased_query_list



class ASTCreatePrivilegeRestrictionStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreatePrivilegeRestrictionStatementProto"""

    def __init__(self, proto: 'ASTCreatePrivilegeRestrictionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def privileges(self) -> Optional['ASTPrivilegesProto']:
        """Field privileges"""
        return self._proto.privileges

    @cached_property
    def object_type(self) -> Optional['ASTIdentifierProto']:
        """Field object_type"""
        return self._proto.object_type

    @cached_property
    def name_path(self) -> Optional['ASTPathExpressionProto']:
        """Field name_path"""
        return self._proto.name_path

    @cached_property
    def restrict_to(self) -> Optional['ASTRestrictToClauseProto']:
        """Field restrict_to"""
        return self._proto.restrict_to



class ASTCreateProcedureStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateProcedureStatementProto"""

    def __init__(self, proto: 'ASTCreateProcedureStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def parameters(self) -> Optional['ASTFunctionParametersProto']:
        """Field parameters"""
        return self._proto.parameters

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def body(self) -> Optional['ASTScriptProto']:
        """Field body"""
        return self._proto.body

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause

    @cached_property
    def language(self) -> Optional['ASTIdentifierProto']:
        """Field language"""
        return self._proto.language

    @cached_property
    def code(self) -> Optional['ASTStringLiteralProto']:
        """Field code"""
        return self._proto.code

    @cached_property
    def external_security(self) -> Optional[int]:
        """Field external_security"""
        return self._proto.external_security



class ASTCreatePropertyGraphStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreatePropertyGraphStatementProto"""

    def __init__(self, proto: 'ASTCreatePropertyGraphStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def node_table_list(self) -> Optional['ASTGraphElementTableListProto']:
        """Field node_table_list"""
        return self._proto.node_table_list

    @cached_property
    def edge_table_list(self) -> Optional['ASTGraphElementTableListProto']:
        """Field edge_table_list"""
        return self._proto.edge_table_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateRowAccessPolicyStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateRowAccessPolicyStatementProto"""

    def __init__(self, proto: 'ASTCreateRowAccessPolicyStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def target_path(self) -> Optional['ASTPathExpressionProto']:
        """Field target_path"""
        return self._proto.target_path

    @cached_property
    def grant_to(self) -> Optional['ASTGrantToClauseProto']:
        """Field grant_to"""
        return self._proto.grant_to

    @cached_property
    def filter_using(self) -> Optional['ASTFilterUsingClauseProto']:
        """Field filter_using"""
        return self._proto.filter_using

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def has_access_keyword(self) -> Optional[bool]:
        """Field has_access_keyword"""
        return self._proto.has_access_keyword



class ASTCreateSchemaStmtBase(ASTCreateStatement):
    """Generated wrapper for ASTCreateSchemaStmtBaseProto"""

    def __init__(self, proto: 'ASTCreateSchemaStmtBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateSequenceStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateSequenceStatementProto"""

    def __init__(self, proto: 'ASTCreateSequenceStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateSnapshotStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateSnapshotStatementProto"""

    def __init__(self, proto: 'ASTCreateSnapshotStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def schema_object_kind(self) -> Optional[int]:
        """Field schema_object_kind"""
        return self._proto.schema_object_kind

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def clone_data_source(self) -> Optional['ASTCloneDataSourceProto']:
        """Field clone_data_source"""
        return self._proto.clone_data_source

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateSnapshotTableStatement(ASTCreateStatement):
    """Generated wrapper for ASTCreateSnapshotTableStatementProto"""

    def __init__(self, proto: 'ASTCreateSnapshotTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def clone_data_source(self) -> Optional['ASTCloneDataSourceProto']:
        """Field clone_data_source"""
        return self._proto.clone_data_source

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list



class ASTCreateTableStmtBase(ASTCreateStatement):
    """Generated wrapper for ASTCreateTableStmtBaseProto"""

    def __init__(self, proto: 'ASTCreateTableStmtBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def table_element_list(self) -> Optional['ASTTableElementListProto']:
        """Field table_element_list"""
        return self._proto.table_element_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def like_table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field like_table_name"""
        return self._proto.like_table_name

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause



class ASTCreateViewStatementBase(ASTCreateStatement):
    """Generated wrapper for ASTCreateViewStatementBaseProto"""

    def __init__(self, proto: 'ASTCreateViewStatementBaseProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.name

    @cached_property
    def column_with_options_list(self) -> Optional['ASTColumnWithOptionsListProto']:
        """Field column_with_options_list"""
        return self._proto.column_with_options_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.sql_security

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.recursive



class ASTDropSearchIndexStatement(ASTDropIndexStatement):
    """Generated wrapper for ASTDropSearchIndexStatementProto"""

    def __init__(self, proto: 'ASTDropSearchIndexStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.parent.table_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTDropVectorIndexStatement(ASTDropIndexStatement):
    """Generated wrapper for ASTDropVectorIndexStatementProto"""

    def __init__(self, proto: 'ASTDropVectorIndexStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field table_name"""
        return self._proto.parent.table_name

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists



class ASTFloatLiteral(ASTPrintableLeaf):
    """Generated wrapper for ASTFloatLiteralProto"""

    def __init__(self, proto: 'ASTFloatLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTForInStatement(ASTLoopStatement):
    """Generated wrapper for ASTForInStatementProto"""

    def __init__(self, proto: 'ASTForInStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.parent.label

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.parent.body

    @cached_property
    def variable(self) -> Optional['ASTIdentifierProto']:
        """Field variable"""
        return self._proto.variable

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query



class ASTIndexAllColumns(ASTPrintableLeaf):
    """Generated wrapper for ASTIndexAllColumnsProto"""

    def __init__(self, proto: 'ASTIndexAllColumnsProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image

    @cached_property
    def column_options(self) -> Optional['ASTIndexItemListProto']:
        """Field column_options"""
        return self._proto.column_options



class ASTIntLiteral(ASTPrintableLeaf):
    """Generated wrapper for ASTIntLiteralProto"""

    def __init__(self, proto: 'ASTIntLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTMacroBody(ASTPrintableLeaf):
    """Generated wrapper for ASTMacroBodyProto"""

    def __init__(self, proto: 'ASTMacroBodyProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTMaxLiteral(ASTPrintableLeaf):
    """Generated wrapper for ASTMaxLiteralProto"""

    def __init__(self, proto: 'ASTMaxLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTNullLiteral(ASTPrintableLeaf):
    """Generated wrapper for ASTNullLiteralProto"""

    def __init__(self, proto: 'ASTNullLiteralProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTRepeatStatement(ASTLoopStatement):
    """Generated wrapper for ASTRepeatStatementProto"""

    def __init__(self, proto: 'ASTRepeatStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.parent.label

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.parent.body

    @cached_property
    def until_clause(self) -> Optional['ASTUntilClauseProto']:
        """Field until_clause"""
        return self._proto.until_clause



class ASTStar(ASTPrintableLeaf):
    """Generated wrapper for ASTStarProto"""

    def __init__(self, proto: 'ASTStarProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image



class ASTStringLiteralComponent(ASTPrintableLeaf):
    """Generated wrapper for ASTStringLiteralComponentProto"""

    def __init__(self, proto: 'ASTStringLiteralComponentProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def parenthesized(self) -> Optional[bool]:
        """Field parenthesized"""
        return self._proto.parent.parent.parent.parenthesized

    @cached_property
    def image(self) -> Optional[str]:
        """Field image"""
        return self._proto.parent.image

    @cached_property
    def string_value(self) -> Optional[str]:
        """Field string_value"""
        return self._proto.string_value



class ASTWhileStatement(ASTLoopStatement):
    """Generated wrapper for ASTWhileStatementProto"""

    def __init__(self, proto: 'ASTWhileStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def label(self) -> Optional['ASTLabelProto']:
        """Field label"""
        return self._proto.parent.label

    @cached_property
    def body(self) -> Optional['ASTStatementListProto']:
        """Field body"""
        return self._proto.parent.body

    @cached_property
    def condition(self) -> Optional['AnyASTExpressionProto']:
        """Field condition"""
        return self._proto.condition



class ResolvedAggregateFunctionCall(ResolvedNonScalarFunctionCallBase):
    """Generated wrapper for ResolvedAggregateFunctionCallProto"""

    def __init__(self, proto: 'ResolvedAggregateFunctionCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.parent.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.parent.parent.type_annotation_map

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.parent.parent.function

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.parent.parent.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.parent.parent.argument_list

    @cached_property
    def generic_argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field generic_argument_list"""
        return self._proto.parent.parent.generic_argument_list

    @cached_property
    def error_mode(self) -> Optional[int]:
        """Field error_mode"""
        return self._proto.parent.parent.error_mode

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.parent.collation_list

    @cached_property
    def distinct(self) -> Optional[bool]:
        """Field distinct"""
        return self._proto.parent.distinct

    @cached_property
    def null_handling_modifier(self) -> Optional[int]:
        """Field null_handling_modifier"""
        return self._proto.parent.null_handling_modifier

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.parent.where_expr

    @cached_property
    def having_modifier(self) -> Optional['ResolvedAggregateHavingModifierProto']:
        """Field having_modifier"""
        return self._proto.having_modifier

    @cached_property
    def order_by_item_list(self) -> List['ResolvedOrderByItemProto']:
        """Field order_by_item_list"""
        return self._proto.order_by_item_list

    @cached_property
    def limit(self) -> Optional['AnyResolvedExprProto']:
        """Field limit"""
        return self._proto.limit

    @cached_property
    def function_call_info(self) -> Optional['ResolvedFunctionCallInfoProto']:
        """Field function_call_info"""
        return self._proto.function_call_info

    @cached_property
    def group_by_list(self) -> List['ResolvedComputedColumnProto']:
        """Field group_by_list"""
        return self._proto.group_by_list

    @cached_property
    def group_by_hint_list(self) -> List['ResolvedOptionProto']:
        """Field group_by_hint_list"""
        return self._proto.group_by_hint_list

    @cached_property
    def group_by_aggregate_list(self) -> List['AnyResolvedComputedColumnBaseProto']:
        """Field group_by_aggregate_list"""
        return self._proto.group_by_aggregate_list

    @cached_property
    def having_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field having_expr"""
        return self._proto.having_expr



class ResolvedAlterColumnDropDefaultAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnDropDefaultActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnDropDefaultActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column



class ResolvedAlterColumnDropGeneratedAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnDropGeneratedActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnDropGeneratedActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column



class ResolvedAlterColumnDropNotNullAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnDropNotNullActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnDropNotNullActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column



class ResolvedAlterColumnOptionsAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnOptionsActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnOptionsActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.option_list



class ResolvedAlterColumnSetDataTypeAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnSetDataTypeActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnSetDataTypeActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column

    @cached_property
    def updated_type(self) -> Optional['TypeProto']:
        """Field updated_type"""
        return self._proto.updated_type

    @cached_property
    def updated_type_parameters(self) -> Optional['TypeParametersProto']:
        """Field updated_type_parameters"""
        return self._proto.updated_type_parameters

    @cached_property
    def updated_annotations(self) -> Optional['ResolvedColumnAnnotationsProto']:
        """Field updated_annotations"""
        return self._proto.updated_annotations



class ResolvedAlterColumnSetDefaultAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnSetDefaultActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnSetDefaultActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column

    @cached_property
    def default_value(self) -> Optional['ResolvedColumnDefaultValueProto']:
        """Field default_value"""
        return self._proto.default_value



class ResolvedAlterColumnSetGeneratedAction(ResolvedAlterColumnAction):
    """Generated wrapper for ResolvedAlterColumnSetGeneratedActionProto"""

    def __init__(self, proto: 'ResolvedAlterColumnSetGeneratedActionProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def is_if_exists(self) -> Optional[bool]:
        """Field is_if_exists"""
        return self._proto.parent.is_if_exists

    @cached_property
    def column(self) -> Optional[str]:
        """Field column"""
        return self._proto.parent.column

    @cached_property
    def generated_column_info(self) -> Optional['ResolvedGeneratedColumnInfoProto']:
        """Field generated_column_info"""
        return self._proto.generated_column_info



class ResolvedAnalyticFunctionCall(ResolvedNonScalarFunctionCallBase):
    """Generated wrapper for ResolvedAnalyticFunctionCallProto"""

    def __init__(self, proto: 'ResolvedAnalyticFunctionCallProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def type(self) -> Optional['TypeProto']:
        """Field type"""
        return self._proto.parent.parent.parent.type

    @cached_property
    def type_annotation_map(self) -> Optional['AnnotationMapProto']:
        """Field type_annotation_map"""
        return self._proto.parent.parent.parent.type_annotation_map

    @cached_property
    def function(self) -> Optional['FunctionRefProto']:
        """Field function"""
        return self._proto.parent.parent.function

    @cached_property
    def signature(self) -> Optional['FunctionSignatureProto']:
        """Field signature"""
        return self._proto.parent.parent.signature

    @cached_property
    def argument_list(self) -> List['AnyResolvedExprProto']:
        """Field argument_list"""
        return self._proto.parent.parent.argument_list

    @cached_property
    def generic_argument_list(self) -> List['ResolvedFunctionArgumentProto']:
        """Field generic_argument_list"""
        return self._proto.parent.parent.generic_argument_list

    @cached_property
    def error_mode(self) -> Optional[int]:
        """Field error_mode"""
        return self._proto.parent.parent.error_mode

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.hint_list

    @cached_property
    def collation_list(self) -> List['ResolvedCollationProto']:
        """Field collation_list"""
        return self._proto.parent.parent.collation_list

    @cached_property
    def distinct(self) -> Optional[bool]:
        """Field distinct"""
        return self._proto.parent.distinct

    @cached_property
    def null_handling_modifier(self) -> Optional[int]:
        """Field null_handling_modifier"""
        return self._proto.parent.null_handling_modifier

    @cached_property
    def where_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field where_expr"""
        return self._proto.parent.where_expr

    @cached_property
    def window_frame(self) -> Optional['ResolvedWindowFrameProto']:
        """Field window_frame"""
        return self._proto.window_frame



class ResolvedComputedColumn(ResolvedComputedColumnImpl):
    """Generated wrapper for ResolvedComputedColumnProto"""

    def __init__(self, proto: 'ResolvedComputedColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr



class ResolvedCreateApproxViewStmt(ResolvedCreateViewBase):
    """Generated wrapper for ResolvedCreateApproxViewStmtProto"""

    def __init__(self, proto: 'ResolvedCreateApproxViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.parent.output_column_list

    @cached_property
    def has_explicit_columns(self) -> Optional[bool]:
        """Field has_explicit_columns"""
        return self._proto.parent.has_explicit_columns

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.parent.sql

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list



class ResolvedCreateExternalSchemaStmt(ResolvedCreateSchemaStmtBase):
    """Generated wrapper for ResolvedCreateExternalSchemaStmtProto"""

    def __init__(self, proto: 'ResolvedCreateExternalSchemaStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.connection



class ResolvedCreateExternalTableStmt(ResolvedCreateTableStmtBase):
    """Generated wrapper for ResolvedCreateExternalTableStmtProto"""

    def __init__(self, proto: 'ResolvedCreateExternalTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list

    @cached_property
    def pseudo_column_list(self) -> List['ResolvedColumnProto']:
        """Field pseudo_column_list"""
        return self._proto.parent.pseudo_column_list

    @cached_property
    def primary_key(self) -> Optional['ResolvedPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.parent.primary_key

    @cached_property
    def foreign_key_list(self) -> List['ResolvedForeignKeyProto']:
        """Field foreign_key_list"""
        return self._proto.parent.foreign_key_list

    @cached_property
    def check_constraint_list(self) -> List['ResolvedCheckConstraintProto']:
        """Field check_constraint_list"""
        return self._proto.parent.check_constraint_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def like_table(self) -> Optional['TableRefProto']:
        """Field like_table"""
        return self._proto.parent.like_table

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.parent.collation_name

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.parent.connection

    @cached_property
    def with_partition_columns(self) -> Optional['ResolvedWithPartitionColumnsProto']:
        """Field with_partition_columns"""
        return self._proto.with_partition_columns



class ResolvedCreateMaterializedViewStmt(ResolvedCreateViewBase):
    """Generated wrapper for ResolvedCreateMaterializedViewStmtProto"""

    def __init__(self, proto: 'ResolvedCreateMaterializedViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.parent.output_column_list

    @cached_property
    def has_explicit_columns(self) -> Optional[bool]:
        """Field has_explicit_columns"""
        return self._proto.parent.has_explicit_columns

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.parent.sql

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def cluster_by_list(self) -> List['AnyResolvedExprProto']:
        """Field cluster_by_list"""
        return self._proto.cluster_by_list

    @cached_property
    def replica_source(self) -> Optional['AnyResolvedScanProto']:
        """Field replica_source"""
        return self._proto.replica_source



class ResolvedCreateSchemaStmt(ResolvedCreateSchemaStmtBase):
    """Generated wrapper for ResolvedCreateSchemaStmtProto"""

    def __init__(self, proto: 'ResolvedCreateSchemaStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.collation_name



class ResolvedCreateTableAsSelectStmt(ResolvedCreateTableStmtBase):
    """Generated wrapper for ResolvedCreateTableAsSelectStmtProto"""

    def __init__(self, proto: 'ResolvedCreateTableAsSelectStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list

    @cached_property
    def pseudo_column_list(self) -> List['ResolvedColumnProto']:
        """Field pseudo_column_list"""
        return self._proto.parent.pseudo_column_list

    @cached_property
    def primary_key(self) -> Optional['ResolvedPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.parent.primary_key

    @cached_property
    def foreign_key_list(self) -> List['ResolvedForeignKeyProto']:
        """Field foreign_key_list"""
        return self._proto.parent.foreign_key_list

    @cached_property
    def check_constraint_list(self) -> List['ResolvedCheckConstraintProto']:
        """Field check_constraint_list"""
        return self._proto.parent.check_constraint_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def like_table(self) -> Optional['TableRefProto']:
        """Field like_table"""
        return self._proto.parent.like_table

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.parent.collation_name

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.parent.connection

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def cluster_by_list(self) -> List['AnyResolvedExprProto']:
        """Field cluster_by_list"""
        return self._proto.cluster_by_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.output_column_list

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.query



class ResolvedCreateTableStmt(ResolvedCreateTableStmtBase):
    """Generated wrapper for ResolvedCreateTableStmtProto"""

    def __init__(self, proto: 'ResolvedCreateTableStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list

    @cached_property
    def pseudo_column_list(self) -> List['ResolvedColumnProto']:
        """Field pseudo_column_list"""
        return self._proto.parent.pseudo_column_list

    @cached_property
    def primary_key(self) -> Optional['ResolvedPrimaryKeyProto']:
        """Field primary_key"""
        return self._proto.parent.primary_key

    @cached_property
    def foreign_key_list(self) -> List['ResolvedForeignKeyProto']:
        """Field foreign_key_list"""
        return self._proto.parent.foreign_key_list

    @cached_property
    def check_constraint_list(self) -> List['ResolvedCheckConstraintProto']:
        """Field check_constraint_list"""
        return self._proto.parent.check_constraint_list

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def like_table(self) -> Optional['TableRefProto']:
        """Field like_table"""
        return self._proto.parent.like_table

    @cached_property
    def collation_name(self) -> Optional['AnyResolvedExprProto']:
        """Field collation_name"""
        return self._proto.parent.collation_name

    @cached_property
    def connection(self) -> Optional['ResolvedConnectionProto']:
        """Field connection"""
        return self._proto.parent.connection

    @cached_property
    def clone_from(self) -> Optional['AnyResolvedScanProto']:
        """Field clone_from"""
        return self._proto.clone_from

    @cached_property
    def copy_from(self) -> Optional['AnyResolvedScanProto']:
        """Field copy_from"""
        return self._proto.copy_from

    @cached_property
    def partition_by_list(self) -> List['AnyResolvedExprProto']:
        """Field partition_by_list"""
        return self._proto.partition_by_list

    @cached_property
    def cluster_by_list(self) -> List['AnyResolvedExprProto']:
        """Field cluster_by_list"""
        return self._proto.cluster_by_list



class ResolvedCreateViewStmt(ResolvedCreateViewBase):
    """Generated wrapper for ResolvedCreateViewStmtProto"""

    def __init__(self, proto: 'ResolvedCreateViewStmtProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def name_path(self) -> List[str]:
        """Field name_path"""
        return self._proto.parent.parent.name_path

    @cached_property
    def create_scope(self) -> Optional[int]:
        """Field create_scope"""
        return self._proto.parent.parent.create_scope

    @cached_property
    def create_mode(self) -> Optional[int]:
        """Field create_mode"""
        return self._proto.parent.parent.create_mode

    @cached_property
    def option_list(self) -> List['ResolvedOptionProto']:
        """Field option_list"""
        return self._proto.parent.option_list

    @cached_property
    def output_column_list(self) -> List['ResolvedOutputColumnProto']:
        """Field output_column_list"""
        return self._proto.parent.output_column_list

    @cached_property
    def has_explicit_columns(self) -> Optional[bool]:
        """Field has_explicit_columns"""
        return self._proto.parent.has_explicit_columns

    @cached_property
    def query(self) -> Optional['AnyResolvedScanProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql(self) -> Optional[str]:
        """Field sql"""
        return self._proto.parent.sql

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def is_value_table(self) -> Optional[bool]:
        """Field is_value_table"""
        return self._proto.parent.is_value_table

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive

    @cached_property
    def column_definition_list(self) -> List['ResolvedColumnDefinitionProto']:
        """Field column_definition_list"""
        return self._proto.parent.column_definition_list



class ResolvedDeferredComputedColumn(ResolvedComputedColumnImpl):
    """Generated wrapper for ResolvedDeferredComputedColumnProto"""

    def __init__(self, proto: 'ResolvedDeferredComputedColumnProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def column(self) -> Optional['ResolvedColumnProto']:
        """Field column"""
        return self._proto.column

    @cached_property
    def expr(self) -> Optional['AnyResolvedExprProto']:
        """Field expr"""
        return self._proto.expr

    @cached_property
    def side_effect_column(self) -> Optional['ResolvedColumnProto']:
        """Field side_effect_column"""
        return self._proto.side_effect_column



class ResolvedGraphEdgeScan(ResolvedGraphElementScan):
    """Generated wrapper for ResolvedGraphEdgeScanProto"""

    def __init__(self, proto: 'ResolvedGraphEdgeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.parent.node_source

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.parent.filter_expr

    @cached_property
    def label_expr(self) -> Optional['AnyResolvedGraphLabelExprProto']:
        """Field label_expr"""
        return self._proto.parent.label_expr

    @cached_property
    def target_element_table_list(self) -> List['GraphElementTableRefProto']:
        """Field target_element_table_list"""
        return self._proto.parent.target_element_table_list

    @cached_property
    def orientation(self) -> Optional[int]:
        """Field orientation"""
        return self._proto.orientation

    @cached_property
    def lhs_hint_list(self) -> List['ResolvedOptionProto']:
        """Field lhs_hint_list"""
        return self._proto.lhs_hint_list

    @cached_property
    def rhs_hint_list(self) -> List['ResolvedOptionProto']:
        """Field rhs_hint_list"""
        return self._proto.rhs_hint_list

    @cached_property
    def cost_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field cost_expr"""
        return self._proto.cost_expr



class ResolvedGraphNodeScan(ResolvedGraphElementScan):
    """Generated wrapper for ResolvedGraphNodeScanProto"""

    def __init__(self, proto: 'ResolvedGraphNodeScanProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parse_location_range

    @cached_property
    def column_list(self) -> List['ResolvedColumnProto']:
        """Field column_list"""
        return self._proto.parent.parent.parent.column_list

    @cached_property
    def hint_list(self) -> List['ResolvedOptionProto']:
        """Field hint_list"""
        return self._proto.parent.parent.parent.hint_list

    @cached_property
    def is_ordered(self) -> Optional[bool]:
        """Field is_ordered"""
        return self._proto.parent.parent.parent.is_ordered

    @cached_property
    def node_source(self) -> Optional[str]:
        """Field node_source"""
        return self._proto.parent.parent.parent.node_source

    @cached_property
    def filter_expr(self) -> Optional['AnyResolvedExprProto']:
        """Field filter_expr"""
        return self._proto.parent.filter_expr

    @cached_property
    def label_expr(self) -> Optional['AnyResolvedGraphLabelExprProto']:
        """Field label_expr"""
        return self._proto.parent.label_expr

    @cached_property
    def target_element_table_list(self) -> List['GraphElementTableRefProto']:
        """Field target_element_table_list"""
        return self._proto.parent.target_element_table_list



class ASTAuxLoadDataStatement(ASTCreateTableStmtBase):
    """Generated wrapper for ASTAuxLoadDataStatementProto"""

    def __init__(self, proto: 'ASTAuxLoadDataStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def table_element_list(self) -> Optional['ASTTableElementListProto']:
        """Field table_element_list"""
        return self._proto.parent.table_element_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def like_table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field like_table_name"""
        return self._proto.parent.like_table_name

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.parent.with_connection_clause

    @cached_property
    def insertion_mode(self) -> Optional[int]:
        """Field insertion_mode"""
        return self._proto.insertion_mode

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def cluster_by(self) -> Optional['ASTClusterByProto']:
        """Field cluster_by"""
        return self._proto.cluster_by

    @cached_property
    def from_files(self) -> Optional['ASTAuxLoadDataFromFilesOptionsListProto']:
        """Field from_files"""
        return self._proto.from_files

    @cached_property
    def with_partition_columns_clause(self) -> Optional['ASTWithPartitionColumnsClauseProto']:
        """Field with_partition_columns_clause"""
        return self._proto.with_partition_columns_clause

    @cached_property
    def load_data_partitions_clause(self) -> Optional['ASTAuxLoadDataPartitionsClauseProto']:
        """Field load_data_partitions_clause"""
        return self._proto.load_data_partitions_clause

    @cached_property
    def is_temp_table(self) -> Optional[bool]:
        """Field is_temp_table"""
        return self._proto.is_temp_table



class ASTCreateApproxViewStatement(ASTCreateViewStatementBase):
    """Generated wrapper for ASTCreateApproxViewStatementProto"""

    def __init__(self, proto: 'ASTCreateApproxViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def column_with_options_list(self) -> Optional['ASTColumnWithOptionsListProto']:
        """Field column_with_options_list"""
        return self._proto.parent.column_with_options_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive



class ASTCreateExternalSchemaStatement(ASTCreateSchemaStmtBase):
    """Generated wrapper for ASTCreateExternalSchemaStatementProto"""

    def __init__(self, proto: 'ASTCreateExternalSchemaStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause



class ASTCreateExternalTableStatement(ASTCreateTableStmtBase):
    """Generated wrapper for ASTCreateExternalTableStatementProto"""

    def __init__(self, proto: 'ASTCreateExternalTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def table_element_list(self) -> Optional['ASTTableElementListProto']:
        """Field table_element_list"""
        return self._proto.parent.table_element_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def like_table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field like_table_name"""
        return self._proto.parent.like_table_name

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.parent.with_connection_clause

    @cached_property
    def with_partition_columns_clause(self) -> Optional['ASTWithPartitionColumnsClauseProto']:
        """Field with_partition_columns_clause"""
        return self._proto.with_partition_columns_clause



class ASTCreateFunctionStatement(ASTCreateFunctionStmtBase):
    """Generated wrapper for ASTCreateFunctionStatementProto"""

    def __init__(self, proto: 'ASTCreateFunctionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def function_declaration(self) -> Optional['ASTFunctionDeclarationProto']:
        """Field function_declaration"""
        return self._proto.parent.function_declaration

    @cached_property
    def language(self) -> Optional['ASTIdentifierProto']:
        """Field language"""
        return self._proto.parent.language

    @cached_property
    def code(self) -> Optional['ASTStringLiteralProto']:
        """Field code"""
        return self._proto.parent.code

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def determinism_level(self) -> Optional[int]:
        """Field determinism_level"""
        return self._proto.parent.determinism_level

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def return_type(self) -> Optional['AnyASTTypeProto']:
        """Field return_type"""
        return self._proto.return_type

    @cached_property
    def sql_function_body(self) -> Optional['ASTSqlFunctionBodyProto']:
        """Field sql_function_body"""
        return self._proto.sql_function_body

    @cached_property
    def is_aggregate(self) -> Optional[bool]:
        """Field is_aggregate"""
        return self._proto.is_aggregate

    @cached_property
    def is_remote(self) -> Optional[bool]:
        """Field is_remote"""
        return self._proto.is_remote

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.with_connection_clause



class ASTCreateMaterializedViewStatement(ASTCreateViewStatementBase):
    """Generated wrapper for ASTCreateMaterializedViewStatementProto"""

    def __init__(self, proto: 'ASTCreateMaterializedViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def column_with_options_list(self) -> Optional['ASTColumnWithOptionsListProto']:
        """Field column_with_options_list"""
        return self._proto.parent.column_with_options_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def cluster_by(self) -> Optional['ASTClusterByProto']:
        """Field cluster_by"""
        return self._proto.cluster_by

    @cached_property
    def replica_source(self) -> Optional['ASTPathExpressionProto']:
        """Field replica_source"""
        return self._proto.replica_source



class ASTCreateSchemaStatement(ASTCreateSchemaStmtBase):
    """Generated wrapper for ASTCreateSchemaStatementProto"""

    def __init__(self, proto: 'ASTCreateSchemaStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.collate



class ASTCreateTableFunctionStatement(ASTCreateFunctionStmtBase):
    """Generated wrapper for ASTCreateTableFunctionStatementProto"""

    def __init__(self, proto: 'ASTCreateTableFunctionStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def function_declaration(self) -> Optional['ASTFunctionDeclarationProto']:
        """Field function_declaration"""
        return self._proto.parent.function_declaration

    @cached_property
    def language(self) -> Optional['ASTIdentifierProto']:
        """Field language"""
        return self._proto.parent.language

    @cached_property
    def code(self) -> Optional['ASTStringLiteralProto']:
        """Field code"""
        return self._proto.parent.code

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def determinism_level(self) -> Optional[int]:
        """Field determinism_level"""
        return self._proto.parent.determinism_level

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def return_tvf_schema(self) -> Optional['ASTTVFSchemaProto']:
        """Field return_tvf_schema"""
        return self._proto.return_tvf_schema

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query



class ASTCreateTableStatement(ASTCreateTableStmtBase):
    """Generated wrapper for ASTCreateTableStatementProto"""

    def __init__(self, proto: 'ASTCreateTableStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def table_element_list(self) -> Optional['ASTTableElementListProto']:
        """Field table_element_list"""
        return self._proto.parent.table_element_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def like_table_name(self) -> Optional['ASTPathExpressionProto']:
        """Field like_table_name"""
        return self._proto.parent.like_table_name

    @cached_property
    def collate(self) -> Optional['ASTCollateProto']:
        """Field collate"""
        return self._proto.parent.collate

    @cached_property
    def with_connection_clause(self) -> Optional['ASTWithConnectionClauseProto']:
        """Field with_connection_clause"""
        return self._proto.parent.with_connection_clause

    @cached_property
    def clone_data_source(self) -> Optional['ASTCloneDataSourceProto']:
        """Field clone_data_source"""
        return self._proto.clone_data_source

    @cached_property
    def copy_data_source(self) -> Optional['ASTCopyDataSourceProto']:
        """Field copy_data_source"""
        return self._proto.copy_data_source

    @cached_property
    def partition_by(self) -> Optional['ASTPartitionByProto']:
        """Field partition_by"""
        return self._proto.partition_by

    @cached_property
    def cluster_by(self) -> Optional['ASTClusterByProto']:
        """Field cluster_by"""
        return self._proto.cluster_by

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.query

    @cached_property
    def spanner_options(self) -> Optional['ASTSpannerTableOptionsProto']:
        """Field spanner_options"""
        return self._proto.spanner_options

    @cached_property
    def ttl(self) -> Optional['ASTTtlClauseProto']:
        """Field ttl"""
        return self._proto.ttl



class ASTCreateViewStatement(ASTCreateViewStatementBase):
    """Generated wrapper for ASTCreateViewStatementProto"""

    def __init__(self, proto: 'ASTCreateViewStatementProto'):
        self._proto = proto

    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        """Field parse_location_range"""
        return self._proto.parent.parent.parent.parent.parent.parse_location_range

    @cached_property
    def scope(self) -> Optional[int]:
        """Field scope"""
        return self._proto.parent.parent.scope

    @cached_property
    def is_or_replace(self) -> Optional[bool]:
        """Field is_or_replace"""
        return self._proto.parent.parent.is_or_replace

    @cached_property
    def is_if_not_exists(self) -> Optional[bool]:
        """Field is_if_not_exists"""
        return self._proto.parent.parent.is_if_not_exists

    @cached_property
    def name(self) -> Optional['ASTPathExpressionProto']:
        """Field name"""
        return self._proto.parent.name

    @cached_property
    def column_with_options_list(self) -> Optional['ASTColumnWithOptionsListProto']:
        """Field column_with_options_list"""
        return self._proto.parent.column_with_options_list

    @cached_property
    def options_list(self) -> Optional['ASTOptionsListProto']:
        """Field options_list"""
        return self._proto.parent.options_list

    @cached_property
    def query(self) -> Optional['ASTQueryProto']:
        """Field query"""
        return self._proto.parent.query

    @cached_property
    def sql_security(self) -> Optional[int]:
        """Field sql_security"""
        return self._proto.parent.sql_security

    @cached_property
    def recursive(self) -> Optional[bool]:
        """Field recursive"""
        return self._proto.parent.recursive


