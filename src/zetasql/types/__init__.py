"""
ZetaSQL Types Module

This module provides Python type wrappers for ZetaSQL protobuf messages.

Key exports:
    - TypeKind: Type-safe enum for ZetaSQL type kinds
    - Type: Enhanced type class with helper methods (overrides generated Type)
    - StructField, ArrayType, StructType, MapType: Directly from proto models
    - All other proto models: ResolvedLiteral, ASTNode, AnalyzeRequest, etc.

Examples:
    >>> from zetasql.types import Type, TypeKind, StructField
    >>> t = Type(type_kind=TypeKind.TYPE_INT64)
    >>> t.is_int64()  # True
    >>> t.type_name()  # 'INT64'
"""

# Import TypeKind enum
from zetasql.types.type_kind import TypeKind

# Import extended Type (overrides generated Type!)
from zetasql.types.type_extensions import Type as ExtendedType

# Re-export all proto models for backward compatibility
from zetasql.types import proto_models
from zetasql.types.proto_models import *  # noqa: F401, F403

# Explicit imports for documentation
from zetasql.types.proto_model import ProtoModel, parse_proto  # noqa: F401

# Override Type with extended version (must be after wildcard import!)
Type = ExtendedType

# Update __all__ to include new exports and override Type
__all__ = [
    # Type system core
    'TypeKind',
    'Type',  # Extended version (overrides generated)
    # Base classes
    'ProtoModel',
    'parse_proto',
    # All generated proto models
    *proto_models.__all__,
]
