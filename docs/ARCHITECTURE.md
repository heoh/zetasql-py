# Architecture

Deep dive into ZetaSQL Python's architecture, design decisions, and implementation details.

## Table of Contents

- [Overview](#overview)
- [Layer Architecture](#layer-architecture)
- [ProtoModel System](#protomodel-system)
- [WASM Integration](#wasm-integration)
- [Design Decisions](#design-decisions)
- [Performance Considerations](#performance-considerations)
- [Extending the Library](#extending-the-library)

---

## Overview

ZetaSQL Python is a Python port of Google's ZetaSQL that brings SQL analysis capabilities to Python applications. The library uses WebAssembly (WASM) to run the C++ ZetaSQL implementation while providing a Pythonic API layer.

### Key Goals

1. **Pythonic API**: Familiar builder patterns and fluent interfaces
2. **Type Safety**: Full type hints for IDE support
3. **Performance**: Efficient WASM communication
4. **Compatibility**: Mirror Java ZetaSQL API where appropriate
5. **Maintainability**: Auto-generated code where possible

---

## Layer Architecture

The library is organized into three distinct layers:

```
┌─────────────────────────────────────────┐
│         Layer 2: API (zetasql.api)      │
│  High-level convenience features        │
│  - Analyzer, PreparedQuery, Builders    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│       Layer 1: Core (zetasql.core)      │
│  WASM communication & ProtoModel        │
│  - ZetaSqlLocalService                  │
│  - ProtoModel infrastructure            │
│  - Exception handling                   │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│       Layer 0: WASI (zetasql.wasi)      │
│  WebAssembly resources                  │
│  - WASM binary (*.wasm)                 │
│  - Generated protobuf definitions       │
│  - Low-level WASI interface             │
└─────────────────────────────────────────┘
```

### Layer 0: WASI

**Location:** `src/zetasql/wasi/`

The foundation layer containing:
- **WASM Binary**: Pre-compiled ZetaSQL C++ implementation
- **Protobuf Definitions**: Auto-generated `_pb2.py` files from `.proto` sources
- **WASI Client**: Low-level interface to WASM runtime

**Key Files:**
- `*.wasm` - ZetaSQL compiled to WebAssembly
- `_pb2/*.py` - Generated protobuf Python code
- `proto/` - Original `.proto` definitions

**Characteristics:**
- Fully auto-generated (never edit manually)
- Direct protobuf compatibility
- Minimal Python logic

### Layer 1: Core

**Location:** `src/zetasql/core/`

The infrastructure layer that bridges WASM and high-level APIs:

#### ZetaSqlLocalService

**File:** `local_service.py`

Singleton service managing WASM communication:

```python
class ZetaSqlLocalService:
    @classmethod
    def get_instance(cls) -> "ZetaSqlLocalService":
        """Get singleton instance."""
        
    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        """Low-level SQL analysis."""
        
    def evaluate(self, request: EvaluateRequest) -> EvaluateResponse:
        """Low-level query execution."""
```

**Responsibilities:**
- WASM lifecycle management
- gRPC-style method invocation
- Protobuf serialization/deserialization
- Resource management

#### ProtoModel System

**Files:** `proto_model/`, `types/`

Pythonic wrapper around protobuf messages:

```python
@dataclass
class ResolvedLiteral(ResolvedExpr):
    """Wrapper with real inheritance."""
    value: Optional[ValueWithType] = None
    has_explicit_type: bool = False
    
    @classmethod
    def from_proto(cls, proto: ResolvedLiteralProto) -> "ResolvedLiteral":
        """Create from protobuf message."""
        
    def to_proto(self) -> ResolvedLiteralProto:
        """Convert to protobuf message."""
```

**Benefits:**
- Real Python inheritance (no parent chains)
- IDE autocomplete support
- Type hints throughout
- Bidirectional proto conversion

#### Exception Handling

**File:** `exceptions.py`

```python
class ZetaSQLError(Exception):
    """Base exception for all ZetaSQL errors."""
```

### Layer 2: API

**Location:** `src/zetasql/api/`

High-level convenience layer with user-facing APIs:

#### Analyzer

**File:** `analyzer.py`

Main entry point for SQL analysis:

```python
class Analyzer:
    def __init__(self, options, catalog=None, service=None):
        """Initialize with options and catalog."""
        
    def analyze_statement(self, sql: str) -> ResolvedStatement:
        """Analyze SQL statement."""
        
    @staticmethod
    def analyze_statement_static(sql, options, catalog):
        """Static method version."""
```

**Design Philosophy:**
- Both instance and static methods (Java-style)
- Convenience wrappers over LocalService
- Error message enhancement

#### Builders

**Files:** `builders/*.py`

Fluent builder pattern for constructing ZetaSQL objects:

```python
class CatalogBuilder:
    def __init__(self, name: str):
        self._catalog = SimpleCatalog(name=name)
        
    def add_table(self, table: SimpleTable) -> Self:
        self._catalog.table.append(table)
        return self
        
    def build(self) -> SimpleCatalog:
        return self._catalog
```

**Builders Provided:**
- `CatalogBuilder` - Build catalogs
- `TableBuilder` - Build tables
- `FunctionBuilder` - Build functions
- `SignatureBuilder` - Build function signatures
- `TVFBuilder` - Build table-valued functions
- `ConstantBuilder` - Build constants

#### PreparedQuery & PreparedExpression

**Files:** `prepared_query.py`, `prepared_expression.py`

Execution layer with parameter binding:

```python
class PreparedQuery:
    def execute(self, parameters=None, table_content=None):
        """Execute with parameters and data."""
        
    @classmethod
    def builder(cls) -> "PreparedQueryBuilder":
        """Get builder instance."""
        
    def __enter__(self):
        """Context manager support."""
```

**Features:**
- Parameter binding
- Table data injection
- Builder pattern
- Context manager support

#### Value API

**File:** `value.py`

Type-safe value creation and manipulation:

```python
class Value:
    @staticmethod
    def int64(value: int) -> "Value":
        """Create INT64 value."""
        
    @staticmethod
    def array(elements: list["Value"]) -> "Value":
        """Create array value."""
        
    def coerce_to(self, target_type: TypeKind) -> "Value":
        """Implicit type conversion."""
```

---

## ProtoModel System

### Problem: Protobuf Parent Chains

ZetaSQL protobuf messages use parent field chains for inheritance:

```protobuf
message ResolvedLiteralProto {
  optional ResolvedExprProto parent = 1;
  optional Value value = 2;
}

message ResolvedExprProto {
  optional ResolvedNodeProto parent = 1;
  optional TypeProto type = 2;
}

message ResolvedNodeProto {
  optional ParseLocationRange parse_location_range = 1;
}
```

This leads to cumbersome access in Python:

```python
# Deep nesting required
literal_proto = ResolvedLiteralProto()
type_kind = literal_proto.parent.type.type_kind        # 😞
location = literal_proto.parent.parent.parse_location_range  # 😞😞
```

### Solution: ProtoModel Wrappers

Auto-generated Python dataclasses with real inheritance:

```python
@dataclass
class ResolvedNode:
    parse_location_range: Optional[ParseLocationRange] = None

@dataclass
class ResolvedExpr(ResolvedNode):
    type: Optional[Type] = None

@dataclass
class ResolvedLiteral(ResolvedExpr):
    value: Optional[ValueWithType] = None
```

Now access is direct:

```python
literal = ResolvedLiteral(...)
type_kind = literal.type.type_kind        # ✨ Direct
location = literal.parse_location_range   # ✨ Inherited
```

### Generation Process

**Script:** `scripts/generate_proto_models.py`

1. **Scan**: Discover all `_pb2.py` files
2. **Parse**: Extract message definitions and parent relationships
3. **Build Graph**: Construct inheritance hierarchy
4. **Generate**: Create dataclass-based models
5. **Write**: Output to `types/proto_model/generated.py`

**To Regenerate:**
```bash
python scripts/generate_proto_models.py \
    --proto-dir src/zetasql/wasi/_pb2 \
    --output src/zetasql/types/proto_model/generated.py
```

### Conversion Methods

Every ProtoModel class has:

```python
@classmethod
def from_proto(cls, proto: ProtoClass) -> "ModelClass":
    """Create model from protobuf message."""
    # Automatically handles parent chain flattening
    
def to_proto(self) -> ProtoClass:
    """Convert model to protobuf message."""
    # Automatically reconstructs parent chains
```

---

## WASM Integration

### Why WASM?

ZetaSQL is implemented in C++ and WASM provides:

1. **Portability**: Run C++ code in Python without native compilation
2. **Safety**: Sandboxed execution environment
3. **Performance**: Near-native speed
4. **Simplicity**: Single binary, no platform-specific builds

### WASI Runtime

**Library Used:** `wasmtime-py`

```python
from zetasql.core.wasm_client import WasmClient

client = WasmClient(wasm_path)
result = client.call_grpc_func("MethodName", request_proto, response_proto_class)
```

### Communication Flow

```
Python Layer
    ↓
ZetaSqlLocalService.analyze(request: AnalyzeRequest)
    ↓
WasmClient.call_grpc_func("ZetaSqlLocalService_Analyze", ...)
    ↓
Serialize request to protobuf bytes
    ↓
WASM binary execution
    ↓
Deserialize response from protobuf bytes
    ↓
Parse to ProtoModel
    ↓
Return to user
```

### Performance Optimization

1. **Singleton Service**: Reuse WASM instance across calls
2. **Lazy Loading**: Load WASM on first use
3. **Minimal Copies**: Direct protobuf serialization
4. **Streaming**: Support for large responses

---

## Design Decisions

### Why Three Layers?

**Separation of Concerns:**
- Layer 0: Platform interface (WASM/Proto)
- Layer 1: Python infrastructure (ProtoModel, Service)
- Layer 2: User-facing API (Convenience features)

**Benefits:**
- Clear abstraction boundaries
- Easy to test each layer independently
- Users can choose API level based on needs

### Why Builder Pattern?

**Motivation:**
- Java ZetaSQL uses builders extensively
- Immutable objects with validation
- Fluent, readable code

**Example:**
```python
# Without builder (verbose, error-prone)
catalog = SimpleCatalog()
catalog.name = "mydb"
catalog.table.append(users_table)
catalog.table.append(orders_table)
catalog.builtin_function_options = builtin_opts

# With builder (clean, fluent)
catalog = (
    CatalogBuilder("mydb")
    .add_table(users_table)
    .add_table(orders_table)
    .with_builtin_functions(builtin_opts)
    .build()
)
```

### Why Both Static and Instance Methods?

**Analyzer Design:**
```python
# Instance method - reuse configuration
analyzer = Analyzer(options, catalog)
stmt1 = analyzer.analyze_statement(sql1)
stmt2 = analyzer.analyze_statement(sql2)

# Static method - one-off analysis
stmt = Analyzer.analyze_statement_static(sql, options, catalog)
```

**Rationale:**
- Instance: Convenient for multiple operations
- Static: Convenient for single operations
- Mirrors Java API for familiarity

### Why ProtoModel Instead of Direct Protobuf?

**Protobuf Issues:**
1. Parent field chains
2. No real inheritance
3. Mutable by default
4. Awkward Python integration

**ProtoModel Benefits:**
1. Real Python inheritance
2. Dataclass-based (immutable-friendly)
3. IDE autocomplete support
4. Type hints throughout
5. Bidirectional conversion

---

## Performance Considerations

### WASM Overhead

**Cold Start:**
- First call: ~100-500ms (WASM initialization)
- Subsequent calls: <1ms overhead

**Mitigation:**
- Use singleton service
- Reuse Analyzer instances
- Batch operations when possible

### Protobuf Serialization

**Cost:** Serialization/deserialization on every WASM call

**Optimization:**
- Use ProtoModel efficiently (lazy conversion)
- Minimize roundtrips
- Cache analysis results when appropriate

### Memory Management

**WASM Memory:**
- Isolated from Python heap
- Automatically managed by wasmtime

**Python Memory:**
- ProtoModel objects are regular Python objects
- Standard garbage collection applies

---

## Extending the Library

### Adding New Builders

Create a new builder following the pattern:

```python
# src/zetasql/api/builders/new_builder.py
from typing_extensions import Self
from zetasql.types import NewProtoModel

class NewBuilder:
    def __init__(self, name: str):
        self._model = NewProtoModel(name=name)
        
    def with_property(self, value: Any) -> Self:
        self._model.property = value
        return self
        
    def build(self) -> NewProtoModel:
        return self._model
```

### Adding New API Methods

Extend Analyzer or create new API classes:

```python
# src/zetasql/api/analyzer.py
class Analyzer:
    def new_feature(self, input: str) -> Result:
        """New analysis feature."""
        request = NewRequest(sql=input, options=self.options.to_proto())
        response = self.service.new_method(request)
        return parse_proto(response.result)
```

### Adding Custom Functions

Register custom functions in catalog:

```python
from zetasql.api import FunctionBuilder, SignatureBuilder

my_func = (
    FunctionBuilder("my_custom_func")
    .add_signature(signature)
    .build()
)

catalog = CatalogBuilder("db").add_function(my_func).build()
```

### Regenerating ProtoModels

After updating proto files:

```bash
# 1. Rebuild proto files (if needed)
./scripts/build_protos.sh

# 2. Regenerate ProtoModels
python scripts/generate_proto_models.py \
    --proto-dir src/zetasql/wasi/_pb2 \
    --output src/zetasql/types/proto_model/generated.py

# 3. Run tests
pytest
```

---

## Testing Strategy

### Unit Tests

**Location:** `tests/`

**Categories:**
- API tests (`test_analyzer.py`, etc.)
- Builder tests (`builders/test_*_builder.py`)
- Execution tests (`execution/test_*.py`)
- Integration tests (`integration/test_*.py`)

**Pattern:**
```python
def test_feature():
    # Setup
    catalog = CatalogBuilder("test").build()
    analyzer = Analyzer(options, catalog)
    
    # Execute
    result = analyzer.analyze_statement("SELECT 1")
    
    # Verify
    assert result is not None
    assert isinstance(result, ResolvedQueryStmt)
```

### Integration Tests

**Purpose:** Test complete workflows

**Examples:**
- Catalog building → Analysis → SQL building
- Query preparation → Execution → Result processing
- Script analysis → Validation → Statement extraction

### Test Fixtures

**Location:** `tests/conftest.py`

Shared fixtures for common setup:
```python
@pytest.fixture
def options():
    return AnalyzerOptions()

@pytest.fixture
def catalog():
    return CatalogBuilder("test").build()
```

---

## Future Directions

### Planned Features

1. **Async API**: Async/await support for analysis and execution
2. **Streaming**: Support for streaming large results
3. **Caching**: Analysis result caching
4. **More Builders**: Additional builder patterns as needed
5. **Performance**: Further WASM optimization

### Contribution Areas

- Additional examples and documentation
- Performance benchmarks
- Integration with popular data tools
- Bug fixes and error message improvements

---

## See Also

- [Getting Started Guide](GETTING_STARTED.md)
- [API Reference](API_REFERENCE.md)
- [Examples](EXAMPLES.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
