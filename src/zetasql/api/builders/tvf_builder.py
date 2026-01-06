"""TVFBuilder - Fluent API for building TableValuedFunction ProtoModel objects."""

from typing_extensions import Self

from zetasql.types import (
    FunctionArgumentType,
    FunctionArgumentTypeOptions,
    FunctionEnums,
    FunctionSignature,
    SignatureArgumentKind,
    TableValuedFunction,
    TVFRelation,
    TVFRelationColumn,
    Type,
    TypeKind,
)

from ._helpers import convert_to_type


class TVFBuilder:
    """Builder for TableValuedFunction ProtoModel objects.

    Args:
        name: TVF name (can be qualified like "pkg.my_tvf")
    """

    def __init__(self, name: str):
        name_path = name.split(".") if "." in name else [name]
        self._tvf = TableValuedFunction(name_path=name_path, signature=FunctionSignature(argument=[], return_type=None))
        self._tvf_type = None
        self._output_columns = []

    def add_argument(
        self,
        name: str,
        type_or_kind: Type | TypeKind | int,
        cardinality: FunctionEnums.ArgumentCardinality = FunctionEnums.ArgumentCardinality.REQUIRED,
    ) -> Self:
        """Add a scalar argument to the TVF."""
        arg_type = convert_to_type(type_or_kind)
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_FIXED,
            type=arg_type,
            options=FunctionArgumentTypeOptions(cardinality=cardinality, argument_name=name),
        )
        self._tvf.signature.argument.append(arg)
        return self

    def add_table_argument(self, name: str) -> Self:
        """Add a TABLE argument to the TVF."""
        arg = FunctionArgumentType(
            kind=SignatureArgumentKind.ARG_TYPE_RELATION,
            options=FunctionArgumentTypeOptions(argument_name=name),
        )
        self._tvf.signature.argument.append(arg)
        return self

    def set_output_schema(self, columns: list[tuple[str, Type | TypeKind | int]]) -> Self:
        """Set fixed output schema for the TVF."""
        self._tvf_type = FunctionEnums.TableValuedFunctionType.FIXED_OUTPUT_SCHEMA_TVF
        self._output_columns = []

        for col_name, type_or_kind in columns:
            col_type = convert_to_type(type_or_kind)
            self._output_columns.append(TVFRelationColumn(name=col_name, type=col_type))

        return self

    def set_forward_input_schema(self) -> Self:
        """Set TVF to forward input schema to output (pass-through)."""
        self._tvf_type = FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF
        return self

    def append_output_column(self, name: str, type_or_kind: Type | TypeKind | int) -> Self:
        """Append a column to the output schema."""
        if self._tvf_type == FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_TVF:
            self._tvf_type = (
                FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS
            )

        col_type = convert_to_type(type_or_kind)
        self._output_columns.append(TVFRelationColumn(name=name, type=col_type))
        return self

    def set_forward_input_schema_with_appended_columns(
        self,
        appended_columns: list[tuple[str, Type | TypeKind | int]],
    ) -> Self:
        """Set TVF to forward input schema plus additional columns."""
        self._tvf_type = (
            FunctionEnums.TableValuedFunctionType.FORWARD_INPUT_SCHEMA_TO_OUTPUT_SCHEMA_WITH_APPENDED_COLUMNS
        )
        self._output_columns = []

        for col_name, type_or_kind in appended_columns:
            col_type = convert_to_type(type_or_kind)
            self._output_columns.append(TVFRelationColumn(name=col_name, type=col_type))

        return self

    def build(self) -> TableValuedFunction:
        """Build and return the TableValuedFunction ProtoModel."""
        if self._tvf_type is not None:
            self._tvf.type = self._tvf_type

        if self._output_columns:
            output_relation = TVFRelation(column=self._output_columns, is_value_table=False)
            self._tvf.signature.return_type = FunctionArgumentType(
                kind=SignatureArgumentKind.ARG_TYPE_RELATION,
                options=FunctionArgumentTypeOptions(relation_input_schema=output_relation),
            )

        return self._tvf


__all__ = ["TVFBuilder"]
