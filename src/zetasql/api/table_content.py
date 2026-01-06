"""
Table Content Factory - Helper for creating TableContent for query execution

This module provides a simple factory function for creating TableContent ProtoModel
objects from Python data, eliminating the need to work with protobuf directly.

Examples:
    >>> from zetasql.api import create_table_content
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

from typing import Any

from zetasql.types import TableContent, TableData, Value


def create_table_content(rows_data: list[list[Any]]) -> TableContent:
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

    def create_cell_value(value: Any) -> Value:
        """Convert Python value to Value ProtoModel."""
        if value is None:
            return Value()
        if isinstance(value, bool):
            return Value(bool_value=value)
        if isinstance(value, int):
            return Value(int64_value=value)
        if isinstance(value, float):
            return Value(double_value=value)
        if isinstance(value, str):
            return Value(string_value=value)
        raise ValueError(
            f"Unsupported value type: {type(value).__name__}. Supported types: None, bool, int, float, str",
        )

    rows = [TableData.Row(cell=[create_cell_value(value) for value in row_data]) for row_data in rows_data]

    table_data = TableData(row=rows)
    return TableContent(table_data=table_data)


__all__ = ["create_table_content"]
