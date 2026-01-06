# Getting Started with ZetaSQL Python

This guide will walk you through the basics of using ZetaSQL Python, from installation to analyzing your first SQL queries.

## Table of Contents

- [Installation](#installation)
- [Core Concepts](#core-concepts)
- [Basic Usage](#basic-usage)
- [Building Catalogs](#building-catalogs)
- [Analyzing SQL](#analyzing-sql)
- [Working with Types](#working-with-types)
- [Next Steps](#next-steps)

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Install from PyPI

```bash
pip install zetasql
```

### Install from Source

```bash
git clone https://github.com/heoh/zetasql-py.git
cd zetasql-py
pip install -e ".[dev]"
```

### Verify Installation

```python
import zetasql
from zetasql.api import Analyzer

print(f"ZetaSQL Python version: {zetasql.__version__}")
```

## Core Concepts

ZetaSQL Python is organized into three layers:

### Layer 0: WASI
- WebAssembly interface to ZetaSQL
- Generated protobuf definitions
- Located in `zetasql.wasi`

### Layer 1: Core
- `ZetaSqlLocalService`: Communication with WASM layer
- ProtoModel infrastructure
- Exception handling
- Located in `zetasql.core`

### Layer 2: API
- High-level convenience features
- Builder patterns
- Java-like API design
- Located in `zetasql.api`

### Types
- ProtoModel classes with inheritance
- Type enums and constants
- Located in `zetasql.types`

## Basic Usage

### Your First SQL Analysis

```python
from zetasql.api import Analyzer, CatalogBuilder
from zetasql.types import AnalyzerOptions, LanguageOptions, ZetaSQLBuiltinFunctionOptions

# Get language options with all features
lang_opts = LanguageOptions.maximum_features()

# Create catalog with builtin functions
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)
catalog = CatalogBuilder("mydb").with_builtin_functions(builtin_opts).build()

# Create analyzer with options
options = AnalyzerOptions(language_options=lang_opts)
analyzer = Analyzer(options, catalog)

# Analyze a simple query
stmt = analyzer.analyze_statement("SELECT 1 + 1 AS result")

print(f"Statement type: {type(stmt).__name__}")
print(f"Output columns: {len(stmt.output_column_list)}")
print(f"Column name: {stmt.output_column_list[0].name}")
```

**Output:**
```
Statement type: ResolvedQueryStmt
Output columns: 1
Column name: result
```

### Analyzing Expressions

```python
from zetasql.api import Analyzer, CatalogBuilder
from zetasql.types import AnalyzerOptions, LanguageOptions, ZetaSQLBuiltinFunctionOptions

# Setup with builtin functions
lang_opts = LanguageOptions.maximum_features()
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)
catalog = CatalogBuilder("mydb").with_builtin_functions(builtin_opts).build()

analyzer = Analyzer(AnalyzerOptions(language_options=lang_opts), catalog)

# Analyze an expression
expr = analyzer.analyze_expression("2 * 3 + 5")

print(f"Expression type: {type(expr).__name__}")
print(f"Type kind: {expr.type.type_kind}")
```

## Building Catalogs

Catalogs define the schema (tables, functions, constants) available for SQL analysis.

### Creating a Simple Table

```python
from zetasql.api import TableBuilder
from zetasql.types import TypeKind

users_table = (
    TableBuilder("users")
    .add_column("user_id", TypeKind.TYPE_INT64)
    .add_column("username", TypeKind.TYPE_STRING)
    .add_column("email", TypeKind.TYPE_STRING)
    .add_column("created_at", TypeKind.TYPE_TIMESTAMP)
    .build()
)

print(f"Table name: {users_table.name}")
print(f"Columns: {len(users_table.column)}")
```

### Building a Catalog with Tables

```python
from zetasql.api import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind

# Create multiple tables
users = (
    TableBuilder("users")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .build()
)

orders = (
    TableBuilder("orders")
    .add_column("order_id", TypeKind.TYPE_INT64)
    .add_column("user_id", TypeKind.TYPE_INT64)
    .add_column("amount", TypeKind.TYPE_DOUBLE)
    .add_column("order_date", TypeKind.TYPE_DATE)
    .build()
)

# Build catalog
catalog = (
    CatalogBuilder("ecommerce")
    .add_table(users)
    .add_table(orders)
    .build()
)

print(f"Catalog name: {catalog.name}")
print(f"Tables: {[t.name for t in catalog.table]}")
```

### Adding Builtin Functions

```python
from zetasql.api import Analyzer, CatalogBuilder, TableBuilder
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions

# Create table
users = (
    TableBuilder("users")
    .add_column("name", TypeKind.TYPE_STRING)
    .build()
)

# Enable all features
lang_opts = LanguageOptions.maximum_features()
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)

catalog = (
    CatalogBuilder("mydb")
    .add_table(users)
    .with_builtin_functions(builtin_opts)
    .build()
)

# Now you can use builtin functions
analyzer = Analyzer(AnalyzerOptions(language_options=lang_opts), catalog)
stmt = analyzer.analyze_statement("SELECT UPPER(name) FROM users")
```

## Analyzing SQL

### Analyzing Statements

```python
from zetasql.api import Analyzer, CatalogBuilder, TableBuilder
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions

# Setup with builtin functions
lang_opts = LanguageOptions.maximum_features()
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)

table = (
    TableBuilder("products")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("price", TypeKind.TYPE_DOUBLE)
    .build()
)

catalog = CatalogBuilder("shop").add_table(table).with_builtin_functions(builtin_opts).build()
analyzer = Analyzer(AnalyzerOptions(language_options=lang_opts), catalog)

# Analyze various SQL statements
queries = [
    "SELECT * FROM products",
    "SELECT name, price FROM products WHERE price > 100",
    "SELECT AVG(price) FROM products",
]
    "SELECT name, price FROM products WHERE price > 100",
    "SELECT AVG(price) FROM products",
]

for sql in queries:
    stmt = analyzer.analyze_statement(sql)
    cols = [col.name for col in stmt.output_column_list]
    print(f"Query: {sql}")
    print(f"  Output columns: {cols}\n")
```

### Static vs Instance Methods

```python
from zetasql.api import Analyzer

# Instance method (with stored options/catalog)
analyzer = Analyzer(options, catalog)
stmt = analyzer.analyze_statement(sql)

# Static method (pass everything each time)
stmt = Analyzer.analyze_statement_static(sql, options, catalog)

# Building SQL back from AST
sql_str = Analyzer.build_statement(stmt, catalog)
```

### Script Analysis

```python
from zetasql.api import Analyzer

# Multi-statement script
script = """
    CREATE TEMP TABLE temp_data AS
    SELECT * FROM users WHERE active = true;
    
    SELECT COUNT(*) FROM temp_data;
"""

metadata = analyzer.extract_table_names_from_script(script)
print(f"Referenced tables: {metadata.tables}")
print(f"Statement count: {metadata.statement_count}")

# Validate script
result = analyzer.validate_script(script)
if result.is_valid:
    print("Script is valid!")
else:
    print("Errors found:")
    for error in result.errors:
        print(f"  - {error}")
```

## Working with Types

### Type Factory

```python
from zetasql.api import TypeFactory
from zetasql.types import TypeKind

# Simple types
int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
string_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)

# Array type
array_type = TypeFactory.create_array_type(int_type)

# Struct type
struct_type = TypeFactory.create_struct_type([
    ("id", int_type),
    ("name", string_type),
])

# Map type (key-value)
map_type = TypeFactory.create_map_type(string_type, int_type)
```

### Value Creation

```python
from zetasql.api import Value
from zetasql.types import TypeKind

# Primitive values
int_val = Value.int64(42)
str_val = Value.string("hello")
bool_val = Value.bool(True)
double_val = Value.double(3.14)

# NULL values
null_int = Value.null(TypeKind.TYPE_INT64)

# Array values
array_val = Value.array([
    Value.int64(1),
    Value.int64(2),
    Value.int64(3),
])

# Struct values
struct_val = Value.struct({
    "id": Value.int64(1),
    "name": Value.string("Alice"),
})

# Access values
print(f"Int value: {int_val.get_int64()}")
print(f"String value: {str_val.get_string()}")
print(f"Array size: {array_val.get_array_size()}")
print(f"Struct field: {struct_val.get_field('name').get_string()}")
```

### Type Conversion

```python
from zetasql.api import Value
from zetasql.types import TypeKind

# Coercion (implicit conversion)
int_val = Value.int64(42)
double_val = int_val.coerce_to(TypeKind.TYPE_DOUBLE)
print(f"Coerced: {double_val.get_double()}")  # 42.0

# Casting (explicit conversion)
str_val = Value.string("123")
int_val = str_val.cast_to(TypeKind.TYPE_INT64)
print(f"Casted: {int_val.get_int64()}")  # 123
```

## Next Steps

Now that you understand the basics, explore:

- **[API Reference](api-reference.md)** - Complete API documentation
- **[Architecture](architecture.md)** - Deep dive into project structure


### Getting Help

- Check the [API Reference](api-reference.md) for detailed method documentation
- Open an issue on [GitHub](https://github.com/heoh/zetasql-py/issues) for bugs or questions
