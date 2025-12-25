"""
CatalogBuilder - Fluent API for building SimpleCatalog ProtoModel objects

This module provides a Java-style builder pattern for constructing catalogs,
making it easy to compose tables and configure builtin functions.

Examples:
    >>> from zetasql.builders import CatalogBuilder, TableBuilder
    >>> from zetasql.types.type_kind import TypeKind
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

from typing import TYPE_CHECKING
from zetasql.types.proto_models import SimpleCatalog, SimpleTable, ZetaSQLBuiltinFunctionOptions

if TYPE_CHECKING:
    from typing import Self
else:
    from typing_extensions import Self


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
        self._catalog = SimpleCatalog(
            name=name,
            table=[]
        )
    
    def add_table(self, table: SimpleTable) -> Self:
        """Add a table to the catalog.
        
        Args:
            table: SimpleTable ProtoModel (typically from TableBuilder)
        
        Returns:
            Self for method chaining
        
        Examples:
            >>> orders = TableBuilder("orders").add_column("id", TypeKind.TYPE_INT64).build()
            >>> catalog = CatalogBuilder("db").add_table(orders).build()
        """
        self._catalog.table.append(table)
        return self
    
    def with_builtin_functions(
        self, 
        options: ZetaSQLBuiltinFunctionOptions
    ) -> Self:
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


__all__ = ['CatalogBuilder']
