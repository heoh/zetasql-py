# ZetaSQL-py Architecture

## Overview

zetasql-py is organized into a clear 3-layer architecture that separates core infrastructure, Java-compatible APIs, and Python-specific extensions.

```
zetasql/
├── core/           # Layer 1: WASI Communication & ProtoModel Infrastructure
├── api/            # Layer 2: Java-style Convenience Features
├── extensions/     # Layer 3: Python-specific Extended APIs
├── types/          # ProtoModel Type System (Layer 1 + 2)
└── wasi/           # WebAssembly Resources (External)
```

## Layer 1: Core Infrastructure (zetasql.core)

**Purpose**: Low-level WASM communication and type-safe protobuf abstraction

**Files**:
- `wasm_client.py` - WASM runtime and memory management
- `local_service.py` - Direct wrapper around ZetaSQL LocalService gRPC methods
- `exceptions.py` - Error handling and status codes
- `func_utils.py` - Parameter decorator utilities

**Characteristics**:
- Direct C++/WASM interaction via wasmtime
- ProtoModel-based API (dataclass wrappers for protobufs)
- No domain-specific convenience features
- Essential infrastructure for all higher layers

**Import Example**:
```python
from zetasql.core import ZetaSqlLocalService, StatusCode, ServerError
```

## Layer 2: Java API-style Convenience (zetasql.api)

**Purpose**: Familiar Java-like APIs for users coming from Java ZetaSQL

**Files**:
- `analyzer.py` - Analyzer with static/instance methods (mirrors Java Analyzer)
- `prepared_query.py` - PreparedQuery with builder pattern (mirrors Java PreparedQuery)
- `catalog_registry.py` - RegisteredCatalog context manager (mirrors Java AutoUnregister)
- `builders/`
  - `table_builder.py` - Fluent table builder
  - `catalog_builder.py` - Fluent catalog builder

**Characteristics**:
- Java API parity (static methods, instance methods, builders)
- Method chaining and fluent APIs
- Context managers for resource management (Python idiom)
- Type checking convenience methods

**Import Example**:
```python
from zetasql.api import Analyzer, PreparedQuery, CatalogBuilder, TableBuilder
```

## Layer 3: Extended APIs (zetasql.extensions)

**Purpose**: Python-specific convenience features not present in Java API

**Files**:
- `table_content.py` - Python-friendly factory for table data creation

**Characteristics**:
- Simplifies common Python patterns
- Converts Python native types to ProtoModel
- No Java equivalent

**Future Extensions**:
- DataFrame integration (pandas, polars)
- More Pythonic abstractions
- SQL builder DSL

**Import Example**:
```python
from zetasql.extensions import create_table_content
```

## Type System (zetasql.types)

**Purpose**: Unified type system for all layers

**Files**:
- `proto_model.py` - Base class for ProtoModel system (Layer 1)
- `proto_models.py` - Auto-generated dataclass wrappers (Layer 1) **[GENERATED - DO NOT EDIT]**
- `proto_model_mixins.py` - Domain logic mixins (Layer 1.5/2)
- `type_extensions.py` - Enhanced Type class (Layer 2)
- `type_factory.py` - Factory methods for Type objects (Layer 2)

**Special Note**:
The types package intentionally mixes Layer 1 and Layer 2 to provide a unified namespace. This avoids forcing users to distinguish between generated models and enhanced types.

**Import Example**:
```python
from zetasql.types import (
    # Layer 1: Generated models
    proto_models,
    TypeKind,
    AnalyzerOptions,
    
    # Layer 2: Enhanced types
    Type,
    TypeFactory,
    
    # Layer 1: Core utilities
    ProtoModel,
    parse_proto,
)
```

## WASI Resources (zetasql.wasi)

**Purpose**: WebAssembly binary and generated protobuf code

**Files**:
- `__init__.py` - Utility for locating WASM binary
- `zetasql.wasm` - Compiled ZetaSQL WebAssembly binary (C++ compiled)
- `_pb2/` - Generated Python protobuf code from ZetaSQL .proto files

**Note**: These are external dependencies. Do not modify manually.

## Dependency Rules

**Critical**: Dependencies must flow **upward** through layers only.

```
Layer 3 (extensions)
    ↓ depends on
Layer 2 (api)
    ↓ depends on
Layer 1 (core)
    ↓ depends on
Layer 0 (external: wasi, protobuf, wasmtime)
```

**Allowed**:
- ✅ Layer 2 imports from Layer 1
- ✅ Layer 3 imports from Layer 2 or Layer 1
- ✅ All layers import from types (unified namespace)

**Forbidden**:
- ❌ Layer 1 imports from Layer 2 or 3
- ❌ Layer 2 imports from Layer 3
- ❌ Circular dependencies between layers

**Exception**: types/proto_model_mixins.py has runtime imports from core.local_service and api.catalog_registry to avoid circular dependencies. These are carefully managed using function-level imports.

