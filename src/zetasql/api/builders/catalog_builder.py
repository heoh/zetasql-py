"""
CatalogBuilder - Fluent API for building SimpleCatalog ProtoModel objects

This module provides a Java-style builder pattern for constructing catalogs,
making it easy to compose tables and configure builtin functions.

Examples:
    >>> from zetasql.builders import CatalogBuilder, TableBuilder
    >>> from zetasql.types import TypeKind
    >>>
    >>> # Build catalog with multiple tables
    >>> orders = (TableBuilder("orders")
    ...     .add_column("order_id", TypeKind.TYPE_INT64)
    ...     .add_column("product_id", TypeKind.TYPE_INT64)
    ...     .build())
    >>>
    >>> products = (TableBuilder("products")
    ...     .add_column("product_id", TypeKind.TYPE_INT64)
    ...     .add_column("name", TypeKind.TYPE_STRING)
    ...     .build())
    >>>
    >>> catalog = (CatalogBuilder("demo")
    ...     .add_table(orders)
    ...     .add_table(products)
    ...     .build())
    >>>
    >>> # Use with LocalService
    >>> service.analyze(sql_statement="SELECT * FROM orders", simple_catalog=catalog)
"""

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

    Provides method chaining for fluent catalog construction. The builder
    creates ProtoModel objects that can be passed directly to LocalService.

    Args:
        name: Catalog name

    Examples:
        >>> # Basic catalog with tables
        >>> catalog = (CatalogBuilder("my_db")
        ...     .add_table(orders_table)
        ...     .add_table(products_table)
        ...     .build())
        >>>
        >>> # With builtin functions
        >>> from zetasql.types.proto_models import ZetaSQLBuiltinFunctionOptions
        >>>
        >>> options = ZetaSQLBuiltinFunctionOptions(...)
        >>> catalog = (CatalogBuilder("my_db")
        ...     .add_table(table)
        ...     .with_builtin_functions(options)
        ...     .build())
    """

    def __init__(self, name: str):
        """Initialize CatalogBuilder.

        Args:
            name: Catalog name
        """
        self._catalog = SimpleCatalog(name=name, table=[])

    def add_table(self, table: SimpleTable) -> Self:
        """Add a table to the catalog.

        Args:
            table: SimpleTable ProtoModel (typically from TableBuilder)

        Returns:
            Self for method chaining

        Raises:
            ValueError: If table with same name already exists (case-insensitive)

        Examples:
            >>> orders = TableBuilder("orders").add_column("id", TypeKind.TYPE_INT64).build()
            >>> catalog = CatalogBuilder("db").add_table(orders).build()
        """
        # Check for duplicates (case-insensitive, Java behavior)
        if table.name:
            new_name = table.name.lower()
            for existing in self._catalog.table:
                if existing.name and existing.name.lower() == new_name:
                    raise ValueError(f"Table '{table.name}' already exists in catalog")

        self._catalog.table.append(table)
        return self

    def with_builtin_functions(self, options: ZetaSQLBuiltinFunctionOptions) -> Self:
        """Configure builtin function options.

        Args:
            options: ZetaSQLBuiltinFunctionOptions ProtoModel

        Returns:
            Self for method chaining

        Examples:
            >>> from zetasql.types.proto_models import ZetaSQLBuiltinFunctionOptions, LanguageOptions
            >>>
            >>> lang_opts = LanguageOptions(...)
            >>> builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)
            >>>
            >>> catalog = (CatalogBuilder("db")
            ...     .add_table(table)
            ...     .with_builtin_functions(builtin_opts)
            ...     .build())
        """
        self._catalog.builtin_function_options = options
        return self

    def add_function(self, function: Function) -> Self:
        """Add a custom function to the catalog.

        Args:
            function: Function ProtoModel (typically from FunctionBuilder)

        Returns:
            Self for method chaining

        Examples:
            >>> from zetasql.api.builders import FunctionBuilder, SignatureBuilder
            >>>
            >>> my_udf = (FunctionBuilder("MY_UDF")
            ...     .add_signature(
            ...         SignatureBuilder()
            ...             .add_argument(TypeKind.TYPE_STRING)
            ...             .set_return_type(TypeKind.TYPE_INT64)
            ...             .build()
            ...     )
            ...     .build())
            >>>
            >>> catalog = (CatalogBuilder("db")
            ...     .add_function(my_udf)
            ...     .build())
        """
        self._catalog.add_function(function)
        return self

    def add_table_valued_function(self, tvf: TableValuedFunction) -> Self:
        """Add a table-valued function to the catalog.

        Args:
            tvf: TableValuedFunction ProtoModel (typically from TVFBuilder)

        Returns:
            Self for method chaining

        Examples:
            >>> from zetasql.api.builders import TVFBuilder
            >>>
            >>> my_tvf = (TVFBuilder("my_tvf")
            ...     .add_argument("input_col", TypeKind.TYPE_INT64)
            ...     .set_output_schema([
            ...         ("output_col", TypeKind.TYPE_STRING),
            ...     ])
            ...     .build())
            >>>
            >>> catalog = (CatalogBuilder("db")
            ...     .add_table_valued_function(my_tvf)
            ...     .build())
        """
        self._catalog.add_table_valued_function(tvf)
        return self

    def add_constant(self, constant: SimpleConstant) -> Self:
        """Add a constant to the catalog.

        Args:
            constant: SimpleConstant ProtoModel (typically from ConstantBuilder)

        Returns:
            Self for method chaining

        Examples:
            >>> from zetasql.api.builders import ConstantBuilder
            >>>
            >>> max_limit = (ConstantBuilder("MAX_LIMIT")
            ...     .set_type(TypeKind.TYPE_INT64)
            ...     .build())
            >>>
            >>> catalog = (CatalogBuilder("db")
            ...     .add_constant(max_limit)
            ...     .build())
        """
        self._catalog.add_constant(constant)
        return self

    def build(self) -> SimpleCatalog:
        """Build and return the SimpleCatalog ProtoModel.

        Returns:
            SimpleCatalog ProtoModel ready to use with LocalService

        Examples:
            >>> catalog = CatalogBuilder("db").add_table(table).build()
            >>>
            >>> # Use directly with LocalService (ProtoModel is auto-converted)
            >>> service = ZetaSqlLocalService()
            >>> response = service.analyze(
            ...     sql_statement="SELECT * FROM orders",
            ...     simple_catalog=catalog
            ... )
        """
        return self._catalog


__all__ = ["CatalogBuilder"]
