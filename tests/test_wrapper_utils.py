"""
Tests for wrapper_utils module
"""

import pytest
from zetasql.wrapper_utils import resolve_type, node_kind
from zetasql.resolved_ast_wrapper import WrapperBase


class TestNodeKind:
    """Tests for node_kind function"""
    
    def test_returns_class_name(self):
        """node_kind should return the class name of the wrapper"""
        # Create a simple wrapper for testing
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        from zetasql.resolved_ast_wrapper import ResolvedLiteral
        wrapper = ResolvedLiteral(proto)
        
        assert node_kind(wrapper) == 'ResolvedLiteral'
    
    def test_works_with_any_wrapper(self):
        """node_kind should work with any wrapper type"""
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        from zetasql.resolved_ast_wrapper import ResolvedQueryStmt
        
        proto = resolved_ast_pb2.ResolvedQueryStmtProto()
        wrapper = ResolvedQueryStmt(proto)
        
        assert node_kind(wrapper) == 'ResolvedQueryStmt'


class TestResolveType:
    """Tests for resolve_type function"""
    
    def test_idempotent_on_concrete_type(self):
        """resolve_type should return the same instance for concrete types"""
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        from zetasql.resolved_ast_wrapper import ResolvedLiteral
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = ResolvedLiteral(proto)
        
        # Should return the same instance
        resolved = resolve_type(wrapper)
        assert resolved is wrapper
        assert node_kind(resolved) == 'ResolvedLiteral'
    
    def test_resolves_oneof_to_concrete_type(self):
        """resolve_type should resolve union types to concrete types"""
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        from zetasql.resolved_ast_wrapper import (
            AnyResolvedScan, 
            ResolvedTableScan
        )
        
        # Create a TableScan proto (just need a valid proto)
        table_scan_proto = resolved_ast_pb2.ResolvedTableScanProto()
        
        # Wrap it in AnyResolvedScan (union type)
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        any_scan_proto.resolved_table_scan_node.CopyFrom(table_scan_proto)
        
        any_scan_wrapper = AnyResolvedScan(any_scan_proto)
        
        # Before resolution
        assert node_kind(any_scan_wrapper) == 'AnyResolvedScan'
        
        # After resolution
        resolved = resolve_type(any_scan_wrapper)
        assert node_kind(resolved) == 'ResolvedTableScan'
        assert isinstance(resolved, ResolvedTableScan)
    
    def test_multiple_calls_are_idempotent(self):
        """Calling resolve_type multiple times should be safe"""
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        from zetasql.resolved_ast_wrapper import ResolvedLiteral
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = ResolvedLiteral(proto)
        
        # Multiple calls should all return the same instance
        resolved1 = resolve_type(wrapper)
        resolved2 = resolve_type(resolved1)
        resolved3 = resolve_type(resolved2)
        
        assert resolved1 is wrapper
        assert resolved2 is wrapper
        assert resolved3 is wrapper
    
    def test_returns_original_on_unknown_variant(self):
        """resolve_type should return original if variant is unknown"""
        # Create a wrapper with mock proto that has WhichOneof but unknown field
        from unittest.mock import Mock
        
        mock_proto = Mock()
        mock_proto.WhichOneof.return_value = 'unknown_field_that_does_not_exist'
        
        # Create a simple wrapper
        wrapper = WrapperBase(mock_proto)
        
        # Should return original wrapper without error
        resolved = resolve_type(wrapper)
        assert resolved is wrapper
    
    def test_returns_original_when_no_variant_set(self):
        """resolve_type should return original if no oneof variant is set"""
        from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
        from zetasql.resolved_ast_wrapper import AnyResolvedScan
        
        # Create empty AnyResolvedScan (no variant set)
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        any_scan_wrapper = AnyResolvedScan(any_scan_proto)
        
        # Should return original
        resolved = resolve_type(any_scan_wrapper)
        assert resolved is any_scan_wrapper
        assert node_kind(resolved) == 'AnyResolvedScan'


class TestFieldNameToClassName:
    """Tests for _field_name_to_class_name helper"""
    
    def test_converts_field_names_correctly(self):
        """Test the internal field name to class name conversion"""
        from zetasql.wrapper_utils import _field_name_to_class_name
        
        # Test various field name patterns
        assert _field_name_to_class_name('resolved_filter_scan_node') == 'ResolvedFilterScan'
        assert _field_name_to_class_name('resolved_project_scan_node') == 'ResolvedProjectScan'
        assert _field_name_to_class_name('resolved_table_scan_node') == 'ResolvedTableScan'
        assert _field_name_to_class_name('resolved_literal_node') == 'ResolvedLiteral'
        assert _field_name_to_class_name('resolved_aggregate_scan_node') == 'ResolvedAggregateScan'
