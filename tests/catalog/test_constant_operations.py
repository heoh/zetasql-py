"""
Constant operations on SimpleCatalog - corresponds to Java Constant class usage

ALL TESTS MARKED AS SKIP - Constant registration API not yet implemented.
These tests define the expected API for future implementation.
"""

import pytest
from zetasql.api.builders import CatalogBuilder
from zetasql.types import TypeKind


@pytest.mark.skip(reason="API not implemented: SimpleCatalog.add_constant() and ConstantBuilder")
class TestCatalogConstantAdd:
    """Test adding constants to catalog - Java: SimpleCatalog.addConstant()"""
    
    def test_add_int64_constant(self):
        """Test adding INT64 constant to catalog.
        
        Expected API (Java):
            Constant constant = new Constant(name, type, value);
            catalog.addConstant(constant);
        
        Expected Python API:
            from zetasql.api.builders import ConstantBuilder
            
            constant = (ConstantBuilder("MAX_LIMIT")
                .set_type(TypeKind.TYPE_INT64)
                .build())
            
            catalog.add_constant(constant)
        
        Note: Constants in ZetaSQL don't typically store values in catalog,
        just names and types. Values are resolved during analysis.
        """
        from zetasql.api.builders import ConstantBuilder
        
        constant = (ConstantBuilder("MAX_LIMIT")
            .set_type(TypeKind.TYPE_INT64)
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_constant(constant)
        
        # Verify constant was added
        assert len(catalog.get_constant_list()) == 1
        assert catalog.get_constant_list()[0].name == "MAX_LIMIT"
    
    def test_add_string_constant(self):
        """Test adding STRING constant."""
        from zetasql.api.builders import ConstantBuilder
        
        constant = (ConstantBuilder("DEFAULT_STATUS")
            .set_type(TypeKind.TYPE_STRING)
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_constant(constant)
        
        const = catalog.get_constant_list()[0]
        assert const.type.type_kind == TypeKind.TYPE_STRING
    
    def test_add_multiple_constants(self):
        """Test adding multiple constants to catalog."""
        from zetasql.api.builders import ConstantBuilder
        
        const1 = ConstantBuilder("MAX_RETRIES").set_type(TypeKind.TYPE_INT64).build()
        const2 = ConstantBuilder("TIMEOUT_MS").set_type(TypeKind.TYPE_INT64).build()
        const3 = ConstantBuilder("DEFAULT_NAME").set_type(TypeKind.TYPE_STRING).build()
        
        catalog = CatalogBuilder("db").build()
        catalog.add_constant(const1)
        catalog.add_constant(const2)
        catalog.add_constant(const3)
        
        assert len(catalog.get_constant_list()) == 3


@pytest.mark.skip(reason="API not implemented: SimpleCatalog.get_constant() and related methods")
class TestCatalogConstantRetrieval:
    """Test retrieving constants from catalog."""
    
    def test_get_constant_list(self):
        """Test SimpleCatalog.get_constant_list() - NOT YET IMPLEMENTED.
        
        Expected API:
            List[Constant] SimpleCatalog.get_constant_list()
        """
        catalog = CatalogBuilder("db").build()
        
        # Expected API
        constants = catalog.get_constant_list()
        
        assert isinstance(constants, list)
    
    def test_get_constant_by_name(self):
        """Test SimpleCatalog.get_constant(name) - NOT YET IMPLEMENTED.
        
        Expected API:
            Constant SimpleCatalog.getConstant(String name)
        """
        from zetasql.api.builders import ConstantBuilder
        
        catalog = CatalogBuilder("db").build()
        const = ConstantBuilder("MY_CONST").set_type(TypeKind.TYPE_INT64).build()
        catalog.add_constant(const)
        
        # Expected API
        retrieved = catalog.get_constant("MY_CONST")
        
        assert retrieved is not None
        assert retrieved.name == "MY_CONST"
    
    def test_get_constant_case_insensitive(self):
        """Test constant lookup is case-insensitive.
        
        Java behavior: case-insensitive lookup
        """
        from zetasql.api.builders import ConstantBuilder
        
        catalog = CatalogBuilder("db").build()
        const = ConstantBuilder("MyConstant").set_type(TypeKind.TYPE_INT64).build()
        catalog.add_constant(const)
        
        # Expected: all should work
        assert catalog.get_constant("MyConstant") is not None
        assert catalog.get_constant("MYCONSTANT") is not None
        assert catalog.get_constant("myconstant") is not None


@pytest.mark.skip(reason="API not implemented: Constants in script analysis")
class TestConstantUsageInAnalysis:
    """Test using constants during SQL analysis - script variable tracking use case."""
    
    def test_analyze_with_declared_constant(self):
        """Test analyzing SQL that references a constant.
        
        Use case: Script analysis with DECLARE statements
        
        Example script:
            DECLARE MAX_LIMIT INT64 DEFAULT 100;
            SELECT * FROM Orders WHERE quantity < MAX_LIMIT;
        
        The constant MAX_LIMIT should be added to catalog during script analysis.
        """
        from zetasql.api.analyzer import Analyzer
        from zetasql.api.builders import ConstantBuilder
        from zetasql.types import AnalyzerOptions, LanguageOptions
        
        # Build catalog with constant
        constant = (ConstantBuilder("MAX_LIMIT")
            .set_type(TypeKind.TYPE_INT64)
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_constant(constant)
        
        # Analyze SQL referencing the constant
        options = AnalyzerOptions(
            language_options=LanguageOptions.maximum_features()
        )
        
        analyzer = Analyzer(options, catalog)
        # Note: Constant references in SQL might need special syntax
        stmt = analyzer.analyze_statement("SELECT MAX_LIMIT")
        
        assert stmt is not None


@pytest.mark.skip(reason="API not implemented: Constant error handling")
class TestCatalogConstantErrors:
    """Test error handling for constant operations."""
    
    def test_add_duplicate_constant_raises_error(self):
        """Test adding duplicate constant raises error."""
        from zetasql.api.builders import ConstantBuilder
        
        catalog = CatalogBuilder("db").build()
        
        const = ConstantBuilder("MY_CONST").set_type(TypeKind.TYPE_INT64).build()
        catalog.add_constant(const)
        
        # Adding same constant again should raise
        with pytest.raises(ValueError):
            catalog.add_constant(const)
    
    def test_get_nonexistent_constant_returns_none(self):
        """Test getting non-existent constant returns None."""
        catalog = CatalogBuilder("db").build()
        
        result = catalog.get_constant("nonexistent")
        assert result is None
