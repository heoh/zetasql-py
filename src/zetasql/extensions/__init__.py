"""ZetaSQL Extensions Layer - Python-specific Convenience APIs.

This package provides Layer 3 extended APIs beyond the Java API:

- table_content: Python-friendly factory for creating TableContent from lists

Future extensions may include:
- DataFrame integration (pandas, polars)
- More Pythonic abstractions
"""

from .table_content import create_table_content

__all__ = [
    'create_table_content',
]
