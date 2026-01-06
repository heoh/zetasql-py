"""
Tests for Value system - handling query execution results.

Tests the Value abstraction for representing typed SQL values,
mirroring Java Value class functionality.
"""

import pytest
from zetasql.api import TypeFactory
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind


@pytest.fixture
def value_catalog(builtin_function_options):
    """Create catalog for value testing."""
    test_table = (TableBuilder("TestTable")
        .add_column("int_col", TypeKind.TYPE_INT64)
        .add_column("string_col", TypeKind.TYPE_STRING)
        .add_column("bool_col", TypeKind.TYPE_BOOL)
        .add_column("double_col", TypeKind.TYPE_DOUBLE)
        .add_column("array_col", TypeFactory.create_array_type(
            TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
        ))
        .build())
    
    return (CatalogBuilder("value_db")
        .add_table(test_table)
        .with_builtin_functions(builtin_function_options)
        .build())


class TestValueBasics:
    """Test basic Value creation and access - Java: Value class"""
    
    def test_create_int64_value(self):
        """Test creating INT64 value - Java: Value.createInt64Value()
        
        Expected API:
            value = Value.int64(42)
            assert value.type_kind == TypeKind.TYPE_INT64
            assert value.get_int64() == 42
        """
        from zetasql.api.value import Value
        
        value = Value.int64(42)
        
        assert value.type_kind == TypeKind.TYPE_INT64
        assert value.get_int64() == 42
        assert not value.is_null()
    
    def test_create_string_value(self):
        """Test creating STRING value - Java: Value.createStringValue()
        
        Expected API:
            value = Value.string("hello")
            assert value.get_string() == "hello"
        """
        from zetasql.api.value import Value
        
        value = Value.string("hello")
        
        assert value.type_kind == TypeKind.TYPE_STRING
        assert value.get_string() == "hello"
        assert not value.is_null()
    
    def test_create_null_value(self):
        """Test creating NULL value - Java: Value.createNullValue()
        
        Expected API:
            value = Value.null(TypeKind.TYPE_INT64)
            assert value.is_null()
        """
        from zetasql.api.value import Value
        
        value = Value.null(TypeKind.TYPE_INT64)
        
        assert value.type_kind == TypeKind.TYPE_INT64
        assert value.is_null()


class TestValueTypes:
    """Test Value for different SQL types - Java: type-specific methods"""
    
    def test_bool_value(self):
        """Test BOOL value - Java: Value.createBoolValue()"""
        from zetasql.api.value import Value
        
        true_val = Value.bool(True)
        false_val = Value.bool(False)
        
        assert true_val.get_bool() is True
        assert false_val.get_bool() is False
    
    def test_double_value(self):
        """Test DOUBLE value - Java: Value.createDoubleValue()"""
        from zetasql.api.value import Value
        
        value = Value.double(3.14159)
        
        assert value.type_kind == TypeKind.TYPE_DOUBLE
        assert abs(value.get_double() - 3.14159) < 0.00001
    
    def test_date_value(self):
        """Test DATE value - Java: Value.createDateValue()
        
        Expected API:
            value = Value.date(2024, 1, 15)  # year, month, day
            assert value.get_date() == datetime.date(2024, 1, 15)
        """
        from zetasql.api.value import Value
        import datetime
        
        value = Value.date(2024, 1, 15)
        
        assert value.type_kind == TypeKind.TYPE_DATE
        assert value.get_date() == datetime.date(2024, 1, 15)
    
    def test_timestamp_value(self):
        """Test TIMESTAMP value - Java: Value.createTimestampValue()
        
        Expected API:
            value = Value.timestamp(datetime.datetime.now())
        """
        from zetasql.api.value import Value
        import datetime
        
        dt = datetime.datetime(2024, 1, 15, 10, 30, 45)
        value = Value.timestamp(dt)
        
        assert value.type_kind == TypeKind.TYPE_TIMESTAMP
        assert value.get_timestamp() == dt


class TestComplexValues:
    """Test complex Value types - Java: arrays, structs"""
    
    def test_array_value(self):
        """Test ARRAY value - Java: Value.createArrayValue()
        
        Expected API:
            elements = [Value.int64(1), Value.int64(2), Value.int64(3)]
            value = Value.array(elements)
            assert value.get_array_size() == 3
        """
        from zetasql.api.value import Value
        
        elements = [Value.int64(1), Value.int64(2), Value.int64(3)]
        value = Value.array(elements)
        
        assert value.type_kind == TypeKind.TYPE_ARRAY
        assert value.get_array_size() == 3
        assert value.get_array_element(0).get_int64() == 1
        assert value.get_array_element(2).get_int64() == 3
    
    def test_struct_value(self):
        """Test STRUCT value - Java: Value.createStructValue()
        
        Expected API:
            value = Value.struct({
                "name": Value.string("Alice"),
                "age": Value.int64(30)
            })
        """
        from zetasql.api.value import Value
        
        value = Value.struct({
            "name": Value.string("Alice"),
            "age": Value.int64(30)
        })
        
        assert value.type_kind == TypeKind.TYPE_STRUCT
        assert value.get_field("name").get_string() == "Alice"
        assert value.get_field("age").get_int64() == 30
    
    def test_nested_array_struct(self):
        """Test nested ARRAY of STRUCT - Java: complex nesting
        
        Expected API:
            structs = [
                Value.struct({"id": Value.int64(1), "name": Value.string("A")}),
                Value.struct({"id": Value.int64(2), "name": Value.string("B")})
            ]
            value = Value.array(structs)
        """
        from zetasql.api.value import Value
        
        structs = [
            Value.struct({"id": Value.int64(1), "name": Value.string("A")}),
            Value.struct({"id": Value.int64(2), "name": Value.string("B")})
        ]
        value = Value.array(structs)
        
        assert value.get_array_size() == 2
        assert value.get_array_element(0).get_field("name").get_string() == "A"


