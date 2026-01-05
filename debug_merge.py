"""Debug MERGE"""
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
WHEN MATCHED THEN
    UPDATE SET name = S.name
"""

stmt = analyzer.analyze_statement(sql)
print(f"Statement type: {type(stmt).__name__}")
print(f"Has when_clause_list: {hasattr(stmt, 'when_clause_list')}")

if hasattr(stmt, 'when_clause_list'):
    clauses = stmt.when_clause_list
    print(f"Number of when clauses: {len(clauses)}")
    
    for i, clause in enumerate(clauses):
        print(f"\n=== When clause {i} ===")
        print(f"Type: {type(clause).__name__}")
        print(f"Has insert_stmt: {hasattr(clause, 'insert_stmt')}")
        print(f"Has update_stmt: {hasattr(clause, 'update_stmt')}")
        
        if hasattr(clause, 'update_stmt'):
            update_stmt = clause.update_stmt
            print(f"update_stmt: {update_stmt}")
            print(f"update_stmt type: {type(update_stmt).__name__ if update_stmt else 'None'}")
            
            if update_stmt:
                print(f"Has update_item_list: {hasattr(update_stmt, 'update_item_list')}")
                if hasattr(update_stmt, 'update_item_list'):
                    items = update_stmt.update_item_list
                    print(f"Number of update items: {len(items)}")
                    
                    for j, item in enumerate(items):
                        print(f"\n  Item {j}:")
                        print(f"    Type: {type(item).__name__}")
                        print(f"    Has target: {hasattr(item, 'target')}")
                        print(f"    Has set_value: {hasattr(item, 'set_value')}")
