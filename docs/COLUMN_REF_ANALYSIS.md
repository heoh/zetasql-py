# Column Lineage - ResolvedColumn vs ResolvedColumnRef 분석 보고서

## 핵심 발견사항

### 1. ZetaSQL AST 구조의 중요한 차이점

**ResolvedColumn**과 **ResolvedColumnRef**는 서로 다른 목적으로 사용됩니다:

#### ResolvedColumn
- **용도**: 컬럼 정의/참조를 나타내는 메타데이터 객체
- **위치**: 모든 컬럼 관련 노드에 존재
- **생성 시점**: 
  - `SELECT id, name FROM users` (단순 프로젝션)
  - `ResolvedComputedColumn`의 정의
  - `ResolvedTableScan`의 column_list

#### ResolvedColumnRef
- **용도**: 표현식 내에서 컬럼을 **실제로 참조**할 때만 생성
- **위치**: 표현식(ResolvedExpr) 트리 내부
- **생성 시점**:
  - `SELECT id * 2 FROM users` (계산식)
  - `SELECT id FROM users WHERE id > 10` (WHERE 조건)
  - `SELECT UPPER(name) FROM users` (함수 인자)

### 2. 테스트 케이스 수정 내역

#### test_level2_ast_walker.py
**추가된 테스트**:
```python
def test_discover_simple_columns(self, analyzer):
    """단순 SELECT에서 컬럼 발견 (ResolvedColumn)"""
    stmt = analyzer.analyze_statement("SELECT id, name FROM users")
    
    columns = []
    def visitor(node):
        if type(node).__name__ == "ResolvedColumn":
            columns.append(node)
    
    walk_resolved_tree(stmt, visitor)
    
    # id, name 컬럼이 발견되어야 함
    assert len(columns) >= 2
    column_names = {col.name for col in columns}
    assert "id" in column_names
    assert "name" in column_names
```

**수정된 테스트**:
```python
def test_discover_column_refs(self, analyzer):
    """컬럼 참조 발견 (표현식 내부에서만 생성됨)"""
    # 변경 전: "SELECT id, name FROM users"  # ColumnRef 없음!
    # 변경 후:
    stmt = analyzer.analyze_statement("SELECT id * 2, name FROM users WHERE id > 10")
    
    column_refs = []
    def visitor(node):
        if "ColumnRef" in type(node).__name__:
            column_refs.append(node)
    
    walk_resolved_tree(stmt, visitor)
    
    # id * 2와 WHERE id > 10에서 두 번 참조
    assert len(column_refs) >= 2
```

#### test_level3_expression.py
**수정 사항**:
1. **Fixture 수정**: `AnalyzerOptions` 추가
2. **Builtin functions 추가**: UPPER, CONCAT 등 사용을 위해
3. **테스트 쿼리 수정**:
   ```python
   # 변경 전
   expr = get_first_computed_expr(analyzer, "SELECT name AS alias FROM users")
   # 문제: name AS alias는 ComputedColumn을 생성하지 않음
   
   # 변경 후  
   expr = get_first_computed_expr(analyzer, "SELECT CONCAT(name, '') AS alias FROM users")
   # 해결: CONCAT 함수로 ComputedColumn 생성
   ```

### 3. expression_finder.py의 핵심 수정

#### 함수 이름 네임스페이스 처리
```python
# 문제: ZetaSQL은 함수 이름에 네임스페이스 추가
# "nullif" → "ZetaSQL:nullif"
# "if" → "ZetaSQL:if"
# "$case_no_value" → "ZetaSQL:$case_no_value"

# 해결책
function_name = ""
if hasattr(expr.function, "name"):
    function_name = expr.function.name
elif hasattr(expr.function, "Name"):
    function_name = expr.function.Name()

# 함수 이름에서 네임스페이스 제거
if ":" in function_name:
    function_name = function_name.split(":")[-1]
```

이 수정으로 NULLIF, IF, CASE 특수 처리가 올바르게 작동합니다.

### 4. 디자인에 미치는 영향

#### ✅ 영향 없음
현재 디자인은 ResolvedColumn과 ResolvedColumnRef의 차이를 **이미 올바르게** 고려하고 있습니다:

1. **Level 2 (ast_walker.py)**: 
   - 모든 ResolvedNode를 순회하므로 두 타입 모두 처리
   - 문제 없음 ✓

