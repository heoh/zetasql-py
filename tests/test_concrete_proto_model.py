"""
Test Concrete (Dataclass-based) ProtoModel

Validates:
- Direct instance creation without proto
- Bidirectional proto conversion (from_proto/to_proto)
- MRO-based parent chain tracking
- Roundtrip consistency
"""

import pytest
from zetasql.types.proto_models import (
    ResolvedNode,
    ResolvedExpr,
    ResolvedLiteral,
    ParseLocationRange,
    Type,
    ValueWithType,
)
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2, value_pb2, parse_location_range_pb2


class TestConcreteProtoModelBasics:
    """Test basic dataclass functionality"""
    
    def test_direct_instance_creation_no_proto(self):
        """Test creating instances directly without proto"""
        # Create without any proto involved
        literal = ResolvedLiteral(
            value=None,
            has_explicit_type=True,
            float_literal_id=123
        )
        
        assert literal.has_explicit_type is True
        assert literal.float_literal_id == 123
        assert literal.value is None
    
    def test_dataclass_features(self):
        """Test that dataclass features work (repr, eq, etc.)"""
        literal1 = ResolvedLiteral(has_explicit_type=True, float_literal_id=42)
        literal2 = ResolvedLiteral(has_explicit_type=True, float_literal_id=42)
        literal3 = ResolvedLiteral(has_explicit_type=False, float_literal_id=42)
        
        # Equality
        assert literal1 == literal2
        assert literal1 != literal3
        
        # Repr should work
        repr_str = repr(literal1)
        assert 'ResolvedLiteral' in repr_str
        assert 'has_explicit_type=True' in repr_str
    
    def test_field_defaults(self):
        """Test that all fields have proper defaults"""
        # Create with no args - should use defaults (now all None)
        literal = ResolvedLiteral()
        
        assert literal.value is None
        assert literal.has_explicit_type is None  # Changed: now Optional
        assert literal.float_literal_id is None  # Changed: now Optional
        assert literal.preserve_in_literal_remover is None  # Changed: now Optional
        
        # Inherited fields should also have defaults
        assert literal.type is None
        assert literal.type_annotation_map is None
        assert literal.parse_location_range is None


class TestProtoConversion:
    """Test bidirectional proto conversion"""
    
    def test_to_proto_simple_fields(self):
        """Test converting simple fields to proto"""
        literal = ResolvedLiteral(
            has_explicit_type=True,
            float_literal_id=456
        )
        
        proto = literal.to_proto()
        
        assert isinstance(proto, resolved_ast_pb2.ResolvedLiteralProto)
        assert proto.has_explicit_type is True
        assert proto.float_literal_id == 456
    
    def test_from_proto_simple_fields(self):
        """Test loading simple fields from proto"""
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        proto.has_explicit_type = True
        proto.float_literal_id = 789
        
        literal = ResolvedLiteral.from_proto(proto)
        
        assert literal.has_explicit_type is True
        assert literal.float_literal_id == 789
    
    def test_roundtrip_simple(self):
        """Test roundtrip conversion preserves data"""
        original = ResolvedLiteral(
            has_explicit_type=True,
            float_literal_id=999,
            preserve_in_literal_remover=True
        )
        
        # Convert to proto and back
        proto = original.to_proto()
        restored = ResolvedLiteral.from_proto(proto)
        
        # Should be equal
        assert restored.has_explicit_type == original.has_explicit_type
        assert restored.float_literal_id == original.float_literal_id
        assert restored.preserve_in_literal_remover == original.preserve_in_literal_remover


class TestParentChainTracking:
    """Test MRO-based parent chain tracking"""
    
    def test_parent_field_to_proto(self):
        """Test that parent fields are placed at proto.parent level"""
        # Create Type (will be at parent level in proto)
        type_obj = Type(type_kind=2)  # INT64
        
        literal = ResolvedLiteral(
            type=type_obj,
            has_explicit_type=True
        )
        
        proto = literal.to_proto()
        
        # type should be at proto.parent.type
        assert proto.parent.type.type_kind == 2
        assert proto.has_explicit_type is True
    
    def test_grandparent_field_to_proto(self):
        """Test that grandparent fields are placed at proto.parent.parent level"""
        loc = ParseLocationRange(start=10, end=20)
        
        literal = ResolvedLiteral(
            parse_location_range=loc,
            has_explicit_type=True
        )
        
        proto = literal.to_proto()
        
        # parse_location_range should be at proto.parent.parent
        assert proto.parent.parent.parse_location_range.start == 10
        assert proto.parent.parent.parse_location_range.end == 20
    
    def test_from_proto_with_parent_chain(self):
        """Test loading fields from proto.parent hierarchy"""
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        proto.has_explicit_type = True
        
        # Set parent field (type)
        proto.parent.type.type_kind = type_pb2.TYPE_STRING
        
        # Set grandparent field (parse_location_range)
        proto.parent.parent.parse_location_range.start = 5
        proto.parent.parent.parse_location_range.end = 15
        
        literal = ResolvedLiteral.from_proto(proto)
        
        # All fields should be populated correctly
        assert literal.has_explicit_type is True
        assert literal.type is not None
        assert literal.type.type_kind == type_pb2.TYPE_STRING
        assert literal.parse_location_range is not None
        assert literal.parse_location_range.start == 5
        assert literal.parse_location_range.end == 15
    
    def test_roundtrip_with_inheritance(self):
        """Test full roundtrip with all inheritance levels"""
        # Create instance with fields from all levels
        original = ResolvedLiteral(
            # Grandparent field (ResolvedNode)
            parse_location_range=ParseLocationRange(start=0, end=100),
            # Parent field (ResolvedExpr)
            type=Type(type_kind=type_pb2.TYPE_INT64),
            # Own fields
            has_explicit_type=True,
            float_literal_id=42
        )
        
        # Roundtrip
        proto = original.to_proto()
        restored = ResolvedLiteral.from_proto(proto)
        
        # Verify all levels
        assert restored.parse_location_range is not None
        assert restored.parse_location_range.start == 0
        assert restored.parse_location_range.end == 100
        
        assert restored.type is not None
        assert restored.type.type_kind == type_pb2.TYPE_INT64
        
        assert restored.has_explicit_type is True
        assert restored.float_literal_id == 42


