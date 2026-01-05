"""Debug INSERT implementation"""
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions
from zetasql_toolkit.lineage import ColumnLineageExtractor

source1 = TableBuilder("source1").add_column("id", TypeKind.TYPE_INT64).add_column("name", TypeKind.TYPE_STRING).build()
target = TableBuilder("target").add_column("id", TypeKind.TYPE_INT64).add_column("name", TypeKind.TYPE_STRING).build()

catalog = (
    CatalogBuilder("test")
    .add_table(source1)
    .add_table(target)
    .with_builtin_functions(options=ZetaSQLBuiltinFunctionOptions(language_options=LanguageOptions.maximum_features()))
    .build()
)

options = AnalyzerOptions(language_options=LanguageOptions.maximum_features())
analyzer = Analyzer(options=options, catalog=catalog)

sql = """
INSERT INTO target(id, name)
SELECT id, name FROM source1
"""

stmt = analyzer.analyze_statement(sql)
print(f"Statement type: {type(stmt).__name__}")
print(f"Has table_scan: {hasattr(stmt, 'table_scan')}")
print(f"Has query: {hasattr(stmt, 'query')}")
print(f"Has insert_column_list: {hasattr(stmt, 'insert_column_list')}")

if hasattr(stmt, 'table_scan'):
    table_scan = stmt.table_scan
    print(f"\nTable scan: {table_scan}")
    if table_scan and hasattr(table_scan, 'table'):
        table = table_scan.table
        print(f"Table: {table}")
        if hasattr(table, 'full_name'):
            print(f"Full name: {table.full_name}")
        if hasattr(table, 'name'):
            print(f"Name: {table.name}")

if hasattr(stmt, 'insert_column_list'):
    insert_cols = stmt.insert_column_list
    print(f"\nInsert column list length: {len(insert_cols)}")
    for i, col in enumerate(insert_cols):
        print(f"  Column {i}: {type(col).__name__}")
        if hasattr(col, 'name'):
            print(f"    name attr: {col.name}")
        if hasattr(col, 'column'):
            print(f"    column attr: {type(col.column).__name__}")

if hasattr(stmt, 'query'):
    query = stmt.query
    print(f"\nQuery: {type(query).__name__}")
    if hasattr(query, 'output_column_list'):
        out_cols = query.output_column_list
        print(f"Output columns length: {len(out_cols)}")

print("\nAttempting extraction...")
try:
    lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
    print(f"Lineages found: {len(lineages)}")
    for lineage in lineages:
        print(f"  {lineage.target.table}.{lineage.target.name} <- {lineage.parents}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
