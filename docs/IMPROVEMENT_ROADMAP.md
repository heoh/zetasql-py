# ZetaSQL-Py 개선 로드맵

> **작성일**: 2025-12-25  
> **목적**: AI Agent와 함께 수행할 개선 작업 계획서  
> **범위**: API 개선, 테스트 강화, 문서화, 개발자 경험 향상

---

## 📊 현황 요약

### 강점
- ✅ **혁신적인 Concrete ProtoModel 시스템**: 34,000+ 줄의 자동 생성 dataclass로 타입 안전한 AST 조작
  - Nested class 구조 (예: `AllowedHintsAndOptions.Hint`)
  - MRO 기반 from_proto/to_proto 자동 변환
  - LocalService가 자동으로 ProtoModel 반환 (proto 직접 조작 불필요)
- ✅ 명확한 프로젝트 구조와 모듈 분리
- ✅ WASM 기반으로 크로스 플랫폼 지원
- ✅ 좋은 예제 코드 (basic_usage.py, execute_query_demo.py)

### 개선 필요 영역
- ✅ **ProtoModel 시스템** (완료): Concrete dataclass 기반으로 타입 안전성 확보
- ❌ 장황한 카탈로그 생성 (raw protobuf 직접 조작)
- ❌ 타입 시스템이 매직 넘버 기반 (type_pb2.TYPE_INT64 = 2)
- ❌ 빌더 패턴 부재
- ❌ 테스트 커버리지 부족 (5개 파일, 56개 테스트 - ProtoModel 테스트 19개 추가)
- ❌ API 레퍼런스 문서 부재
- ❌ 리소스 관리 개선 필요 (수동 cleanup)

---

## 🎯 우선순위 매트릭스

### 🔥 High Priority + Small Effort (Quick Wins)

#### 1. Types Enum Wrapper
**문제**: `type_pb2.TYPE_INT64` 같은 매직 넘버 사용으로 가독성 저하 및 타입 안정성 부족

**해결책**: 타입 안전한 Enum 래퍼 생성
```python
# src/zetasql/types_enum.py
from enum import IntEnum
from zetasql.wasi._pb2.zetasql.public import type_pb2

class Types(IntEnum):
    """Type-safe wrapper for ZetaSQL type constants"""
    INT32 = type_pb2.TYPE_INT32
    INT64 = type_pb2.TYPE_INT64
    STRING = type_pb2.TYPE_STRING
    DOUBLE = type_pb2.TYPE_DOUBLE
    BOOL = type_pb2.TYPE_BOOL
    DATE = type_pb2.TYPE_DATE
    TIMESTAMP = type_pb2.TYPE_TIMESTAMP
    ARRAY = type_pb2.TYPE_ARRAY
    STRUCT = type_pb2.TYPE_STRUCT
    # ... 모든 타입
    
    @classmethod
    def is_numeric(cls, type_kind: int) -> bool:
        """숫자형 타입 체크"""
        return type_kind in {cls.INT32, cls.INT64, cls.FLOAT, cls.DOUBLE}
```

**사용 예시**:
```python
# Before (매직 넘버)
col.type.type_kind = type_pb2.TYPE_INT64  # 2?

# After (명확한 Enum)
col.type.type_kind = Types.INT64  # IDE 자동완성 지원
```

**예상 효과**: 
- IDE 자동완성 개선
- 타입 안정성 향상
- 코드 가독성 대폭 개선

**작업량**: Small (1-2일)  
**파일**: 신규 `src/zetasql/types_enum.py`

---

#### 2. py.typed Marker 추가
**문제**: 패키지가 typed로 마크되지 않아 mypy 등 타입 체커가 타입 힌트를 무시

**해결책**:
```bash
touch src/zetasql/py.typed
```

**pyproject.toml 수정**:
```toml
[tool.setuptools.package-data]
zetasql = [
    "py.typed",  # 추가
    "wasi/*.wasm",
]
```

**예상 효과**: 타입 체킹 활성화로 개발자 경험 향상

**작업량**: Minimal (10분)  
**파일**: `src/zetasql/py.typed` (신규), [pyproject.toml](pyproject.toml)

---

#### 3. AnalyzerOptionsFactory
**문제**: 모든 예제 파일에서 30+ 줄의 중복 코드로 AnalyzerOptions 생성