2. **Level 3 (expression_finder.py)**:
   - `ResolvedColumnRef`**만** 찾도록 설계됨
   - 이것이 **올바른** 동작 (표현식 내 참조만 필요)
   - Java 원본과 동일한 로직 ✓

3. **Level 4 (parent_finder.py)**:
   - `ResolvedComputedColumn`의 `expr` 속성을 Level 3에 전달
   - expr 내부의 ResolvedColumnRef를 찾음
   - 문제 없음 ✓

4. **Level 5 (extractor.py)**:
   - Level 4의 결과를 사용하여 최종 lineage 생성
   - 문제 없음 ✓

#### ⚠️ 주의사항
테스트 작성 시:
- 단순 `SELECT col FROM table`은 **ResolvedColumnRef를 생성하지 않음**
- 표현식 테스트 시 반드시 **함수나 연산자** 포함 필요
- 예: `UPPER(col)`, `col * 2`, `CONCAT(col, '')`

### 5. 테스트 결과 요약

#### 전체 결과
```
Level 1 (models):          19 passed ✓
Level 2 (ast_walker):      17 passed ✓  (1개 추가)
Level 3 (expression):      13 passed ✓  (fixture + 함수이름 수정)
Level 4 (parent):          22 passed, 1 failed
Level 5 (extractor):       23 passed, 7 failed

전체: 75 passed, 8 failed (90% 성공률)
```

#### 실패한 테스트 (8개)
1. `test_cte_with_expression` (Level 4): CTE alias 처리 문제
2. `test_simple_insert` (Level 5): INSERT 구현 미완성
3. `test_insert_with_expression` (Level 5): INSERT 구현 미완성
4. `test_insert_with_subquery` (Level 5): INSERT 구현 미완성
5. `test_merge_update_only` (Level 5): MERGE 구현 미완성
6. `test_merge_insert_only` (Level 5): MERGE 구현 미완성
7. `test_merge_update_and_insert` (Level 5): MERGE 구현 미완성
8. `test_multi_level_cte` (Level 5): 다중 CTE 처리 문제

**중요**: 이 실패들은 ResolvedColumn/ResolvedColumnRef 구분과 **무관**하며, Level 4-5의 **구현 누락** 때문입니다.

### 6. 결론

#### ✅ 검증 완료
- ResolvedColumn vs ResolvedColumnRef 차이를 정확히 이해
- 기존 디자인이 이미 올바르게 설계됨
- Level 2 AST walker는 완벽하게 작동
- Level 3 expression finder의 함수 이름 처리 버그 수정
- 모든 fixture에 AnalyzerOptions 및 builtin functions 추가

#### 📝 권장사항
1. **테스트 문서화**: ResolvedColumn vs ResolvedColumnRef 차이를 README에 명시
2. **Level 4-5 구현 완료**: INSERT, MERGE, CTE 처리 구현
3. **함수 이름 처리**: 네임스페이스 제거 로직이 모든 특수 함수에 적용됨을 확인

#### 🎯 핵심 교훈
> **단순 SELECT는 ResolvedColumnRef를 생성하지 않습니다.**
> 
> 표현식 테스트 시 항상 함수나 연산자를 포함시켜야 합니다.

---

## 수정된 파일 목록

### 소스 코드
1. `src/zetasql_toolkit/lineage/expression_finder.py`
   - 함수 이름 네임스페이스 처리 추가

### 테스트 코드
1. `tests/zetasql_toolkit/lineage/test_level2_ast_walker.py`
   - `test_discover_simple_columns` 추가
   - `test_discover_column_refs` 수정

2. `tests/zetasql_toolkit/lineage/test_level3_expression.py`
   - Analyzer fixture에 AnalyzerOptions 추가
   - simple_catalog에 builtin_functions 추가
   - `test_single_column_ref` 쿼리 수정

3. `tests/zetasql_toolkit/lineage/test_level4_parent.py`
   - Analyzer fixture에 AnalyzerOptions 추가
   - simple_catalog에 builtin_functions 추가

4. `tests/zetasql_toolkit/lineage/test_level5_extractor.py`
   - analyzer, analyzer_bq fixture에 AnalyzerOptions 추가
   - bigquery_like_catalog, simple_catalog에 builtin_functions 추가

---

**작성일**: 2026-01-05
**상태**: 검증 완료 ✓
