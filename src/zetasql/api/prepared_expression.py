"""PreparedExpression wrapper for ZetaSQL expression evaluation.

Provides Java-style PreparedExpression API wrapping the proto-based service.
Mirrors Java PreparedExpression functionality for evaluating SQL expressions.
"""

from typing import Dict, Optional, Any
from zetasql.api.value import Value
from zetasql.core import ZetaSqlLocalService, types, ServerError


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
        options: Optional['types.AnalyzerOptions'] = None,
        catalog: Optional[Any] = None,
        service: Optional[ZetaSqlLocalService] = None,
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
        self._prepared_expression_id: Optional[int] = None
        self._prepared = False
        self._closed = False
        self._output_type: Optional['types.Type'] = None
        self._referenced_columns = []
        self._referenced_parameters = []
        
    @property
    def output_type(self) -> 'types.Type':
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
    
    def _prepare(self, options: Optional['types.AnalyzerOptions'] = None) -> 'PreparedExpression':
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
        
        # Use provided options or create default
        analyze_options = self._options or types.AnalyzerOptions()
        
        # Call service with keyword arguments (service expects individual params)
        try:
            if self._catalog is not None:
                response = self._service.prepare(
                    sql=self._sql,
                    options=analyze_options,
                    simple_catalog=self._catalog
                )
            else:
                response = self._service.prepare(
                    sql=self._sql,
                    options=analyze_options
                )
        except ServerError:
            raise
        
        # Store prepared state
        self._prepared_expression_id = response.prepared.prepared_expression_id
        self._output_type = response.prepared.output_type
        self._referenced_columns = list(response.prepared.referenced_columns)
        self._referenced_parameters = list(response.prepared.referenced_parameters)
        self._prepared = True
        
        return self
    
    def execute(
        self, 
        columns: Optional[Dict[str, Value]] = None,
        parameters: Optional[Dict[str, Value]] = None
    ) -> Value:
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
        
        # Default to empty dicts
        columns = columns or {}
        parameters = parameters or {}
        
        # If not prepared, we need to prepare with inferred types
        if not self._prepared:
            # Add parameter and column types to options before preparing
            if self._options is None:
                self._options = types.AnalyzerOptions()
            
            # Add expression columns based on provided values
            for name, value in columns.items():
                # Create Type from Value's type_kind
                col_type = types.Type(type_kind=value.type_kind)
                # Note: expression_columns expects proto format, not ProtoModel
                # We'll add it during prepare or let evaluate handle it
                # For now, skip auto-adding columns as it's complex
                pass
            
            # Add query parameters based on provided values
            for name, value in parameters.items():
                # Create Type from Value's type_kind
                param_type = types.Type(type_kind=value.type_kind)
                param = types.AnalyzerOptions.QueryParameter(
                    name=name,
                    type=param_type
                )
                # Check if parameter already exists
                param_exists = any(p.name.lower() == name.lower() for p in self._options.query_parameters)
                if not param_exists:
                    self._options.query_parameters.append(param)
            
            self._prepare()
        
        # Build column and parameter lists
        column_params = []
        for name, value in columns.items():
            param = types.EvaluateRequest.Parameter(
                name=name.lower(),  # Normalize to lowercase
                value=value.to_proto()
            )
            column_params.append(param)
        
        param_params = []
        for name, value in parameters.items():
            param = types.EvaluateRequest.Parameter(
                name=name.lower(),  # Normalize to lowercase
                value=value.to_proto()
            )
            param_params.append(param)
        
        # Call service with keyword arguments
        try:
            response = self._service.evaluate(
                prepared_expression_id=self._prepared_expression_id,
                columns=column_params,
                params=param_params
            )
        except ServerError:
            raise
        
        # If not prepared before, store prepared state from response
        if response.prepared and response.prepared.prepared_expression_id:
            self._prepared_expression_id = response.prepared.prepared_expression_id
            self._output_type = response.prepared.output_type
            self._referenced_columns = list(response.prepared.referenced_columns)
            self._referenced_parameters = list(response.prepared.referenced_parameters)
            self._prepared = True
        
        # Return Value from response
        return Value.from_proto(response.value)
    
    def close(self):
        """Release prepared expression resources."""
        if self._prepared and not self._closed and self._prepared_expression_id is not None:
            try:
                request = types.UnprepareRequest(
                    prepared_expression_id=self._prepared_expression_id
                )
                self._service.unprepare(request)
            except Exception:
                # Ignore errors during cleanup
                pass
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
            self.close()
