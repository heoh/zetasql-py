from zetasql.public import annotation_pb2 as _annotation_pb2
from zetasql.public.proto import type_annotation_pb2 as _type_annotation_pb2
from zetasql.public import type_pb2 as _type_pb2
from zetasql.public import type_modifiers_pb2 as _type_modifiers_pb2
from zetasql.public import type_parameters_pb2 as _type_parameters_pb2
from zetasql.proto import function_pb2 as _function_pb2
from zetasql.resolved_ast import serialization_pb2 as _serialization_pb2
from zetasql.resolved_ast import resolved_ast_enums_pb2 as _resolved_ast_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnyResolvedNodeProto(_message.Message):
    __slots__ = ("resolved_argument_node", "resolved_expr_node", "resolved_scan_node", "resolved_statement_node")
    RESOLVED_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_argument_node: AnyResolvedArgumentProto
    resolved_expr_node: AnyResolvedExprProto
    resolved_scan_node: AnyResolvedScanProto
    resolved_statement_node: AnyResolvedStatementProto
    def __init__(self, resolved_argument_node: _Optional[_Union[AnyResolvedArgumentProto, _Mapping]] = ..., resolved_expr_node: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., resolved_scan_node: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., resolved_statement_node: _Optional[_Union[AnyResolvedStatementProto, _Mapping]] = ...) -> None: ...

class AnyResolvedArgumentProto(_message.Message):
    __slots__ = ("resolved_make_proto_field_node", "resolved_column_holder_node", "resolved_order_by_item_node", "resolved_output_column_node", "resolved_with_entry_node", "resolved_option_node", "resolved_window_partitioning_node", "resolved_window_ordering_node", "resolved_window_frame_node", "resolved_analytic_function_group_node", "resolved_window_frame_expr_node", "resolved_dmlvalue_node", "resolved_assert_rows_modified_node", "resolved_insert_row_node", "resolved_update_item_node", "resolved_privilege_node", "resolved_argument_def_node", "resolved_argument_list_node", "resolved_function_argument_node", "resolved_function_signature_holder_node", "resolved_aggregate_having_modifier_node", "resolved_column_definition_node", "resolved_set_operation_item_node", "resolved_index_item_node", "resolved_merge_when_node", "resolved_update_item_element_node", "resolved_column_annotations_node", "resolved_generated_column_info_node", "resolved_model_node", "resolved_alter_action_node", "resolved_unnest_item_node", "resolved_replace_field_item_node", "resolved_connection_node", "resolved_execute_immediate_argument_node", "resolved_descriptor_node", "resolved_extended_cast_element_node", "resolved_with_partition_columns_node", "resolved_extended_cast_node", "resolved_inline_lambda_node", "resolved_constraint_node", "resolved_pivot_column_node", "resolved_returning_clause_node", "resolved_unpivot_arg_node", "resolved_filter_field_arg_node", "resolved_table_and_column_info_node", "resolved_column_default_value_node", "resolved_object_unit_node", "resolved_graph_label_expr_node", "resolved_graph_element_identifier_node", "resolved_graph_element_property_node", "resolved_aux_load_data_partition_filter_node", "resolved_graph_element_table_node", "resolved_graph_node_table_reference_node", "resolved_create_model_aliased_query_node", "resolved_graph_element_label_node", "resolved_graph_property_declaration_node", "resolved_graph_property_definition_node", "resolved_sequence_node", "resolved_grouping_set_multi_column_node", "resolved_grouping_set_base_node", "resolved_grouping_call_node", "resolved_identity_column_info_node", "resolved_graph_path_pattern_quantifier_node", "resolved_computed_column_base_node", "resolved_recursion_depth_modifier_node", "resolved_graph_make_array_variable_node", "resolved_graph_path_mode_node", "resolved_graph_path_search_prefix_node", "resolved_match_recognize_variable_definition_node", "resolved_match_recognize_pattern_expr_node", "resolved_subpipeline_node", "resolved_lock_mode_node", "resolved_pipe_if_case_node", "resolved_output_schema_node", "resolved_measure_group_node", "resolved_on_conflict_clause_node", "resolved_generalized_query_subpipeline_node", "resolved_graph_dynamic_label_specification_node", "resolved_graph_dynamic_properties_specification_node", "resolved_update_field_item_node", "resolved_graph_path_cost_node")
    RESOLVED_MAKE_PROTO_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COLUMN_HOLDER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ORDER_BY_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_OUTPUT_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WITH_ENTRY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_OPTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WINDOW_PARTITIONING_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WINDOW_ORDERING_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WINDOW_FRAME_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ANALYTIC_FUNCTION_GROUP_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WINDOW_FRAME_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DMLVALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ASSERT_ROWS_MODIFIED_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_INSERT_ROW_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UPDATE_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PRIVILEGE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ARGUMENT_DEF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ARGUMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FUNCTION_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FUNCTION_SIGNATURE_HOLDER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AGGREGATE_HAVING_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COLUMN_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SET_OPERATION_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_INDEX_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MERGE_WHEN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UPDATE_ITEM_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COLUMN_ANNOTATIONS_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GENERATED_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MODEL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UNNEST_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REPLACE_FIELD_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONNECTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXECUTE_IMMEDIATE_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DESCRIPTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXTENDED_CAST_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WITH_PARTITION_COLUMNS_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXTENDED_CAST_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_INLINE_LAMBDA_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONSTRAINT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIVOT_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RETURNING_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UNPIVOT_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FILTER_FIELD_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TABLE_AND_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COLUMN_DEFAULT_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_OBJECT_UNIT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_LABEL_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_ELEMENT_IDENTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_ELEMENT_PROPERTY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AUX_LOAD_DATA_PARTITION_FILTER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_ELEMENT_TABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_NODE_TABLE_REFERENCE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_MODEL_ALIASED_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_ELEMENT_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PROPERTY_DECLARATION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PROPERTY_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SEQUENCE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUPING_SET_MULTI_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUPING_SET_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUPING_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_IDENTITY_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_PATTERN_QUANTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COMPUTED_COLUMN_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RECURSION_DEPTH_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_MAKE_ARRAY_VARIABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_SEARCH_PREFIX_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_VARIABLE_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_PATTERN_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBPIPELINE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LOCK_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_IF_CASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_OUTPUT_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MEASURE_GROUP_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ON_CONFLICT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GENERALIZED_QUERY_SUBPIPELINE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_DYNAMIC_LABEL_SPECIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_DYNAMIC_PROPERTIES_SPECIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UPDATE_FIELD_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_COST_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_make_proto_field_node: ResolvedMakeProtoFieldProto
    resolved_column_holder_node: ResolvedColumnHolderProto
    resolved_order_by_item_node: ResolvedOrderByItemProto
    resolved_output_column_node: ResolvedOutputColumnProto
    resolved_with_entry_node: ResolvedWithEntryProto
    resolved_option_node: ResolvedOptionProto
    resolved_window_partitioning_node: ResolvedWindowPartitioningProto
    resolved_window_ordering_node: ResolvedWindowOrderingProto
    resolved_window_frame_node: ResolvedWindowFrameProto
    resolved_analytic_function_group_node: ResolvedAnalyticFunctionGroupProto
    resolved_window_frame_expr_node: ResolvedWindowFrameExprProto
    resolved_dmlvalue_node: ResolvedDMLValueProto
    resolved_assert_rows_modified_node: ResolvedAssertRowsModifiedProto
    resolved_insert_row_node: ResolvedInsertRowProto
    resolved_update_item_node: ResolvedUpdateItemProto
    resolved_privilege_node: ResolvedPrivilegeProto
    resolved_argument_def_node: ResolvedArgumentDefProto
    resolved_argument_list_node: ResolvedArgumentListProto
    resolved_function_argument_node: ResolvedFunctionArgumentProto
    resolved_function_signature_holder_node: ResolvedFunctionSignatureHolderProto
    resolved_aggregate_having_modifier_node: ResolvedAggregateHavingModifierProto
    resolved_column_definition_node: ResolvedColumnDefinitionProto
    resolved_set_operation_item_node: ResolvedSetOperationItemProto
    resolved_index_item_node: ResolvedIndexItemProto
    resolved_merge_when_node: ResolvedMergeWhenProto
    resolved_update_item_element_node: ResolvedUpdateItemElementProto
    resolved_column_annotations_node: ResolvedColumnAnnotationsProto
    resolved_generated_column_info_node: ResolvedGeneratedColumnInfoProto
    resolved_model_node: ResolvedModelProto
    resolved_alter_action_node: AnyResolvedAlterActionProto
    resolved_unnest_item_node: ResolvedUnnestItemProto
    resolved_replace_field_item_node: ResolvedReplaceFieldItemProto
    resolved_connection_node: ResolvedConnectionProto
    resolved_execute_immediate_argument_node: ResolvedExecuteImmediateArgumentProto
    resolved_descriptor_node: ResolvedDescriptorProto
    resolved_extended_cast_element_node: ResolvedExtendedCastElementProto
    resolved_with_partition_columns_node: ResolvedWithPartitionColumnsProto
    resolved_extended_cast_node: ResolvedExtendedCastProto
    resolved_inline_lambda_node: ResolvedInlineLambdaProto
    resolved_constraint_node: AnyResolvedConstraintProto
    resolved_pivot_column_node: ResolvedPivotColumnProto
    resolved_returning_clause_node: ResolvedReturningClauseProto
    resolved_unpivot_arg_node: ResolvedUnpivotArgProto
    resolved_filter_field_arg_node: ResolvedFilterFieldArgProto
    resolved_table_and_column_info_node: ResolvedTableAndColumnInfoProto
    resolved_column_default_value_node: ResolvedColumnDefaultValueProto
    resolved_object_unit_node: ResolvedObjectUnitProto
    resolved_graph_label_expr_node: AnyResolvedGraphLabelExprProto
    resolved_graph_element_identifier_node: ResolvedGraphElementIdentifierProto
    resolved_graph_element_property_node: ResolvedGraphElementPropertyProto
    resolved_aux_load_data_partition_filter_node: ResolvedAuxLoadDataPartitionFilterProto
    resolved_graph_element_table_node: ResolvedGraphElementTableProto
    resolved_graph_node_table_reference_node: ResolvedGraphNodeTableReferenceProto
    resolved_create_model_aliased_query_node: ResolvedCreateModelAliasedQueryProto
    resolved_graph_element_label_node: ResolvedGraphElementLabelProto
    resolved_graph_property_declaration_node: ResolvedGraphPropertyDeclarationProto
    resolved_graph_property_definition_node: ResolvedGraphPropertyDefinitionProto
    resolved_sequence_node: ResolvedSequenceProto
    resolved_grouping_set_multi_column_node: ResolvedGroupingSetMultiColumnProto
    resolved_grouping_set_base_node: AnyResolvedGroupingSetBaseProto
    resolved_grouping_call_node: ResolvedGroupingCallProto
    resolved_identity_column_info_node: ResolvedIdentityColumnInfoProto
    resolved_graph_path_pattern_quantifier_node: ResolvedGraphPathPatternQuantifierProto
    resolved_computed_column_base_node: AnyResolvedComputedColumnBaseProto
    resolved_recursion_depth_modifier_node: ResolvedRecursionDepthModifierProto
    resolved_graph_make_array_variable_node: ResolvedGraphMakeArrayVariableProto
    resolved_graph_path_mode_node: ResolvedGraphPathModeProto
    resolved_graph_path_search_prefix_node: ResolvedGraphPathSearchPrefixProto
    resolved_match_recognize_variable_definition_node: ResolvedMatchRecognizeVariableDefinitionProto
    resolved_match_recognize_pattern_expr_node: AnyResolvedMatchRecognizePatternExprProto
    resolved_subpipeline_node: ResolvedSubpipelineProto
    resolved_lock_mode_node: ResolvedLockModeProto
    resolved_pipe_if_case_node: ResolvedPipeIfCaseProto
    resolved_output_schema_node: ResolvedOutputSchemaProto
    resolved_measure_group_node: ResolvedMeasureGroupProto
    resolved_on_conflict_clause_node: ResolvedOnConflictClauseProto
    resolved_generalized_query_subpipeline_node: ResolvedGeneralizedQuerySubpipelineProto
    resolved_graph_dynamic_label_specification_node: ResolvedGraphDynamicLabelSpecificationProto
    resolved_graph_dynamic_properties_specification_node: ResolvedGraphDynamicPropertiesSpecificationProto
    resolved_update_field_item_node: ResolvedUpdateFieldItemProto
    resolved_graph_path_cost_node: ResolvedGraphPathCostProto
    def __init__(self, resolved_make_proto_field_node: _Optional[_Union[ResolvedMakeProtoFieldProto, _Mapping]] = ..., resolved_column_holder_node: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., resolved_order_by_item_node: _Optional[_Union[ResolvedOrderByItemProto, _Mapping]] = ..., resolved_output_column_node: _Optional[_Union[ResolvedOutputColumnProto, _Mapping]] = ..., resolved_with_entry_node: _Optional[_Union[ResolvedWithEntryProto, _Mapping]] = ..., resolved_option_node: _Optional[_Union[ResolvedOptionProto, _Mapping]] = ..., resolved_window_partitioning_node: _Optional[_Union[ResolvedWindowPartitioningProto, _Mapping]] = ..., resolved_window_ordering_node: _Optional[_Union[ResolvedWindowOrderingProto, _Mapping]] = ..., resolved_window_frame_node: _Optional[_Union[ResolvedWindowFrameProto, _Mapping]] = ..., resolved_analytic_function_group_node: _Optional[_Union[ResolvedAnalyticFunctionGroupProto, _Mapping]] = ..., resolved_window_frame_expr_node: _Optional[_Union[ResolvedWindowFrameExprProto, _Mapping]] = ..., resolved_dmlvalue_node: _Optional[_Union[ResolvedDMLValueProto, _Mapping]] = ..., resolved_assert_rows_modified_node: _Optional[_Union[ResolvedAssertRowsModifiedProto, _Mapping]] = ..., resolved_insert_row_node: _Optional[_Union[ResolvedInsertRowProto, _Mapping]] = ..., resolved_update_item_node: _Optional[_Union[ResolvedUpdateItemProto, _Mapping]] = ..., resolved_privilege_node: _Optional[_Union[ResolvedPrivilegeProto, _Mapping]] = ..., resolved_argument_def_node: _Optional[_Union[ResolvedArgumentDefProto, _Mapping]] = ..., resolved_argument_list_node: _Optional[_Union[ResolvedArgumentListProto, _Mapping]] = ..., resolved_function_argument_node: _Optional[_Union[ResolvedFunctionArgumentProto, _Mapping]] = ..., resolved_function_signature_holder_node: _Optional[_Union[ResolvedFunctionSignatureHolderProto, _Mapping]] = ..., resolved_aggregate_having_modifier_node: _Optional[_Union[ResolvedAggregateHavingModifierProto, _Mapping]] = ..., resolved_column_definition_node: _Optional[_Union[ResolvedColumnDefinitionProto, _Mapping]] = ..., resolved_set_operation_item_node: _Optional[_Union[ResolvedSetOperationItemProto, _Mapping]] = ..., resolved_index_item_node: _Optional[_Union[ResolvedIndexItemProto, _Mapping]] = ..., resolved_merge_when_node: _Optional[_Union[ResolvedMergeWhenProto, _Mapping]] = ..., resolved_update_item_element_node: _Optional[_Union[ResolvedUpdateItemElementProto, _Mapping]] = ..., resolved_column_annotations_node: _Optional[_Union[ResolvedColumnAnnotationsProto, _Mapping]] = ..., resolved_generated_column_info_node: _Optional[_Union[ResolvedGeneratedColumnInfoProto, _Mapping]] = ..., resolved_model_node: _Optional[_Union[ResolvedModelProto, _Mapping]] = ..., resolved_alter_action_node: _Optional[_Union[AnyResolvedAlterActionProto, _Mapping]] = ..., resolved_unnest_item_node: _Optional[_Union[ResolvedUnnestItemProto, _Mapping]] = ..., resolved_replace_field_item_node: _Optional[_Union[ResolvedReplaceFieldItemProto, _Mapping]] = ..., resolved_connection_node: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., resolved_execute_immediate_argument_node: _Optional[_Union[ResolvedExecuteImmediateArgumentProto, _Mapping]] = ..., resolved_descriptor_node: _Optional[_Union[ResolvedDescriptorProto, _Mapping]] = ..., resolved_extended_cast_element_node: _Optional[_Union[ResolvedExtendedCastElementProto, _Mapping]] = ..., resolved_with_partition_columns_node: _Optional[_Union[ResolvedWithPartitionColumnsProto, _Mapping]] = ..., resolved_extended_cast_node: _Optional[_Union[ResolvedExtendedCastProto, _Mapping]] = ..., resolved_inline_lambda_node: _Optional[_Union[ResolvedInlineLambdaProto, _Mapping]] = ..., resolved_constraint_node: _Optional[_Union[AnyResolvedConstraintProto, _Mapping]] = ..., resolved_pivot_column_node: _Optional[_Union[ResolvedPivotColumnProto, _Mapping]] = ..., resolved_returning_clause_node: _Optional[_Union[ResolvedReturningClauseProto, _Mapping]] = ..., resolved_unpivot_arg_node: _Optional[_Union[ResolvedUnpivotArgProto, _Mapping]] = ..., resolved_filter_field_arg_node: _Optional[_Union[ResolvedFilterFieldArgProto, _Mapping]] = ..., resolved_table_and_column_info_node: _Optional[_Union[ResolvedTableAndColumnInfoProto, _Mapping]] = ..., resolved_column_default_value_node: _Optional[_Union[ResolvedColumnDefaultValueProto, _Mapping]] = ..., resolved_object_unit_node: _Optional[_Union[ResolvedObjectUnitProto, _Mapping]] = ..., resolved_graph_label_expr_node: _Optional[_Union[AnyResolvedGraphLabelExprProto, _Mapping]] = ..., resolved_graph_element_identifier_node: _Optional[_Union[ResolvedGraphElementIdentifierProto, _Mapping]] = ..., resolved_graph_element_property_node: _Optional[_Union[ResolvedGraphElementPropertyProto, _Mapping]] = ..., resolved_aux_load_data_partition_filter_node: _Optional[_Union[ResolvedAuxLoadDataPartitionFilterProto, _Mapping]] = ..., resolved_graph_element_table_node: _Optional[_Union[ResolvedGraphElementTableProto, _Mapping]] = ..., resolved_graph_node_table_reference_node: _Optional[_Union[ResolvedGraphNodeTableReferenceProto, _Mapping]] = ..., resolved_create_model_aliased_query_node: _Optional[_Union[ResolvedCreateModelAliasedQueryProto, _Mapping]] = ..., resolved_graph_element_label_node: _Optional[_Union[ResolvedGraphElementLabelProto, _Mapping]] = ..., resolved_graph_property_declaration_node: _Optional[_Union[ResolvedGraphPropertyDeclarationProto, _Mapping]] = ..., resolved_graph_property_definition_node: _Optional[_Union[ResolvedGraphPropertyDefinitionProto, _Mapping]] = ..., resolved_sequence_node: _Optional[_Union[ResolvedSequenceProto, _Mapping]] = ..., resolved_grouping_set_multi_column_node: _Optional[_Union[ResolvedGroupingSetMultiColumnProto, _Mapping]] = ..., resolved_grouping_set_base_node: _Optional[_Union[AnyResolvedGroupingSetBaseProto, _Mapping]] = ..., resolved_grouping_call_node: _Optional[_Union[ResolvedGroupingCallProto, _Mapping]] = ..., resolved_identity_column_info_node: _Optional[_Union[ResolvedIdentityColumnInfoProto, _Mapping]] = ..., resolved_graph_path_pattern_quantifier_node: _Optional[_Union[ResolvedGraphPathPatternQuantifierProto, _Mapping]] = ..., resolved_computed_column_base_node: _Optional[_Union[AnyResolvedComputedColumnBaseProto, _Mapping]] = ..., resolved_recursion_depth_modifier_node: _Optional[_Union[ResolvedRecursionDepthModifierProto, _Mapping]] = ..., resolved_graph_make_array_variable_node: _Optional[_Union[ResolvedGraphMakeArrayVariableProto, _Mapping]] = ..., resolved_graph_path_mode_node: _Optional[_Union[ResolvedGraphPathModeProto, _Mapping]] = ..., resolved_graph_path_search_prefix_node: _Optional[_Union[ResolvedGraphPathSearchPrefixProto, _Mapping]] = ..., resolved_match_recognize_variable_definition_node: _Optional[_Union[ResolvedMatchRecognizeVariableDefinitionProto, _Mapping]] = ..., resolved_match_recognize_pattern_expr_node: _Optional[_Union[AnyResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., resolved_subpipeline_node: _Optional[_Union[ResolvedSubpipelineProto, _Mapping]] = ..., resolved_lock_mode_node: _Optional[_Union[ResolvedLockModeProto, _Mapping]] = ..., resolved_pipe_if_case_node: _Optional[_Union[ResolvedPipeIfCaseProto, _Mapping]] = ..., resolved_output_schema_node: _Optional[_Union[ResolvedOutputSchemaProto, _Mapping]] = ..., resolved_measure_group_node: _Optional[_Union[ResolvedMeasureGroupProto, _Mapping]] = ..., resolved_on_conflict_clause_node: _Optional[_Union[ResolvedOnConflictClauseProto, _Mapping]] = ..., resolved_generalized_query_subpipeline_node: _Optional[_Union[ResolvedGeneralizedQuerySubpipelineProto, _Mapping]] = ..., resolved_graph_dynamic_label_specification_node: _Optional[_Union[ResolvedGraphDynamicLabelSpecificationProto, _Mapping]] = ..., resolved_graph_dynamic_properties_specification_node: _Optional[_Union[ResolvedGraphDynamicPropertiesSpecificationProto, _Mapping]] = ..., resolved_update_field_item_node: _Optional[_Union[ResolvedUpdateFieldItemProto, _Mapping]] = ..., resolved_graph_path_cost_node: _Optional[_Union[ResolvedGraphPathCostProto, _Mapping]] = ...) -> None: ...

class ResolvedArgumentProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: _serialization_pb2.ResolvedNodeProto
    def __init__(self, parent: _Optional[_Union[_serialization_pb2.ResolvedNodeProto, _Mapping]] = ...) -> None: ...

class AnyResolvedExprProto(_message.Message):
    __slots__ = ("resolved_literal_node", "resolved_parameter_node", "resolved_expression_column_node", "resolved_column_ref_node", "resolved_function_call_base_node", "resolved_cast_node", "resolved_make_struct_node", "resolved_make_proto_node", "resolved_get_struct_field_node", "resolved_get_proto_field_node", "resolved_subquery_expr_node", "resolved_dmldefault_node", "resolved_argument_ref_node", "resolved_constant_node", "resolved_replace_field_node", "resolved_get_proto_oneof_node", "resolved_system_variable_node", "resolved_flatten_node", "resolved_flattened_arg_node", "resolved_get_json_field_node", "resolved_filter_field_node", "resolved_with_expr_node", "resolved_catalog_column_ref_node", "resolved_graph_get_element_property_node", "resolved_graph_make_element_node", "resolved_array_aggregate_node", "resolved_graph_is_labeled_predicate_node", "resolved_update_constructor_node", "resolved_get_row_field_node")
    RESOLVED_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PARAMETER_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPRESSION_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COLUMN_REF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FUNCTION_CALL_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CAST_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MAKE_STRUCT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MAKE_PROTO_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GET_STRUCT_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GET_PROTO_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBQUERY_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DMLDEFAULT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ARGUMENT_REF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONSTANT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REPLACE_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GET_PROTO_ONEOF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SYSTEM_VARIABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FLATTEN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FLATTENED_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GET_JSON_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FILTER_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WITH_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CATALOG_COLUMN_REF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_GET_ELEMENT_PROPERTY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_MAKE_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ARRAY_AGGREGATE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_IS_LABELED_PREDICATE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UPDATE_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GET_ROW_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_literal_node: ResolvedLiteralProto
    resolved_parameter_node: ResolvedParameterProto
    resolved_expression_column_node: ResolvedExpressionColumnProto
    resolved_column_ref_node: ResolvedColumnRefProto
    resolved_function_call_base_node: AnyResolvedFunctionCallBaseProto
    resolved_cast_node: ResolvedCastProto
    resolved_make_struct_node: ResolvedMakeStructProto
    resolved_make_proto_node: ResolvedMakeProtoProto
    resolved_get_struct_field_node: ResolvedGetStructFieldProto
    resolved_get_proto_field_node: ResolvedGetProtoFieldProto
    resolved_subquery_expr_node: ResolvedSubqueryExprProto
    resolved_dmldefault_node: ResolvedDMLDefaultProto
    resolved_argument_ref_node: ResolvedArgumentRefProto
    resolved_constant_node: ResolvedConstantProto
    resolved_replace_field_node: ResolvedReplaceFieldProto
    resolved_get_proto_oneof_node: ResolvedGetProtoOneofProto
    resolved_system_variable_node: ResolvedSystemVariableProto
    resolved_flatten_node: ResolvedFlattenProto
    resolved_flattened_arg_node: ResolvedFlattenedArgProto
    resolved_get_json_field_node: ResolvedGetJsonFieldProto
    resolved_filter_field_node: ResolvedFilterFieldProto
    resolved_with_expr_node: ResolvedWithExprProto
    resolved_catalog_column_ref_node: ResolvedCatalogColumnRefProto
    resolved_graph_get_element_property_node: ResolvedGraphGetElementPropertyProto
    resolved_graph_make_element_node: ResolvedGraphMakeElementProto
    resolved_array_aggregate_node: ResolvedArrayAggregateProto
    resolved_graph_is_labeled_predicate_node: ResolvedGraphIsLabeledPredicateProto
    resolved_update_constructor_node: ResolvedUpdateConstructorProto
    resolved_get_row_field_node: ResolvedGetRowFieldProto
    def __init__(self, resolved_literal_node: _Optional[_Union[ResolvedLiteralProto, _Mapping]] = ..., resolved_parameter_node: _Optional[_Union[ResolvedParameterProto, _Mapping]] = ..., resolved_expression_column_node: _Optional[_Union[ResolvedExpressionColumnProto, _Mapping]] = ..., resolved_column_ref_node: _Optional[_Union[ResolvedColumnRefProto, _Mapping]] = ..., resolved_function_call_base_node: _Optional[_Union[AnyResolvedFunctionCallBaseProto, _Mapping]] = ..., resolved_cast_node: _Optional[_Union[ResolvedCastProto, _Mapping]] = ..., resolved_make_struct_node: _Optional[_Union[ResolvedMakeStructProto, _Mapping]] = ..., resolved_make_proto_node: _Optional[_Union[ResolvedMakeProtoProto, _Mapping]] = ..., resolved_get_struct_field_node: _Optional[_Union[ResolvedGetStructFieldProto, _Mapping]] = ..., resolved_get_proto_field_node: _Optional[_Union[ResolvedGetProtoFieldProto, _Mapping]] = ..., resolved_subquery_expr_node: _Optional[_Union[ResolvedSubqueryExprProto, _Mapping]] = ..., resolved_dmldefault_node: _Optional[_Union[ResolvedDMLDefaultProto, _Mapping]] = ..., resolved_argument_ref_node: _Optional[_Union[ResolvedArgumentRefProto, _Mapping]] = ..., resolved_constant_node: _Optional[_Union[ResolvedConstantProto, _Mapping]] = ..., resolved_replace_field_node: _Optional[_Union[ResolvedReplaceFieldProto, _Mapping]] = ..., resolved_get_proto_oneof_node: _Optional[_Union[ResolvedGetProtoOneofProto, _Mapping]] = ..., resolved_system_variable_node: _Optional[_Union[ResolvedSystemVariableProto, _Mapping]] = ..., resolved_flatten_node: _Optional[_Union[ResolvedFlattenProto, _Mapping]] = ..., resolved_flattened_arg_node: _Optional[_Union[ResolvedFlattenedArgProto, _Mapping]] = ..., resolved_get_json_field_node: _Optional[_Union[ResolvedGetJsonFieldProto, _Mapping]] = ..., resolved_filter_field_node: _Optional[_Union[ResolvedFilterFieldProto, _Mapping]] = ..., resolved_with_expr_node: _Optional[_Union[ResolvedWithExprProto, _Mapping]] = ..., resolved_catalog_column_ref_node: _Optional[_Union[ResolvedCatalogColumnRefProto, _Mapping]] = ..., resolved_graph_get_element_property_node: _Optional[_Union[ResolvedGraphGetElementPropertyProto, _Mapping]] = ..., resolved_graph_make_element_node: _Optional[_Union[ResolvedGraphMakeElementProto, _Mapping]] = ..., resolved_array_aggregate_node: _Optional[_Union[ResolvedArrayAggregateProto, _Mapping]] = ..., resolved_graph_is_labeled_predicate_node: _Optional[_Union[ResolvedGraphIsLabeledPredicateProto, _Mapping]] = ..., resolved_update_constructor_node: _Optional[_Union[ResolvedUpdateConstructorProto, _Mapping]] = ..., resolved_get_row_field_node: _Optional[_Union[ResolvedGetRowFieldProto, _Mapping]] = ...) -> None: ...

class ResolvedExprProto(_message.Message):
    __slots__ = ("parent", "type", "type_annotation_map")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ANNOTATION_MAP_FIELD_NUMBER: _ClassVar[int]
    parent: _serialization_pb2.ResolvedNodeProto
    type: _type_pb2.TypeProto
    type_annotation_map: _annotation_pb2.AnnotationMapProto
    def __init__(self, parent: _Optional[_Union[_serialization_pb2.ResolvedNodeProto, _Mapping]] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., type_annotation_map: _Optional[_Union[_annotation_pb2.AnnotationMapProto, _Mapping]] = ...) -> None: ...

class ResolvedLiteralProto(_message.Message):
    __slots__ = ("parent", "value", "has_explicit_type", "float_literal_id", "preserve_in_literal_remover")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPLICIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_LITERAL_ID_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_IN_LITERAL_REMOVER_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    value: _serialization_pb2.ValueWithTypeProto
    has_explicit_type: bool
    float_literal_id: int
    preserve_in_literal_remover: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., has_explicit_type: bool = ..., float_literal_id: _Optional[int] = ..., preserve_in_literal_remover: bool = ...) -> None: ...

class ResolvedParameterProto(_message.Message):
    __slots__ = ("parent", "name", "position", "is_untyped")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    IS_UNTYPED_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    name: str
    position: int
    is_untyped: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., name: _Optional[str] = ..., position: _Optional[int] = ..., is_untyped: bool = ...) -> None: ...

class ResolvedExpressionColumnProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    name: str
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ResolvedCatalogColumnRefProto(_message.Message):
    __slots__ = ("parent", "column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    column: _serialization_pb2.ColumnRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ColumnRefProto, _Mapping]] = ...) -> None: ...

class ResolvedColumnRefProto(_message.Message):
    __slots__ = ("parent", "column", "is_correlated")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    IS_CORRELATED_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    column: _serialization_pb2.ResolvedColumnProto
    is_correlated: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., is_correlated: bool = ...) -> None: ...

class ResolvedGroupingSetMultiColumnProto(_message.Message):
    __slots__ = ("parent", "column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedConstantProto(_message.Message):
    __slots__ = ("parent", "constant")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    constant: _serialization_pb2.ConstantRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., constant: _Optional[_Union[_serialization_pb2.ConstantRefProto, _Mapping]] = ...) -> None: ...

class ResolvedSystemVariableProto(_message.Message):
    __slots__ = ("parent", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedInlineLambdaProto(_message.Message):
    __slots__ = ("parent", "argument_list", "parameter_list", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_LIST_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    argument_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    parameter_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    body: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., argument_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., parameter_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ..., body: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedSequenceProto(_message.Message):
    __slots__ = ("parent", "sequence")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    sequence: _serialization_pb2.SequenceRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., sequence: _Optional[_Union[_serialization_pb2.SequenceRefProto, _Mapping]] = ...) -> None: ...

class ResolvedFilterFieldArgProto(_message.Message):
    __slots__ = ("parent", "include", "field_descriptor_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    FIELD_DESCRIPTOR_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    include: bool
    field_descriptor_path: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.FieldDescriptorRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., include: bool = ..., field_descriptor_path: _Optional[_Iterable[_Union[_serialization_pb2.FieldDescriptorRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedFilterFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "filter_field_arg_list", "reset_cleared_required_fields")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_ARG_LIST_FIELD_NUMBER: _ClassVar[int]
    RESET_CLEARED_REQUIRED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    filter_field_arg_list: _containers.RepeatedCompositeFieldContainer[ResolvedFilterFieldArgProto]
    reset_cleared_required_fields: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., filter_field_arg_list: _Optional[_Iterable[_Union[ResolvedFilterFieldArgProto, _Mapping]]] = ..., reset_cleared_required_fields: bool = ...) -> None: ...

class AnyResolvedFunctionCallBaseProto(_message.Message):
    __slots__ = ("resolved_function_call_node", "resolved_non_scalar_function_call_base_node")
    RESOLVED_FUNCTION_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_NON_SCALAR_FUNCTION_CALL_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_function_call_node: ResolvedFunctionCallProto
    resolved_non_scalar_function_call_base_node: AnyResolvedNonScalarFunctionCallBaseProto
    def __init__(self, resolved_function_call_node: _Optional[_Union[ResolvedFunctionCallProto, _Mapping]] = ..., resolved_non_scalar_function_call_base_node: _Optional[_Union[AnyResolvedNonScalarFunctionCallBaseProto, _Mapping]] = ...) -> None: ...

class ResolvedFunctionCallBaseProto(_message.Message):
    __slots__ = ("parent", "function", "signature", "argument_list", "generic_argument_list", "error_mode", "hint_list", "collation_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    GENERIC_ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    ERROR_MODE_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLATION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    function: _serialization_pb2.FunctionRefProto
    signature: _function_pb2.FunctionSignatureProto
    argument_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    generic_argument_list: _containers.RepeatedCompositeFieldContainer[ResolvedFunctionArgumentProto]
    error_mode: _resolved_ast_enums_pb2.ResolvedFunctionCallBaseEnums.ErrorMode
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    collation_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedCollationProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., function: _Optional[_Union[_serialization_pb2.FunctionRefProto, _Mapping]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., argument_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., generic_argument_list: _Optional[_Iterable[_Union[ResolvedFunctionArgumentProto, _Mapping]]] = ..., error_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedFunctionCallBaseEnums.ErrorMode, str]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., collation_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedCollationProto, _Mapping]]] = ...) -> None: ...

class ResolvedFunctionCallProto(_message.Message):
    __slots__ = ("parent", "function_call_info")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_CALL_INFO_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedFunctionCallBaseProto
    function_call_info: _function_pb2.ResolvedFunctionCallInfoProto
    def __init__(self, parent: _Optional[_Union[ResolvedFunctionCallBaseProto, _Mapping]] = ..., function_call_info: _Optional[_Union[_function_pb2.ResolvedFunctionCallInfoProto, _Mapping]] = ...) -> None: ...

class AnyResolvedNonScalarFunctionCallBaseProto(_message.Message):
    __slots__ = ("resolved_aggregate_function_call_node", "resolved_analytic_function_call_node")
    RESOLVED_AGGREGATE_FUNCTION_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ANALYTIC_FUNCTION_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_aggregate_function_call_node: ResolvedAggregateFunctionCallProto
    resolved_analytic_function_call_node: ResolvedAnalyticFunctionCallProto
    def __init__(self, resolved_aggregate_function_call_node: _Optional[_Union[ResolvedAggregateFunctionCallProto, _Mapping]] = ..., resolved_analytic_function_call_node: _Optional[_Union[ResolvedAnalyticFunctionCallProto, _Mapping]] = ...) -> None: ...

class ResolvedNonScalarFunctionCallBaseProto(_message.Message):
    __slots__ = ("parent", "distinct", "null_handling_modifier", "where_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_FIELD_NUMBER: _ClassVar[int]
    NULL_HANDLING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    WHERE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedFunctionCallBaseProto
    distinct: bool
    null_handling_modifier: _resolved_ast_enums_pb2.ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier
    where_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedFunctionCallBaseProto, _Mapping]] = ..., distinct: bool = ..., null_handling_modifier: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedNonScalarFunctionCallBaseEnums.NullHandlingModifier, str]] = ..., where_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedAggregateFunctionCallProto(_message.Message):
    __slots__ = ("parent", "having_modifier", "order_by_item_list", "limit", "function_call_info", "group_by_list", "group_by_hint_list", "group_by_aggregate_list", "having_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HAVING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_CALL_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_AGGREGATE_LIST_FIELD_NUMBER: _ClassVar[int]
    HAVING_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedNonScalarFunctionCallBaseProto
    having_modifier: ResolvedAggregateHavingModifierProto
    order_by_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedOrderByItemProto]
    limit: AnyResolvedExprProto
    function_call_info: _function_pb2.ResolvedFunctionCallInfoProto
    group_by_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    group_by_hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    group_by_aggregate_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedComputedColumnBaseProto]
    having_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedNonScalarFunctionCallBaseProto, _Mapping]] = ..., having_modifier: _Optional[_Union[ResolvedAggregateHavingModifierProto, _Mapping]] = ..., order_by_item_list: _Optional[_Iterable[_Union[ResolvedOrderByItemProto, _Mapping]]] = ..., limit: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., function_call_info: _Optional[_Union[_function_pb2.ResolvedFunctionCallInfoProto, _Mapping]] = ..., group_by_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., group_by_hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., group_by_aggregate_list: _Optional[_Iterable[_Union[AnyResolvedComputedColumnBaseProto, _Mapping]]] = ..., having_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedAnalyticFunctionCallProto(_message.Message):
    __slots__ = ("parent", "window_frame")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FRAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedNonScalarFunctionCallBaseProto
    window_frame: ResolvedWindowFrameProto
    def __init__(self, parent: _Optional[_Union[ResolvedNonScalarFunctionCallBaseProto, _Mapping]] = ..., window_frame: _Optional[_Union[ResolvedWindowFrameProto, _Mapping]] = ...) -> None: ...

class ResolvedExtendedCastElementProto(_message.Message):
    __slots__ = ("parent", "from_type", "to_type", "function")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FROM_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_TYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    from_type: _type_pb2.TypeProto
    to_type: _type_pb2.TypeProto
    function: _serialization_pb2.FunctionRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., from_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., to_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., function: _Optional[_Union[_serialization_pb2.FunctionRefProto, _Mapping]] = ...) -> None: ...

class ResolvedExtendedCastProto(_message.Message):
    __slots__ = ("parent", "element_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    element_list: _containers.RepeatedCompositeFieldContainer[ResolvedExtendedCastElementProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., element_list: _Optional[_Iterable[_Union[ResolvedExtendedCastElementProto, _Mapping]]] = ...) -> None: ...

class ResolvedCastProto(_message.Message):
    __slots__ = ("parent", "expr", "return_null_on_error", "extended_cast", "format", "time_zone", "type_modifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    RETURN_NULL_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_CAST_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TYPE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    return_null_on_error: bool
    extended_cast: ResolvedExtendedCastProto
    format: AnyResolvedExprProto
    time_zone: AnyResolvedExprProto
    type_modifiers: _type_modifiers_pb2.TypeModifiersProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., return_null_on_error: bool = ..., extended_cast: _Optional[_Union[ResolvedExtendedCastProto, _Mapping]] = ..., format: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., time_zone: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., type_modifiers: _Optional[_Union[_type_modifiers_pb2.TypeModifiersProto, _Mapping]] = ...) -> None: ...

class ResolvedMakeStructProto(_message.Message):
    __slots__ = ("parent", "field_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    field_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., field_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedMakeProtoProto(_message.Message):
    __slots__ = ("parent", "field_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    field_list: _containers.RepeatedCompositeFieldContainer[ResolvedMakeProtoFieldProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., field_list: _Optional[_Iterable[_Union[ResolvedMakeProtoFieldProto, _Mapping]]] = ...) -> None: ...

class ResolvedMakeProtoFieldProto(_message.Message):
    __slots__ = ("parent", "field_descriptor", "format", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    field_descriptor: _serialization_pb2.FieldDescriptorRefProto
    format: _type_annotation_pb2.FieldFormat.Format
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., field_descriptor: _Optional[_Union[_serialization_pb2.FieldDescriptorRefProto, _Mapping]] = ..., format: _Optional[_Union[_type_annotation_pb2.FieldFormat.Format, str]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGetStructFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "field_idx", "field_expr_is_positional")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FIELD_IDX_FIELD_NUMBER: _ClassVar[int]
    FIELD_EXPR_IS_POSITIONAL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    field_idx: int
    field_expr_is_positional: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., field_idx: _Optional[int] = ..., field_expr_is_positional: bool = ...) -> None: ...

class ResolvedGetProtoFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "field_descriptor", "default_value", "get_has_bit", "format", "return_default_value_when_unset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FIELD_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    GET_HAS_BIT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RETURN_DEFAULT_VALUE_WHEN_UNSET_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    field_descriptor: _serialization_pb2.FieldDescriptorRefProto
    default_value: _serialization_pb2.ValueWithTypeProto
    get_has_bit: bool
    format: _type_annotation_pb2.FieldFormat.Format
    return_default_value_when_unset: bool
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., field_descriptor: _Optional[_Union[_serialization_pb2.FieldDescriptorRefProto, _Mapping]] = ..., default_value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., get_has_bit: bool = ..., format: _Optional[_Union[_type_annotation_pb2.FieldFormat.Format, str]] = ..., return_default_value_when_unset: bool = ...) -> None: ...

class ResolvedGetJsonFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "field_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    field_name: str
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., field_name: _Optional[str] = ...) -> None: ...

class ResolvedGetRowFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    column: _serialization_pb2.ColumnRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ColumnRefProto, _Mapping]] = ...) -> None: ...

