"""
Level 5 Tests: Lineage Extractor - CREATE TABLE AS SELECT

Test progression:
✅ Level 1-4: Foundation
✅ Level 5: CTAS lineage extraction
⬜ Level 6-8: INSERT/UPDATE/MERGE and complex cases
"""
import pytest
from zetasql.api import Analyzer, AnalyzerOptions
from zetasql.core.types.proto_models import ResolvedCreateTableAsSelectStmt


class TestExtractorCTASBasic:
    """Test basic CTAS lineage extraction."""
    
    def test_simple_ctas(self, simple_catalog):
        """Test simple CREATE TABLE AS SELECT."""
        from zetasql_toolkit.lineage.extractor import ColumnLineageExtractor
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        sql = "CREATE TABLE target AS SELECT order_id, customer_id FROM orders"
        
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        assert isinstance(stmt, ResolvedCreateTableAsSelectStmt)
        
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
        
        # Should have 2 lineages
        assert len(lineages) == 2
        
        # Check target.order_id -> orders.order_id
        order_lineage = next(
            l for l in lineages if l.target.name.lower() == "order_id"
        )
        assert order_lineage.target.table == "target"
        assert len(order_lineage.parents) == 1
        assert ColumnEntity("orders", "order_id") in order_lineage.parents
    
    def test_ctas_with_alias(self, simple_catalog):
        """Test CTAS with column alias."""
        from zetasql_toolkit.lineage.extractor import ColumnLineageExtractor
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        sql = "CREATE TABLE target AS SELECT order_id AS id FROM orders"
        
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
        
        assert len(lineages) == 1
        lineage = list(lineages)[0]
        
        # target.id -> orders.order_id
        assert lineage.target.table == "target"
        assert lineage.target.name.lower() == "id"
        assert ColumnEntity("orders", "order_id") in lineage.parents


class TestExtractorCTASExpressions:
    """Test CTAS with expressions (matching Java example)."""
    
    def test_ctas_with_nested_functions(self, wikipedia_catalog):
        """Test CTAS with UPPER(CONCAT(...)) - matches Java example."""
        from zetasql_toolkit.lineage.extractor import ColumnLineageExtractor
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        sql = """
        CREATE TABLE target AS
        SELECT
            concatted AS column_alias
        FROM (
            SELECT 
                UPPER(CONCAT(title, comment)) AS concatted
            FROM wikipedia
        )
        GROUP BY 1
        """
        
        options = AnalyzerOptions()
        analyzer = Analyzer(options, wikipedia_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
        
        assert len(lineages) == 1
        lineage = list(lineages)[0]
        
        # target.column_alias -> {wikipedia.title, wikipedia.comment}
        assert lineage.target.table == "target"
        assert lineage.target.name.lower() == "column_alias"
        assert ColumnEntity("wikipedia", "title") in lineage.parents
        assert ColumnEntity("wikipedia", "comment") in lineage.parents


class TestExtractorCTASJoins:
    """Test CTAS with JOINs."""
    
    def test_ctas_with_join(self, simple_catalog):
        """Test CTAS with JOIN."""
        from zetasql_toolkit.lineage.extractor import ColumnLineageExtractor
        from zetasql_toolkit.lineage.models import ColumnEntity
        
        sql = """
        CREATE TABLE target AS
        SELECT o.order_id, c.name
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        """
        
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
        
        assert len(lineages) == 2
        
        # target.order_id -> orders.order_id
        order_lineage = next(l for l in lineages if l.target.name.lower() == "order_id")
        assert ColumnEntity("orders", "order_id") in order_lineage.parents
        
        # target.name -> customers.name
        name_lineage = next(l for l in lineages if l.target.name.lower() == "name")
        assert ColumnEntity("customers", "name") in name_lineage.parents


@pytest.mark.xfail(reason="Level 5 not yet implemented", strict=True)
class TestLevel5Complete:
    """Marker test to verify Level 5 is complete."""
    
    def test_all_level5_tests_pass(self):
        """This test passing means Level 5 is complete."""
        assert True
