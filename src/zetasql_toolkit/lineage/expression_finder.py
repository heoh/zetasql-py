"""ExpressionParentFinder - 표현식 내 직접 컬럼 참조 찾기

Java 원본: com.google.zetasql.toolkit.tools.lineage.ExpressionParentFinder
"""

from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from zetasql.core.types.proto_models import ResolvedExpr, ResolvedColumn


class ExpressionParentFinder:
    """표현식 내에서 직접 참조되는 컬럼을 찾는 클래스.

    Java의 ExpressionParentFinder를 Python으로 이식한 구현입니다.
    singledispatch 대신 isinstance를 사용한 visitor 패턴입니다.
    """

    def __init__(self) -> None:
        """초기화."""
        self.result: List[ResolvedColumn] = []

    @staticmethod
    def find_direct_parents(expr: ResolvedExpr) -> List[ResolvedColumn]:
        """표현식에서 직접 참조하는 컬럼들을 찾음.

        Args:
            expr: 분석할 표현식

        Returns:
            직접 참조되는 ResolvedColumn 리스트
        """
        finder = ExpressionParentFinder()
        finder._visit_expr(expr)
        return finder.result

    def _visit_expr(self, expr: ResolvedExpr) -> None:
        """표현식을 방문하여 컬럼 참조 수집.

        Args:
            expr: 방문할 표현식
        """
        if expr is None:
            return

        type_name = type(expr).__name__

        # ResolvedColumnRef - 직접 컬럼 참조
        if type_name == "ResolvedColumnRef":
            self._visit_column_ref(expr)

        # ResolvedFunctionCall - 함수 호출
        elif type_name == "ResolvedFunctionCall":
            self._visit_function_call(expr)

        # ResolvedAggregateFunctionCall - 집계 함수
        elif type_name == "ResolvedAggregateFunctionCall":
            self._visit_aggregate_function(expr)

        # ResolvedAnalyticFunctionCall - 윈도우 함수
        elif type_name == "ResolvedAnalyticFunctionCall":
            self._visit_analytic_function(expr)

        # ResolvedCast - 타입 캐스팅
        elif type_name == "ResolvedCast":
            self._visit_cast(expr)

        # ResolvedMakeStruct - STRUCT 생성
        elif type_name == "ResolvedMakeStruct":
            self._visit_make_struct(expr)

        # ResolvedGetStructField - STRUCT 필드 접근
        elif type_name == "ResolvedGetStructField":
            self._visit_get_struct_field(expr)

        # ResolvedSubqueryExpr - 서브쿼리 표현식
        elif type_name == "ResolvedSubqueryExpr":
            self._visit_subquery_expr(expr)

        # ResolvedWithExpr - WITH 표현식
        elif type_name == "ResolvedWithExpr":
            self._visit_with_expr(expr)

        # 기타 표현식은 무시 (리터럴, 파라미터 등)

    def _visit_column_ref(self, expr) -> None:
        """컬럼 참조 방문."""
        if hasattr(expr, "column") and expr.column is not None:
            self.result.append(expr.column)

    def _visit_function_call(self, expr) -> None:
        """함수 호출 방문.

        특수 함수 처리:
        - CASE 문: 조건 제외, THEN/ELSE 값만
        - IF: 조건 제외, true/false 값만
        - NULLIF: 첫 번째 인자만
        """
        if not hasattr(expr, "function") or expr.function is None:
            return

        function_name = ""
        if hasattr(expr.function, "name"):
            function_name = expr.function.name
        elif hasattr(expr.function, "Name"):
            function_name = expr.function.Name()

        # 함수 이름에서 네임스페이스 제거 (ZetaSQL:nullif -> nullif)
        if ":" in function_name:
            function_name = function_name.split(":")[-1]

        argument_list = getattr(expr, "argument_list", []) or []

        # CASE 문 처리 (조건 제외)
        if function_name in ("$case_no_value", "$case_with_value"):
            self._visit_case_function(argument_list, function_name)
        # IF 함수 처리 (조건 제외)
        elif function_name == "if":
            self._visit_if_function(argument_list)
        # NULLIF 함수 처리 (첫 번째 인자만)
        elif function_name == "nullif":
            self._visit_nullif_function(argument_list)
        # 일반 함수: 모든 인자 순회
        else:
            for arg in argument_list:
                self._visit_expr(arg)

    def _visit_case_function(self, arguments: list, function_name: str) -> None:
        """CASE 함수 처리 - 조건 제외, 값만 포함.

        $case_no_value: CASE WHEN cond THEN val ... ELSE val END
        $case_with_value: CASE expr WHEN val THEN val ... ELSE val END
        """
        if not arguments:
            return

        # $case_with_value는 첫 인자가 비교 대상 표현식
        start_idx = 1 if function_name == "$case_with_value" else 0

        # WHEN-THEN 쌍과 ELSE 처리
        # 구조: [cond1, then1, cond2, then2, ..., else]
        # 조건(짝수 인덱스)은 제외, 값(홀수 인덱스)만 포함
        for i in range(start_idx, len(arguments)):
            # 마지막 하나가 남으면 ELSE
            remaining = len(arguments) - i
            if remaining == 1:
                # ELSE 값
                self._visit_expr(arguments[i])
            elif (i - start_idx) % 2 == 1:
                # THEN 값 (홀수 위치)
                self._visit_expr(arguments[i])

    def _visit_if_function(self, arguments: list) -> None:
        """IF 함수 처리 - 조건 제외, true/false 값만.

        IF(condition, true_value, false_value)
        """
        if len(arguments) >= 2:
            self._visit_expr(arguments[1])  # true_value
        if len(arguments) >= 3:
            self._visit_expr(arguments[2])  # false_value

    def _visit_nullif_function(self, arguments: list) -> None:
        """NULLIF 함수 처리 - 첫 번째 인자만.

        NULLIF(expr1, expr2) - expr1만 계보에 포함
        """
        if len(arguments) >= 1:
            self._visit_expr(arguments[0])

    def _visit_aggregate_function(self, expr) -> None:
        """집계 함수 방문."""
        argument_list = getattr(expr, "argument_list", []) or []
        for arg in argument_list:
            self._visit_expr(arg)

    def _visit_analytic_function(self, expr) -> None:
        """윈도우(분석) 함수 방문."""
        argument_list = getattr(expr, "argument_list", []) or []
        for arg in argument_list:
            self._visit_expr(arg)

    def _visit_cast(self, expr) -> None:
        """CAST 표현식 방문."""
        if hasattr(expr, "expr") and expr.expr is not None:
            self._visit_expr(expr.expr)

    def _visit_make_struct(self, expr) -> None:
        """MakeStruct 표현식 방문."""
        field_list = getattr(expr, "field_list", []) or []
        for field in field_list:
            self._visit_expr(field)

    def _visit_get_struct_field(self, expr) -> None:
        """GetStructField 표현식 방문.

        최적화: MakeStruct 직후 GetStructField면 해당 필드만 추적
        """
        if not hasattr(expr, "expr") or expr.expr is None:
            return

        inner_expr = expr.expr
        inner_type = type(inner_expr).__name__

        # MakeStruct에서 특정 필드만 가져오는 경우 최적화
        if inner_type == "ResolvedMakeStruct":
            field_idx = getattr(expr, "field_idx", None)
            field_list = getattr(inner_expr, "field_list", []) or []

            if field_idx is not None and 0 <= field_idx < len(field_list):
                self._visit_expr(field_list[field_idx])
                return

        # 그 외의 경우 내부 표현식 전체 방문
        self._visit_expr(inner_expr)

    def _visit_subquery_expr(self, expr) -> None:
        """서브쿼리 표현식 방문.

        SCALAR, ARRAY 서브쿼리만 처리 (EXISTS, IN은 조건이므로 제외)
        """
        subquery_type = getattr(expr, "subquery_type", None)

        # SCALAR, ARRAY 서브쿼리만 처리
        # Java: SubqueryType.SCALAR, SubqueryType.ARRAY
        if subquery_type in (1, 2):  # SCALAR=1, ARRAY=2 (proto enum 값)
            subquery = getattr(expr, "subquery", None)
            if subquery is not None:
                # 서브쿼리의 출력 컬럼을 부모로 추가
                output_column_list = getattr(subquery, "output_column_list", []) or []
                for output_col in output_column_list:
                    if hasattr(output_col, "column"):
                        self.result.append(output_col.column)

    def _visit_with_expr(self, expr) -> None:
        """WITH 표현식 방문."""
        if hasattr(expr, "expr") and expr.expr is not None:
            self._visit_expr(expr.expr)
