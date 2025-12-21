import zetasql


def test_version():
    """Test that version is defined."""
    assert hasattr(zetasql, "__version__")
    assert isinstance(zetasql.__version__, str)
