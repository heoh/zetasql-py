"""FunctionBuilder - Fluent API for building Function ProtoModel objects."""

from typing_extensions import Self

from zetasql.types import (
    Function,
    FunctionArgumentType,
    FunctionArgumentTypeOptions,
    FunctionEnums,
    FunctionSignature,
    SignatureArgumentKind,
    Type,
    TypeKind,
)

from ._helpers import convert_to_type


class FunctionBuilder:
    """Builder for Function ProtoModel objects.

    Args:
        name: Function name (can be multi-part like "pkg.MY_UDF")
        group: Function group (default: "UDF")
        mode: Function mode (default: SCALAR)
    """

    def __init__(self, name: str, group: str = "UDF", mode: int = FunctionEnums.Mode.SCALAR):
        name_path = name.split(".") if "." in name else [name]
        self._function = Function(name_path=name_path, group=group, mode=mode, signature=[])

    def set_group(self, group: str) -> Self:
        """Set function group."""
        self._function.group = group
        return self

    def set_mode(self, mode: int) -> Self:
        """Set function mode."""
        self._function.mode = mode
        return self

    def add_signature(self, signature: FunctionSignature) -> Self:
        """Add a function signature (allows overloading)."""
        self._function.signature.append(signature)
        return self

    def build(self) -> Function:
        """Build and return the Function ProtoModel."""
        return self._function


class SignatureBuilder:
    """Builder for FunctionSignature ProtoModel objects."""

    def __init__(self):
        self._signature = FunctionSignature(argument=[], return_type=None)

    def add_argument(
        self,
        type_or_kind: Type | TypeKind | int,
        cardinality: FunctionEnums.ArgumentCardinality = FunctionEnums.ArgumentCardinality.REQUIRED,
    ) -> Self:
        """Add an argument to the signature."""
        arg_type = convert_to_type(type_or_kind)
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_FIXED,
            type=arg_type,
            options=FunctionArgumentTypeOptions(cardinality=cardinality),
        )
        self._signature.argument.append(arg)
        return self

    def set_return_type(self, type_or_kind: Type | TypeKind | int) -> Self:
        """Set the return type of the signature."""
        ret_type = convert_to_type(type_or_kind)
        self._signature.return_type = FunctionArgumentType(kind=SignatureArgumentKind.ARG_TYPE_FIXED, type=ret_type)
        return self

    def build(self) -> FunctionSignature:
        """Build and return the FunctionSignature ProtoModel."""
        return self._signature


__all__ = ["FunctionBuilder", "SignatureBuilder"]
