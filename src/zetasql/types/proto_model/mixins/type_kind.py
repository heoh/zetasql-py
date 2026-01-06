class TypeKindMixin:
    """Mixin class providing helper methods for TypeKind enum.

    This should be mixed into TypeKind IntEnum to provide type checking
    convenience methods while maintaining IDE autocomplete support.
    """

    def is_simple(self) -> bool:
        """Returns true if this is a simple (non-composite) type."""
        from zetasql.types.proto_model import TypeKind

        return self not in (
            TypeKind.TYPE_ARRAY,
            TypeKind.TYPE_STRUCT,
            TypeKind.TYPE_PROTO,
            TypeKind.TYPE_ENUM,
            TypeKind.TYPE_RANGE,
            TypeKind.TYPE_MAP,
            TypeKind.TYPE_GRAPH_ELEMENT,
            TypeKind.TYPE_GRAPH_PATH,
            TypeKind.TYPE_MEASURE,
        )

    def is_integer(self) -> bool:
        """Returns true for any integer type (signed or unsigned).

        Note: Named is_integer() instead of is_integer() to avoid conflict
        with int.is_integer() method.
        """
        from zetasql.types.proto_model import TypeKind

        return self in (
            TypeKind.TYPE_INT32,
            TypeKind.TYPE_INT64,
            TypeKind.TYPE_UINT32,
            TypeKind.TYPE_UINT64,
        )

    def is_signed_integer(self) -> bool:
        """Returns true for signed integer types."""
        from zetasql.types.proto_model import TypeKind

        return self in (TypeKind.TYPE_INT32, TypeKind.TYPE_INT64)

    def is_unsigned_integer(self) -> bool:
        """Returns true for unsigned integer types."""
        from zetasql.types.proto_model import TypeKind

        return self in (TypeKind.TYPE_UINT32, TypeKind.TYPE_UINT64)

    def is_floating_point(self) -> bool:
        """Returns true for floating point types."""
        from zetasql.types.proto_model import TypeKind

        return self in (TypeKind.TYPE_FLOAT, TypeKind.TYPE_DOUBLE)

    def is_numerical(self) -> bool:
        """Returns true for any numeric type (integer, float, or decimal)."""
        from zetasql.types.proto_model import TypeKind

        return (
            self.is_integer() or self.is_floating_point() or self in (TypeKind.TYPE_NUMERIC, TypeKind.TYPE_BIGNUMERIC)
        )

    def is_temporal(self) -> bool:
        """Returns true for date/time types."""
        from zetasql.types.proto_model import TypeKind

        return self in (
            TypeKind.TYPE_DATE,
            TypeKind.TYPE_TIME,
            TypeKind.TYPE_DATETIME,
            TypeKind.TYPE_TIMESTAMP,
            TypeKind.TYPE_INTERVAL,
        )

    def is_composite(self) -> bool:
        """Returns true for composite types (array, struct, map, etc)."""
        return not self.is_simple()
