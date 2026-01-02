"""Common fixtures for catalog tests."""

import pytest
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import (
    TypeKind,
    AnalyzerOptions,
    LanguageOptions,
    ZetaSQLBuiltinFunctionOptions,
)


@pytest.fixture
def service():
    """Get LocalService singleton."""
    return ZetaSqlLocalService.get_instance()


@pytest.fixture
def options(service):
    """Create analyzer options with maximum features."""
    return AnalyzerOptions(
        language_options=service.get_language_options(maximum_features=True),
    )


@pytest.fixture
def empty_catalog():
    """Create empty catalog for testing."""
    return CatalogBuilder("test_catalog").build()


@pytest.fixture
def sample_table():
    """Create a sample table for testing."""
    return (TableBuilder("SampleTable")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("value", TypeKind.TYPE_DOUBLE)
        .build())
