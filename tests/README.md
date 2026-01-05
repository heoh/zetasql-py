# ZetaSQL-py Test Suite

This test suite mirrors the Java ZetaSQL test structure and provides comprehensive coverage of the Python API.

## Test Structure

```
tests/
├── conftest.py                      # Global fixtures (service, options, etc.)
├── test_analyzer.py                 # ✅ Analyzer API (Java: AnalyzerTest.java)
├── test_script_analysis.py          # ⏸️  Script analysis (multi-statement)
├── test_catalog_registry.py         # ✅ Catalog registration
│
├── catalog/                         # SimpleCatalog operations
│   ├── conftest.py                 # Catalog-specific fixtures
│   ├── test_catalog_basic.py      # ✅ Basic catalog ops (Java: SimpleCatalogTest.java)
│   ├── test_table_operations.py   # ✅ Table add/get operations
│   ├── test_function_operations.py # ⏸️  SKIP - Functions (API not implemented)
│   ├── test_tvf_operations.py     # ⏸️  SKIP - TVFs (API not implemented)
│   └── test_constant_operations.py # ⏸️  SKIP - Constants (API not implemented)
│
├── builders/                        # Builder pattern tests
│   ├── test_table_builder.py      # ✅ TableBuilder
│   └── test_catalog_builder.py    # ✅ CatalogBuilder
│
├── execution/                       # Query execution tests
│   ├── test_prepared_query.py     # ✅ PreparedQuery (Java: PreparedQueryTest.java)
│   ├── test_prepared_expression.py # ⏸️  Expression evaluation (API not implemented)
│   └── test_value.py              # ⏸️  Value system (API not implemented)
│
├── integration/                     # End-to-end workflows
│   └── test_analysis_workflows.py # ✅ Complete analysis scenarios
│
├── core/                           # Low-level service tests
│   └── test_local_service.py      # ✅ LocalService gRPC methods
│
├── extensions/                     # Python extensions
│   └── test_table_content.py      # ✅ TableContent helpers
│
└── types/                          # Type system tests
    ├── test_type_factory.py       # ✅ TypeFactory API
    ├── test_type_extensions.py    # ✅ Type extensions
    └── test_enum_intenum.py       # ✅ IntEnum support
```

## Test Categories

### ✅ **Implemented & Passing (157 tests)**
- `test_analyzer.py` - All Analyzer methods (analyze, build, extract)
- `test_catalog_registry.py` - Catalog registration and context managers
- `catalog/test_catalog_basic.py` - Catalog creation and registration
- `catalog/test_table_operations.py` - Table operations (via builders)
- `builders/` - TableBuilder and CatalogBuilder
- `execution/test_prepared_query.py` - Query execution
- `integration/test_analysis_workflows.py` - Real-world scenarios
- `core/test_local_service.py` - Low-level LocalService methods
- `extensions/test_table_content.py` - TableContent helpers
- `types/` - Type system (TypeFactory, extensions, IntEnum)

### ⏸️ **Skipped (API Not Implemented - 91 tests)**

**Priority 1: Catalog Operations (43 tests)**
- `catalog/test_function_operations.py` - Need: `SimpleCatalog.add_function()`, `FunctionBuilder`
- `catalog/test_tvf_operations.py` - Need: `SimpleCatalog.add_table_valued_function()`, `TVFBuilder`
- `catalog/test_constant_operations.py` - Need: `SimpleCatalog.add_constant()`, `ConstantBuilder`

**Priority 2: Script Analysis (11 tests)**
- `test_script_analysis.py` - Multi-statement parsing, script validation, formatting
  - Script iteration API
  - Error handling with position tracking
  - Metadata extraction
  - Statement boundary detection

**Priority 3: Execution Features (34 tests)**
- `execution/test_prepared_expression.py` - Expression evaluation with parameters
  - PreparedExpression class
  - Parameter binding
  - Batch evaluation
  - Expression reuse
- `execution/test_value.py` - Value system for typed results
  - Value creation (int64, string, bool, etc.)
  - Complex types (arrays, structs)
  - Value comparison and equality
  - Serialization and SQL literals

**Other (4 tests)**
- Expression analysis with node_kind inspection
- Multi-statement parsing edge cases

## Mapping to Java Tests

| Python Test | Java Test | Status | Notes |
|------------|-----------|--------|-------|
| `test_analyzer.py` | `AnalyzerTest.java` | ✅ Complete | All analyze/build/extract methods |
| `test_script_analysis.py` | `ScriptAnalyzer` | ⏸️ Skip | Multi-statement parsing |
| `test_catalog_registry.py` | (N/A) | ✅ Complete | Context managers |
| `catalog/test_catalog_basic.py` | `SimpleCatalogTest.java` | ✅ Partial | Basic ops only |
| `catalog/test_table_operations.py` | `SimpleTableTest.java` | ✅ Complete | Table add/get |
| `catalog/test_function_operations.py` | `FunctionTest.java` | ⏸️ Skip | API not implemented |
| `catalog/test_tvf_operations.py` | `TableValuedFunctionTest.java` | ⏸️ Skip | API not implemented |
| `builders/test_table_builder.py` | (N/A - Python only) | ✅ Complete | Fluent builder API |
| `builders/test_catalog_builder.py` | (N/A - Python only) | ✅ Complete | Fluent builder API |
| `execution/test_prepared_query.py` | `PreparedQueryTest.java` | ✅ Complete | Query execution |
| `execution/test_prepared_expression.py` | `PreparedExpression.java` | ⏸️ Skip | Expression evaluation |
| `execution/test_value.py` | `Value.java` | ⏸️ Skip | Value system |
| `integration/test_analysis_workflows.py` | (N/A - new) | ✅ Complete | Real scenarios |
| `core/test_local_service.py` | (N/A - Python only) | ✅ Complete | Low-level service |
| `extensions/test_table_content.py` | (N/A - Python only) | ✅ Complete | Helper extensions |
| `types/test_type_factory.py` | (N/A - Python only) | ✅ Complete | Type creation |

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run specific category
```bash
pytest tests/test_analyzer.py
pytest tests/catalog/
pytest tests/builders/
pytest tests/integration/
```

