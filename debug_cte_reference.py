"""Debug CTE reference tracking"""
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions
from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

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

# Get output column
output_col = stmt.output_column_list[0]
col = output_col.column

print(f"Output column: {col.name} (table: {col.table_name})")
print(f"Column ID: {id(col)}")

# Find parents
parents = ParentColumnFinder.find_parents_for_column(stmt, col)

print(f"\nFound {len(parents)} parent(s):")
for p in parents:
    print(f"  - {p.name} (table: {p.table_name}, id: {id(p)})")

# Let's trace through manually
print("\n=== Manual trace ===")

# Output column is from the WITH entry
if hasattr(output_col, 'column'):
    print(f"Output column: {output_col.column.name}")

# Check if there's a computed column
from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree

class ComputedColumnTracker:
    def __init__(self):
        self.computed_columns = {}
    
    def visit(self, node):
        if type(node).__name__ == "ResolvedComputedColumn":
            col = node.column
            self.computed_columns[id(col)] = node

tracker = ComputedColumnTracker()
walk_resolved_tree(stmt, tracker.visit)

print(f"\nFound {len(tracker.computed_columns)} computed column(s)")

# Check if output column is computed
if id(col) in tracker.computed_columns:
    print(f"Output column is COMPUTED!")
    comp_col = tracker.computed_columns[id(col)]
    expr = comp_col.expr
    print(f"Expression type: {type(expr).__name__}")
else:
    print(f"Output column is NOT in computed columns")
    print(f"Computed column IDs: {list(tracker.computed_columns.keys())}")
