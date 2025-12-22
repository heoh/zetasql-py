"""
Simple example to inspect ZetaSQL AST structure
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.wasi._pb2.zetasql.public import options_pb2 as public_options_pb2
from google.protobuf import text_format


def create_analyzer_options():
    opts = options_pb2.AnalyzerOptionsProto()
    language_options = opts.language_options
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    
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


def create_catalog(analyzer_options):
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    builtin_opts = catalog.builtin_function_options
    builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
    
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


def main():
    service = ZetaSqlLocalService()
    analyzer_options = create_analyzer_options()
    catalog = create_catalog(analyzer_options)
    
    print("="*70)
    print("1. Simple SELECT - Parsed AST")
    print("="*70)
    
    sql = "SELECT id, name FROM users"
    print(f"\nSQL: {sql}\n")
    
    parse_response = service.parse(sql_statement=sql)
    print(text_format.MessageToString(parse_response, indent=2))
    
    print("\n" + "="*70)
    print("2. SELECT with WHERE - Parsed AST")
    print("="*70)
    
    sql = "SELECT id, name FROM users WHERE age > 18"
    print(f"\nSQL: {sql}\n")
    
    parse_response = service.parse(sql_statement=sql)
    parsed_ast = text_format.MessageToString(parse_response, indent=2)
    
    # Show first 100 lines
    lines = parsed_ast.split('\n')
    for i, line in enumerate(lines[:100]):
        print(line)
    if len(lines) > 100:
        print(f"\n... (총 {len(lines)}줄, 처음 100줄만 표시)")
    
    print("\n" + "="*70)
    print("3. SELECT with WHERE - Resolved AST (Analyzed)")
    print("="*70)
    
    print(f"\nSQL: {sql}\n")
    
    analyze_response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    resolved_ast = text_format.MessageToString(analyze_response, indent=2)
    
    # Show first 150 lines
    lines = resolved_ast.split('\n')
    for i, line in enumerate(lines[:150]):
        print(line)
    if len(lines) > 150:
        print(f"\n... (총 {len(lines)}줄, 처음 150줄만 표시)")
    
    print("\n" + "="*70)
    print("4. Complex Query - Resolved AST")
    print("="*70)
    
    sql = """
    SELECT name, COUNT(*) as cnt 
    FROM users 
    WHERE age > 20 
    GROUP BY name 
    ORDER BY cnt DESC
    """
    print(f"\nSQL: {sql}\n")
    
    analyze_response = service.analyze(
        sql_statement=sql,
        simple_catalog=catalog,
        options=analyzer_options
    )
    
    resolved_ast = text_format.MessageToString(analyze_response, indent=2)
    
    # Show first 200 lines
    lines = resolved_ast.split('\n')
    for i, line in enumerate(lines[:200]):
        print(line)
    if len(lines) > 200:
        print(f"\n... (총 {len(lines)}줄, 처음 200줄만 표시)")


if __name__ == "__main__":
    main()
