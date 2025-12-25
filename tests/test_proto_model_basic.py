"""Test the generated wrapper classes"""
from zetasql.types.proto_model import parse_proto
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zetasql.types import ResolvedLiteral, ResolvedExpr, ResolvedNode, Type, ParseLocationRange
from zetasql.types.type_kind import TypeKind


def test_proto_model_basic():
    """Test basic wrapper functionality"""
    # Create using ProtoModel
    parse_location = ParseLocationRange(start=0, end=10)
    type_obj = Type(type_kind=TypeKind.TYPE_INT64)
    
    literal = ResolvedLiteral(
        has_explicit_type=True,
        float_literal_id=123,
        type=type_obj,
        parse_location_range=parse_location
    )
    
    # Test direct properties
    assert literal.has_explicit_type == True
    assert literal.float_literal_id == 123
    
    # Test inherited properties from ResolvedExpr
    assert literal.type is not None
    assert literal.type.type_kind == TypeKind.TYPE_INT64
    
    # Test inherited properties from ResolvedNode
    assert literal.parse_location_range is not None
    assert literal.parse_location_range.start == 0
    assert literal.parse_location_range.end == 10
    
    # Test isinstance
    assert isinstance(literal, ResolvedLiteral)
    assert isinstance(literal, ResolvedExpr)
    assert isinstance(literal, ResolvedNode)


if __name__ == "__main__":
    test_wrapper_basic()
