"""
Tests for TypeKind enum and Type extensions
"""

import pytest

from zetasql.types import ArrayType, StructField, StructType, Type, TypeKind


class TestTypeKind:
    """Test TypeKind enum wrapper"""

    def test_typekind_values(self):
        """Verify TypeKind enum values match proto"""
        assert TypeKind.TYPE_INT32 == 1
        assert TypeKind.TYPE_INT64 == 2
        assert TypeKind.TYPE_UINT32 == 3
        assert TypeKind.TYPE_UINT64 == 4
        assert TypeKind.TYPE_BOOL == 5
        assert TypeKind.TYPE_FLOAT == 6
        assert TypeKind.TYPE_DOUBLE == 7
        assert TypeKind.TYPE_STRING == 8
        assert TypeKind.TYPE_BYTES == 9
        assert TypeKind.TYPE_DATE == 10
        assert TypeKind.TYPE_ARRAY == 16
        assert TypeKind.TYPE_STRUCT == 17

    def test_typekind_is_integer(self):
        """Test is_integer() method (is_integer conflicts with int.is_integer)"""
        assert TypeKind.TYPE_INT32.is_integer()
        assert TypeKind.TYPE_INT64.is_integer()
        assert TypeKind.TYPE_UINT32.is_integer()
        assert TypeKind.TYPE_UINT64.is_integer()
        assert not TypeKind.TYPE_FLOAT.is_integer()
        assert not TypeKind.TYPE_STRING.is_integer()

    def test_typekind_is_numerical(self):
        """Test is_numerical() method"""
        assert TypeKind.TYPE_INT64.is_numerical()
        assert TypeKind.TYPE_FLOAT.is_numerical()
        assert TypeKind.TYPE_DOUBLE.is_numerical()
        assert TypeKind.TYPE_NUMERIC.is_numerical()
        assert not TypeKind.TYPE_STRING.is_numerical()
        assert not TypeKind.TYPE_BOOL.is_numerical()

    def test_typekind_is_temporal(self):
        """Test is_temporal() method"""
        assert TypeKind.TYPE_DATE.is_temporal()
        assert TypeKind.TYPE_TIME.is_temporal()
        assert TypeKind.TYPE_DATETIME.is_temporal()
        assert TypeKind.TYPE_TIMESTAMP.is_temporal()
        assert TypeKind.TYPE_INTERVAL.is_temporal()
        assert not TypeKind.TYPE_INT64.is_temporal()

    def test_typekind_is_simple(self):
        """Test is_simple() method"""
        assert TypeKind.TYPE_INT64.is_simple()
        assert TypeKind.TYPE_STRING.is_simple()
        assert not TypeKind.TYPE_ARRAY.is_simple()
        assert not TypeKind.TYPE_STRUCT.is_simple()
        assert not TypeKind.TYPE_MAP.is_simple()


