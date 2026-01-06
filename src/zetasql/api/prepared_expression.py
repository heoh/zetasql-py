"""PreparedExpression wrapper for ZetaSQL expression evaluation.

Provides Java-style PreparedExpression API wrapping the proto-based service.
Mirrors Java PreparedExpression functionality for evaluating SQL expressions.
"""

import contextlib
from typing import TYPE_CHECKING, Any, Optional

from zetasql import types
from zetasql.api.value import Value
from zetasql.core import ZetaSqlLocalService

if TYPE_CHECKING:
    from zetasql.types import TypeKind


class PreparedExpression:
    """Wrapper for prepared SQL expression with Java-style API.

    Mirrors Java PreparedExpression for evaluating SQL expressions with parameters
    and column values. Supports automatic preparation on first execute or explicit
    prepare() call.

    Example:
        >>> from zetasql.api import PreparedExpression, Value
        >>> from zetasql.types import AnalyzerOptions
        >>>
        >>> options = AnalyzerOptions()
        >>> expr = PreparedExpression("1 + 2", options, catalog)
        >>> result = expr.execute()
        >>> assert result.get_int64() == 3
        >>>
        >>> # With parameters
        >>> expr2 = PreparedExpression("@x + @y", options, catalog)
        >>> result = expr2.execute(parameters={"x": Value.int32(10), "y": Value.int32(20)})
        >>> assert result.get_int64() == 30
    """

    def __init__(
        self,
        sql: str,
        options: Optional["types.AnalyzerOptions"] = None,
        catalog: Any | None = None,
        service: ZetaSqlLocalService | None = None,
    ):
        """Initialize PreparedExpression.

        Args:
            sql: SQL expression string
            options: AnalyzerOptions for configuring analysis
            catalog: SimpleCatalog with tables/functions (optional)
        """
        self._sql = sql
        self._options = options
        self._catalog = catalog
        self._service = service or ZetaSqlLocalService.get_instance()
        self._prepared_expression_id: int | None = None
        self._prepared = False
        self._closed = False
        self._output_type: types.Type | None = None
        self._referenced_columns = []
        self._referenced_parameters = []

    @property
    def output_type(self) -> "types.Type":
        """Get the output type of this expression.

        Automatically prepares the expression if not yet prepared.

        Returns:
            Type of the expression result

        Raises:
            RuntimeError: If closed
        """
        if self._closed:
            raise RuntimeError("Expression has been closed")
        if not self._prepared:
            self._prepare()
        return self._output_type

    def get_referenced_columns(self):
        """Get list of column names referenced in this expression.

        Returns:
            List of column names (lowercase)
        """
        if not self._prepared:
            raise RuntimeError("Expression not yet prepared")
        if self._closed:
            raise RuntimeError("Expression has been closed")
        return self._referenced_columns

    def get_referenced_parameters(self):
        """Get list of parameters referenced in this expression.

        Returns:
            List of parameter names (lowercase)
        """
        if not self._prepared:
            raise RuntimeError("Expression not yet prepared")
        if self._closed:
            raise RuntimeError("Expression has been closed")
        return self._referenced_parameters

    def _prepare(self, options: Optional["types.AnalyzerOptions"] = None) -> "PreparedExpression":
        """Explicitly prepare the expression for execution.

        Args:
            options: AnalyzerOptions (overrides constructor options if provided)

        Returns:
            Self for chaining

        Raises:
            RuntimeError: If already closed
            ServerError: On preparation error
        """
        if self._prepared:
            return self  # Already prepared
        if self._closed:
            raise RuntimeError("Expression has been closed")

        if options is not None:
            self._options = options

        analyze_options = self._options or types.AnalyzerOptions()

        response = self._service.prepare(sql=self._sql, options=analyze_options, simple_catalog=self._catalog)

        self._prepared_expression_id = response.prepared.prepared_expression_id
        self._output_type = response.prepared.output_type
        self._referenced_columns = list(response.prepared.referenced_columns)
        self._referenced_parameters = list(response.prepared.referenced_parameters)
        self._prepared = True

        return self

    def _add_inferred_types(self, columns: dict[str, Value], parameters: dict[str, Value]) -> None:
        """Add inferred types from column and parameter values to options.

        Args:
            columns: Dictionary mapping column names to Value objects
            parameters: Dictionary mapping parameter names to Value objects
        """
        if self._options is None:
            self._options = types.AnalyzerOptions()

        for name, value in columns.items():
            col_param = types.AnalyzerOptions.QueryParameter(name=name, type=value.get_type())
            if not any(c.name.lower() == name.lower() for c in self._options.expression_columns):
                self._options.expression_columns.append(col_param)

        for name, value in parameters.items():
            param = types.AnalyzerOptions.QueryParameter(name=name, type=value.get_type())
            if not any(p.name.lower() == name.lower() for p in self._options.query_parameters):
                self._options.query_parameters.append(param)

    def execute(self, columns: dict[str, Value] | None = None, parameters: dict[str, Value] | None = None) -> Value:
        """Execute the expression with column/parameter values.

        Supports flexible calling:
        - execute() - no columns/parameters
        - execute(parameters={...}) - parameters only
        - execute(columns={...}, parameters={...}) - both

        Args:
            columns: Dictionary mapping column names to Value objects
            parameters: Dictionary mapping parameter names to Value objects

        Returns:
            Result Value

        Raises:
            ServerError: On evaluation error
        """
        if self._closed:
            raise RuntimeError("Expression has been closed")

        columns = columns or {}
        parameters = parameters or {}

        if not self._prepared:
            self._add_inferred_types(columns, parameters)
            self._prepare()

        column_params = [
            types.EvaluateRequest.Parameter(name=name.lower(), value=value.to_proto())
            for name, value in columns.items()
        ]

        param_params = [
            types.EvaluateRequest.Parameter(name=name.lower(), value=value.to_proto())
            for name, value in parameters.items()
        ]

        response = self._service.evaluate(
            prepared_expression_id=self._prepared_expression_id,
            columns=column_params,
            params=param_params,
        )

        if response.prepared and response.prepared.prepared_expression_id:
            self._prepared_expression_id = response.prepared.prepared_expression_id
            self._output_type = response.prepared.output_type
            self._referenced_columns = list(response.prepared.referenced_columns)
            self._referenced_parameters = list(response.prepared.referenced_parameters)
            self._prepared = True

        return Value.from_proto(response.value)

    def close(self):
        """Release prepared expression resources."""
        if self._prepared and not self._closed and self._prepared_expression_id is not None:
            try:
                self._service.unprepare(prepared_expression_id=self._prepared_expression_id)
            finally:
                self._closed = True

    def __enter__(self):
        """Context manager entry."""
        self._prepare()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
        return False

    def __del__(self):
        """Cleanup on deletion."""
        if not self._closed:
            with contextlib.suppress(Exception):
                self.close()

    @staticmethod
    def builder() -> "PreparedExpression.Builder":
        """Create a new PreparedExpression builder.

        Returns:
            Builder instance for fluent construction

        Example:
            >>> expr = (PreparedExpression.builder()
            ...     .expression("@x + @y")
            ...     .options(options)
            ...     .catalog(catalog)
            ...     .build())
        """
        return PreparedExpression.Builder()

    class Builder:
        """Builder for constructing PreparedExpression instances.

        Provides a fluent interface for configuring and building PreparedExpression
        objects, similar to Java's builder pattern.

        Example:
            >>> builder = PreparedExpression.builder()
            >>> expr = (builder
            ...     .expression("@x + @y")
            ...     .options(options)
            ...     .catalog(catalog)
            ...     .build())
        """

        def __init__(self):
            """Initialize empty builder."""
            self._sql: str | None = None
            self._options: types.AnalyzerOptions | None = None
            self._catalog: Any | None = None
            self._service: ZetaSqlLocalService | None = None
            self._columns: dict[str, types.Type] = {}

        def expression(self, sql: str) -> "PreparedExpression.Builder":
            """Set the SQL expression.

            Args:
                sql: SQL expression string

            Returns:
                Self for chaining
            """
            self._sql = sql
            return self

        def options(self, options: "types.AnalyzerOptions") -> "PreparedExpression.Builder":
            """Set analyzer options.

            Args:
                options: AnalyzerOptions for configuring analysis

            Returns:
                Self for chaining
            """
            self._options = options
            return self

        def catalog(self, catalog: Any) -> "PreparedExpression.Builder":
            """Set the catalog.

            Args:
                catalog: SimpleCatalog with tables/functions

            Returns:
                Self for chaining
            """
            self._catalog = catalog
            return self

        def service(self, service: ZetaSqlLocalService) -> "PreparedExpression.Builder":
            """Set the service instance.

            Args:
                service: ZetaSqlLocalService instance

            Returns:
                Self for chaining
            """
            self._service = service
            return self

        def column(self, name: str, type_kind: "TypeKind") -> "PreparedExpression.Builder":
            """Add an expression column definition.

            Args:
                name: Column name
                type_kind: TypeKind for the column

            Returns:
                Self for chaining

            Example:
                >>> builder.column("age", TypeKind.TYPE_INT64)
            """
            self._columns[name] = types.Type(type_kind=type_kind)
            return self

        def build(self) -> "PreparedExpression":
            """Build the PreparedExpression instance.

            Returns:
                Configured PreparedExpression

            Raises:
                ValueError: If required fields are missing
            """
            if self._sql is None:
                raise ValueError("SQL expression is required")

            # Create the PreparedExpression
            expr = PreparedExpression(
                sql=self._sql,
                options=self._options,
                catalog=self._catalog,
                service=self._service,
            )

            # Add column definitions to options if provided
            if self._columns:
                if expr._options is None:
                    expr._options = types.AnalyzerOptions()

                for name, col_type in self._columns.items():
                    col_param = types.AnalyzerOptions.QueryParameter(name=name, type=col_type)
                    # Check if column already exists
                    col_exists = any(c.name.lower() == name.lower() for c in expr._options.expression_columns)
                    if not col_exists:
                        expr._options.expression_columns.append(col_param)

            return expr
