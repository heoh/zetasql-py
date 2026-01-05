"""Debug MERGE INSERT"""
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
MERGE target T
USING source1 S
ON T.id = S.id
WHEN NOT MATCHED THEN
    INSERT (id, name) VALUES (S.id, S.name)
"""

stmt = analyzer.analyze_statement(sql)
print(f"Statement type: {type(stmt).__name__}")

lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
print(f"\nLineages found: {len(lineages)}")

for lineage in lineages:
    print(f"\nTarget: {lineage.target.table}.{lineage.target.name}")
    print(f"Parents: {len(lineage.parents)}")
    for parent in lineage.parents:
        print(f"  <- {parent.table}.{parent.name}")
