"""Integration tests demonstrating visitor usage with realistic SQL queries."""

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
    """Sales database with employees and sales tables."""
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
    """ASTNodeVisitor usage examples with Parser."""

    def test_visitor_traverses_parsed_ast(self):
        """Collect all node types from a parsed query."""

        class NodeTypeCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.node_types = []

            def default_visit(self, node: ASTNode) -> None:
                self.node_types.append(type(node).__name__)
                super().default_visit(node)  # Call base implementation to descend

        sql = "SELECT (a + b) * c + d FROM table1"
        stmt = Parser.parse_statement_static(sql)

        visitor = NodeTypeCollector()
        visitor.visit(stmt)

        assert "ASTQueryStatement" in visitor.node_types
        assert "ASTSelect" in visitor.node_types

    def test_collect_binary_expressions(self):
        """Selectively collect specific node types (binary expressions)."""

        class BinaryExprCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.binary_exprs = []

            def visit_ASTBinaryExpression(self, node: ASTBinaryExpression) -> None:
                self.binary_exprs.append(node)
                self.descend(node)  # Continue to children

        sql = "SELECT a + b * c FROM table1"  # Has 2 binary ops: + and *
        stmt = Parser.parse_statement_static(sql)

        visitor = BinaryExprCollector()
        visitor.visit(stmt)

        assert len(visitor.binary_exprs) == 2

    def test_collect_table_references(self):
        """Extract table names from multi-table JOIN query."""

        class TableReferenceCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.table_refs = []

            def visit_ASTTablePathExpression(self, node) -> None:
                self.table_refs.append(node)
                self.descend(node)  # Continue to children

        sql = """
            SELECT e.name, s.amount
            FROM employees e
            JOIN sales s ON e.id = s.employee_id
            LEFT JOIN departments d ON e.dept_id = d.id
        """
        stmt = Parser.parse_statement_static(sql)

        visitor = TableReferenceCollector()
        visitor.visit(stmt)

        assert len(visitor.table_refs) == 3  # employees, sales, departments

    def test_collect_column_references(self):
        """Collect all column references (path expressions) from query."""

        class PathExpressionCollector(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.path_expressions = []

            def visit_ASTPathExpression(self, node: ASTPathExpression) -> None:
                self.path_expressions.append(node)
                # Don't descend - we only want the path expressions themselves

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

        assert len(visitor.path_expressions) == 9  # Multiple column and table references

    def test_count_select_statements_in_script(self):
        """Count query statements in multi-statement script."""

        class QueryCounter(ASTNodeVisitor):
            def __init__(self):
                super().__init__()
                self.count = 0

            def visit_ASTQueryStatement(self, node) -> None:
                self.count += 1
                self.descend(node)  # Continue to children

        script = Parser.parse_script_static("""
            SELECT * FROM users;
            SELECT * FROM orders;
            SELECT * FROM products;
        """)

        visitor = QueryCounter()
        for stmt in script.statement_list_node.statement_list:
            visitor.visit(stmt)

        assert visitor.count == 3


class TestResolvedNodeVisitorIntegration:
    """ResolvedNodeVisitor usage examples with Analyzer."""

    def test_collect_all_literals_from_query(self, options, sales_catalog):
        """Extract all literal values from analyzed query."""

        class LiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.literals = []

            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                self.literals.append(node)
                self.descend(node)  # Continue to children

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

        # ZetaSQL constant-folds most literals during analysis; LIMIT remains as literal
        assert len(visitor.literals) == 1

    def test_traverse_join_query_nodes(self, options, sales_catalog):
        """Count all resolved nodes in a JOIN query."""

        class NodeCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.count = 0
                self.node_types = set()

            def default_visit(self, node: ResolvedNode) -> None:
                self.count += 1
                self.node_types.add(type(node).__name__)
                super().default_visit(node)  # Call base to descend

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

        assert visitor.count == 19  # JOIN queries create many resolved nodes
        assert "ResolvedJoinScan" in visitor.node_types

    def test_count_aggregate_nodes(self, options, sales_catalog):
        """Find aggregate scan nodes in GROUP BY query."""

        class AggregateCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.aggregate_scans = []

            def visit_ResolvedAggregateScan(self, node: ResolvedAggregateScan) -> None:
                self.aggregate_scans.append(node)
                self.descend(node)  # Continue to children

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
        """

        analyzer = Analyzer(options, sales_catalog)
        resolved = analyzer.analyze_statement(sql)

        visitor = AggregateCounter()
        visitor.visit(resolved)

        assert len(visitor.aggregate_scans) == 1


class TestAdvancedVisitorPatterns:
    """Advanced visitor patterns for complex queries."""

    def test_analyze_aggregation_query_structure(self, options, sales_catalog):
        """Analyze structure of GROUP BY query with HAVING and ORDER BY."""

        class NodeTypeCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.node_types = []

            def default_visit(self, node: ResolvedNode) -> None:
                self.node_types.append(type(node).__name__)
                super().default_visit(node)  # Call base to descend

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

        assert "ResolvedAggregateScan" in visitor.node_types
        assert "ResolvedOrderByScan" in visitor.node_types
        assert len(visitor.node_types) == 21

    def test_count_subqueries(self, options, sales_catalog):
        """Count subquery expressions in nested query."""

        class SubqueryCounter(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.subquery_count = 0

            def visit_ResolvedSubqueryExpr(self, node) -> None:
                self.subquery_count += 1
                self.descend(node)  # Continue to children

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

        assert visitor.subquery_count == 2  # ZetaSQL may optimize some subqueries

    def test_collect_function_calls(self, options, sales_catalog):
        """Extract all function calls from query with string functions."""

        class FunctionCallCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.function_calls = []

            def visit_ResolvedFunctionCall(self, node) -> None:
                self.function_calls.append(node)
                self.descend(node)  # Continue to children

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

        # UPPER, LOWER, CONCAT, LENGTH (x2) - comparison > is not a function call
        assert len(visitor.function_calls) == 5

    def test_selective_traversal_skip_subqueries(self, options, sales_catalog):
        """Control traversal by skipping certain node types (early exit pattern)."""

        class SelectiveLiteralCollector(ResolvedNodeVisitor):
            def __init__(self):
                super().__init__()
                self.literals = []

            def visit_ResolvedSubqueryExpr(self, node) -> None:
                # Skip subqueries - don't call descend() or super().default_visit()
                pass

            def visit_ResolvedLiteral(self, node: ResolvedLiteral) -> None:
                self.literals.append(node)
                self.descend(node)  # Continue to children

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

        assert len(visitor.literals) == 1  # Only LIMIT literal; WHERE value is optimized
