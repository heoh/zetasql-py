"""Test the generated wrapper classes"""
from zetasql.types.proto_model import parse_proto
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.types import ResolvedLiteral, ResolvedExpr, ResolvedNode


def test_proto_model_basic():
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
    literal = parse_proto(literal_proto).as_type(ResolvedLiteral)
    
    # Test direct properties
    assert literal.has_explicit_type == True
    assert literal.float_literal_id == 123
    
    # Test inherited properties from ResolvedExpr
    assert literal.type is not None
    assert literal.type.type_kind == 1
    
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
