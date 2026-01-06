"""ZetaSQL API Layer - Convenience Features.

This package provides Layer 2 convenience features:

- analyzer: High-level Analyzer class with static/instance methods
- prepared_query: PreparedQuery with builder pattern and context management
- prepared_expression: PreparedExpression for evaluating expressions
- builders: Fluent builder APIs (CatalogBuilder, TableBuilder)

These features mirror the Java ZetaSQL API for familiarity.
"""

from .analyzer import Analyzer, ScriptMetadata, ValidationResult, StatementType, get_statement_type
from .prepared_query import PreparedQuery, PreparedQueryBuilder
from .prepared_expression import PreparedExpression
from .builders import CatalogBuilder, TableBuilder
from .table_content import create_table_content
from .type_factory import TypeFactory
from .value import Value

__all__ = [
    'Analyzer',
    'ScriptMetadata',
    'ValidationResult',
    'StatementType',
    'get_statement_type',
    'PreparedQuery',
    'PreparedQueryBuilder',
    'PreparedExpression',
    'CatalogBuilder',
    'TableBuilder',
    'create_table_content',
    'TypeFactory',
    'Value',
]
