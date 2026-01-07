# ZetaSQL Python

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Python port of Google's [ZetaSQL](https://github.com/google/zetasql) - a powerful SQL analysis and parsing library.

## Overview

ZetaSQL Python brings Google's SQL analyzer to the Python ecosystem, providing:

- **SQL Analysis**: Parse and analyze SQL statements with full type checking
- **Name Resolution**: Resolve table and column references against catalogs
- **Query Building**: Construct and manipulate SQL AST programmatically
- **Expression Evaluation**: Execute queries and expressions with parameter binding
- **Java-like API**: Familiar builder patterns and fluent interfaces

This project is built on top of [zetasql-wasi](https://github.com/heoh/zetasql-wasi), which provides the WebAssembly build of ZetaSQL, enabling ZetaSQL functionality in Python environments.

## Installation

```bash
pip install zetasql
```

**Requirements:** Python 3.10+

## Quick Start

```python
from zetasql.api import Analyzer, CatalogBuilder, TableBuilder
from zetasql.types import AnalyzerOptions, LanguageOptions, TypeKind, ZetaSQLBuiltinFunctionOptions

# Create a catalog with a table
table = (
    TableBuilder("users")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("email", TypeKind.TYPE_STRING)
    .build()
)

# Build catalog with builtin functions
lang_opts = LanguageOptions.maximum_features()
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)

catalog = (
    CatalogBuilder("mydb")
    .add_table(table)
    .with_builtin_functions(builtin_opts)
    .build()
)

# Analyze SQL
options = AnalyzerOptions(language_options=lang_opts)
analyzer = Analyzer(options, catalog)
stmt = analyzer.analyze_statement("SELECT name, email FROM users WHERE id > 100")

print(f"Analyzed {len(stmt.output_column_list)} output columns")
# Output: Analyzed 2 output columns
```

## Key Features

### 🔍 **SQL Parsing & Analysis**
Parse SQL syntax or perform full semantic analysis:
```python
from zetasql.api import Parser, Analyzer

# Parser: Syntax-only parsing (fast, no catalog needed)
ast_stmt = Parser.parse_statement_static("SELECT * FROM users")

# Analyzer: Full semantic analysis with type checking
resolved_stmt = analyzer.analyze_statement("SELECT * FROM users")
```

### 🌲 **AST Traversal**
Visit and inspect SQL parse trees with the Visitor pattern:
```python
from zetasql.api import Parser, ASTNodeVisitor

class TableNameCollector(ASTNodeVisitor):
    def __init__(self):
        super().__init__()
        self.tables = []
    
    def visit_ASTPathExpression(self, node):
        if node.names:
            self.tables.append(".".join([n.identifier for n in node.names]))

stmt = Parser.parse_statement_static("SELECT * FROM users JOIN orders")
visitor = TableNameCollector()
visitor.visit(stmt)
print(visitor.tables)  # ['users', 'orders']
```

### 🏗️ **Builder Pattern APIs**
Fluent interfaces for constructing catalogs, tables, and functions:
```python
from zetasql.api import CatalogBuilder
from zetasql.types import LanguageOptions, ZetaSQLBuiltinFunctionOptions

lang_opts = LanguageOptions.maximum_features()
builtin_opts = ZetaSQLBuiltinFunctionOptions(language_options=lang_opts)

catalog = (
    CatalogBuilder("shop")
    .add_table(orders_table)
    .add_table(products_table)
    .with_builtin_functions(builtin_opts)
    .build()
)
```

### ⚡ **Query Execution**
Execute queries with parameter binding and table data:
```python
from zetasql.api import PreparedQuery, create_table_content

data = create_table_content([[1, "Alice"], [2, "Bob"]])
query = PreparedQuery("SELECT * FROM users WHERE id = @user_id", options, catalog)
result = query.execute(parameters={"user_id": 1}, table_content={"users": data})
```

### 🎯 **Type-Safe Values**
Create and manipulate typed SQL values:
```python
from zetasql.api import Value

int_val = Value.int64(42)
str_val = Value.string("hello")
array_val = Value.array([Value.int64(1), Value.int64(2)])
```

### 📦 **ProtoModel System**
Pythonic wrappers around protobuf messages with real inheritance:
```python
from zetasql.types import ResolvedLiteral

literal = ResolvedLiteral(...)
type_kind = literal.type.type_kind  # Direct access, no parent chain
isinstance(literal, ResolvedExpr)   # True - real inheritance!
```

## Documentation

- **[Getting Started Guide](docs/getting-started.md)** - Detailed tutorials and examples
- **[API Reference](docs/api-reference.md)** - Complete API documentation
- **[ProtoModel Inheritance Hierarchy](docs/proto-model-hierarchy.md)** - The inheritance structure of the ProtoModel classes
- **[Architecture](docs/architecture.md)** - Project structure and design

## Development

```bash
# Clone the repository
git clone https://github.com/heoh/zetasql-py.git
cd zetasql-py

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check src/ tests/
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Project Status

This project is in **alpha** stage. The API is functional but may change as we refine the design. Feedback and contributions are welcome!

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

This is an unofficial Python port of Google's ZetaSQL (also Apache 2.0 licensed) and is not affiliated with Google.

## Acknowledgments

- Original [ZetaSQL project](https://github.com/google/zetasql) by Google
- Built on [zetasql-wasi](https://github.com/heoh/zetasql-wasi) - WebAssembly build of ZetaSQL
- Inspired by the Java ZetaSQL API design
