"""ZetaSQL API Layer - Convenience Features.

This package provides Layer 2 convenience features:

- analyzer: High-level Analyzer class with static/instance methods
- parser: High-level Parser class for syntax-only parsing
- prepared_query: PreparedQuery with builder pattern and context management
- prepared_expression: PreparedExpression for evaluating expressions
- builders: Fluent builder APIs (CatalogBuilder, TableBuilder)

These features mirror the Java ZetaSQL API for familiarity.
"""

from .analyzer import Analyzer, ScriptMetadata, StatementType, ValidationResult, get_statement_type
from .ast_visitor import ASTNodeVisitor
from .builders import (
    CatalogBuilder,
    ConstantBuilder,
    FunctionBuilder,
    SignatureBuilder,
    TableBuilder,
    TVFBuilder,
)
from .parser import Parser
from .prepared_expression import PreparedExpression
from .prepared_query import PreparedQuery, PreparedQueryBuilder
from .resolved_visitor import ResolvedNodeVisitor
from .table_content import create_table_content
from .tree_visitor import TreeVisitor
from .type_factory import TypeFactory
from .value import Value

__all__ = [
    "ASTNodeVisitor",
    "Analyzer",
    "CatalogBuilder",
    "ConstantBuilder",
    "FunctionBuilder",
    "Parser",
    "PreparedExpression",
    "PreparedQuery",
    "PreparedQueryBuilder",
    "ResolvedNodeVisitor",
    "ScriptMetadata",
    "SignatureBuilder",
    "StatementType",
    "TVFBuilder",
    "TableBuilder",
    "TreeVisitor",
    "TypeFactory",
    "ValidationResult",
    "Value",
    "create_table_content",
    "get_statement_type",
]
