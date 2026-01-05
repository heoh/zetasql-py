"""Debug CTE computed column mapping"""
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions
from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

users = TableBuilder("users").add_column("id", TypeKind.TYPE_INT64).add_column("name", TypeKind.TYPE_STRING).build()

catalog = (
    CatalogBuilder("test")
    .add_table(users)
    .with_builtin_functions(options=ZetaSQLBuiltinFunctionOptions(language_options=LanguageOptions.maximum_features()))
    .build()
)

options = AnalyzerOptions(language_options=LanguageOptions.maximum_features())
analyzer = Analyzer(options=options, catalog=catalog)

sql = """
WITH processed AS (
    SELECT UPPER(name) AS upper_name FROM users
)
SELECT upper_name FROM processed
"""

stmt = analyzer.analyze_statement(sql)

# Find WITH scan and WITH ref scan
class WithTracker:
    def __init__(self):
        self.with_scans = []
        self.with_refs = []
        self.computed_columns = []
    
    def visit(self, node):
        node_type = type(node).__name__
        
        if node_type == "ResolvedWithScan":
            self.with_scans.append(node)
        elif node_type == "ResolvedWithRefScan":
            self.with_refs.append(node)
        elif node_type == "ResolvedComputedColumn":
            self.computed_columns.append(node)

tracker = WithTracker()
walk_resolved_tree(stmt, tracker.visit)

print(f"WITH scans: {len(tracker.with_scans)}")
print(f"WITH refs: {len(tracker.with_refs)}")
print(f"Computed columns: {len(tracker.computed_columns)}")

# Check WITH scan structure
if tracker.with_scans:
    with_scan = tracker.with_scans[0]
    entry_list = with_scan.with_entry_list
    
    print(f"\n=== WITH entries: {len(entry_list)} ===")
    for i, entry in enumerate(entry_list):
        print(f"\nEntry {i}:")
        print(f"  Name: {entry.with_query_name}")
        
        if hasattr(entry, 'with_subquery'):
            subquery = entry.with_subquery
            print(f"  Subquery type: {type(subquery).__name__}")
            
            if hasattr(subquery, 'output_column_list'):
                output_cols = subquery.output_column_list
                print(f"  Output columns: {len(output_cols)}")
                
                for j, out_col in enumerate(output_cols):
                    col = out_col.column
                    print(f"    {j}: {col.name} (table: {col.table_name}, id: {id(col)})")

# Check WITH ref structure
if tracker.with_refs:
    with_ref = tracker.with_refs[0]
    print(f"\n=== WITH REF ===")
    print(f"  Name: {with_ref.with_query_name}")
    
    if hasattr(with_ref, 'column_list'):
        col_list = with_ref.column_list
        print(f"  Column list: {len(col_list)}")
        
        for i, col in enumerate(col_list):
            print(f"    {i}: {col.name} (table: {col.table_name}, id: {id(col)})")

# Check computed columns
print(f"\n=== Computed columns ===")
for i, comp in enumerate(tracker.computed_columns):
    col = comp.column
    print(f"{i}: {col.name} (table: {col.table_name}, id: {id(col)})")
    
    if hasattr(comp, 'expr'):
        expr = comp.expr
        print(f"  Expression: {type(expr).__name__}")