### Run only passing tests (exclude skipped)
```bash
pytest tests/ -v
```

### Run with coverage
```bash
pytest tests/ --cov=zetasql --cov-report=html
```

## Test Design Principles

### 1. **Java API Parity**
Tests mirror Java test structure and naming conventions for easy cross-reference.

### 2. **Concrete Assertions**
Instead of:
```python
assert stmt is not None  # ❌ Too vague
```

We use:
```python
assert isinstance(stmt, ResolvedQueryStmt)
assert len(stmt.output_column_list) == 3
assert stmt.output_column_list[0].name == "customer_id"
```

### 3. **Future API Definition**
Skipped tests define the expected API for future implementation:
```python
@pytest.mark.skip(reason="API not implemented: SimpleCatalog.add_function()")
def test_add_function(self):
    """Expected API:
        function = FunctionBuilder("MY_UDF").add_signature(...).build()
        catalog.add_function(function)
    """
    ...
```

### 4. **Shared Fixtures**
- `tests/conftest.py` - Global fixtures (service, options)
- `tests/catalog/conftest.py` - Catalog-specific fixtures
- Session-scoped for expensive resources

### 5. **Complete Coverage**
Even unimplemented features have tests showing ideal usage:
- **156 passing tests** - Current working functionality
- **92 skipped tests** - Roadmap for future implementation
- **0 failing tests** - All tests are intentional

## Test Statistics

```
Total Tests: 248
├── ✅ Passing: 157 (63%)
├── ⏸️  Skipped: 91 (37%)
└── ❌ Failing: 0 (0%)

Distribution by Category:
├── Analyzer & Script: 39 tests (28 pass, 11 skip)
├── Catalog Operations: 61 tests (18 pass, 43 skip)
├── Builders: 21 tests (21 pass, 0 skip)
├── Execution: 58 tests (12 pass, 46 skip)
├── Integration: 10 tests (10 pass, 0 skip)
├── Core: 24 tests (24 pass, 0 skip)
├── Extensions: 12 tests (12 pass, 0 skip)
└── Types: 42 tests (42 pass, 0 skip)
```

## Removed Tests

The following ProtoModel internal tests were removed (user-facing API not affected):
- `test_proto_model_basic.py` - Internal ProtoModel mechanics
- `test_proto_model_chaining.py` - MRO and type casting internals
- `test_proto_model_utils.py` - ProtoModel utilities
- `test_concrete_proto_model.py` - ProtoModel construction details
- `test_nested_messages.py` - Nested proto message handling
- `test_options.py` - Options proto specifics

**Rationale**: These tests focused on ProtoModel implementation details rather than user-facing API. The remaining type tests (`test_type_factory.py`, etc.) cover the public API adequately.

## Adding New Tests

### For New Features
1. Check Java equivalent test (if exists)
2. Add to appropriate directory (`catalog/`, `builders/`, etc.)
3. Use skip markers for unimplemented APIs
4. Follow concrete assertion pattern

### Example: Adding PreparedExpression tests
```python
# tests/execution/test_prepared_expression.py

@pytest.mark.skip(reason="API not implemented: PreparedExpression class")
class TestPreparedExpression:
    def test_execute_with_parameters(self):
        """Expected API:
            expr = PreparedExpression("@param1 + @param2")
            result = expr.execute(params={"param1": 10, "param2": 20})
        """
        ...
```

## Test Maintenance

### When Adding New API
1. Find skipped test for that API
2. Remove `@pytest.mark.skip`
3. Verify test passes
4. Update this README

### When Changing API
1. Update affected tests
2. Ensure Java parity maintained
3. Update skip reasons if needed
4. Run full test suite

## Coverage Goals

- **Current**: ~63% test passing rate (157/248)
- **Core Analysis**: 100% coverage (all passing)
- **Builders**: 100% coverage (all passing)
- **Type System**: 100% coverage (all passing)
- **Target**: 80%+ overall (after implementing Priority 1 catalog operations)

**Focus Areas for Implementation:**
1. **Priority 1**: Catalog operations (functions, TVFs, constants) - 43 tests waiting
2. **Priority 2**: Script analysis - 11 tests waiting
3. **Priority 3**: Execution features (PreparedExpression, Value) - 34 tests waiting

## Questions?

See:
- Java tests: `.external/google-zetasql/javatests/com/google/zetasql/`
- Implementation: `src/zetasql/`
- Examples: `examples/`
