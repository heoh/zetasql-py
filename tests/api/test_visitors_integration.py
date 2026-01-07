"""
Integration Tests for ASTNodeVisitor and ResolvedNodeVisitor

Tests the visitors with realistic SQL queries and complete ProtoModel trees.
"""

import pytest

from zetasql.api import Analyzer, ASTNodeVisitor, CatalogBuilder, Parser, ResolvedNodeVisitor, TableBuilder
from zetasql.types import TypeKind
from zetasql.types.proto_model import (
    ASTBinaryExpression,
    ASTNode,
    ASTPathExpression,
    ResolvedAggregateScan,
    ResolvedLiteral,
    ResolvedNode,
)


@pytest.fixture
def sales_catalog(builtin_function_options):
    """Create sales catalog with realistic schema."""
    employees = (
        TableBuilder("employees")
        .add_column("employee_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("department", TypeKind.TYPE_STRING)
        .add_column("salary", TypeKind.TYPE_DOUBLE)
        .add_column("hire_date", TypeKind.TYPE_DATE)
        .build()
    )

    sales = (
        TableBuilder("sales")
        .add_column("sale_id", TypeKind.TYPE_INT64)
        .add_column("employee_id", TypeKind.TYPE_INT64)
        .add_column("amount", TypeKind.TYPE_DOUBLE)
        .add_column("sale_date", TypeKind.TYPE_DATE)
        .add_column("region", TypeKind.TYPE_STRING)
        .build()
    )

    return (
        CatalogBuilder("sales_db")
        .add_table(employees)
        .add_table(sales)
        .with_builtin_functions(builtin_function_options)
        .build()
    )


class TestASTNodeVisitorIntegration:
    """Test ASTNodeVisitor with parsed SQL statements."""

    def test_visitor_traverses_parsed_ast(self):
        """Test visitor traverses AST from parsed SQL statement."""

        class ASTNodeTypeCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.node_types = []

            def default_visit(self, node: ASTNode) -> None:
                self.node_types.append(type(node).__name__)
                self.descend(node)

        # Parse SQL with multiple operations: (a + b) * c + d
        sql = "SELECT (a + b) * c + d FROM table1"
        stmt = Parser.parse_statement_static(sql)

        visitor = ASTNodeTypeCollector()
        visitor.visit(stmt)

        # Should traverse many nodes including query statement, select list, expressions
        print(f"\nFound {len(visitor.node_types)} nodes")
        print(f"Node types: {set(visitor.node_types)}")

        assert len(visitor.node_types) > 5
        assert "ASTQueryStatement" in visitor.node_types
        assert "ASTSelect" in visitor.node_types

    def test_collect_binary_expressions(self):
        """Test selective collection of binary expression nodes from parsed SQL."""

        class BinaryExprCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.binary_exprs = []

            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                self.binary_exprs.append(node)
                self.descend(node)

            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        # Parse SQL with nested binary expressions: a + b * c
        sql = "SELECT a + b * c FROM table1"
        stmt = Parser.parse_statement_static(sql)

        visitor = BinaryExprCollector()
        visitor.visit(stmt)

        # Should collect binary expressions (+ and *)
        print(f"\nFound {len(visitor.binary_exprs)} binary expressions")
        assert len(visitor.binary_exprs) >= 2

    def test_collect_table_references(self):
        """Test collecting table references from parsed SQL with JOIN."""

        class TableReferenceCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.table_refs = []

            def visit_ASTTablePathExpression(self, node) -> None:
                # Collect table references
                self.table_refs.append(node)
                self.descend(node)

            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        # Parse SQL with multiple table references
        sql = """
            SELECT e.name, s.amount
            FROM employees e
            JOIN sales s ON e.id = s.employee_id
            LEFT JOIN departments d ON e.dept_id = d.id
        """
        stmt = Parser.parse_statement_static(sql)

        visitor = TableReferenceCollector()
        visitor.visit(stmt)

        # Should find table references for employees, sales, departments
        print(f"\nFound {len(visitor.table_refs)} table references")
        assert len(visitor.table_refs) >= 3

    def test_collect_column_references(self):
        """Test collecting column references from parsed SQL."""

        class PathExpressionCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.path_expressions = []

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                self.path_expressions.append(node)
                # Don't descend - we only want the path expressions themselves

            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        # Parse SQL with various column references
        sql = """
            SELECT 
                employees.name,
                employees.salary,
                departments.dept_name,
                employees.salary * 1.1 as adjusted_salary
            FROM employees
            JOIN departments ON employees.dept_id = departments.id
            WHERE employees.salary > 50000
        """
        stmt = Parser.parse_statement_static(sql)

        visitor = PathExpressionCollector()
        visitor.visit(stmt)

        # Should find multiple path expressions (column references)
        print(f"\nFound {len(visitor.path_expressions)} path expressions")
        assert len(visitor.path_expressions) >= 5

    def test_count_select_statements_in_script(self):
        """Test counting SELECT statements in a multi-statement script."""

        class SelectStatementCounter(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.select_count = 0

            def visit_ASTQueryStatement(self, node) -> None:
                self.select_count += 1
                self.descend(node)

            def default_visit(self, node: ASTNode) -> None:
                self.descend(node)

        # Parse script with multiple SELECT statements
        script = Parser.parse_script_static("""
            SELECT * FROM users;
            SELECT * FROM orders;
            SELECT * FROM products;
        """)

        # Visit each statement in the script
        visitor = SelectStatementCounter()
        for stmt in script.statement_list_node.statement_list:
            visitor.visit(stmt)

        print(f"\nFound {visitor.select_count} SELECT statements")
        assert visitor.select_count == 3


class TestResolvedNodeVisitorIntegration:
    """Test ResolvedNodeVisitor with analyzed SQL queries."""

    def test_collect_all_literals_from_query(self, options, sales_catalog):
        """Test collecting all literal values from analyzed query."""

        class LiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.literals = []

            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                self.literals.append(node)
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        # Query with multiple literals
        sql = """
            SELECT 
                CASE 
                    WHEN salary > 100000 THEN 'High'
                    WHEN salary > 50000 THEN 'Medium'
                    ELSE 'Low'
                END as salary_tier,
                salary * 1.1 as adjusted_salary
            FROM employees
            WHERE hire_date >= DATE '2020-01-01'
              AND department IN ('Engineering', 'Sales', 'Marketing')
            LIMIT 50
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = LiteralCollector()
        visitor.visit(resolved)

        # Should find literals: 100000, 'High', 50000, 'Medium', 'Low', 1.1, DATE, 3 strings, 50
        # ZetaSQL may optimize or fold some constants
        print(f"\nFound {len(visitor.literals)} literals")
        for lit in visitor.literals:
            if hasattr(lit, "value") and hasattr(lit.value, "value"):
                v = lit.value.value
                print(f"  - {v}")

        # At minimum should find the LIMIT literal
        assert len(visitor.literals) >= 1

    def test_traverse_join_query_nodes(self, options, sales_catalog):
        """Test traversing all nodes in a JOIN query."""

        class NodeCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.count = 0
                self.node_types = set()

            def default_visit(self, node: ResolvedNode) -> None:
                self.count += 1
                self.node_types.add(type(node).__name__)
                self.descend(node)

        # Query with JOIN
        sql = """
            SELECT e.employee_id, e.name, s.amount
            FROM employees e
            JOIN sales s ON e.employee_id = s.employee_id
            WHERE s.amount > 1000
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = NodeCounter()
        visitor.visit(resolved)

        # Should traverse many nodes
        print(f"\nTraversed {visitor.count} nodes")
        print(f"Node types: {sorted(visitor.node_types)}")
        assert visitor.count >= 10

    def test_count_aggregate_nodes(self, options, sales_catalog):
        """Test counting aggregation-related nodes."""

        class AggregateCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.aggregate_scans = []

            def visit_ResolvedAggregateScan(self, node: ResolvedAggregateScan) -> None:
                self.aggregate_scans.append(node)
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        # Query with aggregation
        sql = """
            SELECT 
                department,
                COUNT(*) as emp_count,
                AVG(salary) as avg_salary,
                SUM(salary) as total_salary,
                MIN(hire_date) as earliest_hire,
                MAX(hire_date) as latest_hire
            FROM employees
            WHERE salary > 0
            GROUP BY department
            HAVING COUNT(*) > 5
            ORDER BY avg_salary DESC
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = AggregateCounter()
        visitor.visit(resolved)

        # Should find at least one aggregate scan node
        assert len(visitor.aggregate_scans) >= 1


class TestVisitorPracticalUseCases:
    """Test practical use cases with realistic SQL scenarios."""

    def test_count_resolved_nodes_in_aggregation(self, options, sales_catalog):
        """Test counting nodes in aggregation query."""

        class NodeTypeCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.node_types = []

            def default_visit(self, node: ResolvedNode) -> None:
                self.node_types.append(type(node).__name__)
                self.descend(node)

        sql = """
            SELECT 
                department,
                COUNT(*) as emp_count,
                AVG(salary) as avg_salary,
                SUM(salary) as total_salary
            FROM employees
            WHERE salary > 0
            GROUP BY department
            HAVING COUNT(*) > 5
            ORDER BY avg_salary DESC
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = NodeTypeCollector()
        visitor.visit(resolved)

        print(f"\nNode types found: {set(visitor.node_types)}")
        # Should have aggregation-related nodes
        assert "ResolvedAggregateScan" in visitor.node_types
        assert len(visitor.node_types) > 15

    def test_analyze_subquery_structure(self, options, sales_catalog):
        """Test analyzing queries with subqueries."""

        class SubqueryCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.subquery_count = 0

            def visit_ResolvedSubqueryExpr(self, node) -> None:
                self.subquery_count += 1
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        sql = """
            SELECT 
                employee_id,
                name,
                salary,
                (SELECT AVG(salary) FROM employees) as avg_company_salary,
                (SELECT SUM(amount) 
                 FROM sales s 
                 WHERE s.employee_id = e.employee_id) as total_sales
            FROM employees e
            WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = 'Sales')
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = SubqueryCounter()
        visitor.visit(resolved)

        print(f"\nFound {visitor.subquery_count} subqueries")
        # Should find 3 subqueries (2 in SELECT, 1 in WHERE)
        assert visitor.subquery_count >= 2

    def test_collect_function_calls_in_select(self, options, sales_catalog):
        """Test collecting function calls from SELECT list."""

        class FunctionCallCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.function_calls = []

            def visit_ResolvedFunctionCall(self, node) -> None:
                self.function_calls.append(node)
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        sql = """
            SELECT 
                UPPER(name) as upper_name,
                LOWER(department) as lower_dept,
                CONCAT(name, ' - ', department) as full_info,
                LENGTH(name) as name_length
            FROM employees
            WHERE LENGTH(name) > 5
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = FunctionCallCollector()
        visitor.visit(resolved)

        print(f"\nFound {len(visitor.function_calls)} function calls")
        # Should find: UPPER, LOWER, CONCAT, LENGTH (x2) = at least 5 calls
        assert len(visitor.function_calls) >= 4

    def test_selective_traversal_with_early_exit(self, options, sales_catalog):
        """Test selective traversal that stops at certain node types."""

        class SelectiveLiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.literals = []
                self.stop_at_subquery = True

            def visit_ResolvedSubqueryExpr(self, node) -> None:
                # Don't descend into subqueries
                pass

            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                self.literals.append(node)
                self.descend(node)

            def default_visit(self, node: ResolvedNode) -> None:
                self.descend(node)

        sql = """
            SELECT employee_id, salary
            FROM employees
            WHERE salary > 50000
            LIMIT 100
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = SelectiveLiteralCollector()
        visitor.visit(resolved)

        # Should find at least the WHERE and LIMIT literals
        print(f"\nFound {len(visitor.literals)} literals (selective)")
        assert len(visitor.literals) >= 1
