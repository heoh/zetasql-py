"""Catalog registry helpers for automatic resource management.

Provides context manager for registered catalogs with automatic cleanup.
"""

from typing import Optional


class RegisteredCatalog:
    """Context manager for registered catalogs.
    
    Equivalent to Java's SimpleCatalog.AutoUnregister.
    Automatically unregisters the catalog when exiting context.
    
    Example:
        >>> catalog = CatalogBuilder("db").add_table(table).build()
        >>> with catalog.register() as catalog_id:
        ...     response = service.analyze(
        ...         sql_statement="SELECT * FROM table",
        ...         registered_catalog_id=catalog_id
        ...     )
        ...     # Automatically unregistered on exit
    """
    
    def __init__(self, service, catalog):
        """Initialize RegisteredCatalog.
        
        Args:
            service: ZetaSqlLocalService instance
            catalog: SimpleCatalog to register
        """
        self._service = service
        self._catalog = catalog
        self._registered_id = None
    
    @property
    def registered_id(self) -> Optional[int]:
        """Get registered catalog ID.
        
        Returns:
            Catalog ID if registered, None otherwise
        """
        return self._registered_id
    
    def __enter__(self) -> int:
        """Register catalog and return ID.
        
        Returns:
            Registered catalog ID
        """
        response = self._service.register_catalog(
            simple_catalog=self._catalog
        )
        self._registered_id = response.registered_id
        return self._registered_id
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Unregister catalog on exit.
        
        Suppresses unregister errors during cleanup to avoid
        masking the original exception.
        """
        if self._registered_id is not None:
            try:
                self._service.unregister_catalog(
                    registered_id=self._registered_id
                )
            except Exception:
                # Suppress unregister errors during cleanup
                # to avoid masking the original exception
                pass
        return False
