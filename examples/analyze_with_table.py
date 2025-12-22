"""
Example: Analyze queries with table definitions using ZetaSQL Local Service

This example demonstrates:
1. Creating a catalog with table definitions
2. Parsing and analyzing CREATE TABLE statements
3. Analyzing SELECT queries against the defined tables
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2


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


def create_catalog_with_table(analyzer_options):
    """Create a catalog with an example table."""
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    
    # Enable builtin functions
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
    # Define a "users" table
    users_table = catalog.table.add()
    users_table.name = "users"
    
    # Add columns
    col_id = users_table.column.add()
    col_id.name = "id"
    col_id.type.type_kind = type_pb2.TYPE_INT64
    
    col_name = users_table.column.add()
    col_name.name = "name"
    col_name.type.type_kind = type_pb2.TYPE_STRING
    
    col_email = users_table.column.add()
    col_email.name = "email"
    col_email.type.type_kind = type_pb2.TYPE_STRING
    
    col_age = users_table.column.add()
    col_age.name = "age"
    col_age.type.type_kind = type_pb2.TYPE_INT64
    
    col_created_at = users_table.column.add()
    col_created_at.name = "created_at"
    col_created_at.type.type_kind = type_pb2.TYPE_TIMESTAMP
    
    # Define an "orders" table
    orders_table = catalog.table.add()
    orders_table.name = "orders"
    
    col_order_id = orders_table.column.add()
    col_order_id.name = "order_id"
    col_order_id.type.type_kind = type_pb2.TYPE_INT64
    
    col_user_id = orders_table.column.add()
    col_user_id.name = "user_id"
    col_user_id.type.type_kind = type_pb2.TYPE_INT64
    
    col_amount = orders_table.column.add()
    col_amount.name = "amount"
    col_amount.type.type_kind = type_pb2.TYPE_DOUBLE
    
    col_order_date = orders_table.column.add()
    col_order_date.name = "order_date"
    col_order_date.type.type_kind = type_pb2.TYPE_DATE
    
    return catalog


def main():
    # Initialize service
    print("Initializing ZetaSQL Local Service...")
    service = ZetaSqlLocalService()
    
    # Create analyzer options
    analyzer_options = create_analyzer_options()
    
    # Create catalog with tables
    catalog = create_catalog_with_table(analyzer_options)
    
    print("\n" + "="*70)
    print("Example 1: Parse CREATE TABLE statement")
    print("="*70)
    
    create_table_sql = """
    CREATE TABLE products (
        product_id INT64,
        name STRING,
        price FLOAT64,
        in_stock BOOL
    )
    """
    
    print(f"\nSQL:\n{create_table_sql}")
    
    try:
        parse_response = service.parse(sql_statement=create_table_sql)
        print("\n✓ CREATE TABLE statement parsed successfully!")
        print(f"  Statement type: {parse_response.parsed_statement.WhichOneof('node')}")
    except Exception as e:
        print(f"\n✗ Parse failed: {e}")
    
    print("\n" + "="*70)
    print("Example 2: Analyze simple SELECT query")
    print("="*70)
    
    simple_query = "SELECT id, name, email FROM users WHERE age > 18"
    print(f"\nSQL:\n{simple_query}")
    
    try:
        analyze_response = service.analyze(
            sql_statement=simple_query,
            simple_catalog=catalog,
            options=analyzer_options
        )
        print("\n✓ Query analyzed successfully!")
        print(f"  Statement type: {analyze_response.resolved_statement.WhichOneof('node')}")
    except Exception as e:
        print(f"\n✗ Analysis failed: {e}")
    
    print("\n" + "="*70)
    print("Example 3: Analyze query with JOIN")
    print("="*70)
    
    join_query = """
    SELECT 
        u.name,
        u.email,
        o.order_id,
        o.amount,
        o.order_date
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    WHERE o.amount > 100.0
    ORDER BY o.order_date DESC
    """
    
    print(f"\nSQL:\n{join_query}")
    
    try:
        analyze_response = service.analyze(
            sql_statement=join_query,
            simple_catalog=catalog,
            options=analyzer_options
        )
        print("\n✓ JOIN query analyzed successfully!")
        print(f"  Statement type: {analyze_response.resolved_statement.WhichOneof('node')}")
    except Exception as e:
        print(f"\n✗ Analysis failed: {e}")
    
    print("\n" + "="*70)
    print("Example 4: Analyze aggregation query")
    print("="*70)
    
    agg_query = """
    SELECT 
        u.name,
        COUNT(*) as order_count,
        SUM(o.amount) as total_amount,
        AVG(o.amount) as avg_amount
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    GROUP BY u.name
    HAVING COUNT(*) > 5
    ORDER BY total_amount DESC
    LIMIT 10
    """
    
    print(f"\nSQL:\n{agg_query}")
    
    try:
        analyze_response = service.analyze(
            sql_statement=agg_query,
            simple_catalog=catalog,
            options=analyzer_options
        )
        print("\n✓ Aggregation query analyzed successfully!")
        print(f"  Statement type: {analyze_response.resolved_statement.WhichOneof('node')}")
    except Exception as e:
        print(f"\n✗ Analysis failed: {e}")
    
    print("\n" + "="*70)
    print("Example 5: Register catalog and reuse it")
    print("="*70)
    
    try:
        # Register the catalog for reuse
        register_response = service.register_catalog(simple_catalog=catalog)
        catalog_id = register_response.registered_id
        print(f"\n✓ Catalog registered with ID: {catalog_id}")
        
        # Use the registered catalog
        query = "SELECT name, COUNT(*) as cnt FROM users GROUP BY name"
        print(f"\nSQL:\n{query}")
        
        analyze_response = service.analyze(
            sql_statement=query,
            registered_catalog_id=catalog_id,
            options=analyzer_options
        )
        print("\n✓ Query analyzed using registered catalog!")
        
        # Clean up
        service.unregister_catalog(registered_id=catalog_id)
        print("✓ Catalog unregistered")
        
    except Exception as e:
        print(f"\n✗ Failed: {e}")
    
    print("\n" + "="*70)
    print("Example 6: Extract table names from query")
    print("="*70)
    
    complex_query = """
    SELECT u.name, o.amount, p.product_name
    FROM users u
    JOIN orders o ON u.id = o.user_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    """
    
    print(f"\nSQL:\n{complex_query}")
    
    try:
        extract_response = service.extract_table_names_from_statement(
            sql_statement=complex_query
        )
        print("\n✓ Table names extracted:")
        for table in extract_response.table_name:
            table_name = ".".join(table.table_name_segment)
            print(f"  - {table_name}")
    except Exception as e:
        print(f"\n✗ Extraction failed: {e}")
    
    print("\n" + "="*70)
    print("Example 7: Format SQL query")
    print("="*70)
    
    messy_query = "select id,name,email from users where age>18 and name like '%john%' order by created_at desc limit 10"
    print(f"\nOriginal SQL:\n{messy_query}")
    
    try:
        format_response = service.format_sql(sql=messy_query)
        print(f"\n✓ Formatted SQL:\n{format_response.sql}")
    except Exception as e:
        print(f"\n✗ Formatting failed: {e}")
    
    print("\n" + "="*70)
    print("All examples completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
