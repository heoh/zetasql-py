# Phase 1 Implementation Plan: Java API Parity

**목표**: Python API를 Java API 수준의 사용성으로 향상 (억지로 똑같이 만들 필요는 없음)

**작성일**: 2025-12-27  
**상태**: 🚧 In Progress

---

## Overview

Java ZetaSQL API와의 비교 분석을 통해 Python API에 부족한 6가지 핵심 기능을 구현합니다.
각 기능은 독립적으로 구현 가능하며, 우선순위에 따라 순차적으로 진행합니다.

---

## Task 1: PreparedQuery 래퍼 클래스 구현 ⭐ HIGH PRIORITY

**목적**: Java의 `PreparedQuery` 클래스와 동등한 기능 제공

**현재 문제점**:
- `prepare_query()` 후 수동으로 `unprepare_query()` 호출 필요
- 예외 발생 시 리소스 누수 위험
- Java의 AutoCloseable에 해당하는 기능 없음

**구현 내용**:

### 1.1 PreparedQuery 클래스 (Context Manager)

**파일**: `src/zetasql/prepared_query.py` (신규)

```python
class PreparedQuery:
    """Context manager for prepared queries with automatic cleanup.
    
    Equivalent to Java's PreparedQuery with AutoCloseable support.
    """
    
    def __init__(self, service, prepared_id, columns):
        self._service = service
        self._prepared_id = prepared_id
        self._columns = columns
        self._closed = False
    
    @property
    def prepared_query_id(self):
        """Get prepared query ID."""
        return self._prepared_id
    
    @property
    def columns(self):
        """Get output column metadata."""
        return self._columns
    
    def execute(self, parameters=None, table_content=None):
        """Execute the prepared query."""
        if self._closed:
            raise RuntimeError("PreparedQuery already closed")
        
        response = self._service.evaluate_query(
            prepared_query_id=self._prepared_id,
            params=parameters or {},
            table_content=table_content or {}
        )
        return response
    
    def close(self):
        """Release server-side resources."""
        if not self._closed:
            try:
                self._service.unprepare_query(
                    prepared_query_id=self._prepared_id
                )
            finally:
                self._closed = True
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
    
    def __del__(self):
        """Cleanup on garbage collection (safety net)."""
        if not self._closed:
            try:
                self.close()
            except:
                pass  # Suppress errors during cleanup
```

### 1.2 PreparedQueryBuilder 클래스

**파일**: `src/zetasql/prepared_query.py` (신규)

```python
class PreparedQueryBuilder:
    """Builder for PreparedQuery with fluent API.
    
    Equivalent to Java's PreparedQuery.Builder pattern.
    """
    
    def __init__(self):
        self._sql = None
        self._options = None
        self._catalog = None
        self._registered_catalog_id = None
        self._table_content = None
        self._service = None
    
    def set_sql(self, sql: str):
        """Set SQL query string."""
        self._sql = sql
        return self
    
    def set_analyzer_options(self, options):
        """Set analyzer options."""
        self._options = options
        return self
    
    def set_catalog(self, catalog):
        """Set unregistered catalog."""
        self._catalog = catalog
        return self
    
    def set_registered_catalog_id(self, catalog_id: int):
        """Set registered catalog ID."""
        self._registered_catalog_id = catalog_id
        return self
    
    def set_table_content(self, table_content):
        """Set table content for execution."""
        self._table_content = table_content
        return self
    
    def set_service(self, service):
        """Set custom service instance (optional)."""
        self._service = service
        return self
    
    def prepare(self) -> PreparedQuery:
        """Prepare the query and return PreparedQuery instance.
        
        Raises:
            ValueError: If required parameters are missing
            InvalidArgumentError: If parameter combination is invalid
        """
        # Validation
        if not self._sql:
            raise ValueError("SQL must be set")
        
        if self._catalog and self._registered_catalog_id:
            raise ValueError(
                "Cannot provide both catalog and registered_catalog_id"
            )
        
        if self._table_content and self._registered_catalog_id:
            raise ValueError(
                "Cannot use table_content with registered catalog"
            )
        
        # Get service
        service = self._service
        if service is None:
            from zetasql.local_service import ZetaSqlLocalService
            service = ZetaSqlLocalService.get_instance()
        
        # Prepare query
        response = service.prepare_query(
            sql=self._sql,
            options=self._options,
            simple_catalog=self._catalog,
            registered_catalog_id=self._registered_catalog_id,
            table_content=self._table_content or {}
        )
        
        return PreparedQuery(
            service=service,
            prepared_id=response.prepared.prepared_query_id,
            columns=response.prepared.columns
        )
    
    @staticmethod
    def builder():
        """Static factory method for builder (Java-style)."""
        return PreparedQueryBuilder()
```

