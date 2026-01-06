from dataclasses import dataclass

from zetasql.types.proto_model.generated import (
    LanguageOptions as _GeneratedLanguageOptions,
)


@dataclass
class LanguageOptions(_GeneratedLanguageOptions):
    """Generated model for LanguageOptionsProto"""

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
        from zetasql.core.local_service import ZetaSqlLocalService

        lang_opts_from_service = ZetaSqlLocalService.get_instance().get_language_options(maximum_features=True)

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
        from zetasql.types.proto_model import NameResolutionMode, ProductMode

        opts = cls()
        opts.name_resolution_mode = NameResolutionMode.NAME_RESOLUTION_DEFAULT
        opts.product_mode = ProductMode.PRODUCT_INTERNAL
        opts.enable_maximum_language_features()
        return opts
