"""Debug INSERT extraction step by step"""
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions
from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder
from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage

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

# Manual extraction
table_scan = getattr(stmt, "table_scan", None)
print(f"table_scan: {table_scan is not None}")

table = getattr(table_scan, "table", None)
print(f"table: {table}")
target_table = getattr(table, "full_name", "") if table else ""
print(f"target_table: '{target_table}'")

query = getattr(stmt, "query", None)
print(f"query: {query is not None}")

insert_column_list = getattr(stmt, "insert_column_list", []) or []
print(f"insert_column_list length: {len(insert_column_list)}")

query_output_list = getattr(query, "output_column_list", []) or [] if query else []
print(f"query_output_list length: {len(query_output_list)}")

print("\nProcessing columns:")
for i, insert_col in enumerate(insert_column_list):
    print(f"\n=== Column {i} ===")
    print(f"insert_col type: {type(insert_col).__name__}")
    print(f"insert_col: {insert_col}")
    
    if i < len(query_output_list):
        query_output = query_output_list[i]
        print(f"query_output type: {type(query_output).__name__}")
        print(f"query_output: {query_output}")
        
        query_column = getattr(query_output, "column", None)
        print(f"query_column: {query_column}")
        
        if query_column:
            col_name = getattr(insert_col, "name", None)
            print(f"col_name: {col_name}")
            
            print(f"Calling ParentColumnFinder.find_parents_for_column...")
            try:
                parents = ParentColumnFinder.find_parents_for_column(stmt, query_column)
                print(f"Parents found: {len(parents)}")
                for p in parents:
                    print(f"  - {p.table_name}.{p.name}")
            except Exception as e:
                print(f"Error finding parents: {e}")
                import traceback
                traceback.print_exc()