### 1.3 통합 및 Export

**파일**: `src/zetasql/__init__.py`

```python
# Add to exports
from zetasql.prepared_query import PreparedQuery, PreparedQueryBuilder
```

**사용 예시**:
```python
# Builder 패턴
with PreparedQuery.builder() \
        .set_sql("SELECT * FROM Orders") \
        .set_analyzer_options(options) \
        .set_catalog(catalog) \
        .set_table_content(table_content) \
        .prepare() as query:
    
    result = query.execute()
    # 자동으로 cleanup
```

**체크리스트**:
- [ ] `PreparedQuery` 클래스 구현
- [ ] `PreparedQueryBuilder` 클래스 구현
- [ ] Context manager 테스트 (정상 종료, 예외 발생 모두)
- [ ] Builder 패턴 테스트
- [ ] 문서화 (docstring + 사용 예시)
- [ ] `__init__.py`에 export 추가

---

## Task 2: RegisteredCatalog Context Manager 추가 ⭐ HIGH PRIORITY

**목적**: Java의 `SimpleCatalog.AutoUnregister`와 동등한 기능

**현재 문제점**:
- `register_catalog()` 후 수동으로 `unregister_catalog()` 호출 필요
- 예외 발생 시 catalog 리소스 누수

**구현 내용**:

### 2.1 RegisteredCatalog 클래스

**파일**: `src/zetasql/catalog_registry.py` (신규)

```python
class RegisteredCatalog:
    """Context manager for registered catalogs.
    
    Equivalent to Java's SimpleCatalog.AutoUnregister.
    """
    
    def __init__(self, service, catalog):
        self._service = service
        self._catalog = catalog
        self._registered_id = None
    
    def __enter__(self):
        response = self._service.register_catalog(
            simple_catalog=self._catalog
        )
        self._registered_id = response.registered_id
        return self._registered_id
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._registered_id is not None:
            try:
                self._service.unregister_catalog(
                    registered_id=self._registered_id
                )
            except Exception:
                # Suppress unregister errors during cleanup
                pass
        return False
```

### 2.2 SimpleCatalog Support (Removed)

**Note**: The `SimpleCatalog.register()` method has been removed to fix the 
architectural issue where core package (Layer 1) was depending on api package (Layer 2).

**Migration**: Use `RegisteredCatalog` directly instead:

```python
from zetasql.api import RegisteredCatalog

catalog = CatalogBuilder("db").add_table(table).build()

# Old way (removed):
# with catalog.register() as catalog_id:
#     ...

# New way:
with RegisteredCatalog(catalog) as catalog_id:
    response = service.analyze(
        sql_statement="SELECT * FROM table",
        registered_catalog_id=catalog_id
    )
    # Automatically unregistered on exit
```

**Benefits**:
- Cleaner architecture: core no longer depends on api
- `RegisteredCatalog(catalog)` uses singleton service by default
- `RegisteredCatalog(catalog, service)` supports custom service instances
```

### 2.3 Export

**파일**: `src/zetasql/__init__.py`

```python
from zetasql.catalog_registry import RegisteredCatalog
```

**사용 예시**:
```python
from zetasql.api import RegisteredCatalog

