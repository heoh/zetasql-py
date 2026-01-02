"""
Common fixtures for all tests.

These fixtures are automatically available to all test files.
"""

import pytest
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.api.analyzer import Analyzer
from zetasql.api.builders import TableBuilder, CatalogBuilder
from zetasql.types import (
    TypeKind,
    AnalyzerOptions,
    LanguageOptions,
    ZetaSQLBuiltinFunctionOptions,
)


@pytest.fixture(scope="session")
def service():
    """Get LocalService singleton - session scoped for efficiency."""
    return ZetaSqlLocalService.get_instance()


@pytest.fixture
def options(service):
    """Create analyzer options with maximum features."""
    return AnalyzerOptions(
        language_options=service.get_language_options(maximum_features=True),
    )


@pytest.fixture
def builtin_function_options():
    """Create builtin function options with maximum features."""
    return ZetaSQLBuiltinFunctionOptions(
        language_options=LanguageOptions.maximum_features(),
    )