class TestNestedMessages:
    """Test handling of nested message fields"""
    
    def test_message_field_none(self):
        """Test that None message fields are handled correctly"""
        literal = ResolvedLiteral(
            value=None,  # Explicitly None
            type=None
        )
        
        proto = literal.to_proto()
        
        # Proto message fields should be empty (not set)
        assert proto.value.ByteSize() == 0
        assert proto.parent.type.ByteSize() == 0
    
    def test_message_field_set(self):
        """Test that set message fields are converted"""
        type_obj = Type(type_kind=type_pb2.TYPE_BOOL)
        literal = ResolvedLiteral(type=type_obj)
        
        proto = literal.to_proto()
        
        # Should be populated
        assert proto.parent.type.ByteSize() > 0
        assert proto.parent.type.type_kind == type_pb2.TYPE_BOOL
    
    def test_from_proto_empty_message(self):
        """Test loading from proto with empty message fields"""
        proto = resolved_ast_pb2.ResolvedLiteralProto()
        # Don't set any message fields
        
        literal = ResolvedLiteral.from_proto(proto)
        
        # Should be None (not set)
        assert literal.value is None
        assert literal.type is None
        assert literal.parse_location_range is None


class TestDefaultValues:
    """Test proper handling of default values"""
    
    def test_primitive_defaults_not_serialized_unnecessarily(self):
        """Test that primitive fields with default values aren't unnecessarily set in proto"""
        literal = ResolvedLiteral(
            # Explicitly set to default values
            has_explicit_type=False,  # default
            float_literal_id=0  # default
        )
        
        proto = literal.to_proto()
        
        # Proto should work correctly (defaults are proto defaults too)
        assert proto.has_explicit_type is False
        assert proto.float_literal_id == 0
    
    def test_non_default_primitives_serialized(self):
        """Test that non-default values are properly serialized"""
        literal = ResolvedLiteral(
            has_explicit_type=True,  # non-default
            float_literal_id=123  # non-default
        )
        
        proto = literal.to_proto()
        
        assert proto.has_explicit_type is True
        assert proto.float_literal_id == 123


class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_empty_instance_roundtrip(self):
        """Test roundtrip with completely empty instance"""
        empty = ResolvedLiteral()
        
        proto = empty.to_proto()
        restored = ResolvedLiteral.from_proto(proto)
        
        # Should have all defaults
        assert restored.has_explicit_type is False
        assert restored.float_literal_id == 0
        assert restored.value is None
    
    def test_partial_fields_roundtrip(self):
        """Test roundtrip with only some fields set"""
        partial = ResolvedLiteral(
            has_explicit_type=True,
            # Other fields left as defaults
        )
        
        proto = partial.to_proto()
        restored = ResolvedLiteral.from_proto(proto)
        
        assert restored.has_explicit_type is True
        assert restored.float_literal_id == 0  # default preserved
        assert restored.value is None  # default preserved


class TestRepeatedFields:
    """Test handling of repeated (list) fields"""
    
    def test_empty_list_default(self):
        """Test that repeated fields default to empty list"""
        from zetasql.types.proto_models import ResolvedScan
        
        scan = ResolvedScan()
        
        assert scan.column_list == []
        assert scan.hint_list == []
    
    def test_repeated_field_roundtrip(self):
        """Test roundtrip with repeated fields"""
        from zetasql.types.proto_models import ResolvedScan, ResolvedColumn
        
        col1 = ResolvedColumn(name="col1", column_id=1)
        col2 = ResolvedColumn(name="col2", column_id=2)
        
        scan = ResolvedScan(column_list=[col1, col2])
        
        proto = scan.to_proto()
        restored = ResolvedScan.from_proto(proto)
        
        assert len(restored.column_list) == 2
        assert restored.column_list[0].name == "col1"
        assert restored.column_list[1].name == "col2"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
