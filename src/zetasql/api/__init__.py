"""ZetaSQL API Layer - Java-style Convenience Features.

This package provides Layer 2 Java API-compatible convenience features:

- analyzer: High-level Analyzer class with static/instance methods
- prepared_query: PreparedQuery with builder pattern and context management
- catalog_registry: RegisteredCatalog context manager
- builders: Fluent builder APIs (CatalogBuilder, TableBuilder)

These features mirror the Java ZetaSQL API for familiarity.
"""

from .analyzer import Analyzer
from .prepared_query import PreparedQuery, PreparedQueryBuilder
from .catalog_registry import RegisteredCatalog
from .builders import CatalogBuilder, TableBuilder

__all__ = [
    'Analyzer',
    'PreparedQuery',
    'PreparedQueryBuilder',
    'RegisteredCatalog',
    'CatalogBuilder',
    'TableBuilder',
]
