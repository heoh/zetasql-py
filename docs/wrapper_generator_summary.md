# ResolvedAST Wrapper Generator - Implementation Summary

## Overview
Automatically generates Python wrapper classes for ZetaSQL proto messages with real inheritance, eliminating deep parent chain access patterns.

## Problem Statement
ZetaSQL proto messages use `parent` fields to simulate inheritance:
```protobuf
message ResolvedLiteralProto {
  ResolvedExprProto parent = 1;  // Contains ResolvedNodeProto parent
  ValueWithTypeProto value = 2;
  // ... other fields
}
```

This creates deep access patterns:
```python
type_kind = literal.parent.type.type_kind  # 2 levels
parse_loc = literal.parent.parent.parse_location_range  # 3 levels
```

## Solution
Generate Python wrapper classes with real inheritance that mirror the proto parent chain structure:
```python
class ResolvedNode:
    parse_location_range: ParseLocationRangeProto

class ResolvedExpr(ResolvedNode):
    type: TypeProto

class ResolvedLiteral(ResolvedExpr):
    value: ValueWithTypeProto
```

Result:
```python
literal = ResolvedLiteral(proto)
literal.type  # Direct access via inheritance
literal.parse_location_range  # Works!
isinstance(literal, ResolvedExpr)  # True
```

## Implementation

### Generator: `scripts/generate_wrappers.py`

**4-Stage Inheritance Extraction:**

1. **Collection** - Load all 947 proto message classes from 66 `_pb2.py` files
2. **Parent Detection** - Extract parent relationships via `DESCRIPTOR.fields_by_name['parent']`
3. **Graph Building** - Construct parent→children relationships
4. **Field Flattening** - Compute all inherited fields for each class

**Key Functions:**

- `extract_inheritance_graph()`: Main algorithm
  - Scans: `src/zetasql/wasi/_pb2/zetasql/**/*_pb2.py`
  - Extracts: parent field → parent message type
  - Builds: Complete 947-node inheritance graph
  - Computes: Depth-first field accumulation

- `generate_property()`: Creates `@cached_property` with correct parent chain
  - Reserved keyword handling: `lambda` → `lambda_`
  - Proto access escaping: `getattr(proto, 'lambda')` for reserved words
  - Parent chain calculation: Finds correct `.parent.parent...` depth

- `generate_class()`: Outputs wrapper class with all fields
  - Inheritance declaration: `class Child(Parent):`
  - Field generation: Inherited fields with parent chain, own fields direct
  - Type hints: Full TYPE_CHECKING imports for IDE support

### Generated File: `src/zetasql/resolved_ast_wrapper.py`

**Statistics:**
- 947 wrapper classes
- 28,375 lines
- 863,787 characters

**Structure:**
```python
from __future__ import annotations
from functools import cached_property
from typing import Optional, List, TYPE_CHECKING

class ResolvedLiteral(ResolvedExpr):
    def __init__(self, proto: 'ResolvedLiteralProto'):
        self._proto = proto
    
    # Inherited from ResolvedNode (2 levels up)
    @cached_property
    def parse_location_range(self) -> Optional['ParseLocationRangeProto']:
        return self._proto.parent.parent.parse_location_range
    
    # Inherited from ResolvedExpr (1 level up)
    @cached_property
    def type(self) -> Optional['TypeProto']:
        return self._proto.parent.type
    
    # Own fields (direct access)
    @cached_property
    def value(self) -> Optional['ValueWithTypeProto']:
        return self._proto.value
```

## Technical Details

### Reserved Keyword Handling
Python keywords like `lambda` are escaped:
- Method name: `lambda_`
- Proto access: `getattr(self._proto, 'lambda')`
- Docstring: Notes the escape

### Inheritance Strategy
Each class stores only its own proto, but generates properties for ALL fields:
- **Own fields**: `self._proto.field`
- **Parent fields**: `self._proto.parent.field`
- **Grandparent fields**: `self._proto.parent.parent.field`