class TestTypeExtensions:
    """Test Type class extensions"""

    def test_type_creation_with_typekind(self):
        """Test creating Type with TypeKind enum"""
        t = Type(type_kind=TypeKind.TYPE_INT64)
        assert t.type_kind == TypeKind.TYPE_INT64
        assert t.type_kind == 2  # IntEnum backward compatibility

    def test_type_is_methods(self):
        """Test is_* type checking methods"""
        int_type = Type(type_kind=TypeKind.TYPE_INT64)
        assert int_type.is_int64()
        assert not int_type.is_string()
        assert not int_type.is_array()

        string_type = Type(type_kind=TypeKind.TYPE_STRING)
        assert string_type.is_string()
        assert not string_type.is_int64()

        array_type = Type(type_kind=TypeKind.TYPE_ARRAY)
        assert array_type.is_array()
        assert not array_type.is_simple()

    def test_type_category_methods(self):
        """Test category checking methods"""
        int_type = Type(type_kind=TypeKind.TYPE_INT64)
        assert int_type.is_integer()
        assert int_type.is_signed_integer()
        assert not int_type.is_unsigned_integer()
        assert int_type.is_numerical()

        float_type = Type(type_kind=TypeKind.TYPE_FLOAT)
        assert float_type.is_floating_point()
        assert float_type.is_numerical()
        assert not float_type.is_integer()

        date_type = Type(type_kind=TypeKind.TYPE_DATE)
        assert date_type.is_temporal()
        assert not date_type.is_numerical()

    def test_type_as_array(self):
        """Test as_array() type narrowing"""
        # Simple type returns None
        int_type = Type(type_kind=TypeKind.TYPE_INT64)
        assert int_type.as_array() is None

        # Array type with element
        element_type = Type(type_kind=TypeKind.TYPE_STRING)
        array_type_info = ArrayType(element_type=element_type)
        array_type = Type(type_kind=TypeKind.TYPE_ARRAY, array_type=array_type_info)

        assert array_type.is_array()
        arr = array_type.as_array()
        assert arr is not None
        assert arr.element_type.type_kind == TypeKind.TYPE_STRING

    def test_type_as_struct(self):
        """Test as_struct() type narrowing"""
        # Simple type returns None
        int_type = Type(type_kind=TypeKind.TYPE_INT64)
        assert int_type.as_struct() is None

        # Struct type with fields
        fields = [
            StructField(field_name="name", field_type=Type(type_kind=TypeKind.TYPE_STRING)),
            StructField(field_name="age", field_type=Type(type_kind=TypeKind.TYPE_INT64)),
        ]
        struct_type_info = StructType(field=fields)
        struct_type = Type(type_kind=TypeKind.TYPE_STRUCT, struct_type=struct_type_info)

        assert struct_type.is_struct()
        st = struct_type.as_struct()
        assert st is not None
        assert len(st.field) == 2
        assert st.field[0].field_name == "name"
        assert st.field[1].field_name == "age"

    def test_type_name_simple(self):
        """Test type_name() for simple types"""
        assert Type(type_kind=TypeKind.TYPE_INT64).type_name() == "INT64"
        assert Type(type_kind=TypeKind.TYPE_STRING).type_name() == "STRING"
        assert Type(type_kind=TypeKind.TYPE_BOOL).type_name() == "BOOL"
        assert Type(type_kind=TypeKind.TYPE_DOUBLE).type_name() == "DOUBLE"

    def test_type_name_array(self):
        """Test type_name() for array types"""
        element_type = Type(type_kind=TypeKind.TYPE_INT64)
        array_type_info = ArrayType(element_type=element_type)
        array_type = Type(type_kind=TypeKind.TYPE_ARRAY, array_type=array_type_info)

        assert array_type.type_name() == "ARRAY<INT64>"

    def test_type_name_struct(self):
        """Test type_name() for struct types"""
        struct_type = Type(type_kind=TypeKind.TYPE_STRUCT)
        assert struct_type.type_name() == "STRUCT<...>"

    def test_type_str_repr(self):
        """Test __str__ and __repr__ methods"""
        t = Type(type_kind=TypeKind.TYPE_INT64)
        assert str(t) == "INT64"
        assert "TYPE_INT64" in repr(t)

    def test_type_proto_compatibility(self):
        """Test that Type works with to_proto/from_proto"""
        # Create type
        original = Type(type_kind=TypeKind.TYPE_STRING)

        # Convert to proto
        proto = original.to_proto()
        assert proto.type_kind == 8  # TYPE_STRING

        # Convert back from proto
        restored = Type.from_proto(proto)
        assert restored.type_kind == TypeKind.TYPE_STRING
        assert restored.is_string()

    def test_backward_compatibility_with_int(self):
        """Test that Type still works with plain integers"""
        # Old style with int (should still work)
        t = Type(type_kind=2)  # TYPE_INT64 as int
        assert t.type_kind == TypeKind.TYPE_INT64
        assert t.is_int64()

        # Comparison with int works
        assert t.type_kind == 2

    def test_complex_type_construction(self):
        """Test construction of complex nested types"""
        # ARRAY<STRUCT<name STRING, age INT64>>

        # 1. Create struct fields
        name_field = StructField(field_name="name", field_type=Type(type_kind=TypeKind.TYPE_STRING))
        age_field = StructField(field_name="age", field_type=Type(type_kind=TypeKind.TYPE_INT64))

        # 2. Create struct type
        struct_type_info = StructType(field=[name_field, age_field])
        struct_type = Type(type_kind=TypeKind.TYPE_STRUCT, struct_type=struct_type_info)

        # 3. Create array of struct
        array_type_info = ArrayType(element_type=struct_type)
        array_type = Type(type_kind=TypeKind.TYPE_ARRAY, array_type=array_type_info)

        # Verify
        assert array_type.is_array()
        arr = array_type.as_array()
        assert arr is not None
        assert arr.element_type.is_struct()

        # Get struct from array element
        elem_struct = arr.element_type.as_struct()
        assert elem_struct is not None
        assert len(elem_struct.field) == 2
        assert elem_struct.field[0].field_name == "name"
        assert elem_struct.field[0].field_type.is_string()
        assert elem_struct.field[1].field_name == "age"
        assert elem_struct.field[1].field_type.is_int64()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