class TestValueComparison:
    """Test Value comparison and equality - Java: equals(), compareTo()"""
    
    def test_value_equality(self):
        """Test Value equality - Java: equals()
        
        Expected API:
            v1 = Value.int64(42)
            v2 = Value.int64(42)
            assert v1.equals(v2)
        """
        from zetasql.api.value import Value
        
        v1 = Value.int64(42)
        v2 = Value.int64(42)
        v3 = Value.int64(43)
        
        assert v1.equals(v2)
        assert not v1.equals(v3)
    
    def test_value_comparison(self):
        """Test Value comparison - Java: compareTo()
        
        Expected API:
            v1 = Value.int64(10)
            v2 = Value.int64(20)
            assert v1.compare_to(v2) < 0
        """
        from zetasql.api.value import Value
        
        v1 = Value.int64(10)
        v2 = Value.int64(20)
        v3 = Value.int64(10)
        
        assert v1.compare_to(v2) < 0
        assert v2.compare_to(v1) > 0
        assert v1.compare_to(v3) == 0
    
    def test_null_comparison(self):
        """Test NULL value comparison - Java: NULL handling
        
        Expected: NULL values have specific comparison semantics
        """
        from zetasql.api.value import Value
        
        null_val = Value.null(TypeKind.TYPE_INT64)
        int_val = Value.int64(42)
        
        assert null_val.is_null()
        assert not null_val.equals(int_val)


class TestValueSerialization:
    """Test Value serialization - Java: toString(), format()"""
    
    def test_value_to_string(self):
        """Test Value string representation - Java: toString()
        
        Expected API:
            value = Value.int64(42)
            assert str(value) == "42"
        """
        from zetasql.api.value import Value
        
        assert str(Value.int64(42)) == "42"
        assert str(Value.string("hello")) == '"hello"'
        assert str(Value.bool(True)) == "true"
    
    def test_value_to_sql_literal(self):
        """Test converting Value to SQL literal - Java: formatSqlLiteral()
        
        Expected API:
            value = Value.string("hello")
            assert value.to_sql_literal() == "'hello'"
        """
        from zetasql.api.value import Value
        
        assert Value.int64(42).to_sql_literal() == "42"
        assert Value.string("hello").to_sql_literal() == "'hello'"
        assert Value.null(TypeKind.TYPE_INT64).to_sql_literal() == "NULL"


class TestValueFromQueryResult:
    """Test creating Values from query execution results - Java: result handling"""
    
    @pytest.mark.skip(reason="Query result to Value not implemented")
    def test_extract_values_from_result(self, options, value_catalog):
        """Test extracting typed values from query results - Java: ResultSet
        
        Expected API:
            query = PreparedQuery.builder()...build()
            with query as q:
                result = q.execute()
                for row in result.rows():
                    int_value = row.get_value("int_col")
                    assert isinstance(int_value, Value)
        """
        from zetasql.api.prepared_query import PreparedQuery
        from zetasql.api.value import Value
        
        query = (PreparedQuery.builder()
            .sql("SELECT 42 as int_col, 'hello' as string_col")
            .options(options)
            .catalog(value_catalog)
            .build())
        
        with query as q:
            result = q.execute()
            row = result.rows()[0]
            
            int_val = row.get_value("int_col")
            assert isinstance(int_val, Value)
            assert int_val.get_int64() == 42
            
            str_val = row.get_value("string_col")
            assert str_val.get_string() == "hello"
    
    @pytest.mark.skip(reason="Value iteration not implemented")
    def test_iterate_array_result(self, options, value_catalog):
        """Test iterating array values from results - Java: array iteration
        
        Expected API:
            result = query.execute()
            array_val = result.rows()[0].get_value("array_col")
            for element in array_val:
                # Process each element
        """
        from zetasql.api.prepared_query import PreparedQuery
        
        query = (PreparedQuery.builder()
            .sql("SELECT [1, 2, 3, 4, 5] as array_col")
            .options(options)
            .catalog(value_catalog)
            .build())
        
        with query as q:
            result = q.execute()
            array_val = result.rows()[0].get_value("array_col")
            
            elements = [elem.get_int64() for elem in array_val]
            assert elements == [1, 2, 3, 4, 5]


class TestValueConversion:
    """Test Value type conversion - Java: coercion, casting"""
    
    def test_coerce_value(self):
        """Test coercing value to different type - Java: coerceTo()
        
        Expected API:
            int_val = Value.int64(42)
            string_val = int_val.coerce_to(TypeKind.TYPE_STRING)
            assert string_val.get_string() == "42"
        """
        from zetasql.api.value import Value
        
        int_val = Value.int64(42)
        string_val = int_val.coerce_to(TypeKind.TYPE_STRING)
        
        assert string_val.type_kind == TypeKind.TYPE_STRING
        assert string_val.get_string() == "42"
    
    def test_cast_value(self):
        """Test explicit casting - Java: castTo()
        
        Expected: Should handle type casting with error checking
        """
        from zetasql.api.value import Value
        
        # Valid cast
        string_val = Value.string("123")
        int_val = string_val.cast_to(TypeKind.TYPE_INT64)
        assert int_val.get_int64() == 123
        
        # Invalid cast should raise
        string_val = Value.string("not_a_number")
        with pytest.raises(ValueError):
            string_val.cast_to(TypeKind.TYPE_INT64)
