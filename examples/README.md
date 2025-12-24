# ZetaSQL LocalService + Wrapper Examples

This directory contains comprehensive examples demonstrating how to use ZetaSQL LocalService with the generated wrapper classes.

## Examples Overview

### 1. `basic_usage.py` - Fundamental Operations
Basic ZetaSQL operations with wrapper classes:
- **Parse**: Parse SQL and examine AST structure
- **Analyze**: Analyze queries with catalog and examine resolved AST
- **Extract Table Names**: Extract table dependencies from queries
- **Format SQL**: Auto-format SQL with proper indentation
- **Multi-Statement Analysis**: Process scripts with multiple statements
- **Wrapper Navigation**: Navigate resolved AST using wrapper classes
- **Type Resolution**: Use `resolve_type()` to handle union types automatically

```bash
python examples/basic_usage.py
```

**Key Concepts:**
- Creating and registering catalogs
- Working with SimpleCatalogProto and SimpleTableProto
- Using ResolvedQueryStmt wrapper for clean AST access
- Type hints and IDE autocompletion benefits
- Using `resolve_type()` and `node_kind()` utilities for type handling

**New Utilities:**
```python
from zetasql.wrapper_utils import resolve_type, node_kind

# Automatically resolve union types to concrete types
scan = resolve_type(scan)  # AnyResolvedScan -> ResolvedFilterScan

# Get the concrete type name
print(node_kind(scan))  # 'ResolvedFilterScan'
```

---

### 2. `advanced_analysis.py` - Query Analysis & Optimization
Advanced query analysis techniques:
- **Query Complexity Analyzer**: Measure query complexity by counting operations
- **SQL Validator**: Validate queries and provide error diagnostics
- **Query Rewriter**: Parse and reformat queries
- **Expression Type Analyzer**: Examine expression types in resolved AST
- **Table Dependency Graph**: Extract and visualize table dependencies
- **Cost Estimator**: Estimate query cost based on operations

```bash
python examples/advanced_analysis.py
```

**Key Techniques:**
- Recursive scan tree traversal
- Operation counting and complexity scoring
- Type system analysis
- Cost-based query analysis

---

### 3. `testing_debugging.py` - Testing & QA Utilities
SQL testing and debugging workflows:
- **SQL Test Suite**: Automated query validation test cases
- **Query Debugger**: Deep dive into resolved AST structure
- **Query Comparison**: Compare queries for semantic equivalence
- **Performance Profiler**: Profile different query patterns
- **Regression Tester**: Regression test suite for SQL queries
- **Schema Validator**: Validate schema changes don't break queries

```bash
python examples/testing_debugging.py
```

**Use Cases:**
- Continuous integration testing
- Query debugging and optimization
- Schema migration validation
- Performance regression detection

---

## Common Patterns

### Setting Up a Catalog

```python
from zetasql.local_service import ZetaSqlLocalService
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2, options_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2, options_pb2 as public_options_pb2

def create_analyzer_options():
    """Create analyzer options with builtin functions enabled."""
    opts = options_pb2.AnalyzerOptionsProto()
    
    language_options = opts.language_options
    language_options.name_resolution_mode = public_options_pb2.NAME_RESOLUTION_DEFAULT
    language_options.product_mode = public_options_pb2.PRODUCT_INTERNAL
    
    # Enable all language features (for SUM, WHERE, JOIN, etc.)
    for feature in dir(public_options_pb2):
        if feature.startswith('FEATURE_'):
            if feature == 'FEATURE_SPANNER_LEGACY_DDL':
                continue
            try:
                feature_value = getattr(public_options_pb2, feature)
                if isinstance(feature_value, int) and feature_value > 0:
                    language_options.enabled_language_features.append(feature_value)
            except:
                pass
    
    return opts

service = ZetaSqlLocalService()
analyzer_options = create_analyzer_options()

# Create catalog
catalog = simple_catalog_pb2.SimpleCatalogProto()
catalog.name = "my_catalog"

# Enable builtin functions (IMPORTANT!)
builtin_opts = catalog.builtin_function_options
builtin_opts.language_options.CopyFrom(analyzer_options.language_options)

# Add table
table = catalog.table.add()
table.name = "users"
table.serialization_id = 1

# Add columns
col = table.column.add()
col.name = "user_id"
col.type.type_kind = type_pb2.TYPE_INT64

# Register
reg_response = service.register_catalog(simple_catalog=catalog)
catalog_id = reg_response.registered_id

# ... use catalog ...

# Clean up
service.unregister_catalog(registered_id=catalog_id)
```

### Analyzing a Query