**현재 패턴** ([execute_query_demo.py](examples/execute_query_demo.py#L10-L40)):
```python
def create_analyzer_options():
    opts = options_pb2.AnalyzerOptionsProto()
    language_options = opts.language_options
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    # 15+ 줄의 feature 활성화...
    return opts
```

**해결책**: Factory 패턴으로 중복 제거
```python
# src/zetasql/options.py
class AnalyzerOptionsFactory:
    @staticmethod
    def default() -> options_pb2.AnalyzerOptionsProto:
        """모든 기능 활성화된 기본 옵션"""
        opts = options_pb2.AnalyzerOptionsProto()
        opts.language_options.name_resolution_mode = NAME_RESOLUTION_DEFAULT
        opts.language_options.product_mode = PRODUCT_INTERNAL
        AnalyzerOptionsFactory._enable_all_features(opts.language_options)
        return opts
    
    @staticmethod
    def strict() -> options_pb2.AnalyzerOptionsProto:
        """엄격한 옵션 (최소 기능)"""
        # ...
```

**사용 예시**:
```python
# Before: 30+ lines
opts = create_analyzer_options()

# After: 1 line
opts = AnalyzerOptionsFactory.default()
```

**예상 효과**: 코드 중복 제거, 사용성 대폭 개선

**작업량**: Small (1일)  
**파일**: 신규 `src/zetasql/options.py`

---

#### 4. 에러 처리 테스트 추가
**문제**: 에러 시나리오 테스트가 전무

**해결책**: 포괄적인 에러 테스트 작성
```python
# tests/test_errors.py
def test_parse_error_invalid_syntax():
    """잘못된 SQL 구문 파싱 에러 검증"""
    service = ZetaSqlLocalService()
    with pytest.raises(ZetaSQLError) as exc_info:
        service.parse(sql_statement="SELECT * FORM table1")  # 오타: FORM
    assert exc_info.value.code == StatusCode.INVALID_ARGUMENT
    assert "FORM" in exc_info.value.message

def test_analyze_error_unknown_table():
    """존재하지 않는 테이블 분석 에러"""
    service = ZetaSqlLocalService()
    catalog = simple_catalog_pb2.SimpleCatalogProto()
    catalog.name = "test"
    with pytest.raises(ZetaSQLError):
        service.analyze(
            sql_statement="SELECT * FROM nonexistent_table",
            simple_catalog=catalog
        )

def test_type_mismatch_error():
    """타입 불일치 에러"""
    # ...
```

**테스트 항목**:
- ✅ 구문 에러 (FORM 대신 FROM)
- ✅ 알 수 없는 테이블/컬럼
- ✅ 타입 불일치
- ✅ 카탈로그 등록 에러
- ✅ 에러 메시지 품질 검증

**작업량**: Small (2일)  
**파일**: 신규 `tests/test_errors.py`

---

#### 5. Quick Start 예제 추가
**문제**: README에 간단한 시작 예제 부재

**해결책**: README에 10줄 Quick Start 추가
```python
## Quick Start

from zetasql.local_service import ZetaSqlLocalService

# Parse SQL
service = ZetaSqlLocalService()
response = service.parse(sql_statement="SELECT 1 AS one")
print(f"Parsed: {response.parsed_statement.WhichOneof('node')}")
# Output: 'query_statement_node'

# For analysis with catalog, see examples/
```

**작업량**: Minimal (15분)  
**파일**: [README.md](README.md)

---

### 🚀 High Priority + Medium Effort

#### 6. Builder Patterns (카탈로그 생성 개선)
**문제**: 카탈로그/테이블 생성이 protobuf 직접 조작으로 장황함

**현재 방식** ([execute_query_demo.py](examples/execute_query_demo.py#L20-L50)):
```python
catalog = simple_catalog_pb2.SimpleCatalogProto()
catalog.name = "demo"
orders = catalog.table.add()
orders.name = "orders"
orders.serialization_id = 1
col = orders.column.add()
col.name = "order_id"
col.type.type_kind = type_pb2.TYPE_INT64
col = orders.column.add()
col.name = "product_id"
col.type.type_kind = type_pb2.TYPE_INT64
# 반복...
```

**해결책**: ProtoModel과 통합된 유창한 빌더 API
```python
# src/zetasql/builders.py
from zetasql.types_enum import Types
from zetasql.types import ProtoModel

class TableBuilder:
    def __init__(self, name: str):
        self.table_proto = simple_catalog_pb2.SimpleTableProto()
        self.table_proto.name = name
    
    def add_column(self, name: str, type_kind: Types) -> 'TableBuilder':
        col = self.table_proto.column.add()
        col.name = name
        col.type.type_kind = type_kind
        return self  # Method chaining
    
    def with_serialization_id(self, id: int) -> 'TableBuilder':
        self.table_proto.serialization_id = id
        return self
    
    def build(self) -> simple_catalog_pb2.SimpleTableProto:
        return self.table_proto

class CatalogBuilder:
    def __init__(self, name: str):
        self.catalog_proto = simple_catalog_pb2.SimpleCatalogProto()
        self.catalog_proto.name = name
    
    def add_table(self, table: simple_catalog_pb2.SimpleTableProto) -> 'CatalogBuilder':
        self.catalog_proto.table.add().CopyFrom(table)
        return self
    
    def with_builtin_functions(self, language_options) -> 'CatalogBuilder':
        self.catalog_proto.builtin_function_options.language_options.CopyFrom(
            language_options
        )
        return self
    
    def build(self) -> simple_catalog_pb2.SimpleCatalogProto:
        return self.catalog_proto
```

**사용 예시**:
```python
# Clean, fluent API
catalog = (CatalogBuilder("demo")
    .add_table(
        TableBuilder("orders")
            .add_column("order_id", Types.INT64)
            .add_column("product_id", Types.INT64)
            .add_column("quantity", Types.INT64)
            .add_column("price", Types.DOUBLE)
            .with_serialization_id(1)
            .build()
    )
    .add_table(
        TableBuilder("products")
            .add_column("product_id", Types.INT64)
            .add_column("name", Types.STRING)
            .build()
    )
    .with_builtin_functions(language_options)
    .build())
```

**비교**:
- **Before**: 50+ 줄의 장황한 protobuf 조작
- **After**: 15줄의 읽기 쉬운 빌더 패턴

**작업량**: Medium (3-5일)  
**파일**: 신규 `src/zetasql/builders.py`  
**의존성**: Types Enum (작업 #1)

---

#### 7. 타입 시스템 테스트
**문제**: 타입 생성/검증 테스트가 전무

**해결책**: 포괄적인 타입 시스템 테스트
```python
# tests/test_types.py
def test_type_enum_constants():
    """Types enum 상수 검증"""
    assert Types.INT64 == type_pb2.TYPE_INT64
    assert Types.STRING == type_pb2.TYPE_STRING

def test_type_checking_methods():
    """타입 카테고리 체크 메서드"""
    assert Types.is_numeric(Types.INT64)
    assert Types.is_numeric(Types.DOUBLE)
    assert not Types.is_numeric(Types.STRING)
    assert Types.is_integer(Types.INT64)

def test_type_factory_simple():
    """단순 타입 생성"""
    type_proto = TypeFactory.create_simple(Types.INT64)
    assert type_proto.type_kind == Types.INT64

def test_type_factory_array():
    """배열 타입 생성"""
    element_type = TypeFactory.create_simple(Types.STRING)
    array_type = TypeFactory.create_array(element_type)
    assert array_type.type_kind == Types.ARRAY
    assert array_type.array_type.element_type.type_kind == Types.STRING

def test_type_factory_struct():
    """구조체 타입 생성"""
    struct_type = TypeFactory.create_struct([
        ("id", TypeFactory.create_simple(Types.INT64)),
        ("name", TypeFactory.create_simple(Types.STRING))
    ])
    assert struct_type.type_kind == Types.STRUCT
    assert len(struct_type.struct_type.field) == 2
```

**작업량**: Medium (3일)  
**파일**: 신규 `tests/test_types.py`  
**의존성**: Types Enum, TypeFactory

---

#### 8. 타입 힌트 강화
**문제**: [local_service.py](src/zetasql/local_service.py)의 타입 힌트가 기본 수준

**해결책**: 포괄적인 타입 힌트 및 오버로드
```python
from typing import Optional, Union, overload
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2

class ZetaSqlLocalService:
    """Client for ZetaSQL Local Service via WASM.
    
    Thread Safety:
        Not thread-safe. Create separate instances for concurrent use.
    
    Example:
        >>> service = ZetaSqlLocalService()
        >>> response = service.parse(sql_statement="SELECT 1")
    """
    
    @overload
    def analyze(
        self,
        *,
        sql_statement: str,
        simple_catalog: simple_catalog_pb2.SimpleCatalogProto,
        options: Optional[options_pb2.AnalyzerOptionsProto] = None
    ) -> proto_models.AnalyzeResponse: ...
    
    @overload
    def analyze(
        self,
        *,
        sql_statement: str,
        registered_catalog_id: int,
        options: Optional[options_pb2.AnalyzerOptionsProto] = None
    ) -> proto_models.AnalyzeResponse: ...
    
    def analyze(self, **kwargs) -> proto_models.AnalyzeResponse:
        """Analyze SQL statement with semantic analysis.
        
        Args:
            sql_statement: SQL string to analyze
            simple_catalog: Inline catalog (mutually exclusive with registered_catalog_id)
            registered_catalog_id: ID from register_catalog() call
            options: Analyzer options (optional)
        
        Returns:
            AnalyzeResponse with resolved AST
        
        Raises:
            ZetaSQLError: If SQL has syntax or semantic errors
        
        Example:
            >>> catalog = simple_catalog_pb2.SimpleCatalogProto()
            >>> catalog.name = "test"
            >>> response = service.analyze(
            ...     sql_statement="SELECT 1",
            ...     simple_catalog=catalog
            ... )
        """
        # 구현...
```

**작업량**: Medium (2-3일)  
**파일**: [src/zetasql/local_service.py](src/zetasql/local_service.py)

---

### 🔧 Medium Priority + Small Effort

#### 9. Context Manager for Catalog Registration
**문제**: 카탈로그 등록/해제를 수동으로 관리해야 함

**현재 방식**:
```python
service = ZetaSqlLocalService()
reg_response = service.register_catalog(simple_catalog=catalog)
catalog_id = reg_response.registered_id

try:
    response = service.analyze(sql_statement=sql, registered_catalog_id=catalog_id)
    # ...
finally:
    service.unregister_catalog(registered_id=catalog_id)
```

**해결책**: Context manager 지원
```python
# src/zetasql/local_service.py
class RegisteredCatalog:
    """Context manager for catalog lifecycle"""
    
    def __init__(self, service: ZetaSqlLocalService, catalog_proto):
        self.service = service
        self.catalog_proto = catalog_proto
        self.catalog_id: Optional[int] = None
    
    def __enter__(self) -> 'RegisteredCatalog':
        resp = self.service.register_catalog(simple_catalog=self.catalog_proto)
        self.catalog_id = resp.registered_id
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.catalog_id:
            try:
                self.service.unregister_catalog(registered_id=self.catalog_id)
            except:
                pass  # Suppress cleanup errors
        return False
    
    def analyze(self, sql_statement: str, options=None):
        """Convenience method for analysis"""
        return self.service.analyze(
            sql_statement=sql_statement,
            registered_catalog_id=self.catalog_id,
            options=options
        )

# ZetaSqlLocalService에 추가
def registered_catalog(self, catalog_proto) -> RegisteredCatalog:
    """Create context manager for catalog registration.
    
    Example:
        >>> with service.registered_catalog(catalog) as cat:
        ...     response = cat.analyze("SELECT * FROM orders")
    """
    return RegisteredCatalog(self, catalog_proto)
```

**사용 예시**:
```python
# Clean resource management
with service.registered_catalog(catalog) as cat:
    response = cat.analyze("SELECT * FROM orders")
    # ...
# Automatic cleanup
```

**작업량**: Small (1-2일)  
**파일**: [src/zetasql/local_service.py](src/zetasql/local_service.py)

---

#### 10. High-Level Query API
**문제**: 사용자가 parse → analyze → format 등을 직접 오케스트레이션해야 함

**해결책**: 고수준 API 래퍼
```python
# src/zetasql/query.py
class QueryAnalyzer:
    """High-level interface for SQL query operations"""
    
    def __init__(self, service: ZetaSqlLocalService):
        self.service = service
        self._default_options = AnalyzerOptionsFactory.default()
    
    def analyze_with_catalog(
        self, 
        sql: str, 
        catalog: simple_catalog_pb2.SimpleCatalogProto,
        options=None
    ) -> proto_models.AnalyzeResponse:
        """Analyze SQL with automatic catalog lifecycle management"""
        with self.service.registered_catalog(catalog) as cat:
            return cat.analyze(sql, options or self._default_options)
    
    def quick_parse(self, sql: str) -> proto_models.ParseResponse:
        """Quick parse without catalog"""
        return self.service.parse(sql_statement=sql)
    
    def format_query(self, sql: str) -> str:
        """Format SQL query"""
        resp = self.service.format_sql(sql=sql)
        return resp.sql
    
    def extract_tables(self, sql: str) -> List[str]:
        """Extract table names from SQL"""
        resp = self.service.extract_table_names_from_statement(sql_statement=sql)
        return [tn.table_name for tn in resp.table_name]
```

**사용 예시**:
```python
analyzer = QueryAnalyzer(service)

# 한 줄로 분석
response = analyzer.analyze_with_catalog(sql, catalog)

# 한 줄로 포맷팅
formatted = analyzer.format_query("select   a,b   from   t")

# 테이블 추출
tables = analyzer.extract_tables("SELECT * FROM orders JOIN products")
```

**작업량**: Small (1-2일)  
**파일**: 신규 `src/zetasql/query.py`  
**의존성**: Context Manager (작업 #9), AnalyzerOptionsFactory (작업 #3)

---

#### 11. 코드 품질 도구 설정
**문제**: 린팅, 포맷팅, 타입 체킹이 CI에 없음

**해결책**: 개발 도구 설정

**pyproject.toml 업데이트**:
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    # 추가:
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.7.0",
    "types-protobuf>=4.24.0",
]

[tool.black]
line-length = 100
target-version = ['py310']

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "UP", "B"]
ignore = ["E501"]  # Line too long (handled by black)

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false  # 점진적 적용
```

**CI 워크플로우 추가** (.github/workflows/test.yml):
```yaml
- name: Check code formatting
  run: |
    pip install black ruff
    black --check src/ tests/
    ruff check src/ tests/

- name: Type check
  run: |
    pip install mypy types-protobuf
    mypy src/zetasql/
```

**Pre-commit hooks** (`.pre-commit-config.yaml`):
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-protobuf]
```

**작업량**: Small (1일)  
**파일**: [pyproject.toml](pyproject.toml), `.pre-commit-config.yaml` (신규), `.github/workflows/test.yml`

---

#### 12. README 개선
**문제**: README가 기본적인 내용만 포함

**추가할 섹션**:

```markdown
## Architecture

zetasql-py runs ZetaSQL's C++ analysis engine compiled to WebAssembly:

```
Python Code → WASM Client → ZetaSQL (WASM) → Protobuf RPC
```

**Benefits:**
- ✅ Native ZetaSQL compatibility
- ✅ No C++ compilation required
- ✅ Cross-platform (Linux, macOS, Windows)

**Trade-offs:**
- ⚠️ 2-3x slower than native C++ (WASM overhead)
- ⚠️ Higher memory usage

---

## Performance Characteristics

| Operation | Typical Time | Use Case |
|-----------|--------------|----------|
| Parse | 5-10ms | Syntax validation |
| Analyze | 20-50ms | Semantic analysis with catalog |
| Execute | 10-100ms | Small query evaluation |

**Suitable for:**
- ✅ Development and testing
- ✅ CI/CD pipelines
- ✅ Query validation tools

**Not recommended for:**
- ❌ High-throughput production workloads
- ❌ Real-time query processing

---

## Troubleshooting

### Error: "WASM file not found"
Ensure the zetasql package is properly installed:
```bash
pip install --force-reinstall zetasql
```

### Error: "timezone features may not work correctly"
Install tzdata package:
```bash
pip install tzdata
```

### Error: "Cannot analyze query"
Check that:
1. Catalog is properly configured
2. All tables and columns exist
3. SQL syntax is valid

---

## Comparison with Java Implementation

| Feature | Python | Java |
|---------|--------|------|
| API Style | Service-based | Object-oriented |
| Catalog Creation | Protobuf (verbose) | Fluent builders |
| Type System | Numeric constants | Type-safe enums |
| Resource Management | Manual/Context managers | Try-with-resources |
| **Proto Models** | **✨ Concrete dataclasses** | Direct proto |

**Key Advantages:** Python's ProtoModel system provides concrete dataclass benefits:
```python
# Python: Concrete dataclass - clean instantiation
from zetasql.types import ResolvedLiteral, Type

# Direct construction (dataclass fields)
literal = ResolvedLiteral(
    type=Type(type_kind=2),  # Still need enum improvement
    value=Value(int64_value=42)
)

# Bidirectional conversion - automatic via MRO
proto = literal.to_proto()  # Convert to proto when needed
model = ResolvedLiteral.from_proto(proto)  # Parse proto back to model

# LocalService returns ProtoModel automatically - no manual conversion!
response = service.parse(sql_statement="SELECT 1")
stmt = response.parsed_statement  # Already concrete ProtoModel, not proto!

# Direct field access (dataclass)
print(stmt.query.query_expr.select_list)  # Clean navigation

# Java: Proto builder pattern
ResolvedLiteralProto.Builder builder = ResolvedLiteralProto.newBuilder();
builder.setType(typeProto);
builder.setValue(valueProto);
ResolvedLiteralProto proto = builder.build();
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

---

## Roadmap

See [IMPROVEMENT_ROADMAP.md](IMPROVEMENT_ROADMAP.md) for planned enhancements.
```

**작업량**: Small (2-3시간)  
**파일**: [README.md](README.md)

---

### 🛠️ Medium Priority + Medium Effort

#### 13. API 레퍼런스 문서 (Sphinx)
**문제**: API 문서 없음

**해결책**: Sphinx 문서 생성

**설정 파일** (`docs/conf.py`):
```python
project = 'zetasql-py'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
html_theme = 'sphinx_rtd_theme'
```

**문서 구조**:
```
docs/
  index.md              # 메인 페이지
  api/
    local_service.md    # Service API
    types.md            # Proto wrappers
    builders.md         # Builder APIs
    exceptions.md       # Error handling
  guides/
    quickstart.md
    catalog_setup.md
    query_analysis.md
  java_comparison.md    # Java vs Python
```

**작업량**: Medium (3-5일)  
**의존성**: 모든 API 개선이 완료된 후

---

#### 14. 쿼리 실행 테스트
**문제**: prepare_query/evaluate_query 관련 테스트가 기본 수준

**추가할 테스트**:
```python
# tests/test_query_execution.py
def test_prepare_and_evaluate():
    """Prepare + Evaluate 워크플로우"""
    service = ZetaSqlLocalService()
    
    # Prepare
    prep_resp = service.prepare_query(sql="SELECT @a + @b AS sum")
    
    # Evaluate with parameters
    eval_resp = service.evaluate_query(
        prepared_query_id=prep_resp.prepared_query_id,
        params={
            "a": Value(int64_value=10),
            "b": Value(int64_value=20)
        }
    )
    
    # Verify result
    assert eval_resp.value.int64_value == 30

def test_parameter_binding():
    """파라미터 바인딩 테스트"""
    # ...

def test_table_content_evaluation():
    """TableContent를 사용한 쿼리 평가"""
    # ...

def test_complex_query_with_joins():
    """조인이 있는 복잡한 쿼리"""
    # ...
```

**작업량**: Medium (3-4일)  
**파일**: `tests/test_query_execution.py` (확장)

---

#### 15. TypeFactory 구현
**문제**: 복잡한 타입(Array, Struct) 생성이 어려움

**해결책**: Java 스타일의 TypeFactory
```python
# src/zetasql/type_factory.py
from typing import List, Tuple
from zetasql.wasi._pb2.zetasql.public import type_pb2
from zetasql.types_enum import Types

class TypeFactory:
    """Factory for creating ZetaSQL types"""
    
    @staticmethod
    def create_simple(type_kind: Types) -> type_pb2.TypeProto:
        """Create simple type
        
        Example:
            >>> int_type = TypeFactory.create_simple(Types.INT64)
        """
        proto = type_pb2.TypeProto()
        proto.type_kind = type_kind
        return proto
    
    @staticmethod
    def create_array(element_type: type_pb2.TypeProto) -> type_pb2.TypeProto:
        """Create array type
        
        Example:
            >>> string_type = TypeFactory.create_simple(Types.STRING)
            >>> array_type = TypeFactory.create_array(string_type)
            >>> # ARRAY<STRING>
        """
        proto = type_pb2.TypeProto()
        proto.type_kind = Types.ARRAY
        proto.array_type.element_type.CopyFrom(element_type)
        return proto
    
    @staticmethod
    def create_struct(
        fields: List[Tuple[str, type_pb2.TypeProto]]
    ) -> type_pb2.TypeProto:
        """Create struct type
        
        Example:
            >>> struct_type = TypeFactory.create_struct([
            ...     ("id", TypeFactory.create_simple(Types.INT64)),
            ...     ("name", TypeFactory.create_simple(Types.STRING))
            ... ])
            >>> # STRUCT<id INT64, name STRING>
        """
        proto = type_pb2.TypeProto()
        proto.type_kind = Types.STRUCT
        for field_name, field_type in fields:
            field = proto.struct_type.field.add()
            field.field_name = field_name
            field.field_type.CopyFrom(field_type)
        return proto
    
    @staticmethod
    def create_proto_type(message_descriptor) -> type_pb2.TypeProto:
        """Create proto type from message descriptor"""
        # Implementation...
```

**사용 예시**:
```python
# 복잡한 타입 생성이 간단해짐
order_struct = TypeFactory.create_struct([
    ("order_id", TypeFactory.create_simple(Types.INT64)),
    ("items", TypeFactory.create_array(
        TypeFactory.create_struct([
            ("product_id", TypeFactory.create_simple(Types.INT64)),
            ("quantity", TypeFactory.create_simple(Types.INT64))
        ])
    ))
])
# STRUCT<order_id INT64, items ARRAY<STRUCT<product_id INT64, quantity INT64>>>
```

**작업량**: Medium (3-4일)  
**파일**: 신규 `src/zetasql/type_factory.py`  
**의존성**: Types Enum (작업 #1)

---

#### 16. PreparedQuery High-Level API
**문제**: prepare_query/evaluate_query가 low-level RPC 호출

**해결책**: Java 스타일의 PreparedQuery 클래스
```python
# src/zetasql/prepared_query.py
from typing import Dict, Any, List, Optional
from contextlib import contextmanager

class PreparedQuery:
    """High-level prepared query interface with auto-cleanup"""
    
    def __init__(self, service: ZetaSqlLocalService, prepared_id: int,
                 response: proto_models.PrepareQueryResponse):
        self.service = service
        self.prepared_id = prepared_id
        self.response = response
        self._closed = False
    
    def execute(self, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Execute query and return results as list of dicts
        
        Args:
            parameters: Query parameters (e.g., {"a": 10, "b": 20})
        
        Returns:
            List of result rows as dicts
        
        Example:
            >>> with PreparedQuery.prepare(service, "SELECT @a + 1") as query:
            ...     results = query.execute({"a": 10})
            ...     print(results)  # [{"": 11}]
        """
        if self._closed:
            raise ValueError("Query already closed")
        
        eval_resp = self.service.evaluate_query(
            prepared_query_id=self.prepared_id,
            params=self._convert_params(parameters or {})
        )
        return self._parse_results(eval_resp)
    
    def close(self):
        """Release resources"""
        if not self._closed:
            try:
                self.service.unprepare_query(prepared_query_id=self.prepared_id)
            except:
                pass
            self._closed = True
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
    
    @classmethod
    @contextmanager
    def prepare(cls, service: ZetaSqlLocalService, sql: str, **kwargs):
        """Prepare query with automatic cleanup
        
        Example:
            >>> with PreparedQuery.prepare(service, "SELECT 1") as query:
            ...     results = query.execute()
        """
        resp = service.prepare_query(sql=sql, **kwargs)
        query = cls(service, resp.prepared_query_id, resp)
        try:
            yield query
        finally:
            query.close()
```

**사용 예시**:
```python
# Clean API with automatic resource management
with PreparedQuery.prepare(service, "SELECT @a * @b AS product") as query:
    results = query.execute({"a": 5, "b": 10})
    print(results)  # [{"product": 50}]
# Automatic cleanup
```

**작업량**: Medium (3-4일)  
**파일**: 신규 `src/zetasql/prepared_query.py`

---

### 📉 Low Priority

#### 17. 응답 캐싱 레이어
**목적**: 동일한 SQL 파싱 결과를 캐싱하여 성능 개선

**구현**:
```python
# src/zetasql/cache.py
from functools import lru_cache
import hashlib

class CachedService:
    def __init__(self, service: ZetaSqlLocalService, cache_size: int = 1000):
        self.service = service
        self._parse_cache = {}
    
    @lru_cache(maxsize=1000)
    def parse_cached(self, sql: str) -> proto_models.ParseResponse:
        """Parse with caching (immutable operation)"""
        return self.service.parse(sql_statement=sql)
```

**작업량**: Medium  
**우선순위**: Low (성능이 문제일 때만)

---

#### 18. Jupyter Notebook 예제
**목적**: 인터랙티브 예제 제공

**구조**:
```
examples/notebooks/
  01_getting_started.ipynb
  02_catalog_setup.ipynb
  03_query_analysis.ipynb
  04_type_system.ipynb
```

**작업량**: Medium  
**우선순위**: Low (문서화 완료 후)

---

## 📋 구현 로드맵

### Phase 1: Foundation (1-2주) - Quick Wins
**목표**: 기본 사용성 대폭 개선

| 작업 | 예상 시간 | 파일 |
|------|-----------|------|
| 1. Types Enum | 1-2일 | `src/zetasql/types_enum.py` |
| 2. py.typed | 10분 | `src/zetasql/py.typed` |
| 3. AnalyzerOptionsFactory | 1일 | `src/zetasql/options.py` |
| 4. 에러 테스트 | 2일 | `tests/test_errors.py` |
| 5. Quick Start | 15분 | `README.md` |

**완료 시 효과**:
- ✅ 타입 안정성 대폭 개선
- ✅ IDE 지원 활성화
- ✅ 코드 중복 제거
- ✅ 에러 처리 신뢰성 향상

---

### Phase 2: API Improvements (2-3주)
**목표**: API를 Java 수준으로 향상

| 작업 | 예상 시간 | 파일 |
|------|-----------|------|
| 6. Builder Patterns | 3-5일 | `src/zetasql/builders.py` |
| 7. 타입 시스템 테스트 | 3일 | `tests/test_types.py` |
| 8. 타입 힌트 강화 | 2-3일 | `src/zetasql/local_service.py` |
| 9. Context Manager | 1-2일 | `src/zetasql/local_service.py` |
| 10. High-Level API | 1-2일 | `src/zetasql/query.py` |
| 11. 코드 품질 도구 | 1일 | `pyproject.toml`, CI 설정 |
| 12. README 개선 | 반나절 | `README.md` |

**완료 시 효과**:
- ✅ 카탈로그 생성이 Java만큼 간결해짐
- ✅ 리소스 관리 자동화
- ✅ 고수준 API로 진입 장벽 낮아짐
- ✅ 테스트 커버리지 향상

---

### Phase 3: Advanced Features (3-4주)
**목표**: Feature parity with Java

| 작업 | 예상 시간 | 파일 |
|------|-----------|------|
| 13. API 문서 (Sphinx) | 3-5일 | `docs/` |
| 14. 쿼리 실행 테스트 | 3-4일 | `tests/test_query_execution.py` |
| 15. TypeFactory | 3-4일 | `src/zetasql/type_factory.py` |
| 16. PreparedQuery API | 3-4일 | `src/zetasql/prepared_query.py` |

**완료 시 효과**:
- ✅ Java와 동등한 기능 수준
- ✅ 전문적인 문서
- ✅ 프로덕션 준비 완료

---

### Phase 4: Polish (1-2주)
**목표**: 프로덕션 품질 마무리

| 작업 | 예상 시간 |
|------|-----------|
| Java-to-Python 마이그레이션 가이드 | 1일 |
| 예제 코드 업데이트 (새 API 사용) | 2일 |
| 성능 벤치마크 | 1일 |
| 릴리스 준비 | 1일 |

---

## 📊 예상 효과

### 코드 가독성
```python
# Before (현재 - proto 직접 조작)
catalog = simple_catalog_pb2.SimpleCatalogProto()
catalog.name = "demo"
table = catalog.table.add()
table.name = "orders"
col = table.column.add()
col.name = "order_id"
col.type.type_kind = type_pb2.TYPE_INT64  # 2 - 매직 넘버!
# 20+ more lines...

# After (Phase 2 완료 후 - Builder + ProtoModel)
catalog = (CatalogBuilder("demo")
    .add_table(
        TableBuilder("orders")
            .add_column("order_id", Types.INT64)  # Type-safe enum
            .add_column("quantity", Types.INT64)
            .build()  # Returns ProtoModel
    )
    .build())  # Returns ProtoModel

# LocalService automatically works with ProtoModel
response = service.analyze(sql="SELECT * FROM orders", simple_catalog=catalog)
resolved = response.resolved_statement  # Already a ProtoModel - no conversion needed!
```

**개선**: 50+ 줄 → 10줄 (80% 감소) + 타입 안정성

---

### 리소스 관리
```python
# Before
service = ZetaSqlLocalService()
reg = service.register_catalog(simple_catalog=catalog)
try:
    response = service.analyze(sql, registered_catalog_id=reg.registered_id)
finally:
    service.unregister_catalog(registered_id=reg.registered_id)

# After
with service.registered_catalog(catalog) as cat:
    response = cat.analyze(sql)
```

**개선**: 명시적 cleanup 불필요

---

### 타입 안정성
```python
# Before
col.type.type_kind = 2  # 이게 뭔 타입?

# After  
col.type.type_kind = Types.INT64  # 명확! IDE 자동완성!
```

---

## 🎯 성공 지표

### 정량적 지표
- ✅ 테스트 커버리지: 37개 → 100+ 개 테스트
- ✅ 코드 라인 수 감소: 예제 코드 30-50% 감소
- ✅ 타입 커버리지: 0% → 80%+ (mypy)
- ✅ 문서 페이지: 1개 (README) → 10+ 페이지

### 정성적 지표
- ✅ 신규 사용자 진입 장벽 대폭 감소
- ✅ Java 개발자들이 쉽게 전환 가능
- ✅ IDE 자동완성으로 API 발견성 향상
- ✅ 에러 메시지 품질 개선

---

## 🚧 의존성 그래프

```
Types Enum (1)
    ├─→ Builder Patterns (6)
    ├─→ TypeFactory (15)
    └─→ Type Tests (7)

py.typed (2) → Type Hints (8)

AnalyzerOptionsFactory (3)
    └─→ High-Level API (10)

Context Manager (9)
    └─→ High-Level API (10)
    └─→ PreparedQuery (16)

All API Improvements (1-16)
    └─→ API Documentation (13)
    └─→ Examples Update
```

---

## 🤝 AI Agent 협업 가이드

### 각 작업의 AI Agent 활용 방안

#### Quick Wins (Phase 1)
1. **Types Enum**: AI가 type_pb2의 모든 상수를 자동 파싱하여 Enum 생성
2. **py.typed**: 단순 파일 생성, 수동 가능
3. **AnalyzerOptionsFactory**: 기존 중복 코드를 AI가 패턴 인식하여 팩토리로 추출
4. **에러 테스트**: AI가 Java 테스트를 참고하여 Python 버전 생성
5. **Quick Start**: AI가 README 구조 분석 후 적절한 위치에 삽입

#### API Improvements (Phase 2)
1. **Builder Patterns**: AI가 protobuf 스키마 분석 → 빌더 API 자동 생성
2. **타입 시스템 테스트**: Java 테스트를 Python으로 변환
3. **타입 힌트**: AI가 메서드 시그니처 분석 → 오버로드 생성
4. **Context Manager**: AI가 try/finally 패턴 인식 → context manager로 변환
5. **High-Level API**: AI가 자주 사용되는 패턴을 helper 메서드로 추출

#### 각 작업 시작 시 제공할 컨텍스트
```
작업: [작업 번호 및 이름]
목표: [이 섹션의 목표 설명 복사]
현재 파일: [관련 파일 경로]
참고 파일: [Java 구현 등 참고할 파일]
예상 코드: [이 문서의 예상 코드 스니펫]
```

---

## 📚 참고 자료

### Java 구현 참고
- [google-zetasql/javatests/com/google/zetasql/](google-zetasql/javatests/com/google/zetasql/) - Java 테스트 예제
- `ResolvedColumnTest.java` - ResolvedColumn 사용 패턴
- `SimpleCatalogTest.java` - Catalog 생성 패턴

### 현재 Python 구현
- [src/zetasql/local_service.py](src/zetasql/local_service.py) - 메인 서비스 API (자동 ProtoModel 반환)
- [src/zetasql/types/proto_model.py](src/zetasql/types/proto_model.py) - ProtoModel 기반 클래스 (MRO 기반 변환)
- [src/zetasql/types/proto_models.py](src/zetasql/types/proto_models.py) - 1,238개 생성된 concrete dataclass (중첩 구조)
- [scripts/generate_proto_models.py](scripts/generate_proto_models.py) - ProtoModel 생성기 (트리 기반)
- [examples/execute_query_demo.py](examples/execute_query_demo.py) - ProtoModel 사용 예제

---

## 📝 작업 체크리스트

작업을 시작할 때 이 섹션을 업데이트하세요:

### Phase 0: ProtoModel System (✅ 완료 - 2025-12-25)
- [x] Concrete dataclass 기반 ProtoModel 구현
- [x] MRO 기반 from_proto/to_proto 자동 변환
- [x] 중첩 클래스 구조 (예: AllowedHintsAndOptions.Hint)
- [x] parse_proto() union type 해소
- [x] LocalService 자동 ProtoModel 반환
- [x] 56개 테스트 (ProtoModel 19개 포함) 통과
- [x] execute_query_demo.py ProtoModel 사용으로 업데이트

### Phase 1: Foundation
- [ ] 1. Types Enum wrapper
- [ ] 2. py.typed marker
- [ ] 3. AnalyzerOptionsFactory  
- [ ] 4. 에러 처리 테스트
- [ ] 5. Quick Start 예제

### Phase 2: API Improvements  
- [ ] 6. Builder Patterns
- [ ] 7. 타입 시스템 테스트
- [ ] 8. 타입 힌트 강화
- [ ] 9. Context Manager
- [ ] 10. High-Level Query API
- [ ] 11. 코드 품질 도구
- [ ] 12. README 개선

### Phase 3: Advanced Features
- [ ] 13. API 레퍼런스 문서
- [ ] 14. 쿼리 실행 테스트
- [ ] 15. TypeFactory
- [ ] 16. PreparedQuery API

### Phase 4: Polish
- [ ] Java-to-Python 마이그레이션 가이드
- [ ] 예제 코드 업데이트
- [ ] 성능 벤치마크
- [ ] 릴리스 준비

---

**작성자**: GitHub Copilot (Claude Sonnet 4.5)  
**마지막 업데이트**: 2025-12-25  
**다음 리뷰**: Phase 1 완료 시