This approach:
- ✅ Enables real Python `isinstance()` checks
- ✅ Provides IDE autocompletion for all inherited properties
- ✅ Uses `@cached_property` for efficient lazy evaluation
- ✅ Maintains proper parent chain access through proto

### Topological Sorting
Classes generated in depth-first order (parents before children) to avoid forward references.

### Cross-File Dependencies
Handles proto messages split across files:
- `ResolvedNodeProto` in `serialization_pb2.py`
- `ResolvedExprProto` in `resolved_ast_pb2.py`
- Full module scanning ensures complete graph

## Usage

### Basic Usage
```python
from zetasql.wasi._pb2.zetasql.resolved_ast import resolved_ast_pb2
from zetasql.resolved_ast_wrapper import ResolvedLiteral

# Create proto
proto = resolved_ast_pb2.ResolvedLiteralProto()
proto.has_explicit_type = True
proto.parent.type.type_kind = 1
proto.parent.parent.parse_location_range.start = 0

# Wrap it
literal = ResolvedLiteral(proto)

# Access fields naturally
print(literal.has_explicit_type)  # Own field
print(literal.type.type_kind)  # Inherited from ResolvedExpr
print(literal.parse_location_range.start)  # Inherited from ResolvedNode

# Type checking works
assert isinstance(literal, ResolvedLiteral)
assert isinstance(literal, ResolvedExpr)
assert isinstance(literal, ResolvedNode)
```

### Regenerating After Proto Changes
```bash
python scripts/generate_wrappers.py
```

This will:
1. Scan all `_pb2.py` files in `src/zetasql/wasi/_pb2`
2. Extract parent relationships
3. Build complete inheritance graph
4. Generate `src/zetasql/resolved_ast_wrapper.py` with all 947 classes

## Testing

Test coverage in `tests/test_wrapper.py`:
- ✅ Direct property access (own fields)
- ✅ Inherited property access (1 level)
- ✅ Deep inherited property access (2 levels)
- ✅ `isinstance()` type checking
- ✅ IDE autocompletion (via type hints)

Run tests:
```bash
python tests/test_wrapper.py
```

## Design Philosophy

Matches Google's approach in C++:
- C++ ZetaSQL uses `AddNode(parent='X')` to generate inheritance
- Python wrapper generator uses `parent` field to reconstruct that inheritance
- Result: Same logical structure in Python as in C++

## Performance

- `@cached_property`: First access computes value, subsequent accesses return cached result
- No upfront cost: Properties computed only when accessed
- Memory efficient: Stores single proto, not duplicated parent data

## Limitations & Future Work

**Current:**
- Manual wrapper import: `from zetasql.resolved_ast_wrapper import X`
- Proto → Wrapper: Manual `ResolvedLiteral(proto)` call

**Potential enhancements:**
- Auto-wrapping utilities: `auto_wrap(proto)` with type registry
- Deserializer: `from_bytes(serialized_data)` → wrapped object
- Bidirectional sync: Wrapper changes → proto updates

## Files Changed

1. **Created:**
   - `scripts/generate_wrappers.py` - Generator script (396 lines)
   - `src/zetasql/resolved_ast_wrapper.py` - Generated wrappers (28,375 lines)
   - `tests/test_wrapper.py` - Test suite

2. **Modified:**
   - `README.md` - Added usage documentation

## Conclusion

Successfully implemented an automated wrapper generator that transforms ZetaSQL's proto parent chains into idiomatic Python inheritance, providing:

- ✨ Clean API: `literal.type` instead of `literal.parent.type`
- 🔍 Type safety: Full type hints for IDE support
- ⚡ Performance: Lazy evaluation with `@cached_property`
- 🔄 Maintainability: Automated regeneration from proto files
- 🐍 Pythonic: Real inheritance, `isinstance()` checks work

The generator is now production-ready and can be rerun whenever proto files change.
