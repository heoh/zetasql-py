"""
Test suite for AnalyzerOptions factory methods and LanguageOptions convenience API.

This test verifies the implementation of IMPROVEMENT_ROADMAP.md Phase 1, Task #3:
- LanguageOptions.enable_maximum_language_features() (Java style)
- LanguageOptions.maximum_features() (C++ style)
- AnalyzerOptions.with_maximum_features() (convenience method)
- Automatic FEATURE_SPANNER_LEGACY_DDL exclusion
"""

import pytest
from zetasql.types import LanguageFeature, NameResolutionMode, ProductMode, LanguageOptions, AnalyzerOptions


class TestLanguageOptionsMaximumFeatures:
    """Test LanguageOptions.maximum_features() class method."""
    
    def test_maximum_features_returns_language_options(self):
        """Should return LanguageOptions instance."""
        lang_opts = LanguageOptions.maximum_features()
        assert isinstance(lang_opts, LanguageOptions)
    
    def test_maximum_features_enables_features(self):
        """Should enable multiple language features."""
        lang_opts = LanguageOptions.maximum_features()
        assert len(lang_opts.enabled_language_features) > 50  # Should have many features
    
    def test_maximum_features_excludes_spanner_legacy_ddl(self):
        """Should exclude FEATURE_SPANNER_LEGACY_DDL (ideally_enabled=false)."""
        lang_opts = LanguageOptions.maximum_features()
        
        # FEATURE_SPANNER_LEGACY_DDL should NOT be in enabled features
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in lang_opts.enabled_language_features
    
    def test_maximum_features_sets_default_modes(self):
        """Should set NAME_RESOLUTION_DEFAULT and PRODUCT_INTERNAL."""
        lang_opts = LanguageOptions.maximum_features()
        assert lang_opts.name_resolution_mode == NameResolutionMode.NAME_RESOLUTION_DEFAULT
        assert lang_opts.product_mode == ProductMode.PRODUCT_INTERNAL


class TestLanguageOptionsEnableMaximumFeatures:
    """Test LanguageOptions.enable_maximum_language_features() instance method."""
    
    def test_enable_maximum_features_returns_self(self):
        """Should return self for method chaining (Java style)."""
        lang_opts = LanguageOptions()
        result = lang_opts.enable_maximum_language_features()
        assert result is lang_opts
    
    def test_enable_maximum_features_enables_features(self):
        """Should enable multiple language features."""
        lang_opts = LanguageOptions()
        lang_opts.enable_maximum_language_features()
        assert len(lang_opts.enabled_language_features) > 50
    
    def test_enable_maximum_features_excludes_spanner_legacy_ddl(self):
        """Should exclude FEATURE_SPANNER_LEGACY_DDL."""
        lang_opts = LanguageOptions()
        lang_opts.enable_maximum_language_features()
        
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in lang_opts.enabled_language_features
    
    def test_enable_maximum_features_method_chaining(self):
        """Should support method chaining."""
        lang_opts = LanguageOptions()
        lang_opts.name_resolution_mode = NameResolutionMode.NAME_RESOLUTION_DEFAULT
        
        result = (lang_opts
                  .enable_maximum_language_features())
        
        assert result.name_resolution_mode == NameResolutionMode.NAME_RESOLUTION_DEFAULT
        assert len(result.enabled_language_features) > 50


class TestAnalyzerOptionsWithMaximumFeatures:
    """Test AnalyzerOptions.with_maximum_features() convenience method."""
    
    def test_with_maximum_features_returns_analyzer_options(self):
        """Should return AnalyzerOptions instance."""
        opts = AnalyzerOptions.with_maximum_features()
        assert isinstance(opts, AnalyzerOptions)
    
    def test_with_maximum_features_has_language_options(self):
        """Should include LanguageOptions with maximum features enabled."""
        opts = AnalyzerOptions.with_maximum_features()
        assert opts.language_options is not None
        assert len(opts.language_options.enabled_language_features) > 50
    
    def test_with_maximum_features_excludes_spanner_legacy_ddl(self):
        """Should exclude FEATURE_SPANNER_LEGACY_DDL via LanguageOptions."""
        opts = AnalyzerOptions.with_maximum_features()
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in opts.language_options.enabled_language_features
    
    def test_with_maximum_features_sets_default_modes(self):
        """Should configure proper name resolution and product modes."""
        opts = AnalyzerOptions.with_maximum_features()
        assert opts.language_options.name_resolution_mode == NameResolutionMode.NAME_RESOLUTION_DEFAULT
        assert opts.language_options.product_mode == ProductMode.PRODUCT_INTERNAL


