"""ColumnLineageExtractor - 컬럼 레벨 계보 추출기

Java 원본: com.google.zetasql.toolkit.tools.lineage.ColumnLineageExtractor
"""

from __future__ import annotations

from typing import Set, Optional, Union, List, TYPE_CHECKING

from zetasql_toolkit.lineage.models import ColumnEntity, ColumnLineage
from zetasql_toolkit.lineage.parent_finder import ParentColumnFinder

if TYPE_CHECKING:
    from zetasql.core.types.proto_models import (
        ResolvedStatement,
        ResolvedCreateTableAsSelectStmt,
        ResolvedCreateViewStmt,
        ResolvedQueryStmt,
        ResolvedInsertStmt,
        ResolvedUpdateStmt,
        ResolvedMergeStmt,
        ResolvedColumn,
        ResolvedOutputColumn,
    )


class ColumnLineageExtractor:
    """다양한 SQL 문장에서 컬럼 레벨 계보를 추출하는 클래스.

    Java의 ColumnLineageExtractor를 Python으로 이식한 구현입니다.

    지원 문장 타입:
    - CREATE TABLE AS SELECT (CTAS)
    - CREATE VIEW / CREATE MATERIALIZED VIEW
    - SELECT (QueryStmt) - target_table 지정 필요
    - INSERT
    - UPDATE
    - MERGE
    """

    @staticmethod
    def extract_column_lineage(
        stmt: ResolvedStatement,
        target_table: Optional[str] = None,
    ) -> Set[ColumnLineage]:
        """문장에서 컬럼 계보를 추출.

        Args:
            stmt: 분석할 resolved statement
            target_table: QueryStmt인 경우 대상 테이블 이름

        Returns:
            컬럼 계보 집합

        Raises:
            TypeError: 지원하지 않는 statement 타입
            ValueError: QueryStmt에서 target_table 누락
        """
        type_name = type(stmt).__name__

        if type_name == "ResolvedCreateTableAsSelectStmt":
            return ColumnLineageExtractor._extract_ctas(stmt)

        elif type_name in ("ResolvedCreateViewStmt", "ResolvedCreateMaterializedViewStmt"):
            return ColumnLineageExtractor._extract_view(stmt)

        elif type_name == "ResolvedQueryStmt":
            if not target_table:
                raise ValueError("target_table is required for QueryStmt")
            return ColumnLineageExtractor._extract_query(stmt, target_table)

        elif type_name == "ResolvedInsertStmt":
            return ColumnLineageExtractor._extract_insert(stmt)

        elif type_name == "ResolvedUpdateStmt":
            return ColumnLineageExtractor._extract_update(stmt)

        elif type_name == "ResolvedMergeStmt":
            return ColumnLineageExtractor._extract_merge(stmt)

        else:
            raise TypeError(f"Unsupported statement type: {type_name}")

    @staticmethod
    def _extract_ctas(stmt) -> Set[ColumnLineage]:
        """CREATE TABLE AS SELECT 계보 추출."""
        name_path = getattr(stmt, "name_path", []) or []
        target_table = ".".join(name_path) if name_path else "unknown"

        output_column_list = getattr(stmt, "output_column_list", []) or []

        return ColumnLineageExtractor._extract_for_output_columns(
            target_table, output_column_list, stmt
        )

    @staticmethod
    def _extract_view(stmt) -> Set[ColumnLineage]:
        """CREATE VIEW 계보 추출."""
        name_path = getattr(stmt, "name_path", []) or []
        target_table = ".".join(name_path) if name_path else "unknown"

        output_column_list = getattr(stmt, "output_column_list", []) or []

        return ColumnLineageExtractor._extract_for_output_columns(
            target_table, output_column_list, stmt
        )

    @staticmethod
    def _extract_query(stmt, target_table: str) -> Set[ColumnLineage]:
        """SELECT 문 계보 추출."""
        output_column_list = getattr(stmt, "output_column_list", []) or []

        return ColumnLineageExtractor._extract_for_output_columns(
            target_table, output_column_list, stmt
        )

    @staticmethod
    def _extract_insert(stmt) -> Set[ColumnLineage]:
        """INSERT 문 계보 추출."""
        result: Set[ColumnLineage] = set()

        # INSERT 대상 테이블
        table_scan = getattr(stmt, "table_scan", None)
        if table_scan is None:
            return result

        table = getattr(table_scan, "table", None)
        target_table = ""
        if table is not None:
            target_table = getattr(table, "full_name", "") or getattr(table, "name", "") or ""

        # query가 없으면 (VALUES만 있는 경우) 빈 결과
        query = getattr(stmt, "query", None)
        if query is None:
            return result

        # insert_column_list와 query.output_column_list 매핑
        insert_column_list = getattr(stmt, "insert_column_list", []) or []
        query_output_list = getattr(query, "output_column_list", []) or []

        for i, insert_col in enumerate(insert_column_list):
            if i >= len(query_output_list):
                break

            query_output = query_output_list[i]
            query_column = getattr(query_output, "column", None)

            if query_column is None:
                continue

            # insert_col의 이름 가져오기
            col_name = getattr(insert_col, "name", None)
            if col_name is None and hasattr(insert_col, "column"):
                col_name = getattr(insert_col.column, "name", None)
            if col_name is None:
                col_name = f"column_{i}"

            # 부모 찾기
            parents = ParentColumnFinder.find_parents_for_column(stmt, query_column)

            # 계보 생성
            lineage = ColumnLineage(
                target=ColumnEntity(table=target_table, name=col_name),
                parents=frozenset(
                    ColumnEntity.from_resolved_column(p) for p in parents
                ),
            )
            result.add(lineage)

        return result

    @staticmethod
    def _extract_update(stmt) -> Set[ColumnLineage]:
        """UPDATE 문 계보 추출."""
        result: Set[ColumnLineage] = set()

        # UPDATE 대상 테이블
        table_scan = getattr(stmt, "table_scan", None)
        if table_scan is None:
            return result

        table = getattr(table_scan, "table", None)
        target_table = ""
        if table is not None:
            target_table = getattr(table, "full_name", "") or getattr(table, "name", "") or ""

        # update_item_list 처리
        update_item_list = getattr(stmt, "update_item_list", []) or []

        for item in update_item_list:
            # target 컬럼
            target = getattr(item, "target", None)
            if target is None:
                continue

            target_column = getattr(target, "column", None)
            if target_column is None:
                continue

            col_name = getattr(target_column, "name", "") or ""

            # set_value 표현식
            set_value = getattr(item, "set_value", None)
            if set_value is None:
                continue

            value_expr = getattr(set_value, "value", None)
            if value_expr is None:
                continue

            # 부모 찾기
            parents = ParentColumnFinder.find_parents_for_expression(stmt, value_expr)

            # 계보 생성
            lineage = ColumnLineage(
                target=ColumnEntity(table=target_table, name=col_name),
                parents=frozenset(
                    ColumnEntity.from_resolved_column(p) for p in parents
                ),
            )
            result.add(lineage)

        return result

    @staticmethod
    def _extract_merge(stmt) -> Set[ColumnLineage]:
        """MERGE 문 계보 추출."""
        result: Set[ColumnLineage] = set()

        # MERGE 대상 테이블
        table_scan = getattr(stmt, "table_scan", None)
        if table_scan is None:
            return result

        table = getattr(table_scan, "table", None)
        target_table = ""
        if table is not None:
            target_table = getattr(table, "full_name", "") or getattr(table, "name", "") or ""

        # when_clause_list 처리
        when_clause_list = getattr(stmt, "when_clause_list", []) or []

        for when_clause in when_clause_list:
            # INSERT 액션
            insert_stmt = getattr(when_clause, "insert_stmt", None)
            if insert_stmt is not None:
                insert_lineages = ColumnLineageExtractor._extract_merge_insert(
                    stmt, insert_stmt, target_table
                )
                result.update(insert_lineages)

            # UPDATE 액션
            update_stmt = getattr(when_clause, "update_stmt", None)
            if update_stmt is not None:
                update_lineages = ColumnLineageExtractor._extract_merge_update(
                    stmt, update_stmt, target_table
                )
                result.update(update_lineages)

        return result

    @staticmethod
    def _extract_merge_insert(
        merge_stmt, insert_stmt, target_table: str
    ) -> Set[ColumnLineage]:
        """MERGE의 INSERT 절 계보 추출."""
        result: Set[ColumnLineage] = set()

        insert_column_list = getattr(insert_stmt, "insert_column_list", []) or []
        row_list = getattr(insert_stmt, "row_list", []) or []

        # 첫 번째 row의 값들과 컬럼 매핑
        if not row_list:
            return result

        first_row = row_list[0]
        value_list = getattr(first_row, "value_list", []) or []

        for i, insert_col in enumerate(insert_column_list):
            if i >= len(value_list):
                break

            # 컬럼 이름
            col_name = getattr(insert_col, "name", None)
            if col_name is None and hasattr(insert_col, "column"):
                col_name = getattr(insert_col.column, "name", None)
            if col_name is None:
                col_name = f"column_{i}"

            # 값 표현식
            value_expr = value_list[i]

            # 부모 찾기
            parents = ParentColumnFinder.find_parents_for_expression(
                merge_stmt, value_expr
            )

            # 계보 생성
            lineage = ColumnLineage(
                target=ColumnEntity(table=target_table, name=col_name),
                parents=frozenset(
                    ColumnEntity.from_resolved_column(p) for p in parents
                ),
            )
            result.add(lineage)

        return result

    @staticmethod
    def _extract_merge_update(
        merge_stmt, update_stmt, target_table: str
    ) -> Set[ColumnLineage]:
        """MERGE의 UPDATE 절 계보 추출."""
        result: Set[ColumnLineage] = set()

        update_item_list = getattr(update_stmt, "update_item_list", []) or []

        for item in update_item_list:
            # target 컬럼
            target = getattr(item, "target", None)
            if target is None:
                continue

            target_column = getattr(target, "column", None)
            if target_column is None:
                continue

            col_name = getattr(target_column, "name", "") or ""

            # set_value 표현식
            set_value = getattr(item, "set_value", None)
            if set_value is None:
                continue

            value_expr = getattr(set_value, "value", None)
            if value_expr is None:
                continue

            # 부모 찾기
            parents = ParentColumnFinder.find_parents_for_expression(
                merge_stmt, value_expr
            )

            # 계보 생성
            lineage = ColumnLineage(
                target=ColumnEntity(table=target_table, name=col_name),
                parents=frozenset(
                    ColumnEntity.from_resolved_column(p) for p in parents
                ),
            )
            result.add(lineage)

        return result

    @staticmethod
    def _extract_for_output_columns(
        target_table: str,
        output_columns: List,
        statement,
    ) -> Set[ColumnLineage]:
        """출력 컬럼들에 대한 계보 추출.

        Args:
            target_table: 대상 테이블 이름
            output_columns: ResolvedOutputColumn 리스트
            statement: 분석할 statement

        Returns:
            컬럼 계보 집합
        """
        result: Set[ColumnLineage] = set()

        for output_col in output_columns:
            # output_col은 ResolvedOutputColumn (name, column 필드)
            col_name = getattr(output_col, "name", None)
            column = getattr(output_col, "column", None)

            if column is None:
                continue

            if col_name is None:
                col_name = getattr(column, "name", None) or "unknown"

            # STRUCT 컬럼 확장
            expanded_cols = ColumnLineageExtractor._expand_column(column)

            for exp_col in expanded_cols:
                # exp_col이 원본과 같으면 원래 이름 사용
                if exp_col is column:
                    final_name = col_name
                else:
                    # STRUCT 필드인 경우 필드 이름 사용
                    final_name = getattr(exp_col, "name", col_name)

                # 부모 찾기
                parents = ParentColumnFinder.find_parents_for_column(statement, exp_col)

                # 계보 생성
                lineage = ColumnLineage(
                    target=ColumnEntity(table=target_table, name=final_name),
                    parents=frozenset(
                        ColumnEntity.from_resolved_column(p) for p in parents
                    ),
                )
                result.add(lineage)

        return result

    @staticmethod
    def _expand_column(column) -> List:
        """STRUCT 컬럼을 필드별로 확장.

        Args:
            column: 확장할 ResolvedColumn

        Returns:
            확장된 컬럼 리스트 (비-STRUCT면 원본만 포함)
        """
        result = [column]

        col_type = getattr(column, "type", None)
        if col_type is None:
            return result

        # STRUCT 타입 체크
        type_kind = getattr(col_type, "type_kind", None)
        # TYPE_STRUCT = 6 (proto enum)
        if type_kind != 6:
            return result

        # STRUCT 필드 확장은 복잡하므로 현재는 원본만 반환
        # TODO: STRUCT 필드별 세부 확장 구현
        return result
