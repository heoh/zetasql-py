"""Test nested message wrappers"""
from zetasql.types.proto_model import parse_proto
import sys
sys.path.insert(0, 'src')

from zetasql.types.proto_models import AllowedHintsAndOptions


def test_nested_messages():
    """Test that nested proto messages are properly wrapped"""
    
    # Create using ProtoModel
    hint = AllowedHintsAndOptions.Hint(
        name="test_hint",
        qualifier="test_qualifier",
        allow_unqualified=True
    )
    
    option = AllowedHintsAndOptions.Option(name="test_option")
    
    # Create wrapper with nested messages
    wrapper = AllowedHintsAndOptions(
        hint=[hint],
        option=[option]
    )
    
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
