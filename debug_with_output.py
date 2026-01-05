"""Debug WITH entry output columns"""
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

# Find WITH scan
class WithTracker:
    def __init__(self):
        self.with_scans = []
    
    def visit(self, node):
        if type(node).__name__ == "ResolvedWithScan":
            self.with_scans.append(node)

tracker = WithTracker()
walk_resolved_tree(stmt, tracker.visit)

with_scan = tracker.with_scans[0]
entry = with_scan.with_entry_list[0]
subquery = entry.with_subquery

print(f"WITH subquery type: {type(subquery).__name__}")
print(f"Has output_column_list: {hasattr(subquery, 'output_column_list')}")

if hasattr(subquery, 'output_column_list'):
    output_cols = subquery.output_column_list
    print(f"Output column list: {len(output_cols)}")
    
    for i, out_col in enumerate(output_cols):
        print(f"\nOutput column {i}:")
        print(f"  Type: {type(out_col).__name__}")
        
        if hasattr(out_col, 'column'):
            col = out_col.column
            print(f"  Column: {col.name} (table: {col.table_name}, id: {id(col)})")
        
        # Check if it's same as computed column
        # Actually output_column_list contains OutputColumn, not ComputedColumn

# Look at the query (ResolvedProjectScan)
print(f"\n=== Subquery structure ===")
print(f"Subquery type: {type(subquery).__name__}")

if hasattr(subquery, 'expr_list'):
    expr_list = subquery.expr_list
    print(f"Expr list: {len(expr_list)}")
    
    for i, expr in enumerate(expr_list):
        print(f"\n  Expr {i}: {type(expr).__name__}")
        
        if hasattr(expr, 'column'):
            col = expr.column
            print(f"    Column: {col.name} (table: {col.table_name}, id: {id(col)})")
        
        if hasattr(expr, 'expr'):
            inner_expr = expr.expr
            print(f"    Inner expr: {type(inner_expr).__name__}")
