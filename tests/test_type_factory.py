"""
Tests for TypeFactory

Tests the factory methods for creating Type ProtoModel objects.
"""

import pytest
from zetasql.types.type_factory import TypeFactory
from zetasql.types.type_kind import TypeKind
from zetasql.types.proto_models import Type, ArrayType, StructType, MapType


class TestTypeFactorySimpleTypes:
    """Test simple type creation."""
    
    def test_create_simple_type_with_typekind(self):
        """Test creating simple type with TypeKind enum."""
        int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        
        assert isinstance(int_type, Type)
        assert int_type.type_kind == TypeKind.TYPE_INT64
        assert int_type.array_type is None
        assert int_type.struct_type is None
    
    def test_create_simple_type_with_int(self):
        """Test creating simple type with integer constant."""
        str_type = TypeFactory.create_simple_type(8)  # TYPE_STRING = 8
        
        assert isinstance(str_type, Type)
        assert str_type.type_kind == 8
    
    def test_create_all_simple_types(self):
        """Test creating all simple type kinds."""
        simple_types = [
            TypeKind.TYPE_INT32,
            TypeKind.TYPE_INT64,
            TypeKind.TYPE_UINT32,
            TypeKind.TYPE_UINT64,
            TypeKind.TYPE_BOOL,
            TypeKind.TYPE_FLOAT,
            TypeKind.TYPE_DOUBLE,
            TypeKind.TYPE_STRING,
            TypeKind.TYPE_BYTES,
            TypeKind.TYPE_DATE,
            TypeKind.TYPE_TIMESTAMP,
        ]
        
        for type_kind in simple_types:
            type_obj = TypeFactory.create_simple_type(type_kind)
            assert type_obj.type_kind == type_kind


class TestTypeFactoryArrayTypes:
    """Test array type creation."""
    
    def test_create_simple_array(self):
        """Test creating ARRAY<STRING>."""
        element_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        array_type = TypeFactory.create_array_type(element_type)
        
        assert isinstance(array_type, Type)
        assert array_type.type_kind == TypeKind.TYPE_ARRAY
        assert array_type.array_type is not None
        assert array_type.array_type.element_type.type_kind == TypeKind.TYPE_STRING
    
    def test_create_nested_array(self):
        """Test creating ARRAY<ARRAY<INT64>>."""
        int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        inner_array = TypeFactory.create_array_type(int_type)
        outer_array = TypeFactory.create_array_type(inner_array)
        
        assert outer_array.type_kind == TypeKind.TYPE_ARRAY
        assert outer_array.array_type.element_type.type_kind == TypeKind.TYPE_ARRAY
        assert outer_array.array_type.element_type.array_type.element_type.type_kind == TypeKind.TYPE_INT64
    
    def test_to_proto_conversion(self):
        """Test that created types can be converted to protobuf."""
        array_type = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        )
        
        # Should be able to convert to proto
        proto = array_type.to_proto()
        assert proto.type_kind == TypeKind.TYPE_ARRAY


class TestTypeFactoryStructTypes:
    """Test struct type creation."""
    
    def test_create_simple_struct(self):
        """Test creating STRUCT<id INT64, name STRING>."""
        struct_type = TypeFactory.create_struct_type([
            ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
            ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
        ])
        
        assert isinstance(struct_type, Type)
        assert struct_type.type_kind == TypeKind.TYPE_STRUCT
        assert struct_type.struct_type is not None
        assert len(struct_type.struct_type.field) == 2
        
        # Check fields
        assert struct_type.struct_type.field[0].field_name == "id"
        assert struct_type.struct_type.field[0].field_type.type_kind == TypeKind.TYPE_INT64
        assert struct_type.struct_type.field[1].field_name == "name"
        assert struct_type.struct_type.field[1].field_type.type_kind == TypeKind.TYPE_STRING
    
    def test_create_nested_struct(self):
        """Test creating struct with nested struct field."""
        address_type = TypeFactory.create_struct_type([
            ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
        ])
        
        person_type = TypeFactory.create_struct_type([
            ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
            ("address", address_type)
        ])
        
        assert person_type.type_kind == TypeKind.TYPE_STRUCT
        assert len(person_type.struct_type.field) == 2
        assert person_type.struct_type.field[1].field_type.type_kind == TypeKind.TYPE_STRUCT
    
    def test_create_empty_struct(self):
        """Test creating struct with no fields."""
        empty_struct = TypeFactory.create_struct_type([])
        
        assert empty_struct.type_kind == TypeKind.TYPE_STRUCT
        assert len(empty_struct.struct_type.field) == 0


class TestTypeFactoryMapTypes:
    """Test map type creation."""
    
    def test_create_simple_map(self):
        """Test creating MAP<STRING, INT64>."""
        key_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        value_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        map_type = TypeFactory.create_map_type(key_type, value_type)
        
        assert isinstance(map_type, Type)
        assert map_type.type_kind == TypeKind.TYPE_MAP
        assert map_type.map_type is not None
        assert map_type.map_type.key_type.type_kind == TypeKind.TYPE_STRING
        assert map_type.map_type.value_type.type_kind == TypeKind.TYPE_INT64
    
    def test_create_complex_map(self):
        """Test creating MAP<STRING, ARRAY<INT64>>."""
        key_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        value_type = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        )
        map_type = TypeFactory.create_map_type(key_type, value_type)
        
        assert map_type.type_kind == TypeKind.TYPE_MAP
        assert map_type.map_type.value_type.type_kind == TypeKind.TYPE_ARRAY


class TestTypeFactoryComplexScenarios:
    """Test complex type composition."""
    
    def test_array_of_structs(self):
        """Test ARRAY<STRUCT<...>>."""
        person_type = TypeFactory.create_struct_type([
            ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
            ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
        ])
        
        people_array = TypeFactory.create_array_type(person_type)
        
        assert people_array.type_kind == TypeKind.TYPE_ARRAY
        assert people_array.array_type.element_type.type_kind == TypeKind.TYPE_STRUCT
    
    def test_struct_with_array_field(self):
        """Test STRUCT<id INT64, tags ARRAY<STRING>>."""
        tags_array = TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
        )
        
        record_type = TypeFactory.create_struct_type([
            ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
            ("tags", tags_array)
        ])
        
        assert record_type.type_kind == TypeKind.TYPE_STRUCT
        assert record_type.struct_type.field[1].field_type.type_kind == TypeKind.TYPE_ARRAY
