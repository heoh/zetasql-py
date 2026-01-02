"""
Table-Valued Function (TVF) operations on SimpleCatalog - mirrors Java TableValuedFunctionTest.java

ALL TESTS MARKED AS SKIP - TVF registration API not yet implemented.
These tests define the expected API for future implementation.
"""

import pytest
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind


@pytest.mark.skip(reason="API not implemented: SimpleCatalog.add_table_valued_function() and TVFBuilder")
class TestCatalogTVFAdd:
    """Test adding TVFs to catalog - Java: SimpleCatalog.addTableValuedFunction()"""
    
    def test_add_simple_tvf(self):
        """Test adding simple TVF to catalog.
        
        Expected API (Java):
            TableValuedFunction tvf = new TableValuedFunction(...);
            catalog.addTableValuedFunction(tvf);
        
        Expected Python API:
            from zetasql.api.builders import TVFBuilder
            
            tvf = (TVFBuilder("my_tvf")
                .add_argument("input_col", TypeKind.TYPE_INT64)
                .set_output_schema([
                    ("output_col1", TypeKind.TYPE_STRING),
                    ("output_col2", TypeKind.TYPE_INT64),
                ])
                .build())
            
            catalog.add_table_valued_function(tvf)
        """
        from zetasql.api.builders import TVFBuilder
        
        tvf = (TVFBuilder("my_tvf")
            .add_argument("input_col", TypeKind.TYPE_INT64)
            .set_output_schema([
                ("output_col1", TypeKind.TYPE_STRING),
                ("output_col2", TypeKind.TYPE_INT64),
            ])
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_table_valued_function(tvf)
        
        # Verify TVF was added
        assert len(catalog.get_tvf_list()) == 1
    
    def test_add_tvf_with_table_argument(self):
        """Test adding TVF that accepts table as input.
        
        TVF like: SELECT * FROM my_tvf(TABLE Orders)
        """
        from zetasql.api.builders import TVFBuilder
        from zetasql.types import FunctionArgumentType, SignatureArgumentKind
        
        tvf = (TVFBuilder("filter_table")
            .add_table_argument("input_table")  # TABLE argument
            .add_argument("filter_value", TypeKind.TYPE_INT64)
            .set_forward_input_schema()  # Output schema matches input
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_table_valued_function(tvf)
        
        assert len(catalog.get_tvf_list()) == 1
    
    def test_add_tvf_with_named_output_columns(self):
        """Test TVF with explicitly named output columns."""
        from zetasql.api.builders import TVFBuilder
        
        tvf = (TVFBuilder("generate_series")
            .add_argument("start", TypeKind.TYPE_INT64)
            .add_argument("end", TypeKind.TYPE_INT64)
            .set_output_schema([
                ("value", TypeKind.TYPE_INT64),
            ])
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_table_valued_function(tvf)
        
        tvf_obj = catalog.get_tvf_list()[0]
        # Verify output schema
        assert len(tvf_obj.output_schema) == 1
        assert tvf_obj.output_schema[0].name == "value"


@pytest.mark.skip(reason="API not implemented: SimpleCatalog.get_tvf_list() and related methods")
class TestCatalogTVFRetrieval:
    """Test retrieving TVFs from catalog - Java: getTVFList(), getTvfByFullName()"""
    
    def test_get_tvf_list(self):
        """Test SimpleCatalog.get_tvf_list() - NOT YET IMPLEMENTED.
        
        Expected API (Java):
            ImmutableList<TableValuedFunction> SimpleCatalog.getTVFList()
        """
        catalog = CatalogBuilder("db").build()
        
        # Expected API
        tvfs = catalog.get_tvf_list()
        
        assert isinstance(tvfs, list)
    
    def test_get_tvf_by_name(self):
        """Test SimpleCatalog.get_tvf_by_full_name() - NOT YET IMPLEMENTED.
        
        Expected API (Java):
            TableValuedFunction SimpleCatalog.getTvfByFullName(String name)
        """
        catalog = CatalogBuilder("db").build()
        # ... add TVF ...
        
        # Expected API
        tvf = catalog.get_tvf_by_full_name("zetasql:my_tvf")
        
        assert tvf is not None


@pytest.mark.skip(reason="API not implemented: TVF signature types")
class TestTVFSignatureTypes:
    """Test different TVF signature types - Java: ForwardInputSchemaToOutputSchemaTVF, etc."""
    
    def test_forward_input_schema_tvf(self):
        """Test TVF that forwards input schema to output.
        
        Java: ForwardInputSchemaToOutputSchemaTVF
        Use case: Filtering TVF that returns same columns as input table
        """
        from zetasql.api.builders import TVFBuilder
        
        tvf = (TVFBuilder("passthrough_filter")
            .add_table_argument("input_table")
            .add_argument("condition", TypeKind.TYPE_BOOL)
            .set_forward_input_schema()  # Output = Input
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_table_valued_function(tvf)
    
    def test_forward_input_schema_with_appended_columns(self):
        """Test TVF that forwards input + adds columns.
        
        Java: ForwardInputSchemaToOutputSchemaWithAppendedColumnTVF
        Use case: Enrichment TVF that adds columns to input
        """
        from zetasql.api.builders import TVFBuilder
        
        tvf = (TVFBuilder("enrich_table")
            .add_table_argument("input_table")
            .set_forward_input_schema()
            .append_output_column("enriched_data", TypeKind.TYPE_STRING)
            .append_output_column("enrichment_score", TypeKind.TYPE_DOUBLE)
            .build())
        
        catalog = CatalogBuilder("db").build()
        catalog.add_table_valued_function(tvf)


@pytest.mark.skip(reason="API not implemented: TVF error handling")
class TestCatalogTVFErrors:
    """Test error handling for TVF operations."""
    
    def test_add_duplicate_tvf_raises_error(self):
        """Test adding duplicate TVF raises error."""
        from zetasql.api.builders import TVFBuilder
        
        catalog = CatalogBuilder("db").build()
        
        tvf = TVFBuilder("my_tvf").build()
        catalog.add_table_valued_function(tvf)
        
        # Adding same TVF again should raise
        with pytest.raises(ValueError):
            catalog.add_table_valued_function(tvf)
    
    def test_get_nonexistent_tvf_returns_none(self):
        """Test getting non-existent TVF returns None."""
        catalog = CatalogBuilder("db").build()
        
        result = catalog.get_tvf_by_full_name("nonexistent_tvf")
        assert result is None