class TestProtoModelIntegration:
    """Test that options work with ProtoModel to_proto/from_proto conversion."""
    
    def test_language_options_to_proto_conversion(self):
        """Should convert to protobuf and back."""
        lang_opts = LanguageOptions.maximum_features()
        
        # Convert to proto
        proto = lang_opts.to_proto()
        assert proto is not None
        
        # Convert back
        lang_opts_2 = LanguageOptions.from_proto(proto)
        assert len(lang_opts_2.enabled_language_features) == len(lang_opts.enabled_language_features)
    
    def test_analyzer_options_to_proto_conversion(self):
        """Should convert to protobuf and back."""
        opts = AnalyzerOptions.with_maximum_features()
        
        # Convert to proto
        proto = opts.to_proto()
        assert proto is not None
        
        # Convert back
        opts_2 = AnalyzerOptions.from_proto(proto)
        assert opts_2.language_options is not None
        assert len(opts_2.language_options.enabled_language_features) > 50


class TestAPIConsistency:
    """Test that Python API matches Java/C++ patterns."""
    
    def test_java_style_instance_method_exists(self):
        """Should have enable_maximum_language_features() like Java."""
        lang_opts = LanguageOptions()
        assert hasattr(lang_opts, 'enable_maximum_language_features')
        assert callable(lang_opts.enable_maximum_language_features)
    
    def test_cpp_style_static_factory_exists(self):
        """Should have maximum_features() class method like C++."""
        assert hasattr(LanguageOptions, 'maximum_features')
        assert callable(LanguageOptions.maximum_features)
    
    def test_convenience_factory_exists(self):
        """Should have with_maximum_features() for easy creation."""
        assert hasattr(AnalyzerOptions, 'with_maximum_features')
        assert callable(AnalyzerOptions.with_maximum_features)
    
    def test_both_patterns_produce_same_result(self):
        """Java-style and C++-style should produce equivalent results."""
        # Java style
        lang_opts_java = LanguageOptions()
        lang_opts_java.name_resolution_mode = NameResolutionMode.NAME_RESOLUTION_DEFAULT
        lang_opts_java.product_mode = ProductMode.PRODUCT_INTERNAL
        lang_opts_java.enable_maximum_language_features()
        
        # C++ style
        lang_opts_cpp = LanguageOptions.maximum_features()
        
        # Should have same enabled features
        assert set(lang_opts_java.enabled_language_features) == set(lang_opts_cpp.enabled_language_features)
        assert lang_opts_java.name_resolution_mode == lang_opts_cpp.name_resolution_mode
        assert lang_opts_java.product_mode == lang_opts_cpp.product_mode


class TestFeatureExclusion:
    """Test that specific features are correctly excluded."""
    
    def test_spanner_legacy_ddl_always_excluded(self):
        """FEATURE_SPANNER_LEGACY_DDL should never be enabled."""
        # Test all three methods
        lang_opts_1 = LanguageOptions().enable_maximum_language_features()
        lang_opts_2 = LanguageOptions.maximum_features()
        opts = AnalyzerOptions.with_maximum_features()
        
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in lang_opts_1.enabled_language_features
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in lang_opts_2.enabled_language_features
        assert LanguageFeature.FEATURE_SPANNER_LEGACY_DDL not in opts.language_options.enabled_language_features
    
    def test_positive_features_only(self):
        """Should only enable features with positive enum values."""
        lang_opts = LanguageOptions.maximum_features()
        
        for feature in lang_opts.enabled_language_features:
            assert feature > 0, f"Feature {feature} should be positive"
    
    def test_common_features_enabled(self):
        """Should enable common released features."""
        lang_opts = LanguageOptions.maximum_features()
        features = lang_opts.enabled_language_features
        
        # Check a few common features are enabled
        assert LanguageFeature.FEATURE_ANALYTIC_FUNCTIONS in features
        assert LanguageFeature.FEATURE_TABLESAMPLE in features
        assert LanguageFeature.FEATURE_V_1_3_NULLS_FIRST_LAST_IN_ORDER_BY in features


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_language_options_before_enable(self):
        """LanguageOptions should start with no features."""
        lang_opts = LanguageOptions()
        assert len(lang_opts.enabled_language_features) == 0
    
    def test_enable_maximum_features_idempotent(self):
        """Calling enable_maximum_language_features twice should be safe."""
        lang_opts = LanguageOptions()
        lang_opts.enable_maximum_language_features()
        features_1 = set(lang_opts.enabled_language_features)
        
        lang_opts.enable_maximum_language_features()
        features_2 = set(lang_opts.enabled_language_features)
        
        assert features_1 == features_2
    
    def test_maximum_features_creates_new_instance(self):
        """maximum_features() should create independent instances."""
        lang_opts_1 = LanguageOptions.maximum_features()
        lang_opts_2 = LanguageOptions.maximum_features()
        
        assert lang_opts_1 is not lang_opts_2
        
        # Modifying one shouldn't affect the other
        lang_opts_1.enabled_language_features = []
        assert len(lang_opts_2.enabled_language_features) > 50
