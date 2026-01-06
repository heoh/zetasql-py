"""ConstantBuilder - Fluent API for building SimpleConstant ProtoModel objects."""

from typing_extensions import Self

from zetasql.types import SimpleConstant, Type, TypeKind

from ._helpers import convert_to_type


class ConstantBuilder:
    """Builder for SimpleConstant ProtoModel objects.

    Args:
        name: Constant name (can be qualified like "pkg.MY_CONST")
    """

    def __init__(self, name: str):
        name_path = name.split(".") if "." in name else [name]
        self._constant = SimpleConstant(name_path=name_path, type=None, value=None)

    def set_type(self, type_or_kind: Type | TypeKind | int) -> Self:
        """Set the type of the constant."""
        self._constant.type = convert_to_type(type_or_kind)
        return self

    def build(self) -> SimpleConstant:
        """Build and return the SimpleConstant ProtoModel."""
        return self._constant
