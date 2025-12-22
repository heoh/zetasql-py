# ZetaSQL Python Examples

This directory contains examples demonstrating how to use the ZetaSQL Python library.

## Examples

### analyze_with_table.py

Comprehensive example showing how to:

1. **Parse CREATE TABLE statements** - Parse DDL statements to understand table structure
2. **Analyze SELECT queries** - Validate and analyze queries against table definitions
3. **Analyze JOIN queries** - Work with multi-table queries
4. **Analyze aggregation queries** - Handle GROUP BY, HAVING, and aggregate functions
5. **Register and reuse catalogs** - Cache table definitions for better performance
6. **Extract table names** - Get list of tables referenced in a query
7. **Format SQL queries** - Automatically format and beautify SQL code

### Running the Examples

Make sure you have installed the package:

```bash
pip install -e .
```

Then run the example:

```bash
python examples/analyze_with_table.py
```

### Expected Output

The example will demonstrate:
- ✓ Successful parsing of CREATE TABLE statements
- ✓ Analysis of SELECT queries with WHERE clauses
- ✓ Analysis of JOIN queries (INNER, LEFT)
- ✓ Analysis of aggregation queries with GROUP BY/HAVING
- ✓ Catalog registration and reuse
- ✓ Table name extraction from complex queries
- ✓ SQL formatting

## Key Concepts

### Creating a Catalog

Tables must be defined in a `SimpleCatalogProto`:

```python
from zetasql.wasi._pb2.zetasql.proto import simple_catalog_pb2
from zetasql.wasi._pb2.zetasql.public import type_pb2

catalog = simple_catalog_pb2.SimpleCatalogProto()

# Add a table
table = catalog.table.add()
table.name = "users"

# Add columns
col = table.column.add()
col.name = "id"
col.type.type_kind = type_pb2.TYPE_INT64
```

### Enabling Builtin Functions

To use operators (`>`, `+`, etc.) and functions (`COUNT`, `SUM`, etc.), enable builtin functions:

```python
builtin_opts = catalog.builtin_function_options
builtin_opts.language_options.CopyFrom(analyzer_options.language_options)
```

### Analyzing Queries

```python
from zetasql.local_service import ZetaSqlLocalService

service = ZetaSqlLocalService()
response = service.analyze(
    sql_statement="SELECT * FROM users WHERE age > 18",
    simple_catalog=catalog,
    options=analyzer_options
)
```

## More Information

- [ZetaSQL Documentation](https://github.com/google/zetasql)
- [Protocol Buffer Reference](https://github.com/google/zetasql/tree/master/zetasql/proto)
