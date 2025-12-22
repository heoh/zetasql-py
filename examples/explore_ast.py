"""
Example: Exploring ZetaSQL AST structure

This example shows how to navigate and extract information from 
ZetaSQL's parsed and resolved AST nodes.
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2
from google.protobuf import text_format


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


def create_simple_catalog(analyzer_options):
    """Create a simple catalog with test tables."""
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    
    # Enable builtin functions
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
    # Create users table
    table = catalog.table.add()
    table.name = "users"
    
    col = table.column.add()
    col.name = "id"
    col.type.type_kind = type_pb2.TYPE_INT64
    
    col = table.column.add()
    col.name = "name"
    col.type.type_kind = type_pb2.TYPE_STRING
    
    col = table.column.add()
    col.name = "age"
    col.type.type_kind = type_pb2.TYPE_INT64
    
    return catalog


def print_proto_structure(proto, indent=0, max_depth=3, visited=None):
    """
    Print protobuf structure without infinite recursion.
    
    Args:
        proto: The protobuf message to print
        indent: Current indentation level
        max_depth: Maximum depth to traverse
        visited: Set of already visited object IDs to prevent cycles
    """
    if visited is None:
        visited = set()
    
    if indent > max_depth:
        print("  " * indent + "... (max depth reached)")
        return
    
    obj_id = id(proto)
    if obj_id in visited:
        print("  " * indent + "... (circular reference)")
        return
    
    visited.add(obj_id)
    
    # Get all fields that are set
    for field in proto.DESCRIPTOR.fields:
        # Check if field is set
        try:
            if field.label == field.LABEL_REPEATED:
                value = getattr(proto, field.name)
                if len(value) == 0:
                    continue
            else:
                # For non-repeated fields, try to check if it's set
                try:
                    if not proto.HasField(field.name):
                        continue
                except ValueError:
                    # Field doesn't support presence checking, get it anyway
                    value = getattr(proto, field.name)
                    # Skip if it's a default value for scalar types
                    if not field.message_type and value == field.default_value:
                        continue
        except:
            continue
            
        value = getattr(proto, field.name)
        
        # Skip parent references to avoid infinite loops
        if field.name == 'parent':
            print("  " * indent + f"{field.name}: <parent reference>")
            continue
        
        if field.label == field.LABEL_REPEATED:
            if len(value) == 0:
                continue
            print("  " * indent + f"{field.name}: [")
            for i, item in enumerate(value[:3]):  # Show only first 3 items
                if field.message_type:
                    print("  " * (indent + 1) + f"[{i}]:")
                    print_proto_structure(item, indent + 2, max_depth, visited.copy())
                else:
                    print("  " * (indent + 1) + f"[{i}]: {item}")
            if len(value) > 3:
                print("  " * (indent + 1) + f"... ({len(value) - 3} more items)")
            print("  " * indent + "]")
        elif field.message_type:
            print("  " * indent + f"{field.name}:")
            print_proto_structure(value, indent + 1, max_depth, visited.copy())
        else:
            # Scalar value
            print("  " * indent + f"{field.name}: {value}")


def extract_table_names_from_resolved_ast(resolved_stmt):
    """
    Extract table names from resolved AST by traversing the structure.
    
    Returns:
        list: List of table names found
    """
    tables = []
    
    def traverse(node, depth=0):
        if depth > 50:  # Prevent infinite recursion
            return
            
        # Check if this node has table information
        if hasattr(node, 'table_scan') and node.HasField('table_scan'):
            table_scan = node.table_scan
            if hasattr(table_scan, 'table') and table_scan.table:
                table_name = table_scan.table.name
                if table_name:
                    tables.append(table_name)
        
        # Traverse all child nodes
        for field in node.DESCRIPTOR.fields:
            # Skip parent references
            if field.name == 'parent':
                continue
            
            try:
                if field.label == field.LABEL_REPEATED:
                    value = getattr(node, field.name)
                    if len(value) == 0:
                        continue
                else:
                    try:
                        if not node.HasField(field.name):
                            continue
                    except ValueError:
                        # Field doesn't support presence, skip if default
                        continue
                        
                value = getattr(node, field.name)
            except:
                continue
            
            if field.label == field.LABEL_REPEATED:
                for item in value:
                    if field.message_type:
                        traverse(item, depth + 1)
            elif field.message_type:
                traverse(value, depth + 1)
    
    traverse(resolved_stmt)
    return tables


def extract_column_names_from_resolved_ast(resolved_stmt):
    """
    Extract column references from resolved AST.
    
    Returns:
        list: List of (table_name, column_name) tuples
    """
    columns = []
    
    def traverse(node, depth=0):
        if depth > 50:
            return
            
        # Check if this node is a column reference
        if hasattr(node, 'column_ref') and node.HasField('column_ref'):
            col_ref = node.column_ref
            if hasattr(col_ref, 'column') and col_ref.column:
                table_name = col_ref.column.table_name if hasattr(col_ref.column, 'table_name') else None
                column_name = col_ref.column.name if hasattr(col_ref.column, 'name') else None
                if column_name:
                    columns.append((table_name, column_name))
        
        # Traverse all child nodes
        for field in node.DESCRIPTOR.fields:
            if field.name == 'parent':
                continue
            
            try:
                if field.label == field.LABEL_REPEATED:
                    value = getattr(node, field.name)
                    if len(value) == 0:
                        continue
                else:
                    try:
                        if not node.HasField(field.name):
                            continue
                    except ValueError:
                        continue
                        
                value = getattr(node, field.name)
            except:
                continue
            
            if field.label == field.LABEL_REPEATED:
                for item in value:
                    if field.message_type:
                        traverse(item, depth + 1)
            elif field.message_type:
                traverse(value, depth + 1)
    
    traverse(resolved_stmt)
    return columns


def main():
    # Initialize service
    print("Initializing ZetaSQL Local Service...")
    service = ZetaSqlLocalService()
    
    analyzer_options = create_analyzer_options()
    catalog = create_simple_catalog(analyzer_options)
    
    print("\n" + "="*70)
    print("Example 1: Parse AST Structure")
    print("="*70)
    
    query = "SELECT id, name FROM users WHERE age > 18"
    print(f"\nSQL: {query}\n")
    
    # Parse
    parse_response = service.parse(sql_statement=query)
    
    print("Parsed AST structure (limited depth):")
    print("-" * 70)
    print_proto_structure(parse_response.parsed_statement, max_depth=4)
    
    print("\n" + "="*70)
    print("Example 2: Resolved AST Structure")
    print("="*70)
    
    # Analyze
    analyze_response = service.analyze(
        sql_statement=query,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    print("\nResolved AST structure (limited depth):")
    print("-" * 70)
    resolved_stmt = analyze_response.resolved_statement.resolved_query_stmt_node
    print_proto_structure(resolved_stmt, max_depth=4)
    
    print("\n" + "="*70)
    print("Example 3: Extract Information from AST")
    print("="*70)
    
    # Extract tables
    tables = extract_table_names_from_resolved_ast(resolved_stmt)
    print(f"\nTables referenced:")
    for table in set(tables):
        print(f"  - {table}")
    
    # Extract columns
    columns = extract_column_names_from_resolved_ast(resolved_stmt)
    print(f"\nColumns referenced:")
    for table, col in columns:
        if table:
            print(f"  - {table}.{col}")
        else:
            print(f"  - {col}")
    
    print("\n" + "="*70)
    print("Example 4: Complex Query Analysis")
    print("="*70)
    
    complex_query = """
    SELECT 
        u.name,
        COUNT(*) as order_count
    FROM users u
    WHERE u.age BETWEEN 20 AND 30
    GROUP BY u.name
    HAVING COUNT(*) > 5
    ORDER BY order_count DESC
    LIMIT 10
    """
    
    print(f"\nSQL: {complex_query}\n")
    
    analyze_response = service.analyze(
        sql_statement=complex_query,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    resolved_stmt = analyze_response.resolved_statement.resolved_query_stmt_node
    
    print("Query structure:")
    print("-" * 70)
    
    # Check for different query components
    if resolved_stmt.HasField('query'):
        query_node = resolved_stmt.query
        print(f"✓ Query type: {query_node.WhichOneof('node')}")
        
        if query_node.HasField('project_scan'):
            proj = query_node.project_scan
            print(f"✓ Projection with {len(proj.expr_list)} expressions")
            
            if proj.HasField('input_scan'):
                input_scan = proj.input_scan
                scan_type = input_scan.WhichOneof('node')
                print(f"✓ Input scan type: {scan_type}")
    
    # Extract all information
    tables = extract_table_names_from_resolved_ast(resolved_stmt)
    columns = extract_column_names_from_resolved_ast(resolved_stmt)
    
    print(f"\n✓ Tables: {set(tables)}")
    print(f"✓ Columns: {len(columns)} references")
    
    print("\n" + "="*70)
    print("Example 5: Using Text Format for Human-Readable Output")
    print("="*70)
    
    simple_query = "SELECT name FROM users LIMIT 5"
    print(f"\nSQL: {simple_query}\n")
    
    analyze_response = service.analyze(
        sql_statement=simple_query,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    # Convert to text format (human-readable)
    resolved_stmt = analyze_response.resolved_statement.resolved_query_stmt_node
    text_output = text_format.MessageToString(resolved_stmt, indent=2)
    
    # Show first 50 lines
    lines = text_output.split('\n')[:50]
    total_lines = len(text_output.split('\n'))
    print("Resolved AST (text format, first 50 lines):")
    print("-" * 70)
    for line in lines:
        print(line)
    if total_lines > 50:
        print(f"\n... ({total_lines - 50} more lines)")
    
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    print("""
The ZetaSQL AST is structured as a tree:
- Protobuf messages contain child nodes (not parent references in normal traversal)
- Parent references exist but should be avoided during traversal to prevent cycles
- Use recursive traversal with depth limits to explore the tree
- Text format provides human-readable output
- Custom extractors can pull specific information (tables, columns, etc.)

For production use, you may want to:
1. Build traversal utilities for your specific needs
2. Use pattern matching on node types
3. Cache visited nodes to handle circular references
4. Limit recursion depth for safety
""")


if __name__ == "__main__":
    main()
