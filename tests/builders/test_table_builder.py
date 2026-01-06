"""
TableBuilder tests - fluent API for building SimpleTable objects
"""

import pytest
from zetasql.api import TypeFactory
from zetasql.api.builders import TableBuilder
from zetasql.types import SimpleTable, TypeKind


class TestTableBuilder:
    """Test TableBuilder functionality."""
    
    def test_simple_table_creation(self):
        """Test creating a simple table with basic columns."""
        table = (TableBuilder("users")
            .add_column("id", TypeKind.TYPE_INT64)
            .add_column("name", TypeKind.TYPE_STRING)
            .add_column("email", TypeKind.TYPE_STRING)
            .build())
        
        assert isinstance(table, SimpleTable)
        assert table.name == "users"
        assert len(table.column) == 3
        
        # Verify column details
        assert table.column[0].name == "id"
        assert table.column[0].type.type_kind == TypeKind.TYPE_INT64
        assert table.column[1].name == "name"
        assert table.column[1].type.type_kind == TypeKind.TYPE_STRING
        assert table.column[2].name == "email"
        assert table.column[2].type.type_kind == TypeKind.TYPE_STRING
    
    def test_table_with_serialization_id(self):
        """Test table with explicit serialization ID."""
        table = (TableBuilder("products", serialization_id=42)
            .add_column("product_id", TypeKind.TYPE_INT64)
            .build())
        
        assert table.serialization_id == 42
        assert table.name == "products"
    
    def test_table_auto_serialization_id(self):
        """Test that serialization_id is None by default (backend assigns)."""
        table1 = TableBuilder("table1").build()
        table2 = TableBuilder("table2").build()
        
        # Both should be None (backend will assign)
        assert table1.serialization_id is None
        assert table2.serialization_id is None
        
        # Proto should not have the field set
        proto1 = table1.to_proto()
        assert not proto1.HasField('serialization_id')
    
    def test_table_with_array_column(self):
        """Test adding column with array type."""
        array_type = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        table = (TableBuilder("items")
            .add_column("item_id", TypeKind.TYPE_INT64)
            .add_column("tags", array_type)
            .build())
        
        assert len(table.column) == 2
        assert table.column[1].name == "tags"
        assert table.column[1].type.type_kind == TypeKind.TYPE_ARRAY
        # Verify element type
        assert table.column[1].type.array_type.element_type.type_kind == TypeKind.TYPE_STRING
    
    def test_table_with_struct_column(self):
        """Test adding struct type column."""
        address_type = TypeFactory.create_struct_type([
            ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("zipcode", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
        ])
        
        table = (TableBuilder("customers")
            .add_column("customer_id", TypeKind.TYPE_INT64)
            .add_column("address", address_type)
            .build())
        
        assert len(table.column) == 2
        assert table.column[1].type.type_kind == TypeKind.TYPE_STRUCT
        # Verify struct fields
        struct_fields = table.column[1].type.struct_type.field
        assert len(struct_fields) == 3
        assert struct_fields[0].field_name == "street"
        assert struct_fields[1].field_name == "city"
        assert struct_fields[2].field_name == "zipcode"
    
    def test_table_with_nested_array(self):
        """Test table with nested array type (array of arrays)."""
        nested_array = TypeFactory.create_array_type(
            TypeFactory.create_array_type(
                TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
            )
        )
        
        table = (TableBuilder("matrix")
            .add_column("id", TypeKind.TYPE_INT64)
            .add_column("data", nested_array)
            .build())
        
        assert table.column[1].type.type_kind == TypeKind.TYPE_ARRAY
        # Verify it's array of array
        inner_type = table.column[1].type.array_type.element_type
        assert inner_type.type_kind == TypeKind.TYPE_ARRAY
        assert inner_type.array_type.element_type.type_kind == TypeKind.TYPE_INT64
    
    def test_value_table(self):
        """Test creating a value table."""
        table = (TableBuilder("value_table")
            .add_column("value", TypeKind.TYPE_STRING)
            .as_value_table()
            .build())
        
        assert table.is_value_table is True
        assert len(table.column) == 1
    
    def test_method_chaining(self):
        """Test that all builder methods support chaining."""
        table = (TableBuilder("chained")
            .add_column("col1", TypeKind.TYPE_INT64)
            .add_column("col2", TypeKind.TYPE_STRING)
            .add_column("col3", TypeKind.TYPE_DOUBLE)
            .with_serialization_id(100)
            .build())
        
        assert table.name == "chained"
        assert table.serialization_id == 100
        assert len(table.column) == 3
    
    def test_table_protomodel_instance(self):
        """Test that built table is a ProtoModel instance."""
        table = (TableBuilder("test")
            .add_column("id", TypeKind.TYPE_INT64)
            .build())
        
        # Should be a SimpleTable ProtoModel
        assert isinstance(table, SimpleTable)
        assert hasattr(table, 'to_proto')  # Has ProtoModel methods
        assert hasattr(table, 'from_proto')
        assert table.name == "test"
        assert len(table.column) == 1
    
    def test_empty_table(self):
        """Test creating table with no columns (edge case)."""
        table = TableBuilder("empty").build()
        
        assert table.name == "empty"
        assert len(table.column) == 0
    
    def test_multiple_tables_independent(self):
        """Test that multiple builder instances are independent."""
        table1 = TableBuilder("table1").add_column("a", TypeKind.TYPE_INT64).build()
        table2 = TableBuilder("table2").add_column("b", TypeKind.TYPE_STRING).build()
        
        # Should be different instances
        assert table1.name != table2.name
        assert table1.column[0].name != table2.column[0].name
        assert table1.column[0].type.type_kind != table2.column[0].type.type_kind
