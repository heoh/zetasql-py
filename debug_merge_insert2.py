"""Debug MERGE INSERT structure"""
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
    INSERT(id, name) VALUES (S.id, S.name)
"""

stmt = analyzer.analyze_statement(sql)

if hasattr(stmt, 'when_clause_list'):
    clauses = stmt.when_clause_list
    print(f"Number of when clauses: {len(clauses)}")
    
    for i, clause in enumerate(clauses):
        print(f"\n=== When clause {i} ===")
        print(f"Has insert_row: {hasattr(clause, 'insert_row')}")
        print(f"Has insert_column_list: {hasattr(clause, 'insert_column_list')}")
        
        if hasattr(clause, 'insert_row'):
            insert_row = clause.insert_row
            print(f"insert_row: {insert_row is not None}")
            
            if insert_row:
                print(f"insert_row type: {type(insert_row).__name__}")
                print(f"Has value_list: {hasattr(insert_row, 'value_list')}")
                
                if hasattr(insert_row, 'value_list'):
                    value_list = insert_row.value_list
                    print(f"value_list length: {len(value_list)}")
                    
                    for j, val in enumerate(value_list):
                        print(f"  Value {j}: {type(val).__name__}")
        
        if hasattr(clause, 'insert_column_list'):
            col_list = clause.insert_column_list
            print(f"insert_column_list length: {len(col_list)}")
            for j, col in enumerate(col_list):
                print(f"  Column {j}: {type(col).__name__} - {getattr(col, 'name', 'no name')}")
