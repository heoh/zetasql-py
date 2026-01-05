"""Debug MERGE clause attributes"""
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

if hasattr(stmt, 'when_clause_list'):
    clauses = stmt.when_clause_list
    if clauses:
        clause = clauses[0]
        print(f"Clause type: {type(clause).__name__}")
        print(f"\nAll attributes:")
        for attr in dir(clause):
            if not attr.startswith('_'):
                try:
                    value = getattr(clause, attr)
                    if not callable(value):
                        print(f"  {attr}: {type(value).__name__}")
                        if hasattr(value, '__len__') and not isinstance(value, str):
                            print(f"    length: {len(value)}")
                except:
                    pass