catalog = CatalogBuilder("catalog").add_table(table).build()

with RegisteredCatalog(catalog) as catalog_id:
    response = service.analyze(
        sql_statement="SELECT * FROM table",
        registered_catalog_id=catalog_id
    )
    # 자동으로 unregister
```

**체크리스트**:
- [ ] `RegisteredCatalog` 클래스 구현
- [ ] `SimpleCatalog.register()` 메서드 추가
- [ ] Context manager 테스트
- [ ] 문서화
- [ ] Export 추가

---

## Task 3: 입력 검증 강화 ⭐ MEDIUM PRIORITY

**목적**: 입력 파라미터 검증 강화

**현재 문제점**:
- 파라미터 검증 부족 (예: sql=None 체크 없음)
- 에러 메시지가 불명확

**구현 내용**:

### 3.1 PreparedQueryBuilder 검증 강화

**파일**: `src/zetasql/prepared_query.py` (수정)

**참고**: 에러 분리는 하지 않습니다. ZetaSQL 서비스에 종속적이므로 
`ZetaSQLError`만 사용하고, 클라이언트 검증에는 Python 표준 `ValueError`를 사용합니다.

```python
def prepare(self) -> PreparedQuery:
    """Prepare the query with strict validation."""
    
    # Required parameters
    if not self._sql or not self._sql.strip():
        raise ValueError("SQL string must not be empty")
    
    # Mutually exclusive parameters
    if self._catalog is not None and self._registered_catalog_id is not None:
        raise ValueError(
            "Cannot provide both catalog and registered_catalog_id. "
            "Use one or the other."
        )
    
    # table_content requires simple_catalog
    if self._table_content and not self._catalog:
        raise ValueError(
            "table_content requires catalog. "
            "Cannot use with registered_catalog_id."
        )
    
    # ... prepare 로직 ...
```

**체크리스트**:
- [x] 새로운 예외 클래스 정의 → **롤백: ZetaSQLError만 사용**
- [x] `PreparedQueryBuilder.prepare()` 검증 추가
- [x] 예외 처리 테스트
- [x] 문서화 (각 예외 타입 설명)

---

## Task 4: Analyzer 헬퍼 클래스 추가 🔵 MEDIUM PRIORITY

**목적**: Java의 `Analyzer` 클래스 포팅

**현재 문제점**:
- 일반적인 분석 작업에 boilerplate 코드 필요
- 정적 유틸리티 메서드 부족

**구현 내용**:

### 4.1 Analyzer 클래스

**파일**: `src/zetasql/analyzer.py` (신규)

```python
from typing import Optional, List
from zetasql.types import proto_models
from zetasql.local_service import ZetaSqlLocalService


