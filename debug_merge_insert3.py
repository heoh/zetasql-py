"""Debug ResolvedDMLValue structure"""
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions

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
MERGE target T
USING source1 S
ON T.id = S.id
WHEN NOT MATCHED THEN
    INSERT(id, name) VALUES (S.id, UPPER(S.name))
"""

stmt = analyzer.analyze_statement(sql)

clause = stmt.when_clause_list[0]
insert_row = clause.insert_row
value_list = insert_row.value_list

print(f"Number of DML values: {len(value_list)}")

for i, dml_value in enumerate(value_list):
    print(f"\n=== DML Value {i} ===")
    print(f"Type: {type(dml_value).__name__}")
    print(f"Has value: {hasattr(dml_value, 'value')}")
    
    if hasattr(dml_value, 'value'):
        value_expr = dml_value.value
        print(f"value type: {type(value_expr).__name__}")
        
        # Check if it's a column reference
        if hasattr(value_expr, 'column'):
            col = value_expr.column
            print(f"  Column name: {col.name}")
            print(f"  Table: {col.table_name}")
        
        # Check if it's a function call
        if hasattr(value_expr, 'function'):
            func = value_expr.function
            print(f"  Function: {func.name if hasattr(func, 'name') else 'unknown'}")
