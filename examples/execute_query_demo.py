#!/usr/bin/env python3
"""
Execute Query Demo - LocalService and ProtoModel Usage Examples

This demo showcases the main capabilities of ZetaSQL's LocalService API and ProtoModel classes
by implementing functionality similar to the execute_query tool's modes:
- Parse: Convert SQL to AST (Abstract Syntax Tree)
- Analyze: Perform semantic analysis with catalog resolution
- Execute: Run queries with sample data
- Unanalyze: Convert resolved AST back to SQL

Demonstrates:
- LocalService API usage (parse, analyze, prepare_query, evaluate_query, build_sql, format_sql)
- Concrete ProtoModel classes for type-safe AST traversal
- Dataclass-based model with from_proto/to_proto conversion
- Multi-table catalog setup with sample data using builders
- Query execution with table content
- Error handling
"""

import sys
from zetasql.local_service import ZetaSqlLocalService
from zetasql.types import (
    ProtoModel,
    ResolvedTableScan,
    ResolvedJoinScan,
    ResolvedFilterScan,
    ResolvedProjectScan,
    ResolvedAggregateScan,
    ResolvedOrderByScan,
    ResolvedLimitOffsetScan,
)
from zetasql.builders import TableBuilder, CatalogBuilder
from zetasql.types.type_kind import TypeKind
from zetasql.types.proto_models import ZetaSQLBuiltinFunctionOptions
from zetasql.wasi._pb2.zetasql.proto import options_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2
from google.protobuf import text_format


# ============================================================================
# Helper Functions
# ============================================================================

def create_analyzer_options():
    """Create analyzer options with all language features enabled."""
    opts = options_pb2.AnalyzerOptionsProto()
    
    language_options = opts.language_options
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    
    # Enable all language features
    for feature in dir(public_options_pb2):
        if feature.startswith('FEATURE_'):
            if feature == 'FEATURE_SPANNER_LEGACY_DDL':
                continue
            try:
                feature_value = getattr(public_options_pb2, feature)
                if isinstance(feature_value, int) and feature_value > 0:
                    language_options.enabled_language_features.append(feature_value)
            except:
                pass
    
    return opts


def create_table_content(rows_data):
    """
    Create TableContent protobuf from row data.
    
    This helper function demonstrates how to build table data for query execution.
    It automatically detects Python types and converts them to appropriate protobuf values.
    
    Args:
        rows_data: List of lists, where each inner list represents a row
                   Example: [["Alice", 25, True], ["Bob", 30, False]]
    
    Returns:
        TableContent protobuf message ready for evaluate_query
    """
    table_content = local_service_pb2.TableContent()
    table_data = table_content.table_data
    
    for row_data in rows_data:
        row = table_data.row.add()
        for value in row_data:
            cell = row.cell.add()
            if value is None:
                cell.is_null = True
            elif isinstance(value, bool):
                cell.bool_value = value
            elif isinstance(value, int):
                cell.int64_value = value
            elif isinstance(value, float):
                cell.double_value = value
            elif isinstance(value, str):
                cell.string_value = value
            else:
                raise ValueError(f"Unsupported value type: {type(value)}")
    
    return table_content


def print_table_result(columns, rows):
    """
    Print query results in ASCII table format.
    
    This helper demonstrates how to format query execution results for display.
    It automatically calculates column widths and adds borders.
    
    Args:
        columns: List of column name strings
        rows: List of row data (each row is a list of cell values)
    """
    if not columns or not rows:
        print("(empty result)")
        return
    
    # Calculate column widths
    col_widths = []
    for i, col_name in enumerate(columns):
        max_width = len(str(col_name))
        for row in rows:
            if i < len(row):
                max_width = max(max_width, len(str(row[i])))
        col_widths.append(max_width)
    
    # Print header
    header = " | ".join(str(col).ljust(width) for col, width in zip(columns, col_widths))
    separator = "-+-".join("-" * width for width in col_widths)
    
    print(header)
    print(separator)
    
    # Print rows
    for row in rows:
        row_str = " | ".join(
            str(row[i] if i < len(row) else "").ljust(width) 
            for i, width in enumerate(col_widths)
        )
        print(row_str)
    
    print(f"\n({len(rows)} rows)")