class Analyzer:
    """Helper class for common analysis operations.
    
    Equivalent to Java's Analyzer class with static and instance methods.
    """
    
    def __init__(
        self,
        options: proto_models.AnalyzerOptions,
        catalog: Optional[proto_models.SimpleCatalog] = None,
        service: Optional[ZetaSqlLocalService] = None
    ):
        """Initialize Analyzer with options and catalog.
        
        Args:
            options: Analyzer options to use for all operations
            catalog: Optional catalog for name resolution
            service: Optional LocalService instance (uses singleton if not provided)
        """
        self.options = options
        self.catalog = catalog
        self.service = service or ZetaSqlLocalService.get_instance()
    
    def analyze_statement(self, sql: str) -> proto_models.ResolvedStatement:
        """Analyze SQL statement and return resolved AST.
        
        Args:
            sql: SQL statement to analyze
        
        Returns:
            Resolved statement AST
        
        Example:
            >>> analyzer = Analyzer(options, catalog)
            >>> stmt = analyzer.analyze_statement("SELECT * FROM Orders")
        """
        response = self.service.analyze(
            sql_statement=sql,
            options=self.options,
            simple_catalog=self.catalog
        )
        return response.resolved_statement
    
    def analyze_expression(self, expression: str) -> proto_models.ResolvedExpr:
        """Analyze SQL expression and return resolved AST.
        
        Args:
            expression: SQL expression to analyze
        
        Returns:
            Resolved expression AST
        """
        response = self.service.analyze(
            sql_expression=expression,
            options=self.options,
            simple_catalog=self.catalog
        )
        return response.resolved_expression
    
    @staticmethod
    def analyze_statement_static(
        sql: str,
        options: proto_models.AnalyzerOptions,
        catalog: Optional[proto_models.SimpleCatalog] = None
    ) -> proto_models.ResolvedStatement:
        """Static method for one-off statement analysis.
        
        Args:
            sql: SQL statement
            options: Analyzer options
            catalog: Optional catalog
        
        Returns:
            Resolved statement AST
        
        Example:
            >>> stmt = Analyzer.analyze_statement_static(sql, options, catalog)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.analyze(
            sql_statement=sql,
            options=options,
            simple_catalog=catalog
        )
        return response.resolved_statement
    
    @staticmethod
    def analyze_expression_static(
        expression: str,
        options: proto_models.AnalyzerOptions,
        catalog: Optional[proto_models.SimpleCatalog] = None
    ) -> proto_models.ResolvedExpr:
        """Static method for one-off expression analysis."""
        service = ZetaSqlLocalService.get_instance()
        response = service.analyze(
            sql_expression=expression,
            options=options,
            simple_catalog=catalog
        )
        return response.resolved_expression
    
    @staticmethod
    def build_statement(
        resolved_stmt: proto_models.ResolvedStatement,
        catalog: Optional[proto_models.SimpleCatalog] = None
    ) -> str:
        """Convert resolved AST back to SQL string.
        
        Args:
            resolved_stmt: Resolved statement AST
            catalog: Optional catalog for type resolution
        
        Returns:
            SQL string
        
        Example:
            >>> sql = Analyzer.build_statement(resolved_stmt, catalog)
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.build_sql(
            resolved_statement=resolved_stmt,
            simple_catalog=catalog
        )
        return response.sql
    
    @staticmethod
    def extract_table_names(sql: str) -> List[str]:
        """Extract table names from SQL without full analysis.
        
        Args:
            sql: SQL statement
        
        Returns:
            List of table names referenced in the statement
        
        Example:
            >>> tables = Analyzer.extract_table_names(
            ...     "SELECT * FROM Orders JOIN Products ON ..."
            ... )
            >>> print(tables)  # ['Orders', 'Products']
        """
        service = ZetaSqlLocalService.get_instance()
        response = service.extract_table_names_from_statement(
            sql_statement=sql
        )
        return response.table_name
```

### 4.2 Export

**파일**: `src/zetasql/__init__.py`

```python
from zetasql.analyzer import Analyzer
```

**사용 예시**:
```python
# 방법 1: 인스턴스 사용
analyzer = Analyzer(options, catalog)
stmt1 = analyzer.analyze_statement("SELECT * FROM Orders")
stmt2 = analyzer.analyze_statement("SELECT * FROM Products")

# 방법 2: 정적 메서드
stmt = Analyzer.analyze_statement_static(sql, options, catalog)
sql = Analyzer.build_statement(resolved_stmt, catalog)
tables = Analyzer.extract_table_names("SELECT * FROM Orders, Products")
```

**체크리스트**:
- [ ] `Analyzer` 클래스 구현
- [ ] 인스턴스 메서드 구현
- [ ] 정적 메서드 구현
- [ ] 테스트 작성
- [ ] 문서화
- [ ] Export 추가

---

## Task 5: Value 헬퍼 메서드 추가 🔵 LOW PRIORITY

**목적**: Java의 `Value.createXxxValue()` 정적 팩토리 메서드와 동등한 기능

**현재 상태**:
- `create_table_content()` 함수가 이미 존재 (table_content.py)
- Value 생성은 가능하지만 직관적인 헬퍼 부족

**구현 내용**:

### 5.1 ValueHelper 클래스

**파일**: `src/zetasql/value_helper.py` (신규)

```python
from typing import List, Any
from zetasql.types import proto_models, TypeKind, TypeFactory


