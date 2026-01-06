"""Internal helper utilities for builders."""

from zetasql.api.type_factory import TypeFactory
from zetasql.types import Type, TypeKind


def convert_to_type(type_or_kind: Type | TypeKind | int) -> Type:
    """Convert TypeKind to Type if needed.

    Args:
        type_or_kind: Type object or TypeKind enum value

    Returns:
        Type object
    """
    if isinstance(type_or_kind, (TypeKind, int)):
        return TypeFactory.create_simple_type(type_or_kind)
    return type_or_kind