def print_section(title):
    """Print a section header for better output organization."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def print_subsection(title):
    """Print a subsection header."""
    print(f"\n--- {title} ---\n")


# ============================================================================
# Catalog and Sample Data Setup
# ============================================================================

def setup_catalog_and_data(service):
    """
    Set up a multi-table catalog with sample data using fluent builder API.
    
    Creates three tables:
    - Customers: Customer information (customer_id, name, email, country)
    - Products: Product catalog (product_id, name, category, unit_price)
    - Orders: Order transactions (order_id, customer_id, product_id, quantity, price, status)
    
    Args:
        service: ZetaSqlLocalService instance
    
    Returns:
        tuple: (catalog_id, analyzer_options, catalog, table_content_dict)
    """
    # Create analyzer options first
    analyzer_options = create_analyzer_options()
    
    # ========== Build Tables with Fluent API ==========
    
    # Customers Table
    customers = (TableBuilder("Customers", serialization_id=1)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("email", TypeKind.TYPE_STRING)
        .add_column("country", TypeKind.TYPE_STRING)
        .build())
    
    # Products Table
    products = (TableBuilder("Products", serialization_id=2)
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("name", TypeKind.TYPE_STRING)
        .add_column("category", TypeKind.TYPE_STRING)
        .add_column("unit_price", TypeKind.TYPE_DOUBLE)
        .build())
    
    # Orders Table
    orders = (TableBuilder("Orders", serialization_id=3)
        .add_column("order_id", TypeKind.TYPE_INT64)
        .add_column("customer_id", TypeKind.TYPE_INT64)
        .add_column("product_id", TypeKind.TYPE_INT64)
        .add_column("quantity", TypeKind.TYPE_INT64)
        .add_column("price", TypeKind.TYPE_DOUBLE)
        .add_column("status", TypeKind.TYPE_STRING)
        .build())
    
    # ========== Build Catalog ==========
    
    # Create builtin function options from analyzer options
    builtin_opts = ZetaSQLBuiltinFunctionOptions(
        language_options=analyzer_options.language_options
    )
    
    catalog = (CatalogBuilder("demo")
        .add_table(customers)
        .add_table(products)
        .add_table(orders)
        .with_builtin_functions(builtin_opts)
        .build())
    
    # ========== Sample Data (unchanged) ==========
    
    # Sample customer data (15 customers)
    customers_data = [
        [1, "Alice Johnson", "alice@example.com", "USA"],
        [2, "Bob Smith", "bob@example.com", "Canada"],
        [3, "Charlie Brown", "charlie@example.com", "UK"],
        [4, "Diana Prince", "diana@example.com", "USA"],
        [5, "Eve Wilson", "eve@example.com", "Australia"],
        [6, "Frank Miller", "frank@example.com", "Germany"],
        [7, "Grace Lee", "grace@example.com", "South Korea"],
        [8, "Henry Davis", "henry@example.com", "USA"],
        [9, "Iris Chen", "iris@example.com", "China"],
        [10, "Jack Robinson", "jack@example.com", "Canada"],
        [11, "Kate Martinez", "kate@example.com", "Spain"],
        [12, "Leo Wang", "leo@example.com", "China"],
        [13, "Mia Anderson", "mia@example.com", "UK"],
        [14, "Noah Taylor", "noah@example.com", "Australia"],
        [15, "Olivia Garcia", "olivia@example.com", "USA"],
    ]
    
    # Sample product data (12 products)
    products_data = [
        [101, "Laptop", "Electronics", 999.99],
        [102, "Mouse", "Electronics", 29.99],
        [103, "Keyboard", "Electronics", 79.99],
        [104, "Monitor", "Electronics", 299.99],
        [105, "Desk Chair", "Furniture", 199.99],
        [106, "Standing Desk", "Furniture", 499.99],
        [107, "Notebook", "Stationery", 4.99],
        [108, "Pen Set", "Stationery", 12.99],
        [109, "Coffee Maker", "Appliances", 89.99],
        [110, "Water Bottle", "Accessories", 19.99],
        [111, "Backpack", "Accessories", 59.99],
        [112, "Headphones", "Electronics", 149.99],
    ]
    
    # Sample order data (20 orders)
    orders_data = [
        [1001, 1, 101, 1, 999.99, "Delivered"],
        [1002, 1, 102, 2, 59.98, "Delivered"],
        [1003, 2, 103, 1, 79.99, "Shipped"],
        [1004, 3, 105, 1, 199.99, "Processing"],
        [1005, 4, 101, 1, 999.99, "Delivered"],
        [1006, 4, 104, 2, 599.98, "Delivered"],
        [1007, 5, 107, 10, 49.90, "Delivered"],
        [1008, 6, 109, 1, 89.99, "Shipped"],
        [1009, 7, 111, 1, 59.99, "Delivered"],
        [1010, 8, 112, 1, 149.99, "Processing"],
        [1011, 9, 101, 1, 999.99, "Cancelled"],
        [1012, 10, 106, 1, 499.99, "Delivered"],
        [1013, 11, 108, 3, 38.97, "Delivered"],
        [1014, 12, 110, 5, 99.95, "Shipped"],
        [1015, 13, 102, 1, 29.99, "Delivered"],
        [1016, 14, 111, 2, 119.98, "Delivered"],
        [1017, 15, 101, 1, 999.99, "Processing"],
        [1018, 2, 112, 1, 149.99, "Delivered"],
        [1019, 5, 109, 1, 89.99, "Cancelled"],
        [1020, 7, 103, 1, 79.99, "Shipped"],
    ]
    
    # Register catalog for analyze operations
    # LocalService now accepts ProtoModel directly - no need for .to_proto()
    reg_response = service.register_catalog(simple_catalog=catalog)
    catalog_id = reg_response.registered_id
    
    # Create table content dictionary
    table_content = {
        "Customers": create_table_content(customers_data),
        "Products": create_table_content(products_data),
        "Orders": create_table_content(orders_data),
    }
    
    return catalog_id, analyzer_options, catalog, table_content

def print_tree(node, depth=0, max_depth=None, prefix="", visited=None):
    """Recursively traverse and print AST structure using ProtoModel dataclasses."""
    if not node:
        return
    if max_depth and depth > max_depth:
        return
    
    indent = "  " * depth
    model_type = type(node).__name__
    print(f"{indent}{prefix}{model_type}")
    
    # For ProtoModel dataclasses, get fields from __dataclass_fields__
    if isinstance(node, ProtoModel) and hasattr(node, '__dataclass_fields__'):
        from dataclasses import fields
        
        for field in fields(node):
            field_name = field.name
            field_value = getattr(node, field_name)
            
            # Skip None values
            if field_value is None:
                continue
            
            # Skip empty lists
            if isinstance(field_value, list) and not field_value:
                continue
            
            # Handle lists
            if isinstance(field_value, list):
                print(f"{indent}  └─ {field_name} [{len(field_value)} items]")
                for i, item in enumerate(field_value):
                    if isinstance(item, ProtoModel):
                        print_tree(item, depth + 2, max_depth, f"[{i}] ")
            
            # Handle ProtoModel objects
            elif isinstance(field_value, ProtoModel):
                print_tree(field_value, depth + 1, max_depth, f"└─ {field_name}: ")
            
            # Handle primitive values (str, int, bool, etc.)
            elif isinstance(field_value, (str, int, float, bool)):
                # Only show non-default primitive values
                if field_value not in ("", 0, 0.0, False):
                    print(f"{indent}  └─ {field_name}: {repr(field_value)}")


# ============================================================================
# Example 1: Parse Mode - AST Traversal with ProtoModel
# ============================================================================

def example_1_parse_mode(service: ZetaSqlLocalService, catalog_id, analyzer_options):
    """
    Demonstrate parsing SQL to AST with ProtoModel-based traversal.
    
    Shows:
    - LocalService.parse() API usage
    - parse_proto() for converting protobuf responses to ProtoModel dataclasses
    - AST ProtoModel classes (ASTQueryStatement, ASTSelect, etc.)
    - Using isinstance for type-safe AST navigation
    - Shallow and deep traversal with dataclass fields
    """
    print_section("Example 1: Parse Mode - AST Traversal with ProtoModel")
    
    sql = """
    SELECT 
        c.name,
        c.country,
        COUNT(*) as order_count
    FROM Customers c
    JOIN Orders o ON c.customer_id = o.customer_id
    WHERE o.status = 'Delivered'
    GROUP BY c.name, c.country
    HAVING COUNT(*) > 1
    ORDER BY order_count DESC
    """
    
    print(f"SQL Query:\n{sql}\n")
    
    # Parse the SQL
    parse_response = service.parse(sql_statement=sql)
    
    # parsed_statement is already a ProtoModel (concrete type)
    # No need for parse_proto() - LocalService handles proto→ProtoModel conversion
    stmt = parse_response.parsed_statement
    
    print(f"Parsed successfully! Statement type: {type(stmt).__name__}")
    print(f"  (ProtoModel dataclass - no proto manipulation needed)")
    
    # ========== Shallow AST Tree Traversal ==========
    print_subsection("Shallow AST Structure")
    print("Shallow traversal (max depth = 3) of the AST structure:\n")
    
    print_tree(stmt, max_depth=3)

    # ========== Full AST Tree Traversal ==========
    print_subsection("Full AST Structure")
    print("Complete view of the parsed query structure:\n")
    
    print_tree(stmt)
    
    print(f"\n💡 ProtoModel Benefits:")
    print(f"  • Concrete dataclass fields (not dynamic properties)")
    print(f"  • Type-safe access with IDE autocompletion")
    print(f"  • from_proto() creates instances from protobuf")
    print(f"  • to_proto() converts back to protobuf for service calls")
    print(f"  • isinstance() checks work naturally")
    

# ============================================================================
# Example 2: Analyze Mode - Semantic Analysis with ProtoModel
# ============================================================================

def example_2_analyze_mode(service, catalog_id, analyzer_options):
    """
    Demonstrate semantic analysis with ProtoModel dataclasses.
    
    Shows:
    - LocalService.analyze() API usage
    - parse_proto() for converting responses to ProtoModel
    - ResolvedQueryStmt ProtoModel for type-safe AST access
    - Using dataclass fields for clean AST navigation
    - Traversing scan tree with concrete model instances
    - Extracting semantic information (tables, columns, joins, filters)
    """
    print_section("Example 2: Analyze Mode - Semantic Analysis with ProtoModel")
    
    sql = """
    SELECT 
        c.name as customer_name,
        p.name as product_name,
        o.quantity,
        o.price
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    JOIN Products p ON o.product_id = p.product_id
    WHERE o.status = 'Delivered' AND o.quantity > 1
    ORDER BY o.price DESC
    LIMIT 10
    """
    
    print(f"SQL Query:\n{sql}\n")
    
    # Analyze the SQL
    analyze_response = service.analyze(
        sql_statement=sql,
        registered_catalog_id=catalog_id,
        options=analyzer_options
    )
    
    # resolved_statement is already a concrete ProtoModel (e.g., ResolvedQueryStmt)
    # LocalService automatically handles union type resolution
    resolved_stmt = analyze_response.resolved_statement

    print_subsection("Using ProtoModel Dataclasses for Clean Access")
    print("Resolved AST analysis with concrete dataclass fields:\n")
    
    # Show output columns
    print(f"📊 Output Columns ({len(resolved_stmt.output_column_list)}):")
    for col in resolved_stmt.output_column_list:
        col_info = f"  • {col.name}"
        if col.column:
            col_info += f" (table: {col.column.table_name}, id: {col.column.column_id})"
        print(col_info)
    
    print(f"\n🌳 Scan Tree Traversal (using ProtoModel dataclass fields):\n")
    
    # Track what we find
    info = {
        'tables': set(),
        'scans': [],
        'has_filter': False,
        'has_join': False,
        'has_limit': False,
    }
    
    def traverse_scan_with_model(scan, depth=0, max_depth=10):
        """Traverse scan tree using ProtoModel dataclasses and isinstance."""
        if depth > max_depth or not scan:
            return
        
        indent = "   " * depth
        
        # scan is a concrete ProtoModel dataclass instance
        scan_type = type(scan).__name__
        
        print(f"{indent}└─ {scan_type}")
        info['scans'].append(scan_type)
        
        # Check scan type using isinstance (type-safe)
        if isinstance(scan, ResolvedTableScan):
            if scan.table:
                table_name = scan.table.name if hasattr(scan.table, 'name') else 'Unknown'
                info['tables'].add(table_name)
                print(f"{indent}   📊 Table: {table_name}")
                if scan.column_list:
                    print(f"{indent}   📑 Columns accessed: {len(scan.column_list)}")
        
        elif isinstance(scan, ResolvedJoinScan):
            info['has_join'] = True
            print(f"{indent}   🔗 Join type: {scan.join_type}")
            if scan.join_expr:
                print(f"{indent}   ✅ Has join condition")
        
        elif isinstance(scan, ResolvedFilterScan):
            info['has_filter'] = True
            if scan.filter_expr:
                print(f"{indent}   🔍 Has filter expression")
        
        elif isinstance(scan, ResolvedProjectScan):
            if scan.expr_list:
                print(f"{indent}   🎯 Expressions: {len(scan.expr_list)}")
        
        elif isinstance(scan, ResolvedAggregateScan):
            if scan.aggregate_list:
                print(f"{indent}   📊 Aggregates: {len(scan.aggregate_list)}")
            if scan.group_by_list:
                print(f"{indent}   📁 Group by: {len(scan.group_by_list)} columns")
        
        elif isinstance(scan, ResolvedOrderByScan):
            if scan.order_by_item_list:
                print(f"{indent}   🔽 Order by: {len(scan.order_by_item_list)} items")
        
        elif isinstance(scan, ResolvedLimitOffsetScan):
            info['has_limit'] = True
            if scan.limit:
                print(f"{indent}   🚫 Has LIMIT clause")
        
        # Navigate to input scan using dataclass field
        if hasattr(scan, 'input_scan') and scan.input_scan:
            traverse_scan_with_model(scan.input_scan, depth + 1, max_depth)
        
        # For JoinScan, also traverse left and right
        if isinstance(scan, ResolvedJoinScan):
            if scan.left_scan:
                print(f"{indent}   │  Left side:")
                traverse_scan_with_model(scan.left_scan, depth + 1, max_depth)
            if scan.right_scan:
                print(f"{indent}   │  Right side:")
                traverse_scan_with_model(scan.right_scan, depth + 1, max_depth)
    
    # Start traversal from query root
    traverse_scan_with_model(resolved_stmt.query)
    
    # Print summary
    print_subsection("Analysis Summary")
    print(f"📋 Query Structure:")
    print(f"  • Tables referenced: {', '.join(info['tables']) if info['tables'] else 'None'}")
    print(f"  • Scan operations: {len(info['scans'])} types ({', '.join(list(set(info['scans']))[:5])})")
    print(f"  • Has WHERE filter: {'Yes' if info['has_filter'] else 'No'}")
    print(f"  • Has JOIN: {'Yes' if info['has_join'] else 'No'}")
    print(f"  • Has LIMIT: {'Yes' if info['has_limit'] else 'No'}")
    print(f"  • Output columns: {len(resolved_stmt.output_column_list)}")
    
    print(f"\n💡 Benefits of ProtoModel dataclasses:")
    print(f"  • Type-safe: isinstance(scan, ResolvedTableScan) for clear type checking")
    print(f"  • Concrete: Direct field access (scan.input_scan, scan.table)")
    print(f"  • Automatic: from_proto() handles union types and nested models")
    print(f"  • IDE-friendly: Full autocompletion and type hints")
    print(f"  • Bidirectional: to_proto() converts back for service calls")


# ============================================================================
# Example 3: Execute Mode - Query Execution with Sample Data
# ============================================================================

def example_3_execute_mode(service, catalog_id, analyzer_options, simple_catalog, table_content):
    """
    Demonstrate query execution with sample data.
    
    Shows:
    - LocalService.prepare_query() API usage
    - LocalService.evaluate_query() with table content
    - LocalService.unprepare_query() for cleanup
    - Result formatting with helper functions
    """
    print_section("Example 3: Execute Mode - Query Execution")
    
    sql = """
    SELECT 
        c.name as customer_name,
        c.country,
        p.name as product_name,
        p.category,
        o.quantity,
        o.price,
        o.status
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    JOIN Products p ON o.product_id = p.product_id
    WHERE o.status IN ('Delivered', 'Shipped')
    ORDER BY o.price DESC
    LIMIT 15
    """
    
    print(f"SQL Query:\n{sql}\n")
    
    # Prepare query (use simple_catalog directly and pass table_content)
    prepare_response = service.prepare_query(
        sql=sql,
        simple_catalog=simple_catalog,
        table_content=table_content
    )
    prepared_id = prepare_response.prepared.prepared_query_id
    
    print(f"Query prepared with ID: {prepared_id}\n")
    
    # Evaluate query (table_content was provided in prepare, so not needed here)
    evaluate_response = service.evaluate_query(
        prepared_query_id=prepared_id
    )
    
    # Extract column names from prepared response
    columns = []
    for col in prepare_response.prepared.columns:
        columns.append(col.name)
    
    # Extract rows from evaluate response
    rows = []
    for row in evaluate_response.content.table_data.row:
        row_data = []
        for cell in row.cell:
            # cell is a ProtoModel - to check which oneof field is set,
            # we can check the underlying proto or use field values
            # Convert back to proto to use HasField for oneof checking
            cell_proto = cell.to_proto()
            
            if cell_proto.HasField('string_value'):
                row_data.append(cell.string_value)
            elif cell_proto.HasField('int64_value'):
                row_data.append(cell.int64_value)
            elif cell_proto.HasField('double_value'):
                row_data.append(f"{cell.double_value:.2f}")
            elif cell_proto.HasField('bool_value'):
                row_data.append(cell.bool_value)
            else:
                # No field set means NULL
                row_data.append(None)
        rows.append(row_data)
    
    # Print results
    print_subsection("Query Results")
    print_table_result(columns, rows)
    
    # Cleanup
    service.unprepare_query(prepared_query_id=prepared_id)
    print(f"\nQuery {prepared_id} unprepared (cleaned up)")


# ============================================================================
# Example 4: Error Handling
# ============================================================================

def example_4_error_handling(service, catalog_id, analyzer_options, simple_catalog, table_content):
    """
    Demonstrate error handling for common mistakes.
    
    Shows:
    - Table not found error
    - Type mismatch error
    - Proper exception handling patterns
    """
    print_section("Example 4: Error Handling")
    
    # Error 1: Non-existent table
    print_subsection("Error Case 1: Non-existent Table")
    
    bad_sql_1 = "SELECT * FROM NonExistentTable"
    print(f"SQL: {bad_sql_1}\n")
    
    try:
        analyze_response = service.analyze(
            sql_statement=bad_sql_1,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        print("Unexpected: Query succeeded")
    except Exception as e:
        print(f"✓ Expected error caught:")
        print(f"  Error type: {type(e).__name__}")
        error_msg = str(e)
        # Show first 200 chars of error message
        if len(error_msg) > 200:
            error_msg = error_msg[:200] + "..."
        print(f"  Message: {error_msg}\n")
    
    # Error 2: Type mismatch
    print_subsection("Error Case 2: Type Mismatch")
    
    bad_sql_2 = "SELECT customer_id + name FROM Customers"
    print(f"SQL: {bad_sql_2}\n")
    
    try:
        analyze_response = service.analyze(
            sql_statement=bad_sql_2,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        print("Unexpected: Query succeeded")
    except Exception as e:
        print(f"✓ Expected error caught:")
        print(f"  Error type: {type(e).__name__}")
        error_msg = str(e)
        if len(error_msg) > 200:
            error_msg = error_msg[:200] + "..."
        print(f"  Message: {error_msg}\n")


# ============================================================================
# Example 5: Unanalyze & Format - SQL Generation
# ============================================================================

def example_5_unanalyze_mode(service, catalog_id, analyzer_options):
    """
    Demonstrate converting resolved AST back to SQL.
    
    Shows:
    - LocalService.build_sql() API usage (unanalyze)
    - LocalService.format_sql() for pretty-printing
    - Comparing original vs regenerated SQL
    """
    print_section("Example 5: Unanalyze & Format - SQL Regeneration")
    
    sql = """
    SELECT c.country, COUNT(*) as customer_count, 
    SUM(o.price) as total_revenue
    FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id
    WHERE o.status = 'Delivered'
    GROUP BY c.country HAVING SUM(o.price) > 500
    ORDER BY total_revenue DESC
    """
    
    print_subsection("Original SQL")
    print(sql)
    
    # Analyze first
    analyze_response = service.analyze(
        sql_statement=sql,
        registered_catalog_id=catalog_id,
        options=analyzer_options
    )
    
    # Build SQL from resolved AST (unanalyze)
    try:
        build_sql_response = service.build_sql(
            resolved_statement=analyze_response.resolved_statement
        )
        regenerated_sql = build_sql_response.sql
        
        print_subsection("Regenerated SQL (from ResolvedAST)")
        print(regenerated_sql)
        
        # Format the regenerated SQL
        format_response = service.format_sql(sql=regenerated_sql)
        formatted_sql = format_response.sql
        
        print_subsection("Formatted SQL")
        print(formatted_sql)
        
        print("\n✓ Successfully converted: SQL → ResolvedAST → SQL")
    except Exception as e:
        print_subsection("Note")
        print(f"build_sql() encountered an issue: {str(e)[:100]}")
        print("This is a known limitation with complex queries in the reference implementation.")
        print("\n✓ Analyze completed successfully, build_sql skipped due to limitation")


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Run all examples sequentially."""
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                    Execute Query Demo - LocalService                       ║
║                      and ProtoModel Usage Examples                         ║
║                                                                            ║
║  This demo showcases ZetaSQL's capabilities through execute_query-style   ║
║  modes: Parse, Analyze, Execute, and Unanalyze                            ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize service
    print("Initializing ZetaSQL LocalService...")
    service = ZetaSqlLocalService()
    
    # Setup catalog and data
    print("Setting up catalog with 3 tables: Customers, Products, Orders...")
    catalog_id, analyzer_options, simple_catalog, table_content = setup_catalog_and_data(service)
    print("✓ Catalog ready with sample data\n")
    
    # Run examples
    try:
        example_1_parse_mode(service, catalog_id, analyzer_options)
        example_2_analyze_mode(service, catalog_id, analyzer_options)
        example_3_execute_mode(service, catalog_id, analyzer_options, simple_catalog, table_content)
        example_4_error_handling(service, catalog_id, analyzer_options, simple_catalog, table_content)
        example_5_unanalyze_mode(service, catalog_id, analyzer_options)
        
        print_section("Demo Complete")
        print("""
All examples executed successfully!

Key Takeaways:
1. LocalService automatically returns ProtoModel instances - no proto manipulation needed
2. ProtoModel provides concrete dataclass fields with full type safety
3. Access AST nodes directly: stmt.query.query_expr.select_list
4. Use isinstance() for type checking: isinstance(scan, ResolvedTableScan)
5. Multi-table catalogs with sample data support complex queries
6. Query execution returns ProtoModel results ready for inspection
7. to_proto() available when you need to pass data back to service calls
8. Error handling catches catalog and type errors naturally

For more examples, see basic_usage.py
For documentation, see EXECUTE_QUERY_DEMO.md
        """)
        
    except Exception as e:
        print(f"\n❌ Error running demo: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
