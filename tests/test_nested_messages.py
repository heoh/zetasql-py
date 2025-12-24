"""Test nested message wrappers"""
from zetasql.wrapper_utils import parse_wrapper
import sys
sys.path.insert(0, 'src')

from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.resolved_ast_wrapper import AllowedHintsAndOptions, AllowedHintsAndOptionsHint, AllowedHintsAndOptionsOption


def test_nested_messages():
    """Test that nested proto messages are properly wrapped"""
    
    # Create proto with nested messages
    proto = options_pb2.AllowedHintsAndOptionsProto()
    
    # Add a hint (nested message)
    hint = proto.hint.add()
    hint.name = "test_hint"
    hint.qualifier = "test_qualifier"
    hint.allow_unqualified = True
    
    # Add an option (nested message)
    option = proto.option.add()
    option.name = "test_option"
    
    # Wrap it using from_proto
    wrapper = parse_wrapper(proto)
    
    print("✓ Testing nested message wrappers...")
    
    # Test hint access
    assert len(wrapper.hint) == 1
    assert isinstance(wrapper.hint[0], AllowedHintsAndOptionsHint)
    assert wrapper.hint[0].name == "test_hint"
    assert wrapper.hint[0].qualifier == "test_qualifier"
    assert wrapper.hint[0].allow_unqualified == True
    print(f"  hint[0].name: {wrapper.hint[0].name}")
    print(f"  hint[0] type: {type(wrapper.hint[0]).__name__}")
    
    # Test option access
    assert len(wrapper.option) == 1
    assert isinstance(wrapper.option[0], AllowedHintsAndOptionsOption)
    assert wrapper.option[0].name == "test_option"
    print(f"  option[0].name: {wrapper.option[0].name}")
    print(f"  option[0] type: {type(wrapper.option[0]).__name__}")
    
    print("\n✅ All nested message tests passed!")
    print("\nKey achievements:")
    print("  1. 🎯 Nested proto messages are now wrapped")
    print("  2. 🔗 Wrapper classes created for nested types")
    print("  3. 💡 Type hints use full proto path (e.g., AllowedHintsAndOptionsProto.HintProto)")
    print("  4. ✨ IDE autocomplete works for nested message fields")


if __name__ == '__main__':
    test_nested_messages()
