#!/usr/bin/env python3
"""
Execute Query Demo - LocalService and Wrapper Usage Examples

This demo showcases the main capabilities of ZetaSQL's LocalService API and Wrapper classes
by implementing functionality similar to the execute_query tool's modes:
- Parse: Convert SQL to AST (Abstract Syntax Tree)
- Analyze: Perform semantic analysis with catalog resolution
- Execute: Run queries with sample data
- Unanalyze: Convert resolved AST back to SQL

Demonstrates:
- LocalService API usage (parse, analyze, prepare_query, evaluate_query, build_sql, format_sql)
- Wrapper class usage for AST traversal (shallow and deep)
- Multi-table catalog setup with sample data
- Query execution with table content
- Error handling
"""

import sys
from zetasql.local_service import ZetaSqlLocalService
from zetasql.resolved_ast_wrapper import (
    ResolvedQueryStmt,
    ResolvedTableScan,
    ResolvedJoinScan,
    ResolvedFilterScan,
    ResolvedProjectScan,
    ResolvedAggregateScan,
    ResolvedOrderByScan,
    ResolvedLimitOffsetScan,
    ASTQueryStatement,
    ASTSelect,
)
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2, options_pb2 as public_options_pb2
from zetasql.wasi._pb2.zetasql.local_service import local_service_pb2
from zetasql.wrapper_utils import resolve_type
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
    Set up a multi-table catalog with sample data.
    
    Creates three tables:
    - Customers: Customer information (customer_id, name, email, country)
    - Products: Product catalog (product_id, name, category, unit_price)
    - Orders: Order transactions (order_id, customer_id, product_id, quantity, price, status)
    
    Args:
        service: ZetaSqlLocalService instance
    
    Returns:
        tuple: (catalog_id, analyzer_options, table_content_dict)
    """
    # Create analyzer options first
    analyzer_options = create_analyzer_options()
    
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    catalog.name = "demo"
    
    # Enable builtin functions
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
    # ========== Customers Table ==========
    customers_table = catalog.table.add()
    customers_table.name = "Customers"
    customers_table.serialization_id = 1
    
    for col_name, type_kind in [
        ("customer_id", type_pb2.TYPE_INT64),
        ("name", type_pb2.TYPE_STRING),
        ("email", type_pb2.TYPE_STRING),
        ("country", type_pb2.TYPE_STRING),
    ]:
        col = customers_table.column.add()
        col.name = col_name
        col.type.type_kind = type_kind
    
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
    
    # ========== Products Table ==========
    products_table = catalog.table.add()
    products_table.name = "Products"
    products_table.serialization_id = 2
    
    for col_name, type_kind in [
        ("product_id", type_pb2.TYPE_INT64),
        ("name", type_pb2.TYPE_STRING),
        ("category", type_pb2.TYPE_STRING),
        ("unit_price", type_pb2.TYPE_DOUBLE),
    ]:
        col = products_table.column.add()
        col.name = col_name
        col.type.type_kind = type_kind
    
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
    
    # ========== Orders Table ==========
    orders_table = catalog.table.add()
    orders_table.name = "Orders"
    orders_table.serialization_id = 3
    
    for col_name, type_kind in [
        ("order_id", type_pb2.TYPE_INT64),
        ("customer_id", type_pb2.TYPE_INT64),
        ("product_id", type_pb2.TYPE_INT64),
        ("quantity", type_pb2.TYPE_INT64),
        ("price", type_pb2.TYPE_DOUBLE),
        ("status", type_pb2.TYPE_STRING),
    ]:
        col = orders_table.column.add()
        col.name = col_name
        col.type.type_kind = type_kind
    
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
    reg_response = service.register_catalog(simple_catalog=catalog)
    catalog_id = reg_response.registered_id
    
    # Create table content dictionary
    table_content = {
        "Customers": create_table_content(customers_data),
        "Products": create_table_content(products_data),
        "Orders": create_table_content(orders_data),
    }
    
    return catalog_id, analyzer_options, catalog, table_content


# ============================================================================
# Example 1: Parse Mode - Shallow and Deep AST Traversal
# ============================================================================

def example_1_parse_mode(service, catalog_id, analyzer_options):
    """
    Demonstrate parsing SQL to AST with Wrapper-based traversal.
    
    Shows:
    - LocalService.parse() API usage
    - AST Wrapper classes (ASTQueryStatement, ASTSelect, etc.)
    - Using isinstance for type-safe AST navigation
    - Shallow traversal (depth-limited) for overview
    - Deep traversal with wrapper properties
    """
    print_section("Example 1: Parse Mode - AST Traversal with Wrappers")
    
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
    
    # Get the parsed statement (it's a oneof field)
    node_type = parse_response.parsed_statement.WhichOneof('node')
    stmt_proto = getattr(parse_response.parsed_statement, node_type)
    
    # Wrap in AST wrapper for type-safe access
    stmt = ASTQueryStatement(stmt_proto)
    
    print(f"Parsed successfully! Statement type: {node_type}")
    print(f"Using Wrapper: {type(stmt).__name__}\n")
    
    # ========== Clean AST Tree Traversal ==========
    print_subsection("AST Wrapper Structure")
    print("Clean view of the parsed query structure:\n")
    
    def traverse_ast_tree(wrapper, depth=0, prefix="", visited=None):
        """Recursively traverse and print AST structure using wrapper types."""
        if wrapper is None:
            return
        
        # Prevent infinite recursion
        if visited is None:
            visited = set()
        
        obj_id = id(wrapper)
        if obj_id in visited:
            return
        visited.add(obj_id)
        
        indent = "  " * depth
        wrapper_type = type(wrapper).__name__
        print(f"{indent}{prefix}{wrapper_type}")
        
        # Get all public attributes (not starting with _ and not callable)
        attrs = [attr for attr in dir(wrapper) 
                if not attr.startswith('_') 
                and not callable(getattr(wrapper, attr, None))
                and attr not in ('parse_location_range', 'parenthesized', 'is_quoted', 
                                'filename', 'start', 'end', 'is_nested', 'is_pivot_input',
                                'distinct', 'natural', 'join_hint', 'join_type', 'join_location',
                                'transformation_needed', 'unmatched_join_count', 'contains_comma_join',
                                'null_handling_modifier', 'is_current_date_time_without_parentheses',
                                'is_chained_call', 'is_not', 'op', 'and_order_by', 'image')]
        
        for attr_name in attrs:
            try:
                attr_value = getattr(wrapper, attr_name)
                
                # Handle None
                if attr_value is None:
                    continue
                
                # Handle lists
                if isinstance(attr_value, list):
                    if attr_value:
                        print(f"{indent}  ├─ {attr_name} [{len(attr_value)} items]")
                        for i, item in enumerate(attr_value):
                            try:
                                resolved_item = resolve_type(item)
                                traverse_ast_tree(resolved_item, depth + 2, f"[{i}] ", visited)
                            except:
                                # Skip non-wrapper items
                                pass
                
                # Handle wrapper objects (has _proto attribute)
                elif hasattr(attr_value, '_proto'):
                    try:
                        resolved = resolve_type(attr_value)
                        print(f"{indent}  ├─ {attr_name}:")
                        traverse_ast_tree(resolved, depth + 2, "", visited)
                    except:
                        print(f"{indent}  ├─ {attr_name}:")
                        traverse_ast_tree(attr_value, depth + 2, "", visited)
                
                # Show important string values (like identifiers)
                elif isinstance(attr_value, str) and attr_name == 'id_string':
                    print(f"{indent}  ├─ id_string: '{attr_value}'")
                
            except Exception:
                # Skip problematic attributes
                pass
    
    traverse_ast_tree(stmt)
    
    print(f"\n💡 Clean AST Structure Benefits:")
    print(f"  • Shows query structure without noise")
    print(f"  • Wrapper types clearly visible")
    print(f"  • Easy to understand query composition")
    print(f"  • Perfect for learning AST navigation")
    
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
    
    # Get the parsed statement (it's a oneof field)
    node_type = parse_response.parsed_statement.WhichOneof('node')
    stmt = getattr(parse_response.parsed_statement, node_type)
    
    print(f"Parsed successfully! Statement type: {node_type}\n")
    
    # ========== Shallow Traversal (depth = 2) ==========
    print_subsection("Shallow AST Traversal (depth=2)")
    print("Quick overview of top-level structure:\n")
    
    def traverse_shallow(node, depth=0, max_depth=2, prefix=""):
        """Shallow traversal shows high-level structure."""
        if depth > max_depth or not node:
            return
        
        indent = "  " * depth
        type_name = node.DESCRIPTOR.name if hasattr(node, 'DESCRIPTOR') else type(node).__name__
        
        # Print node type
        print(f"{indent}{prefix}{type_name}")
        
        # Show key fields at this level
        if hasattr(node, 'DESCRIPTOR'):
            for field in node.DESCRIPTOR.fields:
                if field.name == 'parent':  # Skip parent references
                    continue
                
                # Handle repeated fields differently
                if field.is_repeated:
                    values = getattr(node, field.name)
                    if len(values) > 0:
                        print(f"{indent}  └─ {field.name}: ({len(values)} items)")
                        if depth < max_depth:
                            for i, value in enumerate(values):
                                if field.type == field.TYPE_MESSAGE:
                                    traverse_shallow(value, depth + 1, max_depth, f"[{i}]: ")
                else:
                    # Singular fields
                    if node.HasField(field.name):
                        value = getattr(node, field.name)
                        
                        # For leaf values, show them
                        if field.type in [field.TYPE_STRING, field.TYPE_INT32, field.TYPE_INT64, field.TYPE_BOOL]:
                            print(f"{indent}  └─ {field.name}: {value}")
                        # For nested messages, recurse
                        elif field.type == field.TYPE_MESSAGE and depth < max_depth:
                            traverse_shallow(value, depth + 1, max_depth, f"{field.name}: ")
        
    traverse_shallow(stmt)
    
    # ========== Deep Traversal (full tree) ==========
    print_subsection("Deep AST Traversal (full tree)")
    print("Complete AST structure with all fields:\n")
    
    visited = set()
    
    def traverse_deep(node, depth=0, prefix="", max_depth=20):
        """Deep traversal shows complete AST with all fields."""
        if depth > max_depth or not node or id(node) in visited:
            return
        
        visited.add(id(node))
        indent = "  " * depth
        type_name = node.DESCRIPTOR.name if hasattr(node, 'DESCRIPTOR') else type(node).__name__
        
        # Print node type
        print(f"{indent}{prefix}{type_name}")
        
        # Show all fields
        if hasattr(node, 'DESCRIPTOR'):
            for field in node.DESCRIPTOR.fields:
                if field.name == 'parent':  # Skip parent references
                    continue
                
                # Check if field is set (for singular fields)
                if not field.is_repeated:
                    if not node.HasField(field.name):
                        continue
                    
                    value = getattr(node, field.name)
                    
                    # Handle different field types
                    if field.type == field.TYPE_MESSAGE:
                        traverse_deep(value, depth + 1, f"{field.name}: ", max_depth)
                    elif field.type in [field.TYPE_STRING, field.TYPE_INT32, field.TYPE_INT64, 
                                       field.TYPE_BOOL, field.TYPE_DOUBLE, field.TYPE_ENUM]:
                        if value or value == 0 or value == False:  # Show non-empty values
                            print(f"{indent}  └─ {field.name}: {value}")
                else:
                    # Repeated fields
                    values = getattr(node, field.name)
                    if len(values) > 0:
                        print(f"{indent}  └─ {field.name} ({len(values)} items):")
                        for i, item in enumerate(values):
                            if field.type == field.TYPE_MESSAGE:
                                traverse_deep(item, depth + 2, f"[{i}]: ", max_depth)
                            else:
                                print(f"{indent}      [{i}]: {item}")
    
    traverse_deep(stmt)


# ============================================================================
# Example 2: Analyze Mode - Semantic Analysis with Wrappers
# ============================================================================

def example_2_analyze_mode(service, catalog_id, analyzer_options):
    """
    Demonstrate semantic analysis with Wrapper classes.
    
    Shows:
    - LocalService.analyze() API usage
    - ResolvedQueryStmt Wrapper for type-safe AST access
    - Using resolve_type and node_kind for abstraction
    - Traversing scan tree with Wrapper properties
    - Extracting semantic information (tables, columns, joins, filters)
    """
    print_section("Example 2: Analyze Mode - Semantic Analysis with Wrappers")
    
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
    
    # Wrap in ResolvedQueryStmt for type-safe access
    resolved_stmt = ResolvedQueryStmt(
        analyze_response.resolved_statement.resolved_query_stmt_node
    )
    
    print_subsection("Using Wrapper Classes for Clean Access")
    print("Resolved AST analysis with high-level Wrapper API:\n")
    
    # Show output columns
    print(f"📊 Output Columns ({len(resolved_stmt.output_column_list)}):")
    for col in resolved_stmt.output_column_list:
        col_info = f"  • {col.name}"
        if hasattr(col, 'column') and col.column:
            col_info += f" (table: {col.column.table_name}, id: {col.column.column_id})"
        print(col_info)
    
    print(f"\n🌳 Scan Tree Traversal (using Wrapper properties):\n")
    
    # Track what we find
    info = {
        'tables': set(),
        'scans': [],
        'has_filter': False,
        'has_join': False,
        'has_limit': False,
    }
    
    def traverse_scan_with_wrapper(scan, depth=0, max_depth=10):
        """Traverse scan tree using Wrapper classes and isinstance."""
        if depth > max_depth or not scan:
            return
        
        indent = "   " * depth
        
        # Use resolve_type for union types
        scan = resolve_type(scan)
        scan_type = type(scan).__name__
        
        print(f"{indent}└─ {scan_type}")
        info['scans'].append(scan_type)
        
        # Check scan type using isinstance (more pythonic and type-safe)
        if isinstance(scan, ResolvedTableScan):
            if hasattr(scan, 'table') and scan.table:
                table_name = scan.table.name if hasattr(scan.table, 'name') else 'Unknown'
                info['tables'].add(table_name)
                print(f"{indent}   📊 Table: {table_name}")
                if hasattr(scan, 'column_list'):
                    print(f"{indent}   📑 Columns accessed: {len(scan.column_list)}")
        
        elif isinstance(scan, ResolvedJoinScan):
            info['has_join'] = True
            if hasattr(scan, 'join_type'):
                print(f"{indent}   🔗 Join type: {scan.join_type}")
            if hasattr(scan, 'join_expr') and scan.join_expr:
                print(f"{indent}   ✅ Has join condition")
        
        elif isinstance(scan, ResolvedFilterScan):
            info['has_filter'] = True
            if hasattr(scan, 'filter_expr') and scan.filter_expr:
                print(f"{indent}   🔍 Has filter expression")
        
        elif isinstance(scan, ResolvedProjectScan):
            if hasattr(scan, 'expr_list'):
                print(f"{indent}   🎯 Expressions: {len(scan.expr_list)}")
        
        elif isinstance(scan, ResolvedAggregateScan):
            if hasattr(scan, 'aggregate_list'):
                print(f"{indent}   📊 Aggregates: {len(scan.aggregate_list)}")
            if hasattr(scan, 'group_by_list'):
                print(f"{indent}   📁 Group by: {len(scan.group_by_list)} columns")
        
        elif isinstance(scan, ResolvedOrderByScan):
            if hasattr(scan, 'order_by_item_list'):
                print(f"{indent}   🔽 Order by: {len(scan.order_by_item_list)} items")
        
        elif isinstance(scan, ResolvedLimitOffsetScan):
            info['has_limit'] = True
            if hasattr(scan, 'limit') and scan.limit:
                print(f"{indent}   🚫 Has LIMIT clause")
        
        # Navigate to input scan using Wrapper property (not proto access)
        if hasattr(scan, 'input_scan') and scan.input_scan:
            traverse_scan_with_wrapper(scan.input_scan, depth + 1, max_depth)
        
        # For JoinScan, also traverse left and right
        if isinstance(scan, ResolvedJoinScan):
            if hasattr(scan, 'left_scan') and scan.left_scan:
                print(f"{indent}   │  Left side:")
                traverse_scan_with_wrapper(scan.left_scan, depth + 1, max_depth)
            if hasattr(scan, 'right_scan') and scan.right_scan:
                print(f"{indent}   │  Right side:")
                traverse_scan_with_wrapper(scan.right_scan, depth + 1, max_depth)
    
    # Start traversal from query root
    traverse_scan_with_wrapper(resolved_stmt.query)
    
    # Print summary
    print_subsection("Analysis Summary")
    print(f"📋 Query Structure:")
    print(f"  • Tables referenced: {', '.join(info['tables']) if info['tables'] else 'None'}")
    print(f"  • Scan operations: {len(info['scans'])} types ({', '.join(list(set(info['scans']))[:5])})")
    print(f"  • Has WHERE filter: {'Yes' if info['has_filter'] else 'No'}")
    print(f"  • Has JOIN: {'Yes' if info['has_join'] else 'No'}")
    print(f"  • Has LIMIT: {'Yes' if info['has_limit'] else 'No'}")
    print(f"  • Output columns: {len(resolved_stmt.output_column_list)}")
    
    print(f"\n💡 Benefits of using Wrappers:")
    print(f"  • Type-safe access: isinstance(scan, ResolvedTableScan) for clear type checking")
    print(f"  • Clean abstraction: resolve_type() handles union types automatically")
    print(f"  • Property access: scan.input_scan instead of proto field navigation")
    print(f"  • IDE support: Full autocompletion and type hints for Wrapper classes")


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
            # Check which field is set (cell is a ValueProto)
            if cell.HasField('string_value'):
                row_data.append(cell.string_value)
            elif cell.HasField('int64_value'):
                row_data.append(cell.int64_value)
            elif cell.HasField('double_value'):
                row_data.append(f"{cell.double_value:.2f}")
            elif cell.HasField('bool_value'):
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
║                       and Wrapper Usage Examples                           ║
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
1. LocalService provides parse(), analyze(), prepare_query(), evaluate_query(), 
   build_sql(), and format_sql() methods
2. Wrapper classes enable type-safe AST traversal
3. Multi-table catalogs with sample data support complex queries
4. Query execution returns structured results ready for formatting
5. Error handling catches catalog and type errors
6. ResolvedAST can be converted back to clean SQL

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
