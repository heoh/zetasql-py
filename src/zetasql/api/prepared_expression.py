"""PreparedExpression wrapper for ZetaSQL expression evaluation.

Provides Java-style PreparedExpression API wrapping the proto-based service.
Allows preparing, evaluating, and managing SQL expressions.
"""

from typing import Dict, Optional, Any
from zetasql.api.value import Value
from zetasql.core import local_service, types


class PreparedExpression:
    """Wrapper for prepared SQL expression with Java-style API.
    
    Allows preparing and evaluating SQL expressions with parameters and column values.
    Follows the same pattern as PreparedQuery but for expressions.
    
    Example:
        >>> from zetasql.api import PreparedExpression, Value
        >>> service = local_service.ZetaSqlLocalService()
        >>> expr = PreparedExpression("column1 + @param", service)
        >>> expr.add_column("column1", types.Type(type_kind=types.TypeKind.TYPE_INT64))
        >>> expr.add_parameter("param", types.Type(type_kind=types.TypeKind.TYPE_INT64))
        >>> result = expr.execute({"column1": Value.int64(10), "param": Value.int64(5)})
        >>> assert result.get_int64() == 15
    """
    
    def __init__(self, expression: str, service: Optional[local_service.ZetaSqlLocalService] = None):
        """Initialize PreparedExpression.
        
        Args:
            expression: SQL expression string
            service: ZetaSqlLocalService instance (creates new one if None)
        """
        self._expression = expression
        self._service = service or local_service.ZetaSqlLocalService()
        self._columns: Dict[str, types.Type] = {}
        self._parameters: Dict[str, types.Type] = {}
        self._prepared_expression_id: Optional[int] = None
        self._prepared = False
        
    def add_column(self, name: str, type_: types.Type) -> 'PreparedExpression':
        """Add column definition.
        
        Args:
            name: Column name
            type_: Column type
            
        Returns:
            Self for chaining
        """
        self._columns[name] = type_
        return self
        
    def add_parameter(self, name: str, type_: types.Type) -> 'PreparedExpression':
        """Add parameter definition.
        
        Args:
            name: Parameter name
            type_: Parameter type
            
        Returns:
            Self for chaining
        """
        self._parameters[name] = type_
        return self
    
    def prepare(self) -> 'PreparedExpression':
        """Prepare the expression for execution.
        
        Returns:
            Self for chaining
        """
        if self._prepared:
            return self
            
        # Build AnalyzerOptions with builtin functions enabled
        options = types.AnalyzerOptions()
        if not options.language_options:
            options.language_options = types.LanguageOptions()
        options.language_options.enable_all_builtins()
        
        # Add columns
        for name, type_ in self._columns.items():
            column = types.NameAndType(name=name, type_=type_)
            options.expression_columns.append(column)
        
        # Add parameters
        for name, type_ in self._parameters.items():
            param = types.QueryParameter(name=name, type_=type_)
            options.query_parameters.append(param)
        
        # Call service with keyword arguments
        response = self._service.prepare(
            sql=self._expression,
            options=options
        )
        self._prepared_expression_id = response.prepared.prepared_expression_id
        self._prepared = True
        
        return self
    
    def execute(self, values: Optional[Dict[str, Value]] = None) -> Value:
        """Execute the prepared expression with column/parameter values.
        
        Args:
            values: Dictionary mapping column/parameter names to Values
            
        Returns:
            Result Value
        """
        if not self._prepared:
            self.prepare()
        
        # Build EvaluateRequest
        request = types.EvaluateRequest(
            prepared_expression_id=self._prepared_expression_id
        )
        
        # Add column and parameter values
        if values:
            for name, value in values.items():
                request.columns[name] = value.to_proto()
                request.params[name] = value.to_proto()
        
        # Call service
        response = self._service.evaluate(request)
        
        # Return Value from response
        return Value.from_proto(response.value)
    
    def close(self):
        """Release prepared expression resources."""
        if self._prepared and self._prepared_expression_id is not None:
            request = types.UnprepareRequest(
                prepared_expression_id=self._prepared_expression_id
            )
            self._service.unprepare(request)
            self._prepared = False
            self._prepared_expression_id = None
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
        return False
