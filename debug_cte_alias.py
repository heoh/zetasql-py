"""Debug CTE alias tracking"""
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

# Find output column
output_cols = stmt.output_column_list
print(f"Output columns: {len(output_cols)}")
for i, out_col in enumerate(output_cols):
    col = out_col.column
    print(f"  {i}: {col.name} (table: {col.table_name})")

# Walk AST to find ResolvedComputedColumn nodes
class ColumnFinder:
    def __init__(self):
        self.columns = []
    
    def visit(self, node):
        node_type = type(node).__name__
        if node_type == "ResolvedComputedColumn":
            col = node.column
            print(f"\nFound ComputedColumn: {col.name}")
            print(f"  Table: {col.table_name}")
            
            if hasattr(node, 'expr'):
                expr = node.expr
                print(f"  Expression: {type(expr).__name__}")
                
                # If it's a column ref
                if hasattr(expr, 'column'):
                    ref_col = expr.column
                    print(f"    References: {ref_col.name} (table: {ref_col.table_name})")
                
                # If it's a function call
                if hasattr(expr, 'function'):
                    func = expr.function
                    print(f"    Function: {func.name if hasattr(func, 'name') else 'unknown'}")
                    
                    if hasattr(expr, 'argument_list'):
                        args = expr.argument_list
                        print(f"    Arguments: {len(args)}")
                        for j, arg in enumerate(args):
                            print(f"      Arg {j}: {type(arg).__name__}")
                            if hasattr(arg, 'column'):
                                arg_col = arg.column
                                print(f"        Column: {arg_col.name} (table: {arg_col.table_name})")

finder = ColumnFinder()
walk_resolved_tree(stmt, finder.visit)
