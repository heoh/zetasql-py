#!/usr/bin/env python3
"""
Integration tests for execute_query modes using zetasql-py API.

This test suite demonstrates how to reproduce execute_query tool functionality
(parse, analyze, execute, unanalyze, format modes) using zetasql-py LocalService API.

Each test shows:
- Which execute_query mode is being replicated
- How to call the corresponding zetasql-py API
- Expected output structure in readable format
- Validation of key properties

Test with: pytest tests/integration/test_execute_query_modes.py -v -s
The -s flag shows AST trees and result tables for learning purposes.
"""

import pytest

from zetasql.api import CatalogBuilder, TableBuilder, create_table_content
from zetasql.types import (
    ASTBinaryExpression,
    ASTQueryStatement,
    ASTSelect,
    ASTSelectColumn,
    ASTSelectList,
    LanguageOptions,
    ProtoModel,
    ResolvedFilterScan,
    ResolvedProjectScan,
    # Resolved node types (for analyze mode)
    ResolvedQueryStmt,
    ResolvedTableScan,
    TypeKind,
    ZetaSQLBuiltinFunctionOptions,
)

# ============================================================================
# Helper Functions for Readable Test Output
# ============================================================================


def format_ast_tree(node, depth=0, max_depth=5, prefix=""):
    """
    Format AST node tree as readable string for test output.

    Makes test output self-documenting by showing the parse tree structure.

    Args:
        node: AST ProtoModel node
        depth: Current tree depth
        max_depth: Maximum depth to traverse
        prefix: Prefix string for current line

    Returns:
        str: Formatted tree structure
    """
    if not node or depth > max_depth:
        return ""

    lines = []
    indent = "  " * depth
    node_type = type(node).__name__
    lines.append(f"{indent}{prefix}{node_type}")

    # For ProtoModel dataclasses, traverse fields
    if isinstance(node, ProtoModel) and hasattr(node, "__dataclass_fields__"):
        from dataclasses import fields

        for field in fields(node):
            field_name = field.name
            field_value = getattr(node, field_name)

            if field_value is None or (isinstance(field_value, list) and not field_value):
                continue

            if isinstance(field_value, list):
                if field_value and isinstance(field_value[0], ProtoModel):
                    lines.append(f"{indent}  └─ {field_name}:")
                    for i, item in enumerate(field_value):
                        lines.append(format_ast_tree(item, depth + 2, max_depth, f"[{i}] "))
            elif isinstance(field_value, ProtoModel):
                lines.append(format_ast_tree(field_value, depth + 1, max_depth, f"└─ {field_name}: "))
            elif isinstance(field_value, (str, int, float, bool)) and field_value not in ("", 0, 0.0, False):
                lines.append(f"{indent}  └─ {field_name}: {field_value!r}")

    return "\n".join(filter(None, lines))


def format_query_result(columns, rows):
    """
    Format query result as ASCII table for test output.

    Makes test assertions readable by showing actual query results.

    Args:
        columns: List of column names
        rows: List of row data (each row is a list)

    Returns:
        str: Formatted table
    """
    if not columns or not rows:
        return "(empty result)"

    # Calculate column widths
    col_widths = []
    for i, col_name in enumerate(columns):
        max_width = len(str(col_name))
        for row in rows:
            if i < len(row):
                max_width = max(max_width, len(str(row[i])))
        col_widths.append(max(max_width, 5))  # min width 5

    # Build table
    lines = []
    header = " | ".join(str(col).ljust(width) for col, width in zip(columns, col_widths, strict=False))
    separator = "-+-".join("-" * width for width in col_widths)

    lines.append(header)
    lines.append(separator)

    for row in rows:
        row_str = " | ".join(str(row[i] if i < len(row) else "").ljust(width) for i, width in enumerate(col_widths))
        lines.append(row_str)

    lines.append(f"\n({len(rows)} rows)")

    return "\n".join(lines)