```python
# Use the analyzer_options created above
response = service.analyze(
    sql_statement="SELECT * FROM users WHERE age > 18",
    registered_catalog_id=catalog_id,
    options=analyzer_options  # Important: includes builtin functions
)

# Access resolved AST
resolved_stmt = ResolvedQueryStmt(
    response.resolved_statement.resolved_query_stmt_node
)
```

### Using Wrappers for Clean Access

```python
from zetasql.resolved_ast_wrapper import ResolvedQueryStmt

# Instead of: proto.resolved_statement.resolved_query_stmt_node.output_column_list
# Use wrapper:
resolved_stmt = ResolvedQueryStmt(proto.resolved_statement.resolved_query_stmt_node)

# Clean property access
for col in resolved_stmt.output_column_list:
    print(f"{col.name}: {col.type.type_kind}")

# Inherited properties work too
if resolved_stmt.query:
    print(f"Query scan type: {type(resolved_stmt.query).__name__}")
```

### Traversing the Scan Tree

```python
def walk_scan_tree(scan, depth=0):
    """Recursively walk the resolved scan tree."""
    if not scan:
        return
    
    indent = "  " * depth
    print(f"{indent}{type(scan).__name__}")
    
    # Navigate to input scan
    if hasattr(scan, 'input_scan'):
        walk_scan_tree(scan.input_scan, depth + 1)

walk_scan_tree(resolved_stmt.query)
```

## Type System

ZetaSQL uses numeric type codes for SQL types:

```python
TYPE_INT32 = 1
TYPE_INT64 = 2
TYPE_UINT32 = 3
TYPE_UINT64 = 4
TYPE_BOOL = 5
TYPE_FLOAT = 6
TYPE_DOUBLE = 7
TYPE_STRING = 8
TYPE_BYTES = 9
TYPE_DATE = 10
TYPE_TIMESTAMP = 19
```

Access via `type_pb2` module:

```python
from zetasql.wasi._pb2.zetasql.public import type_pb2

col.type.type_kind = type_pb2.TYPE_STRING
```

## Error Handling

```python
try:
    response = service.analyze(
        sql_statement="SELECT invalid FROM nonexistent",
        registered_catalog_id=catalog_id,
        options=options
    )
except Exception as e:
    # Parse error message
    error_msg = str(e)
    print(f"Query failed: {error_msg}")
```

## Wrapper Benefits

The generated wrapper classes provide:

1. **Clean API**: Direct property access instead of proto chains
   ```python
   # Without wrapper:
   value = proto.parent.parent.field
   
   # With wrapper:
   value = wrapper.field
   ```

2. **Type Hints**: Full IDE autocompletion
   ```python
   resolved_stmt: ResolvedQueryStmt = ...
   # IDE shows all available properties
   ```

3. **Pythonic**: Real inheritance with `isinstance()` checks
   ```python
   if isinstance(scan, ResolvedAggregateScan):
       print(f"Aggregations: {len(scan.aggregate_list)}")
   ```

4. **External Type Conversion**: Automatic Python native types
   ```python
   # google.protobuf.Timestamp → datetime.datetime
   # google.protobuf.Duration → datetime.timedelta
   timestamp: datetime.datetime = wrapper.created_at
   ```

## Running All Examples

Run all examples in sequence:

```bash
python examples/basic_usage.py
python examples/advanced_analysis.py
python examples/testing_debugging.py
```

Or create a master runner:

```bash
for script in examples/*.py; do
    echo "Running $script..."
    python "$script"
    echo ""
done
```

## Further Resources

- **ZetaSQL Documentation**: https://github.com/google/zetasql
- **Wrapper Generator**: `scripts/generate_wrappers.py`
- **Wrapper Classes**: `src/zetasql/resolved_ast_wrapper.py`
- **Design Document**: `docs/wrapper_generator_summary.md`

## Contributing

To add new examples:

1. Create a new `.py` file in `examples/`
2. Follow the pattern of existing examples
3. Include docstrings explaining the example
4. Use wrapper classes for clean AST navigation
5. Add to this README with description

Example template:

```python
#!/usr/bin/env python3
"""
Your example description

Demonstrates specific features or use cases.
"""

from zetasql.local_service import ZetaSqlLocalService
from zetasql.resolved_ast_wrapper import ResolvedQueryStmt


def example_your_feature():
    """Description of what this example does."""
    print("=" * 70)
    print("Example: Your Feature")
    print("=" * 70)
    
    service = ZetaSqlLocalService()
    
    # Your example code...
    
    print()


def main():
    """Run all examples."""
    example_your_feature()


if __name__ == "__main__":
    main()
```
