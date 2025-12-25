"""Test nested message wrappers"""
from zetasql.types.proto_model import parse_proto
import sys
sys.path.insert(0, 'src')

from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.types.proto_models import AllowedHintsAndOptions


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
    wrapper = AllowedHintsAndOptions.from_proto(proto)
    
    # Test hint access
    assert len(wrapper.hint) == 1
    assert isinstance(wrapper.hint[0], AllowedHintsAndOptions.Hint)
    assert wrapper.hint[0].name == "test_hint"
    assert wrapper.hint[0].qualifier == "test_qualifier"
    assert wrapper.hint[0].allow_unqualified == True
    
    # Test option access
    assert len(wrapper.option) == 1
    assert isinstance(wrapper.option[0], AllowedHintsAndOptions.Option)
    assert wrapper.option[0].name == "test_option"


if __name__ == '__main__':
    test_nested_messages()