class ValueHelper:
    """Helper class for creating ZetaSQL Value objects.
    
    Provides Java-style static factory methods for common value types.
    """
    
    @staticmethod
    def create_int64_value(value: int) -> proto_models.Value:
        """Create INT64 value.
        
        Args:
            value: Python integer
        
        Returns:
            Value ProtoModel with INT64 type
        
        Example:
            >>> val = ValueHelper.create_int64_value(42)
        """
        return proto_models.Value(
            type=TypeFactory.create_simple_type(TypeKind.TYPE_INT64),
            int64_value=value
        )
    
    @staticmethod
    def create_string_value(value: str) -> proto_models.Value:
        """Create STRING value."""
        return proto_models.Value(
            type=TypeFactory.create_simple_type(TypeKind.TYPE_STRING),
            string_value=value
        )
    
    @staticmethod
    def create_bool_value(value: bool) -> proto_models.Value:
        """Create BOOL value."""
        return proto_models.Value(
            type=TypeFactory.create_simple_type(TypeKind.TYPE_BOOL),
            bool_value=value
        )
    
    @staticmethod
    def create_double_value(value: float) -> proto_models.Value:
        """Create DOUBLE value."""
        return proto_models.Value(
            type=TypeFactory.create_simple_type(TypeKind.TYPE_DOUBLE),
            double_value=value
        )
    
    @staticmethod
    def create_float_value(value: float) -> proto_models.Value:
        """Create FLOAT value."""
        return proto_models.Value(
            type=TypeFactory.create_simple_type(TypeKind.TYPE_FLOAT),
            float_value=value
        )
    
    @staticmethod
    def create_array_value(
        element_type: proto_models.Type,
        elements: List[proto_models.Value]
    ) -> proto_models.Value:
        """Create ARRAY value.
        
        Args:
            element_type: Type of array elements
            elements: List of Value objects
        
        Returns:
            Value ProtoModel with ARRAY type
        
        Example:
            >>> str_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
            >>> arr = ValueHelper.create_array_value(
            ...     element_type=str_type,
            ...     elements=[
            ...         ValueHelper.create_string_value("a"),
            ...         ValueHelper.create_string_value("b")
            ...     ]
            ... )
        """
        array_type = TypeFactory.create_array_type(element_type)
        return proto_models.Value(
            type=array_type,
            array_value=proto_models.ArrayValue(element=elements)
        )
    
    @staticmethod
    def create_null_value(value_type: proto_models.Type) -> proto_models.Value:
        """Create NULL value of specified type.
        
        Args:
            value_type: Type of the NULL value
        
        Returns:
            Value ProtoModel representing NULL
        """
        return proto_models.Value(
            type=value_type,
            is_null=True
        )
    
    @staticmethod
    def from_python(value: Any, target_type: proto_models.Type) -> proto_models.Value:
        """Convert Python value to ZetaSQL Value.
        
        Args:
            value: Python value (int, str, float, bool, None, list)
            target_type: Target ZetaSQL type
        
        Returns:
            Value ProtoModel
        
        Example:
            >>> val = ValueHelper.from_python(
            ...     42,
            ...     TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
            ... )
        """
        if value is None:
            return ValueHelper.create_null_value(target_type)
        
        # Get type kind from target_type
        type_proto = target_type.to_proto()
        type_kind = type_proto.type_kind
        
        if type_kind == TypeKind.TYPE_INT64:
            return ValueHelper.create_int64_value(int(value))
        elif type_kind == TypeKind.TYPE_STRING:
            return ValueHelper.create_string_value(str(value))
        elif type_kind == TypeKind.TYPE_BOOL:
            return ValueHelper.create_bool_value(bool(value))
        elif type_kind == TypeKind.TYPE_DOUBLE:
            return ValueHelper.create_double_value(float(value))
        elif type_kind == TypeKind.TYPE_FLOAT:
            return ValueHelper.create_float_value(float(value))
        elif type_kind == TypeKind.TYPE_ARRAY:
            if not isinstance(value, list):
                raise TypeError(f"Expected list for ARRAY type, got {type(value)}")
            element_type = target_type  # TODO: extract element type
            elements = [
                ValueHelper.from_python(elem, element_type)
                for elem in value
            ]
            return ValueHelper.create_array_value(element_type, elements)
        else:
            raise NotImplementedError(
                f"Conversion not implemented for type {type_kind}"
            )
