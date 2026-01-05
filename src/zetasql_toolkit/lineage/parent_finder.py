"""ParentColumnFinder - 컬럼의 terminal 부모 추적

Java 원본: com.google.zetasql.toolkit.tools.lineage.ParentColumnFinder
"""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Set, Optional, TYPE_CHECKING

from zetasql_toolkit.lineage.ast_walker import walk_resolved_tree
from zetasql_toolkit.lineage.expression_finder import ExpressionParentFinder

if TYPE_CHECKING:
    from zetasql.core.types.proto_models import (
        ResolvedStatement,
        ResolvedColumn,
        ResolvedExpr,
    )


def _column_key(column) -> str:
    """컬럼의 고유 키 생성 (column_id 기반)."""
    if column is None:
        return ""
    column_id = getattr(column, "column_id", None)
    if column_id is not None:
        return str(column_id)
    # column_id가 없으면 이름 기반
    table = getattr(column, "table_name", "") or ""
    name = getattr(column, "name", "") or ""
    return f"{table}.{name}"


class ParentColumnFinder:
    """컬럼의 terminal(최종 소스) 부모를 찾는 클래스.

    Java의 ParentColumnFinder를 Python으로 이식한 구현입니다.

    알고리즘 (2-pass):
    1. Pass 1: AST 순회하며 컬럼 → 직접 부모 매핑 구축
    2. Pass 2: BFS로 목표 컬럼부터 terminal 컬럼까지 추적
    """

    def __init__(self) -> None:
        """초기화."""
        # 컬럼 → 직접 부모들 매핑
        self.columns_to_parents: Dict[str, List] = {}

        # Terminal 컬럼들 (테이블/TVF에서 직접 읽은 컬럼)
        self.terminal_columns: Set[str] = set()

        # WITH 절 스코프 스택
        self.with_entry_scopes: List[List] = []

        # 현재 계산 중인 컬럼 스택
        self.columns_being_computed: List = []

    @staticmethod
    def find_parents_for_column(
        statement: ResolvedStatement,
        column: ResolvedColumn,
    ) -> List[ResolvedColumn]:
        """컬럼의 terminal 부모들을 찾음.

        Args:
            statement: 분석할 statement
            column: 부모를 찾을 컬럼

        Returns:
            terminal 부모 컬럼 리스트
        """
        finder = ParentColumnFinder()

        # Pass 1: AST 순회하며 맵 구축
        walk_resolved_tree(statement, finder._process_node)

        # Pass 2: BFS로 terminal 부모 찾기
        return finder._resolve_terminal_parents(column)

    @staticmethod
    def find_parents_for_expression(
        statement: ResolvedStatement,
        expr: ResolvedExpr,
    ) -> List[ResolvedColumn]:
        """표현식의 terminal 부모들을 찾음.

        Args:
            statement: 분석할 statement
            expr: 부모를 찾을 표현식

        Returns:
            terminal 부모 컬럼 리스트
        """
        finder = ParentColumnFinder()

        # Pass 1: AST 순회하며 맵 구축
        walk_resolved_tree(statement, finder._process_node)

        # 표현식에서 직접 부모 찾기
        direct_parents = ExpressionParentFinder.find_direct_parents(expr)

        # 각 직접 부모의 terminal 부모 찾기
        all_terminals: List = []
        seen: Set[str] = set()

        for parent in direct_parents:
            terminals = finder._resolve_terminal_parents(parent)
            for t in terminals:
                key = _column_key(t)
                if key not in seen:
                    seen.add(key)
                    all_terminals.append(t)

        return all_terminals

    def _process_node(self, node) -> None:
        """노드 방문 처리."""
        if node is None:
            return

        type_name = type(node).__name__

        # ResolvedComputedColumn - 계산된 컬럼
        if type_name == "ResolvedComputedColumn":
            self._visit_computed_column(node)

        # ResolvedTableScan - 테이블 스캔 (terminal)
        elif type_name == "ResolvedTableScan":
            self._visit_table_scan(node)

        # ResolvedTVFScan - TVF 스캔 (terminal)
        elif type_name == "ResolvedTVFScan":
            self._visit_tvf_scan(node)

        # ResolvedWithScan - WITH 절
        elif type_name == "ResolvedWithScan":
            self._visit_with_scan(node)

        # ResolvedWithRefScan - WITH 참조
        elif type_name == "ResolvedWithRefScan":
            self._visit_with_ref_scan(node)

        # ResolvedSetOperationScan - UNION 등
        elif type_name == "ResolvedSetOperationScan":
            self._visit_set_operation_scan(node)

        # ResolvedArrayScan - UNNEST
        elif type_name == "ResolvedArrayScan":
            self._visit_array_scan(node)

        # ResolvedProjectScan - 프로젝션
        elif type_name == "ResolvedProjectScan":
            self._visit_project_scan(node)

        # ResolvedFilterScan - 필터
        elif type_name == "ResolvedFilterScan":
            self._visit_filter_scan(node)

        # ResolvedAggregateScan - 집계
        elif type_name == "ResolvedAggregateScan":
            self._visit_aggregate_scan(node)

    def _visit_computed_column(self, node) -> None:
        """계산된 컬럼 처리."""
        column = getattr(node, "column", None)
        expr = getattr(node, "expr", None)

        if column is None:
            return

        # MakeStruct 특수 처리
        if expr is not None and type(expr).__name__ == "ResolvedMakeStruct":
            self._expand_make_struct(column, expr)
        else:
            # 표현식에서 직접 부모 찾기
            expr_parents = ExpressionParentFinder.find_direct_parents(expr) if expr else []
            self._add_parents_to_column(column, expr_parents)

    def _expand_make_struct(self, column, make_struct_expr) -> None:
        """MakeStruct 확장 - STRUCT 필드별 매핑."""
        field_list = getattr(make_struct_expr, "field_list", []) or []
        struct_type = getattr(column, "type", None)

        if struct_type is None:
            # 타입 정보 없으면 전체 필드 순회
            all_parents = []
            for field in field_list:
                parents = ExpressionParentFinder.find_direct_parents(field)
                all_parents.extend(parents)
            self._add_parents_to_column(column, all_parents)
            return

        # STRUCT 타입이면 필드별 매핑
        # TODO: STRUCT 필드별 세부 매핑 구현
        all_parents = []
        for field in field_list:
            parents = ExpressionParentFinder.find_direct_parents(field)
            all_parents.extend(parents)
        self._add_parents_to_column(column, all_parents)

    def _visit_table_scan(self, node) -> None:
        """테이블 스캔 처리 - terminal 컬럼 등록."""
        column_list = getattr(node, "column_list", []) or []
        for col in column_list:
            key = _column_key(col)
            self.terminal_columns.add(key)

    def _visit_tvf_scan(self, node) -> None:
        """TVF 스캔 처리 - terminal 컬럼 등록."""
        column_list = getattr(node, "column_list", []) or []
        for col in column_list:
            key = _column_key(col)
            self.terminal_columns.add(key)

    def _visit_with_scan(self, node) -> None:
        """WITH 절 처리."""
        with_entry_list = getattr(node, "with_entry_list", []) or []
        self.with_entry_scopes.append(with_entry_list)

    def _visit_with_ref_scan(self, node) -> None:
        """WITH 참조 처리 - WITH entry 컬럼과 매핑."""
        if not self.with_entry_scopes:
            return

        with_query_name = getattr(node, "with_query_name", None)
        column_list = getattr(node, "column_list", []) or []

        # 현재 스코프에서 해당 WITH entry 찾기
        for scope in reversed(self.with_entry_scopes):
            for entry in scope:
                entry_name = getattr(entry, "with_query_name", None)
                if entry_name == with_query_name:
                    # WITH entry의 서브쿼리 찾기
                    with_subquery = getattr(entry, "with_subquery", None)
                    if with_subquery is None:
                        return
                    
                    # 서브쿼리의 출력 컬럼 찾기
                    # ResolvedProjectScan은 column_list 사용
                    # ResolvedQuery는 output_column_list 사용
                    output_columns = []
                    
                    if hasattr(with_subquery, "column_list"):
                        # ResolvedProjectScan 타입의 경우
                        output_columns = getattr(with_subquery, "column_list", []) or []
                    elif hasattr(with_subquery, "output_column_list"):
                        # ResolvedQuery 타입의 경우
                        output_cols = getattr(with_subquery, "output_column_list", []) or []
                        for out in output_cols:
                            if hasattr(out, "column"):
                                output_columns.append(out.column)
                    
                    # WITH REF 컬럼과 서브쿼리 출력 컬럼 매핑
                    for i, col in enumerate(column_list):
                        if i < len(output_columns):
                            self._add_parents_to_column(col, [output_columns[i]])
                    return

    def _visit_set_operation_scan(self, node) -> None:
        """UNION/INTERSECT/EXCEPT 처리."""
        column_list = getattr(node, "column_list", []) or []
        input_item_list = getattr(node, "input_item_list", []) or []

        # 각 입력 scan의 출력 컬럼과 매핑
        for input_item in input_item_list:
            output_column_list = getattr(input_item, "output_column_list", []) or []
            for i, col in enumerate(column_list):
                if i < len(output_column_list):
                    self._add_parents_to_column(col, [output_column_list[i]])

    def _visit_array_scan(self, node) -> None:
        """UNNEST 처리."""
        # element_column을 array_expr의 컬럼과 매핑
        element_column = getattr(node, "element_column", None)
        array_expr = getattr(node, "array_expr", None)

        if element_column is not None and array_expr is not None:
            parents = ExpressionParentFinder.find_direct_parents(array_expr)
            self._add_parents_to_column(element_column, parents)

    def _visit_project_scan(self, node) -> None:
        """프로젝션 스캔 처리."""
        expr_list = getattr(node, "expr_list", []) or []
        for expr in expr_list:
            if type(expr).__name__ == "ResolvedComputedColumn":
                self._visit_computed_column(expr)

    def _visit_filter_scan(self, node) -> None:
        """필터 스캔 처리."""
        # 필터 조건은 계보에 영향 없음
        pass

    def _visit_aggregate_scan(self, node) -> None:
        """집계 스캔 처리."""
        # 그룹핑 컬럼 처리
        group_by_list = getattr(node, "group_by_list", []) or []
        for item in group_by_list:
            if type(item).__name__ == "ResolvedComputedColumn":
                self._visit_computed_column(item)

        # 집계 컬럼 처리
        aggregate_list = getattr(node, "aggregate_list", []) or []
        for item in aggregate_list:
            if type(item).__name__ == "ResolvedComputedColumn":
                self._visit_computed_column(item)

    def _add_parents_to_column(self, column, parents: List) -> None:
        """컬럼에 부모 추가."""
        if column is None:
            return

        key = _column_key(column)
        if key not in self.columns_to_parents:
            self.columns_to_parents[key] = []

        for parent in parents:
            if parent is not None:
                self.columns_to_parents[key].append(parent)

    def _resolve_terminal_parents(self, column) -> List:
        """BFS로 terminal 부모 찾기."""
        if column is None:
            return []

        result: List = []
        seen: Set[str] = set()
        queue = deque([column])

        while queue:
            current = queue.popleft()
            key = _column_key(current)

            if key in seen:
                continue
            seen.add(key)

            # Terminal 컬럼이면 결과에 추가
            if key in self.terminal_columns:
                result.append(current)
                continue

            # 부모가 있으면 큐에 추가
            parents = self.columns_to_parents.get(key, [])
            if parents:
                for parent in parents:
                    parent_key = _column_key(parent)
                    if parent_key not in seen:
                        queue.append(parent)
            else:
                # 부모가 없는데 terminal도 아니면 그냥 결과에 추가
                # (외부 참조 등)
                result.append(current)

        return result