## Design Patterns

### 1. ProtoModel System

All ZetaSQL protobuf messages are wrapped in dataclass-based ProtoModel classes:

```python
# Generated in proto_models.py
@dataclass
class AnalyzerOptions(ProtoModel):
    _pb_cls: ClassVar = options_pb2.AnalyzerOptions
    language: Optional[LanguageOptions] = None
    ...
    
# Usage
opts = AnalyzerOptions(language=LanguageOptions())
proto = opts.to_proto()  # Convert to protobuf
model = parse_proto(proto)  # Convert back to ProtoModel
```

### 2. Singleton Service

LocalService uses singleton pattern for efficient resource management:

```python
service = ZetaSqlLocalService.get_instance()
```

### 3. Builder Pattern

Fluent APIs for complex object construction:

```python
table = (TableBuilder("users")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .build())
```

### 4. Context Managers

Automatic resource cleanup for server-side resources:

```python
with catalog.register() as catalog_id:
    # Use catalog
    pass  # Auto-unregistered on exit

with PreparedQuery.builder().set_sql(sql).build() as query:
    result = query.execute()
    # Auto-cleaned on exit
```

### 5. Parameter Decorator

Type-safe flexible argument passing:

```python
@parameters(proto_models.AnalyzeRequest)
def analyze(self, *args, **kwargs):
    # Accepts either AnalyzeRequest object or individual kwargs
    request = proto_models.AnalyzeRequest(*args, **kwargs)
    ...
```

## Testing Structure

Tests are organized to mirror the source structure:

```
tests/
├── core/          # Tests for Layer 1 (local_service, etc.)
├── api/           # Tests for Layer 2 (analyzer, prepared_query, builders)
├── extensions/    # Tests for Layer 3 (table_content)
└── types/         # Tests for type system (proto_model, type_factory)
```

## Code Generation

### proto_models.py

Generated by `scripts/generate_proto_models.py`:

```bash
python scripts/generate_proto_models.py
```

**NEVER edit proto_models.py manually**. Regenerate when protobuf definitions change.

## Migration from Old Structure

### Old Import Paths (Deprecated)
```python
# OLD - No longer supported
from zetasql import Analyzer
from zetasql.local_service import ZetaSqlLocalService
from zetasql.builders import TableBuilder
```

### New Import Paths (Current)
```python
# NEW - Use explicit layer paths
from zetasql.api import Analyzer
from zetasql.core import ZetaSqlLocalService
from zetasql.api.builders import TableBuilder
```

## Best Practices

1. **Import from the appropriate layer**:
   - Need WASM access? → `from zetasql.core import ...`
   - Need convenience APIs? → `from zetasql.api import ...`
   - Need Python helpers? → `from zetasql.extensions import ...`
   - Need types? → `from zetasql.types import ...`

2. **Respect dependency direction**:
   - Higher layers can import from lower layers
   - Lower layers should NEVER import from higher layers
   - Use runtime imports if absolutely necessary

3. **Context managers for resources**:
   - Always use context managers for PreparedQuery
   - Always use catalog.register() with context manager

4. **ProtoModel for API**:
   - Use ProtoModel objects, not raw protobufs
   - Let `parse_proto()` handle conversion automatically

5. **Testing**:
   - Place tests in the corresponding layer directory
   - Use fixtures for shared service/catalog setup
   - Test at the appropriate layer (don't test Layer 1 through Layer 2)

## FAQ

**Q: Why keep types/ at the root instead of core/types/?**

A: The types package straddles Layer 1 (proto_model.py, proto_models.py) and Layer 2 (type_extensions.py, type_factory.py). Splitting it would create confusion and force users to know which types are "core" vs "convenience". The unified namespace is more user-friendly.

**Q: Can I add new convenience methods to existing ProtoModel classes?**

A: Yes, use mixins in proto_model_mixins.py. The generator will apply them during generation. See TypeKindMixin for examples.

**Q: Why are there runtime imports in proto_model_mixins.py?**

A: To avoid circular dependencies. LanguageOptionsMixin needs local_service, but local_service imports proto_models which includes LanguageOptions. Runtime imports (inside methods) break the cycle.

**Q: Should I use ZetaSqlLocalService directly or go through higher-level APIs?**

A: Depends on your needs:
- **Typical usage**: Use Layer 2 APIs (Analyzer, PreparedQuery) for convenience
- **Advanced usage**: Use ZetaSqlLocalService directly when you need precise control
- **Library development**: Use core layer when building new abstractions

**Q: How do I add a new Python-specific helper?**

A: Add it to `extensions/`. Examples:
- DataFrame converters: `extensions/dataframe_utils.py`
- SQL builders: `extensions/query_builder.py`
- Result formatters: `extensions/result_formatters.py`

---

**Last Updated**: 2025-12-27
