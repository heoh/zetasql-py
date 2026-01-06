"""CatalogBuilder - Fluent API for building SimpleCatalog ProtoModel objects."""

from typing_extensions import Self

from zetasql.types import (
    Function,
    SimpleCatalog,
    SimpleConstant,
    SimpleTable,
    TableValuedFunction,
    ZetaSQLBuiltinFunctionOptions,
)


class CatalogBuilder:
    """Builder for SimpleCatalog ProtoModel objects.

    Args:
        name: Catalog name
    """

    def __init__(self, name: str):
        self._catalog = SimpleCatalog(name=name, table=[])

    def add_table(self, table: SimpleTable) -> Self:
        """Add a table to the catalog.

        Raises:
            ValueError: If table with same name already exists (case-insensitive)
        """
        if table.name:
            new_name = table.name.lower()
            for existing in self._catalog.table:
                if existing.name and existing.name.lower() == new_name:
                    raise ValueError(f"Table '{table.name}' already exists in catalog")

        self._catalog.table.append(table)
        return self

    def with_builtin_functions(self, options: ZetaSQLBuiltinFunctionOptions) -> Self:
        """Configure builtin function options."""
        self._catalog.builtin_function_options = options
        return self

    def add_function(self, function: Function) -> Self:
        """Add a custom function to the catalog."""
        self._catalog.add_function(function)
        return self

    def add_table_valued_function(self, tvf: TableValuedFunction) -> Self:
        """Add a table-valued function to the catalog."""
        self._catalog.add_table_valued_function(tvf)
        return self

    def add_constant(self, constant: SimpleConstant) -> Self:
        """Add a constant to the catalog."""
        self._catalog.add_constant(constant)
        return self

    def build(self) -> SimpleCatalog:
        """Build and return the SimpleCatalog ProtoModel."""
        return self._catalog


__all__ = ["CatalogBuilder"]
