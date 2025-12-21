from zetasql.parser import ast_enums_pb2 as _ast_enums_pb2
from zetasql.public import parse_location_range_pb2 as _parse_location_range_pb2
from zetasql.public import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnyASTNodeProto(_message.Message):
    __slots__ = ("ast_statement_node", "ast_query_expression_node", "ast_select_list_node", "ast_select_column_node", "ast_expression_node", "ast_alias_node", "ast_table_expression_node", "ast_from_clause_node", "ast_where_clause_node", "ast_grouping_item_node", "ast_group_by_node", "ast_ordering_expression_node", "ast_order_by_node", "ast_limit_offset_node", "ast_on_clause_node", "ast_aliased_query_node", "ast_with_clause_node", "ast_having_node", "ast_type_node", "ast_struct_field_node", "ast_select_as_node", "ast_rollup_node", "ast_struct_constructor_arg_node", "ast_in_list_node", "ast_collate_node", "ast_having_modifier_node", "ast_null_order_node", "ast_on_or_using_clause_list_node", "ast_partition_by_node", "ast_star_except_list_node", "ast_star_modifiers_node", "ast_star_replace_item_node", "ast_unnest_expression_node", "ast_window_clause_node", "ast_window_definition_node", "ast_window_frame_node", "ast_window_frame_expr_node", "ast_window_specification_node", "ast_with_offset_node", "ast_any_some_all_op_node", "ast_statement_list_node", "ast_transaction_mode_node", "ast_transaction_mode_list_node", "ast_with_connection_clause_node", "ast_into_alias_node", "ast_unnest_expression_with_opt_alias_and_offset_node", "ast_pivot_expression_node", "ast_pivot_value_node", "ast_pivot_expression_list_node", "ast_pivot_value_list_node", "ast_unpivot_in_item_node", "ast_unpivot_in_item_list_node", "ast_using_clause_node", "ast_for_system_time_node", "ast_qualify_node", "ast_clamped_between_modifier_node", "ast_format_clause_node", "ast_path_expression_list_node", "ast_cluster_by_node", "ast_new_constructor_arg_node", "ast_options_list_node", "ast_options_entry_node", "ast_function_parameter_node", "ast_function_parameters_node", "ast_function_declaration_node", "ast_sql_function_body_node", "ast_tvf_argument_node", "ast_model_clause_node", "ast_connection_clause_node", "ast_clone_data_source_list_node", "ast_transform_clause_node", "ast_index_item_list_node", "ast_index_storing_expression_list_node", "ast_index_unnest_expression_list_node", "ast_with_partition_columns_clause_node", "ast_type_parameter_list_node", "ast_tvf_schema_node", "ast_tvf_schema_column_node", "ast_table_and_column_info_node", "ast_table_and_column_info_list_node", "ast_templated_parameter_type_node", "ast_assert_rows_modified_node", "ast_returning_clause_node", "ast_column_attribute_node", "ast_column_attribute_list_node", "ast_struct_column_field_node", "ast_generated_column_info_node", "ast_table_element_node", "ast_table_element_list_node", "ast_column_list_node", "ast_column_position_node", "ast_insert_values_row_node", "ast_insert_values_row_list_node", "ast_update_set_value_node", "ast_update_item_node", "ast_update_item_list_node", "ast_merge_action_node", "ast_merge_when_clause_node", "ast_merge_when_clause_list_node", "ast_privilege_node", "ast_privileges_node", "ast_grantee_list_node", "ast_repeatable_clause_node", "ast_filter_fields_arg_node", "ast_replace_fields_arg_node", "ast_sample_size_node", "ast_with_weight_node", "ast_sample_suffix_node", "ast_alter_action_node", "ast_alter_action_list_node", "ast_foreign_key_actions_node", "ast_foreign_key_reference_node", "ast_script_node", "ast_elseif_clause_node", "ast_elseif_clause_list_node", "ast_when_then_clause_node", "ast_when_then_clause_list_node", "ast_hint_node", "ast_hint_entry_node", "ast_unpivot_in_item_label_node", "ast_descriptor_node", "ast_column_schema_node", "ast_descriptor_column_node", "ast_descriptor_column_list_node", "ast_exception_handler_node", "ast_exception_handler_list_node", "ast_identifier_list_node", "ast_until_clause_node", "ast_execute_into_clause_node", "ast_execute_using_argument_node", "ast_execute_using_clause_node", "ast_braced_constructor_field_value_node", "ast_braced_constructor_field_node", "ast_with_report_modifier_node", "ast_location_node", "ast_aux_load_data_from_files_options_list_node", "ast_label_node", "ast_primary_key_element_node", "ast_primary_key_element_list_node", "ast_spanner_table_options_node", "ast_spanner_interleave_clause_node", "ast_ttl_clause_node", "ast_input_output_clause_node", "ast_graph_label_expression_node", "ast_graph_label_filter_node", "ast_select_with_node", "ast_aliased_query_list_node", "ast_column_with_options_node", "ast_column_with_options_list_node", "ast_graph_element_pattern_filler_node", "ast_graph_element_table_list_node", "ast_graph_element_table_node", "ast_graph_node_table_reference_node", "ast_aux_load_data_partitions_clause_node", "ast_graph_element_label_and_properties_list_node", "ast_graph_element_label_and_properties_node", "ast_graph_properties_node", "ast_set_operation_metadata_list_node", "ast_set_operation_all_or_distinct_node", "ast_set_operation_type_node", "ast_set_operation_metadata_node", "ast_set_operation_column_match_mode_node", "ast_set_operation_column_propagation_mode_node", "ast_graph_pattern_node", "ast_cube_node", "ast_grouping_set_node", "ast_grouping_set_list_node", "ast_expression_with_opt_alias_node", "ast_group_by_all_node", "ast_function_type_arg_list_node", "ast_pipe_operator_node", "ast_graph_lhs_hint_node", "ast_graph_rhs_hint_node", "ast_identity_column_info_node", "ast_identity_column_start_with_node", "ast_identity_column_increment_by_node", "ast_identity_column_max_value_node", "ast_identity_column_min_value_node", "ast_graph_path_base_node", "ast_gql_operator_node", "ast_gql_let_variable_definition_list_node", "ast_gql_let_variable_definition_node", "ast_pipe_set_item_node", "ast_graph_property_specification_node", "ast_graph_property_name_and_value_node", "ast_gql_page_limit_node", "ast_gql_page_offset_node", "ast_gql_page_node", "ast_aliased_query_modifiers_node", "ast_recursion_depth_modifier_node", "ast_grouping_item_order_node", "ast_graph_path_mode_node", "ast_graph_path_search_prefix_node", "ast_lock_mode_node", "ast_row_pattern_expression_node", "ast_postfix_table_operator_node", "ast_quantifier_node", "ast_quantifier_bound_node", "ast_subpipeline_node", "ast_after_match_skip_clause_node", "ast_on_conflict_clause_node", "ast_graph_dynamic_label_node", "ast_graph_dynamic_properties_node", "ast_graph_path_search_prefix_count_node", "ast_chained_base_expr_node", "ast_yield_item_list_node", "ast_limit_all_node", "ast_limit_node", "ast_graph_derived_property_node", "ast_graph_derived_property_list_node")
    AST_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_QUERY_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SELECT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SELECT_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALIAS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FROM_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WHERE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUPING_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUP_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ORDERING_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ORDER_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LIMIT_OFFSET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ON_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALIASED_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HAVING_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SELECT_AS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROLLUP_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_CONSTRUCTOR_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IN_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLLATE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HAVING_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NULL_ORDER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ON_OR_USING_CLAUSE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PARTITION_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STAR_EXCEPT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STAR_MODIFIERS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STAR_REPLACE_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNNEST_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WINDOW_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WINDOW_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WINDOW_FRAME_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WINDOW_FRAME_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WINDOW_SPECIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_OFFSET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ANY_SOME_ALL_OP_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STATEMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TRANSACTION_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TRANSACTION_MODE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_CONNECTION_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INTO_ALIAS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNNEST_EXPRESSION_WITH_OPT_ALIAS_AND_OFFSET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIVOT_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIVOT_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIVOT_EXPRESSION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIVOT_VALUE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNPIVOT_IN_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNPIVOT_IN_ITEM_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_USING_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOR_SYSTEM_TIME_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_QUALIFY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CLAMPED_BETWEEN_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FORMAT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PATH_EXPRESSION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CLUSTER_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NEW_CONSTRUCTOR_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_OPTIONS_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_OPTIONS_ENTRY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_PARAMETER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_PARAMETERS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_DECLARATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SQL_FUNCTION_BODY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TVF_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MODEL_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CONNECTION_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CLONE_DATA_SOURCE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TRANSFORM_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INDEX_ITEM_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INDEX_STORING_EXPRESSION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INDEX_UNNEST_EXPRESSION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_PARTITION_COLUMNS_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TYPE_PARAMETER_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TVF_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TVF_SCHEMA_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_AND_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_AND_COLUMN_INFO_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TEMPLATED_PARAMETER_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ASSERT_ROWS_MODIFIED_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RETURNING_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_ATTRIBUTE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_ATTRIBUTE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_COLUMN_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GENERATED_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_ELEMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_POSITION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INSERT_VALUES_ROW_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INSERT_VALUES_ROW_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UPDATE_SET_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UPDATE_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UPDATE_ITEM_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MERGE_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MERGE_WHEN_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MERGE_WHEN_CLAUSE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRIVILEGE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRIVILEGES_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRANTEE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REPEATABLE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FILTER_FIELDS_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REPLACE_FIELDS_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SAMPLE_SIZE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_WEIGHT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SAMPLE_SUFFIX_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_ACTION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOREIGN_KEY_ACTIONS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOREIGN_KEY_REFERENCE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SCRIPT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ELSEIF_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ELSEIF_CLAUSE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WHEN_THEN_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WHEN_THEN_CLAUSE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HINT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HINT_ENTRY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNPIVOT_IN_ITEM_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DESCRIPTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DESCRIPTOR_COLUMN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DESCRIPTOR_COLUMN_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXCEPTION_HANDLER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXCEPTION_HANDLER_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTIFIER_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNTIL_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXECUTE_INTO_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXECUTE_USING_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXECUTE_USING_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BRACED_CONSTRUCTOR_FIELD_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BRACED_CONSTRUCTOR_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_REPORT_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LOCATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_AUX_LOAD_DATA_FROM_FILES_OPTIONS_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRIMARY_KEY_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRIMARY_KEY_ELEMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SPANNER_TABLE_OPTIONS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SPANNER_INTERLEAVE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TTL_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INPUT_OUTPUT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_LABEL_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_LABEL_FILTER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SELECT_WITH_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALIASED_QUERY_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_WITH_OPTIONS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COLUMN_WITH_OPTIONS_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_ELEMENT_PATTERN_FILLER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_ELEMENT_TABLE_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_ELEMENT_TABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_NODE_TABLE_REFERENCE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_AUX_LOAD_DATA_PARTITIONS_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_ELEMENT_LABEL_AND_PROPERTIES_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_ELEMENT_LABEL_AND_PROPERTIES_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PROPERTIES_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_METADATA_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_ALL_OR_DISTINCT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_METADATA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_COLUMN_MATCH_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_COLUMN_PROPAGATION_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CUBE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUPING_SET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUPING_SET_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPRESSION_WITH_OPT_ALIAS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUP_BY_ALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_TYPE_ARG_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_OPERATOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_LHS_HINT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_RHS_HINT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTITY_COLUMN_INFO_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTITY_COLUMN_START_WITH_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTITY_COLUMN_INCREMENT_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTITY_COLUMN_MAX_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTITY_COLUMN_MIN_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATH_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_OPERATOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_LET_VARIABLE_DEFINITION_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_LET_VARIABLE_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_SET_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PROPERTY_SPECIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PROPERTY_NAME_AND_VALUE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_PAGE_LIMIT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_PAGE_OFFSET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_PAGE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALIASED_QUERY_MODIFIERS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RECURSION_DEPTH_MODIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GROUPING_ITEM_ORDER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATH_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATH_SEARCH_PREFIX_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LOCK_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROW_PATTERN_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_POSTFIX_TABLE_OPERATOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_QUANTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_QUANTIFIER_BOUND_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SUBPIPELINE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_AFTER_MATCH_SKIP_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ON_CONFLICT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_DYNAMIC_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_DYNAMIC_PROPERTIES_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATH_SEARCH_PREFIX_COUNT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CHAINED_BASE_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_YIELD_ITEM_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LIMIT_ALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LIMIT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_DERIVED_PROPERTY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_DERIVED_PROPERTY_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_statement_node: AnyASTStatementProto
    ast_query_expression_node: AnyASTQueryExpressionProto
    ast_select_list_node: ASTSelectListProto
    ast_select_column_node: ASTSelectColumnProto
    ast_expression_node: AnyASTExpressionProto
    ast_alias_node: ASTAliasProto
    ast_table_expression_node: AnyASTTableExpressionProto
    ast_from_clause_node: ASTFromClauseProto
    ast_where_clause_node: ASTWhereClauseProto
    ast_grouping_item_node: ASTGroupingItemProto
    ast_group_by_node: ASTGroupByProto
    ast_ordering_expression_node: ASTOrderingExpressionProto
    ast_order_by_node: ASTOrderByProto
    ast_limit_offset_node: ASTLimitOffsetProto
    ast_on_clause_node: ASTOnClauseProto
    ast_aliased_query_node: ASTAliasedQueryProto
    ast_with_clause_node: ASTWithClauseProto
    ast_having_node: ASTHavingProto
    ast_type_node: AnyASTTypeProto
    ast_struct_field_node: ASTStructFieldProto
    ast_select_as_node: ASTSelectAsProto
    ast_rollup_node: ASTRollupProto
    ast_struct_constructor_arg_node: ASTStructConstructorArgProto
    ast_in_list_node: ASTInListProto
    ast_collate_node: ASTCollateProto
    ast_having_modifier_node: ASTHavingModifierProto
    ast_null_order_node: ASTNullOrderProto
    ast_on_or_using_clause_list_node: ASTOnOrUsingClauseListProto
    ast_partition_by_node: ASTPartitionByProto
    ast_star_except_list_node: ASTStarExceptListProto
    ast_star_modifiers_node: ASTStarModifiersProto
    ast_star_replace_item_node: ASTStarReplaceItemProto
    ast_unnest_expression_node: ASTUnnestExpressionProto
    ast_window_clause_node: ASTWindowClauseProto
    ast_window_definition_node: ASTWindowDefinitionProto
    ast_window_frame_node: ASTWindowFrameProto
    ast_window_frame_expr_node: ASTWindowFrameExprProto
    ast_window_specification_node: ASTWindowSpecificationProto
    ast_with_offset_node: ASTWithOffsetProto
    ast_any_some_all_op_node: ASTAnySomeAllOpProto
    ast_statement_list_node: ASTStatementListProto
    ast_transaction_mode_node: AnyASTTransactionModeProto
    ast_transaction_mode_list_node: ASTTransactionModeListProto
    ast_with_connection_clause_node: ASTWithConnectionClauseProto
    ast_into_alias_node: ASTIntoAliasProto
    ast_unnest_expression_with_opt_alias_and_offset_node: ASTUnnestExpressionWithOptAliasAndOffsetProto
    ast_pivot_expression_node: ASTPivotExpressionProto
    ast_pivot_value_node: ASTPivotValueProto
    ast_pivot_expression_list_node: ASTPivotExpressionListProto
    ast_pivot_value_list_node: ASTPivotValueListProto
    ast_unpivot_in_item_node: ASTUnpivotInItemProto
    ast_unpivot_in_item_list_node: ASTUnpivotInItemListProto
    ast_using_clause_node: ASTUsingClauseProto
    ast_for_system_time_node: ASTForSystemTimeProto
    ast_qualify_node: ASTQualifyProto
    ast_clamped_between_modifier_node: ASTClampedBetweenModifierProto
    ast_format_clause_node: ASTFormatClauseProto
    ast_path_expression_list_node: ASTPathExpressionListProto
    ast_cluster_by_node: ASTClusterByProto
    ast_new_constructor_arg_node: ASTNewConstructorArgProto
    ast_options_list_node: ASTOptionsListProto
    ast_options_entry_node: ASTOptionsEntryProto
    ast_function_parameter_node: ASTFunctionParameterProto
    ast_function_parameters_node: ASTFunctionParametersProto
    ast_function_declaration_node: ASTFunctionDeclarationProto
    ast_sql_function_body_node: ASTSqlFunctionBodyProto
    ast_tvf_argument_node: ASTTVFArgumentProto
    ast_model_clause_node: ASTModelClauseProto
    ast_connection_clause_node: ASTConnectionClauseProto
    ast_clone_data_source_list_node: ASTCloneDataSourceListProto
    ast_transform_clause_node: ASTTransformClauseProto
    ast_index_item_list_node: ASTIndexItemListProto
    ast_index_storing_expression_list_node: ASTIndexStoringExpressionListProto
    ast_index_unnest_expression_list_node: ASTIndexUnnestExpressionListProto
    ast_with_partition_columns_clause_node: ASTWithPartitionColumnsClauseProto
    ast_type_parameter_list_node: ASTTypeParameterListProto
    ast_tvf_schema_node: ASTTVFSchemaProto
    ast_tvf_schema_column_node: ASTTVFSchemaColumnProto
    ast_table_and_column_info_node: ASTTableAndColumnInfoProto
    ast_table_and_column_info_list_node: ASTTableAndColumnInfoListProto
    ast_templated_parameter_type_node: ASTTemplatedParameterTypeProto
    ast_assert_rows_modified_node: ASTAssertRowsModifiedProto
    ast_returning_clause_node: ASTReturningClauseProto
    ast_column_attribute_node: AnyASTColumnAttributeProto
    ast_column_attribute_list_node: ASTColumnAttributeListProto
    ast_struct_column_field_node: ASTStructColumnFieldProto
    ast_generated_column_info_node: ASTGeneratedColumnInfoProto
    ast_table_element_node: AnyASTTableElementProto
    ast_table_element_list_node: ASTTableElementListProto
    ast_column_list_node: ASTColumnListProto
    ast_column_position_node: ASTColumnPositionProto
    ast_insert_values_row_node: ASTInsertValuesRowProto
    ast_insert_values_row_list_node: ASTInsertValuesRowListProto
    ast_update_set_value_node: ASTUpdateSetValueProto
    ast_update_item_node: ASTUpdateItemProto
    ast_update_item_list_node: ASTUpdateItemListProto
    ast_merge_action_node: ASTMergeActionProto
    ast_merge_when_clause_node: ASTMergeWhenClauseProto
    ast_merge_when_clause_list_node: ASTMergeWhenClauseListProto
    ast_privilege_node: ASTPrivilegeProto
    ast_privileges_node: ASTPrivilegesProto
    ast_grantee_list_node: ASTGranteeListProto
    ast_repeatable_clause_node: ASTRepeatableClauseProto
    ast_filter_fields_arg_node: ASTFilterFieldsArgProto
    ast_replace_fields_arg_node: ASTReplaceFieldsArgProto
    ast_sample_size_node: ASTSampleSizeProto
    ast_with_weight_node: ASTWithWeightProto
    ast_sample_suffix_node: ASTSampleSuffixProto
    ast_alter_action_node: AnyASTAlterActionProto
    ast_alter_action_list_node: ASTAlterActionListProto
    ast_foreign_key_actions_node: ASTForeignKeyActionsProto
    ast_foreign_key_reference_node: ASTForeignKeyReferenceProto
    ast_script_node: ASTScriptProto
    ast_elseif_clause_node: ASTElseifClauseProto
    ast_elseif_clause_list_node: ASTElseifClauseListProto
    ast_when_then_clause_node: ASTWhenThenClauseProto
    ast_when_then_clause_list_node: ASTWhenThenClauseListProto
    ast_hint_node: ASTHintProto
    ast_hint_entry_node: ASTHintEntryProto
    ast_unpivot_in_item_label_node: ASTUnpivotInItemLabelProto
    ast_descriptor_node: ASTDescriptorProto
    ast_column_schema_node: AnyASTColumnSchemaProto
    ast_descriptor_column_node: ASTDescriptorColumnProto
    ast_descriptor_column_list_node: ASTDescriptorColumnListProto
    ast_exception_handler_node: ASTExceptionHandlerProto
    ast_exception_handler_list_node: ASTExceptionHandlerListProto
    ast_identifier_list_node: ASTIdentifierListProto
    ast_until_clause_node: ASTUntilClauseProto
    ast_execute_into_clause_node: ASTExecuteIntoClauseProto
    ast_execute_using_argument_node: ASTExecuteUsingArgumentProto
    ast_execute_using_clause_node: ASTExecuteUsingClauseProto
    ast_braced_constructor_field_value_node: ASTBracedConstructorFieldValueProto
    ast_braced_constructor_field_node: ASTBracedConstructorFieldProto
    ast_with_report_modifier_node: ASTWithReportModifierProto
    ast_location_node: ASTLocationProto
    ast_aux_load_data_from_files_options_list_node: ASTAuxLoadDataFromFilesOptionsListProto
    ast_label_node: ASTLabelProto
    ast_primary_key_element_node: ASTPrimaryKeyElementProto
    ast_primary_key_element_list_node: ASTPrimaryKeyElementListProto
    ast_spanner_table_options_node: ASTSpannerTableOptionsProto
    ast_spanner_interleave_clause_node: ASTSpannerInterleaveClauseProto
    ast_ttl_clause_node: ASTTtlClauseProto
    ast_input_output_clause_node: ASTInputOutputClauseProto
    ast_graph_label_expression_node: AnyASTGraphLabelExpressionProto
    ast_graph_label_filter_node: ASTGraphLabelFilterProto
    ast_select_with_node: ASTSelectWithProto
    ast_aliased_query_list_node: ASTAliasedQueryListProto
    ast_column_with_options_node: ASTColumnWithOptionsProto
    ast_column_with_options_list_node: ASTColumnWithOptionsListProto
    ast_graph_element_pattern_filler_node: ASTGraphElementPatternFillerProto
    ast_graph_element_table_list_node: ASTGraphElementTableListProto
    ast_graph_element_table_node: ASTGraphElementTableProto
    ast_graph_node_table_reference_node: ASTGraphNodeTableReferenceProto
    ast_aux_load_data_partitions_clause_node: ASTAuxLoadDataPartitionsClauseProto
    ast_graph_element_label_and_properties_list_node: ASTGraphElementLabelAndPropertiesListProto
    ast_graph_element_label_and_properties_node: ASTGraphElementLabelAndPropertiesProto
    ast_graph_properties_node: ASTGraphPropertiesProto
    ast_set_operation_metadata_list_node: ASTSetOperationMetadataListProto
    ast_set_operation_all_or_distinct_node: ASTSetOperationAllOrDistinctProto
    ast_set_operation_type_node: ASTSetOperationTypeProto
    ast_set_operation_metadata_node: ASTSetOperationMetadataProto
    ast_set_operation_column_match_mode_node: ASTSetOperationColumnMatchModeProto
    ast_set_operation_column_propagation_mode_node: ASTSetOperationColumnPropagationModeProto
    ast_graph_pattern_node: ASTGraphPatternProto
    ast_cube_node: ASTCubeProto
    ast_grouping_set_node: ASTGroupingSetProto
    ast_grouping_set_list_node: ASTGroupingSetListProto
    ast_expression_with_opt_alias_node: ASTExpressionWithOptAliasProto
    ast_group_by_all_node: ASTGroupByAllProto
    ast_function_type_arg_list_node: ASTFunctionTypeArgListProto
    ast_pipe_operator_node: AnyASTPipeOperatorProto
    ast_graph_lhs_hint_node: ASTGraphLhsHintProto
    ast_graph_rhs_hint_node: ASTGraphRhsHintProto
    ast_identity_column_info_node: ASTIdentityColumnInfoProto
    ast_identity_column_start_with_node: ASTIdentityColumnStartWithProto
    ast_identity_column_increment_by_node: ASTIdentityColumnIncrementByProto
    ast_identity_column_max_value_node: ASTIdentityColumnMaxValueProto
    ast_identity_column_min_value_node: ASTIdentityColumnMinValueProto
    ast_graph_path_base_node: AnyASTGraphPathBaseProto
    ast_gql_operator_node: AnyASTGqlOperatorProto
    ast_gql_let_variable_definition_list_node: ASTGqlLetVariableDefinitionListProto
    ast_gql_let_variable_definition_node: ASTGqlLetVariableDefinitionProto
    ast_pipe_set_item_node: ASTPipeSetItemProto
    ast_graph_property_specification_node: ASTGraphPropertySpecificationProto
    ast_graph_property_name_and_value_node: ASTGraphPropertyNameAndValueProto
    ast_gql_page_limit_node: ASTGqlPageLimitProto
    ast_gql_page_offset_node: ASTGqlPageOffsetProto
    ast_gql_page_node: ASTGqlPageProto
    ast_aliased_query_modifiers_node: ASTAliasedQueryModifiersProto
    ast_recursion_depth_modifier_node: ASTRecursionDepthModifierProto
    ast_grouping_item_order_node: ASTGroupingItemOrderProto
    ast_graph_path_mode_node: ASTGraphPathModeProto
    ast_graph_path_search_prefix_node: ASTGraphPathSearchPrefixProto
    ast_lock_mode_node: ASTLockModeProto
    ast_row_pattern_expression_node: AnyASTRowPatternExpressionProto
    ast_postfix_table_operator_node: AnyASTPostfixTableOperatorProto
    ast_quantifier_node: AnyASTQuantifierProto
    ast_quantifier_bound_node: ASTQuantifierBoundProto
    ast_subpipeline_node: ASTSubpipelineProto
    ast_after_match_skip_clause_node: ASTAfterMatchSkipClauseProto
    ast_on_conflict_clause_node: ASTOnConflictClauseProto
    ast_graph_dynamic_label_node: ASTGraphDynamicLabelProto
    ast_graph_dynamic_properties_node: ASTGraphDynamicPropertiesProto
    ast_graph_path_search_prefix_count_node: ASTGraphPathSearchPrefixCountProto
    ast_chained_base_expr_node: ASTChainedBaseExprProto
    ast_yield_item_list_node: ASTYieldItemListProto
    ast_limit_all_node: ASTLimitAllProto
    ast_limit_node: ASTLimitProto
    ast_graph_derived_property_node: ASTGraphDerivedPropertyProto
    ast_graph_derived_property_list_node: ASTGraphDerivedPropertyListProto
    def __init__(self, ast_statement_node: _Optional[_Union[AnyASTStatementProto, _Mapping]] = ..., ast_query_expression_node: _Optional[_Union[AnyASTQueryExpressionProto, _Mapping]] = ..., ast_select_list_node: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., ast_select_column_node: _Optional[_Union[ASTSelectColumnProto, _Mapping]] = ..., ast_expression_node: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., ast_alias_node: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., ast_table_expression_node: _Optional[_Union[AnyASTTableExpressionProto, _Mapping]] = ..., ast_from_clause_node: _Optional[_Union[ASTFromClauseProto, _Mapping]] = ..., ast_where_clause_node: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ..., ast_grouping_item_node: _Optional[_Union[ASTGroupingItemProto, _Mapping]] = ..., ast_group_by_node: _Optional[_Union[ASTGroupByProto, _Mapping]] = ..., ast_ordering_expression_node: _Optional[_Union[ASTOrderingExpressionProto, _Mapping]] = ..., ast_order_by_node: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., ast_limit_offset_node: _Optional[_Union[ASTLimitOffsetProto, _Mapping]] = ..., ast_on_clause_node: _Optional[_Union[ASTOnClauseProto, _Mapping]] = ..., ast_aliased_query_node: _Optional[_Union[ASTAliasedQueryProto, _Mapping]] = ..., ast_with_clause_node: _Optional[_Union[ASTWithClauseProto, _Mapping]] = ..., ast_having_node: _Optional[_Union[ASTHavingProto, _Mapping]] = ..., ast_type_node: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., ast_struct_field_node: _Optional[_Union[ASTStructFieldProto, _Mapping]] = ..., ast_select_as_node: _Optional[_Union[ASTSelectAsProto, _Mapping]] = ..., ast_rollup_node: _Optional[_Union[ASTRollupProto, _Mapping]] = ..., ast_struct_constructor_arg_node: _Optional[_Union[ASTStructConstructorArgProto, _Mapping]] = ..., ast_in_list_node: _Optional[_Union[ASTInListProto, _Mapping]] = ..., ast_collate_node: _Optional[_Union[ASTCollateProto, _Mapping]] = ..., ast_having_modifier_node: _Optional[_Union[ASTHavingModifierProto, _Mapping]] = ..., ast_null_order_node: _Optional[_Union[ASTNullOrderProto, _Mapping]] = ..., ast_on_or_using_clause_list_node: _Optional[_Union[ASTOnOrUsingClauseListProto, _Mapping]] = ..., ast_partition_by_node: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., ast_star_except_list_node: _Optional[_Union[ASTStarExceptListProto, _Mapping]] = ..., ast_star_modifiers_node: _Optional[_Union[ASTStarModifiersProto, _Mapping]] = ..., ast_star_replace_item_node: _Optional[_Union[ASTStarReplaceItemProto, _Mapping]] = ..., ast_unnest_expression_node: _Optional[_Union[ASTUnnestExpressionProto, _Mapping]] = ..., ast_window_clause_node: _Optional[_Union[ASTWindowClauseProto, _Mapping]] = ..., ast_window_definition_node: _Optional[_Union[ASTWindowDefinitionProto, _Mapping]] = ..., ast_window_frame_node: _Optional[_Union[ASTWindowFrameProto, _Mapping]] = ..., ast_window_frame_expr_node: _Optional[_Union[ASTWindowFrameExprProto, _Mapping]] = ..., ast_window_specification_node: _Optional[_Union[ASTWindowSpecificationProto, _Mapping]] = ..., ast_with_offset_node: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ..., ast_any_some_all_op_node: _Optional[_Union[ASTAnySomeAllOpProto, _Mapping]] = ..., ast_statement_list_node: _Optional[_Union[ASTStatementListProto, _Mapping]] = ..., ast_transaction_mode_node: _Optional[_Union[AnyASTTransactionModeProto, _Mapping]] = ..., ast_transaction_mode_list_node: _Optional[_Union[ASTTransactionModeListProto, _Mapping]] = ..., ast_with_connection_clause_node: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., ast_into_alias_node: _Optional[_Union[ASTIntoAliasProto, _Mapping]] = ..., ast_unnest_expression_with_opt_alias_and_offset_node: _Optional[_Union[ASTUnnestExpressionWithOptAliasAndOffsetProto, _Mapping]] = ..., ast_pivot_expression_node: _Optional[_Union[ASTPivotExpressionProto, _Mapping]] = ..., ast_pivot_value_node: _Optional[_Union[ASTPivotValueProto, _Mapping]] = ..., ast_pivot_expression_list_node: _Optional[_Union[ASTPivotExpressionListProto, _Mapping]] = ..., ast_pivot_value_list_node: _Optional[_Union[ASTPivotValueListProto, _Mapping]] = ..., ast_unpivot_in_item_node: _Optional[_Union[ASTUnpivotInItemProto, _Mapping]] = ..., ast_unpivot_in_item_list_node: _Optional[_Union[ASTUnpivotInItemListProto, _Mapping]] = ..., ast_using_clause_node: _Optional[_Union[ASTUsingClauseProto, _Mapping]] = ..., ast_for_system_time_node: _Optional[_Union[ASTForSystemTimeProto, _Mapping]] = ..., ast_qualify_node: _Optional[_Union[ASTQualifyProto, _Mapping]] = ..., ast_clamped_between_modifier_node: _Optional[_Union[ASTClampedBetweenModifierProto, _Mapping]] = ..., ast_format_clause_node: _Optional[_Union[ASTFormatClauseProto, _Mapping]] = ..., ast_path_expression_list_node: _Optional[_Union[ASTPathExpressionListProto, _Mapping]] = ..., ast_cluster_by_node: _Optional[_Union[ASTClusterByProto, _Mapping]] = ..., ast_new_constructor_arg_node: _Optional[_Union[ASTNewConstructorArgProto, _Mapping]] = ..., ast_options_list_node: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., ast_options_entry_node: _Optional[_Union[ASTOptionsEntryProto, _Mapping]] = ..., ast_function_parameter_node: _Optional[_Union[ASTFunctionParameterProto, _Mapping]] = ..., ast_function_parameters_node: _Optional[_Union[ASTFunctionParametersProto, _Mapping]] = ..., ast_function_declaration_node: _Optional[_Union[ASTFunctionDeclarationProto, _Mapping]] = ..., ast_sql_function_body_node: _Optional[_Union[ASTSqlFunctionBodyProto, _Mapping]] = ..., ast_tvf_argument_node: _Optional[_Union[ASTTVFArgumentProto, _Mapping]] = ..., ast_model_clause_node: _Optional[_Union[ASTModelClauseProto, _Mapping]] = ..., ast_connection_clause_node: _Optional[_Union[ASTConnectionClauseProto, _Mapping]] = ..., ast_clone_data_source_list_node: _Optional[_Union[ASTCloneDataSourceListProto, _Mapping]] = ..., ast_transform_clause_node: _Optional[_Union[ASTTransformClauseProto, _Mapping]] = ..., ast_index_item_list_node: _Optional[_Union[ASTIndexItemListProto, _Mapping]] = ..., ast_index_storing_expression_list_node: _Optional[_Union[ASTIndexStoringExpressionListProto, _Mapping]] = ..., ast_index_unnest_expression_list_node: _Optional[_Union[ASTIndexUnnestExpressionListProto, _Mapping]] = ..., ast_with_partition_columns_clause_node: _Optional[_Union[ASTWithPartitionColumnsClauseProto, _Mapping]] = ..., ast_type_parameter_list_node: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., ast_tvf_schema_node: _Optional[_Union[ASTTVFSchemaProto, _Mapping]] = ..., ast_tvf_schema_column_node: _Optional[_Union[ASTTVFSchemaColumnProto, _Mapping]] = ..., ast_table_and_column_info_node: _Optional[_Union[ASTTableAndColumnInfoProto, _Mapping]] = ..., ast_table_and_column_info_list_node: _Optional[_Union[ASTTableAndColumnInfoListProto, _Mapping]] = ..., ast_templated_parameter_type_node: _Optional[_Union[ASTTemplatedParameterTypeProto, _Mapping]] = ..., ast_assert_rows_modified_node: _Optional[_Union[ASTAssertRowsModifiedProto, _Mapping]] = ..., ast_returning_clause_node: _Optional[_Union[ASTReturningClauseProto, _Mapping]] = ..., ast_column_attribute_node: _Optional[_Union[AnyASTColumnAttributeProto, _Mapping]] = ..., ast_column_attribute_list_node: _Optional[_Union[ASTColumnAttributeListProto, _Mapping]] = ..., ast_struct_column_field_node: _Optional[_Union[ASTStructColumnFieldProto, _Mapping]] = ..., ast_generated_column_info_node: _Optional[_Union[ASTGeneratedColumnInfoProto, _Mapping]] = ..., ast_table_element_node: _Optional[_Union[AnyASTTableElementProto, _Mapping]] = ..., ast_table_element_list_node: _Optional[_Union[ASTTableElementListProto, _Mapping]] = ..., ast_column_list_node: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., ast_column_position_node: _Optional[_Union[ASTColumnPositionProto, _Mapping]] = ..., ast_insert_values_row_node: _Optional[_Union[ASTInsertValuesRowProto, _Mapping]] = ..., ast_insert_values_row_list_node: _Optional[_Union[ASTInsertValuesRowListProto, _Mapping]] = ..., ast_update_set_value_node: _Optional[_Union[ASTUpdateSetValueProto, _Mapping]] = ..., ast_update_item_node: _Optional[_Union[ASTUpdateItemProto, _Mapping]] = ..., ast_update_item_list_node: _Optional[_Union[ASTUpdateItemListProto, _Mapping]] = ..., ast_merge_action_node: _Optional[_Union[ASTMergeActionProto, _Mapping]] = ..., ast_merge_when_clause_node: _Optional[_Union[ASTMergeWhenClauseProto, _Mapping]] = ..., ast_merge_when_clause_list_node: _Optional[_Union[ASTMergeWhenClauseListProto, _Mapping]] = ..., ast_privilege_node: _Optional[_Union[ASTPrivilegeProto, _Mapping]] = ..., ast_privileges_node: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., ast_grantee_list_node: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ..., ast_repeatable_clause_node: _Optional[_Union[ASTRepeatableClauseProto, _Mapping]] = ..., ast_filter_fields_arg_node: _Optional[_Union[ASTFilterFieldsArgProto, _Mapping]] = ..., ast_replace_fields_arg_node: _Optional[_Union[ASTReplaceFieldsArgProto, _Mapping]] = ..., ast_sample_size_node: _Optional[_Union[ASTSampleSizeProto, _Mapping]] = ..., ast_with_weight_node: _Optional[_Union[ASTWithWeightProto, _Mapping]] = ..., ast_sample_suffix_node: _Optional[_Union[ASTSampleSuffixProto, _Mapping]] = ..., ast_alter_action_node: _Optional[_Union[AnyASTAlterActionProto, _Mapping]] = ..., ast_alter_action_list_node: _Optional[_Union[ASTAlterActionListProto, _Mapping]] = ..., ast_foreign_key_actions_node: _Optional[_Union[ASTForeignKeyActionsProto, _Mapping]] = ..., ast_foreign_key_reference_node: _Optional[_Union[ASTForeignKeyReferenceProto, _Mapping]] = ..., ast_script_node: _Optional[_Union[ASTScriptProto, _Mapping]] = ..., ast_elseif_clause_node: _Optional[_Union[ASTElseifClauseProto, _Mapping]] = ..., ast_elseif_clause_list_node: _Optional[_Union[ASTElseifClauseListProto, _Mapping]] = ..., ast_when_then_clause_node: _Optional[_Union[ASTWhenThenClauseProto, _Mapping]] = ..., ast_when_then_clause_list_node: _Optional[_Union[ASTWhenThenClauseListProto, _Mapping]] = ..., ast_hint_node: _Optional[_Union[ASTHintProto, _Mapping]] = ..., ast_hint_entry_node: _Optional[_Union[ASTHintEntryProto, _Mapping]] = ..., ast_unpivot_in_item_label_node: _Optional[_Union[ASTUnpivotInItemLabelProto, _Mapping]] = ..., ast_descriptor_node: _Optional[_Union[ASTDescriptorProto, _Mapping]] = ..., ast_column_schema_node: _Optional[_Union[AnyASTColumnSchemaProto, _Mapping]] = ..., ast_descriptor_column_node: _Optional[_Union[ASTDescriptorColumnProto, _Mapping]] = ..., ast_descriptor_column_list_node: _Optional[_Union[ASTDescriptorColumnListProto, _Mapping]] = ..., ast_exception_handler_node: _Optional[_Union[ASTExceptionHandlerProto, _Mapping]] = ..., ast_exception_handler_list_node: _Optional[_Union[ASTExceptionHandlerListProto, _Mapping]] = ..., ast_identifier_list_node: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ..., ast_until_clause_node: _Optional[_Union[ASTUntilClauseProto, _Mapping]] = ..., ast_execute_into_clause_node: _Optional[_Union[ASTExecuteIntoClauseProto, _Mapping]] = ..., ast_execute_using_argument_node: _Optional[_Union[ASTExecuteUsingArgumentProto, _Mapping]] = ..., ast_execute_using_clause_node: _Optional[_Union[ASTExecuteUsingClauseProto, _Mapping]] = ..., ast_braced_constructor_field_value_node: _Optional[_Union[ASTBracedConstructorFieldValueProto, _Mapping]] = ..., ast_braced_constructor_field_node: _Optional[_Union[ASTBracedConstructorFieldProto, _Mapping]] = ..., ast_with_report_modifier_node: _Optional[_Union[ASTWithReportModifierProto, _Mapping]] = ..., ast_location_node: _Optional[_Union[ASTLocationProto, _Mapping]] = ..., ast_aux_load_data_from_files_options_list_node: _Optional[_Union[ASTAuxLoadDataFromFilesOptionsListProto, _Mapping]] = ..., ast_label_node: _Optional[_Union[ASTLabelProto, _Mapping]] = ..., ast_primary_key_element_node: _Optional[_Union[ASTPrimaryKeyElementProto, _Mapping]] = ..., ast_primary_key_element_list_node: _Optional[_Union[ASTPrimaryKeyElementListProto, _Mapping]] = ..., ast_spanner_table_options_node: _Optional[_Union[ASTSpannerTableOptionsProto, _Mapping]] = ..., ast_spanner_interleave_clause_node: _Optional[_Union[ASTSpannerInterleaveClauseProto, _Mapping]] = ..., ast_ttl_clause_node: _Optional[_Union[ASTTtlClauseProto, _Mapping]] = ..., ast_input_output_clause_node: _Optional[_Union[ASTInputOutputClauseProto, _Mapping]] = ..., ast_graph_label_expression_node: _Optional[_Union[AnyASTGraphLabelExpressionProto, _Mapping]] = ..., ast_graph_label_filter_node: _Optional[_Union[ASTGraphLabelFilterProto, _Mapping]] = ..., ast_select_with_node: _Optional[_Union[ASTSelectWithProto, _Mapping]] = ..., ast_aliased_query_list_node: _Optional[_Union[ASTAliasedQueryListProto, _Mapping]] = ..., ast_column_with_options_node: _Optional[_Union[ASTColumnWithOptionsProto, _Mapping]] = ..., ast_column_with_options_list_node: _Optional[_Union[ASTColumnWithOptionsListProto, _Mapping]] = ..., ast_graph_element_pattern_filler_node: _Optional[_Union[ASTGraphElementPatternFillerProto, _Mapping]] = ..., ast_graph_element_table_list_node: _Optional[_Union[ASTGraphElementTableListProto, _Mapping]] = ..., ast_graph_element_table_node: _Optional[_Union[ASTGraphElementTableProto, _Mapping]] = ..., ast_graph_node_table_reference_node: _Optional[_Union[ASTGraphNodeTableReferenceProto, _Mapping]] = ..., ast_aux_load_data_partitions_clause_node: _Optional[_Union[ASTAuxLoadDataPartitionsClauseProto, _Mapping]] = ..., ast_graph_element_label_and_properties_list_node: _Optional[_Union[ASTGraphElementLabelAndPropertiesListProto, _Mapping]] = ..., ast_graph_element_label_and_properties_node: _Optional[_Union[ASTGraphElementLabelAndPropertiesProto, _Mapping]] = ..., ast_graph_properties_node: _Optional[_Union[ASTGraphPropertiesProto, _Mapping]] = ..., ast_set_operation_metadata_list_node: _Optional[_Union[ASTSetOperationMetadataListProto, _Mapping]] = ..., ast_set_operation_all_or_distinct_node: _Optional[_Union[ASTSetOperationAllOrDistinctProto, _Mapping]] = ..., ast_set_operation_type_node: _Optional[_Union[ASTSetOperationTypeProto, _Mapping]] = ..., ast_set_operation_metadata_node: _Optional[_Union[ASTSetOperationMetadataProto, _Mapping]] = ..., ast_set_operation_column_match_mode_node: _Optional[_Union[ASTSetOperationColumnMatchModeProto, _Mapping]] = ..., ast_set_operation_column_propagation_mode_node: _Optional[_Union[ASTSetOperationColumnPropagationModeProto, _Mapping]] = ..., ast_graph_pattern_node: _Optional[_Union[ASTGraphPatternProto, _Mapping]] = ..., ast_cube_node: _Optional[_Union[ASTCubeProto, _Mapping]] = ..., ast_grouping_set_node: _Optional[_Union[ASTGroupingSetProto, _Mapping]] = ..., ast_grouping_set_list_node: _Optional[_Union[ASTGroupingSetListProto, _Mapping]] = ..., ast_expression_with_opt_alias_node: _Optional[_Union[ASTExpressionWithOptAliasProto, _Mapping]] = ..., ast_group_by_all_node: _Optional[_Union[ASTGroupByAllProto, _Mapping]] = ..., ast_function_type_arg_list_node: _Optional[_Union[ASTFunctionTypeArgListProto, _Mapping]] = ..., ast_pipe_operator_node: _Optional[_Union[AnyASTPipeOperatorProto, _Mapping]] = ..., ast_graph_lhs_hint_node: _Optional[_Union[ASTGraphLhsHintProto, _Mapping]] = ..., ast_graph_rhs_hint_node: _Optional[_Union[ASTGraphRhsHintProto, _Mapping]] = ..., ast_identity_column_info_node: _Optional[_Union[ASTIdentityColumnInfoProto, _Mapping]] = ..., ast_identity_column_start_with_node: _Optional[_Union[ASTIdentityColumnStartWithProto, _Mapping]] = ..., ast_identity_column_increment_by_node: _Optional[_Union[ASTIdentityColumnIncrementByProto, _Mapping]] = ..., ast_identity_column_max_value_node: _Optional[_Union[ASTIdentityColumnMaxValueProto, _Mapping]] = ..., ast_identity_column_min_value_node: _Optional[_Union[ASTIdentityColumnMinValueProto, _Mapping]] = ..., ast_graph_path_base_node: _Optional[_Union[AnyASTGraphPathBaseProto, _Mapping]] = ..., ast_gql_operator_node: _Optional[_Union[AnyASTGqlOperatorProto, _Mapping]] = ..., ast_gql_let_variable_definition_list_node: _Optional[_Union[ASTGqlLetVariableDefinitionListProto, _Mapping]] = ..., ast_gql_let_variable_definition_node: _Optional[_Union[ASTGqlLetVariableDefinitionProto, _Mapping]] = ..., ast_pipe_set_item_node: _Optional[_Union[ASTPipeSetItemProto, _Mapping]] = ..., ast_graph_property_specification_node: _Optional[_Union[ASTGraphPropertySpecificationProto, _Mapping]] = ..., ast_graph_property_name_and_value_node: _Optional[_Union[ASTGraphPropertyNameAndValueProto, _Mapping]] = ..., ast_gql_page_limit_node: _Optional[_Union[ASTGqlPageLimitProto, _Mapping]] = ..., ast_gql_page_offset_node: _Optional[_Union[ASTGqlPageOffsetProto, _Mapping]] = ..., ast_gql_page_node: _Optional[_Union[ASTGqlPageProto, _Mapping]] = ..., ast_aliased_query_modifiers_node: _Optional[_Union[ASTAliasedQueryModifiersProto, _Mapping]] = ..., ast_recursion_depth_modifier_node: _Optional[_Union[ASTRecursionDepthModifierProto, _Mapping]] = ..., ast_grouping_item_order_node: _Optional[_Union[ASTGroupingItemOrderProto, _Mapping]] = ..., ast_graph_path_mode_node: _Optional[_Union[ASTGraphPathModeProto, _Mapping]] = ..., ast_graph_path_search_prefix_node: _Optional[_Union[ASTGraphPathSearchPrefixProto, _Mapping]] = ..., ast_lock_mode_node: _Optional[_Union[ASTLockModeProto, _Mapping]] = ..., ast_row_pattern_expression_node: _Optional[_Union[AnyASTRowPatternExpressionProto, _Mapping]] = ..., ast_postfix_table_operator_node: _Optional[_Union[AnyASTPostfixTableOperatorProto, _Mapping]] = ..., ast_quantifier_node: _Optional[_Union[AnyASTQuantifierProto, _Mapping]] = ..., ast_quantifier_bound_node: _Optional[_Union[ASTQuantifierBoundProto, _Mapping]] = ..., ast_subpipeline_node: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ..., ast_after_match_skip_clause_node: _Optional[_Union[ASTAfterMatchSkipClauseProto, _Mapping]] = ..., ast_on_conflict_clause_node: _Optional[_Union[ASTOnConflictClauseProto, _Mapping]] = ..., ast_graph_dynamic_label_node: _Optional[_Union[ASTGraphDynamicLabelProto, _Mapping]] = ..., ast_graph_dynamic_properties_node: _Optional[_Union[ASTGraphDynamicPropertiesProto, _Mapping]] = ..., ast_graph_path_search_prefix_count_node: _Optional[_Union[ASTGraphPathSearchPrefixCountProto, _Mapping]] = ..., ast_chained_base_expr_node: _Optional[_Union[ASTChainedBaseExprProto, _Mapping]] = ..., ast_yield_item_list_node: _Optional[_Union[ASTYieldItemListProto, _Mapping]] = ..., ast_limit_all_node: _Optional[_Union[ASTLimitAllProto, _Mapping]] = ..., ast_limit_node: _Optional[_Union[ASTLimitProto, _Mapping]] = ..., ast_graph_derived_property_node: _Optional[_Union[ASTGraphDerivedPropertyProto, _Mapping]] = ..., ast_graph_derived_property_list_node: _Optional[_Union[ASTGraphDerivedPropertyListProto, _Mapping]] = ...) -> None: ...

