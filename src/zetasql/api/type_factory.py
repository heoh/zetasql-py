"""
TypeFactory - Factory methods for creating ZetaSQL Type objects

This module provides Java-style factory methods for creating Type ProtoModel objects,
offering a clean alternative to manual protobuf construction.

Examples:
    >>> from zetasql.api import TypeFactory
    >>> from zetasql.types import TypeKind
    >>>
    >>> # Simple types
    >>> int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
    >>>
    >>> # Array types
    >>> str_array = TypeFactory.create_array_type(
    ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
    ... )
    >>>
    >>> # Struct types
    >>> person_type = TypeFactory.create_struct_type([
    ...     ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
    ...     ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
    ... ])
"""

from zetasql.types import ArrayType, MapType, StructField, StructType, Type, TypeKind


class TypeFactory:
    """Factory for creating ZetaSQL Type ProtoModel objects.

    All methods are static and return Type ProtoModel instances that can be
    used directly with builders or converted to protobuf via .to_proto().

    This API is inspired by the Java TypeFactory but adapted for Python's
    ProtoModel system.
    """

    @staticmethod
    def create_simple_type(type_kind: TypeKind | int) -> Type:
        """Create a simple (non-composite) type.

        Args:
            type_kind: TypeKind enum or integer type kind constant

        Returns:
            Type ProtoModel with the specified type_kind

        Examples:
            >>> int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
            >>> str_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            >>> bool_type = TypeFactory.create_simple_type(TypeKind.TYPE_BOOL)
        """
        return Type(type_kind=int(type_kind))

    @staticmethod
    def create_array_type(element_type: Type) -> Type:
        """Create an array type.

        Args:
            element_type: Type ProtoModel for the array elements

        Returns:
            Type ProtoModel representing ARRAY<element_type>

        Examples:
            >>> # ARRAY<STRING>
            >>> str_array = TypeFactory.create_array_type(
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            ... )
            >>>
            >>> # ARRAY<ARRAY<INT64>> (nested arrays)
            >>> nested = TypeFactory.create_array_type(
            ...     TypeFactory.create_array_type(
            ...         TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
            ...     )
            ... )
        """
        return Type(type_kind=TypeKind.TYPE_ARRAY, array_type=ArrayType(element_type=element_type))

    @staticmethod
    def create_struct_type(fields: list[tuple[str, Type]]) -> Type:
        """Create a struct type.

        Args:
            fields: List of (field_name, field_type) tuples

        Returns:
            Type ProtoModel representing STRUCT<fields>

        Examples:
            >>> # STRUCT<id INT64, name STRING>
            >>> person = TypeFactory.create_struct_type([
            ...     ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
            ...     ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING))
            ... ])
            >>>
            >>> # Nested struct
            >>> order = TypeFactory.create_struct_type([
            ...     ("order_id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
            ...     ("customer", person)  # Use previously created struct
            ... ])
        """
        struct_fields = [StructField(field_name=name, field_type=field_type) for name, field_type in fields]
        return Type(type_kind=TypeKind.TYPE_STRUCT, struct_type=StructType(field=struct_fields))

    @staticmethod
    def create_map_type(key_type: Type, value_type: Type) -> Type:
        """Create a map type.

        Args:
            key_type: Type ProtoModel for map keys
            value_type: Type ProtoModel for map values

        Returns:
            Type ProtoModel representing MAP<key_type, value_type>

        Examples:
            >>> # MAP<STRING, INT64>
            >>> map_type = TypeFactory.create_map_type(
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_STRING),
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
            ... )
        """
        return Type(type_kind=TypeKind.TYPE_MAP, map_type=MapType(key_type=key_type, value_type=value_type))


__all__ = ["TypeFactory"]