class ResolvedFlattenProto(_message.Message):
    __slots__ = ("parent", "expr", "get_field_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    get_field_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., get_field_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedFlattenedArgProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedReplaceFieldItemProto(_message.Message):
    __slots__ = ("parent", "expr", "struct_index_path", "proto_field_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    STRUCT_INDEX_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTO_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expr: AnyResolvedExprProto
    struct_index_path: _containers.RepeatedScalarFieldContainer[int]
    proto_field_path: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.FieldDescriptorRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., struct_index_path: _Optional[_Iterable[int]] = ..., proto_field_path: _Optional[_Iterable[_Union[_serialization_pb2.FieldDescriptorRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedReplaceFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "replace_field_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    replace_field_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedReplaceFieldItemProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., replace_field_item_list: _Optional[_Iterable[_Union[ResolvedReplaceFieldItemProto, _Mapping]]] = ...) -> None: ...

class ResolvedGetProtoOneofProto(_message.Message):
    __slots__ = ("parent", "expr", "oneof_descriptor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    oneof_descriptor: _serialization_pb2.OneofDescriptorRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., oneof_descriptor: _Optional[_Union[_serialization_pb2.OneofDescriptorRefProto, _Mapping]] = ...) -> None: ...

class ResolvedSubqueryExprProto(_message.Message):
    __slots__ = ("parent", "subquery_type", "parameter_list", "in_expr", "in_collation", "subquery", "hint_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_LIST_FIELD_NUMBER: _ClassVar[int]
    IN_EXPR_FIELD_NUMBER: _ClassVar[int]
    IN_COLLATION_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    subquery_type: _resolved_ast_enums_pb2.ResolvedSubqueryExprEnums.SubqueryType
    parameter_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    in_expr: AnyResolvedExprProto
    in_collation: _serialization_pb2.ResolvedCollationProto
    subquery: AnyResolvedScanProto
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., subquery_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedSubqueryExprEnums.SubqueryType, str]] = ..., parameter_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ..., in_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., in_collation: _Optional[_Union[_serialization_pb2.ResolvedCollationProto, _Mapping]] = ..., subquery: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedWithExprProto(_message.Message):
    __slots__ = ("parent", "assignment_list", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    assignment_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., assignment_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class AnyResolvedScanProto(_message.Message):
    __slots__ = ("resolved_single_row_scan_node", "resolved_table_scan_node", "resolved_join_scan_node", "resolved_array_scan_node", "resolved_filter_scan_node", "resolved_set_operation_scan_node", "resolved_order_by_scan_node", "resolved_limit_offset_scan_node", "resolved_with_ref_scan_node", "resolved_analytic_scan_node", "resolved_sample_scan_node", "resolved_project_scan_node", "resolved_with_scan_node", "resolved_tvfscan_node", "resolved_relation_argument_scan_node", "resolved_aggregate_scan_base_node", "resolved_recursive_ref_scan_node", "resolved_recursive_scan_node", "resolved_pivot_scan_node", "resolved_unpivot_scan_node", "resolved_group_rows_scan_node", "resolved_execute_as_role_scan_node", "resolved_graph_table_scan_node", "resolved_graph_path_scan_base_node", "resolved_graph_scan_base_node", "resolved_graph_ref_scan_node", "resolved_static_describe_scan_node", "resolved_assert_scan_node", "resolved_barrier_scan_node", "resolved_match_recognize_scan_node", "resolved_log_scan_node", "resolved_subpipeline_input_scan_node", "resolved_pipe_if_scan_node", "resolved_pipe_fork_scan_node", "resolved_pipe_export_data_scan_node", "resolved_pipe_create_table_scan_node", "resolved_pipe_tee_scan_node", "resolved_pipe_insert_scan_node", "resolved_graph_call_scan_node", "resolved_describe_scan_node", "resolved_unset_argument_scan_node")
    RESOLVED_SINGLE_ROW_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TABLE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_JOIN_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ARRAY_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FILTER_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SET_OPERATION_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ORDER_BY_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LIMIT_OFFSET_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WITH_REF_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ANALYTIC_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SAMPLE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PROJECT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_WITH_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TVFSCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RELATION_ARGUMENT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AGGREGATE_SCAN_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RECURSIVE_REF_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RECURSIVE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIVOT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UNPIVOT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUP_ROWS_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXECUTE_AS_ROLE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_TABLE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_SCAN_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_SCAN_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_REF_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_STATIC_DESCRIBE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ASSERT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_BARRIER_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LOG_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBPIPELINE_INPUT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_IF_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_FORK_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_EXPORT_DATA_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_CREATE_TABLE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_TEE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_PIPE_INSERT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_CALL_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DESCRIBE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UNSET_ARGUMENT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_single_row_scan_node: ResolvedSingleRowScanProto
    resolved_table_scan_node: ResolvedTableScanProto
    resolved_join_scan_node: ResolvedJoinScanProto
    resolved_array_scan_node: ResolvedArrayScanProto
    resolved_filter_scan_node: ResolvedFilterScanProto
    resolved_set_operation_scan_node: ResolvedSetOperationScanProto
    resolved_order_by_scan_node: ResolvedOrderByScanProto
    resolved_limit_offset_scan_node: ResolvedLimitOffsetScanProto
    resolved_with_ref_scan_node: ResolvedWithRefScanProto
    resolved_analytic_scan_node: ResolvedAnalyticScanProto
    resolved_sample_scan_node: ResolvedSampleScanProto
    resolved_project_scan_node: ResolvedProjectScanProto
    resolved_with_scan_node: ResolvedWithScanProto
    resolved_tvfscan_node: ResolvedTVFScanProto
    resolved_relation_argument_scan_node: ResolvedRelationArgumentScanProto
    resolved_aggregate_scan_base_node: AnyResolvedAggregateScanBaseProto
    resolved_recursive_ref_scan_node: ResolvedRecursiveRefScanProto
    resolved_recursive_scan_node: ResolvedRecursiveScanProto
    resolved_pivot_scan_node: ResolvedPivotScanProto
    resolved_unpivot_scan_node: ResolvedUnpivotScanProto
    resolved_group_rows_scan_node: ResolvedGroupRowsScanProto
    resolved_execute_as_role_scan_node: ResolvedExecuteAsRoleScanProto
    resolved_graph_table_scan_node: ResolvedGraphTableScanProto
    resolved_graph_path_scan_base_node: AnyResolvedGraphPathScanBaseProto
    resolved_graph_scan_base_node: AnyResolvedGraphScanBaseProto
    resolved_graph_ref_scan_node: ResolvedGraphRefScanProto
    resolved_static_describe_scan_node: ResolvedStaticDescribeScanProto
    resolved_assert_scan_node: ResolvedAssertScanProto
    resolved_barrier_scan_node: ResolvedBarrierScanProto
    resolved_match_recognize_scan_node: ResolvedMatchRecognizeScanProto
    resolved_log_scan_node: ResolvedLogScanProto
    resolved_subpipeline_input_scan_node: ResolvedSubpipelineInputScanProto
    resolved_pipe_if_scan_node: ResolvedPipeIfScanProto
    resolved_pipe_fork_scan_node: ResolvedPipeForkScanProto
    resolved_pipe_export_data_scan_node: ResolvedPipeExportDataScanProto
    resolved_pipe_create_table_scan_node: ResolvedPipeCreateTableScanProto
    resolved_pipe_tee_scan_node: ResolvedPipeTeeScanProto
    resolved_pipe_insert_scan_node: ResolvedPipeInsertScanProto
    resolved_graph_call_scan_node: ResolvedGraphCallScanProto
    resolved_describe_scan_node: ResolvedDescribeScanProto
    resolved_unset_argument_scan_node: ResolvedUnsetArgumentScanProto
    def __init__(self, resolved_single_row_scan_node: _Optional[_Union[ResolvedSingleRowScanProto, _Mapping]] = ..., resolved_table_scan_node: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., resolved_join_scan_node: _Optional[_Union[ResolvedJoinScanProto, _Mapping]] = ..., resolved_array_scan_node: _Optional[_Union[ResolvedArrayScanProto, _Mapping]] = ..., resolved_filter_scan_node: _Optional[_Union[ResolvedFilterScanProto, _Mapping]] = ..., resolved_set_operation_scan_node: _Optional[_Union[ResolvedSetOperationScanProto, _Mapping]] = ..., resolved_order_by_scan_node: _Optional[_Union[ResolvedOrderByScanProto, _Mapping]] = ..., resolved_limit_offset_scan_node: _Optional[_Union[ResolvedLimitOffsetScanProto, _Mapping]] = ..., resolved_with_ref_scan_node: _Optional[_Union[ResolvedWithRefScanProto, _Mapping]] = ..., resolved_analytic_scan_node: _Optional[_Union[ResolvedAnalyticScanProto, _Mapping]] = ..., resolved_sample_scan_node: _Optional[_Union[ResolvedSampleScanProto, _Mapping]] = ..., resolved_project_scan_node: _Optional[_Union[ResolvedProjectScanProto, _Mapping]] = ..., resolved_with_scan_node: _Optional[_Union[ResolvedWithScanProto, _Mapping]] = ..., resolved_tvfscan_node: _Optional[_Union[ResolvedTVFScanProto, _Mapping]] = ..., resolved_relation_argument_scan_node: _Optional[_Union[ResolvedRelationArgumentScanProto, _Mapping]] = ..., resolved_aggregate_scan_base_node: _Optional[_Union[AnyResolvedAggregateScanBaseProto, _Mapping]] = ..., resolved_recursive_ref_scan_node: _Optional[_Union[ResolvedRecursiveRefScanProto, _Mapping]] = ..., resolved_recursive_scan_node: _Optional[_Union[ResolvedRecursiveScanProto, _Mapping]] = ..., resolved_pivot_scan_node: _Optional[_Union[ResolvedPivotScanProto, _Mapping]] = ..., resolved_unpivot_scan_node: _Optional[_Union[ResolvedUnpivotScanProto, _Mapping]] = ..., resolved_group_rows_scan_node: _Optional[_Union[ResolvedGroupRowsScanProto, _Mapping]] = ..., resolved_execute_as_role_scan_node: _Optional[_Union[ResolvedExecuteAsRoleScanProto, _Mapping]] = ..., resolved_graph_table_scan_node: _Optional[_Union[ResolvedGraphTableScanProto, _Mapping]] = ..., resolved_graph_path_scan_base_node: _Optional[_Union[AnyResolvedGraphPathScanBaseProto, _Mapping]] = ..., resolved_graph_scan_base_node: _Optional[_Union[AnyResolvedGraphScanBaseProto, _Mapping]] = ..., resolved_graph_ref_scan_node: _Optional[_Union[ResolvedGraphRefScanProto, _Mapping]] = ..., resolved_static_describe_scan_node: _Optional[_Union[ResolvedStaticDescribeScanProto, _Mapping]] = ..., resolved_assert_scan_node: _Optional[_Union[ResolvedAssertScanProto, _Mapping]] = ..., resolved_barrier_scan_node: _Optional[_Union[ResolvedBarrierScanProto, _Mapping]] = ..., resolved_match_recognize_scan_node: _Optional[_Union[ResolvedMatchRecognizeScanProto, _Mapping]] = ..., resolved_log_scan_node: _Optional[_Union[ResolvedLogScanProto, _Mapping]] = ..., resolved_subpipeline_input_scan_node: _Optional[_Union[ResolvedSubpipelineInputScanProto, _Mapping]] = ..., resolved_pipe_if_scan_node: _Optional[_Union[ResolvedPipeIfScanProto, _Mapping]] = ..., resolved_pipe_fork_scan_node: _Optional[_Union[ResolvedPipeForkScanProto, _Mapping]] = ..., resolved_pipe_export_data_scan_node: _Optional[_Union[ResolvedPipeExportDataScanProto, _Mapping]] = ..., resolved_pipe_create_table_scan_node: _Optional[_Union[ResolvedPipeCreateTableScanProto, _Mapping]] = ..., resolved_pipe_tee_scan_node: _Optional[_Union[ResolvedPipeTeeScanProto, _Mapping]] = ..., resolved_pipe_insert_scan_node: _Optional[_Union[ResolvedPipeInsertScanProto, _Mapping]] = ..., resolved_graph_call_scan_node: _Optional[_Union[ResolvedGraphCallScanProto, _Mapping]] = ..., resolved_describe_scan_node: _Optional[_Union[ResolvedDescribeScanProto, _Mapping]] = ..., resolved_unset_argument_scan_node: _Optional[_Union[ResolvedUnsetArgumentScanProto, _Mapping]] = ...) -> None: ...

class ResolvedScanProto(_message.Message):
    __slots__ = ("parent", "column_list", "hint_list", "is_ordered", "node_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_ORDERED_FIELD_NUMBER: _ClassVar[int]
    NODE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: _serialization_pb2.ResolvedNodeProto
    column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    is_ordered: bool
    node_source: str
    def __init__(self, parent: _Optional[_Union[_serialization_pb2.ResolvedNodeProto, _Mapping]] = ..., column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., is_ordered: bool = ..., node_source: _Optional[str] = ...) -> None: ...

class ResolvedExecuteAsRoleScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "original_inlined_view", "original_inlined_tvf")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INLINED_VIEW_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_INLINED_TVF_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    original_inlined_view: _serialization_pb2.TableRefProto
    original_inlined_tvf: _serialization_pb2.TableValuedFunctionRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., original_inlined_view: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ..., original_inlined_tvf: _Optional[_Union[_serialization_pb2.TableValuedFunctionRefProto, _Mapping]] = ...) -> None: ...

class ResolvedModelProto(_message.Message):
    __slots__ = ("parent", "model")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    model: _serialization_pb2.ModelRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., model: _Optional[_Union[_serialization_pb2.ModelRefProto, _Mapping]] = ...) -> None: ...

class ResolvedConnectionProto(_message.Message):
    __slots__ = ("parent", "connection")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    connection: _serialization_pb2.ConnectionRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., connection: _Optional[_Union[_serialization_pb2.ConnectionRefProto, _Mapping]] = ...) -> None: ...

class ResolvedDescriptorProto(_message.Message):
    __slots__ = ("parent", "descriptor_column_list", "descriptor_column_name_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_COLUMN_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    descriptor_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    descriptor_column_name_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., descriptor_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., descriptor_column_name_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedSingleRowScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedUnsetArgumentScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedTableScanProto(_message.Message):
    __slots__ = ("parent", "table", "for_system_time_expr", "column_index_list", "alias", "lock_mode", "read_as_row_type", "table_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    FOR_SYSTEM_TIME_EXPR_FIELD_NUMBER: _ClassVar[int]
    COLUMN_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LOCK_MODE_FIELD_NUMBER: _ClassVar[int]
    READ_AS_ROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    table: _serialization_pb2.TableRefProto
    for_system_time_expr: AnyResolvedExprProto
    column_index_list: _containers.RepeatedScalarFieldContainer[int]
    alias: str
    lock_mode: ResolvedLockModeProto
    read_as_row_type: bool
    table_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., table: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ..., for_system_time_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., column_index_list: _Optional[_Iterable[int]] = ..., alias: _Optional[str] = ..., lock_mode: _Optional[_Union[ResolvedLockModeProto, _Mapping]] = ..., read_as_row_type: bool = ..., table_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedJoinScanProto(_message.Message):
    __slots__ = ("parent", "join_type", "left_scan", "right_scan", "join_expr", "has_using", "is_lateral", "parameter_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEFT_SCAN_FIELD_NUMBER: _ClassVar[int]
    RIGHT_SCAN_FIELD_NUMBER: _ClassVar[int]
    JOIN_EXPR_FIELD_NUMBER: _ClassVar[int]
    HAS_USING_FIELD_NUMBER: _ClassVar[int]
    IS_LATERAL_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    join_type: _resolved_ast_enums_pb2.ResolvedJoinScanEnums.JoinType
    left_scan: AnyResolvedScanProto
    right_scan: AnyResolvedScanProto
    join_expr: AnyResolvedExprProto
    has_using: bool
    is_lateral: bool
    parameter_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., join_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedJoinScanEnums.JoinType, str]] = ..., left_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., right_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., join_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., has_using: bool = ..., is_lateral: bool = ..., parameter_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedArrayScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "array_expr_list", "element_column_list", "array_offset_column", "join_expr", "is_outer", "array_zip_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    ARRAY_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ARRAY_OFFSET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    JOIN_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ZIP_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    array_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    element_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    array_offset_column: ResolvedColumnHolderProto
    join_expr: AnyResolvedExprProto
    is_outer: bool
    array_zip_mode: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., array_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., element_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., array_offset_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., join_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., is_outer: bool = ..., array_zip_mode: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedColumnHolderProto(_message.Message):
    __slots__ = ("parent", "column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedFilterScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "filter_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    filter_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., filter_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGroupingCallProto(_message.Message):
    __slots__ = ("parent", "group_by_column", "output_column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_COLUMN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    group_by_column: ResolvedColumnRefProto
    output_column: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., group_by_column: _Optional[_Union[ResolvedColumnRefProto, _Mapping]] = ..., output_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class AnyResolvedGroupingSetBaseProto(_message.Message):
    __slots__ = ("resolved_grouping_set_node", "resolved_rollup_node", "resolved_cube_node", "resolved_grouping_set_list_node", "resolved_grouping_set_product_node")
    RESOLVED_GROUPING_SET_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ROLLUP_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CUBE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUPING_SET_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GROUPING_SET_PRODUCT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_grouping_set_node: ResolvedGroupingSetProto
    resolved_rollup_node: ResolvedRollupProto
    resolved_cube_node: ResolvedCubeProto
    resolved_grouping_set_list_node: ResolvedGroupingSetListProto
    resolved_grouping_set_product_node: ResolvedGroupingSetProductProto
    def __init__(self, resolved_grouping_set_node: _Optional[_Union[ResolvedGroupingSetProto, _Mapping]] = ..., resolved_rollup_node: _Optional[_Union[ResolvedRollupProto, _Mapping]] = ..., resolved_cube_node: _Optional[_Union[ResolvedCubeProto, _Mapping]] = ..., resolved_grouping_set_list_node: _Optional[_Union[ResolvedGroupingSetListProto, _Mapping]] = ..., resolved_grouping_set_product_node: _Optional[_Union[ResolvedGroupingSetProductProto, _Mapping]] = ...) -> None: ...

class ResolvedGroupingSetBaseProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class ResolvedGroupingSetListProto(_message.Message):
    __slots__ = ("parent", "elem_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGroupingSetBaseProto
    elem_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedGroupingSetBaseProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGroupingSetBaseProto, _Mapping]] = ..., elem_list: _Optional[_Iterable[_Union[AnyResolvedGroupingSetBaseProto, _Mapping]]] = ...) -> None: ...

class ResolvedGroupingSetProductProto(_message.Message):
    __slots__ = ("parent", "input_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGroupingSetBaseProto
    input_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedGroupingSetBaseProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGroupingSetBaseProto, _Mapping]] = ..., input_list: _Optional[_Iterable[_Union[AnyResolvedGroupingSetBaseProto, _Mapping]]] = ...) -> None: ...

class ResolvedGroupingSetProto(_message.Message):
    __slots__ = ("parent", "group_by_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGroupingSetBaseProto
    group_by_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGroupingSetBaseProto, _Mapping]] = ..., group_by_column_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedRollupProto(_message.Message):
    __slots__ = ("parent", "rollup_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGroupingSetBaseProto
    rollup_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedGroupingSetMultiColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGroupingSetBaseProto, _Mapping]] = ..., rollup_column_list: _Optional[_Iterable[_Union[ResolvedGroupingSetMultiColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedCubeProto(_message.Message):
    __slots__ = ("parent", "cube_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUBE_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGroupingSetBaseProto
    cube_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedGroupingSetMultiColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGroupingSetBaseProto, _Mapping]] = ..., cube_column_list: _Optional[_Iterable[_Union[ResolvedGroupingSetMultiColumnProto, _Mapping]]] = ...) -> None: ...

class AnyResolvedAggregateScanBaseProto(_message.Message):
    __slots__ = ("resolved_aggregate_scan_node", "resolved_anonymized_aggregate_scan_node", "resolved_differential_privacy_aggregate_scan_node", "resolved_aggregation_threshold_aggregate_scan_node")
    RESOLVED_AGGREGATE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ANONYMIZED_AGGREGATE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DIFFERENTIAL_PRIVACY_AGGREGATE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AGGREGATION_THRESHOLD_AGGREGATE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_aggregate_scan_node: ResolvedAggregateScanProto
    resolved_anonymized_aggregate_scan_node: ResolvedAnonymizedAggregateScanProto
    resolved_differential_privacy_aggregate_scan_node: ResolvedDifferentialPrivacyAggregateScanProto
    resolved_aggregation_threshold_aggregate_scan_node: ResolvedAggregationThresholdAggregateScanProto
    def __init__(self, resolved_aggregate_scan_node: _Optional[_Union[ResolvedAggregateScanProto, _Mapping]] = ..., resolved_anonymized_aggregate_scan_node: _Optional[_Union[ResolvedAnonymizedAggregateScanProto, _Mapping]] = ..., resolved_differential_privacy_aggregate_scan_node: _Optional[_Union[ResolvedDifferentialPrivacyAggregateScanProto, _Mapping]] = ..., resolved_aggregation_threshold_aggregate_scan_node: _Optional[_Union[ResolvedAggregationThresholdAggregateScanProto, _Mapping]] = ...) -> None: ...

class ResolvedAggregateScanBaseProto(_message.Message):
    __slots__ = ("parent", "input_scan", "group_by_list", "collation_list", "aggregate_list", "grouping_set_list", "rollup_column_list", "grouping_call_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLATION_LIST_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SET_LIST_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUPING_CALL_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    group_by_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    collation_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedCollationProto]
    aggregate_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedComputedColumnBaseProto]
    grouping_set_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedGroupingSetBaseProto]
    rollup_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    grouping_call_list: _containers.RepeatedCompositeFieldContainer[ResolvedGroupingCallProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., group_by_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., collation_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedCollationProto, _Mapping]]] = ..., aggregate_list: _Optional[_Iterable[_Union[AnyResolvedComputedColumnBaseProto, _Mapping]]] = ..., grouping_set_list: _Optional[_Iterable[_Union[AnyResolvedGroupingSetBaseProto, _Mapping]]] = ..., rollup_column_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ..., grouping_call_list: _Optional[_Iterable[_Union[ResolvedGroupingCallProto, _Mapping]]] = ...) -> None: ...

class ResolvedAggregateScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAggregateScanBaseProto
    def __init__(self, parent: _Optional[_Union[ResolvedAggregateScanBaseProto, _Mapping]] = ...) -> None: ...

class ResolvedAnonymizedAggregateScanProto(_message.Message):
    __slots__ = ("parent", "k_threshold_expr", "anonymization_option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    K_THRESHOLD_EXPR_FIELD_NUMBER: _ClassVar[int]
    ANONYMIZATION_OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAggregateScanBaseProto
    k_threshold_expr: AnyResolvedExprProto
    anonymization_option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAggregateScanBaseProto, _Mapping]] = ..., k_threshold_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., anonymization_option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedDifferentialPrivacyAggregateScanProto(_message.Message):
    __slots__ = ("parent", "group_selection_threshold_expr", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SELECTION_THRESHOLD_EXPR_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAggregateScanBaseProto
    group_selection_threshold_expr: AnyResolvedExprProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAggregateScanBaseProto, _Mapping]] = ..., group_selection_threshold_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAggregationThresholdAggregateScanProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAggregateScanBaseProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAggregateScanBaseProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedSetOperationItemProto(_message.Message):
    __slots__ = ("parent", "scan", "output_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    scan: AnyResolvedScanProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedSetOperationScanProto(_message.Message):
    __slots__ = ("parent", "op_type", "input_item_list", "column_match_mode", "column_propagation_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_PROPAGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    op_type: _resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationType
    input_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedSetOperationItemProto]
    column_match_mode: _resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationColumnMatchMode
    column_propagation_mode: _resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., op_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationType, str]] = ..., input_item_list: _Optional[_Iterable[_Union[ResolvedSetOperationItemProto, _Mapping]]] = ..., column_match_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationColumnMatchMode, str]] = ..., column_propagation_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedSetOperationScanEnums.SetOperationColumnPropagationMode, str]] = ...) -> None: ...

class ResolvedOrderByScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "order_by_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    order_by_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedOrderByItemProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., order_by_item_list: _Optional[_Iterable[_Union[ResolvedOrderByItemProto, _Mapping]]] = ...) -> None: ...

class ResolvedLimitOffsetScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "limit", "offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    limit: AnyResolvedExprProto
    offset: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., limit: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., offset: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedWithRefScanProto(_message.Message):
    __slots__ = ("parent", "with_query_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_QUERY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    with_query_name: str
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., with_query_name: _Optional[str] = ...) -> None: ...

class ResolvedAnalyticScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "function_group_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    function_group_list: _containers.RepeatedCompositeFieldContainer[ResolvedAnalyticFunctionGroupProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., function_group_list: _Optional[_Iterable[_Union[ResolvedAnalyticFunctionGroupProto, _Mapping]]] = ...) -> None: ...

class ResolvedSampleScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "method", "size", "unit", "repeatable_argument", "weight_column", "partition_by_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    REPEATABLE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    method: str
    size: AnyResolvedExprProto
    unit: _resolved_ast_enums_pb2.ResolvedSampleScanEnums.SampleUnit
    repeatable_argument: AnyResolvedExprProto
    weight_column: ResolvedColumnHolderProto
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., method: _Optional[str] = ..., size: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., unit: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedSampleScanEnums.SampleUnit, str]] = ..., repeatable_argument: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., weight_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class AnyResolvedComputedColumnBaseProto(_message.Message):
    __slots__ = ("resolved_computed_column_impl_node",)
    RESOLVED_COMPUTED_COLUMN_IMPL_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_computed_column_impl_node: AnyResolvedComputedColumnImplProto
    def __init__(self, resolved_computed_column_impl_node: _Optional[_Union[AnyResolvedComputedColumnImplProto, _Mapping]] = ...) -> None: ...

class ResolvedComputedColumnBaseProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class AnyResolvedComputedColumnImplProto(_message.Message):
    __slots__ = ("resolved_computed_column_node", "resolved_deferred_computed_column_node")
    RESOLVED_COMPUTED_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DEFERRED_COMPUTED_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_computed_column_node: ResolvedComputedColumnProto
    resolved_deferred_computed_column_node: ResolvedDeferredComputedColumnProto
    def __init__(self, resolved_computed_column_node: _Optional[_Union[ResolvedComputedColumnProto, _Mapping]] = ..., resolved_deferred_computed_column_node: _Optional[_Union[ResolvedDeferredComputedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedComputedColumnImplProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedComputedColumnBaseProto
    def __init__(self, parent: _Optional[_Union[ResolvedComputedColumnBaseProto, _Mapping]] = ...) -> None: ...

class ResolvedComputedColumnProto(_message.Message):
    __slots__ = ("parent", "column", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedComputedColumnImplProto
    column: _serialization_pb2.ResolvedColumnProto
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedComputedColumnImplProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedDeferredComputedColumnProto(_message.Message):
    __slots__ = ("parent", "column", "expr", "side_effect_column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    SIDE_EFFECT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedComputedColumnImplProto
    column: _serialization_pb2.ResolvedColumnProto
    expr: AnyResolvedExprProto
    side_effect_column: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedComputedColumnImplProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., side_effect_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedOrderByItemProto(_message.Message):
    __slots__ = ("parent", "column_ref", "collation_name", "is_descending", "null_order", "collation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REF_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DESCENDING_FIELD_NUMBER: _ClassVar[int]
    NULL_ORDER_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column_ref: ResolvedColumnRefProto
    collation_name: AnyResolvedExprProto
    is_descending: bool
    null_order: _resolved_ast_enums_pb2.ResolvedOrderByItemEnums.NullOrderMode
    collation: _serialization_pb2.ResolvedCollationProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column_ref: _Optional[_Union[ResolvedColumnRefProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., is_descending: bool = ..., null_order: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedOrderByItemEnums.NullOrderMode, str]] = ..., collation: _Optional[_Union[_serialization_pb2.ResolvedCollationProto, _Mapping]] = ...) -> None: ...

class ResolvedColumnAnnotationsProto(_message.Message):
    __slots__ = ("parent", "collation_name", "not_null", "option_list", "child_list", "type_parameters")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    NOT_NULL_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    CHILD_LIST_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    collation_name: AnyResolvedExprProto
    not_null: bool
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    child_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnAnnotationsProto]
    type_parameters: _type_parameters_pb2.TypeParametersProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., not_null: bool = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., child_list: _Optional[_Iterable[_Union[ResolvedColumnAnnotationsProto, _Mapping]]] = ..., type_parameters: _Optional[_Union[_type_parameters_pb2.TypeParametersProto, _Mapping]] = ...) -> None: ...

class ResolvedGeneratedColumnInfoProto(_message.Message):
    __slots__ = ("parent", "expression", "stored_mode", "generated_mode", "identity_column_info")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    STORED_MODE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_MODE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expression: AnyResolvedExprProto
    stored_mode: _resolved_ast_enums_pb2.ResolvedGeneratedColumnInfoEnums.StoredMode
    generated_mode: _resolved_ast_enums_pb2.ResolvedGeneratedColumnInfoEnums.GeneratedMode
    identity_column_info: ResolvedIdentityColumnInfoProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., stored_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGeneratedColumnInfoEnums.StoredMode, str]] = ..., generated_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGeneratedColumnInfoEnums.GeneratedMode, str]] = ..., identity_column_info: _Optional[_Union[ResolvedIdentityColumnInfoProto, _Mapping]] = ...) -> None: ...

class ResolvedColumnDefaultValueProto(_message.Message):
    __slots__ = ("parent", "expression", "sql")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expression: AnyResolvedExprProto
    sql: str
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., sql: _Optional[str] = ...) -> None: ...

class ResolvedColumnDefinitionProto(_message.Message):
    __slots__ = ("parent", "name", "type", "annotations", "is_hidden", "column", "generated_column_info", "default_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    type: _type_pb2.TypeProto
    annotations: ResolvedColumnAnnotationsProto
    is_hidden: bool
    column: _serialization_pb2.ResolvedColumnProto
    generated_column_info: ResolvedGeneratedColumnInfoProto
    default_value: ResolvedColumnDefaultValueProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., annotations: _Optional[_Union[ResolvedColumnAnnotationsProto, _Mapping]] = ..., is_hidden: bool = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., generated_column_info: _Optional[_Union[ResolvedGeneratedColumnInfoProto, _Mapping]] = ..., default_value: _Optional[_Union[ResolvedColumnDefaultValueProto, _Mapping]] = ...) -> None: ...

class AnyResolvedConstraintProto(_message.Message):
    __slots__ = ("resolved_primary_key_node", "resolved_foreign_key_node", "resolved_check_constraint_node")
    RESOLVED_PRIMARY_KEY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FOREIGN_KEY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CHECK_CONSTRAINT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_primary_key_node: ResolvedPrimaryKeyProto
    resolved_foreign_key_node: ResolvedForeignKeyProto
    resolved_check_constraint_node: ResolvedCheckConstraintProto
    def __init__(self, resolved_primary_key_node: _Optional[_Union[ResolvedPrimaryKeyProto, _Mapping]] = ..., resolved_foreign_key_node: _Optional[_Union[ResolvedForeignKeyProto, _Mapping]] = ..., resolved_check_constraint_node: _Optional[_Union[ResolvedCheckConstraintProto, _Mapping]] = ...) -> None: ...

class ResolvedConstraintProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class ResolvedPrimaryKeyProto(_message.Message):
    __slots__ = ("parent", "column_offset_list", "option_list", "unenforced", "constraint_name", "column_name_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_OFFSET_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    UNENFORCED_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedConstraintProto
    column_offset_list: _containers.RepeatedScalarFieldContainer[int]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    unenforced: bool
    constraint_name: str
    column_name_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedConstraintProto, _Mapping]] = ..., column_offset_list: _Optional[_Iterable[int]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., unenforced: bool = ..., constraint_name: _Optional[str] = ..., column_name_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedForeignKeyProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "referencing_column_offset_list", "referenced_table", "referenced_column_offset_list", "match_mode", "update_action", "delete_action", "enforced", "option_list", "referencing_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_COLUMN_OFFSET_LIST_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_TABLE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_COLUMN_OFFSET_LIST_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedConstraintProto
    constraint_name: str
    referencing_column_offset_list: _containers.RepeatedScalarFieldContainer[int]
    referenced_table: _serialization_pb2.TableRefProto
    referenced_column_offset_list: _containers.RepeatedScalarFieldContainer[int]
    match_mode: _resolved_ast_enums_pb2.ResolvedForeignKeyEnums.MatchMode
    update_action: _resolved_ast_enums_pb2.ResolvedForeignKeyEnums.ActionOperation
    delete_action: _resolved_ast_enums_pb2.ResolvedForeignKeyEnums.ActionOperation
    enforced: bool
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    referencing_column_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedConstraintProto, _Mapping]] = ..., constraint_name: _Optional[str] = ..., referencing_column_offset_list: _Optional[_Iterable[int]] = ..., referenced_table: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ..., referenced_column_offset_list: _Optional[_Iterable[int]] = ..., match_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedForeignKeyEnums.MatchMode, str]] = ..., update_action: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedForeignKeyEnums.ActionOperation, str]] = ..., delete_action: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedForeignKeyEnums.ActionOperation, str]] = ..., enforced: bool = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., referencing_column_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedCheckConstraintProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "expression", "enforced", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedConstraintProto
    constraint_name: str
    expression: AnyResolvedExprProto
    enforced: bool
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedConstraintProto, _Mapping]] = ..., constraint_name: _Optional[str] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., enforced: bool = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedOutputColumnProto(_message.Message):
    __slots__ = ("parent", "name", "column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    column: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedOutputSchemaProto(_message.Message):
    __slots__ = ("parent", "output_column_list", "is_value_table")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    is_value_table: bool
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., is_value_table: bool = ...) -> None: ...

class ResolvedProjectScanProto(_message.Message):
    __slots__ = ("parent", "expr_list", "input_scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    expr_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    input_scan: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., expr_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedTVFScanProto(_message.Message):
    __slots__ = ("parent", "tvf", "signature", "argument_list", "column_index_list", "alias", "function_call_signature")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TVF_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_CALL_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    tvf: _serialization_pb2.TableValuedFunctionRefProto
    signature: _function_pb2.TVFSignatureProto
    argument_list: _containers.RepeatedCompositeFieldContainer[ResolvedFunctionArgumentProto]
    column_index_list: _containers.RepeatedScalarFieldContainer[int]
    alias: str
    function_call_signature: _function_pb2.FunctionSignatureProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., tvf: _Optional[_Union[_serialization_pb2.TableValuedFunctionRefProto, _Mapping]] = ..., signature: _Optional[_Union[_function_pb2.TVFSignatureProto, _Mapping]] = ..., argument_list: _Optional[_Iterable[_Union[ResolvedFunctionArgumentProto, _Mapping]]] = ..., column_index_list: _Optional[_Iterable[int]] = ..., alias: _Optional[str] = ..., function_call_signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ...) -> None: ...

class ResolvedGroupRowsScanProto(_message.Message):
    __slots__ = ("parent", "input_column_list", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    alias: str
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_column_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., alias: _Optional[str] = ...) -> None: ...

