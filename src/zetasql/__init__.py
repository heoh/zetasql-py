"""
ZetaSQL - Python port of Google's ZetaSQL

This is a Python implementation of ZetaSQL, providing SQL analysis and parsing
capabilities for Python applications.
"""

from zetasql.__version__ import __version__
from zetasql.prepared_query import PreparedQuery, PreparedQueryBuilder
from zetasql.catalog_registry import RegisteredCatalog
from zetasql.analyzer import Analyzer
from zetasql.exceptions import (
    ZetaSQLError,
    AnalyzerError,
    InvalidArgumentError,
    ResourceNotFoundError,
    IllegalStateError,
    StatusCode,
)

__all__ = [
    "__version__",
    "PreparedQuery",
    "PreparedQueryBuilder",
    "RegisteredCatalog",
    "Analyzer",
    "ZetaSQLError",
    "AnalyzerError",
    "InvalidArgumentError",
    "ResourceNotFoundError",
    "IllegalStateError",
    "StatusCode",
]
