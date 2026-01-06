"""
ZetaSQL - Python port of Google's ZetaSQL

This is a Python implementation of ZetaSQL, providing SQL analysis and parsing
capabilities for Python applications.

Architecture:
    The library is organized into 3 layers:

    - wasi: Layer 0 - WebAssembly resources and generated protobuf code
    - core: Layer 1 - WASI communication & ProtoModel infrastructure
    - api: Layer 2 - Convenience features
    - types: exported types

Recommended Usage:
    Use explicit import paths for clarity:

    from zetasql.core import ZetaSqlLocalService
    from zetasql.api import Analyzer, PreparedQuery, CatalogBuilder, TableBuilder, create_table_content
    from zetasql.types import TypeKind, AnalyzerOptions, proto_models
"""

from zetasql.__version__ import __version__

__all__ = [
    "__version__",
]
