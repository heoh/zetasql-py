"""
Tests for wrapper_utils module
"""

import pytest
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.types import parse_proto, proto_models


class TestFromProto:
    """Tests for ProtoModel.from_proto classmethod"""
    
    def test_concrete_class_from_proto(self):
        """Concrete wrapper classes should create instances via from_proto"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = parse_proto(proto)
        
        assert isinstance(wrapper, proto_models.ResolvedLiteral)
    
    def test_from_proto_does_not_resolve_unions(self):
        """from_proto() should NOT auto-resolve union types (that's parse_wrapper's job)"""
        
        # Create a TableScan proto
        table_scan_proto = resolved_ast_pb2.ResolvedTableScanProto()
        
        # Wrap it in AnyResolvedScan (union type)
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        any_scan_proto.resolved_table_scan_node.CopyFrom(table_scan_proto)
        
        # Calling from_proto on union class should NOT resolve - just wrap
        wrapper = proto_models.AnyResolvedScan.from_proto(any_scan_proto)
        
        # Should stay as AnyResolvedScan, not resolve to concrete
        assert isinstance(wrapper, proto_models.AnyResolvedScan)


class TestParseWrapper:
    """Tests for parse_wrapper function"""
    
    def test_parses_concrete_proto(self):
        """parse_wrapper should wrap concrete proto types"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = parse_proto(proto)
        
        assert isinstance(wrapper, proto_models.ResolvedLiteral)
    
    def test_resolves_union_proto_to_concrete(self):
        """parse_wrapper should resolve union protos to concrete types"""
        
        # Create a TableScan proto
        table_scan_proto = resolved_ast_pb2.ResolvedTableScanProto()
        
        # Wrap it in AnyResolvedScan (union type)
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        any_scan_proto.resolved_table_scan_node.CopyFrom(table_scan_proto)
        
        wrapper = parse_proto(any_scan_proto)
        
        # Should resolve to the concrete type
        assert isinstance(wrapper, proto_models.ResolvedTableScan)
    
    def test_idempotent_on_same_proto(self):
        """Calling parse_wrapper multiple times on same proto should yield equivalent results"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        
        wrapper1 = parse_proto(proto)
        wrapper2 = parse_proto(proto)
        wrapper3 = parse_proto(proto)
        
        # All should be the same type and reference the same proto
        assert type(wrapper1) == type(wrapper2) == type(wrapper3)
    
    def test_handles_empty_union(self):
        """parse_wrapper should handle union protos with no variant set"""
        
        # Create empty AnyResolvedScan (no variant set)
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        
        wrapper = parse_proto(any_scan_proto)
        
        # Should create AnyResolvedScan wrapper (fallback)
        assert isinstance(wrapper, proto_models.AnyResolvedScan)


class TestAsType:
    """Tests for as_type instance method"""
    
    def test_successful_cast(self):
        """as_type should return self when type matches"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = parse_proto(proto)
        
        result = wrapper.as_type(proto_models.ResolvedLiteral)
        assert result is wrapper
    
    def test_successful_cast_to_parent(self):
        """as_type should work for parent classes"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = parse_proto(proto)
        
        # Should be able to cast to parent types
        as_expr = wrapper.as_type(proto_models.ResolvedExpr)
        assert as_expr is wrapper
        
        as_node = wrapper.as_type(proto_models.ResolvedNode)
        assert as_node is wrapper
    
    def test_failed_cast_raises_typeerror(self):
        """as_type should raise TypeError when type doesn't match"""
        
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        wrapper = parse_proto(proto)
        
        with pytest.raises(TypeError) as exc_info:
            wrapper.as_type(proto_models.ResolvedTableScan)
        
        assert "Cannot cast ResolvedLiteral to ResolvedTableScan" in str(exc_info.value)
    
    def test_use_case_after_isinstance_check(self):
        """as_type is useful after isinstance checks for IDE autocomplete"""
        
        # Create a TableScan
        table_scan_proto = resolved_ast_pb2.ResolvedTableScanProto()
        any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        any_scan_proto.resolved_table_scan_node.CopyFrom(table_scan_proto)
        
        scan = parse_proto(any_scan_proto)
        
        # Use isinstance check + as_type for type narrowing
        if isinstance(scan, proto_models.ResolvedTableScan):
            typed_scan = scan.as_type(proto_models.ResolvedTableScan)
            # Now IDE knows typed_scan is ResolvedTableScan
            assert typed_scan is scan
        else:
            pytest.fail("Expected ResolvedTableScan")