class ResolvedFunctionArgumentProto(_message.Message):
    __slots__ = ("parent", "expr", "scan", "model", "connection", "descriptor_arg", "argument_column_list", "inline_lambda", "sequence", "graph", "argument_alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_ARG_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    INLINE_LAMBDA_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expr: AnyResolvedExprProto
    scan: AnyResolvedScanProto
    model: ResolvedModelProto
    connection: ResolvedConnectionProto
    descriptor_arg: ResolvedDescriptorProto
    argument_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    inline_lambda: ResolvedInlineLambdaProto
    sequence: ResolvedSequenceProto
    graph: _serialization_pb2.PropertyGraphRefProto
    argument_alias: str
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., model: _Optional[_Union[ResolvedModelProto, _Mapping]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., descriptor_arg: _Optional[_Union[ResolvedDescriptorProto, _Mapping]] = ..., argument_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., inline_lambda: _Optional[_Union[ResolvedInlineLambdaProto, _Mapping]] = ..., sequence: _Optional[_Union[ResolvedSequenceProto, _Mapping]] = ..., graph: _Optional[_Union[_serialization_pb2.PropertyGraphRefProto, _Mapping]] = ..., argument_alias: _Optional[str] = ...) -> None: ...

class AnyResolvedStatementProto(_message.Message):
    __slots__ = ("resolved_explain_stmt_node", "resolved_query_stmt_node", "resolved_create_statement_node", "resolved_export_data_stmt_node", "resolved_define_table_stmt_node", "resolved_describe_stmt_node", "resolved_show_stmt_node", "resolved_begin_stmt_node", "resolved_commit_stmt_node", "resolved_rollback_stmt_node", "resolved_drop_stmt_node", "resolved_insert_stmt_node", "resolved_delete_stmt_node", "resolved_update_stmt_node", "resolved_grant_or_revoke_stmt_node", "resolved_alter_table_set_options_stmt_node", "resolved_rename_stmt_node", "resolved_create_row_access_policy_stmt_node", "resolved_drop_row_access_policy_stmt_node", "resolved_drop_function_stmt_node", "resolved_call_stmt_node", "resolved_import_stmt_node", "resolved_module_stmt_node", "resolved_create_database_stmt_node", "resolved_assert_stmt_node", "resolved_merge_stmt_node", "resolved_alter_object_stmt_node", "resolved_set_transaction_stmt_node", "resolved_drop_materialized_view_stmt_node", "resolved_start_batch_stmt_node", "resolved_run_batch_stmt_node", "resolved_abort_batch_stmt_node", "resolved_truncate_stmt_node", "resolved_execute_immediate_stmt_node", "resolved_assignment_stmt_node", "resolved_export_model_stmt_node", "resolved_drop_table_function_stmt_node", "resolved_clone_data_stmt_node", "resolved_analyze_stmt_node", "resolved_drop_snapshot_table_stmt_node", "resolved_aux_load_data_stmt_node", "resolved_drop_privilege_restriction_stmt_node", "resolved_undrop_stmt_node", "resolved_export_metadata_stmt_node", "resolved_drop_index_stmt_node", "resolved_generalized_query_stmt_node", "resolved_multi_stmt_node", "resolved_create_with_entry_stmt_node", "resolved_subpipeline_stmt_node", "resolved_statement_with_pipe_operators_stmt_node")
    RESOLVED_EXPLAIN_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_QUERY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPORT_DATA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DEFINE_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DESCRIBE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SHOW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_BEGIN_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COMMIT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ROLLBACK_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_INSERT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DELETE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UPDATE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRANT_OR_REVOKE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_TABLE_SET_OPTIONS_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RENAME_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_ROW_ACCESS_POLICY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_ROW_ACCESS_POLICY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_FUNCTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CALL_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_IMPORT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MODULE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_DATABASE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ASSERT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MERGE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_OBJECT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SET_TRANSACTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_MATERIALIZED_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_START_BATCH_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RUN_BATCH_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ABORT_BATCH_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TRUNCATE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXECUTE_IMMEDIATE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ASSIGNMENT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPORT_MODEL_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_TABLE_FUNCTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CLONE_DATA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ANALYZE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_SNAPSHOT_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AUX_LOAD_DATA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_PRIVILEGE_RESTRICTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_UNDROP_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_EXPORT_METADATA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_INDEX_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GENERALIZED_QUERY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MULTI_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_WITH_ENTRY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SUBPIPELINE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_STATEMENT_WITH_PIPE_OPERATORS_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_explain_stmt_node: ResolvedExplainStmtProto
    resolved_query_stmt_node: ResolvedQueryStmtProto
    resolved_create_statement_node: AnyResolvedCreateStatementProto
    resolved_export_data_stmt_node: ResolvedExportDataStmtProto
    resolved_define_table_stmt_node: ResolvedDefineTableStmtProto
    resolved_describe_stmt_node: ResolvedDescribeStmtProto
    resolved_show_stmt_node: ResolvedShowStmtProto
    resolved_begin_stmt_node: ResolvedBeginStmtProto
    resolved_commit_stmt_node: ResolvedCommitStmtProto
    resolved_rollback_stmt_node: ResolvedRollbackStmtProto
    resolved_drop_stmt_node: ResolvedDropStmtProto
    resolved_insert_stmt_node: ResolvedInsertStmtProto
    resolved_delete_stmt_node: ResolvedDeleteStmtProto
    resolved_update_stmt_node: ResolvedUpdateStmtProto
    resolved_grant_or_revoke_stmt_node: AnyResolvedGrantOrRevokeStmtProto
    resolved_alter_table_set_options_stmt_node: ResolvedAlterTableSetOptionsStmtProto
    resolved_rename_stmt_node: ResolvedRenameStmtProto
    resolved_create_row_access_policy_stmt_node: ResolvedCreateRowAccessPolicyStmtProto
    resolved_drop_row_access_policy_stmt_node: ResolvedDropRowAccessPolicyStmtProto
    resolved_drop_function_stmt_node: ResolvedDropFunctionStmtProto
    resolved_call_stmt_node: ResolvedCallStmtProto
    resolved_import_stmt_node: ResolvedImportStmtProto
    resolved_module_stmt_node: ResolvedModuleStmtProto
    resolved_create_database_stmt_node: ResolvedCreateDatabaseStmtProto
    resolved_assert_stmt_node: ResolvedAssertStmtProto
    resolved_merge_stmt_node: ResolvedMergeStmtProto
    resolved_alter_object_stmt_node: AnyResolvedAlterObjectStmtProto
    resolved_set_transaction_stmt_node: ResolvedSetTransactionStmtProto
    resolved_drop_materialized_view_stmt_node: ResolvedDropMaterializedViewStmtProto
    resolved_start_batch_stmt_node: ResolvedStartBatchStmtProto
    resolved_run_batch_stmt_node: ResolvedRunBatchStmtProto
    resolved_abort_batch_stmt_node: ResolvedAbortBatchStmtProto
    resolved_truncate_stmt_node: ResolvedTruncateStmtProto
    resolved_execute_immediate_stmt_node: ResolvedExecuteImmediateStmtProto
    resolved_assignment_stmt_node: ResolvedAssignmentStmtProto
    resolved_export_model_stmt_node: ResolvedExportModelStmtProto
    resolved_drop_table_function_stmt_node: ResolvedDropTableFunctionStmtProto
    resolved_clone_data_stmt_node: ResolvedCloneDataStmtProto
    resolved_analyze_stmt_node: ResolvedAnalyzeStmtProto
    resolved_drop_snapshot_table_stmt_node: ResolvedDropSnapshotTableStmtProto
    resolved_aux_load_data_stmt_node: ResolvedAuxLoadDataStmtProto
    resolved_drop_privilege_restriction_stmt_node: ResolvedDropPrivilegeRestrictionStmtProto
    resolved_undrop_stmt_node: ResolvedUndropStmtProto
    resolved_export_metadata_stmt_node: ResolvedExportMetadataStmtProto
    resolved_drop_index_stmt_node: ResolvedDropIndexStmtProto
    resolved_generalized_query_stmt_node: ResolvedGeneralizedQueryStmtProto
    resolved_multi_stmt_node: ResolvedMultiStmtProto
    resolved_create_with_entry_stmt_node: ResolvedCreateWithEntryStmtProto
    resolved_subpipeline_stmt_node: ResolvedSubpipelineStmtProto
    resolved_statement_with_pipe_operators_stmt_node: ResolvedStatementWithPipeOperatorsStmtProto
    def __init__(self, resolved_explain_stmt_node: _Optional[_Union[ResolvedExplainStmtProto, _Mapping]] = ..., resolved_query_stmt_node: _Optional[_Union[ResolvedQueryStmtProto, _Mapping]] = ..., resolved_create_statement_node: _Optional[_Union[AnyResolvedCreateStatementProto, _Mapping]] = ..., resolved_export_data_stmt_node: _Optional[_Union[ResolvedExportDataStmtProto, _Mapping]] = ..., resolved_define_table_stmt_node: _Optional[_Union[ResolvedDefineTableStmtProto, _Mapping]] = ..., resolved_describe_stmt_node: _Optional[_Union[ResolvedDescribeStmtProto, _Mapping]] = ..., resolved_show_stmt_node: _Optional[_Union[ResolvedShowStmtProto, _Mapping]] = ..., resolved_begin_stmt_node: _Optional[_Union[ResolvedBeginStmtProto, _Mapping]] = ..., resolved_commit_stmt_node: _Optional[_Union[ResolvedCommitStmtProto, _Mapping]] = ..., resolved_rollback_stmt_node: _Optional[_Union[ResolvedRollbackStmtProto, _Mapping]] = ..., resolved_drop_stmt_node: _Optional[_Union[ResolvedDropStmtProto, _Mapping]] = ..., resolved_insert_stmt_node: _Optional[_Union[ResolvedInsertStmtProto, _Mapping]] = ..., resolved_delete_stmt_node: _Optional[_Union[ResolvedDeleteStmtProto, _Mapping]] = ..., resolved_update_stmt_node: _Optional[_Union[ResolvedUpdateStmtProto, _Mapping]] = ..., resolved_grant_or_revoke_stmt_node: _Optional[_Union[AnyResolvedGrantOrRevokeStmtProto, _Mapping]] = ..., resolved_alter_table_set_options_stmt_node: _Optional[_Union[ResolvedAlterTableSetOptionsStmtProto, _Mapping]] = ..., resolved_rename_stmt_node: _Optional[_Union[ResolvedRenameStmtProto, _Mapping]] = ..., resolved_create_row_access_policy_stmt_node: _Optional[_Union[ResolvedCreateRowAccessPolicyStmtProto, _Mapping]] = ..., resolved_drop_row_access_policy_stmt_node: _Optional[_Union[ResolvedDropRowAccessPolicyStmtProto, _Mapping]] = ..., resolved_drop_function_stmt_node: _Optional[_Union[ResolvedDropFunctionStmtProto, _Mapping]] = ..., resolved_call_stmt_node: _Optional[_Union[ResolvedCallStmtProto, _Mapping]] = ..., resolved_import_stmt_node: _Optional[_Union[ResolvedImportStmtProto, _Mapping]] = ..., resolved_module_stmt_node: _Optional[_Union[ResolvedModuleStmtProto, _Mapping]] = ..., resolved_create_database_stmt_node: _Optional[_Union[ResolvedCreateDatabaseStmtProto, _Mapping]] = ..., resolved_assert_stmt_node: _Optional[_Union[ResolvedAssertStmtProto, _Mapping]] = ..., resolved_merge_stmt_node: _Optional[_Union[ResolvedMergeStmtProto, _Mapping]] = ..., resolved_alter_object_stmt_node: _Optional[_Union[AnyResolvedAlterObjectStmtProto, _Mapping]] = ..., resolved_set_transaction_stmt_node: _Optional[_Union[ResolvedSetTransactionStmtProto, _Mapping]] = ..., resolved_drop_materialized_view_stmt_node: _Optional[_Union[ResolvedDropMaterializedViewStmtProto, _Mapping]] = ..., resolved_start_batch_stmt_node: _Optional[_Union[ResolvedStartBatchStmtProto, _Mapping]] = ..., resolved_run_batch_stmt_node: _Optional[_Union[ResolvedRunBatchStmtProto, _Mapping]] = ..., resolved_abort_batch_stmt_node: _Optional[_Union[ResolvedAbortBatchStmtProto, _Mapping]] = ..., resolved_truncate_stmt_node: _Optional[_Union[ResolvedTruncateStmtProto, _Mapping]] = ..., resolved_execute_immediate_stmt_node: _Optional[_Union[ResolvedExecuteImmediateStmtProto, _Mapping]] = ..., resolved_assignment_stmt_node: _Optional[_Union[ResolvedAssignmentStmtProto, _Mapping]] = ..., resolved_export_model_stmt_node: _Optional[_Union[ResolvedExportModelStmtProto, _Mapping]] = ..., resolved_drop_table_function_stmt_node: _Optional[_Union[ResolvedDropTableFunctionStmtProto, _Mapping]] = ..., resolved_clone_data_stmt_node: _Optional[_Union[ResolvedCloneDataStmtProto, _Mapping]] = ..., resolved_analyze_stmt_node: _Optional[_Union[ResolvedAnalyzeStmtProto, _Mapping]] = ..., resolved_drop_snapshot_table_stmt_node: _Optional[_Union[ResolvedDropSnapshotTableStmtProto, _Mapping]] = ..., resolved_aux_load_data_stmt_node: _Optional[_Union[ResolvedAuxLoadDataStmtProto, _Mapping]] = ..., resolved_drop_privilege_restriction_stmt_node: _Optional[_Union[ResolvedDropPrivilegeRestrictionStmtProto, _Mapping]] = ..., resolved_undrop_stmt_node: _Optional[_Union[ResolvedUndropStmtProto, _Mapping]] = ..., resolved_export_metadata_stmt_node: _Optional[_Union[ResolvedExportMetadataStmtProto, _Mapping]] = ..., resolved_drop_index_stmt_node: _Optional[_Union[ResolvedDropIndexStmtProto, _Mapping]] = ..., resolved_generalized_query_stmt_node: _Optional[_Union[ResolvedGeneralizedQueryStmtProto, _Mapping]] = ..., resolved_multi_stmt_node: _Optional[_Union[ResolvedMultiStmtProto, _Mapping]] = ..., resolved_create_with_entry_stmt_node: _Optional[_Union[ResolvedCreateWithEntryStmtProto, _Mapping]] = ..., resolved_subpipeline_stmt_node: _Optional[_Union[ResolvedSubpipelineStmtProto, _Mapping]] = ..., resolved_statement_with_pipe_operators_stmt_node: _Optional[_Union[ResolvedStatementWithPipeOperatorsStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedStatementProto(_message.Message):
    __slots__ = ("parent", "hint_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: _serialization_pb2.ResolvedNodeProto
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[_serialization_pb2.ResolvedNodeProto, _Mapping]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedExplainStmtProto(_message.Message):
    __slots__ = ("parent", "statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    statement: AnyResolvedStatementProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., statement: _Optional[_Union[AnyResolvedStatementProto, _Mapping]] = ...) -> None: ...

class ResolvedStatementWithPipeOperatorsStmtProto(_message.Message):
    __slots__ = ("parent", "statement", "suffix_subpipeline_sql")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_SUBPIPELINE_SQL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    statement: AnyResolvedStatementProto
    suffix_subpipeline_sql: str
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., statement: _Optional[_Union[AnyResolvedStatementProto, _Mapping]] = ..., suffix_subpipeline_sql: _Optional[str] = ...) -> None: ...

class ResolvedQueryStmtProto(_message.Message):
    __slots__ = ("parent", "output_column_list", "is_value_table", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    is_value_table: bool
    query: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., is_value_table: bool = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGeneralizedQueryStmtProto(_message.Message):
    __slots__ = ("parent", "output_schema", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    output_schema: ResolvedOutputSchemaProto
    query: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., output_schema: _Optional[_Union[ResolvedOutputSchemaProto, _Mapping]] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedMultiStmtProto(_message.Message):
    __slots__ = ("parent", "statement_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    statement_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedStatementProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., statement_list: _Optional[_Iterable[_Union[AnyResolvedStatementProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateWithEntryStmtProto(_message.Message):
    __slots__ = ("parent", "with_entry")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_ENTRY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    with_entry: ResolvedWithEntryProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., with_entry: _Optional[_Union[ResolvedWithEntryProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateDatabaseStmtProto(_message.Message):
    __slots__ = ("parent", "name_path", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class AnyResolvedCreateStatementProto(_message.Message):
    __slots__ = ("resolved_create_function_stmt_node", "resolved_create_table_function_stmt_node", "resolved_create_index_stmt_node", "resolved_create_constant_stmt_node", "resolved_create_table_stmt_base_node", "resolved_create_model_stmt_node", "resolved_create_view_base_node", "resolved_create_procedure_stmt_node", "resolved_create_entity_stmt_node", "resolved_create_snapshot_table_stmt_node", "resolved_create_privilege_restriction_stmt_node", "resolved_create_property_graph_stmt_node", "resolved_create_schema_stmt_base_node", "resolved_create_connection_stmt_node", "resolved_create_sequence_stmt_node")
    RESOLVED_CREATE_FUNCTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_TABLE_FUNCTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_INDEX_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_CONSTANT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_TABLE_STMT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_MODEL_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_VIEW_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_PROCEDURE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_ENTITY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_SNAPSHOT_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_PRIVILEGE_RESTRICTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_PROPERTY_GRAPH_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_SCHEMA_STMT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_CONNECTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_SEQUENCE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_create_function_stmt_node: ResolvedCreateFunctionStmtProto
    resolved_create_table_function_stmt_node: ResolvedCreateTableFunctionStmtProto
    resolved_create_index_stmt_node: ResolvedCreateIndexStmtProto
    resolved_create_constant_stmt_node: ResolvedCreateConstantStmtProto
    resolved_create_table_stmt_base_node: AnyResolvedCreateTableStmtBaseProto
    resolved_create_model_stmt_node: ResolvedCreateModelStmtProto
    resolved_create_view_base_node: AnyResolvedCreateViewBaseProto
    resolved_create_procedure_stmt_node: ResolvedCreateProcedureStmtProto
    resolved_create_entity_stmt_node: ResolvedCreateEntityStmtProto
    resolved_create_snapshot_table_stmt_node: ResolvedCreateSnapshotTableStmtProto
    resolved_create_privilege_restriction_stmt_node: ResolvedCreatePrivilegeRestrictionStmtProto
    resolved_create_property_graph_stmt_node: ResolvedCreatePropertyGraphStmtProto
    resolved_create_schema_stmt_base_node: AnyResolvedCreateSchemaStmtBaseProto
    resolved_create_connection_stmt_node: ResolvedCreateConnectionStmtProto
    resolved_create_sequence_stmt_node: ResolvedCreateSequenceStmtProto
    def __init__(self, resolved_create_function_stmt_node: _Optional[_Union[ResolvedCreateFunctionStmtProto, _Mapping]] = ..., resolved_create_table_function_stmt_node: _Optional[_Union[ResolvedCreateTableFunctionStmtProto, _Mapping]] = ..., resolved_create_index_stmt_node: _Optional[_Union[ResolvedCreateIndexStmtProto, _Mapping]] = ..., resolved_create_constant_stmt_node: _Optional[_Union[ResolvedCreateConstantStmtProto, _Mapping]] = ..., resolved_create_table_stmt_base_node: _Optional[_Union[AnyResolvedCreateTableStmtBaseProto, _Mapping]] = ..., resolved_create_model_stmt_node: _Optional[_Union[ResolvedCreateModelStmtProto, _Mapping]] = ..., resolved_create_view_base_node: _Optional[_Union[AnyResolvedCreateViewBaseProto, _Mapping]] = ..., resolved_create_procedure_stmt_node: _Optional[_Union[ResolvedCreateProcedureStmtProto, _Mapping]] = ..., resolved_create_entity_stmt_node: _Optional[_Union[ResolvedCreateEntityStmtProto, _Mapping]] = ..., resolved_create_snapshot_table_stmt_node: _Optional[_Union[ResolvedCreateSnapshotTableStmtProto, _Mapping]] = ..., resolved_create_privilege_restriction_stmt_node: _Optional[_Union[ResolvedCreatePrivilegeRestrictionStmtProto, _Mapping]] = ..., resolved_create_property_graph_stmt_node: _Optional[_Union[ResolvedCreatePropertyGraphStmtProto, _Mapping]] = ..., resolved_create_schema_stmt_base_node: _Optional[_Union[AnyResolvedCreateSchemaStmtBaseProto, _Mapping]] = ..., resolved_create_connection_stmt_node: _Optional[_Union[ResolvedCreateConnectionStmtProto, _Mapping]] = ..., resolved_create_sequence_stmt_node: _Optional[_Union[ResolvedCreateSequenceStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateStatementProto(_message.Message):
    __slots__ = ("parent", "name_path", "create_scope", "create_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    create_scope: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateScope
    create_mode: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateMode
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., create_scope: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateScope, str]] = ..., create_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateMode, str]] = ...) -> None: ...

class ResolvedIndexItemProto(_message.Message):
    __slots__ = ("parent", "column_ref", "descending", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REF_FIELD_NUMBER: _ClassVar[int]
    DESCENDING_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column_ref: ResolvedColumnRefProto
    descending: bool
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column_ref: _Optional[_Union[ResolvedColumnRefProto, _Mapping]] = ..., descending: bool = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedUnnestItemProto(_message.Message):
    __slots__ = ("parent", "array_expr", "element_column", "array_offset_column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_EXPR_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    ARRAY_OFFSET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    array_expr: AnyResolvedExprProto
    element_column: _serialization_pb2.ResolvedColumnProto
    array_offset_column: ResolvedColumnHolderProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., array_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., element_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., array_offset_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateIndexStmtProto(_message.Message):
    __slots__ = ("parent", "table_name_path", "table_scan", "is_unique", "is_search", "is_vector", "index_all_columns", "index_item_list", "storing_expression_list", "partition_by_list", "option_list", "computed_columns_list", "unnest_expressions_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    IS_SEARCH_FIELD_NUMBER: _ClassVar[int]
    IS_VECTOR_FIELD_NUMBER: _ClassVar[int]
    INDEX_ALL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    INDEX_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    STORING_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_COLUMNS_LIST_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPRESSIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    table_name_path: _containers.RepeatedScalarFieldContainer[str]
    table_scan: ResolvedTableScanProto
    is_unique: bool
    is_search: bool
    is_vector: bool
    index_all_columns: bool
    index_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedIndexItemProto]
    storing_expression_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    computed_columns_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    unnest_expressions_list: _containers.RepeatedCompositeFieldContainer[ResolvedUnnestItemProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., table_name_path: _Optional[_Iterable[str]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., is_unique: bool = ..., is_search: bool = ..., is_vector: bool = ..., index_all_columns: bool = ..., index_item_list: _Optional[_Iterable[_Union[ResolvedIndexItemProto, _Mapping]]] = ..., storing_expression_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., computed_columns_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., unnest_expressions_list: _Optional[_Iterable[_Union[ResolvedUnnestItemProto, _Mapping]]] = ...) -> None: ...

class AnyResolvedCreateSchemaStmtBaseProto(_message.Message):
    __slots__ = ("resolved_create_schema_stmt_node", "resolved_create_external_schema_stmt_node")
    RESOLVED_CREATE_SCHEMA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_EXTERNAL_SCHEMA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_create_schema_stmt_node: ResolvedCreateSchemaStmtProto
    resolved_create_external_schema_stmt_node: ResolvedCreateExternalSchemaStmtProto
    def __init__(self, resolved_create_schema_stmt_node: _Optional[_Union[ResolvedCreateSchemaStmtProto, _Mapping]] = ..., resolved_create_external_schema_stmt_node: _Optional[_Union[ResolvedCreateExternalSchemaStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateSchemaStmtBaseProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateSchemaStmtProto(_message.Message):
    __slots__ = ("parent", "collation_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateSchemaStmtBaseProto
    collation_name: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateSchemaStmtBaseProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateExternalSchemaStmtProto(_message.Message):
    __slots__ = ("parent", "connection")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateSchemaStmtBaseProto
    connection: ResolvedConnectionProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateSchemaStmtBaseProto, _Mapping]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ...) -> None: ...

class AnyResolvedCreateTableStmtBaseProto(_message.Message):
    __slots__ = ("resolved_create_table_as_select_stmt_node", "resolved_create_external_table_stmt_node", "resolved_create_table_stmt_node")
    RESOLVED_CREATE_TABLE_AS_SELECT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_EXTERNAL_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_create_table_as_select_stmt_node: ResolvedCreateTableAsSelectStmtProto
    resolved_create_external_table_stmt_node: ResolvedCreateExternalTableStmtProto
    resolved_create_table_stmt_node: ResolvedCreateTableStmtProto
    def __init__(self, resolved_create_table_as_select_stmt_node: _Optional[_Union[ResolvedCreateTableAsSelectStmtProto, _Mapping]] = ..., resolved_create_external_table_stmt_node: _Optional[_Union[ResolvedCreateExternalTableStmtProto, _Mapping]] = ..., resolved_create_table_stmt_node: _Optional[_Union[ResolvedCreateTableStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateTableStmtBaseProto(_message.Message):
    __slots__ = ("parent", "option_list", "column_definition_list", "pseudo_column_list", "primary_key", "foreign_key_list", "check_constraint_list", "is_value_table", "like_table", "collation_name", "connection")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    PSEUDO_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    CHECK_CONSTRAINT_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    LIKE_TABLE_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    pseudo_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    primary_key: ResolvedPrimaryKeyProto
    foreign_key_list: _containers.RepeatedCompositeFieldContainer[ResolvedForeignKeyProto]
    check_constraint_list: _containers.RepeatedCompositeFieldContainer[ResolvedCheckConstraintProto]
    is_value_table: bool
    like_table: _serialization_pb2.TableRefProto
    collation_name: AnyResolvedExprProto
    connection: ResolvedConnectionProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ..., pseudo_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., primary_key: _Optional[_Union[ResolvedPrimaryKeyProto, _Mapping]] = ..., foreign_key_list: _Optional[_Iterable[_Union[ResolvedForeignKeyProto, _Mapping]]] = ..., check_constraint_list: _Optional[_Iterable[_Union[ResolvedCheckConstraintProto, _Mapping]]] = ..., is_value_table: bool = ..., like_table: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateTableStmtProto(_message.Message):
    __slots__ = ("parent", "clone_from", "copy_from", "partition_by_list", "cluster_by_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLONE_FROM_FIELD_NUMBER: _ClassVar[int]
    COPY_FROM_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateTableStmtBaseProto
    clone_from: AnyResolvedScanProto
    copy_from: AnyResolvedScanProto
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    cluster_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateTableStmtBaseProto, _Mapping]] = ..., clone_from: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., copy_from: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., cluster_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateTableAsSelectStmtProto(_message.Message):
    __slots__ = ("parent", "partition_by_list", "cluster_by_list", "output_column_list", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateTableStmtBaseProto
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    cluster_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    query: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateTableStmtBaseProto, _Mapping]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., cluster_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateModelAliasedQueryProto(_message.Message):
    __slots__ = ("parent", "alias", "query", "output_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    alias: str
    query: AnyResolvedScanProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., alias: _Optional[str] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateModelStmtProto(_message.Message):
    __slots__ = ("parent", "option_list", "output_column_list", "query", "aliased_query_list", "transform_input_column_list", "transform_list", "transform_output_column_list", "transform_analytic_function_group_list", "input_column_definition_list", "output_column_definition_list", "is_remote", "connection")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ALIASED_QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_INPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_LIST_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ANALYTIC_FUNCTION_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_REMOTE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    query: AnyResolvedScanProto
    aliased_query_list: _containers.RepeatedCompositeFieldContainer[ResolvedCreateModelAliasedQueryProto]
    transform_input_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    transform_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    transform_output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    transform_analytic_function_group_list: _containers.RepeatedCompositeFieldContainer[ResolvedAnalyticFunctionGroupProto]
    input_column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    output_column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    is_remote: bool
    connection: ResolvedConnectionProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., aliased_query_list: _Optional[_Iterable[_Union[ResolvedCreateModelAliasedQueryProto, _Mapping]]] = ..., transform_input_column_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ..., transform_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., transform_output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., transform_analytic_function_group_list: _Optional[_Iterable[_Union[ResolvedAnalyticFunctionGroupProto, _Mapping]]] = ..., input_column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ..., output_column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ..., is_remote: bool = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ...) -> None: ...

class AnyResolvedCreateViewBaseProto(_message.Message):
    __slots__ = ("resolved_create_view_stmt_node", "resolved_create_materialized_view_stmt_node", "resolved_create_approx_view_stmt_node")
    RESOLVED_CREATE_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_MATERIALIZED_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CREATE_APPROX_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_create_view_stmt_node: ResolvedCreateViewStmtProto
    resolved_create_materialized_view_stmt_node: ResolvedCreateMaterializedViewStmtProto
    resolved_create_approx_view_stmt_node: ResolvedCreateApproxViewStmtProto
    def __init__(self, resolved_create_view_stmt_node: _Optional[_Union[ResolvedCreateViewStmtProto, _Mapping]] = ..., resolved_create_materialized_view_stmt_node: _Optional[_Union[ResolvedCreateMaterializedViewStmtProto, _Mapping]] = ..., resolved_create_approx_view_stmt_node: _Optional[_Union[ResolvedCreateApproxViewStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateViewBaseProto(_message.Message):
    __slots__ = ("parent", "option_list", "output_column_list", "has_explicit_columns", "query", "sql", "sql_security", "is_value_table", "recursive", "column_definition_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPLICIT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    has_explicit_columns: bool
    query: AnyResolvedScanProto
    sql: str
    sql_security: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity
    is_value_table: bool
    recursive: bool
    column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., has_explicit_columns: bool = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., sql: _Optional[str] = ..., sql_security: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity, str]] = ..., is_value_table: bool = ..., recursive: bool = ..., column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateViewStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateViewBaseProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateViewBaseProto, _Mapping]] = ...) -> None: ...

class ResolvedWithPartitionColumnsProto(_message.Message):
    __slots__ = ("parent", "column_definition_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateSnapshotTableStmtProto(_message.Message):
    __slots__ = ("parent", "clone_from", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLONE_FROM_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    clone_from: AnyResolvedScanProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., clone_from: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateExternalTableStmtProto(_message.Message):
    __slots__ = ("parent", "with_partition_columns")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_PARTITION_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateTableStmtBaseProto
    with_partition_columns: ResolvedWithPartitionColumnsProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateTableStmtBaseProto, _Mapping]] = ..., with_partition_columns: _Optional[_Union[ResolvedWithPartitionColumnsProto, _Mapping]] = ...) -> None: ...

class ResolvedExportModelStmtProto(_message.Message):
    __slots__ = ("parent", "model_name_path", "connection", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    model_name_path: _containers.RepeatedScalarFieldContainer[str]
    connection: ResolvedConnectionProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., model_name_path: _Optional[_Iterable[str]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedExportDataStmtProto(_message.Message):
    __slots__ = ("parent", "connection", "option_list", "output_column_list", "is_value_table", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    connection: ResolvedConnectionProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    is_value_table: bool
    query: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., is_value_table: bool = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedExportMetadataStmtProto(_message.Message):
    __slots__ = ("parent", "schema_object_kind", "name_path", "connection", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    schema_object_kind: str
    name_path: _containers.RepeatedScalarFieldContainer[str]
    connection: ResolvedConnectionProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., schema_object_kind: _Optional[str] = ..., name_path: _Optional[_Iterable[str]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedDefineTableStmtProto(_message.Message):
    __slots__ = ("parent", "name_path", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedDescribeStmtProto(_message.Message):
    __slots__ = ("parent", "object_type", "name_path", "from_name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    FROM_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    object_type: str
    name_path: _containers.RepeatedScalarFieldContainer[str]
    from_name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., object_type: _Optional[str] = ..., name_path: _Optional[_Iterable[str]] = ..., from_name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedShowStmtProto(_message.Message):
    __slots__ = ("parent", "identifier", "name_path", "like_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    LIKE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    identifier: str
    name_path: _containers.RepeatedScalarFieldContainer[str]
    like_expr: ResolvedLiteralProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., identifier: _Optional[str] = ..., name_path: _Optional[_Iterable[str]] = ..., like_expr: _Optional[_Union[ResolvedLiteralProto, _Mapping]] = ...) -> None: ...

class ResolvedBeginStmtProto(_message.Message):
    __slots__ = ("parent", "read_write_mode", "isolation_level_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    read_write_mode: _resolved_ast_enums_pb2.ResolvedBeginStmtEnums.ReadWriteMode
    isolation_level_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., read_write_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedBeginStmtEnums.ReadWriteMode, str]] = ..., isolation_level_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedSetTransactionStmtProto(_message.Message):
    __slots__ = ("parent", "read_write_mode", "isolation_level_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_LEVEL_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    read_write_mode: _resolved_ast_enums_pb2.ResolvedBeginStmtEnums.ReadWriteMode
    isolation_level_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., read_write_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedBeginStmtEnums.ReadWriteMode, str]] = ..., isolation_level_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedCommitStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ...) -> None: ...

class ResolvedRollbackStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ...) -> None: ...

class ResolvedStartBatchStmtProto(_message.Message):
    __slots__ = ("parent", "batch_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    batch_type: str
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., batch_type: _Optional[str] = ...) -> None: ...

class ResolvedRunBatchStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ...) -> None: ...

class ResolvedAbortBatchStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ...) -> None: ...

class ResolvedDropStmtProto(_message.Message):
    __slots__ = ("parent", "object_type", "is_if_exists", "name_path", "drop_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    DROP_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    object_type: str
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    drop_mode: _resolved_ast_enums_pb2.ResolvedDropStmtEnums.DropMode
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., object_type: _Optional[str] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ..., drop_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedDropStmtEnums.DropMode, str]] = ...) -> None: ...

class ResolvedDropMaterializedViewStmtProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedDropSnapshotTableStmtProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedRecursiveRefScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedRecursionDepthModifierProto(_message.Message):
    __slots__ = ("parent", "lower_bound", "upper_bound", "recursion_depth_column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    RECURSION_DEPTH_COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    lower_bound: AnyResolvedExprProto
    upper_bound: AnyResolvedExprProto
    recursion_depth_column: ResolvedColumnHolderProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., lower_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., upper_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., recursion_depth_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ...) -> None: ...

class ResolvedRecursiveScanProto(_message.Message):
    __slots__ = ("parent", "op_type", "non_recursive_term", "recursive_term", "recursion_depth_modifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    NON_RECURSIVE_TERM_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_TERM_FIELD_NUMBER: _ClassVar[int]
    RECURSION_DEPTH_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    op_type: _resolved_ast_enums_pb2.ResolvedRecursiveScanEnums.RecursiveSetOperationType
    non_recursive_term: ResolvedSetOperationItemProto
    recursive_term: ResolvedSetOperationItemProto
    recursion_depth_modifier: ResolvedRecursionDepthModifierProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., op_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedRecursiveScanEnums.RecursiveSetOperationType, str]] = ..., non_recursive_term: _Optional[_Union[ResolvedSetOperationItemProto, _Mapping]] = ..., recursive_term: _Optional[_Union[ResolvedSetOperationItemProto, _Mapping]] = ..., recursion_depth_modifier: _Optional[_Union[ResolvedRecursionDepthModifierProto, _Mapping]] = ...) -> None: ...

class ResolvedWithScanProto(_message.Message):
    __slots__ = ("parent", "with_entry_list", "query", "recursive")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_ENTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    with_entry_list: _containers.RepeatedCompositeFieldContainer[ResolvedWithEntryProto]
    query: AnyResolvedScanProto
    recursive: bool
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., with_entry_list: _Optional[_Iterable[_Union[ResolvedWithEntryProto, _Mapping]]] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., recursive: bool = ...) -> None: ...

class ResolvedWithEntryProto(_message.Message):
    __slots__ = ("parent", "with_query_name", "with_subquery")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_QUERY_NAME_FIELD_NUMBER: _ClassVar[int]
    WITH_SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    with_query_name: str
    with_subquery: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., with_query_name: _Optional[str] = ..., with_subquery: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedOptionProto(_message.Message):
    __slots__ = ("parent", "qualifier", "name", "value", "assignment_op")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_OP_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    qualifier: str
    name: str
    value: AnyResolvedExprProto
    assignment_op: _resolved_ast_enums_pb2.ResolvedOptionEnums.AssignmentOp
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., qualifier: _Optional[str] = ..., name: _Optional[str] = ..., value: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., assignment_op: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedOptionEnums.AssignmentOp, str]] = ...) -> None: ...

class ResolvedWindowPartitioningProto(_message.Message):
    __slots__ = ("parent", "partition_by_list", "hint_list", "collation_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLATION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    partition_by_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    collation_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedCollationProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., partition_by_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., collation_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedCollationProto, _Mapping]]] = ...) -> None: ...

class ResolvedWindowOrderingProto(_message.Message):
    __slots__ = ("parent", "order_by_item_list", "hint_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    order_by_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedOrderByItemProto]
    hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., order_by_item_list: _Optional[_Iterable[_Union[ResolvedOrderByItemProto, _Mapping]]] = ..., hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedWindowFrameProto(_message.Message):
    __slots__ = ("parent", "frame_unit", "start_expr", "end_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FRAME_UNIT_FIELD_NUMBER: _ClassVar[int]
    START_EXPR_FIELD_NUMBER: _ClassVar[int]
    END_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    frame_unit: _resolved_ast_enums_pb2.ResolvedWindowFrameEnums.FrameUnit
    start_expr: ResolvedWindowFrameExprProto
    end_expr: ResolvedWindowFrameExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., frame_unit: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedWindowFrameEnums.FrameUnit, str]] = ..., start_expr: _Optional[_Union[ResolvedWindowFrameExprProto, _Mapping]] = ..., end_expr: _Optional[_Union[ResolvedWindowFrameExprProto, _Mapping]] = ...) -> None: ...

class ResolvedAnalyticFunctionGroupProto(_message.Message):
    __slots__ = ("parent", "partition_by", "order_by", "analytic_function_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    ANALYTIC_FUNCTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    partition_by: ResolvedWindowPartitioningProto
    order_by: ResolvedWindowOrderingProto
    analytic_function_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedComputedColumnBaseProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., partition_by: _Optional[_Union[ResolvedWindowPartitioningProto, _Mapping]] = ..., order_by: _Optional[_Union[ResolvedWindowOrderingProto, _Mapping]] = ..., analytic_function_list: _Optional[_Iterable[_Union[AnyResolvedComputedColumnBaseProto, _Mapping]]] = ...) -> None: ...

class ResolvedWindowFrameExprProto(_message.Message):
    __slots__ = ("parent", "boundary_type", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    boundary_type: _resolved_ast_enums_pb2.ResolvedWindowFrameExprEnums.BoundaryType
    expression: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., boundary_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedWindowFrameExprEnums.BoundaryType, str]] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedDMLValueProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    value: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., value: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedDMLDefaultProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedAssertStmtProto(_message.Message):
    __slots__ = ("parent", "expression", "description")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    expression: AnyResolvedExprProto
    description: str
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class ResolvedAssertRowsModifiedProto(_message.Message):
    __slots__ = ("parent", "rows")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    rows: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., rows: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedOnConflictClauseProto(_message.Message):
    __slots__ = ("parent", "conflict_action", "conflict_target_column_list", "unique_constraint_name", "insert_row_scan", "update_item_list", "update_where_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_TARGET_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    INSERT_ROW_SCAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_WHERE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    conflict_action: _resolved_ast_enums_pb2.ResolvedOnConflictClauseEnums.ConflictAction
    conflict_target_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    unique_constraint_name: str
    insert_row_scan: ResolvedTableScanProto
    update_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateItemProto]
    update_where_expression: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., conflict_action: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedOnConflictClauseEnums.ConflictAction, str]] = ..., conflict_target_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., unique_constraint_name: _Optional[str] = ..., insert_row_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., update_item_list: _Optional[_Iterable[_Union[ResolvedUpdateItemProto, _Mapping]]] = ..., update_where_expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedInsertRowProto(_message.Message):
    __slots__ = ("parent", "value_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    value_list: _containers.RepeatedCompositeFieldContainer[ResolvedDMLValueProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., value_list: _Optional[_Iterable[_Union[ResolvedDMLValueProto, _Mapping]]] = ...) -> None: ...

class ResolvedInsertStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "insert_mode", "assert_rows_modified", "returning", "insert_column_list", "query_parameter_list", "query", "query_output_column_list", "row_list", "column_access_list", "on_conflict_clause", "topologically_sorted_generated_column_id_list", "generated_column_expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    INSERT_MODE_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    INSERT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETER_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ROW_LIST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ACCESS_LIST_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGICALLY_SORTED_GENERATED_COLUMN_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    insert_mode: _resolved_ast_enums_pb2.ResolvedInsertStmtEnums.InsertMode
    assert_rows_modified: ResolvedAssertRowsModifiedProto
    returning: ResolvedReturningClauseProto
    insert_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    query_parameter_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    query: AnyResolvedScanProto
    query_output_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    row_list: _containers.RepeatedCompositeFieldContainer[ResolvedInsertRowProto]
    column_access_list: _containers.RepeatedScalarFieldContainer[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess]
    on_conflict_clause: ResolvedOnConflictClauseProto
    topologically_sorted_generated_column_id_list: _containers.RepeatedScalarFieldContainer[int]
    generated_column_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., insert_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedInsertStmtEnums.InsertMode, str]] = ..., assert_rows_modified: _Optional[_Union[ResolvedAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ResolvedReturningClauseProto, _Mapping]] = ..., insert_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., query_parameter_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., query_output_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., row_list: _Optional[_Iterable[_Union[ResolvedInsertRowProto, _Mapping]]] = ..., column_access_list: _Optional[_Iterable[_Union[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess, str]]] = ..., on_conflict_clause: _Optional[_Union[ResolvedOnConflictClauseProto, _Mapping]] = ..., topologically_sorted_generated_column_id_list: _Optional[_Iterable[int]] = ..., generated_column_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedDeleteStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "assert_rows_modified", "returning", "column_access_list", "array_offset_column", "where_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ACCESS_LIST_FIELD_NUMBER: _ClassVar[int]
    ARRAY_OFFSET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    assert_rows_modified: ResolvedAssertRowsModifiedProto
    returning: ResolvedReturningClauseProto
    column_access_list: _containers.RepeatedScalarFieldContainer[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess]
    array_offset_column: ResolvedColumnHolderProto
    where_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., assert_rows_modified: _Optional[_Union[ResolvedAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ResolvedReturningClauseProto, _Mapping]] = ..., column_access_list: _Optional[_Iterable[_Union[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess, str]]] = ..., array_offset_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., where_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedUpdateItemProto(_message.Message):
    __slots__ = ("parent", "target", "set_value", "element_column", "update_item_element_list", "delete_list", "update_list", "insert_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SET_VALUE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    DELETE_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_LIST_FIELD_NUMBER: _ClassVar[int]
    INSERT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    target: AnyResolvedExprProto
    set_value: ResolvedDMLValueProto
    element_column: ResolvedColumnHolderProto
    update_item_element_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateItemElementProto]
    delete_list: _containers.RepeatedCompositeFieldContainer[ResolvedDeleteStmtProto]
    update_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateStmtProto]
    insert_list: _containers.RepeatedCompositeFieldContainer[ResolvedInsertStmtProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., target: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., set_value: _Optional[_Union[ResolvedDMLValueProto, _Mapping]] = ..., element_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., update_item_element_list: _Optional[_Iterable[_Union[ResolvedUpdateItemElementProto, _Mapping]]] = ..., delete_list: _Optional[_Iterable[_Union[ResolvedDeleteStmtProto, _Mapping]]] = ..., update_list: _Optional[_Iterable[_Union[ResolvedUpdateStmtProto, _Mapping]]] = ..., insert_list: _Optional[_Iterable[_Union[ResolvedInsertStmtProto, _Mapping]]] = ...) -> None: ...

class ResolvedUpdateItemElementProto(_message.Message):
    __slots__ = ("parent", "subscript", "update_item")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    subscript: AnyResolvedExprProto
    update_item: ResolvedUpdateItemProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., subscript: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., update_item: _Optional[_Union[ResolvedUpdateItemProto, _Mapping]] = ...) -> None: ...

class ResolvedUpdateStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "column_access_list", "assert_rows_modified", "returning", "array_offset_column", "where_expr", "update_item_list", "from_scan", "topologically_sorted_generated_column_id_list", "generated_column_expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ACCESS_LIST_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    ARRAY_OFFSET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    WHERE_EXPR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    FROM_SCAN_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGICALLY_SORTED_GENERATED_COLUMN_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    column_access_list: _containers.RepeatedScalarFieldContainer[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess]
    assert_rows_modified: ResolvedAssertRowsModifiedProto
    returning: ResolvedReturningClauseProto
    array_offset_column: ResolvedColumnHolderProto
    where_expr: AnyResolvedExprProto
    update_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateItemProto]
    from_scan: AnyResolvedScanProto
    topologically_sorted_generated_column_id_list: _containers.RepeatedScalarFieldContainer[int]
    generated_column_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., column_access_list: _Optional[_Iterable[_Union[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess, str]]] = ..., assert_rows_modified: _Optional[_Union[ResolvedAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ResolvedReturningClauseProto, _Mapping]] = ..., array_offset_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., where_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., update_item_list: _Optional[_Iterable[_Union[ResolvedUpdateItemProto, _Mapping]]] = ..., from_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., topologically_sorted_generated_column_id_list: _Optional[_Iterable[int]] = ..., generated_column_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedMergeWhenProto(_message.Message):
    __slots__ = ("parent", "match_type", "match_expr", "action_type", "insert_column_list", "insert_row", "update_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_EXPR_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSERT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    INSERT_ROW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    match_type: _resolved_ast_enums_pb2.ResolvedMergeWhenEnums.MatchType
    match_expr: AnyResolvedExprProto
    action_type: _resolved_ast_enums_pb2.ResolvedMergeWhenEnums.ActionType
    insert_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    insert_row: ResolvedInsertRowProto
    update_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateItemProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., match_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMergeWhenEnums.MatchType, str]] = ..., match_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., action_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMergeWhenEnums.ActionType, str]] = ..., insert_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., insert_row: _Optional[_Union[ResolvedInsertRowProto, _Mapping]] = ..., update_item_list: _Optional[_Iterable[_Union[ResolvedUpdateItemProto, _Mapping]]] = ...) -> None: ...

class ResolvedMergeStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "column_access_list", "from_scan", "merge_expr", "when_clause_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ACCESS_LIST_FIELD_NUMBER: _ClassVar[int]
    FROM_SCAN_FIELD_NUMBER: _ClassVar[int]
    MERGE_EXPR_FIELD_NUMBER: _ClassVar[int]
    WHEN_CLAUSE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    column_access_list: _containers.RepeatedScalarFieldContainer[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess]
    from_scan: AnyResolvedScanProto
    merge_expr: AnyResolvedExprProto
    when_clause_list: _containers.RepeatedCompositeFieldContainer[ResolvedMergeWhenProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., column_access_list: _Optional[_Iterable[_Union[_resolved_ast_enums_pb2.ResolvedStatementEnums.ObjectAccess, str]]] = ..., from_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., merge_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., when_clause_list: _Optional[_Iterable[_Union[ResolvedMergeWhenProto, _Mapping]]] = ...) -> None: ...

class ResolvedTruncateStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "where_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    WHERE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    where_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., where_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedObjectUnitProto(_message.Message):
    __slots__ = ("parent", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedPrivilegeProto(_message.Message):
    __slots__ = ("parent", "action_type", "unit_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    action_type: str
    unit_list: _containers.RepeatedCompositeFieldContainer[ResolvedObjectUnitProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., action_type: _Optional[str] = ..., unit_list: _Optional[_Iterable[_Union[ResolvedObjectUnitProto, _Mapping]]] = ...) -> None: ...

class AnyResolvedGrantOrRevokeStmtProto(_message.Message):
    __slots__ = ("resolved_grant_stmt_node", "resolved_revoke_stmt_node")
    RESOLVED_GRANT_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REVOKE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_grant_stmt_node: ResolvedGrantStmtProto
    resolved_revoke_stmt_node: ResolvedRevokeStmtProto
    def __init__(self, resolved_grant_stmt_node: _Optional[_Union[ResolvedGrantStmtProto, _Mapping]] = ..., resolved_revoke_stmt_node: _Optional[_Union[ResolvedRevokeStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedGrantOrRevokeStmtProto(_message.Message):
    __slots__ = ("parent", "privilege_list", "object_type_list", "name_path", "grantee_list", "grantee_expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_LIST_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    privilege_list: _containers.RepeatedCompositeFieldContainer[ResolvedPrivilegeProto]
    object_type_list: _containers.RepeatedScalarFieldContainer[str]
    name_path: _containers.RepeatedScalarFieldContainer[str]
    grantee_list: _containers.RepeatedScalarFieldContainer[str]
    grantee_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., privilege_list: _Optional[_Iterable[_Union[ResolvedPrivilegeProto, _Mapping]]] = ..., object_type_list: _Optional[_Iterable[str]] = ..., name_path: _Optional[_Iterable[str]] = ..., grantee_list: _Optional[_Iterable[str]] = ..., grantee_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedGrantStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGrantOrRevokeStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedGrantOrRevokeStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedRevokeStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGrantOrRevokeStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedGrantOrRevokeStmtProto, _Mapping]] = ...) -> None: ...

class AnyResolvedAlterObjectStmtProto(_message.Message):
    __slots__ = ("resolved_alter_row_access_policy_stmt_node", "resolved_alter_table_stmt_node", "resolved_alter_view_stmt_node", "resolved_alter_materialized_view_stmt_node", "resolved_alter_database_stmt_node", "resolved_alter_all_row_access_policies_stmt_node", "resolved_alter_entity_stmt_node", "resolved_alter_schema_stmt_node", "resolved_alter_privilege_restriction_stmt_node", "resolved_alter_model_stmt_node", "resolved_alter_approx_view_stmt_node", "resolved_alter_external_schema_stmt_node", "resolved_alter_connection_stmt_node", "resolved_alter_index_stmt_node", "resolved_alter_sequence_stmt_node")
    RESOLVED_ALTER_ROW_ACCESS_POLICY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_TABLE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_MATERIALIZED_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_DATABASE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_ALL_ROW_ACCESS_POLICIES_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_ENTITY_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_SCHEMA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_PRIVILEGE_RESTRICTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_MODEL_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_APPROX_VIEW_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_EXTERNAL_SCHEMA_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_CONNECTION_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_INDEX_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_SEQUENCE_STMT_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_alter_row_access_policy_stmt_node: ResolvedAlterRowAccessPolicyStmtProto
    resolved_alter_table_stmt_node: ResolvedAlterTableStmtProto
    resolved_alter_view_stmt_node: ResolvedAlterViewStmtProto
    resolved_alter_materialized_view_stmt_node: ResolvedAlterMaterializedViewStmtProto
    resolved_alter_database_stmt_node: ResolvedAlterDatabaseStmtProto
    resolved_alter_all_row_access_policies_stmt_node: ResolvedAlterAllRowAccessPoliciesStmtProto
    resolved_alter_entity_stmt_node: ResolvedAlterEntityStmtProto
    resolved_alter_schema_stmt_node: ResolvedAlterSchemaStmtProto
    resolved_alter_privilege_restriction_stmt_node: ResolvedAlterPrivilegeRestrictionStmtProto
    resolved_alter_model_stmt_node: ResolvedAlterModelStmtProto
    resolved_alter_approx_view_stmt_node: ResolvedAlterApproxViewStmtProto
    resolved_alter_external_schema_stmt_node: ResolvedAlterExternalSchemaStmtProto
    resolved_alter_connection_stmt_node: ResolvedAlterConnectionStmtProto
    resolved_alter_index_stmt_node: ResolvedAlterIndexStmtProto
    resolved_alter_sequence_stmt_node: ResolvedAlterSequenceStmtProto
    def __init__(self, resolved_alter_row_access_policy_stmt_node: _Optional[_Union[ResolvedAlterRowAccessPolicyStmtProto, _Mapping]] = ..., resolved_alter_table_stmt_node: _Optional[_Union[ResolvedAlterTableStmtProto, _Mapping]] = ..., resolved_alter_view_stmt_node: _Optional[_Union[ResolvedAlterViewStmtProto, _Mapping]] = ..., resolved_alter_materialized_view_stmt_node: _Optional[_Union[ResolvedAlterMaterializedViewStmtProto, _Mapping]] = ..., resolved_alter_database_stmt_node: _Optional[_Union[ResolvedAlterDatabaseStmtProto, _Mapping]] = ..., resolved_alter_all_row_access_policies_stmt_node: _Optional[_Union[ResolvedAlterAllRowAccessPoliciesStmtProto, _Mapping]] = ..., resolved_alter_entity_stmt_node: _Optional[_Union[ResolvedAlterEntityStmtProto, _Mapping]] = ..., resolved_alter_schema_stmt_node: _Optional[_Union[ResolvedAlterSchemaStmtProto, _Mapping]] = ..., resolved_alter_privilege_restriction_stmt_node: _Optional[_Union[ResolvedAlterPrivilegeRestrictionStmtProto, _Mapping]] = ..., resolved_alter_model_stmt_node: _Optional[_Union[ResolvedAlterModelStmtProto, _Mapping]] = ..., resolved_alter_approx_view_stmt_node: _Optional[_Union[ResolvedAlterApproxViewStmtProto, _Mapping]] = ..., resolved_alter_external_schema_stmt_node: _Optional[_Union[ResolvedAlterExternalSchemaStmtProto, _Mapping]] = ..., resolved_alter_connection_stmt_node: _Optional[_Union[ResolvedAlterConnectionStmtProto, _Mapping]] = ..., resolved_alter_index_stmt_node: _Optional[_Union[ResolvedAlterIndexStmtProto, _Mapping]] = ..., resolved_alter_sequence_stmt_node: _Optional[_Union[ResolvedAlterSequenceStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterObjectStmtProto(_message.Message):
    __slots__ = ("parent", "name_path", "alter_action_list", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    ALTER_ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    alter_action_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedAlterActionProto]
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., alter_action_list: _Optional[_Iterable[_Union[AnyResolvedAlterActionProto, _Mapping]]] = ..., is_if_exists: bool = ...) -> None: ...

class ResolvedAlterDatabaseStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterIndexStmtProto(_message.Message):
    __slots__ = ("parent", "table_name_path", "index_type", "table_scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    table_name_path: _containers.RepeatedScalarFieldContainer[str]
    index_type: _resolved_ast_enums_pb2.ResolvedAlterIndexStmtEnums.AlterIndexType
    table_scan: ResolvedTableScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ..., table_name_path: _Optional[_Iterable[str]] = ..., index_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedAlterIndexStmtEnums.AlterIndexType, str]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterMaterializedViewStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterApproxViewStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterSchemaStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterExternalSchemaStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterModelStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterTableStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterViewStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class AnyResolvedAlterActionProto(_message.Message):
    __slots__ = ("resolved_set_options_action_node", "resolved_add_column_action_node", "resolved_drop_column_action_node", "resolved_grant_to_action_node", "resolved_filter_using_action_node", "resolved_revoke_from_action_node", "resolved_rename_to_action_node", "resolved_set_as_action_node", "resolved_add_constraint_action_node", "resolved_drop_constraint_action_node", "resolved_drop_primary_key_action_node", "resolved_rename_column_action_node", "resolved_set_collate_clause_node", "resolved_restrict_to_action_node", "resolved_add_to_restrictee_list_action_node", "resolved_remove_from_restrictee_list_action_node", "resolved_alter_column_action_node", "resolved_alter_sub_entity_action_node", "resolved_add_sub_entity_action_node", "resolved_drop_sub_entity_action_node", "resolved_add_column_identifier_action_node", "resolved_rebuild_action_node")
    RESOLVED_SET_OPTIONS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ADD_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRANT_TO_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FILTER_USING_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REVOKE_FROM_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RENAME_TO_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SET_AS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ADD_CONSTRAINT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_CONSTRAINT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_PRIMARY_KEY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RENAME_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_SET_COLLATE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_RESTRICT_TO_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ADD_TO_RESTRICTEE_LIST_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REMOVE_FROM_RESTRICTEE_LIST_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ADD_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_DROP_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ADD_COLUMN_IDENTIFIER_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REBUILD_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_set_options_action_node: ResolvedSetOptionsActionProto
    resolved_add_column_action_node: ResolvedAddColumnActionProto
    resolved_drop_column_action_node: ResolvedDropColumnActionProto
    resolved_grant_to_action_node: ResolvedGrantToActionProto
    resolved_filter_using_action_node: ResolvedFilterUsingActionProto
    resolved_revoke_from_action_node: ResolvedRevokeFromActionProto
    resolved_rename_to_action_node: ResolvedRenameToActionProto
    resolved_set_as_action_node: ResolvedSetAsActionProto
    resolved_add_constraint_action_node: ResolvedAddConstraintActionProto
    resolved_drop_constraint_action_node: ResolvedDropConstraintActionProto
    resolved_drop_primary_key_action_node: ResolvedDropPrimaryKeyActionProto
    resolved_rename_column_action_node: ResolvedRenameColumnActionProto
    resolved_set_collate_clause_node: ResolvedSetCollateClauseProto
    resolved_restrict_to_action_node: ResolvedRestrictToActionProto
    resolved_add_to_restrictee_list_action_node: ResolvedAddToRestricteeListActionProto
    resolved_remove_from_restrictee_list_action_node: ResolvedRemoveFromRestricteeListActionProto
    resolved_alter_column_action_node: AnyResolvedAlterColumnActionProto
    resolved_alter_sub_entity_action_node: ResolvedAlterSubEntityActionProto
    resolved_add_sub_entity_action_node: ResolvedAddSubEntityActionProto
    resolved_drop_sub_entity_action_node: ResolvedDropSubEntityActionProto
    resolved_add_column_identifier_action_node: ResolvedAddColumnIdentifierActionProto
    resolved_rebuild_action_node: ResolvedRebuildActionProto
    def __init__(self, resolved_set_options_action_node: _Optional[_Union[ResolvedSetOptionsActionProto, _Mapping]] = ..., resolved_add_column_action_node: _Optional[_Union[ResolvedAddColumnActionProto, _Mapping]] = ..., resolved_drop_column_action_node: _Optional[_Union[ResolvedDropColumnActionProto, _Mapping]] = ..., resolved_grant_to_action_node: _Optional[_Union[ResolvedGrantToActionProto, _Mapping]] = ..., resolved_filter_using_action_node: _Optional[_Union[ResolvedFilterUsingActionProto, _Mapping]] = ..., resolved_revoke_from_action_node: _Optional[_Union[ResolvedRevokeFromActionProto, _Mapping]] = ..., resolved_rename_to_action_node: _Optional[_Union[ResolvedRenameToActionProto, _Mapping]] = ..., resolved_set_as_action_node: _Optional[_Union[ResolvedSetAsActionProto, _Mapping]] = ..., resolved_add_constraint_action_node: _Optional[_Union[ResolvedAddConstraintActionProto, _Mapping]] = ..., resolved_drop_constraint_action_node: _Optional[_Union[ResolvedDropConstraintActionProto, _Mapping]] = ..., resolved_drop_primary_key_action_node: _Optional[_Union[ResolvedDropPrimaryKeyActionProto, _Mapping]] = ..., resolved_rename_column_action_node: _Optional[_Union[ResolvedRenameColumnActionProto, _Mapping]] = ..., resolved_set_collate_clause_node: _Optional[_Union[ResolvedSetCollateClauseProto, _Mapping]] = ..., resolved_restrict_to_action_node: _Optional[_Union[ResolvedRestrictToActionProto, _Mapping]] = ..., resolved_add_to_restrictee_list_action_node: _Optional[_Union[ResolvedAddToRestricteeListActionProto, _Mapping]] = ..., resolved_remove_from_restrictee_list_action_node: _Optional[_Union[ResolvedRemoveFromRestricteeListActionProto, _Mapping]] = ..., resolved_alter_column_action_node: _Optional[_Union[AnyResolvedAlterColumnActionProto, _Mapping]] = ..., resolved_alter_sub_entity_action_node: _Optional[_Union[ResolvedAlterSubEntityActionProto, _Mapping]] = ..., resolved_add_sub_entity_action_node: _Optional[_Union[ResolvedAddSubEntityActionProto, _Mapping]] = ..., resolved_drop_sub_entity_action_node: _Optional[_Union[ResolvedDropSubEntityActionProto, _Mapping]] = ..., resolved_add_column_identifier_action_node: _Optional[_Union[ResolvedAddColumnIdentifierActionProto, _Mapping]] = ..., resolved_rebuild_action_node: _Optional[_Union[ResolvedRebuildActionProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class AnyResolvedAlterColumnActionProto(_message.Message):
    __slots__ = ("resolved_alter_column_options_action_node", "resolved_alter_column_drop_not_null_action_node", "resolved_alter_column_set_data_type_action_node", "resolved_alter_column_set_default_action_node", "resolved_alter_column_drop_default_action_node", "resolved_alter_column_drop_generated_action_node", "resolved_alter_column_set_generated_action_node")
    RESOLVED_ALTER_COLUMN_OPTIONS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_DROP_NOT_NULL_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_SET_DATA_TYPE_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_SET_DEFAULT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_DROP_DEFAULT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_DROP_GENERATED_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_ALTER_COLUMN_SET_GENERATED_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_alter_column_options_action_node: ResolvedAlterColumnOptionsActionProto
    resolved_alter_column_drop_not_null_action_node: ResolvedAlterColumnDropNotNullActionProto
    resolved_alter_column_set_data_type_action_node: ResolvedAlterColumnSetDataTypeActionProto
    resolved_alter_column_set_default_action_node: ResolvedAlterColumnSetDefaultActionProto
    resolved_alter_column_drop_default_action_node: ResolvedAlterColumnDropDefaultActionProto
    resolved_alter_column_drop_generated_action_node: ResolvedAlterColumnDropGeneratedActionProto
    resolved_alter_column_set_generated_action_node: ResolvedAlterColumnSetGeneratedActionProto
    def __init__(self, resolved_alter_column_options_action_node: _Optional[_Union[ResolvedAlterColumnOptionsActionProto, _Mapping]] = ..., resolved_alter_column_drop_not_null_action_node: _Optional[_Union[ResolvedAlterColumnDropNotNullActionProto, _Mapping]] = ..., resolved_alter_column_set_data_type_action_node: _Optional[_Union[ResolvedAlterColumnSetDataTypeActionProto, _Mapping]] = ..., resolved_alter_column_set_default_action_node: _Optional[_Union[ResolvedAlterColumnSetDefaultActionProto, _Mapping]] = ..., resolved_alter_column_drop_default_action_node: _Optional[_Union[ResolvedAlterColumnDropDefaultActionProto, _Mapping]] = ..., resolved_alter_column_drop_generated_action_node: _Optional[_Union[ResolvedAlterColumnDropGeneratedActionProto, _Mapping]] = ..., resolved_alter_column_set_generated_action_node: _Optional[_Union[ResolvedAlterColumnSetGeneratedActionProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    column: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., column: _Optional[str] = ...) -> None: ...

class ResolvedSetOptionsActionProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAlterSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "entity_type", "name", "alter_action", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALTER_ACTION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    entity_type: str
    name: str
    alter_action: AnyResolvedAlterActionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., entity_type: _Optional[str] = ..., name: _Optional[str] = ..., alter_action: _Optional[_Union[AnyResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ResolvedAddSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "entity_type", "name", "options_list", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    entity_type: str
    name: str
    options_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., entity_type: _Optional[str] = ..., name: _Optional[str] = ..., options_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ResolvedDropSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "entity_type", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    entity_type: str
    name: str
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., entity_type: _Optional[str] = ..., name: _Optional[str] = ..., is_if_exists: bool = ...) -> None: ...

class ResolvedAddColumnActionProto(_message.Message):
    __slots__ = ("parent", "is_if_not_exists", "column_definition")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_not_exists: bool
    column_definition: ResolvedColumnDefinitionProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_not_exists: bool = ..., column_definition: _Optional[_Union[ResolvedColumnDefinitionProto, _Mapping]] = ...) -> None: ...

class ResolvedAddColumnIdentifierActionProto(_message.Message):
    __slots__ = ("parent", "name", "options_list", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    name: str
    options_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., name: _Optional[str] = ..., options_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ResolvedRebuildActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ...) -> None: ...

class ResolvedAddConstraintActionProto(_message.Message):
    __slots__ = ("parent", "is_if_not_exists", "constraint", "table")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_not_exists: bool
    constraint: AnyResolvedConstraintProto
    table: _serialization_pb2.TableRefProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_not_exists: bool = ..., constraint: _Optional[_Union[AnyResolvedConstraintProto, _Mapping]] = ..., table: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ...) -> None: ...

class ResolvedDropConstraintActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    name: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., name: _Optional[str] = ...) -> None: ...

class ResolvedDropPrimaryKeyActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ResolvedAlterColumnOptionsActionProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAlterColumnDropNotNullActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnDropGeneratedActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnSetGeneratedActionProto(_message.Message):
    __slots__ = ("parent", "generated_column_info")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    generated_column_info: ResolvedGeneratedColumnInfoProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ..., generated_column_info: _Optional[_Union[ResolvedGeneratedColumnInfoProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnSetDataTypeActionProto(_message.Message):
    __slots__ = ("parent", "updated_type", "updated_type_parameters", "updated_annotations")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    updated_type: _type_pb2.TypeProto
    updated_type_parameters: _type_parameters_pb2.TypeParametersProto
    updated_annotations: ResolvedColumnAnnotationsProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ..., updated_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., updated_type_parameters: _Optional[_Union[_type_parameters_pb2.TypeParametersProto, _Mapping]] = ..., updated_annotations: _Optional[_Union[ResolvedColumnAnnotationsProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnSetDefaultActionProto(_message.Message):
    __slots__ = ("parent", "default_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    default_value: ResolvedColumnDefaultValueProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ..., default_value: _Optional[_Union[ResolvedColumnDefaultValueProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterColumnDropDefaultActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterColumnActionProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterColumnActionProto, _Mapping]] = ...) -> None: ...

class ResolvedDropColumnActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    name: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., name: _Optional[str] = ...) -> None: ...

class ResolvedRenameColumnActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name", "new_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    name: str
    new_name: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., name: _Optional[str] = ..., new_name: _Optional[str] = ...) -> None: ...

class ResolvedSetAsActionProto(_message.Message):
    __slots__ = ("parent", "entity_body_json", "entity_body_text")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BODY_TEXT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    entity_body_json: str
    entity_body_text: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., entity_body_json: _Optional[str] = ..., entity_body_text: _Optional[str] = ...) -> None: ...

class ResolvedSetCollateClauseProto(_message.Message):
    __slots__ = ("parent", "collation_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    collation_name: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterTableSetOptionsStmtProto(_message.Message):
    __slots__ = ("parent", "name_path", "option_list", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., is_if_exists: bool = ...) -> None: ...

class ResolvedRenameStmtProto(_message.Message):
    __slots__ = ("parent", "object_type", "old_name_path", "new_name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OLD_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    object_type: str
    old_name_path: _containers.RepeatedScalarFieldContainer[str]
    new_name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., object_type: _Optional[str] = ..., old_name_path: _Optional[_Iterable[str]] = ..., new_name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedCreatePrivilegeRestrictionStmtProto(_message.Message):
    __slots__ = ("parent", "column_privilege_list", "object_type", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_PRIVILEGE_LIST_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    column_privilege_list: _containers.RepeatedCompositeFieldContainer[ResolvedPrivilegeProto]
    object_type: str
    restrictee_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., column_privilege_list: _Optional[_Iterable[_Union[ResolvedPrivilegeProto, _Mapping]]] = ..., object_type: _Optional[str] = ..., restrictee_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateRowAccessPolicyStmtProto(_message.Message):
    __slots__ = ("parent", "create_mode", "name", "target_name_path", "grantee_list", "grantee_expr_list", "table_scan", "predicate", "predicate_str")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_MODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_STR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    create_mode: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateMode
    name: str
    target_name_path: _containers.RepeatedScalarFieldContainer[str]
    grantee_list: _containers.RepeatedScalarFieldContainer[str]
    grantee_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    table_scan: ResolvedTableScanProto
    predicate: AnyResolvedExprProto
    predicate_str: str
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., create_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.CreateMode, str]] = ..., name: _Optional[str] = ..., target_name_path: _Optional[_Iterable[str]] = ..., grantee_list: _Optional[_Iterable[str]] = ..., grantee_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., predicate: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., predicate_str: _Optional[str] = ...) -> None: ...

class ResolvedDropPrivilegeRestrictionStmtProto(_message.Message):
    __slots__ = ("parent", "object_type", "is_if_exists", "name_path", "column_privilege_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    COLUMN_PRIVILEGE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    object_type: str
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    column_privilege_list: _containers.RepeatedCompositeFieldContainer[ResolvedPrivilegeProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., object_type: _Optional[str] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ..., column_privilege_list: _Optional[_Iterable[_Union[ResolvedPrivilegeProto, _Mapping]]] = ...) -> None: ...

class ResolvedDropRowAccessPolicyStmtProto(_message.Message):
    __slots__ = ("parent", "is_drop_all", "is_if_exists", "name", "target_name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_DROP_ALL_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_drop_all: bool
    is_if_exists: bool
    name: str
    target_name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_drop_all: bool = ..., is_if_exists: bool = ..., name: _Optional[str] = ..., target_name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedDropIndexStmtProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name", "table_name_path", "index_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_if_exists: bool
    name: str
    table_name_path: _containers.RepeatedScalarFieldContainer[str]
    index_type: _resolved_ast_enums_pb2.ResolvedDropIndexStmtEnums.IndexType
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., name: _Optional[str] = ..., table_name_path: _Optional[_Iterable[str]] = ..., index_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedDropIndexStmtEnums.IndexType, str]] = ...) -> None: ...

class ResolvedGrantToActionProto(_message.Message):
    __slots__ = ("parent", "grantee_expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    grantee_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., grantee_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedRestrictToActionProto(_message.Message):
    __slots__ = ("parent", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    restrictee_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., restrictee_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedAddToRestricteeListActionProto(_message.Message):
    __slots__ = ("parent", "is_if_not_exists", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_not_exists: bool
    restrictee_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_not_exists: bool = ..., restrictee_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedRemoveFromRestricteeListActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    is_if_exists: bool
    restrictee_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., restrictee_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedFilterUsingActionProto(_message.Message):
    __slots__ = ("parent", "predicate", "predicate_str")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_STR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    predicate: AnyResolvedExprProto
    predicate_str: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., predicate: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., predicate_str: _Optional[str] = ...) -> None: ...

class ResolvedRevokeFromActionProto(_message.Message):
    __slots__ = ("parent", "revokee_expr_list", "is_revoke_from_all")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REVOKEE_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKE_FROM_ALL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    revokee_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    is_revoke_from_all: bool
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., revokee_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., is_revoke_from_all: bool = ...) -> None: ...

class ResolvedRenameToActionProto(_message.Message):
    __slots__ = ("parent", "new_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterActionProto
    new_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedAlterActionProto, _Mapping]] = ..., new_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedAlterPrivilegeRestrictionStmtProto(_message.Message):
    __slots__ = ("parent", "column_privilege_list", "object_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_PRIVILEGE_LIST_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    column_privilege_list: _containers.RepeatedCompositeFieldContainer[ResolvedPrivilegeProto]
    object_type: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ..., column_privilege_list: _Optional[_Iterable[_Union[ResolvedPrivilegeProto, _Mapping]]] = ..., object_type: _Optional[str] = ...) -> None: ...

class ResolvedAlterRowAccessPolicyStmtProto(_message.Message):
    __slots__ = ("parent", "name", "table_scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    name: str
    table_scan: ResolvedTableScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ..., name: _Optional[str] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ...) -> None: ...

class ResolvedAlterAllRowAccessPoliciesStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    table_scan: ResolvedTableScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateConstantStmtProto(_message.Message):
    __slots__ = ("parent", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateFunctionStmtProto(_message.Message):
    __slots__ = ("parent", "has_explicit_return_type", "return_type", "argument_name_list", "signature", "is_aggregate", "language", "code", "aggregate_expression_list", "function_expression", "option_list", "sql_security", "determinism_level", "is_remote", "connection")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPLICIT_RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    DETERMINISM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_REMOTE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    has_explicit_return_type: bool
    return_type: _type_pb2.TypeProto
    argument_name_list: _containers.RepeatedScalarFieldContainer[str]
    signature: _function_pb2.FunctionSignatureProto
    is_aggregate: bool
    language: str
    code: str
    aggregate_expression_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    function_expression: AnyResolvedExprProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    sql_security: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity
    determinism_level: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.DeterminismLevel
    is_remote: bool
    connection: ResolvedConnectionProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., has_explicit_return_type: bool = ..., return_type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., argument_name_list: _Optional[_Iterable[str]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., is_aggregate: bool = ..., language: _Optional[str] = ..., code: _Optional[str] = ..., aggregate_expression_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., function_expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., sql_security: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity, str]] = ..., determinism_level: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.DeterminismLevel, str]] = ..., is_remote: bool = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ...) -> None: ...

class ResolvedArgumentDefProto(_message.Message):
    __slots__ = ("parent", "name", "type", "argument_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    type: _type_pb2.TypeProto
    argument_kind: _resolved_ast_enums_pb2.ResolvedArgumentDefEnums.ArgumentKind
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ..., argument_kind: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedArgumentDefEnums.ArgumentKind, str]] = ...) -> None: ...

class ResolvedArgumentRefProto(_message.Message):
    __slots__ = ("parent", "name", "argument_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    name: str
    argument_kind: _resolved_ast_enums_pb2.ResolvedArgumentDefEnums.ArgumentKind
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., name: _Optional[str] = ..., argument_kind: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedArgumentDefEnums.ArgumentKind, str]] = ...) -> None: ...

class ResolvedCreateTableFunctionStmtProto(_message.Message):
    __slots__ = ("parent", "argument_name_list", "signature", "has_explicit_return_schema", "option_list", "language", "code", "query", "output_column_list", "is_value_table", "sql_security")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HAS_EXPLICIT_RETURN_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    argument_name_list: _containers.RepeatedScalarFieldContainer[str]
    signature: _function_pb2.FunctionSignatureProto
    has_explicit_return_schema: bool
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    language: str
    code: str
    query: AnyResolvedScanProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    is_value_table: bool
    sql_security: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., argument_name_list: _Optional[_Iterable[str]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., has_explicit_return_schema: bool = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., language: _Optional[str] = ..., code: _Optional[str] = ..., query: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., is_value_table: bool = ..., sql_security: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity, str]] = ...) -> None: ...

