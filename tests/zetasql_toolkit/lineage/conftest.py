"""Shared test fixtures for lineage tests."""
import pytest
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind


@pytest.fixture
def simple_catalog():
    """
    Create a simple test catalog with basic tables.
    
    Tables:
    - orders: order_id (INT64), customer_id (INT64), amount (DOUBLE)
    - customers: id (INT64), name (STRING)
    """
    orders = (
        TableBuilder("orders")
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .build()
    )
    
    customers = (
        TableBuilder("customers")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .build()
    )
    
    return CatalogBuilder("test").add_table(orders).add_table(customers).build()


@pytest.fixture
def wikipedia_catalog():
    """
    Create catalog matching the Java example (ExtractColumnLevelLineage.java).
    
    Tables:
    - wikipedia: title (STRING), comment (STRING)
    - shakespeare: corpus (STRING), word (STRING), word_count (INT64)
    """
    wikipedia = (
        TableBuilder("wikipedia")
        .add_column("title", TypeKind.TYPE_STRING)
        .add_column("comment", TypeKind.TYPE_STRING)
        .build()
    )
    
    shakespeare = (
        TableBuilder("shakespeare")
        .add_column("corpus", TypeKind.TYPE_STRING)
        .add_column("word", TypeKind.TYPE_STRING)
        .add_column("word_count", TypeKind.TYPE_INT64)
        .build()
    )
    
    return (
        CatalogBuilder("test")
        .add_table(wikipedia)
        .add_table(shakespeare)
        .build()
    )


@pytest.fixture
def struct_catalog():
    """
    Create catalog with STRUCT types for testing STRUCT expansion.
    
    Tables:
    - users: id (INT64), profile (STRUCT<name STRING, age INT64>)
    """
    from zetasql.types import StructType, StructField, SimpleType
    
    profile_type = StructType([
        StructField("name", SimpleType(TypeKind.TYPE_STRING)),
        StructField("age", SimpleType(TypeKind.TYPE_INT64))
    ])
    
    users = (
        TableBuilder("users")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("profile", profile_type)
        .build()
    )
    
    return CatalogBuilder("test").add_table(users).build()
