"""Test wrapper chaining and nested access"""
from zetasql.types import parse_proto
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.types import ResolvedLiteral, ParseLocationRange


def test_proto_model_chaining():
    """Test that wrappers return wrappers, enabling clean chaining"""
    
    # Create proto with nested structure
    literal_proto = resolved_ast_pb2.ResolvedLiteralProto()
    literal_proto.has_explicit_type = True
    literal_proto.parent.type.type_kind = 1
    literal_proto.parent.parent.parse_location_range.start = 10
    literal_proto.parent.parent.parse_location_range.end = 20
    literal_proto.parent.parent.parse_location_range.filename = "test.sql"
    
    # Wrap it using from_proto
    literal = parse_proto(literal_proto).as_type(ResolvedLiteral)
    
    print("✓ Testing wrapper chaining...")
    
    assert isinstance(literal.parse_location_range, ParseLocationRange), "Should return ParseLocationRange wrapper!"
    assert literal.parse_location_range.filename == "test.sql"
    assert literal.parse_location_range.start == 10
    assert literal.parse_location_range.end == 20
    assert literal.type.type_kind == 1
    
    # Create proto without type_annotation_map
    literal_proto2 = resolved_ast_pb2.ResolvedLiteralProto()
    literal2 = parse_proto(literal_proto2).as_type(ResolvedLiteral)
    
    # Should return None for empty message
    assert literal2.type_annotation_map is None
    assert literal2.parse_location_range is None


if __name__ == "__main__":
    test_proto_model_chaining()
