#!/usr/bin/env python3
"""
Basic ZetaSQL LocalService examples with Wrappers

Simple examples demonstrating common ZetaSQL operations.
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.resolved_ast_wrapper import ResolvedQueryStmt
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2, options_pb2 as public_options_pb2


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


def create_sample_catalog(service):
    """Create and register a sample catalog with tables."""
    # Create analyzer options first
    analyzer_options = create_analyzer_options()
    
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    catalog.name = "demo"
    
    # Enable builtin functions
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
    # Create orders table
    orders = catalog.table.add()
    orders.name = "orders"
    orders.serialization_id = 1
    
    for col_name, type_kind in [
        ("order_id", type_pb2.TYPE_INT64),
        ("product_id", type_pb2.TYPE_INT64),
        ("customer_id", type_pb2.TYPE_INT64),
        ("quantity", type_pb2.TYPE_INT64),
        ("price", type_pb2.TYPE_DOUBLE),
        ("status", type_pb2.TYPE_STRING),
    ]:
        col = orders.column.add()
        col.name = col_name
        col.type.type_kind = type_kind
    
    # Register catalog
    reg_response = service.register_catalog(simple_catalog=catalog)
    return reg_response.registered_id, create_analyzer_options()


def example_1_parse():
    """Example 1: Parse SQL and check syntax."""
    print("=" * 70)
    print("Example 1: Parse SQL")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    
    sql = "SELECT product_id, SUM(quantity) FROM orders GROUP BY product_id"
    
    print(f"\nSQL: {sql}")
    
    response = service.parse(sql_statement=sql)
    
    print(f"\n✅ Parse successful!")
    print(f"   Statement type: {response.parsed_statement.WhichOneof('node')}")
    print()


def example_2_analyze():
    """Example 2: Analyze SQL with catalog."""
    print("=" * 70)
    print("Example 2: Analyze SQL")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = "SELECT product_id, SUM(quantity) as total FROM orders WHERE quantity > 0 GROUP BY product_id"
        
        print(f"\nSQL: {sql}")
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        # Use wrapper for clean access
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n✅ Analysis successful!")
        print(f"\n📊 Output Columns:")
        for i, col in enumerate(resolved_stmt.output_column_list, 1):
            col_info = f"{col.name}"
            if col.column:
                col_info += f" (column_id={col.column.column_id})"
            print(f"   {i}. {col_info}")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_3_extract_tables():
    """Example 3: Extract table names from SQL."""
    print("=" * 70)
    print("Example 3: Extract Table Names")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    
    sql = """
        SELECT o.order_id, p.product_name
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
    """
    
    print(f"\nSQL: {sql.strip()}")
    
    response = service.extract_table_names_from_statement(sql_statement=sql)
    
    print(f"\n✅ Found {len(response.table_name)} table(s):")
    for table_name in response.table_name:
        path = '.'.join(table_name.table_name_segment)
        print(f"   • {path}")
    
    print()


def example_4_format():
    """Example 4: Format SQL."""
    print("=" * 70)
    print("Example 4: Format SQL")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    
    ugly_sql = "SELECT a,b,c FROM table1 WHERE x=1 AND y=2"
    
    print(f"\nBefore: {ugly_sql}")
    
    response = service.format_sql(sql=ugly_sql)
    
    print(f"\nAfter:")
    for line in response.sql.split('\n'):
        print(f"   {line}")
    
    print()


def example_5_wrapper_benefits():
    """Example 5: Demonstrate wrapper benefits."""
    print("=" * 70)
    print("Example 5: Wrapper Benefits")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = "SELECT order_id, quantity * price as total FROM orders WHERE quantity > 0"
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        # Use wrapper
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n💡 Wrapper provides clean access:\n")
        
        # Direct property access (no .parent.parent chains!)
        print(f"   # Instead of: proto.parent.output_column_list")
        print(f"   # Use: resolved_stmt.output_column_list")
        print(f"   Output columns: {len(resolved_stmt.output_column_list)}")
        
        # Navigate scan tree
        print(f"\n   # Navigate query tree")
        if resolved_stmt.query:
            print(f"   Query scan: {type(resolved_stmt.query).__name__}")
            
            current = resolved_stmt.query
            depth = 1
            while hasattr(current, 'input_scan') and current.input_scan:
                current = current.input_scan
                print(f"   {'  ' * depth}└─ {type(current).__name__}")
                depth += 1
        
        print(f"\n   ✨ Benefits:")
        print(f"      • Clean API")
        print(f"      • Type hints for IDE")
        print(f"      • Python isinstance() works")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_6_scan_tree_traversal():
    """Example 6: Traverse scan tree using wrappers."""
    print("=" * 70)
    print("Example 6: Scan Tree Traversal with Wrappers")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = """
            SELECT product_id, quantity * price as revenue
            FROM orders
            WHERE status = 'completed' AND quantity > 0
        """
        
        print(f"\nSQL: {sql.strip()}")
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n🌳 Scan Tree (using wrapper navigation):\n")
        
        def traverse_scan(scan, depth=0):
            """Recursively traverse using wrapper methods."""
            if not scan:
                return
            
            indent = "   " * depth
            scan_type = type(scan).__name__
            print(f"{indent}└─ {scan_type}")
            
            # Show relevant information based on scan type
            if 'Project' in scan_type:
                if hasattr(scan, 'expr_list'):
                    print(f"{indent}   Expressions: {len(scan.expr_list)}")
            
            elif 'Filter' in scan_type:
                if hasattr(scan, 'filter_expr'):
                    print(f"{indent}   Has filter expression: Yes")
            
            elif 'TableScan' in scan_type:
                if hasattr(scan, 'table') and scan.table:
                    print(f"{indent}   Table: {scan.table.name if hasattr(scan.table, 'name') else 'N/A'}")
                if hasattr(scan, 'column_list'):
                    print(f"{indent}   Columns: {len(scan.column_list)}")
            
            # Navigate to input scan using wrapper property
            if hasattr(scan, 'input_scan'):
                traverse_scan(scan.input_scan, depth + 1)
        
        traverse_scan(resolved_stmt.query)
        
        print(f"\n💡 Wrapper makes tree navigation clean:")
        print(f"   • Type checking: isinstance(scan, ResolvedFilterScan)")
        print(f"   • Property access: scan.input_scan (no proto chains)")
        print(f"   • IDE support: Full autocompletion")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_7_aggregate_analysis():
    """Example 7: Analyze aggregation queries with wrappers."""
    print("=" * 70)
    print("Example 7: Aggregate Query Analysis")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = """
            SELECT 
                product_id,
                COUNT(*) as order_count,
                SUM(quantity) as total_quantity,
                AVG(price) as avg_price,
                MAX(price) as max_price
            FROM orders
            WHERE quantity > 0
            GROUP BY product_id
            HAVING COUNT(*) > 5
        """
        
        print(f"\nSQL: {sql.strip()}")
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n📊 Aggregation Analysis:\n")
        
        # Find the aggregate scan
        def find_aggregate_scan(scan):
            """Find AggregateScan using wrapper."""
            if not scan:
                return None
            
            if 'Aggregate' in type(scan).__name__:
                return scan
            
            if hasattr(scan, 'input_scan'):
                return find_aggregate_scan(scan.input_scan)
            
            return None
        
        agg_scan = find_aggregate_scan(resolved_stmt.query)
        
        if agg_scan:
            print(f"   Found: {type(agg_scan).__name__}")
            
            if hasattr(agg_scan, 'aggregate_list'):
                print(f"\n   Aggregation Functions:")
                for i, agg in enumerate(agg_scan.aggregate_list, 1):
                    if hasattr(agg, 'function') and agg.function:
                        func_name = agg.function.name if hasattr(agg.function, 'name') else 'Unknown'
                        print(f"      {i}. {func_name}()")
            
            if hasattr(agg_scan, 'group_by_list'):
                print(f"\n   GROUP BY columns: {len(agg_scan.group_by_list)}")
            
            if hasattr(agg_scan, 'having'):
                print(f"   Has HAVING clause: {agg_scan.having is not None}")
        
        print(f"\n   Output columns: {len(resolved_stmt.output_column_list)}")
        for col in resolved_stmt.output_column_list:
            print(f"      • {col.name}")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_8_column_tracking():
    """Example 8: Track column references through the query."""
    print("=" * 70)
    print("Example 8: Column Reference Tracking")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = "SELECT order_id, product_id, quantity * 2 as double_qty FROM orders"
        
        print(f"\nSQL: {sql}")
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n🔍 Column Analysis:\n")
        
        # Output columns
        print(f"   Output Columns:")
        for col in resolved_stmt.output_column_list:
            print(f"      • {col.name}")
            if hasattr(col, 'column') and col.column:
                print(f"        - ID: {col.column.column_id}")
        
        # Find table scan and check its columns
        def find_table_scan(scan):
            """Find TableScan in tree."""
            if not scan:
                return None
            
            if 'TableScan' in type(scan).__name__:
                return scan
            
            if hasattr(scan, 'input_scan'):
                return find_table_scan(scan.input_scan)
            
            return None
        
        table_scan = find_table_scan(resolved_stmt.query)
        
        if table_scan:
            print(f"\n   Source Table:")
            if hasattr(table_scan, 'table') and table_scan.table:
                print(f"      • Name: {table_scan.table.name if hasattr(table_scan.table, 'name') else 'N/A'}")
            
            if hasattr(table_scan, 'column_list'):
                print(f"      • Columns scanned: {len(table_scan.column_list)}")
        
        print(f"\n💡 Wrapper benefits for column tracking:")
        print(f"   • Direct access to column_list")
        print(f"   • Navigate through scan tree easily")
        print(f"   • Type-safe column references")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_9_expression_analysis():
    """Example 9: Analyze expressions in the query."""
    print("=" * 70)
    print("Example 9: Expression Analysis with Wrappers")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    try:
        sql = """
            SELECT 
                order_id,
                quantity * price as revenue,
                quantity * price * 1.1 as revenue_with_tax
            FROM orders
        """
        
        print(f"\nSQL: {sql.strip()}")
        
        response = service.analyze(
            sql_statement=sql,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        
        resolved_stmt = ResolvedQueryStmt(
            response.resolved_statement.resolved_query_stmt_node
        )
        
        print(f"\n🧮 Expression Analysis:\n")
        
        # Find project scan
        current = resolved_stmt.query
        while current and 'Project' not in type(current).__name__:
            if hasattr(current, 'input_scan'):
                current = current.input_scan
            else:
                break
        
        if current and hasattr(current, 'expr_list'):
            print(f"   Found {len(current.expr_list)} projected expressions")
            
            for i, expr in enumerate(current.expr_list, 1):
                expr_type = type(expr).__name__
                print(f"\n   Expression {i}: {expr_type}")
                
                # Show expression details
                if 'FunctionCall' in expr_type:
                    if hasattr(expr, 'function') and expr.function:
                        func_name = expr.function.name if hasattr(expr.function, 'name') else 'Unknown'
                        print(f"      Function: {func_name}")
                    if hasattr(expr, 'argument_list'):
                        print(f"      Arguments: {len(expr.argument_list)}")
                
                elif 'ColumnRef' in expr_type:
                    if hasattr(expr, 'column') and expr.column:
                        col_name = expr.column.name if hasattr(expr.column, 'name') else 'N/A'
                        print(f"      Column: {col_name}")
        
        print(f"\n   Output mapping:")
        for col in resolved_stmt.output_column_list:
            print(f"      {col.name}")
        
        print(f"\n💡 Expression wrappers provide:")
        print(f"   • Type information for each expression")
        print(f"   • Function call details")
        print(f"   • Argument lists")
        print(f"   • Column references")
        
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print()


def example_10_query_complexity():
    """Example 10: Measure query complexity using wrappers."""
    print("=" * 70)
    print("Example 10: Query Complexity Measurement")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    catalog_id, analyzer_options = create_sample_catalog(service)
    
    queries = [
        ("Simple", "SELECT * FROM orders"),
        ("Filtered", "SELECT * FROM orders WHERE quantity > 10"),
        ("Aggregated", "SELECT product_id, SUM(quantity) FROM orders GROUP BY product_id"),
        ("Complex", """
            SELECT product_id, COUNT(*) as cnt, SUM(quantity * price) as revenue
            FROM orders
            WHERE status = 'completed' AND quantity > 0
            GROUP BY product_id
            HAVING COUNT(*) > 5
        """),
    ]
    
    print(f"\n📊 Analyzing query complexity:\n")
    
    try:
        for name, sql in queries:
            response = service.analyze(
                sql_statement=sql,
                registered_catalog_id=catalog_id,
                options=analyzer_options
            )
            
            resolved_stmt = ResolvedQueryStmt(
                response.resolved_statement.resolved_query_stmt_node
            )
            
            # Count scan operations
            scan_count = 0
            filter_count = 0
            aggregate_count = 0
            project_count = 0
            
            def count_operations(scan):
                nonlocal scan_count, filter_count, aggregate_count, project_count
                if not scan:
                    return
                
                # For AnyResolvedScan, get the actual scan from proto
                if type(scan).__name__ == 'AnyResolvedScan':
                    # Get the actual scan type from proto
                    scan_proto = scan._proto
                    which = scan_proto.WhichOneof('node')
                    if which:
                        actual_scan_proto = getattr(scan_proto, which)
                        # Import the appropriate wrapper
                        from zetasql.resolved_ast_wrapper import (
                            ResolvedProjectScan, ResolvedFilterScan, 
                            ResolvedAggregateScan, ResolvedTableScan
                        )
                        
                        # Wrap the actual scan
                        if 'project_scan' in which:
                            scan = ResolvedProjectScan(actual_scan_proto)
                        elif 'filter_scan' in which:
                            scan = ResolvedFilterScan(actual_scan_proto)
                        elif 'aggregate_scan' in which:
                            scan = ResolvedAggregateScan(actual_scan_proto)
                        elif 'table_scan' in which:
                            scan = ResolvedTableScan(actual_scan_proto)
                
                scan_count += 1
                scan_type = type(scan).__name__
                
                if 'Filter' in scan_type:
                    filter_count += 1
                elif 'Aggregate' in scan_type:
                    aggregate_count += 1
                elif 'Project' in scan_type:
                    project_count += 1
                
                if hasattr(scan, 'input_scan') and scan.input_scan:
                    count_operations(scan.input_scan)
            
            count_operations(resolved_stmt.query)
            
            complexity_score = scan_count + filter_count * 2 + aggregate_count * 3 + project_count
            
            print(f"   {name}:")
            print(f"      Scans: {scan_count}, Filters: {filter_count}, Aggregates: {aggregate_count}, Projects: {project_count}")
            print(f"      Complexity score: {complexity_score}")
    
    finally:
        service.unregister_catalog(registered_id=catalog_id)
    
    print(f"\n💡 Wrapper makes complexity analysis easy:")
    print(f"   • Traverse tree with type checking")
    print(f"   • Count operations by type name")
    print(f"   • Handle union types (AnyResolvedScan)")
    
    print()


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("ZetaSQL LocalService + Wrapper Examples")
    print("=" * 70 + "\n")
    
    # Basic examples
    example_1_parse()
    example_2_analyze()
    example_3_extract_tables()
    example_4_format()
    example_5_wrapper_benefits()
    
    # Advanced wrapper usage examples
    example_6_scan_tree_traversal()
    example_7_aggregate_analysis()
    example_8_column_tracking()
    example_9_expression_analysis()
    example_10_query_complexity()
    
    print("=" * 70)
    print("✨ All examples completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