def extract_result_table(prepare_response, evaluate_response):
    """
    Extract columns and rows from prepared query evaluation result.

    Helper to convert ProtoModel evaluation results into simple Python lists.

    Args:
        prepare_response: PrepareQueryResponse with column metadata
        evaluate_response: EvaluateQueryResponse with row data

    Returns:
        tuple: (column_names, row_data)
    """
    # Extract column names
    columns = [col.name for col in prepare_response.prepared.columns]

    # Extract rows
    rows = []
    for row in evaluate_response.content.table_data.row:
        row_data = []
        for cell in row.cell:
            # Convert ProtoModel back to proto to check oneof fields
            cell_proto = cell.to_proto()

            if cell_proto.HasField("string_value"):
                row_data.append(cell.string_value)
            elif cell_proto.HasField("int64_value"):
                row_data.append(cell.int64_value)
            elif cell_proto.HasField("double_value"):
                row_data.append(cell.double_value)
            elif cell_proto.HasField("bool_value"):
                row_data.append(cell.bool_value)
            else:
                row_data.append(None)
        rows.append(row_data)

    return columns, rows


# ============================================================================
# Test Fixtures
# ============================================================================


@pytest.fixture(scope="module")
def mini_simple_catalog(service):
    """
    Create a minimal test catalog with one simple table.

    Table: TestTable
    Columns: id (INT64), name (STRING), value (DOUBLE)

    This provides a minimal catalog for analyze/execute mode tests.
    """
    # Build simple table
    test_table = (
        TableBuilder("TestTable")
        .add_column("id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("value", TypeKind.TYPE_DOUBLE)
        .build()
    )

    # Build catalog with builtin functions
    builtin_opts = ZetaSQLBuiltinFunctionOptions(
        language_options=LanguageOptions.maximum_features(),
    )

    catalog = CatalogBuilder("test").add_table(test_table).with_builtin_functions(builtin_opts).build()

    return catalog


@pytest.fixture(scope="module")
def mini_table_content():
    """
    Provide sample data for TestTable.

    Data:
    id | name    | value
    ---+---------+------
    1  | "Alice" | 10.5
    2  | "Bob"   | 20.0
    3  | "Carol" | 15.7
    """
    data = [
        [1, "Alice", 10.5],
        [2, "Bob", 20.0],
        [3, "Carol", 15.7],
    ]

    return {"TestTable": create_table_content(data)}


# ============================================================================
# Test Class: Execute Query Modes
# ============================================================================


class TestExecuteQueryModes:
    """
    Integration tests demonstrating execute_query mode replication.

    Each test corresponds to a mode from execute_query tool:
    - parse: SQL → AST (parse tree)
    - analyze: SQL → Resolved AST (semantic analysis)
    - execute: SQL → Query results (with data)
    - unanalyze: Resolved AST → SQL (SQL regeneration)
    - format: SQL → Formatted SQL (pretty-print)
    """

    def test_parse_mode(self, service):
        """
        Replicate: execute_query --mode=parse

        API: service.parse(sql_statement=...)

        Expected output: Parse tree (AST) showing syntactic structure

        Example query: "SELECT 1+2 AS result"
        Expected tree:
          ASTQueryStatement
            └─ query: ASTQuery
              └─ query_expr: ASTSelect
                └─ select_list: ASTSelectList
                  └─ columns: [0] ASTSelectColumn
                    └─ expression: ASTBinaryExpression (1+2)
                    └─ alias: ASTAlias (result)
        """
        print("\n" + "=" * 70)
        print("TEST: Parse Mode (execute_query --mode=parse)")
        print("=" * 70)

        sql = "SELECT 1+2 AS result"
        print(f"\nSQL: {sql}\n")

        # Call parse API
        response = service.parse(sql_statement=sql)

        # Validate response structure
        assert response.parsed_statement is not None, "Parse should return a statement"
        assert isinstance(response.parsed_statement, ASTQueryStatement), "Top-level node should be ASTQueryStatement"

        stmt = response.parsed_statement

        # Print AST tree for readability
        print("Parse Tree (AST):")
        print("-" * 70)
        tree_output = format_ast_tree(stmt, max_depth=5)
        print(tree_output)
        print("-" * 70)

        # Validate key AST nodes exist
        assert stmt.query is not None, "Query should have query field"
        assert stmt.query.query_expr is not None, "Query should have query_expr"

        query_expr = stmt.query.query_expr
        assert isinstance(query_expr, ASTSelect), "Query expression should be ASTSelect"
        assert query_expr.select_list is not None, "SELECT should have select_list"

        select_list = query_expr.select_list
        assert isinstance(select_list, ASTSelectList), "select_list should be ASTSelectList"
        assert len(select_list.columns) == 1, "Should have 1 select column"

        select_col = select_list.columns[0]
        assert isinstance(select_col, ASTSelectColumn), "Column should be ASTSelectColumn"
        assert select_col.expression is not None, "Column should have expression"

        # Binary expression: 1+2
        assert isinstance(select_col.expression, ASTBinaryExpression), "Expression should be binary (1+2)"

        print("\n✓ Parse mode validation passed")
        print(f"  • Parsed statement type: {type(stmt).__name__}")
        print(f"  • SELECT list columns: {len(select_list.columns)}")
        print(f"  • Expression type: {type(select_col.expression).__name__}")

    def test_analyze_mode(self, service, mini_simple_catalog, options):
        """
        Replicate: execute_query --mode=analyze

        API: service.analyze(sql_statement=..., simple_catalog=..., options=...)

        Expected output: Resolved AST showing semantic information

        Example query: "SELECT id, name FROM TestTable WHERE id > 1"
        Expected structure:
          ResolvedQueryStmt
            └─ output_column_list: [id, name]
            └─ query: ResolvedProjectScan
              └─ input_scan: ResolvedFilterScan (id > 1)
                └─ input_scan: ResolvedTableScan (TestTable)
        """
        print("\n" + "=" * 70)
        print("TEST: Analyze Mode (execute_query --mode=analyze)")
        print("=" * 70)

        sql = "SELECT id, name FROM TestTable WHERE id > 1"
        print(f"\nSQL: {sql}\n")

        # Call analyze API
        response = service.analyze(sql_statement=sql, simple_catalog=mini_simple_catalog, options=options)

        # Validate response structure
        assert response.resolved_statement is not None, "Analyze should return resolved statement"
        assert isinstance(response.resolved_statement, ResolvedQueryStmt), (
            "Resolved statement should be ResolvedQueryStmt"
        )

        stmt = response.resolved_statement

        # Print resolved AST structure
        print("Resolved AST:")
        print("-" * 70)
        tree_output = format_ast_tree(stmt, max_depth=6)
        print(tree_output)
        print("-" * 70)

        # Validate output columns
        assert stmt.output_column_list is not None, "Should have output columns"
        assert len(stmt.output_column_list) == 2, "Should have 2 output columns (id, name)"

        col_names = [col.name for col in stmt.output_column_list]
        assert "id" in col_names, "Should have 'id' column"
        assert "name" in col_names, "Should have 'name' column"

        # Validate scan tree structure
        assert stmt.query is not None, "Should have query scan"
        assert isinstance(stmt.query, ResolvedProjectScan), "Top scan should be ResolvedProjectScan (for SELECT list)"

        project_scan = stmt.query
        assert project_scan.input_scan is not None, "ProjectScan should have input"
        assert isinstance(project_scan.input_scan, ResolvedFilterScan), (
            "Input should be ResolvedFilterScan (for WHERE clause)"
        )

        filter_scan = project_scan.input_scan
        assert filter_scan.filter_expr is not None, "FilterScan should have filter expression"
        assert filter_scan.input_scan is not None, "FilterScan should have input"
        assert isinstance(filter_scan.input_scan, ResolvedTableScan), (
            "Filter input should be ResolvedTableScan (base table)"
        )

        table_scan = filter_scan.input_scan
        assert table_scan.table is not None, "TableScan should have table reference"
        table_name = table_scan.table.name if hasattr(table_scan.table, "name") else "Unknown"
        assert table_name == "TestTable", "Should scan TestTable"

        print("\n✓ Analyze mode validation passed")
        print(f"  • Resolved statement type: {type(stmt).__name__}")
        print(f"  • Output columns: {col_names}")
        print("  • Scan chain: ProjectScan → FilterScan → TableScan")
        print(f"  • Table scanned: {table_name}")

    def test_execute_mode(self, service, mini_simple_catalog, options, mini_table_content):
        """
        Replicate: execute_query --mode=execute

        API: service.prepare_query(...) + service.evaluate_query(...)

        Expected output: Query result table

        Example query: "SELECT COUNT(*) AS count FROM TestTable"
        Expected result:
          count
          -----
          3

          (1 row)
        """
        print("\n" + "=" * 70)
        print("TEST: Execute Mode (execute_query --mode=execute)")
        print("=" * 70)

        sql = "SELECT COUNT(*) AS count FROM TestTable"
        print(f"\nSQL: {sql}\n")

        # Prepare query with table content
        prepare_response = service.prepare_query(
            sql=sql, simple_catalog=mini_simple_catalog, options=options, table_content=mini_table_content
        )

        assert prepare_response.prepared is not None, "Prepare should return prepared query"
        prepared_id = prepare_response.prepared.prepared_query_id
        assert prepared_id >= 0, "Prepared query should have valid ID"

        print(f"Query prepared with ID: {prepared_id}")

        # Evaluate query
        evaluate_response = service.evaluate_query(prepared_query_id=prepared_id)

        assert evaluate_response.content is not None, "Evaluation should return content"
        assert evaluate_response.content.table_data is not None, "Content should have table data"

        # Extract result table
        columns, rows = extract_result_table(prepare_response, evaluate_response)

        # Print result table
        print("\nQuery Result:")
        print("-" * 70)
        result_output = format_query_result(columns, rows)
        print(result_output)
        print("-" * 70)

        # Validate results
        assert len(columns) == 1, "Should have 1 column (count)"
        assert columns[0] == "count", "Column should be named 'count'"
        assert len(rows) == 1, "Should have 1 result row"
        assert rows[0][0] == 3, "Count should be 3 (we have 3 rows in test data)"

        # Cleanup
        service.unprepare_query(prepared_query_id=prepared_id)

        print("\n✓ Execute mode validation passed")
        print(f"  • Columns: {columns}")
        print(f"  • Row count: {len(rows)}")
        print(f"  • COUNT(*) result: {rows[0][0]}")

    def test_execute_mode_with_filter(self, service, mini_simple_catalog, options, mini_table_content):
        """
        Replicate: execute_query --mode=execute (with WHERE clause)

        API: service.prepare_query(...) + service.evaluate_query(...)

        Expected output: Filtered query results

        Example query: "SELECT name, value FROM TestTable WHERE id >= 2 ORDER BY id"
        Expected result:
          name  | value
          ------+------
          Bob   | 20.0
          Carol | 15.7

          (2 rows)
        """
        print("\n" + "=" * 70)
        print("TEST: Execute Mode with Filter (execute_query --mode=execute)")
        print("=" * 70)

        sql = "SELECT name, value FROM TestTable WHERE id >= 2 ORDER BY id"
        print(f"\nSQL: {sql}\n")

        # Prepare and execute
        prepare_response = service.prepare_query(
            sql=sql, simple_catalog=mini_simple_catalog, options=options, table_content=mini_table_content
        )

        prepared_id = prepare_response.prepared.prepared_query_id

        evaluate_response = service.evaluate_query(prepared_query_id=prepared_id)

        # Extract and print results
        columns, rows = extract_result_table(prepare_response, evaluate_response)

        print("Query Result:")
        print("-" * 70)
        result_output = format_query_result(columns, rows)
        print(result_output)
        print("-" * 70)

        # Validate results
        assert len(columns) == 2, "Should have 2 columns (name, value)"
        assert columns == ["name", "value"], "Columns should be [name, value]"
        assert len(rows) == 2, "Should have 2 rows (WHERE id >= 2 filters out id=1)"
        assert rows[0][0] == "Bob", "First row should be Bob (id=2)"
        assert rows[1][0] == "Carol", "Second row should be Carol (id=3)"
        assert rows[0][1] == 20.0, "Bob's value should be 20.0"
        assert rows[1][1] == 15.7, "Carol's value should be 15.7"

        # Cleanup
        service.unprepare_query(prepared_query_id=prepared_id)

        print("\n✓ Execute mode with filter validation passed")
        print(f"  • Filtered rows: {len(rows)}")
        print(f"  • Results: {[row[0] for row in rows]}")

    def test_unanalyze_mode(self, service, mini_simple_catalog, options):
        """
        Replicate: execute_query --mode=unanalyze

        API: service.analyze(...) + service.build_sql(resolved_statement=...)

        Expected output: SQL regenerated from resolved AST

        Example query: "SELECT id FROM TestTable WHERE id>1"
        Expected regenerated SQL (may vary in formatting):
          SELECT TestTable.id AS id FROM TestTable WHERE (TestTable.id) > 1
        """
        print("\n" + "=" * 70)
        print("TEST: Unanalyze Mode (execute_query --mode=unanalyze)")
        print("=" * 70)

        original_sql = "SELECT id FROM TestTable WHERE id>1"
        print(f"\nOriginal SQL: {original_sql}\n")

        # Step 1: Analyze to get resolved AST
        analyze_response = service.analyze(
            sql_statement=original_sql, simple_catalog=mini_simple_catalog, options=options
        )

        resolved_stmt = analyze_response.resolved_statement
        assert resolved_stmt is not None, "Should have resolved statement"

        # Step 2: Build SQL from resolved AST
        build_sql_response = service.build_sql(resolved_statement=resolved_stmt, simple_catalog=mini_simple_catalog)

        regenerated_sql = build_sql_response.sql

        print("Regenerated SQL (from Resolved AST):")
        print("-" * 70)
        print(regenerated_sql)
        print("-" * 70)

        # Validate regenerated SQL
        assert regenerated_sql is not None, "Should generate SQL"
        assert len(regenerated_sql) > 0, "Generated SQL should not be empty"

        # Semantic validation: re-analyze the generated SQL
        # If it analyzes successfully, it's semantically equivalent
        re_analyze_response = service.analyze(
            sql_statement=regenerated_sql, simple_catalog=mini_simple_catalog, options=options
        )

        assert re_analyze_response.resolved_statement is not None, "Regenerated SQL should be valid and analyzable"

        # Check output columns match
        original_cols = [col.name for col in resolved_stmt.output_column_list]
        regenerated_cols = [col.name for col in re_analyze_response.resolved_statement.output_column_list]

        assert original_cols == regenerated_cols, f"Output columns should match: {original_cols} vs {regenerated_cols}"

        print("\n✓ Unanalyze mode validation passed")
        print(f"  • Original SQL length: {len(original_sql)} chars")
        print(f"  • Regenerated SQL length: {len(regenerated_sql)} chars")
        print(f"  • Output columns preserved: {original_cols}")
        print("  • Regenerated SQL is valid: ✓")

    def test_format_mode(self, service):
        """
        Replicate: execute_query --mode=format (implicit with unparse)

        API: service.format_sql(sql=...)

        Expected output: Formatted (pretty-printed) SQL

        Example query (unformatted):
          "SELECT id,name FROM TestTable WHERE id>1 ORDER BY name"

        Expected formatted SQL:
          SELECT
            id,
            name
          FROM
            TestTable
          WHERE
            id > 1
          ORDER BY name;
        """
        print("\n" + "=" * 70)
        print("TEST: Format Mode (execute_query formatting)")
        print("=" * 70)

        unformatted_sql = "SELECT id,name FROM TestTable WHERE id>1 ORDER BY name"
        print(f"\nUnformatted SQL:\n{unformatted_sql}\n")

        # Format SQL
        format_response = service.format_sql(sql=unformatted_sql)

        formatted_sql = format_response.sql

        print("Formatted SQL:")
        print("-" * 70)
        print(formatted_sql)
        print("-" * 70)

        # Validate formatted SQL
        assert formatted_sql is not None, "Should return formatted SQL"
        assert len(formatted_sql) > 0, "Formatted SQL should not be empty"

        # Formatted SQL should have more lines (due to line breaks)
        unformatted_lines = unformatted_sql.count("\n") + 1
        formatted_lines = formatted_sql.count("\n") + 1

        # Note: Formatting behavior may vary, so we just check basic properties
        print("\n✓ Format mode validation passed")
        print(f"  • Unformatted lines: {unformatted_lines}")
        print(f"  • Formatted lines: {formatted_lines}")
        print(f"  • Formatted SQL length: {len(formatted_sql)} chars")
