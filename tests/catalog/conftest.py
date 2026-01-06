"""Common fixtures for catalog tests."""

import pytest

from zetasql.api import CatalogBuilder, TableBuilder
from zetasql.types import (
    TypeKind,
)


@pytest.fixture
def empty_catalog():
    """Create empty catalog for testing."""
    return CatalogBuilder("test_catalog").build()


@pytest.fixture
def sample_table():
    """Create a sample table for testing."""
    return (
        TableBuilder("SampleTable")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("value", TypeKind.TYPE_DOUBLE)
        .build()
    )
