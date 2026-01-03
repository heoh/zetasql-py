"""
Function operations on SimpleCatalog - mirrors Java FunctionTest.java

ALL TESTS MARKED AS SKIP - Function registration API not yet implemented.
These tests define the expected API for future implementation.
"""

import pytest
from zetasql.api.builders import CatalogBuilder
from zetasql.types import TypeKind


class TestCatalogFunctionAdd:
    """Test adding functions to catalog - Java: SimpleCatalog.addFunction()"""
    
    def test_add_scalar_function(self):
        """Test adding scalar UDF to catalog.
        
        Expected API (Java):
            Function func = new Function(name, group, mode, signatures);
            catalog.addFunction(func);
        
        Expected Python API:
            from zetasql.api.builders import FunctionBuilder, SignatureBuilder
            
            function = (FunctionBuilder("MY_UDF")
                .set_group("UDF")
                .add_signature(
                    SignatureBuilder()
                        .add_argument(TypeKind.TYPE_STRING)
                        .set_return_type(TypeKind.TYPE_INT64)
                        .build()
                )
                .build())
            
            catalog.add_function(function)
        """
        from zetasql.api.builders import FunctionBuilder, SignatureBuilder
        
        function = (FunctionBuilder("MY_UDF")
            .add_signature(
                SignatureBuilder()
                    .add_argument(TypeKind.TYPE_STRING)
                    .set_return_type(TypeKind.TYPE_INT64)
                    .build()
            )
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_function(function)
        
        # Verify function was added
        assert len(catalog.get_function_list()) == 1
        assert catalog.get_function_list()[0].name_path[-1] == "MY_UDF"
    
    def test_add_function_with_multiple_signatures(self):
        """Test adding function with overloaded signatures.
        
        Expected: function with multiple signatures (overloads)
        """
        from zetasql.api.builders import FunctionBuilder, SignatureBuilder
        
        function = (FunctionBuilder("CONVERT")
            .add_signature(
                SignatureBuilder()
                    .add_argument(TypeKind.TYPE_STRING)
                    .set_return_type(TypeKind.TYPE_INT64)
                    .build()
            )
            .add_signature(
                SignatureBuilder()
                    .add_argument(TypeKind.TYPE_INT64)
                    .set_return_type(TypeKind.TYPE_STRING)
                    .build()
            )
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_function(function)
        
        func = catalog.get_function_list()[0]
        assert len(func.signature) == 2


class TestCatalogFunctionRetrieval:
    """Test retrieving functions from catalog - Java: getFunctionList(), getFunctionByFullName()"""
    
    def test_get_function_list(self):
        """Test SimpleCatalog.get_function_list() - NOT YET IMPLEMENTED.
        
        Expected API (Java):
            ImmutableList<Function> SimpleCatalog.getFunctionList()
        """
        catalog = CatalogBuilder("db").build()
        
        # Expected API
        functions = catalog.get_function_list()
        
        assert isinstance(functions, list)
    
    def test_get_function_by_name(self):
        """Test SimpleCatalog.get_function() or get_function_by_full_name() - NOT YET IMPLEMENTED.
        
        Expected API (Java):
            Function SimpleCatalog.getFunctionByFullName(String name)
        """
        from zetasql.api.builders import FunctionBuilder, SignatureBuilder
        
        function = (FunctionBuilder("MY_UDF")
            .add_signature(
                SignatureBuilder()
                    .add_argument(TypeKind.TYPE_STRING)
                    .set_return_type(TypeKind.TYPE_INT64)
                    .build()
            )
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_function(function)
        
        # Test retrieval by full name with group
        func = catalog.get_function_by_full_name("UDF:MY_UDF")
        assert func is not None
        assert "MY_UDF" in func.name_path
        
        # Test retrieval by name only
        func = catalog.get_function_by_full_name("MY_UDF")
        assert func is not None
        assert "MY_UDF" in func.name_path
    
    def test_get_function_name_list(self):
        """Test SimpleCatalog.get_function_name_list() - NOT YET IMPLEMENTED.
        
        Expected API (Java):
            ImmutableList<String> SimpleCatalog.getFunctionNameList()
        """
        catalog = CatalogBuilder("db").build()
        
        # Expected API
        names = catalog.get_function_name_list()
        
        assert isinstance(names, list)
        # Names should be in format "group:function_name"


class TestFunctionSignatureBuilder:
    """Test FunctionSignature and FunctionArgumentType builders.
    
    Java classes:
        - FunctionSignature
        - FunctionArgumentType
        - ArgumentCardinality (REQUIRED, OPTIONAL, REPEATED)
    """
    
    def test_signature_with_required_args(self):
        """Test building signature with required arguments."""
        from zetasql.api.builders import SignatureBuilder
        from zetasql.types import FunctionEnums
        
        sig = (SignatureBuilder()
            .add_argument(TypeKind.TYPE_STRING, FunctionEnums.ArgumentCardinality.REQUIRED)
            .add_argument(TypeKind.TYPE_INT64, FunctionEnums.ArgumentCardinality.REQUIRED)
            .set_return_type(TypeKind.TYPE_BOOL)
            .build())
        
        assert len(sig.argument) == 2
        assert sig.return_type.type.type_kind == TypeKind.TYPE_BOOL
    
    def test_signature_with_optional_args(self):
        """Test building signature with optional arguments."""
        from zetasql.api.builders import SignatureBuilder
        from zetasql.types import FunctionEnums
        
        sig = (SignatureBuilder()
            .add_argument(TypeKind.TYPE_STRING, FunctionEnums.ArgumentCardinality.REQUIRED)
            .add_argument(TypeKind.TYPE_INT64, FunctionEnums.ArgumentCardinality.OPTIONAL)
            .set_return_type(TypeKind.TYPE_STRING)
            .build())
        
        assert sig.argument[1].options.cardinality == FunctionEnums.ArgumentCardinality.OPTIONAL
    
    def test_signature_with_repeated_args(self):
        """Test building signature with repeated (variadic) arguments."""
        from zetasql.api.builders import SignatureBuilder
        from zetasql.types import FunctionEnums
        
        # Function like CONCAT(str1, str2, ...) - variadic
        sig = (SignatureBuilder()
            .add_argument(TypeKind.TYPE_STRING, FunctionEnums.ArgumentCardinality.REPEATED)
            .set_return_type(TypeKind.TYPE_STRING)
            .build())
        
        assert sig.argument[0].options.cardinality == FunctionEnums.ArgumentCardinality.REPEATED



class TestCatalogFunctionErrors:
    """Test error handling for function operations."""
    
    def test_add_duplicate_function_raises_error(self):
        """Test adding duplicate function raises error.
        
        Java behavior: throws IllegalArgumentException
        """
        from zetasql.api.builders import FunctionBuilder
        
        catalog = CatalogBuilder("db").build()
        
        func = FunctionBuilder("MY_UDF").build()
        catalog.add_function(func)
        
        # Adding same function again should raise
        with pytest.raises(ValueError):
            catalog.add_function(func)
    
    def test_get_nonexistent_function_returns_none(self):
        """Test getting non-existent function returns None."""
        catalog = CatalogBuilder("db").build()
        
        result = catalog.get_function_by_full_name("nonexistent_func")
        assert result is None
