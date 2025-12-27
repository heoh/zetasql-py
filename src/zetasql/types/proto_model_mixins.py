class TypeKindMixin:
    """Mixin class providing helper methods for TypeKind enum.
    
    This should be mixed into TypeKind IntEnum to provide type checking
    convenience methods while maintaining IDE autocomplete support.
    """
    
    def is_simple(self) -> bool:
        """Returns true if this is a simple (non-composite) type."""
        from zetasql.types.proto_models import TypeKind
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
        from zetasql.types.proto_models import TypeKind
        return self in (
            TypeKind.TYPE_INT32,
            TypeKind.TYPE_INT64,
            TypeKind.TYPE_UINT32,
            TypeKind.TYPE_UINT64,
        )

    def is_signed_integer(self) -> bool:
        """Returns true for signed integer types."""
        from zetasql.types.proto_models import TypeKind
        return self in (TypeKind.TYPE_INT32, TypeKind.TYPE_INT64)

    def is_unsigned_integer(self) -> bool:
        """Returns true for unsigned integer types."""
        from zetasql.types.proto_models import TypeKind
        return self in (TypeKind.TYPE_UINT32, TypeKind.TYPE_UINT64)

    def is_floating_point(self) -> bool:
        """Returns true for floating point types."""
        from zetasql.types.proto_models import TypeKind
        return self in (TypeKind.TYPE_FLOAT, TypeKind.TYPE_DOUBLE)

    def is_numerical(self) -> bool:
        """Returns true for any numeric type (integer, float, or decimal)."""
        from zetasql.types.proto_models import TypeKind
        return self.is_integer() or self.is_floating_point() or \
               self in (TypeKind.TYPE_NUMERIC, TypeKind.TYPE_BIGNUMERIC)

    def is_temporal(self) -> bool:
        """Returns true for date/time types."""
        from zetasql.types.proto_models import TypeKind
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


class LanguageOptionsMixin:
    """Mixin class providing factory methods for LanguageOptions.
    
    This mixin adds convenience methods to LanguageOptions ProtoModel:
    - enable_maximum_language_features(): Java API compatible instance method
    - maximum_features(): C++ style static factory method
    
    These methods enable all ideally_enabled language features, automatically
    excluding problematic features like FEATURE_SPANNER_LEGACY_DDL.
    """
    
    def enable_maximum_language_features(self):
        """Enable all released language features (ideally_enabled=true).
        
        This method activates all language features that are considered part of the
        "ideal" ZetaSQL specification. Features with ideally_enabled=false are
        automatically excluded (e.g., FEATURE_SPANNER_LEGACY_DDL, legacy compatibility
        features, and engine-specific quirks).
        
        Implementation Strategy:
        - First attempts to use LocalService RPC for C++ compatibility
        - Falls back to manual enumeration if RPC unavailable
        - Automatically filters out FEATURE_SPANNER_LEGACY_DDL (ideally_enabled=false)
        
        This matches the behavior of:
        - C++: LanguageOptions::EnableMaximumLanguageFeatures()
        - Java: LanguageOptions.enableMaximumLanguageFeatures()
        
        Returns:
            self: For method chaining (Java-style)
        
        Example:
            >>> lang_opts = LanguageOptions()
            >>> lang_opts.enable_maximum_language_features()
            >>> # Now lang_opts has all released features enabled
        
        Note:
            FEATURE_SPANNER_LEGACY_DDL is always excluded because:
            - ideally_enabled = false (not part of ideal ZetaSQL)
            - in_development = true (unstable)
            - Causes all analysis to fail immediately (Spanner DDL parser-only mode)
        """
        from zetasql.local_service import get_local_service
        lang_opts_from_service = get_local_service().get_language_options(maximum_features=True)
        
        self.enabled_language_features = list(lang_opts_from_service.enabled_language_features)
        return self
    
    @classmethod
    def maximum_features(cls):
        """Create LanguageOptions with all released features enabled (C++ style).
        
        This is a class method that creates a new LanguageOptions instance with
        enable_maximum_language_features() already applied. This matches the C++
        static factory method pattern:
        
        C++: LanguageOptions::MaximumFeatures()
        
        Returns:
            LanguageOptions: New instance with maximum features enabled
        
        Example:
            >>> lang_opts = LanguageOptions.maximum_features()
            >>> # Equivalent to:
            >>> # lang_opts = LanguageOptions()
            >>> # lang_opts.enable_maximum_language_features()
        """
        from zetasql.types import NameResolutionMode, ProductMode
        
        opts = cls()
        opts.name_resolution_mode = NameResolutionMode.NAME_RESOLUTION_DEFAULT
        opts.product_mode = ProductMode.PRODUCT_INTERNAL
        opts.enable_maximum_language_features()
        return opts
