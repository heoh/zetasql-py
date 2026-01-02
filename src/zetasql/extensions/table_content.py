"""
Table Content Factory - Helper for creating TableContent for query execution

This module provides a simple factory function for creating TableContent ProtoModel
objects from Python data, eliminating the need to work with protobuf directly.

Examples:
    >>> from zetasql.table_content import create_table_content
    >>> 
    >>> # Simple data
    >>> data = [
    ...     [1, "Alice", True],
    ...     [2, "Bob", False]
    ... ]
    >>> content = create_table_content(data)
    >>> 
    >>> # Use with LocalService
    >>> service.prepare_query(sql=sql, simple_catalog=catalog, table_content={"users": content})
"""

from typing import List, Any
from zetasql.types.proto_models import TableContent, TableData, Value


def create_table_content(rows_data: List[List[Any]]) -> TableContent:
    """Create TableContent ProtoModel from row data.
    
    This helper function builds table data for query execution, automatically
    detecting Python types and converting them to appropriate Value fields.
    
    Args:
        rows_data: List of lists, where each inner list represents a row.
                   Supported types: None, bool, int, float, str
                   
                   Example: [
                       ["Alice", 25, True],
                       ["Bob", 30, False]
                   ]
    
    Returns:
        TableContent ProtoModel ready for use with LocalService
    
    Examples:
        >>> # Simple table data
        >>> customers = create_table_content([
        ...     [1, "Alice", "alice@example.com"],
        ...     [2, "Bob", "bob@example.com"]
        ... ])
        >>> 
        >>> # With null values
        >>> data = create_table_content([
        ...     [1, "Alice", None],
        ...     [2, None, "test@example.com"]
        ... ])
        >>> 
        >>> # Use in query execution
        >>> table_content = {
        ...     "customers": create_table_content(customer_data),
        ...     "products": create_table_content(product_data)
        ... }
        >>> response = service.prepare_query(
        ...     sql="SELECT * FROM customers",
        ...     simple_catalog=catalog,
        ...     table_content=table_content
        ... )
    
    Raises:
        ValueError: If an unsupported value type is encountered
    """
    rows = []
    
    for row_data in rows_data:
        cells = []
        for value in row_data:
            # Create Value ProtoModel for each cell
            if value is None:
                # Null value - no field set, but we could add a marker if needed
                # For now, just create empty Value (will be treated as NULL)
                cells.append(Value())
            elif isinstance(value, bool):
                cells.append(Value(bool_value=value))
            elif isinstance(value, int):
                cells.append(Value(int64_value=value))
            elif isinstance(value, float):
                cells.append(Value(double_value=value))
            elif isinstance(value, str):
                cells.append(Value(string_value=value))
            else:
                raise ValueError(
                    f"Unsupported value type: {type(value).__name__}. "
                    f"Supported types: None, bool, int, float, str"
                )
        
        # Create Row with cells
        rows.append(TableData.Row(cell=cells))
    
    # Create TableData with rows
    table_data = TableData(row=rows)
    
    # Create and return TableContent
    return TableContent(table_data=table_data)


__all__ = ['create_table_content']
