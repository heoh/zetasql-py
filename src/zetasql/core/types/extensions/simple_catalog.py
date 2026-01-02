from dataclasses import dataclass
from zetasql.core.types.proto_models import (
    SimpleCatalog as _GeneratedSimpleCatalog,
)

@dataclass
class SimpleCatalog(_GeneratedSimpleCatalog):
    """Generated model for SimpleCatalogProto"""
    
    def register(self, service=None):
        """Register catalog and return context manager for auto-unregister.
        
        Equivalent to Java's catalog.register() for try-with-resources pattern.
        Automatically unregisters the catalog when exiting the context.
        
        Args:
            service: Optional LocalService instance. Uses singleton if not provided.
        
        Returns:
            RegisteredCatalog context manager that yields the catalog ID
        
        Example:
            >>> catalog = CatalogBuilder("db").add_table(table).build()
            >>> with catalog.register() as catalog_id:
            ...     # Use catalog_id for operations
            ...     response = service.analyze(
            ...         sql_statement="SELECT * FROM table",
            ...         registered_catalog_id=catalog_id
            ...     )
            ...     # Automatically unregistered on exit
        
        See Also:
            RegisteredCatalog: The context manager implementation
        """
        if service is None:
            from zetasql.core.local_service import ZetaSqlLocalService
            service = ZetaSqlLocalService.get_instance()
        
        from zetasql.api.catalog_registry import RegisteredCatalog
        return RegisteredCatalog(service, self)
