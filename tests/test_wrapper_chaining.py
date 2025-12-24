"""Test wrapper chaining and nested access"""
from zetasql.wrapper_utils import parse_wrapper
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.resolved_ast_wrapper import ResolvedLiteral, ParseLocationRange


def test_wrapper_chaining():
    """Test that wrappers return wrappers, enabling clean chaining"""
    
    # Create proto with nested structure
    literal_proto = resolved_ast_pb2.ResolvedLiteralProto()
    literal_proto.has_explicit_type = True
    literal_proto.parent.type.type_kind = 1
    literal_proto.parent.parent.parse_location_range.start = 10
    literal_proto.parent.parent.parse_location_range.end = 20
    literal_proto.parent.parent.parse_location_range.filename = "test.sql"
    
    # Wrap it using from_proto
    literal = parse_wrapper(literal_proto)
    
    print("✓ Testing wrapper chaining...")
    
    # Test that nested access returns wrappers, not proto
    parse_loc = literal.parse_location_range
    print(f"  parse_location_range type: {type(parse_loc).__name__}")
    assert isinstance(parse_loc, ParseLocationRange), "Should return ParseLocationRange wrapper!"
    
    # Test chained access
    print(f"  parse_location_range.filename: {parse_loc.filename}")
    assert parse_loc.filename == "test.sql"
    assert parse_loc.start == 10
    assert parse_loc.end == 20
    
    # Test direct chained access
    print(f"  literal.parse_location_range.filename: {literal.parse_location_range.filename}")
    assert literal.parse_location_range.filename == "test.sql"
    
    # Test that type is also wrapped
    type_obj = literal.type
    print(f"  type object type: {type(type_obj).__name__}")
    # Type wrapper has type_kind property
    assert type_obj.type_kind == 1
    
    print("\n✓ Testing None handling...")
    
    # Create proto without type_annotation_map
    literal_proto2 = resolved_ast_pb2.ResolvedLiteralProto()
    literal2 = parse_wrapper(literal_proto2)
    
    # Should return None for empty message
    assert literal2.type_annotation_map is None
    assert literal2.parse_location_range is None
    print("  Empty fields correctly return None")
    
    print("\n✅ All chaining tests passed!")
    print("\nKey benefits:")
    print("  1. 🔗 Clean chaining: literal.parse_location_range.filename")
    print("  2. 🎯 Type safety: All return values are typed wrappers")
    print("  3. 💡 IDE support: Autocomplete works at every level")
    print("  4. ✨ Consistent API: Everything is a wrapper, not proto")


if __name__ == "__main__":
    test_wrapper_chaining()
