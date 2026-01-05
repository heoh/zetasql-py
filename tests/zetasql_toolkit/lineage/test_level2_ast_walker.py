"""
Level 2 Tests: AST Walker

Test progression:
✅ Level 1: Basic data models
✅ Level 2: AST walker utilities  
⬜ Level 3: Expression finder
⬜ Level 4: Parent finder
⬜ Level 5: Extractor (CTAS)
⬜ Level 6-8: Advanced features
"""
import pytest
from zetasql.api import Analyzer, AnalyzerOptions


class TestASTWalker:
    """Test generic AST traversal utilities."""
    
    def test_walk_simple_query(self, simple_catalog):
        """Test walking a simple SELECT query AST."""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree
        
        sql = "SELECT order_id, customer_id FROM orders"
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        visited_nodes = []
        
        def visitor(node):
            visited_nodes.append(type(node).__name__)
        
        walk_resolved_tree(stmt, visitor)
        
        # Should visit multiple node types
        assert len(visited_nodes) > 0
        assert "ResolvedQueryStmt" in visited_nodes
    
    def test_walk_visits_all_nodes(self, simple_catalog):
        """Test that walker visits nested nodes."""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree
        from zetasql.core.types.proto_models import (
            ResolvedQueryStmt,
            ResolvedProjectScan,
            ResolvedTableScan,
        )
        
        sql = "SELECT order_id FROM orders"
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        node_types = []
        
        def visitor(node):
            node_types.append(type(node))
        
        walk_resolved_tree(stmt, visitor)
        
        # Should visit query, project scan, and table scan
        assert ResolvedQueryStmt in node_types
        assert ResolvedProjectScan in node_types
        assert ResolvedTableScan in node_types
    
    def test_walk_handles_lists(self, simple_catalog):
        """Test that walker handles node lists (e.g., expr_list)."""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree
        from zetasql.core.types.proto_models import ResolvedColumnRef
        
        sql = "SELECT order_id, customer_id, amount FROM orders"
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        column_refs = []
        
        def visitor(node):
            if isinstance(node, ResolvedColumnRef):
                column_refs.append(node)
        
        walk_resolved_tree(stmt, visitor)
        
        # Should find 3 column references
        assert len(column_refs) == 3


class TestVisitorDispatch:
    """Test singledispatch-based visitor pattern."""
    
    def test_visitor_dispatch_basic(self, simple_catalog):
        """Test basic visitor dispatch to different node types."""
        from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree, visit_resolved_node
        from zetasql.core.types.proto_models import ResolvedTableScan
        
        sql = "SELECT order_id FROM orders"
        options = AnalyzerOptions()
        analyzer = Analyzer(options, simple_catalog)
        stmt = analyzer.analyze_statement(sql)
        
        class MockFinder:
            def __init__(self):
                self.table_scans = []
        
        finder = MockFinder()
        
        # Register a handler for ResolvedTableScan
        @visit_resolved_node.register(ResolvedTableScan)
        def _(node: ResolvedTableScan, f: MockFinder):
            f.table_scans.append(node.table.name)
        
        def visitor(node):
            visit_resolved_node(node, finder)
        
        walk_resolved_tree(stmt, visitor)
        
        # Should have visited the orders table
        assert "orders" in finder.table_scans


@pytest.mark.xfail(reason="Level 2 not yet implemented", strict=True)
class TestLevel2Complete:
    """Marker test to verify Level 2 is complete."""
    
    def test_all_level2_tests_pass(self):
        """This test passing means Level 2 is complete."""
        assert True