class ASTNodeProto(_message.Message):
    __slots__ = ("parse_location_range",)
    PARSE_LOCATION_RANGE_FIELD_NUMBER: _ClassVar[int]
    parse_location_range: _parse_location_range_pb2.ParseLocationRangeProto
    def __init__(self, parse_location_range: _Optional[_Union[_parse_location_range_pb2.ParseLocationRangeProto, _Mapping]] = ...) -> None: ...

class AnyASTStatementProto(_message.Message):
    __slots__ = ("ast_query_statement_node", "ast_script_statement_node", "ast_hinted_statement_node", "ast_explain_statement_node", "ast_describe_statement_node", "ast_show_statement_node", "ast_begin_statement_node", "ast_set_transaction_statement_node", "ast_commit_statement_node", "ast_rollback_statement_node", "ast_start_batch_statement_node", "ast_run_batch_statement_node", "ast_abort_batch_statement_node", "ast_ddl_statement_node", "ast_drop_all_row_access_policies_statement_node", "ast_rename_statement_node", "ast_import_statement_node", "ast_module_statement_node", "ast_clone_data_statement_node", "ast_create_database_statement_node", "ast_export_data_statement_node", "ast_export_model_statement_node", "ast_call_statement_node", "ast_define_table_statement_node", "ast_analyze_statement_node", "ast_assert_statement_node", "ast_delete_statement_node", "ast_insert_statement_node", "ast_update_statement_node", "ast_truncate_statement_node", "ast_merge_statement_node", "ast_grant_statement_node", "ast_revoke_statement_node", "ast_alter_all_row_access_policies_statement_node", "ast_parameter_assignment_node", "ast_system_variable_assignment_node", "ast_execute_immediate_statement_node", "ast_define_macro_statement_node", "ast_export_metadata_statement_node", "ast_create_locality_group_statement_node", "ast_run_statement_node", "ast_subpipeline_statement_node", "ast_statement_with_pipe_operators_node")
    AST_QUERY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SCRIPT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HINTED_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPLAIN_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DESCRIBE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SHOW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BEGIN_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_TRANSACTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COMMIT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROLLBACK_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_START_BATCH_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RUN_BATCH_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ABORT_BATCH_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DDL_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_ALL_ROW_ACCESS_POLICIES_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RENAME_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IMPORT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MODULE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CLONE_DATA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_DATABASE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPORT_DATA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPORT_MODEL_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CALL_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DEFINE_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ANALYZE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ASSERT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DELETE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INSERT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UPDATE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TRUNCATE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MERGE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRANT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REVOKE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_ALL_ROW_ACCESS_POLICIES_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PARAMETER_ASSIGNMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SYSTEM_VARIABLE_ASSIGNMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXECUTE_IMMEDIATE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DEFINE_MACRO_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPORT_METADATA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_LOCALITY_GROUP_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RUN_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SUBPIPELINE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STATEMENT_WITH_PIPE_OPERATORS_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_query_statement_node: ASTQueryStatementProto
    ast_script_statement_node: AnyASTScriptStatementProto
    ast_hinted_statement_node: ASTHintedStatementProto
    ast_explain_statement_node: ASTExplainStatementProto
    ast_describe_statement_node: ASTDescribeStatementProto
    ast_show_statement_node: ASTShowStatementProto
    ast_begin_statement_node: ASTBeginStatementProto
    ast_set_transaction_statement_node: ASTSetTransactionStatementProto
    ast_commit_statement_node: ASTCommitStatementProto
    ast_rollback_statement_node: ASTRollbackStatementProto
    ast_start_batch_statement_node: ASTStartBatchStatementProto
    ast_run_batch_statement_node: ASTRunBatchStatementProto
    ast_abort_batch_statement_node: ASTAbortBatchStatementProto
    ast_ddl_statement_node: AnyASTDdlStatementProto
    ast_drop_all_row_access_policies_statement_node: ASTDropAllRowAccessPoliciesStatementProto
    ast_rename_statement_node: ASTRenameStatementProto
    ast_import_statement_node: ASTImportStatementProto
    ast_module_statement_node: ASTModuleStatementProto
    ast_clone_data_statement_node: ASTCloneDataStatementProto
    ast_create_database_statement_node: ASTCreateDatabaseStatementProto
    ast_export_data_statement_node: ASTExportDataStatementProto
    ast_export_model_statement_node: ASTExportModelStatementProto
    ast_call_statement_node: ASTCallStatementProto
    ast_define_table_statement_node: ASTDefineTableStatementProto
    ast_analyze_statement_node: ASTAnalyzeStatementProto
    ast_assert_statement_node: ASTAssertStatementProto
    ast_delete_statement_node: ASTDeleteStatementProto
    ast_insert_statement_node: ASTInsertStatementProto
    ast_update_statement_node: ASTUpdateStatementProto
    ast_truncate_statement_node: ASTTruncateStatementProto
    ast_merge_statement_node: ASTMergeStatementProto
    ast_grant_statement_node: ASTGrantStatementProto
    ast_revoke_statement_node: ASTRevokeStatementProto
    ast_alter_all_row_access_policies_statement_node: ASTAlterAllRowAccessPoliciesStatementProto
    ast_parameter_assignment_node: ASTParameterAssignmentProto
    ast_system_variable_assignment_node: ASTSystemVariableAssignmentProto
    ast_execute_immediate_statement_node: ASTExecuteImmediateStatementProto
    ast_define_macro_statement_node: ASTDefineMacroStatementProto
    ast_export_metadata_statement_node: ASTExportMetadataStatementProto
    ast_create_locality_group_statement_node: ASTCreateLocalityGroupStatementProto
    ast_run_statement_node: ASTRunStatementProto
    ast_subpipeline_statement_node: ASTSubpipelineStatementProto
    ast_statement_with_pipe_operators_node: ASTStatementWithPipeOperatorsProto
    def __init__(self, ast_query_statement_node: _Optional[_Union[ASTQueryStatementProto, _Mapping]] = ..., ast_script_statement_node: _Optional[_Union[AnyASTScriptStatementProto, _Mapping]] = ..., ast_hinted_statement_node: _Optional[_Union[ASTHintedStatementProto, _Mapping]] = ..., ast_explain_statement_node: _Optional[_Union[ASTExplainStatementProto, _Mapping]] = ..., ast_describe_statement_node: _Optional[_Union[ASTDescribeStatementProto, _Mapping]] = ..., ast_show_statement_node: _Optional[_Union[ASTShowStatementProto, _Mapping]] = ..., ast_begin_statement_node: _Optional[_Union[ASTBeginStatementProto, _Mapping]] = ..., ast_set_transaction_statement_node: _Optional[_Union[ASTSetTransactionStatementProto, _Mapping]] = ..., ast_commit_statement_node: _Optional[_Union[ASTCommitStatementProto, _Mapping]] = ..., ast_rollback_statement_node: _Optional[_Union[ASTRollbackStatementProto, _Mapping]] = ..., ast_start_batch_statement_node: _Optional[_Union[ASTStartBatchStatementProto, _Mapping]] = ..., ast_run_batch_statement_node: _Optional[_Union[ASTRunBatchStatementProto, _Mapping]] = ..., ast_abort_batch_statement_node: _Optional[_Union[ASTAbortBatchStatementProto, _Mapping]] = ..., ast_ddl_statement_node: _Optional[_Union[AnyASTDdlStatementProto, _Mapping]] = ..., ast_drop_all_row_access_policies_statement_node: _Optional[_Union[ASTDropAllRowAccessPoliciesStatementProto, _Mapping]] = ..., ast_rename_statement_node: _Optional[_Union[ASTRenameStatementProto, _Mapping]] = ..., ast_import_statement_node: _Optional[_Union[ASTImportStatementProto, _Mapping]] = ..., ast_module_statement_node: _Optional[_Union[ASTModuleStatementProto, _Mapping]] = ..., ast_clone_data_statement_node: _Optional[_Union[ASTCloneDataStatementProto, _Mapping]] = ..., ast_create_database_statement_node: _Optional[_Union[ASTCreateDatabaseStatementProto, _Mapping]] = ..., ast_export_data_statement_node: _Optional[_Union[ASTExportDataStatementProto, _Mapping]] = ..., ast_export_model_statement_node: _Optional[_Union[ASTExportModelStatementProto, _Mapping]] = ..., ast_call_statement_node: _Optional[_Union[ASTCallStatementProto, _Mapping]] = ..., ast_define_table_statement_node: _Optional[_Union[ASTDefineTableStatementProto, _Mapping]] = ..., ast_analyze_statement_node: _Optional[_Union[ASTAnalyzeStatementProto, _Mapping]] = ..., ast_assert_statement_node: _Optional[_Union[ASTAssertStatementProto, _Mapping]] = ..., ast_delete_statement_node: _Optional[_Union[ASTDeleteStatementProto, _Mapping]] = ..., ast_insert_statement_node: _Optional[_Union[ASTInsertStatementProto, _Mapping]] = ..., ast_update_statement_node: _Optional[_Union[ASTUpdateStatementProto, _Mapping]] = ..., ast_truncate_statement_node: _Optional[_Union[ASTTruncateStatementProto, _Mapping]] = ..., ast_merge_statement_node: _Optional[_Union[ASTMergeStatementProto, _Mapping]] = ..., ast_grant_statement_node: _Optional[_Union[ASTGrantStatementProto, _Mapping]] = ..., ast_revoke_statement_node: _Optional[_Union[ASTRevokeStatementProto, _Mapping]] = ..., ast_alter_all_row_access_policies_statement_node: _Optional[_Union[ASTAlterAllRowAccessPoliciesStatementProto, _Mapping]] = ..., ast_parameter_assignment_node: _Optional[_Union[ASTParameterAssignmentProto, _Mapping]] = ..., ast_system_variable_assignment_node: _Optional[_Union[ASTSystemVariableAssignmentProto, _Mapping]] = ..., ast_execute_immediate_statement_node: _Optional[_Union[ASTExecuteImmediateStatementProto, _Mapping]] = ..., ast_define_macro_statement_node: _Optional[_Union[ASTDefineMacroStatementProto, _Mapping]] = ..., ast_export_metadata_statement_node: _Optional[_Union[ASTExportMetadataStatementProto, _Mapping]] = ..., ast_create_locality_group_statement_node: _Optional[_Union[ASTCreateLocalityGroupStatementProto, _Mapping]] = ..., ast_run_statement_node: _Optional[_Union[ASTRunStatementProto, _Mapping]] = ..., ast_subpipeline_statement_node: _Optional[_Union[ASTSubpipelineStatementProto, _Mapping]] = ..., ast_statement_with_pipe_operators_node: _Optional[_Union[ASTStatementWithPipeOperatorsProto, _Mapping]] = ...) -> None: ...

class ASTStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTQueryStatementProto(_message.Message):
    __slots__ = ("parent", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    query: ASTQueryProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ...) -> None: ...

class ASTSubpipelineStatementProto(_message.Message):
    __slots__ = ("parent", "subpipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    subpipeline: ASTSubpipelineProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ...) -> None: ...

class AnyASTQueryExpressionProto(_message.Message):
    __slots__ = ("ast_query_node", "ast_select_node", "ast_set_operation_node", "ast_table_clause_node", "ast_from_query_node", "ast_gql_query_node", "ast_aliased_query_expression_node", "ast_gql_graph_pattern_query_node", "ast_gql_linear_ops_query_node")
    AST_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SELECT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FROM_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALIASED_QUERY_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_GRAPH_PATTERN_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_LINEAR_OPS_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_query_node: ASTQueryProto
    ast_select_node: ASTSelectProto
    ast_set_operation_node: ASTSetOperationProto
    ast_table_clause_node: ASTTableClauseProto
    ast_from_query_node: ASTFromQueryProto
    ast_gql_query_node: ASTGqlQueryProto
    ast_aliased_query_expression_node: ASTAliasedQueryExpressionProto
    ast_gql_graph_pattern_query_node: ASTGqlGraphPatternQueryProto
    ast_gql_linear_ops_query_node: ASTGqlLinearOpsQueryProto
    def __init__(self, ast_query_node: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., ast_select_node: _Optional[_Union[ASTSelectProto, _Mapping]] = ..., ast_set_operation_node: _Optional[_Union[ASTSetOperationProto, _Mapping]] = ..., ast_table_clause_node: _Optional[_Union[ASTTableClauseProto, _Mapping]] = ..., ast_from_query_node: _Optional[_Union[ASTFromQueryProto, _Mapping]] = ..., ast_gql_query_node: _Optional[_Union[ASTGqlQueryProto, _Mapping]] = ..., ast_aliased_query_expression_node: _Optional[_Union[ASTAliasedQueryExpressionProto, _Mapping]] = ..., ast_gql_graph_pattern_query_node: _Optional[_Union[ASTGqlGraphPatternQueryProto, _Mapping]] = ..., ast_gql_linear_ops_query_node: _Optional[_Union[ASTGqlLinearOpsQueryProto, _Mapping]] = ...) -> None: ...

class ASTQueryExpressionProto(_message.Message):
    __slots__ = ("parent", "parenthesized")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parenthesized: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parenthesized: bool = ...) -> None: ...

