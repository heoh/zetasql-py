"""PreparedQuery wrapper for automatic resource management.

Provides Java-style PreparedQuery with context manager support
for automatic cleanup of server-side resources.
"""

import contextlib
from typing import Any

import zetasql.types
from zetasql.core import IllegalStateError, InvalidArgumentError, ZetaSqlLocalService


class PreparedQuery:
    """Context manager for prepared queries with automatic cleanup.

    Equivalent to Java's PreparedQuery with AutoCloseable support.
    Automatically releases server-side resources when exiting context.

    Example:
        >>> with PreparedQuery.builder() \\
        ...         .set_sql("SELECT * FROM Orders") \\
        ...         .set_analyzer_options(options) \\
        ...         .set_catalog(catalog) \\
        ...         .prepare() as query:
        ...     result = query.execute()
        ...     # Automatically cleaned up on exit
    """

    def __init__(self, service: ZetaSqlLocalService, prepared_id: int, columns: list):
        """Initialize PreparedQuery.

        Args:
            service: ZetaSqlLocalService instance
            prepared_id: Server-side prepared query ID
            columns: List of output column metadata
        """
        self._service = service
        self._prepared_id = prepared_id
        self._columns = columns
        self._closed = False

    @property
    def prepared_query_id(self) -> int:
        """Get prepared query ID.

        Returns:
            Server-side prepared query identifier
        """
        return self._prepared_id

    @property
    def columns(self) -> list:
        """Get output column metadata.

        Returns:
            List of column descriptors (name, type, etc.)
        """
        return self._columns

    def execute(self, parameters: dict[str, Any] | None = None, table_content: dict[str, Any] | None = None):
        """Execute the prepared query.

        Args:
            parameters: Optional query parameters (for parameterized queries)
            table_content: Optional table content override

        Returns:
            EvaluateQueryResponse with query results

        Raises:
            IllegalStateError: If query has already been closed

        Example:
            >>> response = query.execute()
            >>> for row in response.content.table_data.row:
            ...     print(row)
        """
        if self._closed:
            raise IllegalStateError("PreparedQuery already closed. Cannot execute closed query.")

        response = self._service.evaluate_query(
            prepared_query_id=self._prepared_id,
            params=parameters or {},
            table_content=table_content or {},
        )
        return response

    def close(self):
        """Release server-side resources. Safe to call multiple times."""
        if not self._closed:
            try:
                self._service.unprepare_query(prepared_query_id=self._prepared_id)
            finally:
                self._closed = True

    def __enter__(self):
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager and cleanup resources."""
        self.close()
        return False

    def __del__(self):
        """Cleanup on garbage collection. Explicit close() or context manager usage is preferred."""
        if not self._closed:
            with contextlib.suppress(Exception):
                self.close()

    @staticmethod
    def builder():
        """Create a new PreparedQueryBuilder.

        Returns:
            PreparedQueryBuilder instance for fluent API

        Example:
            >>> query = PreparedQuery.builder() \\
            ...     .set_sql("SELECT * FROM Orders") \\
            ...     .set_analyzer_options(options) \\
            ...     .prepare()
        """
        return PreparedQueryBuilder()


class PreparedQueryBuilder:
    """Builder for PreparedQuery with fluent API.

    Equivalent to Java's PreparedQuery.Builder pattern.
    Provides method chaining for convenient query preparation.

    Example:
        >>> builder = PreparedQueryBuilder()
        >>> builder.set_sql("SELECT id FROM Orders") \\
        ...        .set_analyzer_options(options) \\
        ...        .set_catalog(catalog) \\
        ...        .set_table_content({"Orders": orders_data})
        >>> with builder.prepare() as query:
        ...     result = query.execute()
    """

    def __init__(self):
        """Initialize empty builder."""
        self._sql = None
        self._options = None
        self._catalog = None
        self._registered_catalog_id = None
        self._table_content = None
        self._service = None

    def set_sql(self, sql: str):
        """Set SQL query string.

        Args:
            sql: SQL query to prepare

        Returns:
            Self for method chaining
        """
        self._sql = sql
        return self

    def set_analyzer_options(self, options: zetasql.types.AnalyzerOptions):
        """Set analyzer options.

        Args:
            options: Analyzer options for query analysis

        Returns:
            Self for method chaining
        """
        self._options = options
        return self

    def set_catalog(self, catalog: zetasql.types.SimpleCatalog):
        """Set unregistered catalog.

        Args:
            catalog: Simple catalog with tables and functions

        Returns:
            Self for method chaining

        Note:
            Mutually exclusive with set_registered_catalog_id()
        """
        self._catalog = catalog
        return self

    def set_registered_catalog_id(self, catalog_id: int):
        """Set registered catalog ID.

        Args:
            catalog_id: ID of previously registered catalog

        Returns:
            Self for method chaining

        Note:
            Mutually exclusive with set_catalog()
        """
        self._registered_catalog_id = catalog_id
        return self

    def set_table_content(self, table_content: dict[str, Any]):
        """Set table content for execution.

        Args:
            table_content: Dict mapping table names to TableContent objects

        Returns:
            Self for method chaining

        Note:
            Only valid with set_catalog(), not with registered catalog
        """
        self._table_content = table_content
        return self

    def set_service(self, service):
        """Set custom service instance (optional).

        Args:
            service: ZetaSqlLocalService instance

        Returns:
            Self for method chaining

        Note:
            If not set, uses singleton instance
        """
        self._service = service
        return self

    def prepare(self) -> PreparedQuery:
        """Prepare the query and return PreparedQuery instance.

        Returns:
            PreparedQuery instance ready for execution

        Raises:
            InvalidArgumentError: If required parameters are missing or invalid

        Example:
            >>> query = builder.prepare()
            >>> try:
            ...     result = query.execute()
            ... finally:
            ...     query.close()
        """
        # Validation - SQL is required
        if not self._sql:
            raise InvalidArgumentError("SQL must be set")

        # Validate SQL is not just whitespace
        if not self._sql.strip():
            raise InvalidArgumentError("SQL string must not be empty or whitespace-only")

        # Mutually exclusive parameters
        if self._catalog and self._registered_catalog_id:
            raise InvalidArgumentError("Cannot provide both catalog and registered_catalog_id. Use one or the other.")

        # table_content requires simple_catalog
        if self._table_content and self._registered_catalog_id:
            raise InvalidArgumentError(
                "Cannot use table_content with registered catalog. table_content requires simple_catalog.",
            )

        service = self._service or ZetaSqlLocalService.get_instance()

        response = service.prepare_query(
            sql=self._sql,
            options=self._options,
            simple_catalog=self._catalog,
            registered_catalog_id=self._registered_catalog_id,
            table_content=self._table_content or {},
        )

        return PreparedQuery(
            service=service,
            prepared_id=response.prepared.prepared_query_id,
            columns=response.prepared.columns,
        )
