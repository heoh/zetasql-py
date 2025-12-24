"""Test the generated wrapper classes"""
from zetasql.types.proto_model import parse_proto
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.types.proto_models import ResolvedLiteral, ResolvedExpr, ResolvedNode


def test_wrapper_basic():
    """Test basic wrapper functionality"""
    # Create a proto object
    literal_proto = resolved_ast_pb2.ResolvedLiteralProto()
    
    # Set some fields
    literal_proto.has_explicit_type = True
    literal_proto.float_literal_id = 123
    
    # Set parent field (ResolvedExpr)
    literal_proto.parent.type.type_kind = 1
    
    # Set parent.parent field (ResolvedNode)
    literal_proto.parent.parent.parse_location_range.start = 0
    literal_proto.parent.parent.parse_location_range.end = 10
    
    # Wrap it using from_proto
    literal = parse_proto(literal_proto)
    
    # Test direct properties
    print("✓ Testing direct properties...")
    assert literal.has_explicit_type == True
    assert literal.float_literal_id == 123
    print(f"  has_explicit_type: {literal.has_explicit_type}")
    print(f"  float_literal_id: {literal.float_literal_id}")
    
    # Test inherited properties from ResolvedExpr
    print("\n✓ Testing inherited properties from ResolvedExpr...")
    assert literal.type is not None
    assert literal.type.type_kind == 1
    print(f"  type.type_kind: {literal.type.type_kind}")
    
    # Test inherited properties from ResolvedNode
    print("\n✓ Testing inherited properties from ResolvedNode...")
    assert literal.parse_location_range is not None
    assert literal.parse_location_range.start == 0
    assert literal.parse_location_range.end == 10
    print(f"  parse_location_range.start: {literal.parse_location_range.start}")
    print(f"  parse_location_range.end: {literal.parse_location_range.end}")
    
    # Test isinstance
    print("\n✓ Testing isinstance checks...")
    assert isinstance(literal, ResolvedLiteral)
    assert isinstance(literal, ResolvedExpr)
    assert isinstance(literal, ResolvedNode)
    print(f"  isinstance(literal, ResolvedLiteral): {isinstance(literal, ResolvedLiteral)}")
    print(f"  isinstance(literal, ResolvedExpr): {isinstance(literal, ResolvedExpr)}")
    print(f"  isinstance(literal, ResolvedNode): {isinstance(literal, ResolvedNode)}")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_wrapper_basic()
