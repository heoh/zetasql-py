"""
Analyzer Options Factory - Simplified API for creating ZetaSQL AnalyzerOptions.

This module re-exports LanguageOptions and AnalyzerOptions with convenience methods
added via mixins. The actual implementation is in proto_model_mixins.py and is
automatically merged into the generated ProtoModel classes.

Key Features:
- LanguageOptions.enable_maximum_language_features(): Java API compatible
- LanguageOptions.maximum_features(): C++ style factory
- AnalyzerOptions.with_maximum_features(): One-line creation
- Automatic ideally_enabled filtering (FEATURE_SPANNER_LEGACY_DDL excluded)

Examples:
    >>> from zetasql.options import LanguageOptions, AnalyzerOptions
    >>> 
    >>> # Java style - instance method
    >>> lang_opts = LanguageOptions()
    >>> lang_opts.enable_maximum_language_features()
    >>> 
    >>> # C++ style - class method
    >>> lang_opts = LanguageOptions.maximum_features()
    >>> 
    >>> # Recommended - one-liner
    >>> opts = AnalyzerOptions.with_maximum_features()

Implementation Notes:
    The convenience methods are defined in proto_model_mixins.py as
    LanguageOptionsMixin and AnalyzerOptionsMixin. During proto model
    generation, these mixins are automatically merged into the generated
    LanguageOptions and AnalyzerOptions classes.
    
    This approach provides:
    - Clean API surface (methods appear as native class methods)
    - IDE autocomplete support
    - Type safety
    - No runtime monkey-patching overhead
"""

from zetasql.types.proto_models import LanguageOptions, AnalyzerOptions

__all__ = [
    'LanguageOptions',
    'AnalyzerOptions',
]