class ASTAliasedQueryExpressionProto(_message.Message):
    __slots__ = ("parent", "query", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    query: ASTQueryProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTQueryProto(_message.Message):
    __slots__ = ("parent", "with_clause", "query_expr", "order_by", "limit_offset", "is_nested", "is_pivot_input", "pipe_operator_list", "lock_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    QUERY_EXPR_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_NESTED_FIELD_NUMBER: _ClassVar[int]
    IS_PIVOT_INPUT_FIELD_NUMBER: _ClassVar[int]
    PIPE_OPERATOR_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCK_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    with_clause: ASTWithClauseProto
    query_expr: AnyASTQueryExpressionProto
    order_by: ASTOrderByProto
    limit_offset: ASTLimitOffsetProto
    is_nested: bool
    is_pivot_input: bool
    pipe_operator_list: _containers.RepeatedCompositeFieldContainer[AnyASTPipeOperatorProto]
    lock_mode: ASTLockModeProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., with_clause: _Optional[_Union[ASTWithClauseProto, _Mapping]] = ..., query_expr: _Optional[_Union[AnyASTQueryExpressionProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., limit_offset: _Optional[_Union[ASTLimitOffsetProto, _Mapping]] = ..., is_nested: bool = ..., is_pivot_input: bool = ..., pipe_operator_list: _Optional[_Iterable[_Union[AnyASTPipeOperatorProto, _Mapping]]] = ..., lock_mode: _Optional[_Union[ASTLockModeProto, _Mapping]] = ...) -> None: ...

class ASTFromQueryProto(_message.Message):
    __slots__ = ("parent", "from_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FROM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    from_clause: ASTFromClauseProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., from_clause: _Optional[_Union[ASTFromClauseProto, _Mapping]] = ...) -> None: ...

class ASTSubpipelineProto(_message.Message):
    __slots__ = ("parent", "pipe_operator_list", "parenthesized")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIPE_OPERATOR_LIST_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    pipe_operator_list: _containers.RepeatedCompositeFieldContainer[AnyASTPipeOperatorProto]
    parenthesized: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., pipe_operator_list: _Optional[_Iterable[_Union[AnyASTPipeOperatorProto, _Mapping]]] = ..., parenthesized: bool = ...) -> None: ...

class AnyASTPipeOperatorProto(_message.Message):
    __slots__ = ("ast_pipe_extend_node", "ast_pipe_aggregate_node", "ast_pipe_set_operation_node", "ast_pipe_join_node", "ast_pipe_call_node", "ast_pipe_window_node", "ast_pipe_where_node", "ast_pipe_select_node", "ast_pipe_limit_offset_node", "ast_pipe_order_by_node", "ast_pipe_distinct_node", "ast_pipe_tablesample_node", "ast_pipe_as_node", "ast_pipe_static_describe_node", "ast_pipe_assert_node", "ast_pipe_drop_node", "ast_pipe_set_node", "ast_pipe_pivot_node", "ast_pipe_unpivot_node", "ast_pipe_rename_item_node", "ast_pipe_rename_node", "ast_pipe_log_node", "ast_pipe_if_node", "ast_pipe_if_case_node", "ast_pipe_fork_node", "ast_pipe_export_data_node", "ast_pipe_recursive_union_node", "ast_pipe_match_recognize_node", "ast_pipe_create_table_node", "ast_pipe_tee_node", "ast_pipe_insert_node", "ast_pipe_with_node", "ast_pipe_describe_node")
    AST_PIPE_EXTEND_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_AGGREGATE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_SET_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_JOIN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_WINDOW_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_WHERE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_SELECT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_LIMIT_OFFSET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_ORDER_BY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_DISTINCT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_TABLESAMPLE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_AS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_STATIC_DESCRIBE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_ASSERT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_DROP_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_SET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_PIVOT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_UNPIVOT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_RENAME_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_RENAME_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_LOG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_IF_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_IF_CASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_FORK_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_EXPORT_DATA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_RECURSIVE_UNION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_MATCH_RECOGNIZE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_CREATE_TABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_TEE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_INSERT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_WITH_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_DESCRIBE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_pipe_extend_node: ASTPipeExtendProto
    ast_pipe_aggregate_node: ASTPipeAggregateProto
    ast_pipe_set_operation_node: ASTPipeSetOperationProto
    ast_pipe_join_node: ASTPipeJoinProto
    ast_pipe_call_node: ASTPipeCallProto
    ast_pipe_window_node: ASTPipeWindowProto
    ast_pipe_where_node: ASTPipeWhereProto
    ast_pipe_select_node: ASTPipeSelectProto
    ast_pipe_limit_offset_node: ASTPipeLimitOffsetProto
    ast_pipe_order_by_node: ASTPipeOrderByProto
    ast_pipe_distinct_node: ASTPipeDistinctProto
    ast_pipe_tablesample_node: ASTPipeTablesampleProto
    ast_pipe_as_node: ASTPipeAsProto
    ast_pipe_static_describe_node: ASTPipeStaticDescribeProto
    ast_pipe_assert_node: ASTPipeAssertProto
    ast_pipe_drop_node: ASTPipeDropProto
    ast_pipe_set_node: ASTPipeSetProto
    ast_pipe_pivot_node: ASTPipePivotProto
    ast_pipe_unpivot_node: ASTPipeUnpivotProto
    ast_pipe_rename_item_node: ASTPipeRenameItemProto
    ast_pipe_rename_node: ASTPipeRenameProto
    ast_pipe_log_node: ASTPipeLogProto
    ast_pipe_if_node: ASTPipeIfProto
    ast_pipe_if_case_node: ASTPipeIfCaseProto
    ast_pipe_fork_node: ASTPipeForkProto
    ast_pipe_export_data_node: ASTPipeExportDataProto
    ast_pipe_recursive_union_node: ASTPipeRecursiveUnionProto
    ast_pipe_match_recognize_node: ASTPipeMatchRecognizeProto
    ast_pipe_create_table_node: ASTPipeCreateTableProto
    ast_pipe_tee_node: ASTPipeTeeProto
    ast_pipe_insert_node: ASTPipeInsertProto
    ast_pipe_with_node: ASTPipeWithProto
    ast_pipe_describe_node: ASTPipeDescribeProto
    def __init__(self, ast_pipe_extend_node: _Optional[_Union[ASTPipeExtendProto, _Mapping]] = ..., ast_pipe_aggregate_node: _Optional[_Union[ASTPipeAggregateProto, _Mapping]] = ..., ast_pipe_set_operation_node: _Optional[_Union[ASTPipeSetOperationProto, _Mapping]] = ..., ast_pipe_join_node: _Optional[_Union[ASTPipeJoinProto, _Mapping]] = ..., ast_pipe_call_node: _Optional[_Union[ASTPipeCallProto, _Mapping]] = ..., ast_pipe_window_node: _Optional[_Union[ASTPipeWindowProto, _Mapping]] = ..., ast_pipe_where_node: _Optional[_Union[ASTPipeWhereProto, _Mapping]] = ..., ast_pipe_select_node: _Optional[_Union[ASTPipeSelectProto, _Mapping]] = ..., ast_pipe_limit_offset_node: _Optional[_Union[ASTPipeLimitOffsetProto, _Mapping]] = ..., ast_pipe_order_by_node: _Optional[_Union[ASTPipeOrderByProto, _Mapping]] = ..., ast_pipe_distinct_node: _Optional[_Union[ASTPipeDistinctProto, _Mapping]] = ..., ast_pipe_tablesample_node: _Optional[_Union[ASTPipeTablesampleProto, _Mapping]] = ..., ast_pipe_as_node: _Optional[_Union[ASTPipeAsProto, _Mapping]] = ..., ast_pipe_static_describe_node: _Optional[_Union[ASTPipeStaticDescribeProto, _Mapping]] = ..., ast_pipe_assert_node: _Optional[_Union[ASTPipeAssertProto, _Mapping]] = ..., ast_pipe_drop_node: _Optional[_Union[ASTPipeDropProto, _Mapping]] = ..., ast_pipe_set_node: _Optional[_Union[ASTPipeSetProto, _Mapping]] = ..., ast_pipe_pivot_node: _Optional[_Union[ASTPipePivotProto, _Mapping]] = ..., ast_pipe_unpivot_node: _Optional[_Union[ASTPipeUnpivotProto, _Mapping]] = ..., ast_pipe_rename_item_node: _Optional[_Union[ASTPipeRenameItemProto, _Mapping]] = ..., ast_pipe_rename_node: _Optional[_Union[ASTPipeRenameProto, _Mapping]] = ..., ast_pipe_log_node: _Optional[_Union[ASTPipeLogProto, _Mapping]] = ..., ast_pipe_if_node: _Optional[_Union[ASTPipeIfProto, _Mapping]] = ..., ast_pipe_if_case_node: _Optional[_Union[ASTPipeIfCaseProto, _Mapping]] = ..., ast_pipe_fork_node: _Optional[_Union[ASTPipeForkProto, _Mapping]] = ..., ast_pipe_export_data_node: _Optional[_Union[ASTPipeExportDataProto, _Mapping]] = ..., ast_pipe_recursive_union_node: _Optional[_Union[ASTPipeRecursiveUnionProto, _Mapping]] = ..., ast_pipe_match_recognize_node: _Optional[_Union[ASTPipeMatchRecognizeProto, _Mapping]] = ..., ast_pipe_create_table_node: _Optional[_Union[ASTPipeCreateTableProto, _Mapping]] = ..., ast_pipe_tee_node: _Optional[_Union[ASTPipeTeeProto, _Mapping]] = ..., ast_pipe_insert_node: _Optional[_Union[ASTPipeInsertProto, _Mapping]] = ..., ast_pipe_with_node: _Optional[_Union[ASTPipeWithProto, _Mapping]] = ..., ast_pipe_describe_node: _Optional[_Union[ASTPipeDescribeProto, _Mapping]] = ...) -> None: ...

class ASTPipeOperatorProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTPipeExtendProto(_message.Message):
    __slots__ = ("parent", "select")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    select: ASTSelectProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ...) -> None: ...

class ASTPipeRenameItemProto(_message.Message):
    __slots__ = ("parent", "old_name", "new_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OLD_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    old_name: ASTIdentifierProto
    new_name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., old_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., new_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTPipeRenameProto(_message.Message):
    __slots__ = ("parent", "rename_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RENAME_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    rename_item_list: _containers.RepeatedCompositeFieldContainer[ASTPipeRenameItemProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., rename_item_list: _Optional[_Iterable[_Union[ASTPipeRenameItemProto, _Mapping]]] = ...) -> None: ...

class ASTPipeAggregateProto(_message.Message):
    __slots__ = ("parent", "select", "select_with")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    SELECT_WITH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    select: ASTSelectProto
    select_with: ASTSelectWithProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ..., select_with: _Optional[_Union[ASTSelectWithProto, _Mapping]] = ...) -> None: ...

class ASTPipeSetOperationProto(_message.Message):
    __slots__ = ("parent", "metadata", "inputs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    metadata: ASTSetOperationMetadataProto
    inputs: _containers.RepeatedCompositeFieldContainer[AnyASTQueryExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., metadata: _Optional[_Union[ASTSetOperationMetadataProto, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[AnyASTQueryExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTPipeJoinProto(_message.Message):
    __slots__ = ("parent", "join")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    join: ASTJoinProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., join: _Optional[_Union[ASTJoinProto, _Mapping]] = ...) -> None: ...

class ASTPipeCallProto(_message.Message):
    __slots__ = ("parent", "tvf")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TVF_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    tvf: ASTTVFProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., tvf: _Optional[_Union[ASTTVFProto, _Mapping]] = ...) -> None: ...

class ASTPipeWindowProto(_message.Message):
    __slots__ = ("parent", "select")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    select: ASTSelectProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ...) -> None: ...

class ASTPipeWhereProto(_message.Message):
    __slots__ = ("parent", "where")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    where: ASTWhereClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., where: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeSelectProto(_message.Message):
    __slots__ = ("parent", "select")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    select: ASTSelectProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ...) -> None: ...

class ASTPipeLimitOffsetProto(_message.Message):
    __slots__ = ("parent", "limit_offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    limit_offset: ASTLimitOffsetProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., limit_offset: _Optional[_Union[ASTLimitOffsetProto, _Mapping]] = ...) -> None: ...

class ASTPipeOrderByProto(_message.Message):
    __slots__ = ("parent", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    order_by: ASTOrderByProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ...) -> None: ...

class ASTPipeDistinctProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ...) -> None: ...

class ASTPipeTablesampleProto(_message.Message):
    __slots__ = ("parent", "sample")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    sample: ASTSampleClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., sample: _Optional[_Union[ASTSampleClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeMatchRecognizeProto(_message.Message):
    __slots__ = ("parent", "match_recognize")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MATCH_RECOGNIZE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    match_recognize: ASTMatchRecognizeClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., match_recognize: _Optional[_Union[ASTMatchRecognizeClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeAsProto(_message.Message):
    __slots__ = ("parent", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTPipeDescribeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ...) -> None: ...

class ASTPipeStaticDescribeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ...) -> None: ...

class ASTPipeAssertProto(_message.Message):
    __slots__ = ("parent", "condition", "message_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    condition: AnyASTExpressionProto
    message_list: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., message_list: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTPipeLogProto(_message.Message):
    __slots__ = ("parent", "hint", "subpipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    hint: ASTHintProto
    subpipeline: ASTSubpipelineProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ...) -> None: ...

class ASTPipeDropProto(_message.Message):
    __slots__ = ("parent", "column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    column_list: ASTIdentifierListProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., column_list: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ...) -> None: ...

class ASTPipeSetItemProto(_message.Message):
    __slots__ = ("parent", "column", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    column: ASTIdentifierProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., column: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTPipeSetProto(_message.Message):
    __slots__ = ("parent", "set_item_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SET_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    set_item_list: _containers.RepeatedCompositeFieldContainer[ASTPipeSetItemProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., set_item_list: _Optional[_Iterable[_Union[ASTPipeSetItemProto, _Mapping]]] = ...) -> None: ...

class ASTPipePivotProto(_message.Message):
    __slots__ = ("parent", "pivot_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIVOT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    pivot_clause: ASTPivotClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., pivot_clause: _Optional[_Union[ASTPivotClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeUnpivotProto(_message.Message):
    __slots__ = ("parent", "unpivot_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    unpivot_clause: ASTUnpivotClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., unpivot_clause: _Optional[_Union[ASTUnpivotClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeIfProto(_message.Message):
    __slots__ = ("parent", "hint", "if_cases", "else_subpipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    IF_CASES_FIELD_NUMBER: _ClassVar[int]
    ELSE_SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    hint: ASTHintProto
    if_cases: _containers.RepeatedCompositeFieldContainer[ASTPipeIfCaseProto]
    else_subpipeline: ASTSubpipelineProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., if_cases: _Optional[_Iterable[_Union[ASTPipeIfCaseProto, _Mapping]]] = ..., else_subpipeline: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ...) -> None: ...

class ASTPipeIfCaseProto(_message.Message):
    __slots__ = ("parent", "condition", "subpipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    condition: AnyASTExpressionProto
    subpipeline: ASTSubpipelineProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., subpipeline: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ...) -> None: ...

class ASTPipeForkProto(_message.Message):
    __slots__ = ("parent", "hint", "subpipeline_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    hint: ASTHintProto
    subpipeline_list: _containers.RepeatedCompositeFieldContainer[ASTSubpipelineProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., subpipeline_list: _Optional[_Iterable[_Union[ASTSubpipelineProto, _Mapping]]] = ...) -> None: ...

class ASTPipeTeeProto(_message.Message):
    __slots__ = ("parent", "hint", "subpipeline_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    SUBPIPELINE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    hint: ASTHintProto
    subpipeline_list: _containers.RepeatedCompositeFieldContainer[ASTSubpipelineProto]
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., subpipeline_list: _Optional[_Iterable[_Union[ASTSubpipelineProto, _Mapping]]] = ...) -> None: ...

class ASTPipeWithProto(_message.Message):
    __slots__ = ("parent", "with_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    with_clause: ASTWithClauseProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., with_clause: _Optional[_Union[ASTWithClauseProto, _Mapping]] = ...) -> None: ...

class ASTPipeExportDataProto(_message.Message):
    __slots__ = ("parent", "export_data_statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DATA_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    export_data_statement: ASTExportDataStatementProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., export_data_statement: _Optional[_Union[ASTExportDataStatementProto, _Mapping]] = ...) -> None: ...

class ASTPipeCreateTableProto(_message.Message):
    __slots__ = ("parent", "create_table_statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TABLE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    create_table_statement: ASTCreateTableStatementProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., create_table_statement: _Optional[_Union[ASTCreateTableStatementProto, _Mapping]] = ...) -> None: ...

class ASTPipeInsertProto(_message.Message):
    __slots__ = ("parent", "insert_statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSERT_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    insert_statement: ASTInsertStatementProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., insert_statement: _Optional[_Union[ASTInsertStatementProto, _Mapping]] = ...) -> None: ...

class ASTSelectProto(_message.Message):
    __slots__ = ("parent", "hint", "select_with", "distinct", "select_as", "select_list", "from_clause", "where_clause", "group_by", "having", "qualify", "window_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    SELECT_WITH_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_FIELD_NUMBER: _ClassVar[int]
    SELECT_AS_FIELD_NUMBER: _ClassVar[int]
    SELECT_LIST_FIELD_NUMBER: _ClassVar[int]
    FROM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    HAVING_FIELD_NUMBER: _ClassVar[int]
    QUALIFY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    hint: ASTHintProto
    select_with: ASTSelectWithProto
    distinct: bool
    select_as: ASTSelectAsProto
    select_list: ASTSelectListProto
    from_clause: ASTFromClauseProto
    where_clause: ASTWhereClauseProto
    group_by: ASTGroupByProto
    having: ASTHavingProto
    qualify: ASTQualifyProto
    window_clause: ASTWindowClauseProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., select_with: _Optional[_Union[ASTSelectWithProto, _Mapping]] = ..., distinct: bool = ..., select_as: _Optional[_Union[ASTSelectAsProto, _Mapping]] = ..., select_list: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., from_clause: _Optional[_Union[ASTFromClauseProto, _Mapping]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ..., group_by: _Optional[_Union[ASTGroupByProto, _Mapping]] = ..., having: _Optional[_Union[ASTHavingProto, _Mapping]] = ..., qualify: _Optional[_Union[ASTQualifyProto, _Mapping]] = ..., window_clause: _Optional[_Union[ASTWindowClauseProto, _Mapping]] = ...) -> None: ...

class ASTSelectListProto(_message.Message):
    __slots__ = ("parent", "columns")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    columns: _containers.RepeatedCompositeFieldContainer[ASTSelectColumnProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[ASTSelectColumnProto, _Mapping]]] = ...) -> None: ...

class ASTSelectColumnProto(_message.Message):
    __slots__ = ("parent", "expression", "alias", "grouping_item_order")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    GROUPING_ITEM_ORDER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    grouping_item_order: ASTGroupingItemOrderProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., grouping_item_order: _Optional[_Union[ASTGroupingItemOrderProto, _Mapping]] = ...) -> None: ...

class AnyASTExpressionProto(_message.Message):
    __slots__ = ("ast_leaf_node", "ast_identifier_node", "ast_generalized_path_expression_node", "ast_and_expr_node", "ast_binary_expression_node", "ast_or_expr_node", "ast_cast_expression_node", "ast_function_call_node", "ast_array_constructor_node", "ast_struct_constructor_with_parens_node", "ast_struct_constructor_with_keyword_node", "ast_in_expression_node", "ast_between_expression_node", "ast_date_or_time_literal_node", "ast_case_value_expression_node", "ast_case_no_value_expression_node", "ast_bitwise_shift_expression_node", "ast_dot_star_node", "ast_dot_star_with_modifiers_node", "ast_expression_subquery_node", "ast_extract_expression_node", "ast_interval_expr_node", "ast_named_argument_node", "ast_star_with_modifiers_node", "ast_unary_expression_node", "ast_like_expression_node", "ast_parameter_expr_base_node", "ast_lambda_node", "ast_analytic_function_call_node", "ast_new_constructor_node", "ast_default_literal_node", "ast_replace_fields_expression_node", "ast_braced_constructor_node", "ast_braced_new_constructor_node", "ast_with_expression_node", "ast_range_literal_node", "ast_sequence_arg_node", "ast_expression_with_alias_node", "ast_struct_braced_constructor_node", "ast_int_or_unbounded_node", "ast_graph_is_labeled_predicate_node", "ast_braced_constructor_lhs_node", "ast_update_constructor_node", "ast_input_table_argument_node", "ast_concat_expr_node")
    AST_LEAF_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IDENTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GENERALIZED_PATH_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_AND_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BINARY_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_OR_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CAST_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ARRAY_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_CONSTRUCTOR_WITH_PARENS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_CONSTRUCTOR_WITH_KEYWORD_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_IN_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BETWEEN_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DATE_OR_TIME_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CASE_VALUE_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CASE_NO_VALUE_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BITWISE_SHIFT_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DOT_STAR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DOT_STAR_WITH_MODIFIERS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPRESSION_SUBQUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXTRACT_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INTERVAL_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NAMED_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STAR_WITH_MODIFIERS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNARY_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LIKE_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PARAMETER_EXPR_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LAMBDA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ANALYTIC_FUNCTION_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NEW_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DEFAULT_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REPLACE_FIELDS_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BRACED_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BRACED_NEW_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_WITH_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RANGE_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SEQUENCE_ARG_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXPRESSION_WITH_ALIAS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_BRACED_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INT_OR_UNBOUNDED_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_IS_LABELED_PREDICATE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BRACED_CONSTRUCTOR_LHS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UPDATE_CONSTRUCTOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INPUT_TABLE_ARGUMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CONCAT_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_leaf_node: AnyASTLeafProto
    ast_identifier_node: ASTIdentifierProto
    ast_generalized_path_expression_node: AnyASTGeneralizedPathExpressionProto
    ast_and_expr_node: ASTAndExprProto
    ast_binary_expression_node: ASTBinaryExpressionProto
    ast_or_expr_node: ASTOrExprProto
    ast_cast_expression_node: ASTCastExpressionProto
    ast_function_call_node: ASTFunctionCallProto
    ast_array_constructor_node: ASTArrayConstructorProto
    ast_struct_constructor_with_parens_node: ASTStructConstructorWithParensProto
    ast_struct_constructor_with_keyword_node: ASTStructConstructorWithKeywordProto
    ast_in_expression_node: ASTInExpressionProto
    ast_between_expression_node: ASTBetweenExpressionProto
    ast_date_or_time_literal_node: ASTDateOrTimeLiteralProto
    ast_case_value_expression_node: ASTCaseValueExpressionProto
    ast_case_no_value_expression_node: ASTCaseNoValueExpressionProto
    ast_bitwise_shift_expression_node: ASTBitwiseShiftExpressionProto
    ast_dot_star_node: ASTDotStarProto
    ast_dot_star_with_modifiers_node: ASTDotStarWithModifiersProto
    ast_expression_subquery_node: ASTExpressionSubqueryProto
    ast_extract_expression_node: ASTExtractExpressionProto
    ast_interval_expr_node: ASTIntervalExprProto
    ast_named_argument_node: ASTNamedArgumentProto
    ast_star_with_modifiers_node: ASTStarWithModifiersProto
    ast_unary_expression_node: ASTUnaryExpressionProto
    ast_like_expression_node: ASTLikeExpressionProto
    ast_parameter_expr_base_node: AnyASTParameterExprBaseProto
    ast_lambda_node: ASTLambdaProto
    ast_analytic_function_call_node: ASTAnalyticFunctionCallProto
    ast_new_constructor_node: ASTNewConstructorProto
    ast_default_literal_node: ASTDefaultLiteralProto
    ast_replace_fields_expression_node: ASTReplaceFieldsExpressionProto
    ast_braced_constructor_node: ASTBracedConstructorProto
    ast_braced_new_constructor_node: ASTBracedNewConstructorProto
    ast_with_expression_node: ASTWithExpressionProto
    ast_range_literal_node: ASTRangeLiteralProto
    ast_sequence_arg_node: ASTSequenceArgProto
    ast_expression_with_alias_node: ASTExpressionWithAliasProto
    ast_struct_braced_constructor_node: ASTStructBracedConstructorProto
    ast_int_or_unbounded_node: ASTIntOrUnboundedProto
    ast_graph_is_labeled_predicate_node: ASTGraphIsLabeledPredicateProto
    ast_braced_constructor_lhs_node: ASTBracedConstructorLhsProto
    ast_update_constructor_node: ASTUpdateConstructorProto
    ast_input_table_argument_node: ASTInputTableArgumentProto
    ast_concat_expr_node: ASTConcatExprProto
    def __init__(self, ast_leaf_node: _Optional[_Union[AnyASTLeafProto, _Mapping]] = ..., ast_identifier_node: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., ast_generalized_path_expression_node: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., ast_and_expr_node: _Optional[_Union[ASTAndExprProto, _Mapping]] = ..., ast_binary_expression_node: _Optional[_Union[ASTBinaryExpressionProto, _Mapping]] = ..., ast_or_expr_node: _Optional[_Union[ASTOrExprProto, _Mapping]] = ..., ast_cast_expression_node: _Optional[_Union[ASTCastExpressionProto, _Mapping]] = ..., ast_function_call_node: _Optional[_Union[ASTFunctionCallProto, _Mapping]] = ..., ast_array_constructor_node: _Optional[_Union[ASTArrayConstructorProto, _Mapping]] = ..., ast_struct_constructor_with_parens_node: _Optional[_Union[ASTStructConstructorWithParensProto, _Mapping]] = ..., ast_struct_constructor_with_keyword_node: _Optional[_Union[ASTStructConstructorWithKeywordProto, _Mapping]] = ..., ast_in_expression_node: _Optional[_Union[ASTInExpressionProto, _Mapping]] = ..., ast_between_expression_node: _Optional[_Union[ASTBetweenExpressionProto, _Mapping]] = ..., ast_date_or_time_literal_node: _Optional[_Union[ASTDateOrTimeLiteralProto, _Mapping]] = ..., ast_case_value_expression_node: _Optional[_Union[ASTCaseValueExpressionProto, _Mapping]] = ..., ast_case_no_value_expression_node: _Optional[_Union[ASTCaseNoValueExpressionProto, _Mapping]] = ..., ast_bitwise_shift_expression_node: _Optional[_Union[ASTBitwiseShiftExpressionProto, _Mapping]] = ..., ast_dot_star_node: _Optional[_Union[ASTDotStarProto, _Mapping]] = ..., ast_dot_star_with_modifiers_node: _Optional[_Union[ASTDotStarWithModifiersProto, _Mapping]] = ..., ast_expression_subquery_node: _Optional[_Union[ASTExpressionSubqueryProto, _Mapping]] = ..., ast_extract_expression_node: _Optional[_Union[ASTExtractExpressionProto, _Mapping]] = ..., ast_interval_expr_node: _Optional[_Union[ASTIntervalExprProto, _Mapping]] = ..., ast_named_argument_node: _Optional[_Union[ASTNamedArgumentProto, _Mapping]] = ..., ast_star_with_modifiers_node: _Optional[_Union[ASTStarWithModifiersProto, _Mapping]] = ..., ast_unary_expression_node: _Optional[_Union[ASTUnaryExpressionProto, _Mapping]] = ..., ast_like_expression_node: _Optional[_Union[ASTLikeExpressionProto, _Mapping]] = ..., ast_parameter_expr_base_node: _Optional[_Union[AnyASTParameterExprBaseProto, _Mapping]] = ..., ast_lambda_node: _Optional[_Union[ASTLambdaProto, _Mapping]] = ..., ast_analytic_function_call_node: _Optional[_Union[ASTAnalyticFunctionCallProto, _Mapping]] = ..., ast_new_constructor_node: _Optional[_Union[ASTNewConstructorProto, _Mapping]] = ..., ast_default_literal_node: _Optional[_Union[ASTDefaultLiteralProto, _Mapping]] = ..., ast_replace_fields_expression_node: _Optional[_Union[ASTReplaceFieldsExpressionProto, _Mapping]] = ..., ast_braced_constructor_node: _Optional[_Union[ASTBracedConstructorProto, _Mapping]] = ..., ast_braced_new_constructor_node: _Optional[_Union[ASTBracedNewConstructorProto, _Mapping]] = ..., ast_with_expression_node: _Optional[_Union[ASTWithExpressionProto, _Mapping]] = ..., ast_range_literal_node: _Optional[_Union[ASTRangeLiteralProto, _Mapping]] = ..., ast_sequence_arg_node: _Optional[_Union[ASTSequenceArgProto, _Mapping]] = ..., ast_expression_with_alias_node: _Optional[_Union[ASTExpressionWithAliasProto, _Mapping]] = ..., ast_struct_braced_constructor_node: _Optional[_Union[ASTStructBracedConstructorProto, _Mapping]] = ..., ast_int_or_unbounded_node: _Optional[_Union[ASTIntOrUnboundedProto, _Mapping]] = ..., ast_graph_is_labeled_predicate_node: _Optional[_Union[ASTGraphIsLabeledPredicateProto, _Mapping]] = ..., ast_braced_constructor_lhs_node: _Optional[_Union[ASTBracedConstructorLhsProto, _Mapping]] = ..., ast_update_constructor_node: _Optional[_Union[ASTUpdateConstructorProto, _Mapping]] = ..., ast_input_table_argument_node: _Optional[_Union[ASTInputTableArgumentProto, _Mapping]] = ..., ast_concat_expr_node: _Optional[_Union[ASTConcatExprProto, _Mapping]] = ...) -> None: ...

class ASTExpressionProto(_message.Message):
    __slots__ = ("parent", "parenthesized")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parenthesized: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parenthesized: bool = ...) -> None: ...

class AnyASTLeafProto(_message.Message):
    __slots__ = ("ast_string_literal_node", "ast_numeric_literal_node", "ast_bignumeric_literal_node", "ast_bytes_literal_node", "ast_json_literal_node", "ast_printable_leaf_node")
    AST_STRING_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NUMERIC_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BIGNUMERIC_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BYTES_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_JSON_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRINTABLE_LEAF_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_string_literal_node: ASTStringLiteralProto
    ast_numeric_literal_node: ASTNumericLiteralProto
    ast_bignumeric_literal_node: ASTBigNumericLiteralProto
    ast_bytes_literal_node: ASTBytesLiteralProto
    ast_json_literal_node: ASTJSONLiteralProto
    ast_printable_leaf_node: AnyASTPrintableLeafProto
    def __init__(self, ast_string_literal_node: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., ast_numeric_literal_node: _Optional[_Union[ASTNumericLiteralProto, _Mapping]] = ..., ast_bignumeric_literal_node: _Optional[_Union[ASTBigNumericLiteralProto, _Mapping]] = ..., ast_bytes_literal_node: _Optional[_Union[ASTBytesLiteralProto, _Mapping]] = ..., ast_json_literal_node: _Optional[_Union[ASTJSONLiteralProto, _Mapping]] = ..., ast_printable_leaf_node: _Optional[_Union[AnyASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTLeafProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTPrintableLeafProto(_message.Message):
    __slots__ = ("ast_int_literal_node", "ast_boolean_literal_node", "ast_star_node", "ast_float_literal_node", "ast_null_literal_node", "ast_max_literal_node", "ast_index_all_columns_node", "ast_macro_body_node", "ast_string_literal_component_node", "ast_bytes_literal_component_node")
    AST_INT_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BOOLEAN_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STAR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FLOAT_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_NULL_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MAX_LITERAL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INDEX_ALL_COLUMNS_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MACRO_BODY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRING_LITERAL_COMPONENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BYTES_LITERAL_COMPONENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_int_literal_node: ASTIntLiteralProto
    ast_boolean_literal_node: ASTBooleanLiteralProto
    ast_star_node: ASTStarProto
    ast_float_literal_node: ASTFloatLiteralProto
    ast_null_literal_node: ASTNullLiteralProto
    ast_max_literal_node: ASTMaxLiteralProto
    ast_index_all_columns_node: ASTIndexAllColumnsProto
    ast_macro_body_node: ASTMacroBodyProto
    ast_string_literal_component_node: ASTStringLiteralComponentProto
    ast_bytes_literal_component_node: ASTBytesLiteralComponentProto
    def __init__(self, ast_int_literal_node: _Optional[_Union[ASTIntLiteralProto, _Mapping]] = ..., ast_boolean_literal_node: _Optional[_Union[ASTBooleanLiteralProto, _Mapping]] = ..., ast_star_node: _Optional[_Union[ASTStarProto, _Mapping]] = ..., ast_float_literal_node: _Optional[_Union[ASTFloatLiteralProto, _Mapping]] = ..., ast_null_literal_node: _Optional[_Union[ASTNullLiteralProto, _Mapping]] = ..., ast_max_literal_node: _Optional[_Union[ASTMaxLiteralProto, _Mapping]] = ..., ast_index_all_columns_node: _Optional[_Union[ASTIndexAllColumnsProto, _Mapping]] = ..., ast_macro_body_node: _Optional[_Union[ASTMacroBodyProto, _Mapping]] = ..., ast_string_literal_component_node: _Optional[_Union[ASTStringLiteralComponentProto, _Mapping]] = ..., ast_bytes_literal_component_node: _Optional[_Union[ASTBytesLiteralComponentProto, _Mapping]] = ...) -> None: ...

class ASTPrintableLeafProto(_message.Message):
    __slots__ = ("parent", "image")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    image: str
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., image: _Optional[str] = ...) -> None: ...

class ASTIntLiteralProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTIdentifierProto(_message.Message):
    __slots__ = ("parent", "id_string", "is_quoted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ID_STRING_FIELD_NUMBER: _ClassVar[int]
    IS_QUOTED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    id_string: str
    is_quoted: bool
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., id_string: _Optional[str] = ..., is_quoted: bool = ...) -> None: ...

class ASTAliasProto(_message.Message):
    __slots__ = ("parent", "identifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class AnyASTGeneralizedPathExpressionProto(_message.Message):
    __slots__ = ("ast_path_expression_node", "ast_array_element_node", "ast_dot_generalized_field_node", "ast_dot_identifier_node", "ast_extended_path_expression_node")
    AST_PATH_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ARRAY_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DOT_GENERALIZED_FIELD_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DOT_IDENTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EXTENDED_PATH_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_path_expression_node: ASTPathExpressionProto
    ast_array_element_node: ASTArrayElementProto
    ast_dot_generalized_field_node: ASTDotGeneralizedFieldProto
    ast_dot_identifier_node: ASTDotIdentifierProto
    ast_extended_path_expression_node: ASTExtendedPathExpressionProto
    def __init__(self, ast_path_expression_node: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., ast_array_element_node: _Optional[_Union[ASTArrayElementProto, _Mapping]] = ..., ast_dot_generalized_field_node: _Optional[_Union[ASTDotGeneralizedFieldProto, _Mapping]] = ..., ast_dot_identifier_node: _Optional[_Union[ASTDotIdentifierProto, _Mapping]] = ..., ast_extended_path_expression_node: _Optional[_Union[ASTExtendedPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGeneralizedPathExpressionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTPathExpressionProto(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGeneralizedPathExpressionProto
    names: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    def __init__(self, parent: _Optional[_Union[ASTGeneralizedPathExpressionProto, _Mapping]] = ..., names: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ...) -> None: ...

class AnyASTPostfixTableOperatorProto(_message.Message):
    __slots__ = ("ast_pivot_clause_node", "ast_unpivot_clause_node", "ast_sample_clause_node", "ast_match_recognize_clause_node")
    AST_PIVOT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNPIVOT_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SAMPLE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MATCH_RECOGNIZE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_pivot_clause_node: ASTPivotClauseProto
    ast_unpivot_clause_node: ASTUnpivotClauseProto
    ast_sample_clause_node: ASTSampleClauseProto
    ast_match_recognize_clause_node: ASTMatchRecognizeClauseProto
    def __init__(self, ast_pivot_clause_node: _Optional[_Union[ASTPivotClauseProto, _Mapping]] = ..., ast_unpivot_clause_node: _Optional[_Union[ASTUnpivotClauseProto, _Mapping]] = ..., ast_sample_clause_node: _Optional[_Union[ASTSampleClauseProto, _Mapping]] = ..., ast_match_recognize_clause_node: _Optional[_Union[ASTMatchRecognizeClauseProto, _Mapping]] = ...) -> None: ...

class ASTPostfixTableOperatorProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class AnyASTTableExpressionProto(_message.Message):
    __slots__ = ("ast_table_path_expression_node", "ast_join_node", "ast_parenthesized_join_node", "ast_table_subquery_node", "ast_tvf_node", "ast_table_data_source_node", "ast_graph_table_query_node", "ast_pipe_join_lhs_placeholder_node")
    AST_TABLE_PATH_EXPRESSION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_JOIN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PARENTHESIZED_JOIN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_SUBQUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TVF_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_DATA_SOURCE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_TABLE_QUERY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PIPE_JOIN_LHS_PLACEHOLDER_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_table_path_expression_node: ASTTablePathExpressionProto
    ast_join_node: ASTJoinProto
    ast_parenthesized_join_node: ASTParenthesizedJoinProto
    ast_table_subquery_node: ASTTableSubqueryProto
    ast_tvf_node: ASTTVFProto
    ast_table_data_source_node: AnyASTTableDataSourceProto
    ast_graph_table_query_node: ASTGraphTableQueryProto
    ast_pipe_join_lhs_placeholder_node: ASTPipeJoinLhsPlaceholderProto
    def __init__(self, ast_table_path_expression_node: _Optional[_Union[ASTTablePathExpressionProto, _Mapping]] = ..., ast_join_node: _Optional[_Union[ASTJoinProto, _Mapping]] = ..., ast_parenthesized_join_node: _Optional[_Union[ASTParenthesizedJoinProto, _Mapping]] = ..., ast_table_subquery_node: _Optional[_Union[ASTTableSubqueryProto, _Mapping]] = ..., ast_tvf_node: _Optional[_Union[ASTTVFProto, _Mapping]] = ..., ast_table_data_source_node: _Optional[_Union[AnyASTTableDataSourceProto, _Mapping]] = ..., ast_graph_table_query_node: _Optional[_Union[ASTGraphTableQueryProto, _Mapping]] = ..., ast_pipe_join_lhs_placeholder_node: _Optional[_Union[ASTPipeJoinLhsPlaceholderProto, _Mapping]] = ...) -> None: ...

class ASTTableExpressionProto(_message.Message):
    __slots__ = ("parent", "postfix_operators")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_OPERATORS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    postfix_operators: _containers.RepeatedCompositeFieldContainer[AnyASTPostfixTableOperatorProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., postfix_operators: _Optional[_Iterable[_Union[AnyASTPostfixTableOperatorProto, _Mapping]]] = ...) -> None: ...

class ASTTablePathExpressionProto(_message.Message):
    __slots__ = ("parent", "path_expr", "unnest_expr", "hint", "alias", "with_offset", "for_system_time")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_EXPR_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPR_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    WITH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FOR_SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    path_expr: ASTPathExpressionProto
    unnest_expr: ASTUnnestExpressionProto
    hint: ASTHintProto
    alias: ASTAliasProto
    with_offset: ASTWithOffsetProto
    for_system_time: ASTForSystemTimeProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., path_expr: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., unnest_expr: _Optional[_Union[ASTUnnestExpressionProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., with_offset: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ..., for_system_time: _Optional[_Union[ASTForSystemTimeProto, _Mapping]] = ...) -> None: ...

class ASTPipeJoinLhsPlaceholderProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ...) -> None: ...

class ASTFromClauseProto(_message.Message):
    __slots__ = ("parent", "table_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_expression: AnyASTTableExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_expression: _Optional[_Union[AnyASTTableExpressionProto, _Mapping]] = ...) -> None: ...

class ASTWhereClauseProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTBooleanLiteralProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    value: bool
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ..., value: bool = ...) -> None: ...

class ASTAndExprProto(_message.Message):
    __slots__ = ("parent", "conjuncts")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONJUNCTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    conjuncts: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., conjuncts: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTBinaryExpressionProto(_message.Message):
    __slots__ = ("parent", "op", "is_not", "lhs", "rhs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    RHS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    op: _ast_enums_pb2.ASTBinaryExpressionEnums.Op
    is_not: bool
    lhs: AnyASTExpressionProto
    rhs: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., op: _Optional[_Union[_ast_enums_pb2.ASTBinaryExpressionEnums.Op, str]] = ..., is_not: bool = ..., lhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., rhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTStringLiteralProto(_message.Message):
    __slots__ = ("parent", "components", "string_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    components: _containers.RepeatedCompositeFieldContainer[ASTStringLiteralComponentProto]
    string_value: str
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., components: _Optional[_Iterable[_Union[ASTStringLiteralComponentProto, _Mapping]]] = ..., string_value: _Optional[str] = ...) -> None: ...

class ASTStringLiteralComponentProto(_message.Message):
    __slots__ = ("parent", "string_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    string_value: str
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ..., string_value: _Optional[str] = ...) -> None: ...

class ASTStarProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTOrExprProto(_message.Message):
    __slots__ = ("parent", "disjuncts")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISJUNCTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    disjuncts: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., disjuncts: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTConcatExprProto(_message.Message):
    __slots__ = ("parent", "operands")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERANDS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    operands: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., operands: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTOrderingExpressionProto(_message.Message):
    __slots__ = ("parent", "expression", "collate", "null_order", "ordering_spec", "option_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    NULL_ORDER_FIELD_NUMBER: _ClassVar[int]
    ORDERING_SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    collate: ASTCollateProto
    null_order: ASTNullOrderProto
    ordering_spec: _ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec
    option_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ..., null_order: _Optional[_Union[ASTNullOrderProto, _Mapping]] = ..., ordering_spec: _Optional[_Union[_ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec, str]] = ..., option_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTOrderByProto(_message.Message):
    __slots__ = ("parent", "hint", "ordering_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    ORDERING_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    hint: ASTHintProto
    ordering_expressions: _containers.RepeatedCompositeFieldContainer[ASTOrderingExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., ordering_expressions: _Optional[_Iterable[_Union[ASTOrderingExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTGroupingItemOrderProto(_message.Message):
    __slots__ = ("parent", "ordering_spec", "null_order")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDERING_SPEC_FIELD_NUMBER: _ClassVar[int]
    NULL_ORDER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    ordering_spec: _ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec
    null_order: ASTNullOrderProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., ordering_spec: _Optional[_Union[_ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec, str]] = ..., null_order: _Optional[_Union[ASTNullOrderProto, _Mapping]] = ...) -> None: ...

class ASTGroupingItemProto(_message.Message):
    __slots__ = ("parent", "expression", "rollup", "cube", "grouping_set_list", "alias", "grouping_item_order")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FIELD_NUMBER: _ClassVar[int]
    CUBE_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SET_LIST_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    GROUPING_ITEM_ORDER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    rollup: ASTRollupProto
    cube: ASTCubeProto
    grouping_set_list: ASTGroupingSetListProto
    alias: ASTAliasProto
    grouping_item_order: ASTGroupingItemOrderProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., rollup: _Optional[_Union[ASTRollupProto, _Mapping]] = ..., cube: _Optional[_Union[ASTCubeProto, _Mapping]] = ..., grouping_set_list: _Optional[_Union[ASTGroupingSetListProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., grouping_item_order: _Optional[_Union[ASTGroupingItemOrderProto, _Mapping]] = ...) -> None: ...

class ASTGroupByProto(_message.Message):
    __slots__ = ("parent", "hint", "all", "grouping_items", "and_order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    GROUPING_ITEMS_FIELD_NUMBER: _ClassVar[int]
    AND_ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    hint: ASTHintProto
    all: ASTGroupByAllProto
    grouping_items: _containers.RepeatedCompositeFieldContainer[ASTGroupingItemProto]
    and_order_by: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., all: _Optional[_Union[ASTGroupByAllProto, _Mapping]] = ..., grouping_items: _Optional[_Iterable[_Union[ASTGroupingItemProto, _Mapping]]] = ..., and_order_by: bool = ...) -> None: ...

class ASTGroupByAllProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTLimitAllProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTLimitProto(_message.Message):
    __slots__ = ("parent", "all", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    all: ASTLimitAllProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., all: _Optional[_Union[ASTLimitAllProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTLimitOffsetProto(_message.Message):
    __slots__ = ("parent", "limit", "offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    limit: ASTLimitProto
    offset: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., limit: _Optional[_Union[ASTLimitProto, _Mapping]] = ..., offset: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTFloatLiteralProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTNullLiteralProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTOnClauseProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTAliasedQueryProto(_message.Message):
    __slots__ = ("parent", "alias", "query", "modifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    alias: ASTIdentifierProto
    query: ASTQueryProto
    modifiers: ASTAliasedQueryModifiersProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., alias: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., modifiers: _Optional[_Union[ASTAliasedQueryModifiersProto, _Mapping]] = ...) -> None: ...

class ASTJoinProto(_message.Message):
    __slots__ = ("parent", "lhs", "hint", "rhs", "on_clause", "using_clause", "clause_list", "join_type", "join_hint", "natural", "unmatched_join_count", "transformation_needed", "contains_comma_join", "join_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    RHS_FIELD_NUMBER: _ClassVar[int]
    ON_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    USING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_LIST_FIELD_NUMBER: _ClassVar[int]
    JOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOIN_HINT_FIELD_NUMBER: _ClassVar[int]
    NATURAL_FIELD_NUMBER: _ClassVar[int]
    UNMATCHED_JOIN_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_NEEDED_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_COMMA_JOIN_FIELD_NUMBER: _ClassVar[int]
    JOIN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    lhs: AnyASTTableExpressionProto
    hint: ASTHintProto
    rhs: AnyASTTableExpressionProto
    on_clause: ASTOnClauseProto
    using_clause: ASTUsingClauseProto
    clause_list: ASTOnOrUsingClauseListProto
    join_type: _ast_enums_pb2.ASTJoinEnums.JoinType
    join_hint: _ast_enums_pb2.ASTJoinEnums.JoinHint
    natural: bool
    unmatched_join_count: int
    transformation_needed: bool
    contains_comma_join: bool
    join_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., lhs: _Optional[_Union[AnyASTTableExpressionProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., rhs: _Optional[_Union[AnyASTTableExpressionProto, _Mapping]] = ..., on_clause: _Optional[_Union[ASTOnClauseProto, _Mapping]] = ..., using_clause: _Optional[_Union[ASTUsingClauseProto, _Mapping]] = ..., clause_list: _Optional[_Union[ASTOnOrUsingClauseListProto, _Mapping]] = ..., join_type: _Optional[_Union[_ast_enums_pb2.ASTJoinEnums.JoinType, str]] = ..., join_hint: _Optional[_Union[_ast_enums_pb2.ASTJoinEnums.JoinHint, str]] = ..., natural: bool = ..., unmatched_join_count: _Optional[int] = ..., transformation_needed: bool = ..., contains_comma_join: bool = ..., join_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTWithClauseProto(_message.Message):
    __slots__ = ("parent", "recursive")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    recursive: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., recursive: bool = ..., **kwargs) -> None: ...

class ASTHavingProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTTypeProto(_message.Message):
    __slots__ = ("ast_simple_type_node", "ast_array_type_node", "ast_struct_type_node", "ast_range_type_node", "ast_function_type_node", "ast_map_type_node")
    AST_SIMPLE_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ARRAY_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RANGE_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FUNCTION_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_MAP_TYPE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_simple_type_node: ASTSimpleTypeProto
    ast_array_type_node: ASTArrayTypeProto
    ast_struct_type_node: ASTStructTypeProto
    ast_range_type_node: ASTRangeTypeProto
    ast_function_type_node: ASTFunctionTypeProto
    ast_map_type_node: ASTMapTypeProto
    def __init__(self, ast_simple_type_node: _Optional[_Union[ASTSimpleTypeProto, _Mapping]] = ..., ast_array_type_node: _Optional[_Union[ASTArrayTypeProto, _Mapping]] = ..., ast_struct_type_node: _Optional[_Union[ASTStructTypeProto, _Mapping]] = ..., ast_range_type_node: _Optional[_Union[ASTRangeTypeProto, _Mapping]] = ..., ast_function_type_node: _Optional[_Union[ASTFunctionTypeProto, _Mapping]] = ..., ast_map_type_node: _Optional[_Union[ASTMapTypeProto, _Mapping]] = ...) -> None: ...

class ASTTypeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTSimpleTypeProto(_message.Message):
    __slots__ = ("parent", "type_name", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    type_name: ASTPathExpressionProto
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., type_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTArrayTypeProto(_message.Message):
    __slots__ = ("parent", "element_type", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    element_type: AnyASTTypeProto
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., element_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTStructFieldProto(_message.Message):
    __slots__ = ("parent", "name", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    type: AnyASTTypeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ...) -> None: ...

class ASTStructTypeProto(_message.Message):
    __slots__ = ("parent", "struct_fields", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    struct_fields: _containers.RepeatedCompositeFieldContainer[ASTStructFieldProto]
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., struct_fields: _Optional[_Iterable[_Union[ASTStructFieldProto, _Mapping]]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTFunctionTypeArgListProto(_message.Message):
    __slots__ = ("parent", "args")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    args: _containers.RepeatedCompositeFieldContainer[AnyASTTypeProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., args: _Optional[_Iterable[_Union[AnyASTTypeProto, _Mapping]]] = ...) -> None: ...

class ASTFunctionTypeProto(_message.Message):
    __slots__ = ("parent", "arg_list", "return_type", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARG_LIST_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    arg_list: ASTFunctionTypeArgListProto
    return_type: AnyASTTypeProto
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., arg_list: _Optional[_Union[ASTFunctionTypeArgListProto, _Mapping]] = ..., return_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTCastExpressionProto(_message.Message):
    __slots__ = ("parent", "expr", "type", "format", "is_safe_cast")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    IS_SAFE_CAST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    expr: AnyASTExpressionProto
    type: AnyASTTypeProto
    format: ASTFormatClauseProto
    is_safe_cast: bool
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., format: _Optional[_Union[ASTFormatClauseProto, _Mapping]] = ..., is_safe_cast: bool = ...) -> None: ...

class ASTSelectAsProto(_message.Message):
    __slots__ = ("parent", "type_name", "as_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    AS_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    type_name: ASTPathExpressionProto
    as_mode: _ast_enums_pb2.ASTSelectAsEnums.AsMode
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., type_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., as_mode: _Optional[_Union[_ast_enums_pb2.ASTSelectAsEnums.AsMode, str]] = ...) -> None: ...

class ASTRollupProto(_message.Message):
    __slots__ = ("parent", "expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTCubeProto(_message.Message):
    __slots__ = ("parent", "expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTGroupingSetProto(_message.Message):
    __slots__ = ("parent", "expression", "rollup", "cube")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FIELD_NUMBER: _ClassVar[int]
    CUBE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    rollup: ASTRollupProto
    cube: ASTCubeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., rollup: _Optional[_Union[ASTRollupProto, _Mapping]] = ..., cube: _Optional[_Union[ASTCubeProto, _Mapping]] = ...) -> None: ...

class ASTGroupingSetListProto(_message.Message):
    __slots__ = ("parent", "grouping_sets")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SETS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    grouping_sets: _containers.RepeatedCompositeFieldContainer[ASTGroupingSetProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., grouping_sets: _Optional[_Iterable[_Union[ASTGroupingSetProto, _Mapping]]] = ...) -> None: ...

class ASTExpressionWithAliasProto(_message.Message):
    __slots__ = ("parent", "expression", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTFunctionCallProto(_message.Message):
    __slots__ = ("parent", "function", "arguments", "having_modifier", "clamped_between_modifier", "order_by", "limit_offset", "hint", "null_handling_modifier", "distinct", "is_current_date_time_without_parentheses", "with_report_modifier", "group_by", "where_expr", "having_expr", "is_chained_call")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    HAVING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    CLAMPED_BETWEEN_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    NULL_HANDLING_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENT_DATE_TIME_WITHOUT_PARENTHESES_FIELD_NUMBER: _ClassVar[int]
    WITH_REPORT_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    WHERE_EXPR_FIELD_NUMBER: _ClassVar[int]
    HAVING_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_CHAINED_CALL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    function: ASTPathExpressionProto
    arguments: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    having_modifier: ASTHavingModifierProto
    clamped_between_modifier: ASTClampedBetweenModifierProto
    order_by: ASTOrderByProto
    limit_offset: ASTLimitOffsetProto
    hint: ASTHintProto
    null_handling_modifier: _ast_enums_pb2.ASTFunctionCallEnums.NullHandlingModifier
    distinct: bool
    is_current_date_time_without_parentheses: bool
    with_report_modifier: ASTWithReportModifierProto
    group_by: ASTGroupByProto
    where_expr: ASTWhereClauseProto
    having_expr: ASTHavingProto
    is_chained_call: bool
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., function: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ..., having_modifier: _Optional[_Union[ASTHavingModifierProto, _Mapping]] = ..., clamped_between_modifier: _Optional[_Union[ASTClampedBetweenModifierProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., limit_offset: _Optional[_Union[ASTLimitOffsetProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., null_handling_modifier: _Optional[_Union[_ast_enums_pb2.ASTFunctionCallEnums.NullHandlingModifier, str]] = ..., distinct: bool = ..., is_current_date_time_without_parentheses: bool = ..., with_report_modifier: _Optional[_Union[ASTWithReportModifierProto, _Mapping]] = ..., group_by: _Optional[_Union[ASTGroupByProto, _Mapping]] = ..., where_expr: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ..., having_expr: _Optional[_Union[ASTHavingProto, _Mapping]] = ..., is_chained_call: bool = ...) -> None: ...

class ASTChainedBaseExprProto(_message.Message):
    __slots__ = ("parent", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTArrayConstructorProto(_message.Message):
    __slots__ = ("parent", "type", "elements")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    type: ASTArrayTypeProto
    elements: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., type: _Optional[_Union[ASTArrayTypeProto, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTStructConstructorArgProto(_message.Message):
    __slots__ = ("parent", "expression", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTStructConstructorWithParensProto(_message.Message):
    __slots__ = ("parent", "field_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    field_expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., field_expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTStructConstructorWithKeywordProto(_message.Message):
    __slots__ = ("parent", "struct_type", "fields")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    struct_type: ASTStructTypeProto
    fields: _containers.RepeatedCompositeFieldContainer[ASTStructConstructorArgProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., struct_type: _Optional[_Union[ASTStructTypeProto, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[ASTStructConstructorArgProto, _Mapping]]] = ...) -> None: ...

class ASTInExpressionProto(_message.Message):
    __slots__ = ("parent", "lhs", "hint", "in_list", "query", "unnest_expr", "is_not", "in_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    IN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    lhs: AnyASTExpressionProto
    hint: ASTHintProto
    in_list: ASTInListProto
    query: ASTQueryProto
    unnest_expr: ASTUnnestExpressionProto
    is_not: bool
    in_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., lhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., in_list: _Optional[_Union[ASTInListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., unnest_expr: _Optional[_Union[ASTUnnestExpressionProto, _Mapping]] = ..., is_not: bool = ..., in_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTInListProto(_message.Message):
    __slots__ = ("parent", "list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    list: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., list: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTBetweenExpressionProto(_message.Message):
    __slots__ = ("parent", "lhs", "low", "high", "is_not", "between_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    lhs: AnyASTExpressionProto
    low: AnyASTExpressionProto
    high: AnyASTExpressionProto
    is_not: bool
    between_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., lhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., low: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., high: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_not: bool = ..., between_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTNumericLiteralProto(_message.Message):
    __slots__ = ("parent", "string_literal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_LITERAL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    string_literal: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., string_literal: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTBigNumericLiteralProto(_message.Message):
    __slots__ = ("parent", "string_literal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_LITERAL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    string_literal: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., string_literal: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTBytesLiteralProto(_message.Message):
    __slots__ = ("parent", "components", "bytes_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    components: _containers.RepeatedCompositeFieldContainer[ASTBytesLiteralComponentProto]
    bytes_value: str
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., components: _Optional[_Iterable[_Union[ASTBytesLiteralComponentProto, _Mapping]]] = ..., bytes_value: _Optional[str] = ...) -> None: ...

class ASTBytesLiteralComponentProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTDateOrTimeLiteralProto(_message.Message):
    __slots__ = ("parent", "string_literal", "type_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_LITERAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    string_literal: ASTStringLiteralProto
    type_kind: _type_pb2.TypeKind
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., string_literal: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., type_kind: _Optional[_Union[_type_pb2.TypeKind, str]] = ...) -> None: ...

class ASTMaxLiteralProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTJSONLiteralProto(_message.Message):
    __slots__ = ("parent", "string_literal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_LITERAL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLeafProto
    string_literal: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTLeafProto, _Mapping]] = ..., string_literal: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTCaseValueExpressionProto(_message.Message):
    __slots__ = ("parent", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    arguments: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTCaseNoValueExpressionProto(_message.Message):
    __slots__ = ("parent", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    arguments: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTArrayElementProto(_message.Message):
    __slots__ = ("parent", "array", "position", "open_bracket_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    OPEN_BRACKET_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGeneralizedPathExpressionProto
    array: AnyASTExpressionProto
    position: AnyASTExpressionProto
    open_bracket_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTGeneralizedPathExpressionProto, _Mapping]] = ..., array: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., position: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., open_bracket_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTBitwiseShiftExpressionProto(_message.Message):
    __slots__ = ("parent", "lhs", "rhs", "is_left_shift", "operator_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    RHS_FIELD_NUMBER: _ClassVar[int]
    IS_LEFT_SHIFT_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    lhs: AnyASTExpressionProto
    rhs: AnyASTExpressionProto
    is_left_shift: bool
    operator_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., lhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., rhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_left_shift: bool = ..., operator_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTCollateProto(_message.Message):
    __slots__ = ("parent", "collation_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATION_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    collation_name: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., collation_name: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTDotGeneralizedFieldProto(_message.Message):
    __slots__ = ("parent", "expr", "path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGeneralizedPathExpressionProto
    expr: AnyASTExpressionProto
    path: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTGeneralizedPathExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTDotIdentifierProto(_message.Message):
    __slots__ = ("parent", "expr", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGeneralizedPathExpressionProto
    expr: AnyASTExpressionProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTGeneralizedPathExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTDotStarProto(_message.Message):
    __slots__ = ("parent", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTDotStarWithModifiersProto(_message.Message):
    __slots__ = ("parent", "expr", "modifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    expr: AnyASTExpressionProto
    modifiers: ASTStarModifiersProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., modifiers: _Optional[_Union[ASTStarModifiersProto, _Mapping]] = ...) -> None: ...

class ASTExpressionSubqueryProto(_message.Message):
    __slots__ = ("parent", "hint", "query", "modifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    hint: ASTHintProto
    query: ASTQueryProto
    modifier: _ast_enums_pb2.ASTExpressionSubqueryEnums.Modifier
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., modifier: _Optional[_Union[_ast_enums_pb2.ASTExpressionSubqueryEnums.Modifier, str]] = ...) -> None: ...

class ASTExtractExpressionProto(_message.Message):
    __slots__ = ("parent", "lhs_expr", "rhs_expr", "time_zone_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_EXPR_FIELD_NUMBER: _ClassVar[int]
    RHS_EXPR_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    lhs_expr: AnyASTExpressionProto
    rhs_expr: AnyASTExpressionProto
    time_zone_expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., lhs_expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., rhs_expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., time_zone_expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTHavingModifierProto(_message.Message):
    __slots__ = ("parent", "expr", "modifier_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expr: AnyASTExpressionProto
    modifier_kind: _ast_enums_pb2.ASTHavingModifierEnums.ModifierKind
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., modifier_kind: _Optional[_Union[_ast_enums_pb2.ASTHavingModifierEnums.ModifierKind, str]] = ...) -> None: ...

class ASTIntervalExprProto(_message.Message):
    __slots__ = ("parent", "interval_value", "date_part_name", "date_part_name_to")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_PART_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_PART_NAME_TO_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    interval_value: AnyASTExpressionProto
    date_part_name: ASTIdentifierProto
    date_part_name_to: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., interval_value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., date_part_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., date_part_name_to: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTSequenceArgProto(_message.Message):
    __slots__ = ("parent", "sequence_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    sequence_path: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., sequence_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTNamedArgumentProto(_message.Message):
    __slots__ = ("parent", "name", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    name: ASTIdentifierProto
    expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTInputTableArgumentProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTNullOrderProto(_message.Message):
    __slots__ = ("parent", "nulls_first")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NULLS_FIRST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    nulls_first: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., nulls_first: bool = ...) -> None: ...

class ASTOnOrUsingClauseListProto(_message.Message):
    __slots__ = ("parent", "on_or_using_clause_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ON_OR_USING_CLAUSE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    on_or_using_clause_list: _containers.RepeatedCompositeFieldContainer[ASTNodeProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., on_or_using_clause_list: _Optional[_Iterable[_Union[ASTNodeProto, _Mapping]]] = ...) -> None: ...

class ASTParenthesizedJoinProto(_message.Message):
    __slots__ = ("parent", "join")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    join: ASTJoinProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., join: _Optional[_Union[ASTJoinProto, _Mapping]] = ...) -> None: ...

class ASTPartitionByProto(_message.Message):
    __slots__ = ("parent", "hint", "partitioning_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    PARTITIONING_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    hint: ASTHintProto
    partitioning_expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., partitioning_expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTSetOperationProto(_message.Message):
    __slots__ = ("parent", "metadata", "inputs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    metadata: ASTSetOperationMetadataListProto
    inputs: _containers.RepeatedCompositeFieldContainer[AnyASTQueryExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., metadata: _Optional[_Union[ASTSetOperationMetadataListProto, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[AnyASTQueryExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTSetOperationMetadataListProto(_message.Message):
    __slots__ = ("parent", "set_operation_metadata_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SET_OPERATION_METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    set_operation_metadata_list: _containers.RepeatedCompositeFieldContainer[ASTSetOperationMetadataProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., set_operation_metadata_list: _Optional[_Iterable[_Union[ASTSetOperationMetadataProto, _Mapping]]] = ...) -> None: ...

class ASTSetOperationAllOrDistinctProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: _ast_enums_pb2.ASTSetOperationEnums.AllOrDistinct
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[_ast_enums_pb2.ASTSetOperationEnums.AllOrDistinct, str]] = ...) -> None: ...

class ASTSetOperationTypeProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: _ast_enums_pb2.ASTSetOperationEnums.OperationType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[_ast_enums_pb2.ASTSetOperationEnums.OperationType, str]] = ...) -> None: ...

class ASTSetOperationColumnMatchModeProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: _ast_enums_pb2.ASTSetOperationEnums.ColumnMatchMode
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[_ast_enums_pb2.ASTSetOperationEnums.ColumnMatchMode, str]] = ...) -> None: ...

class ASTSetOperationColumnPropagationModeProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: _ast_enums_pb2.ASTSetOperationEnums.ColumnPropagationMode
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[_ast_enums_pb2.ASTSetOperationEnums.ColumnPropagationMode, str]] = ...) -> None: ...

class ASTSetOperationMetadataProto(_message.Message):
    __slots__ = ("parent", "op_type", "all_or_distinct", "hint", "column_match_mode", "column_propagation_mode", "corresponding_by_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALL_OR_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_PROPAGATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_BY_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    op_type: ASTSetOperationTypeProto
    all_or_distinct: ASTSetOperationAllOrDistinctProto
    hint: ASTHintProto
    column_match_mode: ASTSetOperationColumnMatchModeProto
    column_propagation_mode: ASTSetOperationColumnPropagationModeProto
    corresponding_by_column_list: ASTColumnListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., op_type: _Optional[_Union[ASTSetOperationTypeProto, _Mapping]] = ..., all_or_distinct: _Optional[_Union[ASTSetOperationAllOrDistinctProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., column_match_mode: _Optional[_Union[ASTSetOperationColumnMatchModeProto, _Mapping]] = ..., column_propagation_mode: _Optional[_Union[ASTSetOperationColumnPropagationModeProto, _Mapping]] = ..., corresponding_by_column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ...) -> None: ...

class ASTStarExceptListProto(_message.Message):
    __slots__ = ("parent", "identifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifiers: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifiers: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ...) -> None: ...

class ASTStarModifiersProto(_message.Message):
    __slots__ = ("parent", "except_list", "replace_items")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_LIST_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    except_list: ASTStarExceptListProto
    replace_items: _containers.RepeatedCompositeFieldContainer[ASTStarReplaceItemProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., except_list: _Optional[_Union[ASTStarExceptListProto, _Mapping]] = ..., replace_items: _Optional[_Iterable[_Union[ASTStarReplaceItemProto, _Mapping]]] = ...) -> None: ...

class ASTStarReplaceItemProto(_message.Message):
    __slots__ = ("parent", "expression", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTStarWithModifiersProto(_message.Message):
    __slots__ = ("parent", "modifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    modifiers: ASTStarModifiersProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., modifiers: _Optional[_Union[ASTStarModifiersProto, _Mapping]] = ...) -> None: ...

class ASTTableSubqueryProto(_message.Message):
    __slots__ = ("parent", "subquery", "alias", "is_lateral")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    IS_LATERAL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    subquery: ASTQueryProto
    alias: ASTAliasProto
    is_lateral: bool
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., subquery: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., is_lateral: bool = ...) -> None: ...

class ASTUnaryExpressionProto(_message.Message):
    __slots__ = ("parent", "operand", "op")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    operand: AnyASTExpressionProto
    op: _ast_enums_pb2.ASTUnaryExpressionEnums.Op
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., operand: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., op: _Optional[_Union[_ast_enums_pb2.ASTUnaryExpressionEnums.Op, str]] = ...) -> None: ...

class ASTExpressionWithOptAliasProto(_message.Message):
    __slots__ = ("parent", "expression", "optional_alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    optional_alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., optional_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTUnnestExpressionProto(_message.Message):
    __slots__ = ("parent", "expressions", "array_zip_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ZIP_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expressions: _containers.RepeatedCompositeFieldContainer[ASTExpressionWithOptAliasProto]
    array_zip_mode: ASTNamedArgumentProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[ASTExpressionWithOptAliasProto, _Mapping]]] = ..., array_zip_mode: _Optional[_Union[ASTNamedArgumentProto, _Mapping]] = ...) -> None: ...

class ASTWindowClauseProto(_message.Message):
    __slots__ = ("parent", "windows")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    windows: _containers.RepeatedCompositeFieldContainer[ASTWindowDefinitionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., windows: _Optional[_Iterable[_Union[ASTWindowDefinitionProto, _Mapping]]] = ...) -> None: ...

class ASTWindowDefinitionProto(_message.Message):
    __slots__ = ("parent", "name", "window_spec")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WINDOW_SPEC_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    window_spec: ASTWindowSpecificationProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., window_spec: _Optional[_Union[ASTWindowSpecificationProto, _Mapping]] = ...) -> None: ...

class ASTWindowFrameProto(_message.Message):
    __slots__ = ("parent", "start_expr", "end_expr", "frame_unit")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_EXPR_FIELD_NUMBER: _ClassVar[int]
    END_EXPR_FIELD_NUMBER: _ClassVar[int]
    FRAME_UNIT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    start_expr: ASTWindowFrameExprProto
    end_expr: ASTWindowFrameExprProto
    frame_unit: _ast_enums_pb2.ASTWindowFrameEnums.FrameUnit
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., start_expr: _Optional[_Union[ASTWindowFrameExprProto, _Mapping]] = ..., end_expr: _Optional[_Union[ASTWindowFrameExprProto, _Mapping]] = ..., frame_unit: _Optional[_Union[_ast_enums_pb2.ASTWindowFrameEnums.FrameUnit, str]] = ...) -> None: ...

class ASTWindowFrameExprProto(_message.Message):
    __slots__ = ("parent", "expression", "boundary_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    boundary_type: _ast_enums_pb2.ASTWindowFrameExprEnums.BoundaryType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., boundary_type: _Optional[_Union[_ast_enums_pb2.ASTWindowFrameExprEnums.BoundaryType, str]] = ...) -> None: ...

class ASTLikeExpressionProto(_message.Message):
    __slots__ = ("parent", "lhs", "op", "hint", "in_list", "query", "unnest_expr", "is_not", "like_location")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LHS_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    LIKE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    lhs: AnyASTExpressionProto
    op: ASTAnySomeAllOpProto
    hint: ASTHintProto
    in_list: ASTInListProto
    query: ASTQueryProto
    unnest_expr: ASTUnnestExpressionProto
    is_not: bool
    like_location: ASTLocationProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., lhs: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., op: _Optional[_Union[ASTAnySomeAllOpProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., in_list: _Optional[_Union[ASTInListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., unnest_expr: _Optional[_Union[ASTUnnestExpressionProto, _Mapping]] = ..., is_not: bool = ..., like_location: _Optional[_Union[ASTLocationProto, _Mapping]] = ...) -> None: ...

class ASTWindowSpecificationProto(_message.Message):
    __slots__ = ("parent", "base_window_name", "partition_by", "order_by", "window_frame")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BASE_WINDOW_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FRAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    base_window_name: ASTIdentifierProto
    partition_by: ASTPartitionByProto
    order_by: ASTOrderByProto
    window_frame: ASTWindowFrameProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., base_window_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., window_frame: _Optional[_Union[ASTWindowFrameProto, _Mapping]] = ...) -> None: ...

class ASTWithOffsetProto(_message.Message):
    __slots__ = ("parent", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTAnySomeAllOpProto(_message.Message):
    __slots__ = ("parent", "op")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    op: _ast_enums_pb2.ASTAnySomeAllOpEnums.Op
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., op: _Optional[_Union[_ast_enums_pb2.ASTAnySomeAllOpEnums.Op, str]] = ...) -> None: ...

class AnyASTParameterExprBaseProto(_message.Message):
    __slots__ = ("ast_parameter_expr_node", "ast_system_variable_expr_node")
    AST_PARAMETER_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SYSTEM_VARIABLE_EXPR_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_parameter_expr_node: ASTParameterExprProto
    ast_system_variable_expr_node: ASTSystemVariableExprProto
    def __init__(self, ast_parameter_expr_node: _Optional[_Union[ASTParameterExprProto, _Mapping]] = ..., ast_system_variable_expr_node: _Optional[_Union[ASTSystemVariableExprProto, _Mapping]] = ...) -> None: ...

class ASTParameterExprBaseProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTStatementListProto(_message.Message):
    __slots__ = ("parent", "statement_list", "variable_declarations_allowed")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_DECLARATIONS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    statement_list: _containers.RepeatedCompositeFieldContainer[AnyASTStatementProto]
    variable_declarations_allowed: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., statement_list: _Optional[_Iterable[_Union[AnyASTStatementProto, _Mapping]]] = ..., variable_declarations_allowed: bool = ...) -> None: ...

class AnyASTScriptStatementProto(_message.Message):
    __slots__ = ("ast_if_statement_node", "ast_case_statement_node", "ast_raise_statement_node", "ast_begin_end_block_node", "ast_variable_declaration_node", "ast_break_continue_statement_node", "ast_return_statement_node", "ast_single_assignment_node", "ast_assignment_from_struct_node", "ast_loop_statement_node")
    AST_IF_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CASE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RAISE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BEGIN_END_BLOCK_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_VARIABLE_DECLARATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_BREAK_CONTINUE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RETURN_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SINGLE_ASSIGNMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ASSIGNMENT_FROM_STRUCT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_LOOP_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_if_statement_node: ASTIfStatementProto
    ast_case_statement_node: ASTCaseStatementProto
    ast_raise_statement_node: ASTRaiseStatementProto
    ast_begin_end_block_node: ASTBeginEndBlockProto
    ast_variable_declaration_node: ASTVariableDeclarationProto
    ast_break_continue_statement_node: AnyASTBreakContinueStatementProto
    ast_return_statement_node: ASTReturnStatementProto
    ast_single_assignment_node: ASTSingleAssignmentProto
    ast_assignment_from_struct_node: ASTAssignmentFromStructProto
    ast_loop_statement_node: AnyASTLoopStatementProto
    def __init__(self, ast_if_statement_node: _Optional[_Union[ASTIfStatementProto, _Mapping]] = ..., ast_case_statement_node: _Optional[_Union[ASTCaseStatementProto, _Mapping]] = ..., ast_raise_statement_node: _Optional[_Union[ASTRaiseStatementProto, _Mapping]] = ..., ast_begin_end_block_node: _Optional[_Union[ASTBeginEndBlockProto, _Mapping]] = ..., ast_variable_declaration_node: _Optional[_Union[ASTVariableDeclarationProto, _Mapping]] = ..., ast_break_continue_statement_node: _Optional[_Union[AnyASTBreakContinueStatementProto, _Mapping]] = ..., ast_return_statement_node: _Optional[_Union[ASTReturnStatementProto, _Mapping]] = ..., ast_single_assignment_node: _Optional[_Union[ASTSingleAssignmentProto, _Mapping]] = ..., ast_assignment_from_struct_node: _Optional[_Union[ASTAssignmentFromStructProto, _Mapping]] = ..., ast_loop_statement_node: _Optional[_Union[AnyASTLoopStatementProto, _Mapping]] = ...) -> None: ...

class ASTScriptStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTHintedStatementProto(_message.Message):
    __slots__ = ("parent", "hint", "statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    hint: ASTHintProto
    statement: AnyASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., statement: _Optional[_Union[AnyASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTStatementWithPipeOperatorsProto(_message.Message):
    __slots__ = ("parent", "statement", "pipe_operator_suffix")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PIPE_OPERATOR_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    statement: AnyASTStatementProto
    pipe_operator_suffix: ASTSubpipelineStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., statement: _Optional[_Union[AnyASTStatementProto, _Mapping]] = ..., pipe_operator_suffix: _Optional[_Union[ASTSubpipelineStatementProto, _Mapping]] = ...) -> None: ...

class ASTExplainStatementProto(_message.Message):
    __slots__ = ("parent", "statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    statement: AnyASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., statement: _Optional[_Union[AnyASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTDescribeStatementProto(_message.Message):
    __slots__ = ("parent", "optional_identifier", "name", "optional_from_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FROM_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    optional_identifier: ASTIdentifierProto
    name: ASTPathExpressionProto
    optional_from_name: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., optional_identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., optional_from_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTShowStatementProto(_message.Message):
    __slots__ = ("parent", "identifier", "optional_name", "optional_like_string")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LIKE_STRING_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    identifier: ASTIdentifierProto
    optional_name: ASTPathExpressionProto
    optional_like_string: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., optional_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., optional_like_string: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class AnyASTTransactionModeProto(_message.Message):
    __slots__ = ("ast_transaction_isolation_level_node", "ast_transaction_read_write_mode_node")
    AST_TRANSACTION_ISOLATION_LEVEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TRANSACTION_READ_WRITE_MODE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_transaction_isolation_level_node: ASTTransactionIsolationLevelProto
    ast_transaction_read_write_mode_node: ASTTransactionReadWriteModeProto
    def __init__(self, ast_transaction_isolation_level_node: _Optional[_Union[ASTTransactionIsolationLevelProto, _Mapping]] = ..., ast_transaction_read_write_mode_node: _Optional[_Union[ASTTransactionReadWriteModeProto, _Mapping]] = ...) -> None: ...

class ASTTransactionModeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTTransactionIsolationLevelProto(_message.Message):
    __slots__ = ("parent", "identifier1", "identifier2")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER1_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER2_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTransactionModeProto
    identifier1: ASTIdentifierProto
    identifier2: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTTransactionModeProto, _Mapping]] = ..., identifier1: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., identifier2: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTTransactionReadWriteModeProto(_message.Message):
    __slots__ = ("parent", "mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTransactionModeProto
    mode: _ast_enums_pb2.ASTTransactionReadWriteModeEnums.Mode
    def __init__(self, parent: _Optional[_Union[ASTTransactionModeProto, _Mapping]] = ..., mode: _Optional[_Union[_ast_enums_pb2.ASTTransactionReadWriteModeEnums.Mode, str]] = ...) -> None: ...

class ASTTransactionModeListProto(_message.Message):
    __slots__ = ("parent", "elements")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    elements: _containers.RepeatedCompositeFieldContainer[AnyASTTransactionModeProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[AnyASTTransactionModeProto, _Mapping]]] = ...) -> None: ...

class ASTBeginStatementProto(_message.Message):
    __slots__ = ("parent", "mode_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    mode_list: ASTTransactionModeListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., mode_list: _Optional[_Union[ASTTransactionModeListProto, _Mapping]] = ...) -> None: ...

class ASTSetTransactionStatementProto(_message.Message):
    __slots__ = ("parent", "mode_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    mode_list: ASTTransactionModeListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., mode_list: _Optional[_Union[ASTTransactionModeListProto, _Mapping]] = ...) -> None: ...

class ASTCommitStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTRollbackStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTStartBatchStatementProto(_message.Message):
    __slots__ = ("parent", "batch_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    batch_type: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., batch_type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTRunBatchStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTAbortBatchStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class AnyASTDdlStatementProto(_message.Message):
    __slots__ = ("ast_drop_entity_statement_node", "ast_drop_function_statement_node", "ast_drop_table_function_statement_node", "ast_drop_materialized_view_statement_node", "ast_drop_snapshot_table_statement_node", "ast_create_statement_node", "ast_drop_row_access_policy_statement_node", "ast_drop_statement_node", "ast_alter_statement_base_node", "ast_drop_privilege_restriction_statement_node", "ast_undrop_statement_node", "ast_drop_index_statement_node")
    AST_DROP_ENTITY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_FUNCTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_TABLE_FUNCTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_MATERIALIZED_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_SNAPSHOT_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_ROW_ACCESS_POLICY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_STATEMENT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_PRIVILEGE_RESTRICTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_UNDROP_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_INDEX_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_drop_entity_statement_node: ASTDropEntityStatementProto
    ast_drop_function_statement_node: ASTDropFunctionStatementProto
    ast_drop_table_function_statement_node: ASTDropTableFunctionStatementProto
    ast_drop_materialized_view_statement_node: ASTDropMaterializedViewStatementProto
    ast_drop_snapshot_table_statement_node: ASTDropSnapshotTableStatementProto
    ast_create_statement_node: AnyASTCreateStatementProto
    ast_drop_row_access_policy_statement_node: ASTDropRowAccessPolicyStatementProto
    ast_drop_statement_node: ASTDropStatementProto
    ast_alter_statement_base_node: AnyASTAlterStatementBaseProto
    ast_drop_privilege_restriction_statement_node: ASTDropPrivilegeRestrictionStatementProto
    ast_undrop_statement_node: ASTUndropStatementProto
    ast_drop_index_statement_node: AnyASTDropIndexStatementProto
    def __init__(self, ast_drop_entity_statement_node: _Optional[_Union[ASTDropEntityStatementProto, _Mapping]] = ..., ast_drop_function_statement_node: _Optional[_Union[ASTDropFunctionStatementProto, _Mapping]] = ..., ast_drop_table_function_statement_node: _Optional[_Union[ASTDropTableFunctionStatementProto, _Mapping]] = ..., ast_drop_materialized_view_statement_node: _Optional[_Union[ASTDropMaterializedViewStatementProto, _Mapping]] = ..., ast_drop_snapshot_table_statement_node: _Optional[_Union[ASTDropSnapshotTableStatementProto, _Mapping]] = ..., ast_create_statement_node: _Optional[_Union[AnyASTCreateStatementProto, _Mapping]] = ..., ast_drop_row_access_policy_statement_node: _Optional[_Union[ASTDropRowAccessPolicyStatementProto, _Mapping]] = ..., ast_drop_statement_node: _Optional[_Union[ASTDropStatementProto, _Mapping]] = ..., ast_alter_statement_base_node: _Optional[_Union[AnyASTAlterStatementBaseProto, _Mapping]] = ..., ast_drop_privilege_restriction_statement_node: _Optional[_Union[ASTDropPrivilegeRestrictionStatementProto, _Mapping]] = ..., ast_undrop_statement_node: _Optional[_Union[ASTUndropStatementProto, _Mapping]] = ..., ast_drop_index_statement_node: _Optional[_Union[AnyASTDropIndexStatementProto, _Mapping]] = ...) -> None: ...

class ASTDdlStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ...) -> None: ...

class ASTDropEntityStatementProto(_message.Message):
    __slots__ = ("parent", "entity_type", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    entity_type: ASTIdentifierProto
    name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., entity_type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropFunctionStatementProto(_message.Message):
    __slots__ = ("parent", "name", "parameters", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    parameters: ASTFunctionParametersProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., parameters: _Optional[_Union[ASTFunctionParametersProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropTableFunctionStatementProto(_message.Message):
    __slots__ = ("parent", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropAllRowAccessPoliciesStatementProto(_message.Message):
    __slots__ = ("parent", "table_name", "has_access_keyword")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_ACCESS_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    table_name: ASTPathExpressionProto
    has_access_keyword: bool
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., has_access_keyword: bool = ...) -> None: ...

class ASTDropMaterializedViewStatementProto(_message.Message):
    __slots__ = ("parent", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropSnapshotTableStatementProto(_message.Message):
    __slots__ = ("parent", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class AnyASTDropIndexStatementProto(_message.Message):
    __slots__ = ("ast_drop_search_index_statement_node", "ast_drop_vector_index_statement_node")
    AST_DROP_SEARCH_INDEX_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_VECTOR_INDEX_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_drop_search_index_statement_node: ASTDropSearchIndexStatementProto
    ast_drop_vector_index_statement_node: ASTDropVectorIndexStatementProto
    def __init__(self, ast_drop_search_index_statement_node: _Optional[_Union[ASTDropSearchIndexStatementProto, _Mapping]] = ..., ast_drop_vector_index_statement_node: _Optional[_Union[ASTDropVectorIndexStatementProto, _Mapping]] = ...) -> None: ...

class ASTDropIndexStatementProto(_message.Message):
    __slots__ = ("parent", "name", "table_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    table_name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropSearchIndexStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDropIndexStatementProto
    def __init__(self, parent: _Optional[_Union[ASTDropIndexStatementProto, _Mapping]] = ...) -> None: ...

class ASTDropVectorIndexStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDropIndexStatementProto
    def __init__(self, parent: _Optional[_Union[ASTDropIndexStatementProto, _Mapping]] = ...) -> None: ...

class ASTRenameStatementProto(_message.Message):
    __slots__ = ("parent", "identifier", "old_name", "new_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OLD_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    identifier: ASTIdentifierProto
    old_name: ASTPathExpressionProto
    new_name: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., old_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., new_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTImportStatementProto(_message.Message):
    __slots__ = ("parent", "name", "string_value", "alias", "into_alias", "options_list", "import_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    INTO_ALIAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IMPORT_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTPathExpressionProto
    string_value: ASTStringLiteralProto
    alias: ASTAliasProto
    into_alias: ASTIntoAliasProto
    options_list: ASTOptionsListProto
    import_kind: _ast_enums_pb2.ASTImportStatementEnums.ImportKind
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., string_value: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., into_alias: _Optional[_Union[ASTIntoAliasProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., import_kind: _Optional[_Union[_ast_enums_pb2.ASTImportStatementEnums.ImportKind, str]] = ...) -> None: ...

class ASTModuleStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTWithConnectionClauseProto(_message.Message):
    __slots__ = ("parent", "connection_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    connection_clause: ASTConnectionClauseProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., connection_clause: _Optional[_Union[ASTConnectionClauseProto, _Mapping]] = ...) -> None: ...

class ASTIntoAliasProto(_message.Message):
    __slots__ = ("parent", "identifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTUnnestExpressionWithOptAliasAndOffsetProto(_message.Message):
    __slots__ = ("parent", "unnest_expression", "optional_alias", "optional_with_offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALIAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_WITH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    unnest_expression: ASTUnnestExpressionProto
    optional_alias: ASTAliasProto
    optional_with_offset: ASTWithOffsetProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., unnest_expression: _Optional[_Union[ASTUnnestExpressionProto, _Mapping]] = ..., optional_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., optional_with_offset: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ...) -> None: ...

class ASTPivotExpressionProto(_message.Message):
    __slots__ = ("parent", "expression", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTPivotValueProto(_message.Message):
    __slots__ = ("parent", "value", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: AnyASTExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTPivotExpressionListProto(_message.Message):
    __slots__ = ("parent", "expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expressions: _containers.RepeatedCompositeFieldContainer[ASTPivotExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[ASTPivotExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTPivotValueListProto(_message.Message):
    __slots__ = ("parent", "values")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    values: _containers.RepeatedCompositeFieldContainer[ASTPivotValueProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., values: _Optional[_Iterable[_Union[ASTPivotValueProto, _Mapping]]] = ...) -> None: ...

class ASTPivotClauseProto(_message.Message):
    __slots__ = ("parent", "pivot_expressions", "for_expression", "pivot_values", "output_alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIVOT_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PIVOT_VALUES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPostfixTableOperatorProto
    pivot_expressions: ASTPivotExpressionListProto
    for_expression: AnyASTExpressionProto
    pivot_values: ASTPivotValueListProto
    output_alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTPostfixTableOperatorProto, _Mapping]] = ..., pivot_expressions: _Optional[_Union[ASTPivotExpressionListProto, _Mapping]] = ..., for_expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., pivot_values: _Optional[_Union[ASTPivotValueListProto, _Mapping]] = ..., output_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTUnpivotInItemProto(_message.Message):
    __slots__ = ("parent", "unpivot_columns", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    unpivot_columns: ASTPathExpressionListProto
    alias: ASTUnpivotInItemLabelProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., unpivot_columns: _Optional[_Union[ASTPathExpressionListProto, _Mapping]] = ..., alias: _Optional[_Union[ASTUnpivotInItemLabelProto, _Mapping]] = ...) -> None: ...

class ASTUnpivotInItemListProto(_message.Message):
    __slots__ = ("parent", "in_items")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    in_items: _containers.RepeatedCompositeFieldContainer[ASTUnpivotInItemProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., in_items: _Optional[_Iterable[_Union[ASTUnpivotInItemProto, _Mapping]]] = ...) -> None: ...

class ASTUnpivotClauseProto(_message.Message):
    __slots__ = ("parent", "unpivot_output_value_columns", "unpivot_output_name_column", "unpivot_in_items", "output_alias", "null_filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_OUTPUT_VALUE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_OUTPUT_NAME_COLUMN_FIELD_NUMBER: _ClassVar[int]
    UNPIVOT_IN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ALIAS_FIELD_NUMBER: _ClassVar[int]
    NULL_FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPostfixTableOperatorProto
    unpivot_output_value_columns: ASTPathExpressionListProto
    unpivot_output_name_column: ASTPathExpressionProto
    unpivot_in_items: ASTUnpivotInItemListProto
    output_alias: ASTAliasProto
    null_filter: _ast_enums_pb2.ASTUnpivotClauseEnums.NullFilter
    def __init__(self, parent: _Optional[_Union[ASTPostfixTableOperatorProto, _Mapping]] = ..., unpivot_output_value_columns: _Optional[_Union[ASTPathExpressionListProto, _Mapping]] = ..., unpivot_output_name_column: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., unpivot_in_items: _Optional[_Union[ASTUnpivotInItemListProto, _Mapping]] = ..., output_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., null_filter: _Optional[_Union[_ast_enums_pb2.ASTUnpivotClauseEnums.NullFilter, str]] = ...) -> None: ...

class ASTUsingClauseProto(_message.Message):
    __slots__ = ("parent", "keys")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    keys: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., keys: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ...) -> None: ...

class ASTForSystemTimeProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTMatchRecognizeClauseProto(_message.Message):
    __slots__ = ("parent", "partition_by", "order_by", "measures", "after_match_skip_clause", "pattern", "pattern_variable_definition_list", "output_alias", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    MEASURES_FIELD_NUMBER: _ClassVar[int]
    AFTER_MATCH_SKIP_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATTERN_VARIABLE_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ALIAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPostfixTableOperatorProto
    partition_by: ASTPartitionByProto
    order_by: ASTOrderByProto
    measures: ASTSelectListProto
    after_match_skip_clause: ASTAfterMatchSkipClauseProto
    pattern: AnyASTRowPatternExpressionProto
    pattern_variable_definition_list: ASTSelectListProto
    output_alias: ASTAliasProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTPostfixTableOperatorProto, _Mapping]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., measures: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., after_match_skip_clause: _Optional[_Union[ASTAfterMatchSkipClauseProto, _Mapping]] = ..., pattern: _Optional[_Union[AnyASTRowPatternExpressionProto, _Mapping]] = ..., pattern_variable_definition_list: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., output_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTAfterMatchSkipClauseProto(_message.Message):
    __slots__ = ("parent", "target_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    target_type: _ast_enums_pb2.ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., target_type: _Optional[_Union[_ast_enums_pb2.ASTAfterMatchSkipClauseEnums.AfterMatchSkipTargetType, str]] = ...) -> None: ...

class AnyASTRowPatternExpressionProto(_message.Message):
    __slots__ = ("ast_row_pattern_variable_node", "ast_row_pattern_operation_node", "ast_empty_row_pattern_node", "ast_row_pattern_quantification_node", "ast_row_pattern_anchor_node")
    AST_ROW_PATTERN_VARIABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROW_PATTERN_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_EMPTY_ROW_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROW_PATTERN_QUANTIFICATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ROW_PATTERN_ANCHOR_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_row_pattern_variable_node: ASTRowPatternVariableProto
    ast_row_pattern_operation_node: ASTRowPatternOperationProto
    ast_empty_row_pattern_node: ASTEmptyRowPatternProto
    ast_row_pattern_quantification_node: ASTRowPatternQuantificationProto
    ast_row_pattern_anchor_node: ASTRowPatternAnchorProto
    def __init__(self, ast_row_pattern_variable_node: _Optional[_Union[ASTRowPatternVariableProto, _Mapping]] = ..., ast_row_pattern_operation_node: _Optional[_Union[ASTRowPatternOperationProto, _Mapping]] = ..., ast_empty_row_pattern_node: _Optional[_Union[ASTEmptyRowPatternProto, _Mapping]] = ..., ast_row_pattern_quantification_node: _Optional[_Union[ASTRowPatternQuantificationProto, _Mapping]] = ..., ast_row_pattern_anchor_node: _Optional[_Union[ASTRowPatternAnchorProto, _Mapping]] = ...) -> None: ...

class ASTRowPatternExpressionProto(_message.Message):
    __slots__ = ("parent", "parenthesized")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parenthesized: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parenthesized: bool = ...) -> None: ...

class ASTRowPatternVariableProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTRowPatternExpressionProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTRowPatternExpressionProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTRowPatternOperationProto(_message.Message):
    __slots__ = ("parent", "op_type", "inputs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTRowPatternExpressionProto
    op_type: _ast_enums_pb2.ASTRowPatternOperationEnums.OperationType
    inputs: _containers.RepeatedCompositeFieldContainer[AnyASTRowPatternExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTRowPatternExpressionProto, _Mapping]] = ..., op_type: _Optional[_Union[_ast_enums_pb2.ASTRowPatternOperationEnums.OperationType, str]] = ..., inputs: _Optional[_Iterable[_Union[AnyASTRowPatternExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTEmptyRowPatternProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTRowPatternExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTRowPatternExpressionProto, _Mapping]] = ...) -> None: ...

class ASTRowPatternAnchorProto(_message.Message):
    __slots__ = ("parent", "anchor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTRowPatternExpressionProto
    anchor: _ast_enums_pb2.ASTRowPatternAnchorEnums.Anchor
    def __init__(self, parent: _Optional[_Union[ASTRowPatternExpressionProto, _Mapping]] = ..., anchor: _Optional[_Union[_ast_enums_pb2.ASTRowPatternAnchorEnums.Anchor, str]] = ...) -> None: ...

class AnyASTQuantifierProto(_message.Message):
    __slots__ = ("ast_bounded_quantifier_node", "ast_fixed_quantifier_node", "ast_symbol_quantifier_node")
    AST_BOUNDED_QUANTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FIXED_QUANTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SYMBOL_QUANTIFIER_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_bounded_quantifier_node: ASTBoundedQuantifierProto
    ast_fixed_quantifier_node: ASTFixedQuantifierProto
    ast_symbol_quantifier_node: ASTSymbolQuantifierProto
    def __init__(self, ast_bounded_quantifier_node: _Optional[_Union[ASTBoundedQuantifierProto, _Mapping]] = ..., ast_fixed_quantifier_node: _Optional[_Union[ASTFixedQuantifierProto, _Mapping]] = ..., ast_symbol_quantifier_node: _Optional[_Union[ASTSymbolQuantifierProto, _Mapping]] = ...) -> None: ...

class ASTQuantifierProto(_message.Message):
    __slots__ = ("parent", "is_reluctant")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_RELUCTANT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    is_reluctant: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., is_reluctant: bool = ...) -> None: ...

class ASTBoundedQuantifierProto(_message.Message):
    __slots__ = ("parent", "lower_bound", "upper_bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQuantifierProto
    lower_bound: ASTQuantifierBoundProto
    upper_bound: ASTQuantifierBoundProto
    def __init__(self, parent: _Optional[_Union[ASTQuantifierProto, _Mapping]] = ..., lower_bound: _Optional[_Union[ASTQuantifierBoundProto, _Mapping]] = ..., upper_bound: _Optional[_Union[ASTQuantifierBoundProto, _Mapping]] = ...) -> None: ...

class ASTQuantifierBoundProto(_message.Message):
    __slots__ = ("parent", "bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    bound: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., bound: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTFixedQuantifierProto(_message.Message):
    __slots__ = ("parent", "bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQuantifierProto
    bound: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTQuantifierProto, _Mapping]] = ..., bound: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTSymbolQuantifierProto(_message.Message):
    __slots__ = ("parent", "symbol")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQuantifierProto
    symbol: _ast_enums_pb2.ASTSymbolQuantifierEnums.Symbol
    def __init__(self, parent: _Optional[_Union[ASTQuantifierProto, _Mapping]] = ..., symbol: _Optional[_Union[_ast_enums_pb2.ASTSymbolQuantifierEnums.Symbol, str]] = ...) -> None: ...

class ASTRowPatternQuantificationProto(_message.Message):
    __slots__ = ("parent", "operand", "quantifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    QUANTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTRowPatternExpressionProto
    operand: AnyASTRowPatternExpressionProto
    quantifier: AnyASTQuantifierProto
    def __init__(self, parent: _Optional[_Union[ASTRowPatternExpressionProto, _Mapping]] = ..., operand: _Optional[_Union[AnyASTRowPatternExpressionProto, _Mapping]] = ..., quantifier: _Optional[_Union[AnyASTQuantifierProto, _Mapping]] = ...) -> None: ...

class ASTQualifyProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTClampedBetweenModifierProto(_message.Message):
    __slots__ = ("parent", "low", "high")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    low: AnyASTExpressionProto
    high: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., low: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., high: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTWithReportModifierProto(_message.Message):
    __slots__ = ("parent", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTFormatClauseProto(_message.Message):
    __slots__ = ("parent", "format", "time_zone_expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    format: AnyASTExpressionProto
    time_zone_expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., format: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., time_zone_expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTPathExpressionListProto(_message.Message):
    __slots__ = ("parent", "path_expression_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    path_expression_list: _containers.RepeatedCompositeFieldContainer[ASTPathExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., path_expression_list: _Optional[_Iterable[_Union[ASTPathExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTParameterExprProto(_message.Message):
    __slots__ = ("parent", "name", "position")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTParameterExprBaseProto
    name: ASTIdentifierProto
    position: int
    def __init__(self, parent: _Optional[_Union[ASTParameterExprBaseProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., position: _Optional[int] = ...) -> None: ...

class ASTSystemVariableExprProto(_message.Message):
    __slots__ = ("parent", "path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTParameterExprBaseProto
    path: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTParameterExprBaseProto, _Mapping]] = ..., path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTLambdaProto(_message.Message):
    __slots__ = ("parent", "argument_list", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    argument_list: AnyASTExpressionProto
    body: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., argument_list: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., body: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTAnalyticFunctionCallProto(_message.Message):
    __slots__ = ("parent", "function", "window_spec")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_SPEC_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    function: ASTFunctionCallProto
    window_spec: ASTWindowSpecificationProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., function: _Optional[_Union[ASTFunctionCallProto, _Mapping]] = ..., window_spec: _Optional[_Union[ASTWindowSpecificationProto, _Mapping]] = ...) -> None: ...

class ASTClusterByProto(_message.Message):
    __slots__ = ("parent", "clustering_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    clustering_expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., clustering_expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTNewConstructorArgProto(_message.Message):
    __slots__ = ("parent", "expression", "optional_identifier", "optional_path_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PATH_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    optional_identifier: ASTIdentifierProto
    optional_path_expression: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., optional_identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., optional_path_expression: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTNewConstructorProto(_message.Message):
    __slots__ = ("parent", "type_name", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    type_name: ASTSimpleTypeProto
    arguments: _containers.RepeatedCompositeFieldContainer[ASTNewConstructorArgProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., type_name: _Optional[_Union[ASTSimpleTypeProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[ASTNewConstructorArgProto, _Mapping]]] = ...) -> None: ...

class ASTBracedConstructorLhsProto(_message.Message):
    __slots__ = ("parent", "extended_path_expr", "operation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_PATH_EXPR_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    extended_path_expr: AnyASTGeneralizedPathExpressionProto
    operation: _ast_enums_pb2.ASTBracedConstructorLhsEnums.Operation
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., extended_path_expr: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., operation: _Optional[_Union[_ast_enums_pb2.ASTBracedConstructorLhsEnums.Operation, str]] = ...) -> None: ...

class ASTBracedConstructorFieldValueProto(_message.Message):
    __slots__ = ("parent", "expression", "colon_prefixed")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    COLON_PREFIXED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    colon_prefixed: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., colon_prefixed: bool = ...) -> None: ...

class ASTBracedConstructorFieldProto(_message.Message):
    __slots__ = ("parent", "value", "comma_separated", "braced_constructor_lhs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COMMA_SEPARATED_FIELD_NUMBER: _ClassVar[int]
    BRACED_CONSTRUCTOR_LHS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: ASTBracedConstructorFieldValueProto
    comma_separated: bool
    braced_constructor_lhs: ASTBracedConstructorLhsProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[ASTBracedConstructorFieldValueProto, _Mapping]] = ..., comma_separated: bool = ..., braced_constructor_lhs: _Optional[_Union[ASTBracedConstructorLhsProto, _Mapping]] = ...) -> None: ...

class ASTBracedConstructorProto(_message.Message):
    __slots__ = ("parent", "fields")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    fields: _containers.RepeatedCompositeFieldContainer[ASTBracedConstructorFieldProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[ASTBracedConstructorFieldProto, _Mapping]]] = ...) -> None: ...

class ASTBracedNewConstructorProto(_message.Message):
    __slots__ = ("parent", "type_name", "braced_constructor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    BRACED_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    type_name: ASTSimpleTypeProto
    braced_constructor: ASTBracedConstructorProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., type_name: _Optional[_Union[ASTSimpleTypeProto, _Mapping]] = ..., braced_constructor: _Optional[_Union[ASTBracedConstructorProto, _Mapping]] = ...) -> None: ...

class ASTExtendedPathExpressionProto(_message.Message):
    __slots__ = ("parent", "parenthesized_path", "generalized_path_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_PATH_FIELD_NUMBER: _ClassVar[int]
    GENERALIZED_PATH_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGeneralizedPathExpressionProto
    parenthesized_path: AnyASTGeneralizedPathExpressionProto
    generalized_path_expression: AnyASTGeneralizedPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTGeneralizedPathExpressionProto, _Mapping]] = ..., parenthesized_path: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., generalized_path_expression: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTUpdateConstructorProto(_message.Message):
    __slots__ = ("parent", "function", "braced_constructor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    BRACED_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    function: ASTFunctionCallProto
    braced_constructor: ASTBracedConstructorProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., function: _Optional[_Union[ASTFunctionCallProto, _Mapping]] = ..., braced_constructor: _Optional[_Union[ASTBracedConstructorProto, _Mapping]] = ...) -> None: ...

class ASTStructBracedConstructorProto(_message.Message):
    __slots__ = ("parent", "type_name", "braced_constructor")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    BRACED_CONSTRUCTOR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    type_name: AnyASTTypeProto
    braced_constructor: ASTBracedConstructorProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., type_name: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., braced_constructor: _Optional[_Union[ASTBracedConstructorProto, _Mapping]] = ...) -> None: ...

class ASTOptionsListProto(_message.Message):
    __slots__ = ("parent", "options_entries")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    options_entries: _containers.RepeatedCompositeFieldContainer[ASTOptionsEntryProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., options_entries: _Optional[_Iterable[_Union[ASTOptionsEntryProto, _Mapping]]] = ...) -> None: ...

class ASTOptionsEntryProto(_message.Message):
    __slots__ = ("parent", "name", "value", "assignment_op")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_OP_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    value: AnyASTExpressionProto
    assignment_op: _ast_enums_pb2.ASTOptionsEntryEnums.AssignmentOp
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., assignment_op: _Optional[_Union[_ast_enums_pb2.ASTOptionsEntryEnums.AssignmentOp, str]] = ...) -> None: ...

class AnyASTCreateStatementProto(_message.Message):
    __slots__ = ("ast_create_constant_statement_node", "ast_create_procedure_statement_node", "ast_create_model_statement_node", "ast_create_index_statement_node", "ast_create_snapshot_table_statement_node", "ast_create_entity_statement_node", "ast_create_row_access_policy_statement_node", "ast_create_table_stmt_base_node", "ast_create_view_statement_base_node", "ast_create_function_stmt_base_node", "ast_create_privilege_restriction_statement_node", "ast_create_property_graph_statement_node", "ast_create_snapshot_statement_node", "ast_create_schema_stmt_base_node", "ast_create_connection_statement_node", "ast_create_sequence_statement_node")
    AST_CREATE_CONSTANT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_PROCEDURE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_MODEL_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_INDEX_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_SNAPSHOT_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_ENTITY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_ROW_ACCESS_POLICY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_TABLE_STMT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_VIEW_STATEMENT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_FUNCTION_STMT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_PRIVILEGE_RESTRICTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_PROPERTY_GRAPH_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_SNAPSHOT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_SCHEMA_STMT_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_CONNECTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_SEQUENCE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_create_constant_statement_node: ASTCreateConstantStatementProto
    ast_create_procedure_statement_node: ASTCreateProcedureStatementProto
    ast_create_model_statement_node: ASTCreateModelStatementProto
    ast_create_index_statement_node: ASTCreateIndexStatementProto
    ast_create_snapshot_table_statement_node: ASTCreateSnapshotTableStatementProto
    ast_create_entity_statement_node: ASTCreateEntityStatementProto
    ast_create_row_access_policy_statement_node: ASTCreateRowAccessPolicyStatementProto
    ast_create_table_stmt_base_node: AnyASTCreateTableStmtBaseProto
    ast_create_view_statement_base_node: AnyASTCreateViewStatementBaseProto
    ast_create_function_stmt_base_node: AnyASTCreateFunctionStmtBaseProto
    ast_create_privilege_restriction_statement_node: ASTCreatePrivilegeRestrictionStatementProto
    ast_create_property_graph_statement_node: ASTCreatePropertyGraphStatementProto
    ast_create_snapshot_statement_node: ASTCreateSnapshotStatementProto
    ast_create_schema_stmt_base_node: AnyASTCreateSchemaStmtBaseProto
    ast_create_connection_statement_node: ASTCreateConnectionStatementProto
    ast_create_sequence_statement_node: ASTCreateSequenceStatementProto
    def __init__(self, ast_create_constant_statement_node: _Optional[_Union[ASTCreateConstantStatementProto, _Mapping]] = ..., ast_create_procedure_statement_node: _Optional[_Union[ASTCreateProcedureStatementProto, _Mapping]] = ..., ast_create_model_statement_node: _Optional[_Union[ASTCreateModelStatementProto, _Mapping]] = ..., ast_create_index_statement_node: _Optional[_Union[ASTCreateIndexStatementProto, _Mapping]] = ..., ast_create_snapshot_table_statement_node: _Optional[_Union[ASTCreateSnapshotTableStatementProto, _Mapping]] = ..., ast_create_entity_statement_node: _Optional[_Union[ASTCreateEntityStatementProto, _Mapping]] = ..., ast_create_row_access_policy_statement_node: _Optional[_Union[ASTCreateRowAccessPolicyStatementProto, _Mapping]] = ..., ast_create_table_stmt_base_node: _Optional[_Union[AnyASTCreateTableStmtBaseProto, _Mapping]] = ..., ast_create_view_statement_base_node: _Optional[_Union[AnyASTCreateViewStatementBaseProto, _Mapping]] = ..., ast_create_function_stmt_base_node: _Optional[_Union[AnyASTCreateFunctionStmtBaseProto, _Mapping]] = ..., ast_create_privilege_restriction_statement_node: _Optional[_Union[ASTCreatePrivilegeRestrictionStatementProto, _Mapping]] = ..., ast_create_property_graph_statement_node: _Optional[_Union[ASTCreatePropertyGraphStatementProto, _Mapping]] = ..., ast_create_snapshot_statement_node: _Optional[_Union[ASTCreateSnapshotStatementProto, _Mapping]] = ..., ast_create_schema_stmt_base_node: _Optional[_Union[AnyASTCreateSchemaStmtBaseProto, _Mapping]] = ..., ast_create_connection_statement_node: _Optional[_Union[ASTCreateConnectionStatementProto, _Mapping]] = ..., ast_create_sequence_statement_node: _Optional[_Union[ASTCreateSequenceStatementProto, _Mapping]] = ...) -> None: ...

class ASTCreateStatementProto(_message.Message):
    __slots__ = ("parent", "scope", "is_or_replace", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    IS_OR_REPLACE_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    scope: _ast_enums_pb2.ASTCreateStatementEnums.Scope
    is_or_replace: bool
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., scope: _Optional[_Union[_ast_enums_pb2.ASTCreateStatementEnums.Scope, str]] = ..., is_or_replace: bool = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTFunctionParameterProto(_message.Message):
    __slots__ = ("parent", "name", "type", "templated_parameter_type", "tvf_schema", "alias", "default_value", "procedure_parameter_mode", "is_not_aggregate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATED_PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TVF_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_PARAMETER_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    type: AnyASTTypeProto
    templated_parameter_type: ASTTemplatedParameterTypeProto
    tvf_schema: ASTTVFSchemaProto
    alias: ASTAliasProto
    default_value: AnyASTExpressionProto
    procedure_parameter_mode: _ast_enums_pb2.ASTFunctionParameterEnums.ProcedureParameterMode
    is_not_aggregate: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., templated_parameter_type: _Optional[_Union[ASTTemplatedParameterTypeProto, _Mapping]] = ..., tvf_schema: _Optional[_Union[ASTTVFSchemaProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., default_value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., procedure_parameter_mode: _Optional[_Union[_ast_enums_pb2.ASTFunctionParameterEnums.ProcedureParameterMode, str]] = ..., is_not_aggregate: bool = ...) -> None: ...

class ASTFunctionParametersProto(_message.Message):
    __slots__ = ("parent", "parameter_entries")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parameter_entries: _containers.RepeatedCompositeFieldContainer[ASTFunctionParameterProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parameter_entries: _Optional[_Iterable[_Union[ASTFunctionParameterProto, _Mapping]]] = ...) -> None: ...

class ASTFunctionDeclarationProto(_message.Message):
    __slots__ = ("parent", "name", "parameters")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTPathExpressionProto
    parameters: ASTFunctionParametersProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., parameters: _Optional[_Union[ASTFunctionParametersProto, _Mapping]] = ...) -> None: ...

class ASTSqlFunctionBodyProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTTVFArgumentProto(_message.Message):
    __slots__ = ("parent", "expr", "table_clause", "model_clause", "connection_clause", "desc")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    TABLE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    MODEL_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expr: AnyASTExpressionProto
    table_clause: ASTTableClauseProto
    model_clause: ASTModelClauseProto
    connection_clause: ASTConnectionClauseProto
    desc: ASTDescriptorProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., table_clause: _Optional[_Union[ASTTableClauseProto, _Mapping]] = ..., model_clause: _Optional[_Union[ASTModelClauseProto, _Mapping]] = ..., connection_clause: _Optional[_Union[ASTConnectionClauseProto, _Mapping]] = ..., desc: _Optional[_Union[ASTDescriptorProto, _Mapping]] = ...) -> None: ...

class ASTTVFProto(_message.Message):
    __slots__ = ("parent", "name", "argument_entries", "hint", "alias", "is_lateral")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    IS_LATERAL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    name: ASTPathExpressionProto
    argument_entries: _containers.RepeatedCompositeFieldContainer[ASTTVFArgumentProto]
    hint: ASTHintProto
    alias: ASTAliasProto
    is_lateral: bool
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., argument_entries: _Optional[_Iterable[_Union[ASTTVFArgumentProto, _Mapping]]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., is_lateral: bool = ...) -> None: ...

class ASTTableClauseProto(_message.Message):
    __slots__ = ("parent", "table_path", "tvf", "where_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    TVF_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    table_path: ASTPathExpressionProto
    tvf: ASTTVFProto
    where_clause: ASTWhereClauseProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., table_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., tvf: _Optional[_Union[ASTTVFProto, _Mapping]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ...) -> None: ...

class ASTModelClauseProto(_message.Message):
    __slots__ = ("parent", "model_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    model_path: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., model_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTConnectionClauseProto(_message.Message):
    __slots__ = ("parent", "connection_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    connection_path: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., connection_path: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTTableDataSourceProto(_message.Message):
    __slots__ = ("ast_clone_data_source_node", "ast_copy_data_source_node")
    AST_CLONE_DATA_SOURCE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_COPY_DATA_SOURCE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_clone_data_source_node: ASTCloneDataSourceProto
    ast_copy_data_source_node: ASTCopyDataSourceProto
    def __init__(self, ast_clone_data_source_node: _Optional[_Union[ASTCloneDataSourceProto, _Mapping]] = ..., ast_copy_data_source_node: _Optional[_Union[ASTCopyDataSourceProto, _Mapping]] = ...) -> None: ...

class ASTTableDataSourceProto(_message.Message):
    __slots__ = ("parent", "path_expr", "for_system_time", "where_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_EXPR_FIELD_NUMBER: _ClassVar[int]
    FOR_SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    path_expr: ASTPathExpressionProto
    for_system_time: ASTForSystemTimeProto
    where_clause: ASTWhereClauseProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., path_expr: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., for_system_time: _Optional[_Union[ASTForSystemTimeProto, _Mapping]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ...) -> None: ...

class ASTCloneDataSourceProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableDataSourceProto
    def __init__(self, parent: _Optional[_Union[ASTTableDataSourceProto, _Mapping]] = ...) -> None: ...

class ASTCopyDataSourceProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableDataSourceProto
    def __init__(self, parent: _Optional[_Union[ASTTableDataSourceProto, _Mapping]] = ...) -> None: ...

class ASTCloneDataSourceListProto(_message.Message):
    __slots__ = ("parent", "data_sources")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    data_sources: _containers.RepeatedCompositeFieldContainer[ASTCloneDataSourceProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., data_sources: _Optional[_Iterable[_Union[ASTCloneDataSourceProto, _Mapping]]] = ...) -> None: ...

class ASTCloneDataStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "data_source_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: ASTPathExpressionProto
    data_source_list: ASTCloneDataSourceListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., data_source_list: _Optional[_Union[ASTCloneDataSourceListProto, _Mapping]] = ...) -> None: ...

class ASTCreateConnectionStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCreateConstantStatementProto(_message.Message):
    __slots__ = ("parent", "name", "expr")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    expr: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTCreateDatabaseStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCreateProcedureStatementProto(_message.Message):
    __slots__ = ("parent", "name", "parameters", "options_list", "body", "with_connection_clause", "language", "code", "external_security")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    parameters: ASTFunctionParametersProto
    options_list: ASTOptionsListProto
    body: ASTScriptProto
    with_connection_clause: ASTWithConnectionClauseProto
    language: ASTIdentifierProto
    code: ASTStringLiteralProto
    external_security: _ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., parameters: _Optional[_Union[ASTFunctionParametersProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., body: _Optional[_Union[ASTScriptProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., language: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., code: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., external_security: _Optional[_Union[_ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity, str]] = ...) -> None: ...

class AnyASTCreateSchemaStmtBaseProto(_message.Message):
    __slots__ = ("ast_create_schema_statement_node", "ast_create_external_schema_statement_node")
    AST_CREATE_SCHEMA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_EXTERNAL_SCHEMA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_create_schema_statement_node: ASTCreateSchemaStatementProto
    ast_create_external_schema_statement_node: ASTCreateExternalSchemaStatementProto
    def __init__(self, ast_create_schema_statement_node: _Optional[_Union[ASTCreateSchemaStatementProto, _Mapping]] = ..., ast_create_external_schema_statement_node: _Optional[_Union[ASTCreateExternalSchemaStatementProto, _Mapping]] = ...) -> None: ...

class ASTCreateSchemaStmtBaseProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCreateSchemaStatementProto(_message.Message):
    __slots__ = ("parent", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateSchemaStmtBaseProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTCreateSchemaStmtBaseProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTCreateExternalSchemaStatementProto(_message.Message):
    __slots__ = ("parent", "with_connection_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateSchemaStmtBaseProto
    with_connection_clause: ASTWithConnectionClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateSchemaStmtBaseProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ...) -> None: ...

class ASTAliasedQueryListProto(_message.Message):
    __slots__ = ("parent", "aliased_query_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIASED_QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    aliased_query_list: _containers.RepeatedCompositeFieldContainer[ASTAliasedQueryProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., aliased_query_list: _Optional[_Iterable[_Union[ASTAliasedQueryProto, _Mapping]]] = ...) -> None: ...

class ASTTransformClauseProto(_message.Message):
    __slots__ = ("parent", "select_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    select_list: ASTSelectListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., select_list: _Optional[_Union[ASTSelectListProto, _Mapping]] = ...) -> None: ...

class ASTCreateModelStatementProto(_message.Message):
    __slots__ = ("parent", "name", "transform_clause", "options_list", "query", "input_output_clause", "is_remote", "with_connection_clause", "aliased_query_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INPUT_OUTPUT_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    IS_REMOTE_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ALIASED_QUERY_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    transform_clause: ASTTransformClauseProto
    options_list: ASTOptionsListProto
    query: ASTQueryProto
    input_output_clause: ASTInputOutputClauseProto
    is_remote: bool
    with_connection_clause: ASTWithConnectionClauseProto
    aliased_query_list: ASTAliasedQueryListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., transform_clause: _Optional[_Union[ASTTransformClauseProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., input_output_clause: _Optional[_Union[ASTInputOutputClauseProto, _Mapping]] = ..., is_remote: bool = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., aliased_query_list: _Optional[_Union[ASTAliasedQueryListProto, _Mapping]] = ...) -> None: ...

class ASTIndexAllColumnsProto(_message.Message):
    __slots__ = ("parent", "column_options")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    column_options: ASTIndexItemListProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ..., column_options: _Optional[_Union[ASTIndexItemListProto, _Mapping]] = ...) -> None: ...

class ASTIndexItemListProto(_message.Message):
    __slots__ = ("parent", "ordering_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDERING_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    ordering_expressions: _containers.RepeatedCompositeFieldContainer[ASTOrderingExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., ordering_expressions: _Optional[_Iterable[_Union[ASTOrderingExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTIndexStoringExpressionListProto(_message.Message):
    __slots__ = ("parent", "expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expressions: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expressions: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTIndexUnnestExpressionListProto(_message.Message):
    __slots__ = ("parent", "unnest_expressions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNNEST_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    unnest_expressions: _containers.RepeatedCompositeFieldContainer[ASTUnnestExpressionWithOptAliasAndOffsetProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., unnest_expressions: _Optional[_Iterable[_Union[ASTUnnestExpressionWithOptAliasAndOffsetProto, _Mapping]]] = ...) -> None: ...

class ASTCreateIndexStatementProto(_message.Message):
    __slots__ = ("parent", "name", "table_name", "optional_table_alias", "optional_index_unnest_expression_list", "index_item_list", "optional_index_storing_expressions", "optional_partition_by", "options_list", "is_unique", "is_search", "spanner_interleave_clause", "spanner_is_null_filtered", "is_vector")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_TABLE_ALIAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INDEX_UNNEST_EXPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    INDEX_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INDEX_STORING_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    IS_SEARCH_FIELD_NUMBER: _ClassVar[int]
    SPANNER_INTERLEAVE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    SPANNER_IS_NULL_FILTERED_FIELD_NUMBER: _ClassVar[int]
    IS_VECTOR_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    table_name: ASTPathExpressionProto
    optional_table_alias: ASTAliasProto
    optional_index_unnest_expression_list: ASTIndexUnnestExpressionListProto
    index_item_list: ASTIndexItemListProto
    optional_index_storing_expressions: ASTIndexStoringExpressionListProto
    optional_partition_by: ASTPartitionByProto
    options_list: ASTOptionsListProto
    is_unique: bool
    is_search: bool
    spanner_interleave_clause: ASTSpannerInterleaveClauseProto
    spanner_is_null_filtered: bool
    is_vector: bool
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., optional_table_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., optional_index_unnest_expression_list: _Optional[_Union[ASTIndexUnnestExpressionListProto, _Mapping]] = ..., index_item_list: _Optional[_Union[ASTIndexItemListProto, _Mapping]] = ..., optional_index_storing_expressions: _Optional[_Union[ASTIndexStoringExpressionListProto, _Mapping]] = ..., optional_partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., is_unique: bool = ..., is_search: bool = ..., spanner_interleave_clause: _Optional[_Union[ASTSpannerInterleaveClauseProto, _Mapping]] = ..., spanner_is_null_filtered: bool = ..., is_vector: bool = ...) -> None: ...

class ASTExportDataStatementProto(_message.Message):
    __slots__ = ("parent", "with_connection_clause", "options_list", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    with_connection_clause: ASTWithConnectionClauseProto
    options_list: ASTOptionsListProto
    query: ASTQueryProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ...) -> None: ...

class ASTExportModelStatementProto(_message.Message):
    __slots__ = ("parent", "model_name_path", "with_connection_clause", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    model_name_path: ASTPathExpressionProto
    with_connection_clause: ASTWithConnectionClauseProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., model_name_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTExportMetadataStatementProto(_message.Message):
    __slots__ = ("parent", "schema_object_kind", "name_path", "with_connection_clause", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    schema_object_kind: _ast_enums_pb2.SchemaObjectKind
    name_path: ASTPathExpressionProto
    with_connection_clause: ASTWithConnectionClauseProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., schema_object_kind: _Optional[_Union[_ast_enums_pb2.SchemaObjectKind, str]] = ..., name_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCallStatementProto(_message.Message):
    __slots__ = ("parent", "procedure_name", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROCEDURE_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    procedure_name: ASTPathExpressionProto
    arguments: _containers.RepeatedCompositeFieldContainer[ASTTVFArgumentProto]
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., procedure_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[ASTTVFArgumentProto, _Mapping]]] = ...) -> None: ...

class ASTDefineTableStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCreateLocalityGroupStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTWithPartitionColumnsClauseProto(_message.Message):
    __slots__ = ("parent", "table_element_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_element_list: ASTTableElementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_element_list: _Optional[_Union[ASTTableElementListProto, _Mapping]] = ...) -> None: ...

class ASTCreateSnapshotStatementProto(_message.Message):
    __slots__ = ("parent", "schema_object_kind", "name", "clone_data_source", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    schema_object_kind: _ast_enums_pb2.SchemaObjectKind
    name: ASTPathExpressionProto
    clone_data_source: ASTCloneDataSourceProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., schema_object_kind: _Optional[_Union[_ast_enums_pb2.SchemaObjectKind, str]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., clone_data_source: _Optional[_Union[ASTCloneDataSourceProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTCreateSnapshotTableStatementProto(_message.Message):
    __slots__ = ("parent", "name", "clone_data_source", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    clone_data_source: ASTCloneDataSourceProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., clone_data_source: _Optional[_Union[ASTCloneDataSourceProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTTypeParameterListProto(_message.Message):
    __slots__ = ("parent", "parameters")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parameters: _containers.RepeatedCompositeFieldContainer[AnyASTLeafProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[AnyASTLeafProto, _Mapping]]] = ...) -> None: ...

class ASTTVFSchemaProto(_message.Message):
    __slots__ = ("parent", "columns")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    columns: _containers.RepeatedCompositeFieldContainer[ASTTVFSchemaColumnProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., columns: _Optional[_Iterable[_Union[ASTTVFSchemaColumnProto, _Mapping]]] = ...) -> None: ...

class ASTTVFSchemaColumnProto(_message.Message):
    __slots__ = ("parent", "name", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    type: AnyASTTypeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ...) -> None: ...

class ASTTableAndColumnInfoProto(_message.Message):
    __slots__ = ("parent", "table_name", "column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_name: ASTPathExpressionProto
    column_list: ASTColumnListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ...) -> None: ...

class ASTTableAndColumnInfoListProto(_message.Message):
    __slots__ = ("parent", "table_and_column_info_entries")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_AND_COLUMN_INFO_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_and_column_info_entries: _containers.RepeatedCompositeFieldContainer[ASTTableAndColumnInfoProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_and_column_info_entries: _Optional[_Iterable[_Union[ASTTableAndColumnInfoProto, _Mapping]]] = ...) -> None: ...

class ASTTemplatedParameterTypeProto(_message.Message):
    __slots__ = ("parent", "kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    kind: _ast_enums_pb2.ASTTemplatedParameterTypeEnums.TemplatedTypeKind
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., kind: _Optional[_Union[_ast_enums_pb2.ASTTemplatedParameterTypeEnums.TemplatedTypeKind, str]] = ...) -> None: ...

class ASTDefaultLiteralProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTAnalyzeStatementProto(_message.Message):
    __slots__ = ("parent", "options_list", "table_and_column_info_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    TABLE_AND_COLUMN_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    options_list: ASTOptionsListProto
    table_and_column_info_list: ASTTableAndColumnInfoListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., table_and_column_info_list: _Optional[_Union[ASTTableAndColumnInfoListProto, _Mapping]] = ...) -> None: ...

class ASTAssertStatementProto(_message.Message):
    __slots__ = ("parent", "expr", "description")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    expr: AnyASTExpressionProto
    description: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., description: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTAssertRowsModifiedProto(_message.Message):
    __slots__ = ("parent", "num_rows")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    num_rows: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., num_rows: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTReturningClauseProto(_message.Message):
    __slots__ = ("parent", "select_list", "action_alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTION_ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    select_list: ASTSelectListProto
    action_alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., select_list: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., action_alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTOnConflictClauseProto(_message.Message):
    __slots__ = ("parent", "conflict_action", "conflict_target", "unique_constraint_name", "update_item_list", "update_where_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_TARGET_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    conflict_action: _ast_enums_pb2.ASTOnConflictClauseEnums.ConflictAction
    conflict_target: ASTColumnListProto
    unique_constraint_name: ASTIdentifierProto
    update_item_list: ASTUpdateItemListProto
    update_where_clause: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., conflict_action: _Optional[_Union[_ast_enums_pb2.ASTOnConflictClauseEnums.ConflictAction, str]] = ..., conflict_target: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., unique_constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., update_item_list: _Optional[_Union[ASTUpdateItemListProto, _Mapping]] = ..., update_where_clause: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTDeleteStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "alias", "offset", "where", "assert_rows_modified", "returning", "hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: AnyASTGeneralizedPathExpressionProto
    alias: ASTAliasProto
    offset: ASTWithOffsetProto
    where: AnyASTExpressionProto
    assert_rows_modified: ASTAssertRowsModifiedProto
    returning: ASTReturningClauseProto
    hint: ASTHintProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., offset: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ..., where: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., assert_rows_modified: _Optional[_Union[ASTAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ASTReturningClauseProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ...) -> None: ...

class AnyASTColumnAttributeProto(_message.Message):
    __slots__ = ("ast_not_null_column_attribute_node", "ast_hidden_column_attribute_node", "ast_primary_key_column_attribute_node", "ast_foreign_key_column_attribute_node")
    AST_NOT_NULL_COLUMN_ATTRIBUTE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_HIDDEN_COLUMN_ATTRIBUTE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_PRIMARY_KEY_COLUMN_ATTRIBUTE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOREIGN_KEY_COLUMN_ATTRIBUTE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_not_null_column_attribute_node: ASTNotNullColumnAttributeProto
    ast_hidden_column_attribute_node: ASTHiddenColumnAttributeProto
    ast_primary_key_column_attribute_node: ASTPrimaryKeyColumnAttributeProto
    ast_foreign_key_column_attribute_node: ASTForeignKeyColumnAttributeProto
    def __init__(self, ast_not_null_column_attribute_node: _Optional[_Union[ASTNotNullColumnAttributeProto, _Mapping]] = ..., ast_hidden_column_attribute_node: _Optional[_Union[ASTHiddenColumnAttributeProto, _Mapping]] = ..., ast_primary_key_column_attribute_node: _Optional[_Union[ASTPrimaryKeyColumnAttributeProto, _Mapping]] = ..., ast_foreign_key_column_attribute_node: _Optional[_Union[ASTForeignKeyColumnAttributeProto, _Mapping]] = ...) -> None: ...

class ASTColumnAttributeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTNotNullColumnAttributeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnAttributeProto
    def __init__(self, parent: _Optional[_Union[ASTColumnAttributeProto, _Mapping]] = ...) -> None: ...

class ASTHiddenColumnAttributeProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnAttributeProto
    def __init__(self, parent: _Optional[_Union[ASTColumnAttributeProto, _Mapping]] = ...) -> None: ...

class ASTPrimaryKeyColumnAttributeProto(_message.Message):
    __slots__ = ("parent", "enforced")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnAttributeProto
    enforced: bool
    def __init__(self, parent: _Optional[_Union[ASTColumnAttributeProto, _Mapping]] = ..., enforced: bool = ...) -> None: ...

class ASTForeignKeyColumnAttributeProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "reference")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnAttributeProto
    constraint_name: ASTIdentifierProto
    reference: ASTForeignKeyReferenceProto
    def __init__(self, parent: _Optional[_Union[ASTColumnAttributeProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., reference: _Optional[_Union[ASTForeignKeyReferenceProto, _Mapping]] = ...) -> None: ...

class ASTColumnAttributeListProto(_message.Message):
    __slots__ = ("parent", "values")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    values: _containers.RepeatedCompositeFieldContainer[AnyASTColumnAttributeProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., values: _Optional[_Iterable[_Union[AnyASTColumnAttributeProto, _Mapping]]] = ...) -> None: ...

class ASTStructColumnFieldProto(_message.Message):
    __slots__ = ("parent", "name", "schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    schema: AnyASTColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., schema: _Optional[_Union[AnyASTColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTGeneratedColumnInfoProto(_message.Message):
    __slots__ = ("parent", "expression", "stored_mode", "generated_mode", "identity_column_info")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    STORED_MODE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_MODE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    stored_mode: _ast_enums_pb2.ASTGeneratedColumnInfoEnums.StoredMode
    generated_mode: _ast_enums_pb2.ASTGeneratedColumnInfoEnums.GeneratedMode
    identity_column_info: ASTIdentityColumnInfoProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., stored_mode: _Optional[_Union[_ast_enums_pb2.ASTGeneratedColumnInfoEnums.StoredMode, str]] = ..., generated_mode: _Optional[_Union[_ast_enums_pb2.ASTGeneratedColumnInfoEnums.GeneratedMode, str]] = ..., identity_column_info: _Optional[_Union[ASTIdentityColumnInfoProto, _Mapping]] = ...) -> None: ...

class AnyASTTableElementProto(_message.Message):
    __slots__ = ("ast_column_definition_node", "ast_table_constraint_node")
    AST_COLUMN_DEFINITION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_TABLE_CONSTRAINT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_column_definition_node: ASTColumnDefinitionProto
    ast_table_constraint_node: AnyASTTableConstraintProto
    def __init__(self, ast_column_definition_node: _Optional[_Union[ASTColumnDefinitionProto, _Mapping]] = ..., ast_table_constraint_node: _Optional[_Union[AnyASTTableConstraintProto, _Mapping]] = ...) -> None: ...

class ASTTableElementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTColumnDefinitionProto(_message.Message):
    __slots__ = ("parent", "name", "schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableElementProto
    name: ASTIdentifierProto
    schema: AnyASTColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTTableElementProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., schema: _Optional[_Union[AnyASTColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTTableElementListProto(_message.Message):
    __slots__ = ("parent", "elements")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    elements: _containers.RepeatedCompositeFieldContainer[AnyASTTableElementProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[AnyASTTableElementProto, _Mapping]]] = ...) -> None: ...

class ASTColumnListProto(_message.Message):
    __slots__ = ("parent", "identifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifiers: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifiers: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ...) -> None: ...

class ASTColumnPositionProto(_message.Message):
    __slots__ = ("parent", "identifier", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier: ASTIdentifierProto
    type: _ast_enums_pb2.ASTColumnPositionEnums.RelativePositionType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., type: _Optional[_Union[_ast_enums_pb2.ASTColumnPositionEnums.RelativePositionType, str]] = ...) -> None: ...

class ASTInsertValuesRowProto(_message.Message):
    __slots__ = ("parent", "values")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    values: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., values: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTInsertValuesRowListProto(_message.Message):
    __slots__ = ("parent", "rows")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    rows: _containers.RepeatedCompositeFieldContainer[ASTInsertValuesRowProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[ASTInsertValuesRowProto, _Mapping]]] = ...) -> None: ...

class ASTInsertStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "column_list", "rows", "query", "assert_rows_modified", "returning", "deprecated_parse_progress", "insert_mode", "hint", "on_conflict")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PARSE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    INSERT_MODE_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: AnyASTGeneralizedPathExpressionProto
    column_list: ASTColumnListProto
    rows: ASTInsertValuesRowListProto
    query: ASTQueryProto
    assert_rows_modified: ASTAssertRowsModifiedProto
    returning: ASTReturningClauseProto
    deprecated_parse_progress: int
    insert_mode: _ast_enums_pb2.ASTInsertStatementEnums.InsertMode
    hint: ASTHintProto
    on_conflict: ASTOnConflictClauseProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., rows: _Optional[_Union[ASTInsertValuesRowListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., assert_rows_modified: _Optional[_Union[ASTAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ASTReturningClauseProto, _Mapping]] = ..., deprecated_parse_progress: _Optional[int] = ..., insert_mode: _Optional[_Union[_ast_enums_pb2.ASTInsertStatementEnums.InsertMode, str]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., on_conflict: _Optional[_Union[ASTOnConflictClauseProto, _Mapping]] = ...) -> None: ...

class ASTUpdateSetValueProto(_message.Message):
    __slots__ = ("parent", "path", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    path: AnyASTGeneralizedPathExpressionProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., path: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTUpdateItemProto(_message.Message):
    __slots__ = ("parent", "set_value", "insert_statement", "delete_statement", "update_statement")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SET_VALUE_FIELD_NUMBER: _ClassVar[int]
    INSERT_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    DELETE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    set_value: ASTUpdateSetValueProto
    insert_statement: ASTInsertStatementProto
    delete_statement: ASTDeleteStatementProto
    update_statement: ASTUpdateStatementProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., set_value: _Optional[_Union[ASTUpdateSetValueProto, _Mapping]] = ..., insert_statement: _Optional[_Union[ASTInsertStatementProto, _Mapping]] = ..., delete_statement: _Optional[_Union[ASTDeleteStatementProto, _Mapping]] = ..., update_statement: _Optional[_Union[ASTUpdateStatementProto, _Mapping]] = ...) -> None: ...

class ASTUpdateItemListProto(_message.Message):
    __slots__ = ("parent", "update_items")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    update_items: _containers.RepeatedCompositeFieldContainer[ASTUpdateItemProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., update_items: _Optional[_Iterable[_Union[ASTUpdateItemProto, _Mapping]]] = ...) -> None: ...

class ASTUpdateStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "alias", "offset", "update_item_list", "from_clause", "where", "assert_rows_modified", "returning", "hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    FROM_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    ASSERT_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: AnyASTGeneralizedPathExpressionProto
    alias: ASTAliasProto
    offset: ASTWithOffsetProto
    update_item_list: ASTUpdateItemListProto
    from_clause: ASTFromClauseProto
    where: AnyASTExpressionProto
    assert_rows_modified: ASTAssertRowsModifiedProto
    returning: ASTReturningClauseProto
    hint: ASTHintProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., offset: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ..., update_item_list: _Optional[_Union[ASTUpdateItemListProto, _Mapping]] = ..., from_clause: _Optional[_Union[ASTFromClauseProto, _Mapping]] = ..., where: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., assert_rows_modified: _Optional[_Union[ASTAssertRowsModifiedProto, _Mapping]] = ..., returning: _Optional[_Union[ASTReturningClauseProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ...) -> None: ...

class ASTTruncateStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "where")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: ASTPathExpressionProto
    where: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., where: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTMergeActionProto(_message.Message):
    __slots__ = ("parent", "insert_column_list", "insert_row", "update_item_list", "action_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSERT_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    INSERT_ROW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    insert_column_list: ASTColumnListProto
    insert_row: ASTInsertValuesRowProto
    update_item_list: ASTUpdateItemListProto
    action_type: _ast_enums_pb2.ASTMergeActionEnums.ActionType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., insert_column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., insert_row: _Optional[_Union[ASTInsertValuesRowProto, _Mapping]] = ..., update_item_list: _Optional[_Union[ASTUpdateItemListProto, _Mapping]] = ..., action_type: _Optional[_Union[_ast_enums_pb2.ASTMergeActionEnums.ActionType, str]] = ...) -> None: ...

class ASTMergeWhenClauseProto(_message.Message):
    __slots__ = ("parent", "search_condition", "action", "match_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    search_condition: AnyASTExpressionProto
    action: ASTMergeActionProto
    match_type: _ast_enums_pb2.ASTMergeWhenClauseEnums.MatchType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., search_condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., action: _Optional[_Union[ASTMergeActionProto, _Mapping]] = ..., match_type: _Optional[_Union[_ast_enums_pb2.ASTMergeWhenClauseEnums.MatchType, str]] = ...) -> None: ...

class ASTMergeWhenClauseListProto(_message.Message):
    __slots__ = ("parent", "clause_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLAUSE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    clause_list: _containers.RepeatedCompositeFieldContainer[ASTMergeWhenClauseProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., clause_list: _Optional[_Iterable[_Union[ASTMergeWhenClauseProto, _Mapping]]] = ...) -> None: ...

class ASTMergeStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "alias", "table_expression", "merge_condition", "when_clauses")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    TABLE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    MERGE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    WHEN_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path: ASTPathExpressionProto
    alias: ASTAliasProto
    table_expression: AnyASTTableExpressionProto
    merge_condition: AnyASTExpressionProto
    when_clauses: ASTMergeWhenClauseListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., table_expression: _Optional[_Union[AnyASTTableExpressionProto, _Mapping]] = ..., merge_condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., when_clauses: _Optional[_Union[ASTMergeWhenClauseListProto, _Mapping]] = ...) -> None: ...

class ASTPrivilegeProto(_message.Message):
    __slots__ = ("parent", "privilege_action", "paths")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    privilege_action: ASTIdentifierProto
    paths: ASTPathExpressionListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., privilege_action: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., paths: _Optional[_Union[ASTPathExpressionListProto, _Mapping]] = ...) -> None: ...

class ASTPrivilegesProto(_message.Message):
    __slots__ = ("parent", "privileges")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    privileges: _containers.RepeatedCompositeFieldContainer[ASTPrivilegeProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., privileges: _Optional[_Iterable[_Union[ASTPrivilegeProto, _Mapping]]] = ...) -> None: ...

class ASTGranteeListProto(_message.Message):
    __slots__ = ("parent", "grantee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    grantee_list: _containers.RepeatedCompositeFieldContainer[AnyASTExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., grantee_list: _Optional[_Iterable[_Union[AnyASTExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTGrantStatementProto(_message.Message):
    __slots__ = ("parent", "privileges", "target_type_parts", "target_path", "grantee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_PARTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    privileges: ASTPrivilegesProto
    target_type_parts: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    target_path: ASTPathExpressionProto
    grantee_list: ASTGranteeListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., privileges: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., target_type_parts: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., grantee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ...) -> None: ...

class ASTRevokeStatementProto(_message.Message):
    __slots__ = ("parent", "privileges", "target_type_parts", "target_path", "grantee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_PARTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    privileges: ASTPrivilegesProto
    target_type_parts: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    target_path: ASTPathExpressionProto
    grantee_list: ASTGranteeListProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., privileges: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., target_type_parts: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., grantee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ...) -> None: ...

class ASTRepeatableClauseProto(_message.Message):
    __slots__ = ("parent", "argument")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    argument: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., argument: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTFilterFieldsArgProto(_message.Message):
    __slots__ = ("parent", "path_expression", "filter_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    path_expression: AnyASTGeneralizedPathExpressionProto
    filter_type: _ast_enums_pb2.ASTFilterFieldsArgEnums.FilterType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., path_expression: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ..., filter_type: _Optional[_Union[_ast_enums_pb2.ASTFilterFieldsArgEnums.FilterType, str]] = ...) -> None: ...

class ASTReplaceFieldsArgProto(_message.Message):
    __slots__ = ("parent", "expression", "path_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    PATH_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    path_expression: AnyASTGeneralizedPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., path_expression: _Optional[_Union[AnyASTGeneralizedPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTReplaceFieldsExpressionProto(_message.Message):
    __slots__ = ("parent", "expr", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    expr: AnyASTExpressionProto
    arguments: _containers.RepeatedCompositeFieldContainer[ASTReplaceFieldsArgProto]
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., expr: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[ASTReplaceFieldsArgProto, _Mapping]]] = ...) -> None: ...

class ASTSampleSizeProto(_message.Message):
    __slots__ = ("parent", "size", "partition_by", "unit")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    size: AnyASTExpressionProto
    partition_by: ASTPartitionByProto
    unit: _ast_enums_pb2.ASTSampleSizeEnums.Unit
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., size: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., unit: _Optional[_Union[_ast_enums_pb2.ASTSampleSizeEnums.Unit, str]] = ...) -> None: ...

class ASTWithWeightProto(_message.Message):
    __slots__ = ("parent", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTSampleSuffixProto(_message.Message):
    __slots__ = ("parent", "weight", "repeat")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    weight: ASTWithWeightProto
    repeat: ASTRepeatableClauseProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., weight: _Optional[_Union[ASTWithWeightProto, _Mapping]] = ..., repeat: _Optional[_Union[ASTRepeatableClauseProto, _Mapping]] = ...) -> None: ...

class ASTSampleClauseProto(_message.Message):
    __slots__ = ("parent", "sample_method", "sample_size", "sample_suffix")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_METHOD_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPostfixTableOperatorProto
    sample_method: ASTIdentifierProto
    sample_size: ASTSampleSizeProto
    sample_suffix: ASTSampleSuffixProto
    def __init__(self, parent: _Optional[_Union[ASTPostfixTableOperatorProto, _Mapping]] = ..., sample_method: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., sample_size: _Optional[_Union[ASTSampleSizeProto, _Mapping]] = ..., sample_suffix: _Optional[_Union[ASTSampleSuffixProto, _Mapping]] = ...) -> None: ...

class AnyASTAlterActionProto(_message.Message):
    __slots__ = ("ast_set_options_action_node", "ast_set_as_action_node", "ast_add_constraint_action_node", "ast_drop_primary_key_action_node", "ast_drop_constraint_action_node", "ast_alter_constraint_enforcement_action_node", "ast_alter_constraint_set_options_action_node", "ast_add_column_action_node", "ast_drop_column_action_node", "ast_rename_column_action_node", "ast_alter_column_type_action_node", "ast_alter_column_options_action_node", "ast_alter_column_drop_not_null_action_node", "ast_grant_to_clause_node", "ast_filter_using_clause_node", "ast_revoke_from_clause_node", "ast_rename_to_clause_node", "ast_set_collate_clause_node", "ast_alter_column_set_default_action_node", "ast_alter_column_drop_default_action_node", "ast_restrict_to_clause_node", "ast_add_to_restrictee_list_clause_node", "ast_remove_from_restrictee_list_clause_node", "ast_alter_sub_entity_action_node", "ast_add_sub_entity_action_node", "ast_drop_sub_entity_action_node", "ast_add_ttl_action_node", "ast_replace_ttl_action_node", "ast_drop_ttl_action_node", "ast_spanner_alter_column_action_node", "ast_spanner_set_on_delete_action_node", "ast_alter_column_drop_generated_action_node", "ast_add_column_identifier_action_node", "ast_rebuild_action_node", "ast_alter_column_set_generated_action_node")
    AST_SET_OPTIONS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_AS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_CONSTRAINT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_PRIMARY_KEY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_CONSTRAINT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_CONSTRAINT_ENFORCEMENT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_CONSTRAINT_SET_OPTIONS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RENAME_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_TYPE_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_OPTIONS_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_DROP_NOT_NULL_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRANT_TO_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FILTER_USING_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REVOKE_FROM_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RENAME_TO_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SET_COLLATE_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_SET_DEFAULT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_DROP_DEFAULT_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RESTRICT_TO_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_TO_RESTRICTEE_LIST_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REMOVE_FROM_RESTRICTEE_LIST_CLAUSE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_SUB_ENTITY_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_TTL_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REPLACE_TTL_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_DROP_TTL_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SPANNER_ALTER_COLUMN_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_SPANNER_SET_ON_DELETE_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_DROP_GENERATED_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ADD_COLUMN_IDENTIFIER_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REBUILD_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_COLUMN_SET_GENERATED_ACTION_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_set_options_action_node: ASTSetOptionsActionProto
    ast_set_as_action_node: ASTSetAsActionProto
    ast_add_constraint_action_node: ASTAddConstraintActionProto
    ast_drop_primary_key_action_node: ASTDropPrimaryKeyActionProto
    ast_drop_constraint_action_node: ASTDropConstraintActionProto
    ast_alter_constraint_enforcement_action_node: ASTAlterConstraintEnforcementActionProto
    ast_alter_constraint_set_options_action_node: ASTAlterConstraintSetOptionsActionProto
    ast_add_column_action_node: ASTAddColumnActionProto
    ast_drop_column_action_node: ASTDropColumnActionProto
    ast_rename_column_action_node: ASTRenameColumnActionProto
    ast_alter_column_type_action_node: ASTAlterColumnTypeActionProto
    ast_alter_column_options_action_node: ASTAlterColumnOptionsActionProto
    ast_alter_column_drop_not_null_action_node: ASTAlterColumnDropNotNullActionProto
    ast_grant_to_clause_node: ASTGrantToClauseProto
    ast_filter_using_clause_node: ASTFilterUsingClauseProto
    ast_revoke_from_clause_node: ASTRevokeFromClauseProto
    ast_rename_to_clause_node: ASTRenameToClauseProto
    ast_set_collate_clause_node: ASTSetCollateClauseProto
    ast_alter_column_set_default_action_node: ASTAlterColumnSetDefaultActionProto
    ast_alter_column_drop_default_action_node: ASTAlterColumnDropDefaultActionProto
    ast_restrict_to_clause_node: ASTRestrictToClauseProto
    ast_add_to_restrictee_list_clause_node: ASTAddToRestricteeListClauseProto
    ast_remove_from_restrictee_list_clause_node: ASTRemoveFromRestricteeListClauseProto
    ast_alter_sub_entity_action_node: ASTAlterSubEntityActionProto
    ast_add_sub_entity_action_node: ASTAddSubEntityActionProto
    ast_drop_sub_entity_action_node: ASTDropSubEntityActionProto
    ast_add_ttl_action_node: ASTAddTtlActionProto
    ast_replace_ttl_action_node: ASTReplaceTtlActionProto
    ast_drop_ttl_action_node: ASTDropTtlActionProto
    ast_spanner_alter_column_action_node: ASTSpannerAlterColumnActionProto
    ast_spanner_set_on_delete_action_node: ASTSpannerSetOnDeleteActionProto
    ast_alter_column_drop_generated_action_node: ASTAlterColumnDropGeneratedActionProto
    ast_add_column_identifier_action_node: ASTAddColumnIdentifierActionProto
    ast_rebuild_action_node: ASTRebuildActionProto
    ast_alter_column_set_generated_action_node: ASTAlterColumnSetGeneratedActionProto
    def __init__(self, ast_set_options_action_node: _Optional[_Union[ASTSetOptionsActionProto, _Mapping]] = ..., ast_set_as_action_node: _Optional[_Union[ASTSetAsActionProto, _Mapping]] = ..., ast_add_constraint_action_node: _Optional[_Union[ASTAddConstraintActionProto, _Mapping]] = ..., ast_drop_primary_key_action_node: _Optional[_Union[ASTDropPrimaryKeyActionProto, _Mapping]] = ..., ast_drop_constraint_action_node: _Optional[_Union[ASTDropConstraintActionProto, _Mapping]] = ..., ast_alter_constraint_enforcement_action_node: _Optional[_Union[ASTAlterConstraintEnforcementActionProto, _Mapping]] = ..., ast_alter_constraint_set_options_action_node: _Optional[_Union[ASTAlterConstraintSetOptionsActionProto, _Mapping]] = ..., ast_add_column_action_node: _Optional[_Union[ASTAddColumnActionProto, _Mapping]] = ..., ast_drop_column_action_node: _Optional[_Union[ASTDropColumnActionProto, _Mapping]] = ..., ast_rename_column_action_node: _Optional[_Union[ASTRenameColumnActionProto, _Mapping]] = ..., ast_alter_column_type_action_node: _Optional[_Union[ASTAlterColumnTypeActionProto, _Mapping]] = ..., ast_alter_column_options_action_node: _Optional[_Union[ASTAlterColumnOptionsActionProto, _Mapping]] = ..., ast_alter_column_drop_not_null_action_node: _Optional[_Union[ASTAlterColumnDropNotNullActionProto, _Mapping]] = ..., ast_grant_to_clause_node: _Optional[_Union[ASTGrantToClauseProto, _Mapping]] = ..., ast_filter_using_clause_node: _Optional[_Union[ASTFilterUsingClauseProto, _Mapping]] = ..., ast_revoke_from_clause_node: _Optional[_Union[ASTRevokeFromClauseProto, _Mapping]] = ..., ast_rename_to_clause_node: _Optional[_Union[ASTRenameToClauseProto, _Mapping]] = ..., ast_set_collate_clause_node: _Optional[_Union[ASTSetCollateClauseProto, _Mapping]] = ..., ast_alter_column_set_default_action_node: _Optional[_Union[ASTAlterColumnSetDefaultActionProto, _Mapping]] = ..., ast_alter_column_drop_default_action_node: _Optional[_Union[ASTAlterColumnDropDefaultActionProto, _Mapping]] = ..., ast_restrict_to_clause_node: _Optional[_Union[ASTRestrictToClauseProto, _Mapping]] = ..., ast_add_to_restrictee_list_clause_node: _Optional[_Union[ASTAddToRestricteeListClauseProto, _Mapping]] = ..., ast_remove_from_restrictee_list_clause_node: _Optional[_Union[ASTRemoveFromRestricteeListClauseProto, _Mapping]] = ..., ast_alter_sub_entity_action_node: _Optional[_Union[ASTAlterSubEntityActionProto, _Mapping]] = ..., ast_add_sub_entity_action_node: _Optional[_Union[ASTAddSubEntityActionProto, _Mapping]] = ..., ast_drop_sub_entity_action_node: _Optional[_Union[ASTDropSubEntityActionProto, _Mapping]] = ..., ast_add_ttl_action_node: _Optional[_Union[ASTAddTtlActionProto, _Mapping]] = ..., ast_replace_ttl_action_node: _Optional[_Union[ASTReplaceTtlActionProto, _Mapping]] = ..., ast_drop_ttl_action_node: _Optional[_Union[ASTDropTtlActionProto, _Mapping]] = ..., ast_spanner_alter_column_action_node: _Optional[_Union[ASTSpannerAlterColumnActionProto, _Mapping]] = ..., ast_spanner_set_on_delete_action_node: _Optional[_Union[ASTSpannerSetOnDeleteActionProto, _Mapping]] = ..., ast_alter_column_drop_generated_action_node: _Optional[_Union[ASTAlterColumnDropGeneratedActionProto, _Mapping]] = ..., ast_add_column_identifier_action_node: _Optional[_Union[ASTAddColumnIdentifierActionProto, _Mapping]] = ..., ast_rebuild_action_node: _Optional[_Union[ASTRebuildActionProto, _Mapping]] = ..., ast_alter_column_set_generated_action_node: _Optional[_Union[ASTAlterColumnSetGeneratedActionProto, _Mapping]] = ...) -> None: ...

class ASTAlterActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTSetOptionsActionProto(_message.Message):
    __slots__ = ("parent", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTSetAsActionProto(_message.Message):
    __slots__ = ("parent", "json_body", "text_body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JSON_BODY_FIELD_NUMBER: _ClassVar[int]
    TEXT_BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    json_body: ASTJSONLiteralProto
    text_body: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., json_body: _Optional[_Union[ASTJSONLiteralProto, _Mapping]] = ..., text_body: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTAddConstraintActionProto(_message.Message):
    __slots__ = ("parent", "constraint", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    constraint: AnyASTTableConstraintProto
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., constraint: _Optional[_Union[AnyASTTableConstraintProto, _Mapping]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTDropPrimaryKeyActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropConstraintActionProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    constraint_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterConstraintEnforcementActionProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "is_if_exists", "is_enforced")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    IS_ENFORCED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    constraint_name: ASTIdentifierProto
    is_if_exists: bool
    is_enforced: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ..., is_enforced: bool = ...) -> None: ...

class ASTAlterConstraintSetOptionsActionProto(_message.Message):
    __slots__ = ("parent", "constraint_name", "options_list", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    constraint_name: ASTIdentifierProto
    options_list: ASTOptionsListProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAddColumnIdentifierActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "options_list", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    options_list: ASTOptionsListProto
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTAddColumnActionProto(_message.Message):
    __slots__ = ("parent", "column_definition", "column_position", "fill_expression", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    COLUMN_POSITION_FIELD_NUMBER: _ClassVar[int]
    FILL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_definition: ASTColumnDefinitionProto
    column_position: ASTColumnPositionProto
    fill_expression: AnyASTExpressionProto
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_definition: _Optional[_Union[ASTColumnDefinitionProto, _Mapping]] = ..., column_position: _Optional[_Union[ASTColumnPositionProto, _Mapping]] = ..., fill_expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTDropColumnActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTRenameColumnActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "new_column_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    new_column_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., new_column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnTypeActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "schema", "collate", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    schema: AnyASTColumnSchemaProto
    collate: ASTCollateProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., schema: _Optional[_Union[AnyASTColumnSchemaProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnOptionsActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "options_list", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    options_list: ASTOptionsListProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnSetDefaultActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "default_expression", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    default_expression: AnyASTExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., default_expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnDropDefaultActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnDropNotNullActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnDropGeneratedActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterColumnSetGeneratedActionProto(_message.Message):
    __slots__ = ("parent", "column_name", "generated_column_info", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_name: ASTIdentifierProto
    generated_column_info: ASTGeneratedColumnInfoProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., generated_column_info: _Optional[_Union[ASTGeneratedColumnInfoProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTGrantToClauseProto(_message.Message):
    __slots__ = ("parent", "grantee_list", "has_grant_keyword_and_parens")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    HAS_GRANT_KEYWORD_AND_PARENS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    grantee_list: ASTGranteeListProto
    has_grant_keyword_and_parens: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., grantee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ..., has_grant_keyword_and_parens: bool = ...) -> None: ...

class ASTRestrictToClauseProto(_message.Message):
    __slots__ = ("parent", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    restrictee_list: ASTGranteeListProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., restrictee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ...) -> None: ...

class ASTAddToRestricteeListClauseProto(_message.Message):
    __slots__ = ("parent", "is_if_not_exists", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    is_if_not_exists: bool
    restrictee_list: ASTGranteeListProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., is_if_not_exists: bool = ..., restrictee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ...) -> None: ...

class ASTRemoveFromRestricteeListClauseProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "restrictee_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTEE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    is_if_exists: bool
    restrictee_list: ASTGranteeListProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ..., restrictee_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ...) -> None: ...

class ASTFilterUsingClauseProto(_message.Message):
    __slots__ = ("parent", "predicate", "has_filter_keyword")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    HAS_FILTER_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    predicate: AnyASTExpressionProto
    has_filter_keyword: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., predicate: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., has_filter_keyword: bool = ...) -> None: ...

class ASTRevokeFromClauseProto(_message.Message):
    __slots__ = ("parent", "revoke_from_list", "is_revoke_from_all")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REVOKE_FROM_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_REVOKE_FROM_ALL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    revoke_from_list: ASTGranteeListProto
    is_revoke_from_all: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., revoke_from_list: _Optional[_Union[ASTGranteeListProto, _Mapping]] = ..., is_revoke_from_all: bool = ...) -> None: ...

class ASTRenameToClauseProto(_message.Message):
    __slots__ = ("parent", "new_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    new_name: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., new_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTSetCollateClauseProto(_message.Message):
    __slots__ = ("parent", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTAlterSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "type", "name", "action", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    type: ASTIdentifierProto
    name: ASTIdentifierProto
    action: AnyASTAlterActionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., action: _Optional[_Union[AnyASTAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAddSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "type", "name", "options_list", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    type: ASTIdentifierProto
    name: ASTIdentifierProto
    options_list: ASTOptionsListProto
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTDropSubEntityActionProto(_message.Message):
    __slots__ = ("parent", "type", "name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    type: ASTIdentifierProto
    name: ASTIdentifierProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAddTtlActionProto(_message.Message):
    __slots__ = ("parent", "expression", "is_if_not_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    expression: AnyASTExpressionProto
    is_if_not_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_if_not_exists: bool = ...) -> None: ...

class ASTReplaceTtlActionProto(_message.Message):
    __slots__ = ("parent", "expression", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    expression: AnyASTExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTDropTtlActionProto(_message.Message):
    __slots__ = ("parent", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterActionListProto(_message.Message):
    __slots__ = ("parent", "actions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    actions: _containers.RepeatedCompositeFieldContainer[AnyASTAlterActionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[AnyASTAlterActionProto, _Mapping]]] = ...) -> None: ...

class ASTAlterAllRowAccessPoliciesStatementProto(_message.Message):
    __slots__ = ("parent", "table_name_path", "alter_action")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    ALTER_ACTION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    table_name_path: ASTPathExpressionProto
    alter_action: AnyASTAlterActionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., table_name_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., alter_action: _Optional[_Union[AnyASTAlterActionProto, _Mapping]] = ...) -> None: ...

class ASTForeignKeyActionsProto(_message.Message):
    __slots__ = ("parent", "update_action", "delete_action")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    update_action: _ast_enums_pb2.ASTForeignKeyActionsEnums.Action
    delete_action: _ast_enums_pb2.ASTForeignKeyActionsEnums.Action
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., update_action: _Optional[_Union[_ast_enums_pb2.ASTForeignKeyActionsEnums.Action, str]] = ..., delete_action: _Optional[_Union[_ast_enums_pb2.ASTForeignKeyActionsEnums.Action, str]] = ...) -> None: ...

class ASTForeignKeyReferenceProto(_message.Message):
    __slots__ = ("parent", "table_name", "column_list", "actions", "match", "enforced")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_name: ASTPathExpressionProto
    column_list: ASTColumnListProto
    actions: ASTForeignKeyActionsProto
    match: _ast_enums_pb2.ASTForeignKeyReferenceEnums.Match
    enforced: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., actions: _Optional[_Union[ASTForeignKeyActionsProto, _Mapping]] = ..., match: _Optional[_Union[_ast_enums_pb2.ASTForeignKeyReferenceEnums.Match, str]] = ..., enforced: bool = ...) -> None: ...

class ASTScriptProto(_message.Message):
    __slots__ = ("parent", "statement_list_node")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    statement_list_node: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., statement_list_node: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTElseifClauseProto(_message.Message):
    __slots__ = ("parent", "condition", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    condition: AnyASTExpressionProto
    body: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., body: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTElseifClauseListProto(_message.Message):
    __slots__ = ("parent", "elseif_clauses")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELSEIF_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    elseif_clauses: _containers.RepeatedCompositeFieldContainer[ASTElseifClauseProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., elseif_clauses: _Optional[_Iterable[_Union[ASTElseifClauseProto, _Mapping]]] = ...) -> None: ...

class ASTIfStatementProto(_message.Message):
    __slots__ = ("parent", "condition", "then_list", "elseif_clauses", "else_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    THEN_LIST_FIELD_NUMBER: _ClassVar[int]
    ELSEIF_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    ELSE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    condition: AnyASTExpressionProto
    then_list: ASTStatementListProto
    elseif_clauses: ASTElseifClauseListProto
    else_list: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., then_list: _Optional[_Union[ASTStatementListProto, _Mapping]] = ..., elseif_clauses: _Optional[_Union[ASTElseifClauseListProto, _Mapping]] = ..., else_list: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTWhenThenClauseProto(_message.Message):
    __slots__ = ("parent", "condition", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    condition: AnyASTExpressionProto
    body: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., body: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTWhenThenClauseListProto(_message.Message):
    __slots__ = ("parent", "when_then_clauses")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WHEN_THEN_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    when_then_clauses: _containers.RepeatedCompositeFieldContainer[ASTWhenThenClauseProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., when_then_clauses: _Optional[_Iterable[_Union[ASTWhenThenClauseProto, _Mapping]]] = ...) -> None: ...

class ASTCaseStatementProto(_message.Message):
    __slots__ = ("parent", "expression", "when_then_clauses", "else_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    WHEN_THEN_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    ELSE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    expression: AnyASTExpressionProto
    when_then_clauses: ASTWhenThenClauseListProto
    else_list: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., when_then_clauses: _Optional[_Union[ASTWhenThenClauseListProto, _Mapping]] = ..., else_list: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTHintProto(_message.Message):
    __slots__ = ("parent", "num_shards_hint", "hint_entries")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARDS_HINT_FIELD_NUMBER: _ClassVar[int]
    HINT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    num_shards_hint: ASTIntLiteralProto
    hint_entries: _containers.RepeatedCompositeFieldContainer[ASTHintEntryProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., num_shards_hint: _Optional[_Union[ASTIntLiteralProto, _Mapping]] = ..., hint_entries: _Optional[_Iterable[_Union[ASTHintEntryProto, _Mapping]]] = ...) -> None: ...

class ASTHintEntryProto(_message.Message):
    __slots__ = ("parent", "qualifier", "name", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    qualifier: ASTIdentifierProto
    name: ASTIdentifierProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., qualifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTUnpivotInItemLabelProto(_message.Message):
    __slots__ = ("parent", "string_label", "int_label")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRING_LABEL_FIELD_NUMBER: _ClassVar[int]
    INT_LABEL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    string_label: ASTStringLiteralProto
    int_label: ASTIntLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., string_label: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., int_label: _Optional[_Union[ASTIntLiteralProto, _Mapping]] = ...) -> None: ...

class ASTDescriptorProto(_message.Message):
    __slots__ = ("parent", "columns")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    columns: ASTDescriptorColumnListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., columns: _Optional[_Union[ASTDescriptorColumnListProto, _Mapping]] = ...) -> None: ...

class AnyASTColumnSchemaProto(_message.Message):
    __slots__ = ("ast_simple_column_schema_node", "ast_struct_column_schema_node", "ast_inferred_type_column_schema_node", "ast_element_type_column_schema_node")
    AST_SIMPLE_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_STRUCT_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_INFERRED_TYPE_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ELEMENT_TYPE_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_simple_column_schema_node: ASTSimpleColumnSchemaProto
    ast_struct_column_schema_node: ASTStructColumnSchemaProto
    ast_inferred_type_column_schema_node: ASTInferredTypeColumnSchemaProto
    ast_element_type_column_schema_node: AnyASTElementTypeColumnSchemaProto
    def __init__(self, ast_simple_column_schema_node: _Optional[_Union[ASTSimpleColumnSchemaProto, _Mapping]] = ..., ast_struct_column_schema_node: _Optional[_Union[ASTStructColumnSchemaProto, _Mapping]] = ..., ast_inferred_type_column_schema_node: _Optional[_Union[ASTInferredTypeColumnSchemaProto, _Mapping]] = ..., ast_element_type_column_schema_node: _Optional[_Union[AnyASTElementTypeColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTColumnSchemaProto(_message.Message):
    __slots__ = ("parent", "type_parameters", "generated_column_info", "default_expression", "collate", "attributes", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    type_parameters: ASTTypeParameterListProto
    generated_column_info: ASTGeneratedColumnInfoProto
    default_expression: AnyASTExpressionProto
    collate: ASTCollateProto
    attributes: ASTColumnAttributeListProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., generated_column_info: _Optional[_Union[ASTGeneratedColumnInfoProto, _Mapping]] = ..., default_expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ..., attributes: _Optional[_Union[ASTColumnAttributeListProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTSimpleColumnSchemaProto(_message.Message):
    __slots__ = ("parent", "type_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnSchemaProto
    type_name: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTColumnSchemaProto, _Mapping]] = ..., type_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTElementTypeColumnSchemaProto(_message.Message):
    __slots__ = ("ast_array_column_schema_node", "ast_range_column_schema_node")
    AST_ARRAY_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_RANGE_COLUMN_SCHEMA_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_array_column_schema_node: ASTArrayColumnSchemaProto
    ast_range_column_schema_node: ASTRangeColumnSchemaProto
    def __init__(self, ast_array_column_schema_node: _Optional[_Union[ASTArrayColumnSchemaProto, _Mapping]] = ..., ast_range_column_schema_node: _Optional[_Union[ASTRangeColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTElementTypeColumnSchemaProto(_message.Message):
    __slots__ = ("parent", "element_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnSchemaProto
    element_schema: AnyASTColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTColumnSchemaProto, _Mapping]] = ..., element_schema: _Optional[_Union[AnyASTColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTArrayColumnSchemaProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTElementTypeColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTElementTypeColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTRangeColumnSchemaProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTElementTypeColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTElementTypeColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTPrimaryKeyElementProto(_message.Message):
    __slots__ = ("parent", "column", "ordering_spec", "null_order")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    ORDERING_SPEC_FIELD_NUMBER: _ClassVar[int]
    NULL_ORDER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    column: ASTIdentifierProto
    ordering_spec: _ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec
    null_order: ASTNullOrderProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., column: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., ordering_spec: _Optional[_Union[_ast_enums_pb2.ASTOrderingExpressionEnums.OrderingSpec, str]] = ..., null_order: _Optional[_Union[ASTNullOrderProto, _Mapping]] = ...) -> None: ...

class ASTPrimaryKeyElementListProto(_message.Message):
    __slots__ = ("parent", "elements")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    elements: _containers.RepeatedCompositeFieldContainer[ASTPrimaryKeyElementProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[ASTPrimaryKeyElementProto, _Mapping]]] = ...) -> None: ...

class AnyASTTableConstraintProto(_message.Message):
    __slots__ = ("ast_primary_key_node", "ast_foreign_key_node", "ast_check_constraint_node")
    AST_PRIMARY_KEY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOREIGN_KEY_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CHECK_CONSTRAINT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_primary_key_node: ASTPrimaryKeyProto
    ast_foreign_key_node: ASTForeignKeyProto
    ast_check_constraint_node: ASTCheckConstraintProto
    def __init__(self, ast_primary_key_node: _Optional[_Union[ASTPrimaryKeyProto, _Mapping]] = ..., ast_foreign_key_node: _Optional[_Union[ASTForeignKeyProto, _Mapping]] = ..., ast_check_constraint_node: _Optional[_Union[ASTCheckConstraintProto, _Mapping]] = ...) -> None: ...

class ASTTableConstraintProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableElementProto
    def __init__(self, parent: _Optional[_Union[ASTTableElementProto, _Mapping]] = ...) -> None: ...

class ASTPrimaryKeyProto(_message.Message):
    __slots__ = ("parent", "element_list", "options_list", "constraint_name", "enforced")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    ENFORCED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableConstraintProto
    element_list: ASTPrimaryKeyElementListProto
    options_list: ASTOptionsListProto
    constraint_name: ASTIdentifierProto
    enforced: bool
    def __init__(self, parent: _Optional[_Union[ASTTableConstraintProto, _Mapping]] = ..., element_list: _Optional[_Union[ASTPrimaryKeyElementListProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., enforced: bool = ...) -> None: ...

class ASTForeignKeyProto(_message.Message):
    __slots__ = ("parent", "column_list", "reference", "options_list", "constraint_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableConstraintProto
    column_list: ASTColumnListProto
    reference: ASTForeignKeyReferenceProto
    options_list: ASTOptionsListProto
    constraint_name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTTableConstraintProto, _Mapping]] = ..., column_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., reference: _Optional[_Union[ASTForeignKeyReferenceProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTCheckConstraintProto(_message.Message):
    __slots__ = ("parent", "expression", "options_list", "constraint_name", "is_enforced")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ENFORCED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableConstraintProto
    expression: AnyASTExpressionProto
    options_list: ASTOptionsListProto
    constraint_name: ASTIdentifierProto
    is_enforced: bool
    def __init__(self, parent: _Optional[_Union[ASTTableConstraintProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., constraint_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., is_enforced: bool = ...) -> None: ...

class ASTDescriptorColumnProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTDescriptorColumnListProto(_message.Message):
    __slots__ = ("parent", "descriptor_column_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_COLUMN_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    descriptor_column_list: _containers.RepeatedCompositeFieldContainer[ASTDescriptorColumnProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., descriptor_column_list: _Optional[_Iterable[_Union[ASTDescriptorColumnProto, _Mapping]]] = ...) -> None: ...

class ASTCreateEntityStatementProto(_message.Message):
    __slots__ = ("parent", "type", "name", "options_list", "json_body", "text_body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    JSON_BODY_FIELD_NUMBER: _ClassVar[int]
    TEXT_BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    type: ASTIdentifierProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    json_body: ASTJSONLiteralProto
    text_body: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., json_body: _Optional[_Union[ASTJSONLiteralProto, _Mapping]] = ..., text_body: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTRaiseStatementProto(_message.Message):
    __slots__ = ("parent", "message")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    message: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., message: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTExceptionHandlerProto(_message.Message):
    __slots__ = ("parent", "statement_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    statement_list: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., statement_list: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTExceptionHandlerListProto(_message.Message):
    __slots__ = ("parent", "exception_handler_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_HANDLER_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    exception_handler_list: _containers.RepeatedCompositeFieldContainer[ASTExceptionHandlerProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., exception_handler_list: _Optional[_Iterable[_Union[ASTExceptionHandlerProto, _Mapping]]] = ...) -> None: ...

class ASTBeginEndBlockProto(_message.Message):
    __slots__ = ("parent", "label", "statement_list_node", "handler_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    HANDLER_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    label: ASTLabelProto
    statement_list_node: ASTStatementListProto
    handler_list: ASTExceptionHandlerListProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., label: _Optional[_Union[ASTLabelProto, _Mapping]] = ..., statement_list_node: _Optional[_Union[ASTStatementListProto, _Mapping]] = ..., handler_list: _Optional[_Union[ASTExceptionHandlerListProto, _Mapping]] = ...) -> None: ...

class ASTIdentifierListProto(_message.Message):
    __slots__ = ("parent", "identifier_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier_list: _containers.RepeatedCompositeFieldContainer[ASTIdentifierProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier_list: _Optional[_Iterable[_Union[ASTIdentifierProto, _Mapping]]] = ...) -> None: ...

class ASTVariableDeclarationProto(_message.Message):
    __slots__ = ("parent", "variable_list", "type", "default_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    variable_list: ASTIdentifierListProto
    type: AnyASTTypeProto
    default_value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., variable_list: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ..., type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., default_value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTUntilClauseProto(_message.Message):
    __slots__ = ("parent", "condition")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    condition: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTBreakContinueStatementProto(_message.Message):
    __slots__ = ("ast_break_statement_node", "ast_continue_statement_node")
    AST_BREAK_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CONTINUE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_break_statement_node: ASTBreakStatementProto
    ast_continue_statement_node: ASTContinueStatementProto
    def __init__(self, ast_break_statement_node: _Optional[_Union[ASTBreakStatementProto, _Mapping]] = ..., ast_continue_statement_node: _Optional[_Union[ASTContinueStatementProto, _Mapping]] = ...) -> None: ...

class ASTBreakContinueStatementProto(_message.Message):
    __slots__ = ("parent", "label")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    label: ASTLabelProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., label: _Optional[_Union[ASTLabelProto, _Mapping]] = ...) -> None: ...

class ASTBreakStatementProto(_message.Message):
    __slots__ = ("parent", "keyword")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    parent: ASTBreakContinueStatementProto
    keyword: _ast_enums_pb2.ASTBreakContinueStatementEnums.BreakContinueKeyword
    def __init__(self, parent: _Optional[_Union[ASTBreakContinueStatementProto, _Mapping]] = ..., keyword: _Optional[_Union[_ast_enums_pb2.ASTBreakContinueStatementEnums.BreakContinueKeyword, str]] = ...) -> None: ...

class ASTContinueStatementProto(_message.Message):
    __slots__ = ("parent", "keyword")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    parent: ASTBreakContinueStatementProto
    keyword: _ast_enums_pb2.ASTBreakContinueStatementEnums.BreakContinueKeyword
    def __init__(self, parent: _Optional[_Union[ASTBreakContinueStatementProto, _Mapping]] = ..., keyword: _Optional[_Union[_ast_enums_pb2.ASTBreakContinueStatementEnums.BreakContinueKeyword, str]] = ...) -> None: ...

class ASTDropPrivilegeRestrictionStatementProto(_message.Message):
    __slots__ = ("parent", "is_if_exists", "privileges", "object_type", "name_path")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    is_if_exists: bool
    privileges: ASTPrivilegesProto
    object_type: ASTIdentifierProto
    name_path: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., is_if_exists: bool = ..., privileges: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., object_type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTDropRowAccessPolicyStatementProto(_message.Message):
    __slots__ = ("parent", "name", "table_name", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    table_name: ASTPathExpressionProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTCreatePrivilegeRestrictionStatementProto(_message.Message):
    __slots__ = ("parent", "privileges", "object_type", "name_path", "restrict_to")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_TO_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    privileges: ASTPrivilegesProto
    object_type: ASTIdentifierProto
    name_path: ASTPathExpressionProto
    restrict_to: ASTRestrictToClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., privileges: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., object_type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., name_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., restrict_to: _Optional[_Union[ASTRestrictToClauseProto, _Mapping]] = ...) -> None: ...

class ASTCreateRowAccessPolicyStatementProto(_message.Message):
    __slots__ = ("parent", "target_path", "grant_to", "filter_using", "name", "has_access_keyword")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    GRANT_TO_FIELD_NUMBER: _ClassVar[int]
    FILTER_USING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HAS_ACCESS_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    target_path: ASTPathExpressionProto
    grant_to: ASTGrantToClauseProto
    filter_using: ASTFilterUsingClauseProto
    name: ASTPathExpressionProto
    has_access_keyword: bool
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., target_path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., grant_to: _Optional[_Union[ASTGrantToClauseProto, _Mapping]] = ..., filter_using: _Optional[_Union[ASTFilterUsingClauseProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., has_access_keyword: bool = ...) -> None: ...

class ASTDropStatementProto(_message.Message):
    __slots__ = ("parent", "name", "drop_mode", "is_if_exists", "schema_object_kind")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DROP_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    name: ASTPathExpressionProto
    drop_mode: _ast_enums_pb2.ASTDropStatementEnums.DropMode
    is_if_exists: bool
    schema_object_kind: _ast_enums_pb2.SchemaObjectKind
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., drop_mode: _Optional[_Union[_ast_enums_pb2.ASTDropStatementEnums.DropMode, str]] = ..., is_if_exists: bool = ..., schema_object_kind: _Optional[_Union[_ast_enums_pb2.SchemaObjectKind, str]] = ...) -> None: ...

class ASTReturnStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ...) -> None: ...

class ASTSingleAssignmentProto(_message.Message):
    __slots__ = ("parent", "variable", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    variable: ASTIdentifierProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., variable: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTParameterAssignmentProto(_message.Message):
    __slots__ = ("parent", "parameter", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    parameter: ASTParameterExprProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., parameter: _Optional[_Union[ASTParameterExprProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTSystemVariableAssignmentProto(_message.Message):
    __slots__ = ("parent", "system_variable", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    system_variable: ASTSystemVariableExprProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., system_variable: _Optional[_Union[ASTSystemVariableExprProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTAssignmentFromStructProto(_message.Message):
    __slots__ = ("parent", "variables", "struct_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    STRUCT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    variables: ASTIdentifierListProto
    struct_expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., variables: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ..., struct_expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTCreateTableStmtBaseProto(_message.Message):
    __slots__ = ("ast_create_table_statement_node", "ast_create_external_table_statement_node", "ast_aux_load_data_statement_node")
    AST_CREATE_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_EXTERNAL_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_AUX_LOAD_DATA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_create_table_statement_node: ASTCreateTableStatementProto
    ast_create_external_table_statement_node: ASTCreateExternalTableStatementProto
    ast_aux_load_data_statement_node: ASTAuxLoadDataStatementProto
    def __init__(self, ast_create_table_statement_node: _Optional[_Union[ASTCreateTableStatementProto, _Mapping]] = ..., ast_create_external_table_statement_node: _Optional[_Union[ASTCreateExternalTableStatementProto, _Mapping]] = ..., ast_aux_load_data_statement_node: _Optional[_Union[ASTAuxLoadDataStatementProto, _Mapping]] = ...) -> None: ...

class ASTCreateTableStmtBaseProto(_message.Message):
    __slots__ = ("parent", "name", "table_element_list", "options_list", "like_table_name", "collate", "with_connection_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_ELEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    LIKE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    table_element_list: ASTTableElementListProto
    options_list: ASTOptionsListProto
    like_table_name: ASTPathExpressionProto
    collate: ASTCollateProto
    with_connection_clause: ASTWithConnectionClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., table_element_list: _Optional[_Union[ASTTableElementListProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., like_table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ...) -> None: ...

class ASTCreateTableStatementProto(_message.Message):
    __slots__ = ("parent", "clone_data_source", "copy_data_source", "partition_by", "cluster_by", "query", "spanner_options", "ttl")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLONE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    COPY_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SPANNER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateTableStmtBaseProto
    clone_data_source: ASTCloneDataSourceProto
    copy_data_source: ASTCopyDataSourceProto
    partition_by: ASTPartitionByProto
    cluster_by: ASTClusterByProto
    query: ASTQueryProto
    spanner_options: ASTSpannerTableOptionsProto
    ttl: ASTTtlClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateTableStmtBaseProto, _Mapping]] = ..., clone_data_source: _Optional[_Union[ASTCloneDataSourceProto, _Mapping]] = ..., copy_data_source: _Optional[_Union[ASTCopyDataSourceProto, _Mapping]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., cluster_by: _Optional[_Union[ASTClusterByProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., spanner_options: _Optional[_Union[ASTSpannerTableOptionsProto, _Mapping]] = ..., ttl: _Optional[_Union[ASTTtlClauseProto, _Mapping]] = ...) -> None: ...

class ASTCreateExternalTableStatementProto(_message.Message):
    __slots__ = ("parent", "with_partition_columns_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WITH_PARTITION_COLUMNS_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateTableStmtBaseProto
    with_partition_columns_clause: ASTWithPartitionColumnsClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateTableStmtBaseProto, _Mapping]] = ..., with_partition_columns_clause: _Optional[_Union[ASTWithPartitionColumnsClauseProto, _Mapping]] = ...) -> None: ...

class AnyASTCreateViewStatementBaseProto(_message.Message):
    __slots__ = ("ast_create_view_statement_node", "ast_create_materialized_view_statement_node", "ast_create_approx_view_statement_node")
    AST_CREATE_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_MATERIALIZED_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_APPROX_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_create_view_statement_node: ASTCreateViewStatementProto
    ast_create_materialized_view_statement_node: ASTCreateMaterializedViewStatementProto
    ast_create_approx_view_statement_node: ASTCreateApproxViewStatementProto
    def __init__(self, ast_create_view_statement_node: _Optional[_Union[ASTCreateViewStatementProto, _Mapping]] = ..., ast_create_materialized_view_statement_node: _Optional[_Union[ASTCreateMaterializedViewStatementProto, _Mapping]] = ..., ast_create_approx_view_statement_node: _Optional[_Union[ASTCreateApproxViewStatementProto, _Mapping]] = ...) -> None: ...

class ASTCreateViewStatementBaseProto(_message.Message):
    __slots__ = ("parent", "name", "column_with_options_list", "options_list", "query", "sql_security", "recursive")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_WITH_OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    column_with_options_list: ASTColumnWithOptionsListProto
    options_list: ASTOptionsListProto
    query: ASTQueryProto
    sql_security: _ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity
    recursive: bool
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., column_with_options_list: _Optional[_Union[ASTColumnWithOptionsListProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ..., sql_security: _Optional[_Union[_ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity, str]] = ..., recursive: bool = ...) -> None: ...

class ASTCreateViewStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateViewStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateViewStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTCreateMaterializedViewStatementProto(_message.Message):
    __slots__ = ("parent", "partition_by", "cluster_by", "replica_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateViewStatementBaseProto
    partition_by: ASTPartitionByProto
    cluster_by: ASTClusterByProto
    replica_source: ASTPathExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTCreateViewStatementBaseProto, _Mapping]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., cluster_by: _Optional[_Union[ASTClusterByProto, _Mapping]] = ..., replica_source: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ...) -> None: ...

class ASTCreateApproxViewStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateViewStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateViewStatementBaseProto, _Mapping]] = ...) -> None: ...

class AnyASTLoopStatementProto(_message.Message):
    __slots__ = ("ast_while_statement_node", "ast_repeat_statement_node", "ast_for_in_statement_node")
    AST_WHILE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_REPEAT_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_FOR_IN_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_while_statement_node: ASTWhileStatementProto
    ast_repeat_statement_node: ASTRepeatStatementProto
    ast_for_in_statement_node: ASTForInStatementProto
    def __init__(self, ast_while_statement_node: _Optional[_Union[ASTWhileStatementProto, _Mapping]] = ..., ast_repeat_statement_node: _Optional[_Union[ASTRepeatStatementProto, _Mapping]] = ..., ast_for_in_statement_node: _Optional[_Union[ASTForInStatementProto, _Mapping]] = ...) -> None: ...

class ASTLoopStatementProto(_message.Message):
    __slots__ = ("parent", "label", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTScriptStatementProto
    label: ASTLabelProto
    body: ASTStatementListProto
    def __init__(self, parent: _Optional[_Union[ASTScriptStatementProto, _Mapping]] = ..., label: _Optional[_Union[ASTLabelProto, _Mapping]] = ..., body: _Optional[_Union[ASTStatementListProto, _Mapping]] = ...) -> None: ...

class ASTWhileStatementProto(_message.Message):
    __slots__ = ("parent", "condition")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLoopStatementProto
    condition: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTLoopStatementProto, _Mapping]] = ..., condition: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTRepeatStatementProto(_message.Message):
    __slots__ = ("parent", "until_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNTIL_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLoopStatementProto
    until_clause: ASTUntilClauseProto
    def __init__(self, parent: _Optional[_Union[ASTLoopStatementProto, _Mapping]] = ..., until_clause: _Optional[_Union[ASTUntilClauseProto, _Mapping]] = ...) -> None: ...

class ASTForInStatementProto(_message.Message):
    __slots__ = ("parent", "variable", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTLoopStatementProto
    variable: ASTIdentifierProto
    query: ASTQueryProto
    def __init__(self, parent: _Optional[_Union[ASTLoopStatementProto, _Mapping]] = ..., variable: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ...) -> None: ...

class AnyASTAlterStatementBaseProto(_message.Message):
    __slots__ = ("ast_alter_database_statement_node", "ast_alter_schema_statement_node", "ast_alter_table_statement_node", "ast_alter_view_statement_node", "ast_alter_materialized_view_statement_node", "ast_alter_row_access_policy_statement_node", "ast_alter_entity_statement_node", "ast_alter_privilege_restriction_statement_node", "ast_alter_model_statement_node", "ast_alter_approx_view_statement_node", "ast_alter_external_schema_statement_node", "ast_alter_connection_statement_node", "ast_alter_index_statement_node", "ast_alter_sequence_statement_node")
    AST_ALTER_DATABASE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_SCHEMA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_TABLE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_MATERIALIZED_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_ROW_ACCESS_POLICY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_ENTITY_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_PRIVILEGE_RESTRICTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_MODEL_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_APPROX_VIEW_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_EXTERNAL_SCHEMA_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_CONNECTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_INDEX_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_ALTER_SEQUENCE_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_alter_database_statement_node: ASTAlterDatabaseStatementProto
    ast_alter_schema_statement_node: ASTAlterSchemaStatementProto
    ast_alter_table_statement_node: ASTAlterTableStatementProto
    ast_alter_view_statement_node: ASTAlterViewStatementProto
    ast_alter_materialized_view_statement_node: ASTAlterMaterializedViewStatementProto
    ast_alter_row_access_policy_statement_node: ASTAlterRowAccessPolicyStatementProto
    ast_alter_entity_statement_node: ASTAlterEntityStatementProto
    ast_alter_privilege_restriction_statement_node: ASTAlterPrivilegeRestrictionStatementProto
    ast_alter_model_statement_node: ASTAlterModelStatementProto
    ast_alter_approx_view_statement_node: ASTAlterApproxViewStatementProto
    ast_alter_external_schema_statement_node: ASTAlterExternalSchemaStatementProto
    ast_alter_connection_statement_node: ASTAlterConnectionStatementProto
    ast_alter_index_statement_node: ASTAlterIndexStatementProto
    ast_alter_sequence_statement_node: ASTAlterSequenceStatementProto
    def __init__(self, ast_alter_database_statement_node: _Optional[_Union[ASTAlterDatabaseStatementProto, _Mapping]] = ..., ast_alter_schema_statement_node: _Optional[_Union[ASTAlterSchemaStatementProto, _Mapping]] = ..., ast_alter_table_statement_node: _Optional[_Union[ASTAlterTableStatementProto, _Mapping]] = ..., ast_alter_view_statement_node: _Optional[_Union[ASTAlterViewStatementProto, _Mapping]] = ..., ast_alter_materialized_view_statement_node: _Optional[_Union[ASTAlterMaterializedViewStatementProto, _Mapping]] = ..., ast_alter_row_access_policy_statement_node: _Optional[_Union[ASTAlterRowAccessPolicyStatementProto, _Mapping]] = ..., ast_alter_entity_statement_node: _Optional[_Union[ASTAlterEntityStatementProto, _Mapping]] = ..., ast_alter_privilege_restriction_statement_node: _Optional[_Union[ASTAlterPrivilegeRestrictionStatementProto, _Mapping]] = ..., ast_alter_model_statement_node: _Optional[_Union[ASTAlterModelStatementProto, _Mapping]] = ..., ast_alter_approx_view_statement_node: _Optional[_Union[ASTAlterApproxViewStatementProto, _Mapping]] = ..., ast_alter_external_schema_statement_node: _Optional[_Union[ASTAlterExternalSchemaStatementProto, _Mapping]] = ..., ast_alter_connection_statement_node: _Optional[_Union[ASTAlterConnectionStatementProto, _Mapping]] = ..., ast_alter_index_statement_node: _Optional[_Union[ASTAlterIndexStatementProto, _Mapping]] = ..., ast_alter_sequence_statement_node: _Optional[_Union[ASTAlterSequenceStatementProto, _Mapping]] = ...) -> None: ...

class ASTAlterStatementBaseProto(_message.Message):
    __slots__ = ("parent", "path", "action_list", "is_if_exists")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    path: ASTPathExpressionProto
    action_list: ASTAlterActionListProto
    is_if_exists: bool
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., path: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., action_list: _Optional[_Union[ASTAlterActionListProto, _Mapping]] = ..., is_if_exists: bool = ...) -> None: ...

class ASTAlterConnectionStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterDatabaseStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterSchemaStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterExternalSchemaStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterTableStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterViewStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterMaterializedViewStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterApproxViewStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterModelStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...

class ASTAlterPrivilegeRestrictionStatementProto(_message.Message):
    __slots__ = ("parent", "privileges", "object_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    privileges: ASTPrivilegesProto
    object_type: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ..., privileges: _Optional[_Union[ASTPrivilegesProto, _Mapping]] = ..., object_type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTAlterRowAccessPolicyStatementProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTAlterEntityStatementProto(_message.Message):
    __slots__ = ("parent", "type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    type: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ..., type: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTRebuildActionProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ...) -> None: ...

class ASTAlterIndexStatementProto(_message.Message):
    __slots__ = ("parent", "table_name", "index_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    table_name: ASTPathExpressionProto
    index_type: _ast_enums_pb2.ASTAlterIndexStatementEnums.IndexType
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., index_type: _Optional[_Union[_ast_enums_pb2.ASTAlterIndexStatementEnums.IndexType, str]] = ...) -> None: ...

class AnyASTCreateFunctionStmtBaseProto(_message.Message):
    __slots__ = ("ast_create_function_statement_node", "ast_create_table_function_statement_node")
    AST_CREATE_FUNCTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_CREATE_TABLE_FUNCTION_STATEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_create_function_statement_node: ASTCreateFunctionStatementProto
    ast_create_table_function_statement_node: ASTCreateTableFunctionStatementProto
    def __init__(self, ast_create_function_statement_node: _Optional[_Union[ASTCreateFunctionStatementProto, _Mapping]] = ..., ast_create_table_function_statement_node: _Optional[_Union[ASTCreateTableFunctionStatementProto, _Mapping]] = ...) -> None: ...

class ASTCreateFunctionStmtBaseProto(_message.Message):
    __slots__ = ("parent", "function_declaration", "language", "code", "options_list", "determinism_level", "sql_security")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_DECLARATION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    DETERMINISM_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SQL_SECURITY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    function_declaration: ASTFunctionDeclarationProto
    language: ASTIdentifierProto
    code: ASTStringLiteralProto
    options_list: ASTOptionsListProto
    determinism_level: _ast_enums_pb2.ASTCreateFunctionStmtBaseEnums.DeterminismLevel
    sql_security: _ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., function_declaration: _Optional[_Union[ASTFunctionDeclarationProto, _Mapping]] = ..., language: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., code: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ..., determinism_level: _Optional[_Union[_ast_enums_pb2.ASTCreateFunctionStmtBaseEnums.DeterminismLevel, str]] = ..., sql_security: _Optional[_Union[_ast_enums_pb2.ASTCreateStatementEnums.SqlSecurity, str]] = ...) -> None: ...

class ASTCreateFunctionStatementProto(_message.Message):
    __slots__ = ("parent", "return_type", "sql_function_body", "is_aggregate", "is_remote", "with_connection_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RETURN_TYPE_FIELD_NUMBER: _ClassVar[int]
    SQL_FUNCTION_BODY_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    IS_REMOTE_FIELD_NUMBER: _ClassVar[int]
    WITH_CONNECTION_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateFunctionStmtBaseProto
    return_type: AnyASTTypeProto
    sql_function_body: ASTSqlFunctionBodyProto
    is_aggregate: bool
    is_remote: bool
    with_connection_clause: ASTWithConnectionClauseProto
    def __init__(self, parent: _Optional[_Union[ASTCreateFunctionStmtBaseProto, _Mapping]] = ..., return_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., sql_function_body: _Optional[_Union[ASTSqlFunctionBodyProto, _Mapping]] = ..., is_aggregate: bool = ..., is_remote: bool = ..., with_connection_clause: _Optional[_Union[ASTWithConnectionClauseProto, _Mapping]] = ...) -> None: ...

class ASTCreateTableFunctionStatementProto(_message.Message):
    __slots__ = ("parent", "return_tvf_schema", "query")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RETURN_TVF_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateFunctionStmtBaseProto
    return_tvf_schema: ASTTVFSchemaProto
    query: ASTQueryProto
    def __init__(self, parent: _Optional[_Union[ASTCreateFunctionStmtBaseProto, _Mapping]] = ..., return_tvf_schema: _Optional[_Union[ASTTVFSchemaProto, _Mapping]] = ..., query: _Optional[_Union[ASTQueryProto, _Mapping]] = ...) -> None: ...

class ASTStructColumnSchemaProto(_message.Message):
    __slots__ = ("parent", "struct_fields")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnSchemaProto
    struct_fields: _containers.RepeatedCompositeFieldContainer[ASTStructColumnFieldProto]
    def __init__(self, parent: _Optional[_Union[ASTColumnSchemaProto, _Mapping]] = ..., struct_fields: _Optional[_Iterable[_Union[ASTStructColumnFieldProto, _Mapping]]] = ...) -> None: ...

class ASTInferredTypeColumnSchemaProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTColumnSchemaProto
    def __init__(self, parent: _Optional[_Union[ASTColumnSchemaProto, _Mapping]] = ...) -> None: ...

class ASTExecuteIntoClauseProto(_message.Message):
    __slots__ = ("parent", "identifiers")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifiers: ASTIdentifierListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifiers: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ...) -> None: ...

class ASTExecuteUsingArgumentProto(_message.Message):
    __slots__ = ("parent", "expression", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTExecuteUsingClauseProto(_message.Message):
    __slots__ = ("parent", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    arguments: _containers.RepeatedCompositeFieldContainer[ASTExecuteUsingArgumentProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[ASTExecuteUsingArgumentProto, _Mapping]]] = ...) -> None: ...

class ASTExecuteImmediateStatementProto(_message.Message):
    __slots__ = ("parent", "sql", "into_clause", "using_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    INTO_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    USING_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    sql: AnyASTExpressionProto
    into_clause: ASTExecuteIntoClauseProto
    using_clause: ASTExecuteUsingClauseProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., sql: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., into_clause: _Optional[_Union[ASTExecuteIntoClauseProto, _Mapping]] = ..., using_clause: _Optional[_Union[ASTExecuteUsingClauseProto, _Mapping]] = ...) -> None: ...

class ASTAuxLoadDataFromFilesOptionsListProto(_message.Message):
    __slots__ = ("parent", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTAuxLoadDataPartitionsClauseProto(_message.Message):
    __slots__ = ("parent", "partition_filter", "is_overwrite")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    partition_filter: AnyASTExpressionProto
    is_overwrite: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., partition_filter: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., is_overwrite: bool = ...) -> None: ...

class ASTAuxLoadDataStatementProto(_message.Message):
    __slots__ = ("parent", "insertion_mode", "partition_by", "cluster_by", "from_files", "with_partition_columns_clause", "load_data_partitions_clause", "is_temp_table")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSERTION_MODE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_BY_FIELD_NUMBER: _ClassVar[int]
    FROM_FILES_FIELD_NUMBER: _ClassVar[int]
    WITH_PARTITION_COLUMNS_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LOAD_DATA_PARTITIONS_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    IS_TEMP_TABLE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateTableStmtBaseProto
    insertion_mode: _ast_enums_pb2.ASTAuxLoadDataStatementEnums.InsertionMode
    partition_by: ASTPartitionByProto
    cluster_by: ASTClusterByProto
    from_files: ASTAuxLoadDataFromFilesOptionsListProto
    with_partition_columns_clause: ASTWithPartitionColumnsClauseProto
    load_data_partitions_clause: ASTAuxLoadDataPartitionsClauseProto
    is_temp_table: bool
    def __init__(self, parent: _Optional[_Union[ASTCreateTableStmtBaseProto, _Mapping]] = ..., insertion_mode: _Optional[_Union[_ast_enums_pb2.ASTAuxLoadDataStatementEnums.InsertionMode, str]] = ..., partition_by: _Optional[_Union[ASTPartitionByProto, _Mapping]] = ..., cluster_by: _Optional[_Union[ASTClusterByProto, _Mapping]] = ..., from_files: _Optional[_Union[ASTAuxLoadDataFromFilesOptionsListProto, _Mapping]] = ..., with_partition_columns_clause: _Optional[_Union[ASTWithPartitionColumnsClauseProto, _Mapping]] = ..., load_data_partitions_clause: _Optional[_Union[ASTAuxLoadDataPartitionsClauseProto, _Mapping]] = ..., is_temp_table: bool = ...) -> None: ...

class ASTLabelProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTWithExpressionProto(_message.Message):
    __slots__ = ("parent", "variables", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    variables: ASTSelectListProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., variables: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTTtlClauseProto(_message.Message):
    __slots__ = ("parent", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTLocationProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTInputOutputClauseProto(_message.Message):
    __slots__ = ("parent", "input", "output")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    input: ASTTableElementListProto
    output: ASTTableElementListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., input: _Optional[_Union[ASTTableElementListProto, _Mapping]] = ..., output: _Optional[_Union[ASTTableElementListProto, _Mapping]] = ...) -> None: ...

class ASTSpannerTableOptionsProto(_message.Message):
    __slots__ = ("parent", "primary_key", "interleave_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    INTERLEAVE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    primary_key: ASTPrimaryKeyProto
    interleave_clause: ASTSpannerInterleaveClauseProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., primary_key: _Optional[_Union[ASTPrimaryKeyProto, _Mapping]] = ..., interleave_clause: _Optional[_Union[ASTSpannerInterleaveClauseProto, _Mapping]] = ...) -> None: ...

class ASTSpannerInterleaveClauseProto(_message.Message):
    __slots__ = ("parent", "table_name", "type", "action")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    table_name: ASTPathExpressionProto
    type: _ast_enums_pb2.ASTSpannerInterleaveClauseEnums.Type
    action: _ast_enums_pb2.ASTForeignKeyActionsEnums.Action
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., table_name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., type: _Optional[_Union[_ast_enums_pb2.ASTSpannerInterleaveClauseEnums.Type, str]] = ..., action: _Optional[_Union[_ast_enums_pb2.ASTForeignKeyActionsEnums.Action, str]] = ...) -> None: ...

class ASTSpannerAlterColumnActionProto(_message.Message):
    __slots__ = ("parent", "column_definition")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    column_definition: ASTColumnDefinitionProto
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., column_definition: _Optional[_Union[ASTColumnDefinitionProto, _Mapping]] = ...) -> None: ...

class ASTSpannerSetOnDeleteActionProto(_message.Message):
    __slots__ = ("parent", "action")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterActionProto
    action: _ast_enums_pb2.ASTForeignKeyActionsEnums.Action
    def __init__(self, parent: _Optional[_Union[ASTAlterActionProto, _Mapping]] = ..., action: _Optional[_Union[_ast_enums_pb2.ASTForeignKeyActionsEnums.Action, str]] = ...) -> None: ...

class ASTRangeLiteralProto(_message.Message):
    __slots__ = ("parent", "type", "range_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    type: ASTRangeTypeProto
    range_value: ASTStringLiteralProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., type: _Optional[_Union[ASTRangeTypeProto, _Mapping]] = ..., range_value: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ...) -> None: ...

class ASTRangeTypeProto(_message.Message):
    __slots__ = ("parent", "element_type", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    element_type: AnyASTTypeProto
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., element_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTCreatePropertyGraphStatementProto(_message.Message):
    __slots__ = ("parent", "name", "node_table_list", "edge_table_list", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    node_table_list: ASTGraphElementTableListProto
    edge_table_list: ASTGraphElementTableListProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., node_table_list: _Optional[_Union[ASTGraphElementTableListProto, _Mapping]] = ..., edge_table_list: _Optional[_Union[ASTGraphElementTableListProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTGraphElementTableListProto(_message.Message):
    __slots__ = ("parent", "element_tables")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TABLES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    element_tables: _containers.RepeatedCompositeFieldContainer[ASTGraphElementTableProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., element_tables: _Optional[_Iterable[_Union[ASTGraphElementTableProto, _Mapping]]] = ...) -> None: ...

class ASTGraphElementTableProto(_message.Message):
    __slots__ = ("parent", "name", "alias", "key_list", "source_node_reference", "dest_node_reference", "label_properties_list", "dynamic_label", "dynamic_properties")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DEST_NODE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    LABEL_PROPERTIES_LIST_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LABEL_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTPathExpressionProto
    alias: ASTAliasProto
    key_list: ASTColumnListProto
    source_node_reference: ASTGraphNodeTableReferenceProto
    dest_node_reference: ASTGraphNodeTableReferenceProto
    label_properties_list: ASTGraphElementLabelAndPropertiesListProto
    dynamic_label: ASTGraphDynamicLabelProto
    dynamic_properties: ASTGraphDynamicPropertiesProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., key_list: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., source_node_reference: _Optional[_Union[ASTGraphNodeTableReferenceProto, _Mapping]] = ..., dest_node_reference: _Optional[_Union[ASTGraphNodeTableReferenceProto, _Mapping]] = ..., label_properties_list: _Optional[_Union[ASTGraphElementLabelAndPropertiesListProto, _Mapping]] = ..., dynamic_label: _Optional[_Union[ASTGraphDynamicLabelProto, _Mapping]] = ..., dynamic_properties: _Optional[_Union[ASTGraphDynamicPropertiesProto, _Mapping]] = ...) -> None: ...

class ASTGraphNodeTableReferenceProto(_message.Message):
    __slots__ = ("parent", "node_table_identifier", "edge_table_columns", "node_table_columns", "node_reference_type")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EDGE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NODE_TABLE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NODE_REFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    node_table_identifier: ASTIdentifierProto
    edge_table_columns: ASTColumnListProto
    node_table_columns: ASTColumnListProto
    node_reference_type: _ast_enums_pb2.ASTGraphNodeTableReferenceEnums.NodeReferenceType
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., node_table_identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., edge_table_columns: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., node_table_columns: _Optional[_Union[ASTColumnListProto, _Mapping]] = ..., node_reference_type: _Optional[_Union[_ast_enums_pb2.ASTGraphNodeTableReferenceEnums.NodeReferenceType, str]] = ...) -> None: ...

class ASTGraphElementLabelAndPropertiesListProto(_message.Message):
    __slots__ = ("parent", "label_properties_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_PROPERTIES_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    label_properties_list: _containers.RepeatedCompositeFieldContainer[ASTGraphElementLabelAndPropertiesProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., label_properties_list: _Optional[_Iterable[_Union[ASTGraphElementLabelAndPropertiesProto, _Mapping]]] = ...) -> None: ...

class ASTGraphElementLabelAndPropertiesProto(_message.Message):
    __slots__ = ("parent", "label_name", "properties", "label_options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABEL_OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    label_name: ASTIdentifierProto
    properties: ASTGraphPropertiesProto
    label_options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., label_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., properties: _Optional[_Union[ASTGraphPropertiesProto, _Mapping]] = ..., label_options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTGraphDerivedPropertyProto(_message.Message):
    __slots__ = ("parent", "expression", "alias", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    expression: AnyASTExpressionProto
    alias: ASTAliasProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTGraphDerivedPropertyListProto(_message.Message):
    __slots__ = ("parent", "properties")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    properties: _containers.RepeatedCompositeFieldContainer[ASTGraphDerivedPropertyProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., properties: _Optional[_Iterable[_Union[ASTGraphDerivedPropertyProto, _Mapping]]] = ...) -> None: ...

class ASTGraphPropertiesProto(_message.Message):
    __slots__ = ("parent", "no_properties", "derived_property_list", "all_except_columns")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NO_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DERIVED_PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    ALL_EXCEPT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    no_properties: bool
    derived_property_list: ASTGraphDerivedPropertyListProto
    all_except_columns: ASTColumnListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., no_properties: bool = ..., derived_property_list: _Optional[_Union[ASTGraphDerivedPropertyListProto, _Mapping]] = ..., all_except_columns: _Optional[_Union[ASTColumnListProto, _Mapping]] = ...) -> None: ...

class ASTGraphDynamicLabelProto(_message.Message):
    __slots__ = ("parent", "label")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    label: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., label: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphDynamicPropertiesProto(_message.Message):
    __slots__ = ("parent", "properties")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    properties: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., properties: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphPatternProto(_message.Message):
    __slots__ = ("parent", "paths", "where_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    paths: _containers.RepeatedCompositeFieldContainer[ASTGraphPathPatternProto]
    where_clause: ASTWhereClauseProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., paths: _Optional[_Iterable[_Union[ASTGraphPathPatternProto, _Mapping]]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ...) -> None: ...

class ASTGqlQueryProto(_message.Message):
    __slots__ = ("parent", "graph_table")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_TABLE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    graph_table: ASTGraphTableQueryProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., graph_table: _Optional[_Union[ASTGraphTableQueryProto, _Mapping]] = ...) -> None: ...

class ASTGqlGraphPatternQueryProto(_message.Message):
    __slots__ = ("parent", "graph_reference", "graph_pattern")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    graph_reference: ASTPathExpressionProto
    graph_pattern: ASTGraphPatternProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., graph_reference: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., graph_pattern: _Optional[_Union[ASTGraphPatternProto, _Mapping]] = ...) -> None: ...

class ASTGqlLinearOpsQueryProto(_message.Message):
    __slots__ = ("parent", "graph_reference", "linear_ops")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    LINEAR_OPS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTQueryExpressionProto
    graph_reference: ASTPathExpressionProto
    linear_ops: ASTGqlOperatorListProto
    def __init__(self, parent: _Optional[_Union[ASTQueryExpressionProto, _Mapping]] = ..., graph_reference: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., linear_ops: _Optional[_Union[ASTGqlOperatorListProto, _Mapping]] = ...) -> None: ...

class ASTGraphTableQueryProto(_message.Message):
    __slots__ = ("parent", "graph_reference", "graph_op", "graph_table_shape", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_OP_FIELD_NUMBER: _ClassVar[int]
    GRAPH_TABLE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTableExpressionProto
    graph_reference: ASTPathExpressionProto
    graph_op: AnyASTGqlOperatorProto
    graph_table_shape: ASTSelectListProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTTableExpressionProto, _Mapping]] = ..., graph_reference: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., graph_op: _Optional[_Union[AnyASTGqlOperatorProto, _Mapping]] = ..., graph_table_shape: _Optional[_Union[ASTSelectListProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class AnyASTGraphLabelExpressionProto(_message.Message):
    __slots__ = ("ast_graph_element_label_node", "ast_graph_wildcard_label_node", "ast_graph_label_operation_node")
    AST_GRAPH_ELEMENT_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_WILDCARD_LABEL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_LABEL_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_graph_element_label_node: ASTGraphElementLabelProto
    ast_graph_wildcard_label_node: ASTGraphWildcardLabelProto
    ast_graph_label_operation_node: ASTGraphLabelOperationProto
    def __init__(self, ast_graph_element_label_node: _Optional[_Union[ASTGraphElementLabelProto, _Mapping]] = ..., ast_graph_wildcard_label_node: _Optional[_Union[ASTGraphWildcardLabelProto, _Mapping]] = ..., ast_graph_label_operation_node: _Optional[_Union[ASTGraphLabelOperationProto, _Mapping]] = ...) -> None: ...

class ASTGraphLabelExpressionProto(_message.Message):
    __slots__ = ("parent", "parenthesized")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    parenthesized: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., parenthesized: bool = ...) -> None: ...

class ASTGraphElementLabelProto(_message.Message):
    __slots__ = ("parent", "name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphLabelExpressionProto
    name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTGraphLabelExpressionProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class ASTGraphWildcardLabelProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphLabelExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTGraphLabelExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphLabelOperationProto(_message.Message):
    __slots__ = ("parent", "op_type", "inputs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphLabelExpressionProto
    op_type: _ast_enums_pb2.ASTGraphLabelOperationEnums.OperationType
    inputs: _containers.RepeatedCompositeFieldContainer[AnyASTGraphLabelExpressionProto]
    def __init__(self, parent: _Optional[_Union[ASTGraphLabelExpressionProto, _Mapping]] = ..., op_type: _Optional[_Union[_ast_enums_pb2.ASTGraphLabelOperationEnums.OperationType, str]] = ..., inputs: _Optional[_Iterable[_Union[AnyASTGraphLabelExpressionProto, _Mapping]]] = ...) -> None: ...

class ASTGraphLabelFilterProto(_message.Message):
    __slots__ = ("parent", "label_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    label_expression: AnyASTGraphLabelExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., label_expression: _Optional[_Union[AnyASTGraphLabelExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphIsLabeledPredicateProto(_message.Message):
    __slots__ = ("parent", "is_not", "operand", "label_expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FIELD_NUMBER: _ClassVar[int]
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    is_not: bool
    operand: AnyASTExpressionProto
    label_expression: AnyASTGraphLabelExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., is_not: bool = ..., operand: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., label_expression: _Optional[_Union[AnyASTGraphLabelExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphElementPatternFillerProto(_message.Message):
    __slots__ = ("parent", "variable_name", "label_filter", "where_clause", "property_specification", "hint", "edge_cost")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FILTER_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    EDGE_COST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    variable_name: ASTIdentifierProto
    label_filter: ASTGraphLabelFilterProto
    where_clause: ASTWhereClauseProto
    property_specification: ASTGraphPropertySpecificationProto
    hint: ASTHintProto
    edge_cost: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., variable_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., label_filter: _Optional[_Union[ASTGraphLabelFilterProto, _Mapping]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ..., property_specification: _Optional[_Union[ASTGraphPropertySpecificationProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., edge_cost: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphPropertySpecificationProto(_message.Message):
    __slots__ = ("parent", "property_name_and_value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_AND_VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    property_name_and_value: _containers.RepeatedCompositeFieldContainer[ASTGraphPropertyNameAndValueProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., property_name_and_value: _Optional[_Iterable[_Union[ASTGraphPropertyNameAndValueProto, _Mapping]]] = ...) -> None: ...

class ASTGraphPropertyNameAndValueProto(_message.Message):
    __slots__ = ("parent", "property_name", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    property_name: ASTIdentifierProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., property_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class AnyASTGraphPathBaseProto(_message.Message):
    __slots__ = ("ast_graph_element_pattern_node", "ast_graph_path_pattern_node")
    AST_GRAPH_ELEMENT_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_PATH_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_graph_element_pattern_node: AnyASTGraphElementPatternProto
    ast_graph_path_pattern_node: ASTGraphPathPatternProto
    def __init__(self, ast_graph_element_pattern_node: _Optional[_Union[AnyASTGraphElementPatternProto, _Mapping]] = ..., ast_graph_path_pattern_node: _Optional[_Union[ASTGraphPathPatternProto, _Mapping]] = ...) -> None: ...

class ASTGraphPathBaseProto(_message.Message):
    __slots__ = ("parent", "quantifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUANTIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    quantifier: AnyASTQuantifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., quantifier: _Optional[_Union[AnyASTQuantifierProto, _Mapping]] = ...) -> None: ...

class AnyASTGraphElementPatternProto(_message.Message):
    __slots__ = ("ast_graph_node_pattern_node", "ast_graph_edge_pattern_node")
    AST_GRAPH_NODE_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GRAPH_EDGE_PATTERN_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_graph_node_pattern_node: ASTGraphNodePatternProto
    ast_graph_edge_pattern_node: ASTGraphEdgePatternProto
    def __init__(self, ast_graph_node_pattern_node: _Optional[_Union[ASTGraphNodePatternProto, _Mapping]] = ..., ast_graph_edge_pattern_node: _Optional[_Union[ASTGraphEdgePatternProto, _Mapping]] = ...) -> None: ...

class ASTGraphElementPatternProto(_message.Message):
    __slots__ = ("parent", "filler")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILLER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphPathBaseProto
    filler: ASTGraphElementPatternFillerProto
    def __init__(self, parent: _Optional[_Union[ASTGraphPathBaseProto, _Mapping]] = ..., filler: _Optional[_Union[ASTGraphElementPatternFillerProto, _Mapping]] = ...) -> None: ...

class ASTGraphNodePatternProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphElementPatternProto
    def __init__(self, parent: _Optional[_Union[ASTGraphElementPatternProto, _Mapping]] = ...) -> None: ...

class ASTGraphLhsHintProto(_message.Message):
    __slots__ = ("parent", "hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    hint: ASTHintProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ...) -> None: ...

class ASTGraphRhsHintProto(_message.Message):
    __slots__ = ("parent", "hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    hint: ASTHintProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ...) -> None: ...

class ASTGraphPathSearchPrefixProto(_message.Message):
    __slots__ = ("parent", "type", "path_count")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_COUNT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    type: _ast_enums_pb2.ASTGraphPathSearchPrefixEnums.PathSearchPrefixType
    path_count: ASTGraphPathSearchPrefixCountProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., type: _Optional[_Union[_ast_enums_pb2.ASTGraphPathSearchPrefixEnums.PathSearchPrefixType, str]] = ..., path_count: _Optional[_Union[ASTGraphPathSearchPrefixCountProto, _Mapping]] = ...) -> None: ...

class ASTGraphPathSearchPrefixCountProto(_message.Message):
    __slots__ = ("parent", "path_count")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_COUNT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    path_count: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., path_count: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGraphEdgePatternProto(_message.Message):
    __slots__ = ("parent", "orientation", "lhs_hint", "rhs_hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    LHS_HINT_FIELD_NUMBER: _ClassVar[int]
    RHS_HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphElementPatternProto
    orientation: _ast_enums_pb2.ASTGraphEdgePatternEnums.EdgeOrientation
    lhs_hint: ASTGraphLhsHintProto
    rhs_hint: ASTGraphRhsHintProto
    def __init__(self, parent: _Optional[_Union[ASTGraphElementPatternProto, _Mapping]] = ..., orientation: _Optional[_Union[_ast_enums_pb2.ASTGraphEdgePatternEnums.EdgeOrientation, str]] = ..., lhs_hint: _Optional[_Union[ASTGraphLhsHintProto, _Mapping]] = ..., rhs_hint: _Optional[_Union[ASTGraphRhsHintProto, _Mapping]] = ...) -> None: ...

class ASTGraphPathModeProto(_message.Message):
    __slots__ = ("parent", "path_mode")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_MODE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    path_mode: _ast_enums_pb2.ASTGraphPathModeEnums.PathMode
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., path_mode: _Optional[_Union[_ast_enums_pb2.ASTGraphPathModeEnums.PathMode, str]] = ...) -> None: ...

class ASTGraphPathPatternProto(_message.Message):
    __slots__ = ("parent", "hint", "where_clause", "path_mode", "input_pattern_list", "parenthesized", "search_prefix", "path_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    PATH_MODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_PATTERN_LIST_FIELD_NUMBER: _ClassVar[int]
    PARENTHESIZED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PATH_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGraphPathBaseProto
    hint: ASTHintProto
    where_clause: ASTWhereClauseProto
    path_mode: ASTGraphPathModeProto
    input_pattern_list: _containers.RepeatedCompositeFieldContainer[AnyASTGraphPathBaseProto]
    parenthesized: bool
    search_prefix: ASTGraphPathSearchPrefixProto
    path_name: ASTIdentifierProto
    def __init__(self, parent: _Optional[_Union[ASTGraphPathBaseProto, _Mapping]] = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ..., where_clause: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ..., path_mode: _Optional[_Union[ASTGraphPathModeProto, _Mapping]] = ..., input_pattern_list: _Optional[_Iterable[_Union[AnyASTGraphPathBaseProto, _Mapping]]] = ..., parenthesized: bool = ..., search_prefix: _Optional[_Union[ASTGraphPathSearchPrefixProto, _Mapping]] = ..., path_name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ...) -> None: ...

class AnyASTGqlOperatorProto(_message.Message):
    __slots__ = ("ast_gql_match_node", "ast_gql_return_node", "ast_gql_operator_list_node", "ast_gql_let_node", "ast_gql_filter_node", "ast_gql_order_by_and_page_node", "ast_gql_set_operation_node", "ast_gql_with_node", "ast_gql_for_node", "ast_gql_sample_node", "ast_gql_call_base_node")
    AST_GQL_MATCH_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_RETURN_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_OPERATOR_LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_LET_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_FILTER_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_ORDER_BY_AND_PAGE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_SET_OPERATION_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_WITH_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_FOR_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_SAMPLE_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_CALL_BASE_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_gql_match_node: ASTGqlMatchProto
    ast_gql_return_node: ASTGqlReturnProto
    ast_gql_operator_list_node: ASTGqlOperatorListProto
    ast_gql_let_node: ASTGqlLetProto
    ast_gql_filter_node: ASTGqlFilterProto
    ast_gql_order_by_and_page_node: ASTGqlOrderByAndPageProto
    ast_gql_set_operation_node: ASTGqlSetOperationProto
    ast_gql_with_node: ASTGqlWithProto
    ast_gql_for_node: ASTGqlForProto
    ast_gql_sample_node: ASTGqlSampleProto
    ast_gql_call_base_node: AnyASTGqlCallBaseProto
    def __init__(self, ast_gql_match_node: _Optional[_Union[ASTGqlMatchProto, _Mapping]] = ..., ast_gql_return_node: _Optional[_Union[ASTGqlReturnProto, _Mapping]] = ..., ast_gql_operator_list_node: _Optional[_Union[ASTGqlOperatorListProto, _Mapping]] = ..., ast_gql_let_node: _Optional[_Union[ASTGqlLetProto, _Mapping]] = ..., ast_gql_filter_node: _Optional[_Union[ASTGqlFilterProto, _Mapping]] = ..., ast_gql_order_by_and_page_node: _Optional[_Union[ASTGqlOrderByAndPageProto, _Mapping]] = ..., ast_gql_set_operation_node: _Optional[_Union[ASTGqlSetOperationProto, _Mapping]] = ..., ast_gql_with_node: _Optional[_Union[ASTGqlWithProto, _Mapping]] = ..., ast_gql_for_node: _Optional[_Union[ASTGqlForProto, _Mapping]] = ..., ast_gql_sample_node: _Optional[_Union[ASTGqlSampleProto, _Mapping]] = ..., ast_gql_call_base_node: _Optional[_Union[AnyASTGqlCallBaseProto, _Mapping]] = ...) -> None: ...

class ASTGqlOperatorProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ...) -> None: ...

class ASTGqlMatchProto(_message.Message):
    __slots__ = ("parent", "graph_pattern", "optional", "hint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    graph_pattern: ASTGraphPatternProto
    optional: bool
    hint: ASTHintProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., graph_pattern: _Optional[_Union[ASTGraphPatternProto, _Mapping]] = ..., optional: bool = ..., hint: _Optional[_Union[ASTHintProto, _Mapping]] = ...) -> None: ...

class ASTGqlReturnProto(_message.Message):
    __slots__ = ("parent", "select", "order_by_page")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_PAGE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    select: ASTSelectProto
    order_by_page: ASTGqlOrderByAndPageProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ..., order_by_page: _Optional[_Union[ASTGqlOrderByAndPageProto, _Mapping]] = ...) -> None: ...

class ASTGqlWithProto(_message.Message):
    __slots__ = ("parent", "select")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SELECT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    select: ASTSelectProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., select: _Optional[_Union[ASTSelectProto, _Mapping]] = ...) -> None: ...

class ASTGqlForProto(_message.Message):
    __slots__ = ("parent", "identifier", "expression", "with_offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    WITH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    identifier: ASTIdentifierProto
    expression: AnyASTExpressionProto
    with_offset: ASTWithOffsetProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ..., with_offset: _Optional[_Union[ASTWithOffsetProto, _Mapping]] = ...) -> None: ...

class AnyASTGqlCallBaseProto(_message.Message):
    __slots__ = ("ast_gql_named_call_node", "ast_gql_inline_subquery_call_node")
    AST_GQL_NAMED_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    AST_GQL_INLINE_SUBQUERY_CALL_NODE_FIELD_NUMBER: _ClassVar[int]
    ast_gql_named_call_node: ASTGqlNamedCallProto
    ast_gql_inline_subquery_call_node: ASTGqlInlineSubqueryCallProto
    def __init__(self, ast_gql_named_call_node: _Optional[_Union[ASTGqlNamedCallProto, _Mapping]] = ..., ast_gql_inline_subquery_call_node: _Optional[_Union[ASTGqlInlineSubqueryCallProto, _Mapping]] = ...) -> None: ...

class ASTGqlCallBaseProto(_message.Message):
    __slots__ = ("parent", "optional", "is_partitioning", "name_capture_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    IS_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    NAME_CAPTURE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    optional: bool
    is_partitioning: bool
    name_capture_list: ASTIdentifierListProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., optional: bool = ..., is_partitioning: bool = ..., name_capture_list: _Optional[_Union[ASTIdentifierListProto, _Mapping]] = ...) -> None: ...

class ASTGqlNamedCallProto(_message.Message):
    __slots__ = ("parent", "tvf_call", "yield_clause")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TVF_CALL_FIELD_NUMBER: _ClassVar[int]
    YIELD_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlCallBaseProto
    tvf_call: ASTTVFProto
    yield_clause: ASTYieldItemListProto
    def __init__(self, parent: _Optional[_Union[ASTGqlCallBaseProto, _Mapping]] = ..., tvf_call: _Optional[_Union[ASTTVFProto, _Mapping]] = ..., yield_clause: _Optional[_Union[ASTYieldItemListProto, _Mapping]] = ...) -> None: ...

class ASTYieldItemListProto(_message.Message):
    __slots__ = ("parent", "yield_items")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    YIELD_ITEMS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    yield_items: _containers.RepeatedCompositeFieldContainer[ASTExpressionWithOptAliasProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., yield_items: _Optional[_Iterable[_Union[ASTExpressionWithOptAliasProto, _Mapping]]] = ...) -> None: ...

class ASTGqlInlineSubqueryCallProto(_message.Message):
    __slots__ = ("parent", "subquery")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlCallBaseProto
    subquery: ASTQueryProto
    def __init__(self, parent: _Optional[_Union[ASTGqlCallBaseProto, _Mapping]] = ..., subquery: _Optional[_Union[ASTQueryProto, _Mapping]] = ...) -> None: ...

class ASTGqlLetProto(_message.Message):
    __slots__ = ("parent", "variable_definition_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_DEFINITION_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    variable_definition_list: ASTGqlLetVariableDefinitionListProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., variable_definition_list: _Optional[_Union[ASTGqlLetVariableDefinitionListProto, _Mapping]] = ...) -> None: ...

class ASTGqlLetVariableDefinitionListProto(_message.Message):
    __slots__ = ("parent", "variable_definitions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    variable_definitions: _containers.RepeatedCompositeFieldContainer[ASTGqlLetVariableDefinitionProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., variable_definitions: _Optional[_Iterable[_Union[ASTGqlLetVariableDefinitionProto, _Mapping]]] = ...) -> None: ...

class ASTGqlLetVariableDefinitionProto(_message.Message):
    __slots__ = ("parent", "identifier", "expression")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier: ASTIdentifierProto
    expression: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., expression: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGqlFilterProto(_message.Message):
    __slots__ = ("parent", "condition")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    condition: ASTWhereClauseProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., condition: _Optional[_Union[ASTWhereClauseProto, _Mapping]] = ...) -> None: ...

class ASTGqlOperatorListProto(_message.Message):
    __slots__ = ("parent", "operators")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OPERATORS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    operators: _containers.RepeatedCompositeFieldContainer[AnyASTGqlOperatorProto]
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., operators: _Optional[_Iterable[_Union[AnyASTGqlOperatorProto, _Mapping]]] = ...) -> None: ...

class ASTGqlSetOperationProto(_message.Message):
    __slots__ = ("parent", "metadata", "inputs")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    metadata: ASTSetOperationMetadataListProto
    inputs: _containers.RepeatedCompositeFieldContainer[AnyASTGqlOperatorProto]
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., metadata: _Optional[_Union[ASTSetOperationMetadataListProto, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[AnyASTGqlOperatorProto, _Mapping]]] = ...) -> None: ...

class ASTGqlPageLimitProto(_message.Message):
    __slots__ = ("parent", "limit")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    limit: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., limit: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGqlPageOffsetProto(_message.Message):
    __slots__ = ("parent", "offset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    offset: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., offset: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTGqlPageProto(_message.Message):
    __slots__ = ("parent", "offset", "limit")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    offset: ASTGqlPageOffsetProto
    limit: ASTGqlPageLimitProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., offset: _Optional[_Union[ASTGqlPageOffsetProto, _Mapping]] = ..., limit: _Optional[_Union[ASTGqlPageLimitProto, _Mapping]] = ...) -> None: ...

class ASTGqlOrderByAndPageProto(_message.Message):
    __slots__ = ("parent", "order_by", "page")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    order_by: ASTOrderByProto
    page: ASTGqlPageProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., order_by: _Optional[_Union[ASTOrderByProto, _Mapping]] = ..., page: _Optional[_Union[ASTGqlPageProto, _Mapping]] = ...) -> None: ...

class ASTGqlSampleProto(_message.Message):
    __slots__ = ("parent", "sample")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTGqlOperatorProto
    sample: ASTSampleClauseProto
    def __init__(self, parent: _Optional[_Union[ASTGqlOperatorProto, _Mapping]] = ..., sample: _Optional[_Union[ASTSampleClauseProto, _Mapping]] = ...) -> None: ...

class ASTSelectWithProto(_message.Message):
    __slots__ = ("parent", "identifier", "options")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    identifier: ASTIdentifierProto
    options: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., identifier: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTColumnWithOptionsProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    name: ASTIdentifierProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTColumnWithOptionsListProto(_message.Message):
    __slots__ = ("parent", "column_with_options")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_WITH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    column_with_options: _containers.RepeatedCompositeFieldContainer[ASTColumnWithOptionsProto]
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., column_with_options: _Optional[_Iterable[_Union[ASTColumnWithOptionsProto, _Mapping]]] = ...) -> None: ...

class ASTMacroBodyProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPrintableLeafProto
    def __init__(self, parent: _Optional[_Union[ASTPrintableLeafProto, _Mapping]] = ...) -> None: ...

class ASTDefineMacroStatementProto(_message.Message):
    __slots__ = ("parent", "name", "body")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    name: ASTIdentifierProto
    body: ASTMacroBodyProto
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTIdentifierProto, _Mapping]] = ..., body: _Optional[_Union[ASTMacroBodyProto, _Mapping]] = ...) -> None: ...

class ASTUndropStatementProto(_message.Message):
    __slots__ = ("parent", "schema_object_kind", "name", "is_if_not_exists", "for_system_time", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_OBJECT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    FOR_SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTDdlStatementProto
    schema_object_kind: _ast_enums_pb2.SchemaObjectKind
    name: ASTPathExpressionProto
    is_if_not_exists: bool
    for_system_time: ASTForSystemTimeProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTDdlStatementProto, _Mapping]] = ..., schema_object_kind: _Optional[_Union[_ast_enums_pb2.SchemaObjectKind, str]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., is_if_not_exists: bool = ..., for_system_time: _Optional[_Union[ASTForSystemTimeProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTIdentityColumnInfoProto(_message.Message):
    __slots__ = ("parent", "start_with_value", "increment_by_value", "max_value", "min_value", "cycling_enabled")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_WITH_VALUE_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_BY_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    CYCLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    start_with_value: ASTIdentityColumnStartWithProto
    increment_by_value: ASTIdentityColumnIncrementByProto
    max_value: ASTIdentityColumnMaxValueProto
    min_value: ASTIdentityColumnMinValueProto
    cycling_enabled: bool
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., start_with_value: _Optional[_Union[ASTIdentityColumnStartWithProto, _Mapping]] = ..., increment_by_value: _Optional[_Union[ASTIdentityColumnIncrementByProto, _Mapping]] = ..., max_value: _Optional[_Union[ASTIdentityColumnMaxValueProto, _Mapping]] = ..., min_value: _Optional[_Union[ASTIdentityColumnMinValueProto, _Mapping]] = ..., cycling_enabled: bool = ...) -> None: ...

class ASTIdentityColumnStartWithProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTIdentityColumnIncrementByProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTIdentityColumnMaxValueProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTIdentityColumnMinValueProto(_message.Message):
    __slots__ = ("parent", "value")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    value: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., value: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTAliasedQueryModifiersProto(_message.Message):
    __slots__ = ("parent", "recursion_depth_modifier")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RECURSION_DEPTH_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    recursion_depth_modifier: ASTRecursionDepthModifierProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., recursion_depth_modifier: _Optional[_Union[ASTRecursionDepthModifierProto, _Mapping]] = ...) -> None: ...

class ASTIntOrUnboundedProto(_message.Message):
    __slots__ = ("parent", "bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTExpressionProto
    bound: AnyASTExpressionProto
    def __init__(self, parent: _Optional[_Union[ASTExpressionProto, _Mapping]] = ..., bound: _Optional[_Union[AnyASTExpressionProto, _Mapping]] = ...) -> None: ...

class ASTRecursionDepthModifierProto(_message.Message):
    __slots__ = ("parent", "alias", "lower_bound", "upper_bound")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    alias: ASTAliasProto
    lower_bound: ASTIntOrUnboundedProto
    upper_bound: ASTIntOrUnboundedProto
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ..., lower_bound: _Optional[_Union[ASTIntOrUnboundedProto, _Mapping]] = ..., upper_bound: _Optional[_Union[ASTIntOrUnboundedProto, _Mapping]] = ...) -> None: ...

class ASTMapTypeProto(_message.Message):
    __slots__ = ("parent", "key_type", "value_type", "type_parameters", "collate")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    COLLATE_FIELD_NUMBER: _ClassVar[int]
    parent: ASTTypeProto
    key_type: AnyASTTypeProto
    value_type: AnyASTTypeProto
    type_parameters: ASTTypeParameterListProto
    collate: ASTCollateProto
    def __init__(self, parent: _Optional[_Union[ASTTypeProto, _Mapping]] = ..., key_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., value_type: _Optional[_Union[AnyASTTypeProto, _Mapping]] = ..., type_parameters: _Optional[_Union[ASTTypeParameterListProto, _Mapping]] = ..., collate: _Optional[_Union[ASTCollateProto, _Mapping]] = ...) -> None: ...

class ASTLockModeProto(_message.Message):
    __slots__ = ("parent", "strength")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    parent: ASTNodeProto
    strength: _ast_enums_pb2.ASTLockModeEnums.LockStrengthSpec
    def __init__(self, parent: _Optional[_Union[ASTNodeProto, _Mapping]] = ..., strength: _Optional[_Union[_ast_enums_pb2.ASTLockModeEnums.LockStrengthSpec, str]] = ...) -> None: ...

class ASTPipeRecursiveUnionProto(_message.Message):
    __slots__ = ("parent", "metadata", "recursion_depth_modifier", "input_subpipeline", "input_subquery", "alias")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RECURSION_DEPTH_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    INPUT_SUBPIPELINE_FIELD_NUMBER: _ClassVar[int]
    INPUT_SUBQUERY_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTPipeOperatorProto
    metadata: ASTSetOperationMetadataProto
    recursion_depth_modifier: ASTRecursionDepthModifierProto
    input_subpipeline: ASTSubpipelineProto
    input_subquery: AnyASTQueryExpressionProto
    alias: ASTAliasProto
    def __init__(self, parent: _Optional[_Union[ASTPipeOperatorProto, _Mapping]] = ..., metadata: _Optional[_Union[ASTSetOperationMetadataProto, _Mapping]] = ..., recursion_depth_modifier: _Optional[_Union[ASTRecursionDepthModifierProto, _Mapping]] = ..., input_subpipeline: _Optional[_Union[ASTSubpipelineProto, _Mapping]] = ..., input_subquery: _Optional[_Union[AnyASTQueryExpressionProto, _Mapping]] = ..., alias: _Optional[_Union[ASTAliasProto, _Mapping]] = ...) -> None: ...

class ASTRunStatementProto(_message.Message):
    __slots__ = ("parent", "target_path_expression", "target_string_literal", "arguments")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_STRING_LITERAL_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    parent: ASTStatementProto
    target_path_expression: ASTPathExpressionProto
    target_string_literal: ASTStringLiteralProto
    arguments: _containers.RepeatedCompositeFieldContainer[ASTNamedArgumentProto]
    def __init__(self, parent: _Optional[_Union[ASTStatementProto, _Mapping]] = ..., target_path_expression: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., target_string_literal: _Optional[_Union[ASTStringLiteralProto, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[ASTNamedArgumentProto, _Mapping]]] = ...) -> None: ...

class ASTCreateSequenceStatementProto(_message.Message):
    __slots__ = ("parent", "name", "options_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: ASTCreateStatementProto
    name: ASTPathExpressionProto
    options_list: ASTOptionsListProto
    def __init__(self, parent: _Optional[_Union[ASTCreateStatementProto, _Mapping]] = ..., name: _Optional[_Union[ASTPathExpressionProto, _Mapping]] = ..., options_list: _Optional[_Union[ASTOptionsListProto, _Mapping]] = ...) -> None: ...

class ASTAlterSequenceStatementProto(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: ASTAlterStatementBaseProto
    def __init__(self, parent: _Optional[_Union[ASTAlterStatementBaseProto, _Mapping]] = ...) -> None: ...