class ResolvedRelationArgumentScanProto(_message.Message):
    __slots__ = ("parent", "name", "is_value_table")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_TABLE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    name: str
    is_value_table: bool
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., name: _Optional[str] = ..., is_value_table: bool = ...) -> None: ...

class ResolvedArgumentListProto(_message.Message):
    __slots__ = ("parent", "arg_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARG_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    arg_list: _containers.RepeatedCompositeFieldContainer[ResolvedArgumentDefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., arg_list: _Optional[_Iterable[_Union[ResolvedArgumentDefProto, _Mapping]]] = ...) -> None: ...

class ResolvedFunctionSignatureHolderProto(_message.Message):
    __slots__ = ("parent", "signature")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    signature: _function_pb2.FunctionSignatureProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ...) -> None: ...

class ResolvedDropFunctionStmtProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name_path", "arguments", "signature")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    arguments: ResolvedArgumentListProto
    signature: ResolvedFunctionSignatureHolderProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ..., arguments: _Optional[_Union[ResolvedArgumentListProto, _Mapping]] = ..., signature: _Optional[_Union[ResolvedFunctionSignatureHolderProto, _Mapping]] = ...) -> None: ...

class ResolvedDropTableFunctionStmtProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    is_if_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ...) -> None: ...

class ResolvedCallStmtProto(_message.Message):
    __slots__ = ("parent", "procedure", "signature", "argument_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    procedure: _serialization_pb2.ProcedureRefProto
    signature: _function_pb2.FunctionSignatureProto
    argument_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., procedure: _Optional[_Union[_serialization_pb2.ProcedureRefProto, _Mapping]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., argument_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedImportStmtProto(_message.Message):
    __slots__ = ("parent", "import_kind", "name_path", "file_path", "alias_path", "into_alias_path", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ALIAS_PATH_FIELD_NUMBER: _ClassVar[int]
    INTO_ALIAS_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    import_kind: _resolved_ast_enums_pb2.ResolvedImportStmtEnums.ImportKind
    name_path: _containers.RepeatedScalarFieldContainer[str]
    file_path: str
    alias_path: _containers.RepeatedScalarFieldContainer[str]
    into_alias_path: _containers.RepeatedScalarFieldContainer[str]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., import_kind: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedImportStmtEnums.ImportKind, str]] = ..., name_path: _Optional[_Iterable[str]] = ..., file_path: _Optional[str] = ..., alias_path: _Optional[_Iterable[str]] = ..., into_alias_path: _Optional[_Iterable[str]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedModuleStmtProto(_message.Message):
    __slots__ = ("parent", "name_path", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    name_path: _containers.RepeatedScalarFieldContainer[str]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., name_path: _Optional[_Iterable[str]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAggregateHavingModifierProto(_message.Message):
    __slots__ = ("parent", "kind", "having_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    HAVING_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    kind: _resolved_ast_enums_pb2.ResolvedAggregateHavingModifierEnums.HavingModifierKind
    having_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., kind: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedAggregateHavingModifierEnums.HavingModifierKind, str]] = ..., having_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateMaterializedViewStmtProto(_message.Message):
    __slots__ = ("parent", "partition_by_list", "cluster_by_list", "replica_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateViewBaseProto
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    cluster_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    replica_source: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateViewBaseProto, _Mapping]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., cluster_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., replica_source: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateApproxViewStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateViewBaseProto
    def __init__(self, parent: _Optional[_Union[ResolvedCreateViewBaseProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateProcedureStmtProto(_message.Message):
    __slots__ = ("parent", "argument_name_list", "signature", "option_list", "procedure_body", "connection", "language", "code", "external_security")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_BODY_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    argument_name_list: _containers.RepeatedScalarFieldContainer[str]
    signature: _function_pb2.FunctionSignatureProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    procedure_body: str
    connection: ResolvedConnectionProto
    language: str
    code: str
    external_security: _resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., argument_name_list: _Optional[_Iterable[str]] = ..., signature: _Optional[_Union[_function_pb2.FunctionSignatureProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., procedure_body: _Optional[str] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., language: _Optional[str] = ..., code: _Optional[str] = ..., external_security: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedCreateStatementEnums.SqlSecurity, str]] = ...) -> None: ...

class ResolvedExecuteImmediateArgumentProto(_message.Message):
    __slots__ = ("parent", "name", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    expression: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., expression: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedExecuteImmediateStmtProto(_message.Message):
    __slots__ = ("parent", "sql", "into_identifier_list", "using_argument_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    INTO_IDENTIFIER_LIST_FIELD_NUMBER: _ClassVar[int]
    USING_ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    sql: AnyResolvedExprProto
    into_identifier_list: _containers.RepeatedScalarFieldContainer[str]
    using_argument_list: _containers.RepeatedCompositeFieldContainer[ResolvedExecuteImmediateArgumentProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., sql: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., into_identifier_list: _Optional[_Iterable[str]] = ..., using_argument_list: _Optional[_Iterable[_Union[ResolvedExecuteImmediateArgumentProto, _Mapping]]] = ...) -> None: ...

class ResolvedAssignmentStmtProto(_message.Message):
    __slots__ = ("parent", "target", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    target: AnyResolvedExprProto
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., target: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateEntityStmtProto(_message.Message):
    __slots__ = ("parent", "entity_type", "entity_body_json", "entity_body_text", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BODY_JSON_FIELD_NUMBER: _ClassVar[int]
    ENTITY_BODY_TEXT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    entity_type: str
    entity_body_json: str
    entity_body_text: str
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., entity_type: _Optional[str] = ..., entity_body_json: _Optional[str] = ..., entity_body_text: _Optional[str] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAlterEntityStmtProto(_message.Message):
    __slots__ = ("parent", "entity_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    entity_type: str
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ..., entity_type: _Optional[str] = ...) -> None: ...

class ResolvedPivotColumnProto(_message.Message):
    __slots__ = ("parent", "column", "pivot_expr_index", "pivot_value_index")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    PIVOT_EXPR_INDEX_FIELD_NUMBER: _ClassVar[int]
    PIVOT_VALUE_INDEX_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column: _serialization_pb2.ResolvedColumnProto
    pivot_expr_index: int
    pivot_value_index: int
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., pivot_expr_index: _Optional[int] = ..., pivot_value_index: _Optional[int] = ...) -> None: ...

class ResolvedPivotScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "group_by_list", "pivot_expr_list", "for_expr", "pivot_value_list", "pivot_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    PIVOT_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    FOR_EXPR_FIELD_NUMBER: _ClassVar[int]
    PIVOT_VALUE_LIST_FIELD_NUMBER: _ClassVar[int]
    PIVOT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    group_by_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    pivot_expr_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    for_expr: AnyResolvedExprProto
    pivot_value_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    pivot_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedPivotColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., group_by_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., pivot_expr_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., for_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., pivot_value_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., pivot_column_list: _Optional[_Iterable[_Union[ResolvedPivotColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedReturningClauseProto(_message.Message):
    __slots__ = ("parent", "output_column_list", "action_column", "expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTION_COLUMN_FIELD_NUMBER: _ClassVar[int]
    EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    action_column: ResolvedColumnHolderProto
    expr_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., action_column: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., expr_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedUnpivotArgProto(_message.Message):
    __slots__ = ("parent", "column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    column_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., column_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedUnpivotScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "value_column_list", "label_column", "label_list", "unpivot_arg_list", "projected_input_column_list", "include_nulls")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    VALUE_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    LABEL_COLUMN_FIELD_NUMBER: _ClassVar[int]
    LABEL_LIST_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_ARG_LIST_FIELD_NUMBER: _ClassVar[int]
    PROJECTED_INPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NULLS_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    value_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    label_column: _serialization_pb2.ResolvedColumnProto
    label_list: _containers.RepeatedCompositeFieldContainer[ResolvedLiteralProto]
    unpivot_arg_list: _containers.RepeatedCompositeFieldContainer[ResolvedUnpivotArgProto]
    projected_input_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    include_nulls: bool
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., value_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., label_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., label_list: _Optional[_Iterable[_Union[ResolvedLiteralProto, _Mapping]]] = ..., unpivot_arg_list: _Optional[_Iterable[_Union[ResolvedUnpivotArgProto, _Mapping]]] = ..., projected_input_column_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., include_nulls: bool = ...) -> None: ...

class ResolvedMatchRecognizeScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "option_list", "analytic_function_group_list", "pattern_variable_definition_list", "pattern", "after_match_skip_mode", "measure_group_list", "match_number_column", "match_row_number_column", "classifier_column")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    ANALYTIC_FUNCTION_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    PATTERN_VARIABLE_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    AFTER_MATCH_SKIP_MODE_FIELD_NUMBER: _ClassVar[int]
    MEASURE_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    MATCH_NUMBER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    MATCH_ROW_NUMBER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    analytic_function_group_list: _containers.RepeatedCompositeFieldContainer[ResolvedAnalyticFunctionGroupProto]
    pattern_variable_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedMatchRecognizeVariableDefinitionProto]
    pattern: AnyResolvedMatchRecognizePatternExprProto
    after_match_skip_mode: _resolved_ast_enums_pb2.ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode
    measure_group_list: _containers.RepeatedCompositeFieldContainer[ResolvedMeasureGroupProto]
    match_number_column: _serialization_pb2.ResolvedColumnProto
    match_row_number_column: _serialization_pb2.ResolvedColumnProto
    classifier_column: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., analytic_function_group_list: _Optional[_Iterable[_Union[ResolvedAnalyticFunctionGroupProto, _Mapping]]] = ..., pattern_variable_definition_list: _Optional[_Iterable[_Union[ResolvedMatchRecognizeVariableDefinitionProto, _Mapping]]] = ..., pattern: _Optional[_Union[AnyResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., after_match_skip_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMatchRecognizeScanEnums.AfterMatchSkipMode, str]] = ..., measure_group_list: _Optional[_Iterable[_Union[ResolvedMeasureGroupProto, _Mapping]]] = ..., match_number_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., match_row_number_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., classifier_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedMeasureGroupProto(_message.Message):
    __slots__ = ("parent", "pattern_variable_ref", "aggregate_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATTERN_VARIABLE_REF_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    pattern_variable_ref: ResolvedMatchRecognizePatternVariableRefProto
    aggregate_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedComputedColumnBaseProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., pattern_variable_ref: _Optional[_Union[ResolvedMatchRecognizePatternVariableRefProto, _Mapping]] = ..., aggregate_list: _Optional[_Iterable[_Union[AnyResolvedComputedColumnBaseProto, _Mapping]]] = ...) -> None: ...

class ResolvedMatchRecognizeVariableDefinitionProto(_message.Message):
    __slots__ = ("parent", "name", "predicate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    predicate: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., predicate: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class AnyResolvedMatchRecognizePatternExprProto(_message.Message):
    __slots__ = ("resolved_match_recognize_pattern_empty_node", "resolved_match_recognize_pattern_variable_ref_node", "resolved_match_recognize_pattern_operation_node", "resolved_match_recognize_pattern_quantification_node", "resolved_match_recognize_pattern_anchor_node")
    RESOLVED_MATCH_RECOGNIZE_PATTERN_EMPTY_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_PATTERN_VARIABLE_REF_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_PATTERN_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_PATTERN_QUANTIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MATCH_RECOGNIZE_PATTERN_ANCHOR_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_match_recognize_pattern_empty_node: ResolvedMatchRecognizePatternEmptyProto
    resolved_match_recognize_pattern_variable_ref_node: ResolvedMatchRecognizePatternVariableRefProto
    resolved_match_recognize_pattern_operation_node: ResolvedMatchRecognizePatternOperationProto
    resolved_match_recognize_pattern_quantification_node: ResolvedMatchRecognizePatternQuantificationProto
    resolved_match_recognize_pattern_anchor_node: ResolvedMatchRecognizePatternAnchorProto
    def __init__(self, resolved_match_recognize_pattern_empty_node: _Optional[_Union[ResolvedMatchRecognizePatternEmptyProto, _Mapping]] = ..., resolved_match_recognize_pattern_variable_ref_node: _Optional[_Union[ResolvedMatchRecognizePatternVariableRefProto, _Mapping]] = ..., resolved_match_recognize_pattern_operation_node: _Optional[_Union[ResolvedMatchRecognizePatternOperationProto, _Mapping]] = ..., resolved_match_recognize_pattern_quantification_node: _Optional[_Union[ResolvedMatchRecognizePatternQuantificationProto, _Mapping]] = ..., resolved_match_recognize_pattern_anchor_node: _Optional[_Union[ResolvedMatchRecognizePatternAnchorProto, _Mapping]] = ...) -> None: ...

class ResolvedMatchRecognizePatternExprProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class ResolvedMatchRecognizePatternEmptyProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedMatchRecognizePatternExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedMatchRecognizePatternExprProto, _Mapping]] = ...) -> None: ...

class ResolvedMatchRecognizePatternAnchorProto(_message.Message):
    __slots__ = ("parent", "mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedMatchRecognizePatternExprProto
    mode: _resolved_ast_enums_pb2.ResolvedMatchRecognizePatternAnchorEnums.Mode
    def __init__(self, parent: _Optional[_Union[ResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMatchRecognizePatternAnchorEnums.Mode, str]] = ...) -> None: ...

class ResolvedMatchRecognizePatternVariableRefProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedMatchRecognizePatternExprProto
    name: str
    def __init__(self, parent: _Optional[_Union[ResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ResolvedMatchRecognizePatternOperationProto(_message.Message):
    __slots__ = ("parent", "op_type", "operand_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERAND_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedMatchRecognizePatternExprProto
    op_type: _resolved_ast_enums_pb2.ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType
    operand_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedMatchRecognizePatternExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., op_type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedMatchRecognizePatternOperationEnums.MatchRecognizePatternOperationType, str]] = ..., operand_list: _Optional[_Iterable[_Union[AnyResolvedMatchRecognizePatternExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedMatchRecognizePatternQuantificationProto(_message.Message):
    __slots__ = ("parent", "operand", "lower_bound", "upper_bound", "is_reluctant")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    IS_RELUCTANT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedMatchRecognizePatternExprProto
    operand: AnyResolvedMatchRecognizePatternExprProto
    lower_bound: AnyResolvedExprProto
    upper_bound: AnyResolvedExprProto
    is_reluctant: bool
    def __init__(self, parent: _Optional[_Union[ResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., operand: _Optional[_Union[AnyResolvedMatchRecognizePatternExprProto, _Mapping]] = ..., lower_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., upper_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., is_reluctant: bool = ...) -> None: ...

class ResolvedCloneDataStmtProto(_message.Message):
    __slots__ = ("parent", "target_table", "clone_from")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TABLE_FIELD_NUMBER: _ClassVar[int]
    CLONE_FROM_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    target_table: ResolvedTableScanProto
    clone_from: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., target_table: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., clone_from: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedTableAndColumnInfoProto(_message.Message):
    __slots__ = ("parent", "table", "column_index_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    table: _serialization_pb2.TableRefProto
    column_index_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., table: _Optional[_Union[_serialization_pb2.TableRefProto, _Mapping]] = ..., column_index_list: _Optional[_Iterable[int]] = ...) -> None: ...

class ResolvedAnalyzeStmtProto(_message.Message):
    __slots__ = ("parent", "option_list", "table_and_column_index_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    TABLE_AND_COLUMN_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    table_and_column_index_list: _containers.RepeatedCompositeFieldContainer[ResolvedTableAndColumnInfoProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., table_and_column_index_list: _Optional[_Iterable[_Union[ResolvedTableAndColumnInfoProto, _Mapping]]] = ...) -> None: ...

class ResolvedAuxLoadDataPartitionFilterProto(_message.Message):
    __slots__ = ("parent", "filter", "is_overwrite")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    filter: AnyResolvedExprProto
    is_overwrite: bool
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., filter: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., is_overwrite: bool = ...) -> None: ...

class ResolvedAuxLoadDataStmtProto(_message.Message):
    __slots__ = ("parent", "insertion_mode", "is_temp_table", "name_path", "partition_filter", "output_column_list", "column_definition_list", "pseudo_column_list", "primary_key", "foreign_key_list", "check_constraint_list", "partition_by_list", "cluster_by_list", "option_list", "with_partition_columns", "connection", "from_files_option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSERTION_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_TEMP_TABLE_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    PSEUDO_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    CHECK_CONSTRAINT_LIST_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    WITH_PARTITION_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    FROM_FILES_OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    insertion_mode: _resolved_ast_enums_pb2.ResolvedAuxLoadDataStmtEnums.InsertionMode
    is_temp_table: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    partition_filter: ResolvedAuxLoadDataPartitionFilterProto
    output_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedOutputColumnProto]
    column_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnDefinitionProto]
    pseudo_column_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.ResolvedColumnProto]
    primary_key: ResolvedPrimaryKeyProto
    foreign_key_list: _containers.RepeatedCompositeFieldContainer[ResolvedForeignKeyProto]
    check_constraint_list: _containers.RepeatedCompositeFieldContainer[ResolvedCheckConstraintProto]
    partition_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    cluster_by_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    with_partition_columns: ResolvedWithPartitionColumnsProto
    connection: ResolvedConnectionProto
    from_files_option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., insertion_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedAuxLoadDataStmtEnums.InsertionMode, str]] = ..., is_temp_table: bool = ..., name_path: _Optional[_Iterable[str]] = ..., partition_filter: _Optional[_Union[ResolvedAuxLoadDataPartitionFilterProto, _Mapping]] = ..., output_column_list: _Optional[_Iterable[_Union[ResolvedOutputColumnProto, _Mapping]]] = ..., column_definition_list: _Optional[_Iterable[_Union[ResolvedColumnDefinitionProto, _Mapping]]] = ..., pseudo_column_list: _Optional[_Iterable[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]]] = ..., primary_key: _Optional[_Union[ResolvedPrimaryKeyProto, _Mapping]] = ..., foreign_key_list: _Optional[_Iterable[_Union[ResolvedForeignKeyProto, _Mapping]]] = ..., check_constraint_list: _Optional[_Iterable[_Union[ResolvedCheckConstraintProto, _Mapping]]] = ..., partition_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., cluster_by_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., with_partition_columns: _Optional[_Union[ResolvedWithPartitionColumnsProto, _Mapping]] = ..., connection: _Optional[_Union[ResolvedConnectionProto, _Mapping]] = ..., from_files_option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreatePropertyGraphStmtProto(_message.Message):
    __slots__ = ("parent", "node_table_list", "edge_table_list", "label_list", "property_declaration_list", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    LABEL_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATION_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    node_table_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphElementTableProto]
    edge_table_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphElementTableProto]
    label_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphElementLabelProto]
    property_declaration_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphPropertyDeclarationProto]
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., node_table_list: _Optional[_Iterable[_Union[ResolvedGraphElementTableProto, _Mapping]]] = ..., edge_table_list: _Optional[_Iterable[_Union[ResolvedGraphElementTableProto, _Mapping]]] = ..., label_list: _Optional[_Iterable[_Union[ResolvedGraphElementLabelProto, _Mapping]]] = ..., property_declaration_list: _Optional[_Iterable[_Union[ResolvedGraphPropertyDeclarationProto, _Mapping]]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphElementTableProto(_message.Message):
    __slots__ = ("parent", "alias", "input_scan", "key_list", "source_node_reference", "dest_node_reference", "label_name_list", "property_definition_list", "dynamic_label", "dynamic_properties")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DEST_NODE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    LABEL_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LABEL_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    alias: str
    input_scan: AnyResolvedScanProto
    key_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    source_node_reference: ResolvedGraphNodeTableReferenceProto
    dest_node_reference: ResolvedGraphNodeTableReferenceProto
    label_name_list: _containers.RepeatedScalarFieldContainer[str]
    property_definition_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphPropertyDefinitionProto]
    dynamic_label: ResolvedGraphDynamicLabelSpecificationProto
    dynamic_properties: ResolvedGraphDynamicPropertiesSpecificationProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., alias: _Optional[str] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., key_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., source_node_reference: _Optional[_Union[ResolvedGraphNodeTableReferenceProto, _Mapping]] = ..., dest_node_reference: _Optional[_Union[ResolvedGraphNodeTableReferenceProto, _Mapping]] = ..., label_name_list: _Optional[_Iterable[str]] = ..., property_definition_list: _Optional[_Iterable[_Union[ResolvedGraphPropertyDefinitionProto, _Mapping]]] = ..., dynamic_label: _Optional[_Union[ResolvedGraphDynamicLabelSpecificationProto, _Mapping]] = ..., dynamic_properties: _Optional[_Union[ResolvedGraphDynamicPropertiesSpecificationProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphNodeTableReferenceProto(_message.Message):
    __slots__ = ("parent", "node_table_identifier", "edge_table_column_list", "node_table_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    node_table_identifier: str
    edge_table_column_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    node_table_column_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., node_table_identifier: _Optional[str] = ..., edge_table_column_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., node_table_column_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphElementLabelProto(_message.Message):
    __slots__ = ("parent", "name", "property_declaration_name_list", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATION_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    property_declaration_name_list: _containers.RepeatedScalarFieldContainer[str]
    options_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., property_declaration_name_list: _Optional[_Iterable[str]] = ..., options_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphPropertyDeclarationProto(_message.Message):
    __slots__ = ("parent", "name", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    name: str
    type: _type_pb2.TypeProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphPropertyDefinitionProto(_message.Message):
    __slots__ = ("parent", "expr", "sql", "property_declaration_name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DECLARATION_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expr: AnyResolvedExprProto
    sql: str
    property_declaration_name: str
    options_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., sql: _Optional[str] = ..., property_declaration_name: _Optional[str] = ..., options_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphDynamicLabelSpecificationProto(_message.Message):
    __slots__ = ("parent", "label_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    label_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., label_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphDynamicPropertiesSpecificationProto(_message.Message):
    __slots__ = ("parent", "property_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    property_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., property_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class AnyResolvedGraphScanBaseProto(_message.Message):
    __slots__ = ("resolved_graph_scan_node", "resolved_graph_linear_scan_node")
    RESOLVED_GRAPH_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_LINEAR_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_graph_scan_node: ResolvedGraphScanProto
    resolved_graph_linear_scan_node: ResolvedGraphLinearScanProto
    def __init__(self, resolved_graph_scan_node: _Optional[_Union[ResolvedGraphScanProto, _Mapping]] = ..., resolved_graph_linear_scan_node: _Optional[_Union[ResolvedGraphLinearScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphScanBaseProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphRefScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphLinearScanProto(_message.Message):
    __slots__ = ("parent", "scan_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphScanBaseProto
    scan_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedScanProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGraphScanBaseProto, _Mapping]] = ..., scan_list: _Optional[_Iterable[_Union[AnyResolvedScanProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphTableScanProto(_message.Message):
    __slots__ = ("parent", "property_graph", "input_scan", "shape_expr_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_GRAPH_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    SHAPE_EXPR_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    property_graph: _serialization_pb2.PropertyGraphRefProto
    input_scan: AnyResolvedGraphScanBaseProto
    shape_expr_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., property_graph: _Optional[_Union[_serialization_pb2.PropertyGraphRefProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedGraphScanBaseProto, _Mapping]] = ..., shape_expr_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphCallScanProto(_message.Message):
    __slots__ = ("parent", "optional", "subquery", "input_scan", "parameter_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    optional: bool
    subquery: AnyResolvedScanProto
    input_scan: AnyResolvedScanProto
    parameter_list: _containers.RepeatedCompositeFieldContainer[ResolvedColumnRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., optional: bool = ..., subquery: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., parameter_list: _Optional[_Iterable[_Union[ResolvedColumnRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphScanProto(_message.Message):
    __slots__ = ("parent", "input_scan_list", "filter_expr", "input_scan", "optional")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_LIST_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPR_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphScanBaseProto
    input_scan_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphPathScanProto]
    filter_expr: AnyResolvedExprProto
    input_scan: AnyResolvedScanProto
    optional: bool
    def __init__(self, parent: _Optional[_Union[ResolvedGraphScanBaseProto, _Mapping]] = ..., input_scan_list: _Optional[_Iterable[_Union[ResolvedGraphPathScanProto, _Mapping]]] = ..., filter_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., optional: bool = ...) -> None: ...

class ResolvedGraphPathPatternQuantifierProto(_message.Message):
    __slots__ = ("parent", "lower_bound", "upper_bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    lower_bound: AnyResolvedExprProto
    upper_bound: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., lower_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., upper_bound: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphPathSearchPrefixProto(_message.Message):
    __slots__ = ("parent", "type", "path_count")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_COUNT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    type: _resolved_ast_enums_pb2.ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType
    path_count: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., type: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGraphPathSearchPrefixEnums.PathSearchPrefixType, str]] = ..., path_count: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class AnyResolvedGraphPathScanBaseProto(_message.Message):
    __slots__ = ("resolved_graph_element_scan_node", "resolved_graph_path_scan_node")
    RESOLVED_GRAPH_ELEMENT_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_PATH_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_graph_element_scan_node: AnyResolvedGraphElementScanProto
    resolved_graph_path_scan_node: ResolvedGraphPathScanProto
    def __init__(self, resolved_graph_element_scan_node: _Optional[_Union[AnyResolvedGraphElementScanProto, _Mapping]] = ..., resolved_graph_path_scan_node: _Optional[_Union[ResolvedGraphPathScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphPathScanBaseProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class AnyResolvedGraphElementScanProto(_message.Message):
    __slots__ = ("resolved_graph_node_scan_node", "resolved_graph_edge_scan_node")
    RESOLVED_GRAPH_NODE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_EDGE_SCAN_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_graph_node_scan_node: ResolvedGraphNodeScanProto
    resolved_graph_edge_scan_node: ResolvedGraphEdgeScanProto
    def __init__(self, resolved_graph_node_scan_node: _Optional[_Union[ResolvedGraphNodeScanProto, _Mapping]] = ..., resolved_graph_edge_scan_node: _Optional[_Union[ResolvedGraphEdgeScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphElementScanProto(_message.Message):
    __slots__ = ("parent", "filter_expr", "label_expr", "target_element_table_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPR_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXPR_FIELD_NUMBER: _ClassVar[int]
    TARGET_ELEMENT_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphPathScanBaseProto
    filter_expr: AnyResolvedExprProto
    label_expr: AnyResolvedGraphLabelExprProto
    target_element_table_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.GraphElementTableRefProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGraphPathScanBaseProto, _Mapping]] = ..., filter_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., label_expr: _Optional[_Union[AnyResolvedGraphLabelExprProto, _Mapping]] = ..., target_element_table_list: _Optional[_Iterable[_Union[_serialization_pb2.GraphElementTableRefProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphNodeScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphElementScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedGraphElementScanProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphEdgeScanProto(_message.Message):
    __slots__ = ("parent", "orientation", "lhs_hint_list", "rhs_hint_list", "cost_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    LHS_HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    RHS_HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    COST_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphElementScanProto
    orientation: _resolved_ast_enums_pb2.ResolvedGraphEdgeScanEnums.EdgeOrientation
    lhs_hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    rhs_hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    cost_expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedGraphElementScanProto, _Mapping]] = ..., orientation: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGraphEdgeScanEnums.EdgeOrientation, str]] = ..., lhs_hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., rhs_hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., cost_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphGetElementPropertyProto(_message.Message):
    __slots__ = ("parent", "expr", "property", "property_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    property: _serialization_pb2.GraphPropertyDeclarationRefProto
    property_name: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., property: _Optional[_Union[_serialization_pb2.GraphPropertyDeclarationRefProto, _Mapping]] = ..., property_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class AnyResolvedGraphLabelExprProto(_message.Message):
    __slots__ = ("resolved_graph_label_nary_expr_node", "resolved_graph_label_node", "resolved_graph_wild_card_label_node")
    RESOLVED_GRAPH_LABEL_NARY_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GRAPH_WILD_CARD_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    resolved_graph_label_nary_expr_node: ResolvedGraphLabelNaryExprProto
    resolved_graph_label_node: ResolvedGraphLabelProto
    resolved_graph_wild_card_label_node: ResolvedGraphWildCardLabelProto
    def __init__(self, resolved_graph_label_nary_expr_node: _Optional[_Union[ResolvedGraphLabelNaryExprProto, _Mapping]] = ..., resolved_graph_label_node: _Optional[_Union[ResolvedGraphLabelProto, _Mapping]] = ..., resolved_graph_wild_card_label_node: _Optional[_Union[ResolvedGraphWildCardLabelProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphLabelExprProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphLabelNaryExprProto(_message.Message):
    __slots__ = ("parent", "op", "operand_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    OPERAND_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphLabelExprProto
    op: _resolved_ast_enums_pb2.ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType
    operand_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedGraphLabelExprProto]
    def __init__(self, parent: _Optional[_Union[ResolvedGraphLabelExprProto, _Mapping]] = ..., op: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGraphLabelNaryExprEnums.GraphLogicalOpType, str]] = ..., operand_list: _Optional[_Iterable[_Union[AnyResolvedGraphLabelExprProto, _Mapping]]] = ...) -> None: ...

class ResolvedGraphLabelProto(_message.Message):
    __slots__ = ("parent", "label", "label_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LABEL_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphLabelExprProto
    label: _serialization_pb2.GraphElementLabelRefProto
    label_name: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedGraphLabelExprProto, _Mapping]] = ..., label: _Optional[_Union[_serialization_pb2.GraphElementLabelRefProto, _Mapping]] = ..., label_name: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphWildCardLabelProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphLabelExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedGraphLabelExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphElementIdentifierProto(_message.Message):
    __slots__ = ("parent", "element_table", "key_list", "source_node_identifier", "dest_node_identifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TABLE_FIELD_NUMBER: _ClassVar[int]
    KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DEST_NODE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    element_table: _serialization_pb2.GraphElementTableRefProto
    key_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedExprProto]
    source_node_identifier: ResolvedGraphElementIdentifierProto
    dest_node_identifier: ResolvedGraphElementIdentifierProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., element_table: _Optional[_Union[_serialization_pb2.GraphElementTableRefProto, _Mapping]] = ..., key_list: _Optional[_Iterable[_Union[AnyResolvedExprProto, _Mapping]]] = ..., source_node_identifier: _Optional[_Union[ResolvedGraphElementIdentifierProto, _Mapping]] = ..., dest_node_identifier: _Optional[_Union[ResolvedGraphElementIdentifierProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphElementPropertyProto(_message.Message):
    __slots__ = ("parent", "declaration", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    declaration: _serialization_pb2.GraphPropertyDeclarationRefProto
    expr: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., declaration: _Optional[_Union[_serialization_pb2.GraphPropertyDeclarationRefProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphMakeElementProto(_message.Message):
    __slots__ = ("parent", "identifier", "property_list", "label_list", "dynamic_labels", "dynamic_properties")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    LABEL_LIST_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LABELS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    identifier: ResolvedGraphElementIdentifierProto
    property_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphElementPropertyProto]
    label_list: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.GraphElementLabelRefProto]
    dynamic_labels: AnyResolvedExprProto
    dynamic_properties: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., identifier: _Optional[_Union[ResolvedGraphElementIdentifierProto, _Mapping]] = ..., property_list: _Optional[_Iterable[_Union[ResolvedGraphElementPropertyProto, _Mapping]]] = ..., label_list: _Optional[_Iterable[_Union[_serialization_pb2.GraphElementLabelRefProto, _Mapping]]] = ..., dynamic_labels: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., dynamic_properties: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedArrayAggregateProto(_message.Message):
    __slots__ = ("parent", "array", "element_column", "pre_aggregate_computed_column_list", "aggregate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    PRE_AGGREGATE_COMPUTED_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    array: AnyResolvedExprProto
    element_column: _serialization_pb2.ResolvedColumnProto
    pre_aggregate_computed_column_list: _containers.RepeatedCompositeFieldContainer[ResolvedComputedColumnProto]
    aggregate: ResolvedAggregateFunctionCallProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., array: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., element_column: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., pre_aggregate_computed_column_list: _Optional[_Iterable[_Union[ResolvedComputedColumnProto, _Mapping]]] = ..., aggregate: _Optional[_Union[ResolvedAggregateFunctionCallProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphMakeArrayVariableProto(_message.Message):
    __slots__ = ("parent", "element", "array")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    element: _serialization_pb2.ResolvedColumnProto
    array: _serialization_pb2.ResolvedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., element: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., array: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphPathModeProto(_message.Message):
    __slots__ = ("parent", "path_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    path_mode: _resolved_ast_enums_pb2.ResolvedGraphPathModeEnums.PathMode
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., path_mode: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedGraphPathModeEnums.PathMode, str]] = ...) -> None: ...

class ResolvedGraphPathCostProto(_message.Message):
    __slots__ = ("parent", "cost_supertype")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COST_SUPERTYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    cost_supertype: _type_pb2.TypeProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., cost_supertype: _Optional[_Union[_type_pb2.TypeProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphPathScanProto(_message.Message):
    __slots__ = ("parent", "input_scan_list", "filter_expr", "path", "head", "tail", "path_hint_list", "quantifier", "group_variable_list", "path_mode", "search_prefix", "path_cost")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_LIST_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    PATH_HINT_LIST_FIELD_NUMBER: _ClassVar[int]
    QUANTIFIER_FIELD_NUMBER: _ClassVar[int]
    GROUP_VARIABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    PATH_MODE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PATH_COST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedGraphPathScanBaseProto
    input_scan_list: _containers.RepeatedCompositeFieldContainer[AnyResolvedGraphPathScanBaseProto]
    filter_expr: AnyResolvedExprProto
    path: ResolvedColumnHolderProto
    head: _serialization_pb2.ResolvedColumnProto
    tail: _serialization_pb2.ResolvedColumnProto
    path_hint_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    quantifier: ResolvedGraphPathPatternQuantifierProto
    group_variable_list: _containers.RepeatedCompositeFieldContainer[ResolvedGraphMakeArrayVariableProto]
    path_mode: ResolvedGraphPathModeProto
    search_prefix: ResolvedGraphPathSearchPrefixProto
    path_cost: ResolvedGraphPathCostProto
    def __init__(self, parent: _Optional[_Union[ResolvedGraphPathScanBaseProto, _Mapping]] = ..., input_scan_list: _Optional[_Iterable[_Union[AnyResolvedGraphPathScanBaseProto, _Mapping]]] = ..., filter_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., path: _Optional[_Union[ResolvedColumnHolderProto, _Mapping]] = ..., head: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., tail: _Optional[_Union[_serialization_pb2.ResolvedColumnProto, _Mapping]] = ..., path_hint_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ..., quantifier: _Optional[_Union[ResolvedGraphPathPatternQuantifierProto, _Mapping]] = ..., group_variable_list: _Optional[_Iterable[_Union[ResolvedGraphMakeArrayVariableProto, _Mapping]]] = ..., path_mode: _Optional[_Union[ResolvedGraphPathModeProto, _Mapping]] = ..., search_prefix: _Optional[_Union[ResolvedGraphPathSearchPrefixProto, _Mapping]] = ..., path_cost: _Optional[_Union[ResolvedGraphPathCostProto, _Mapping]] = ...) -> None: ...

class ResolvedGraphIsLabeledPredicateProto(_message.Message):
    __slots__ = ("parent", "is_not", "expr", "label_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    is_not: bool
    expr: AnyResolvedExprProto
    label_expr: AnyResolvedGraphLabelExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., is_not: bool = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., label_expr: _Optional[_Union[AnyResolvedGraphLabelExprProto, _Mapping]] = ...) -> None: ...

class ResolvedUndropStmtProto(_message.Message):
    __slots__ = ("parent", "schema_object_kind", "is_if_not_exists", "name_path", "for_system_time_expr", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    FOR_SYSTEM_TIME_EXPR_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    schema_object_kind: str
    is_if_not_exists: bool
    name_path: _containers.RepeatedScalarFieldContainer[str]
    for_system_time_expr: AnyResolvedExprProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., schema_object_kind: _Optional[str] = ..., is_if_not_exists: bool = ..., name_path: _Optional[_Iterable[str]] = ..., for_system_time_expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedIdentityColumnInfoProto(_message.Message):
    __slots__ = ("parent", "start_with_value", "increment_by_value", "max_value", "min_value", "cycling_enabled")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_WITH_VALUE_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    CYCLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    start_with_value: _serialization_pb2.ValueWithTypeProto
    increment_by_value: _serialization_pb2.ValueWithTypeProto
    max_value: _serialization_pb2.ValueWithTypeProto
    min_value: _serialization_pb2.ValueWithTypeProto
    cycling_enabled: bool
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., start_with_value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., increment_by_value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., max_value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., min_value: _Optional[_Union[_serialization_pb2.ValueWithTypeProto, _Mapping]] = ..., cycling_enabled: bool = ...) -> None: ...

class ResolvedDescribeScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "describe_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    DESCRIBE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    describe_expr: ResolvedComputedColumnProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., describe_expr: _Optional[_Union[ResolvedComputedColumnProto, _Mapping]] = ...) -> None: ...

class ResolvedStaticDescribeScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "describe_text")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    DESCRIBE_TEXT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    describe_text: str
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., describe_text: _Optional[str] = ...) -> None: ...

class ResolvedAssertScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "condition", "message")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    condition: AnyResolvedExprProto
    message: AnyResolvedExprProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., condition: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., message: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ...) -> None: ...

class ResolvedLogScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "subpipeline", "output_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    subpipeline: ResolvedSubpipelineProto
    output_schema: ResolvedOutputSchemaProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ResolvedSubpipelineProto, _Mapping]] = ..., output_schema: _Optional[_Union[ResolvedOutputSchemaProto, _Mapping]] = ...) -> None: ...

class ResolvedPipeIfScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "selected_case", "if_case_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CASE_FIELD_NUMBER: _ClassVar[int]
    IF_CASE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    selected_case: int
    if_case_list: _containers.RepeatedCompositeFieldContainer[ResolvedPipeIfCaseProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., selected_case: _Optional[int] = ..., if_case_list: _Optional[_Iterable[_Union[ResolvedPipeIfCaseProto, _Mapping]]] = ...) -> None: ...

class ResolvedPipeIfCaseProto(_message.Message):
    __slots__ = ("parent", "condition", "subpipeline_sql", "subpipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_SQL_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    condition: AnyResolvedExprProto
    subpipeline_sql: str
    subpipeline: ResolvedSubpipelineProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., condition: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., subpipeline_sql: _Optional[str] = ..., subpipeline: _Optional[_Union[ResolvedSubpipelineProto, _Mapping]] = ...) -> None: ...

class ResolvedPipeForkScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "subpipeline_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    subpipeline_list: _containers.RepeatedCompositeFieldContainer[ResolvedGeneralizedQuerySubpipelineProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., subpipeline_list: _Optional[_Iterable[_Union[ResolvedGeneralizedQuerySubpipelineProto, _Mapping]]] = ...) -> None: ...

class ResolvedPipeTeeScanProto(_message.Message):
    __slots__ = ("parent", "input_scan", "subpipeline_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    subpipeline_list: _containers.RepeatedCompositeFieldContainer[ResolvedGeneralizedQuerySubpipelineProto]
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ..., subpipeline_list: _Optional[_Iterable[_Union[ResolvedGeneralizedQuerySubpipelineProto, _Mapping]]] = ...) -> None: ...

class ResolvedPipeExportDataScanProto(_message.Message):
    __slots__ = ("parent", "export_data_stmt")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DATA_STMT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    export_data_stmt: ResolvedExportDataStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., export_data_stmt: _Optional[_Union[ResolvedExportDataStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedPipeCreateTableScanProto(_message.Message):
    __slots__ = ("parent", "create_table_as_select_stmt")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TABLE_AS_SELECT_STMT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    create_table_as_select_stmt: ResolvedCreateTableAsSelectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., create_table_as_select_stmt: _Optional[_Union[ResolvedCreateTableAsSelectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedPipeInsertScanProto(_message.Message):
    __slots__ = ("parent", "insert_stmt")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSERT_STMT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    insert_stmt: ResolvedInsertStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., insert_stmt: _Optional[_Union[ResolvedInsertStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedSubpipelineProto(_message.Message):
    __slots__ = ("parent", "scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    scan: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedSubpipelineInputScanProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedSubpipelineStmtProto(_message.Message):
    __slots__ = ("parent", "table_scan", "subpipeline", "output_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCAN_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedStatementProto
    table_scan: ResolvedTableScanProto
    subpipeline: ResolvedSubpipelineProto
    output_schema: ResolvedOutputSchemaProto
    def __init__(self, parent: _Optional[_Union[ResolvedStatementProto, _Mapping]] = ..., table_scan: _Optional[_Union[ResolvedTableScanProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ResolvedSubpipelineProto, _Mapping]] = ..., output_schema: _Optional[_Union[ResolvedOutputSchemaProto, _Mapping]] = ...) -> None: ...

class ResolvedGeneralizedQuerySubpipelineProto(_message.Message):
    __slots__ = ("parent", "subpipeline", "output_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    subpipeline: ResolvedSubpipelineProto
    output_schema: ResolvedOutputSchemaProto
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ResolvedSubpipelineProto, _Mapping]] = ..., output_schema: _Optional[_Union[ResolvedOutputSchemaProto, _Mapping]] = ...) -> None: ...

class ResolvedBarrierScanProto(_message.Message):
    __slots__ = ("parent", "input_scan")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCAN_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedScanProto
    input_scan: AnyResolvedScanProto
    def __init__(self, parent: _Optional[_Union[ResolvedScanProto, _Mapping]] = ..., input_scan: _Optional[_Union[AnyResolvedScanProto, _Mapping]] = ...) -> None: ...

class ResolvedCreateConnectionStmtProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAlterConnectionStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...

class ResolvedLockModeProto(_message.Message):
    __slots__ = ("parent", "strength")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    strength: _resolved_ast_enums_pb2.ResolvedLockModeEnums.LockStrengthType
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., strength: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedLockModeEnums.LockStrengthType, str]] = ...) -> None: ...

class ResolvedUpdateFieldItemProto(_message.Message):
    __slots__ = ("parent", "expr", "proto_field_path", "operation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    PROTO_FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedArgumentProto
    expr: AnyResolvedExprProto
    proto_field_path: _containers.RepeatedCompositeFieldContainer[_serialization_pb2.FieldDescriptorRefProto]
    operation: _resolved_ast_enums_pb2.ResolvedUpdateFieldItemEnums.Operation
    def __init__(self, parent: _Optional[_Union[ResolvedArgumentProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., proto_field_path: _Optional[_Iterable[_Union[_serialization_pb2.FieldDescriptorRefProto, _Mapping]]] = ..., operation: _Optional[_Union[_resolved_ast_enums_pb2.ResolvedUpdateFieldItemEnums.Operation, str]] = ...) -> None: ...

class ResolvedUpdateConstructorProto(_message.Message):
    __slots__ = ("parent", "expr", "alias", "update_field_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedExprProto
    expr: AnyResolvedExprProto
    alias: str
    update_field_item_list: _containers.RepeatedCompositeFieldContainer[ResolvedUpdateFieldItemProto]
    def __init__(self, parent: _Optional[_Union[ResolvedExprProto, _Mapping]] = ..., expr: _Optional[_Union[AnyResolvedExprProto, _Mapping]] = ..., alias: _Optional[str] = ..., update_field_item_list: _Optional[_Iterable[_Union[ResolvedUpdateFieldItemProto, _Mapping]]] = ...) -> None: ...

class ResolvedCreateSequenceStmtProto(_message.Message):
    __slots__ = ("parent", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedCreateStatementProto
    option_list: _containers.RepeatedCompositeFieldContainer[ResolvedOptionProto]
    def __init__(self, parent: _Optional[_Union[ResolvedCreateStatementProto, _Mapping]] = ..., option_list: _Optional[_Iterable[_Union[ResolvedOptionProto, _Mapping]]] = ...) -> None: ...

class ResolvedAlterSequenceStmtProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ResolvedAlterObjectStmtProto
    def __init__(self, parent: _Optional[_Union[ResolvedAlterObjectStmtProto, _Mapping]] = ...) -> None: ...
