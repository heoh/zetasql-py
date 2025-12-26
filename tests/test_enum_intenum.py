"""
Tests for IntEnum support in proto models.

Tests that enum fields are properly typed as IntEnum and provide
IDE autocomplete and type safety.
"""

import pytest
from enum import IntEnum

from zetasql.types.proto_models import (
    ResolvedJoinScan,
    ResolvedJoinScanEnums,
)
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2


class TestIntEnumSupport:
    """Test IntEnum support for proto enum fields"""
    
    def test_nested_enum_exists(self):
        """Test that nested enum class exists and is IntEnum"""
        assert hasattr(ResolvedJoinScanEnums, 'JoinType')
        assert issubclass(ResolvedJoinScanEnums.JoinType, IntEnum)
    
    def test_enum_values_exist(self):
        """Test that enum values are accessible"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        assert hasattr(JoinType, 'INNER')
        assert hasattr(JoinType, 'LEFT')
        assert hasattr(JoinType, 'RIGHT')
        assert hasattr(JoinType, 'FULL')
    
    def test_enum_values_are_correct(self):
        """Test that enum values have correct integer values"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        assert JoinType.INNER == 0
        assert JoinType.LEFT == 1
        assert JoinType.RIGHT == 2
        assert JoinType.FULL == 3
    
    def test_enum_is_int_compatible(self):
        """Test that IntEnum is compatible with int (backward compatibility)"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        # IntEnum should be instance of int
        assert isinstance(JoinType.INNER, int)
        
        # Can compare with int
        assert JoinType.INNER == 0
        assert JoinType.LEFT == 1
        
        # Can use in arithmetic
        assert JoinType.INNER + 1 == 1
    
    def test_create_with_enum_value(self):
        """Test creating model with enum value"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        scan = ResolvedJoinScan(
            join_type=JoinType.INNER,
            column_list=[],
            hint_list=[],
        )
        
        assert scan.join_type == JoinType.INNER
        assert scan.join_type == 0  # Still compatible with int
    
    def test_create_with_int_value(self):
        """Test backward compatibility: creating with int value"""
        scan = ResolvedJoinScan(
            join_type=1,  # Using int directly
            column_list=[],
            hint_list=[],
        )
        
        # Should still work
        assert scan.join_type == 1
    
    def test_to_proto_conversion(self):
        """Test converting model with enum to proto"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        scan = ResolvedJoinScan(
            join_type=JoinType.LEFT,
            column_list=[],
            hint_list=[],
        )
        
        proto = scan.to_proto()
        
        # Proto should have the int value
        assert proto.join_type == 1
        assert proto.join_type == JoinType.LEFT
    
    def test_from_proto_conversion(self):
        """Test converting proto with enum to model"""
        # Create a proto with enum field
        proto = resolved_ast_pb2.ResolvedJoinScanProto()
        proto.join_type = 2  # RIGHT
        
        # Convert to model
        scan = ResolvedJoinScan.from_proto(proto)
        
        # Should be converted to IntEnum
        assert scan.join_type == ResolvedJoinScanEnums.JoinType.RIGHT
        assert isinstance(scan.join_type, IntEnum)
        assert scan.join_type == 2  # Still compatible with int
    
    def test_from_proto_with_zero_value(self):
        """Test from_proto with zero/default enum value"""
        proto = resolved_ast_pb2.ResolvedJoinScanProto()
        proto.join_type = 0  # INNER (default)
        
        scan = ResolvedJoinScan.from_proto(proto)
        
        assert scan.join_type == ResolvedJoinScanEnums.JoinType.INNER
        assert scan.join_type == 0
    
    def test_enum_name_property(self):
        """Test that enum has name property for debugging"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        assert JoinType.INNER.name == 'INNER'
        assert JoinType.LEFT.name == 'LEFT'
        assert JoinType.RIGHT.name == 'RIGHT'
        assert JoinType.FULL.name == 'FULL'
    
    def test_enum_comparison(self):
        """Test enum comparison works correctly"""
        JoinType = ResolvedJoinScanEnums.JoinType
        
        assert JoinType.INNER == JoinType.INNER
        assert JoinType.INNER != JoinType.LEFT
        assert JoinType.LEFT < JoinType.RIGHT
        assert JoinType.FULL > JoinType.INNER


class TestTypeHinting:
    """Test that type hints work correctly with IDEs"""
    
    def test_type_hint_is_correct(self):
        """Test that join_type field has correct type hint"""
        import inspect
        from typing import get_type_hints
        
        # Get type hints for ResolvedJoinScan
        hints = get_type_hints(ResolvedJoinScan)
        
        # join_type should be hinted as Optional[ResolvedJoinScanEnums.JoinType]
        # Note: Due to forward references, we check the string representation
        join_type_hint = ResolvedJoinScan.__annotations__['join_type']
        
        # Should reference the nested enum
        assert 'ResolvedJoinScanEnums.JoinType' in str(join_type_hint)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
