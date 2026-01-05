# ZetaSQL Toolkit for Python - Column-Level Lineage Extraction

## 1. 개요

이 프로젝트는 Google ZetaSQL Java Toolkit의 Column-Level Lineage 추출 기능을 Python으로 포팅합니다.

**원본 Java 코드**: `.external/zetasql-toolkit/zetasql-toolkit-core/src/main/java/com/google/zetasql/toolkit/tools/lineage/`

### 1.1 지원 기능

- **CREATE TABLE AS SELECT** (CTAS) 문의 컬럼 계보 추출
- **CREATE VIEW** 문의 컬럼 계보 추출
- **INSERT** 문의 컬럼 계보 추출
- **UPDATE** 문의 컬럼 계보 추출
- **MERGE** 문의 컬럼 계보 추출
- **중첩 표현식 처리** (UPPER, CONCAT, CASE 등)
- **STRUCT 필드 확장**
- **WITH 절 (CTE) 처리**
- **서브쿼리 처리**

### 1.2 Java vs Python 차이점

| 항목 | Java | Python |
|-----|------|--------|
| Visitor 패턴 | `accept()` / `visit()` | `functools.singledispatch` |
| 트리 순회 | 자동 (Visitor) | 수동 (리플렉션) |
| 타입 체크 | 컴파일 타임 | 런타임 `isinstance()` |

---

## 2. 아키텍처

```
src/zetasql_toolkit/
├── __init__.py
├── DESIGN.md                    # 이 문서
└── lineage/
    ├── __init__.py
    ├── models.py                # Level 1: 데이터 모델
    ├── ast_walker.py            # Level 2: AST 순회 유틸리티
    ├── expression_finder.py     # Level 3: 표현식 부모 찾기
    ├── parent_finder.py         # Level 4: 컬럼 부모 추적
    └── extractor.py             # Level 5: 계보 추출기
```

---

## 3. 구현 레벨

### Level 1: 데이터 모델 (`models.py`)

**목표**: 계보 정보를 표현하는 기본 데이터 구조

```python
@dataclass
class ColumnEntity:
    """테이블.컬럼 참조를 나타내는 엔티티"""
    table: str
    name: str

@dataclass  
class ColumnLineage:
    """컬럼 간 계보 관계"""
    target: ColumnEntity
    parents: Set[ColumnEntity]
```

**테스트 기준**:
- [ ] ColumnEntity 생성 및 동등성 비교
- [ ] ColumnEntity.from_resolved_column() 팩토리 메서드
- [ ] ColumnLineage 생성 및 해시 가능성

---

### Level 2: AST Walker (`ast_walker.py`)

**목표**: ResolvedAST를 재귀적으로 순회하는 유틸리티

Java의 `Visitor.accept()` 패턴을 대체합니다.

```python
def walk_resolved_tree(node: ResolvedNode, visitor_fn: Callable):
    """ResolvedAST를 DFS로 순회"""
    visitor_fn(node)
    for child in get_child_nodes(node):
        walk_resolved_tree(child, visitor_fn)

def get_child_nodes(node: ResolvedNode) -> List[ResolvedNode]:
    """노드의 자식 노드들을 반환"""
    ...
```

**테스트 기준**:
- [ ] 단순 SELECT 문 순회
- [ ] 모든 노드 타입 방문 확인
- [ ] 중첩 구조 (JOIN, 서브쿼리) 순회

---

### Level 3: ExpressionParentFinder (`expression_finder.py`)

**목표**: 표현식 내에서 직접 참조되는 컬럼 찾기

Java의 `ExpressionParentFinder` 클래스를 이식합니다.

```python
class ExpressionParentFinder:
    @staticmethod
    def find_direct_parents(expr: ResolvedExpr) -> List[ResolvedColumn]:
        """표현식에서 직접 참조하는 컬럼들 반환"""
        ...
```

**처리할 표현식 타입**:
- `ResolvedColumnRef` - 직접 컬럼 참조
- `ResolvedFunctionCall` - 함수 호출 (UPPER, CONCAT 등)
- `ResolvedCast` - 타입 캐스팅
- `ResolvedMakeStruct` - STRUCT 생성
- `ResolvedGetStructField` - STRUCT 필드 접근
- `ResolvedSubqueryExpr` - 서브쿼리

**특수 함수 처리**:
- `$case_no_value`, `$case_with_value` - CASE 문 (조건 제외)
- `if` - IF 함수 (조건 제외)
- `nullif` - 첫 번째 인자만

**테스트 기준**:
- [ ] 단순 컬럼 참조: `col1`
- [ ] 함수 호출: `UPPER(col1)`
- [ ] 중첩 함수: `UPPER(CONCAT(col1, col2))`
- [ ] CASE 문: `CASE WHEN x THEN col1 ELSE col2 END`
- [ ] STRUCT 접근: `struct_col.field`

---

### Level 4: ParentColumnFinder (`parent_finder.py`)

**목표**: 컬럼의 최종 소스(terminal) 컬럼 추적

Java의 `ParentColumnFinder` 클래스를 이식합니다.

```python
class ParentColumnFinder:
    @staticmethod
    def find_parents_for_column(
        statement: ResolvedStatement,
        column: ResolvedColumn
    ) -> List[ResolvedColumn]:
        """컬럼의 terminal 부모들을 찾음"""
        ...
```

