"""
Tests for table_content module

Tests the create_table_content factory function.
"""

import pytest

from zetasql.api import create_table_content
from zetasql.types import TableContent


class TestCreateTableContent:
    """Test create_table_content factory function."""

    def test_empty_table(self):
        """Test creating empty table content."""
        content = create_table_content([])

        assert isinstance(content, TableContent)
        assert content.table_data is not None
        assert len(content.table_data.row) == 0

    def test_simple_integer_data(self):
        """Test creating table with integer data."""
        data = [[1, 2, 3], [4, 5, 6]]
        content = create_table_content(data)

        assert len(content.table_data.row) == 2
        assert len(content.table_data.row[0].cell) == 3

        # Check first row values
        assert content.table_data.row[0].cell[0].int64_value == 1
        assert content.table_data.row[0].cell[1].int64_value == 2
        assert content.table_data.row[0].cell[2].int64_value == 3

    def test_string_data(self):
        """Test creating table with string data."""
        data = [["Alice", "alice@example.com"], ["Bob", "bob@example.com"]]
        content = create_table_content(data)

        assert len(content.table_data.row) == 2
        assert content.table_data.row[0].cell[0].string_value == "Alice"
        assert content.table_data.row[0].cell[1].string_value == "alice@example.com"

    def test_boolean_data(self):
        """Test creating table with boolean data."""
        data = [[True, False], [False, True]]
        content = create_table_content(data)

        assert content.table_data.row[0].cell[0].bool_value is True
        assert content.table_data.row[0].cell[1].bool_value is False

    def test_float_data(self):
        """Test creating table with float data."""
        data = [[1.5, 2.7], [3.14, 9.99]]
        content = create_table_content(data)

        assert content.table_data.row[0].cell[0].double_value == 1.5
        assert content.table_data.row[0].cell[1].double_value == 2.7

    def test_mixed_types(self):
        """Test creating table with mixed types."""
        data = [[1, "Alice", True, 99.99], [2, "Bob", False, 149.99]]
        content = create_table_content(data)

        row = content.table_data.row[0]
        assert row.cell[0].int64_value == 1
        assert row.cell[1].string_value == "Alice"
        assert row.cell[2].bool_value is True
        assert row.cell[3].double_value == 99.99

    def test_null_values(self):
        """Test creating table with None values."""
        data = [[1, None, "Alice"], [None, 2, None]]
        content = create_table_content(data)

        # None values create empty Value objects (all fields None by default)
        assert content.table_data.row[0].cell[1].string_value is None
        assert content.table_data.row[0].cell[1].int64_value is None

    def test_unsupported_type_raises_error(self):
        """Test that unsupported types raise ValueError."""
        data = [
            [1, 2, {"key": "value"}]  # dict not supported
        ]

        with pytest.raises(ValueError) as exc_info:
            create_table_content(data)

        assert "Unsupported value type" in str(exc_info.value)
        assert "dict" in str(exc_info.value)

    def test_variable_row_lengths(self):
        """Test creating table with rows of different lengths."""
        data = [[1, 2, 3], [4, 5], [6]]
        content = create_table_content(data)

        assert len(content.table_data.row[0].cell) == 3
        assert len(content.table_data.row[1].cell) == 2
        assert len(content.table_data.row[2].cell) == 1

    def test_large_dataset(self):
        """Test creating table with many rows."""
        data = [[i, f"name_{i}", i * 1.5] for i in range(100)]
        content = create_table_content(data)

        assert len(content.table_data.row) == 100
        assert content.table_data.row[50].cell[0].int64_value == 50
        assert content.table_data.row[50].cell[1].string_value == "name_50"

    def test_returns_protomodel(self):
        """Test that result is a ProtoModel instance."""
        data = [[1, 2]]
        content = create_table_content(data)

        # Should be TableContent ProtoModel
        assert isinstance(content, TableContent)
        assert hasattr(content, "to_proto")
        assert hasattr(content, "table_data")

    def test_integration_example(self):
        """Test realistic usage scenario."""
        # Customer data
        customers = create_table_content(
            [
                [1, "Alice Johnson", "alice@example.com", "USA"],
                [2, "Bob Smith", "bob@example.com", "Canada"],
                [3, "Charlie Brown", "charlie@example.com", "UK"],
            ]
        )

        # Products data
        products = create_table_content([[101, "Laptop", "Electronics", 999.99], [102, "Mouse", "Electronics", 29.99]])

        # Both should be TableContent ProtoModels
        assert isinstance(customers, TableContent)
        assert isinstance(products, TableContent)

        # Can be used in dictionary for service calls
        table_content = {"customers": customers, "products": products}

        assert len(table_content) == 2
        assert "customers" in table_content
        assert "products" in table_content
