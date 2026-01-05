"""Column-Level Lineage Extraction Demo

Java ExtractColumnLevelLineage.java의 Python 포팅 버전입니다.
"""

from zetasql.api import Analyzer
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind, AnalyzerOptions

from zetasql_toolkit.lineage import ColumnLineageExtractor


def output_lineage(query: str, lineages):
    """리니지 출력 (Java 버전과 동일한 형식)"""
    print("\nQuery:")
    print(query)
    print("\nLineage:")
    
    for lineage in lineages:
        print(f"{lineage.target}")
        for parent in lineage.parents:
            print(f"\t\t<- {parent}")
    
    print()
    print()


def lineage_for_create_table_as_select(catalog):
    """CREATE TABLE AS SELECT 문의 리니지 추출"""
    
    query = """
CREATE TABLE target_table AS
SELECT
    title AS article_title,
    comment AS article_comment
FROM wikipedia
"""
    
    options = AnalyzerOptions()
    analyzer = Analyzer(options, catalog)
    stmt = analyzer.analyze_statement(query)
    
    lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
    
    print("=" * 70)
    print("Extracted column lineage from CREATE TABLE AS SELECT")
    output_lineage(query, lineages)


def lineage_for_ctas_with_subquery(catalog):
    """CREATE TABLE AS SELECT with 서브쿼리"""
    
    query = """
CREATE TABLE target_table AS
SELECT
    article_title
FROM (
    SELECT 
        title AS article_title
    FROM wikipedia
)
"""
    
    options = AnalyzerOptions()
    analyzer = Analyzer(options, catalog)
    stmt = analyzer.analyze_statement(query)
    
    lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
    
    print("=" * 70)
    print("Extracted column lineage from CTAS with Subquery")
    output_lineage(query, lineages)


def lineage_for_insert_statement(catalog):
    """INSERT 문의 리니지 추출"""
    
    query = """
INSERT INTO wikipedia(title, comment)
SELECT
    corpus AS title,
    word AS comment
FROM shakespeare
"""
    
    options = AnalyzerOptions()
    analyzer = Analyzer(options, catalog)
    stmt = analyzer.analyze_statement(query)
    
    lineages = ColumnLineageExtractor.extract_column_lineage(stmt)
    
    print("=" * 70)
    print("Extracted column lineage from INSERT")
    output_lineage(query, lineages)


def main():
    """메인 함수"""
    
    print()
    print("=" * 70)
    print(" ZetaSQL Toolkit for Python - Column Lineage Extraction Demo")
    print("=" * 70)
    print()
    
    # 카탈로그 구축
    wikipedia = (
        TableBuilder("wikipedia")
        .add_column("title", TypeKind.TYPE_STRING)
        .add_column("comment", TypeKind.TYPE_STRING)
        .add_column("views", TypeKind.TYPE_INT64)
        .build()
    )
    
    shakespeare = (
        TableBuilder("shakespeare")
        .add_column("corpus", TypeKind.TYPE_STRING)
        .add_column("word", TypeKind.TYPE_STRING)
        .add_column("word_count", TypeKind.TYPE_INT64)
        .build()
    )
    
    catalog = (
        CatalogBuilder("demo_catalog")
        .add_table(wikipedia)
        .add_table(shakespeare)
        .build()
    )
    
    # 테스트 실행
    lineage_for_create_table_as_select(catalog)
    lineage_for_ctas_with_subquery(catalog)
    
    try:
        lineage_for_insert_statement(catalog)
    except Exception as e:
        print("=" * 70)
        print(f"INSERT lineage extraction: Not yet fully implemented")
        print(f"Error: {e}")
        print()
    
    print("=" * 70)
    print(" Demo completed!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