**알고리즘** (2-pass):

1. **Pass 1 - 맵 구축**: AST 순회하며 컬럼 → 부모 매핑 생성
2. **Pass 2 - BFS 해석**: 목표 컬럼부터 terminal까지 추적

**처리할 노드 타입**:
- `ResolvedComputedColumn` - 계산된 컬럼
- `ResolvedTableScan` - 테이블 스캔 (terminal)
- `ResolvedTVFScan` - TVF 스캔 (terminal)
- `ResolvedWithScan` - WITH 절
- `ResolvedWithRefScan` - WITH 참조
- `ResolvedSetOperationScan` - UNION 등
- `ResolvedArrayScan` - UNNEST

**테스트 기준**:
- [ ] 직접 컬럼 선택: `SELECT col FROM table`
- [ ] 별칭: `SELECT col AS alias FROM table`
- [ ] 표현식: `SELECT UPPER(col) FROM table`
- [ ] JOIN: `SELECT a.col, b.col FROM a JOIN b`
- [ ] WITH 절: `WITH cte AS (...) SELECT ... FROM cte`
- [ ] 서브쿼리: `SELECT * FROM (SELECT col FROM table)`

---

### Level 5: ColumnLineageExtractor (`extractor.py`)

**목표**: 최종 계보 추출 API

Java의 `ColumnLineageExtractor` 클래스를 이식합니다.

```python
class ColumnLineageExtractor:
    @staticmethod
    def extract_column_lineage(
        stmt: ResolvedStatement
    ) -> Set[ColumnLineage]:
        """문장에서 컬럼 계보 추출"""
        ...
```

**지원 문장 타입**:
- `ResolvedCreateTableAsSelectStmt`
- `ResolvedCreateViewStmt` / `ResolvedCreateMaterializedViewStmt`
- `ResolvedQueryStmt` (target_table 필요)
- `ResolvedInsertStmt`
- `ResolvedUpdateStmt`
- `ResolvedMergeStmt`

**테스트 기준**:
- [ ] CTAS: `CREATE TABLE t AS SELECT ...`
- [ ] INSERT: `INSERT INTO t SELECT ...`
- [ ] UPDATE: `UPDATE t SET col = expr`
- [ ] MERGE: `MERGE INTO t USING s ...`

---

## 4. 테스트 전략

### 4.1 레벨별 독립 테스트

각 레벨은 하위 레벨의 구현 없이도 테스트 가능해야 합니다.

```
tests/zetasql_toolkit/lineage/
├── test_level1_models.py        # 데이터 모델만
├── test_level2_ast_walker.py    # AST 순회만
├── test_level3_expression.py    # 표현식 분석
├── test_level4_parent.py        # 부모 추적
└── test_level5_extractor.py     # 통합 테스트
```

### 4.2 점진적 완성도 확인

```bash
# Level 1만 완료
pytest tests/zetasql_toolkit/lineage/test_level1_models.py

# Level 1-2 완료
pytest tests/zetasql_toolkit/lineage/test_level{1,2}*.py

# 전체 완료
pytest tests/zetasql_toolkit/lineage/
```

### 4.3 테스트 카테고리

1. **단위 테스트**: 각 클래스/함수 독립 테스트
2. **통합 테스트**: 전체 파이프라인 테스트
3. **회귀 테스트**: Java 예제와 동일 결과 확인

---

## 5. 사용 예시

```python
from zetasql.api import Analyzer
from zetasql.api.builders import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind
from zetasql_toolkit.lineage import ColumnLineageExtractor

# 1. 카탈로그 구축
wiki = (TableBuilder("wikipedia")
    .add_column("title", TypeKind.TYPE_STRING)
    .add_column("comment", TypeKind.TYPE_STRING)
    .build())

catalog = CatalogBuilder("demo").add_table(wiki).build()

# 2. SQL 분석
sql = """
CREATE TABLE target AS
SELECT 
    UPPER(CONCAT(title, comment)) AS full_text
FROM wikipedia
"""

analyzer = Analyzer(catalog=catalog)
stmt = analyzer.analyze_statement(sql)

# 3. 계보 추출
lineages = ColumnLineageExtractor.extract_column_lineage(stmt)

# 4. 결과 출력
for lineage in lineages:
    print(f"{lineage.target.table}.{lineage.target.name}")
    for parent in lineage.parents:
        print(f"  <- {parent.table}.{parent.name}")

# 출력:
# target.full_text
#   <- wikipedia.title
#   <- wikipedia.comment
```

---

## 6. 참고 자료

- **Java 원본**: `.external/zetasql-toolkit/zetasql-toolkit-core/src/main/java/com/google/zetasql/toolkit/tools/lineage/`
- **zetasql-py API**: `src/zetasql/api/`
- **Proto 모델**: `src/zetasql/core/types/proto_models.py`

---

## 7. 구현 진행 상황

- [ ] Level 1: 데이터 모델
- [ ] Level 2: AST Walker
- [ ] Level 3: ExpressionParentFinder
- [ ] Level 4: ParentColumnFinder
- [ ] Level 5: ColumnLineageExtractor
- [ ] 데모 예제