```

### 5.2 Export

**파일**: `src/zetasql/__init__.py`

```python
from zetasql.value_helper import ValueHelper
```

**사용 예시**:
```python
# 직접 생성
val1 = ValueHelper.create_int64_value(42)
val2 = ValueHelper.create_string_value("hello")

# Python 값에서 변환
val3 = ValueHelper.from_python(42, int64_type)
```

**체크리스트**:
- [ ] `ValueHelper` 클래스 구현
- [ ] 기본 타입 팩토리 메서드
- [ ] ARRAY, STRUCT 등 복합 타입 지원
- [ ] `from_python()` 변환 메서드
- [ ] 테스트 작성
- [ ] 문서화
- [ ] Export 추가

---

## Task 6: 문서화 개선 📚 ONGOING

**목적**: Java Javadoc 수준의 상세한 문서화

**구현 내용**:

### 6.1 API 문서화

각 클래스/메서드에 상세한 docstring 추가:
- Args: 모든 파라미터 설명
- Returns: 반환값 설명
- Raises: 발생 가능한 예외
- Example: 사용 예시 코드
- See Also: 관련 API 참조

### 6.2 가이드 문서

**파일**: `docs/API_USAGE_GUIDE.md` (신규)

내용:
- Quick Start
- 주요 패턴별 사용 예시
- Java API와의 차이점
- 모범 사례 (Best Practices)
- FAQ

**체크리스트**:
- [ ] PreparedQuery docstring
- [ ] RegisteredCatalog docstring
- [ ] Analyzer docstring
- [ ] ValueHelper docstring
- [ ] API_USAGE_GUIDE.md 작성
- [ ] execute_query_demo.py 업데이트

---

## Implementation Order (권장 순서)

1. **Task 1: PreparedQuery** (가장 중요, 메모리 누수 방지)
2. **Task 2: RegisteredCatalog** (PreparedQuery와 함께 사용)
3. **Task 3: 예외 강화** (Task 1, 2에서 사용)
4. **Task 4: Analyzer** (독립적, 편의성 향상)
5. **Task 5: ValueHelper** (선택적, 우선순위 낮음)
6. **Task 6: 문서화** (모든 작업과 병행)

---

## Testing Strategy

각 Task별 테스트 파일:
- `tests/test_prepared_query.py`
- `tests/test_catalog_registry.py`
- `tests/test_exceptions.py`
- `tests/test_analyzer.py`
- `tests/test_value_helper.py`

테스트 커버리지:
- 정상 케이스
- 예외 케이스
- Context manager cleanup
- 리소스 누수 검증

---

## Progress Tracking

- [ ] Task 1: PreparedQuery 완료
- [ ] Task 2: RegisteredCatalog 완료
- [ ] Task 3: 예외 강화 완료
- [ ] Task 4: Analyzer 완료
- [ ] Task 5: ValueHelper 완료
- [ ] Task 6: 문서화 완료

**완료 기준**: 모든 체크리스트 항목 완료 + 테스트 통과 + 문서화 완료

---

## Notes

- `@parameters` 데코레이터가 이미 잘 동작하므로 LocalService 메서드 시그니처는 수정하지 않음
- Python 관습을 따르되 Java API와의 일관성 유지
- 억지로 똑같이 만들 필요는 없음 - Pythonic하게 개선
