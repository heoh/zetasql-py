# Examples

Practical examples demonstrating common usage patterns for ZetaSQL Python.

## Table of Contents

- [Basic SQL Analysis](#basic-sql-analysis)
- [Catalog Building](#catalog-building)
- [Query Execution](#query-execution)
- [Expression Evaluation](#expression-evaluation)
- [Custom Functions](#custom-functions)
- [Script Analysis](#script-analysis)
- [Working with Values](#working-with-values)
- [Error Handling](#error-handling)
- [Advanced Patterns](#advanced-patterns)

---

## Basic SQL Analysis

### Simple Query Analysis

```python
from zetasql.api import Analyzer, CatalogBuilder
from zetasql.types import AnalyzerOptions

# Create analyzer
catalog = CatalogBuilder("mydb").build()
options = AnalyzerOptions()
analyzer = Analyzer(options, catalog)

# Analyze simple expression
stmt = analyzer.analyze_statement("SELECT 1 + 1 AS result")

# Inspect result
print(f"Statement type: {type(stmt).__name__}")
print(f"Output columns: {[col.name for col in stmt.output_column_list]}")
# Output: ['result']
```

### Analyzing Multiple Statements

```python
from zetasql.api import Analyzer

queries = [
    "SELECT 1",
    "SELECT 'hello' AS greeting",
    "SELECT CURRENT_DATE()",
]

for sql in queries:
    try:
        stmt = analyzer.analyze_statement(sql)
        print(f"✓ Valid: {sql}")
    except Exception as e:
        print(f"✗ Invalid: {sql} - {e}")
```

### Getting Statement Types

```python
from zetasql.api import Analyzer, get_statement_type, StatementType

queries = {
    "SELECT * FROM users": StatementType.QUERY,
    "INSERT INTO users VALUES (1, 'Alice')": StatementType.DML,
    "CREATE TABLE new_users (id INT64)": StatementType.DDL,
}

for sql, expected_type in queries.items():
    stmt = analyzer.analyze_statement(sql)
    actual_type = get_statement_type(stmt)
    assert actual_type == expected_type
    print(f"{sql} → {actual_type}")
```

---

## Catalog Building

### E-Commerce Database Catalog

```python
from zetasql.api import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind, LanguageOptions, ZetaSQLBuiltinFunctionOptions

# Define tables
customers = (
    TableBuilder("customers")
    .add_column("customer_id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("email", TypeKind.TYPE_STRING)
    .add_column("country", TypeKind.TYPE_STRING)
    .add_column("created_at", TypeKind.TYPE_TIMESTAMP)
    .build()
)

orders = (
    TableBuilder("orders")
    .add_column("order_id", TypeKind.TYPE_INT64)
    .add_column("customer_id", TypeKind.TYPE_INT64)
    .add_column("order_date", TypeKind.TYPE_DATE)
    .add_column("status", TypeKind.TYPE_STRING)
    .add_column("total_amount", TypeKind.TYPE_DOUBLE)
    .build()
)

order_items = (
    TableBuilder("order_items")
    .add_column("item_id", TypeKind.TYPE_INT64)
    .add_column("order_id", TypeKind.TYPE_INT64)
    .add_column("product_id", TypeKind.TYPE_INT64)
    .add_column("quantity", TypeKind.TYPE_INT64)
    .add_column("unit_price", TypeKind.TYPE_DOUBLE)
    .build()
)

products = (
    TableBuilder("products")
    .add_column("product_id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("category", TypeKind.TYPE_STRING)
    .add_column("price", TypeKind.TYPE_DOUBLE)
    .add_column("in_stock", TypeKind.TYPE_BOOL)
    .build()
)

# Build catalog with builtin functions
builtin_opts = ZetaSQLBuiltinFunctionOptions(
    language_options=LanguageOptions.maximum_features()
)

catalog = (
    CatalogBuilder("ecommerce")
    .add_table(customers)
    .add_table(orders)
    .add_table(order_items)
    .add_table(products)
    .with_builtin_functions(builtin_opts)
    .build()
)

print(f"Catalog '{catalog.name}' with {len(catalog.table)} tables")
```

### Complex Table with Nested Types

```python
from zetasql.api import TableBuilder, TypeFactory
from zetasql.types import TypeKind

# Create struct type for address
address_type = TypeFactory.create_struct_type([
    ("street", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
    ("city", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
    ("zip", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
])

# Create array type for phone numbers
phone_array_type = TypeFactory.create_array_type(
    TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
)

# Build table with complex types
users = (
    TableBuilder("users")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("address", address_type)
    .add_column("phone_numbers", phone_array_type)
    .build()
)
```

---

## Query Execution

### Basic Query Execution

```python
from zetasql.api import PreparedQuery, create_table_content
from zetasql.types import AnalyzerOptions

# Create table data
users_data = create_table_content([
    [1, "Alice", "alice@example.com"],
    [2, "Bob", "bob@example.com"],
    [3, "Charlie", "charlie@example.com"],
])

# Prepare and execute query
query = PreparedQuery(
    "SELECT * FROM users WHERE id > 1",
    AnalyzerOptions(),
    catalog
)

result = query.execute(table_content={"users": users_data})

# Process results
print(f"Rows returned: {len(result.rows)}")
for row in result.rows:
    print(f"  {row}")
```

### Query with Parameters

```python
from zetasql.api import PreparedQuery, create_table_content, Value

# Data
products_data = create_table_content([
    [1, "Laptop", 999.99],
    [2, "Mouse", 29.99],
    [3, "Keyboard", 79.99],
    [4, "Monitor", 299.99],
])

# Parameterized query
query = PreparedQuery(
    "SELECT * FROM products WHERE price BETWEEN @min_price AND @max_price",
    options,
    catalog
)

result = query.execute(
    parameters={
        "min_price": Value.double(50.0),
        "max_price": Value.double(500.0),
    },
    table_content={"products": products_data}
)

print(f"Found {len(result.rows)} products in price range")
```

### Using Context Manager

```python
from zetasql.api import PreparedQuery

with PreparedQuery(sql, options, catalog) as query:
    result = query.execute(
        parameters={"user_id": Value.int64(42)},
        table_content={"users": users_data}
    )
    # Process results
    for row in result.rows:
        print(row)
# Automatically cleaned up
```

### Chaining with Builder

```python
from zetasql.api import PreparedQuery

result = (
    PreparedQuery.builder()
    .sql("SELECT * FROM users WHERE country = @country AND created_at > @date")
    .options(options)
    .catalog(catalog)
    .build()
    .with_parameters({
        "country": Value.string("USA"),
        "date": Value.timestamp(datetime.datetime(2024, 1, 1))
    })
    .with_table_content({"users": users_data})
    .execute()
)
```

---

## Expression Evaluation

### Simple Expression

```python
from zetasql.api import PreparedExpression, Value

expr = PreparedExpression("2 * 3 + 5", options)
result = expr.execute()

print(f"Result: {result.get_int64()}")  # 11
```

### Expression with Parameters

```python
from zetasql.api import PreparedExpression, Value

expr = PreparedExpression("@x * @y + @z", options)

result = expr.execute(parameters={
    "x": Value.int64(10),
    "y": Value.int64(5),
    "z": Value.int64(3),
})

print(f"10 * 5 + 3 = {result.get_int64()}")  # 53
```

### Expression with Columns

```python
from zetasql.api import PreparedExpression, Value
from zetasql.types import TypeKind

# Build expression with columns
expr = (
    PreparedExpression.builder()
    .expression("price * quantity * (1 - discount)")
    .options(options)
    .column("price", TypeKind.TYPE_DOUBLE)
    .column("quantity", TypeKind.TYPE_INT64)
    .column("discount", TypeKind.TYPE_DOUBLE)
    .build()
)

# Evaluate with column values
result = expr.execute(columns={
    "price": Value.double(99.99),
    "quantity": Value.int64(3),
    "discount": Value.double(0.1),  # 10% discount
})

print(f"Total: ${result.get_double():.2f}")
```

### String Operations

```python
from zetasql.api import PreparedExpression, Value

expressions = [
    ("UPPER(@name)", {"name": Value.string("alice")}),
    ("CONCAT(@first, ' ', @last)", {
        "first": Value.string("John"),
        "last": Value.string("Doe")
    }),
    ("LENGTH(@text)", {"text": Value.string("hello")}),
]

for expr_str, params in expressions:
    expr = PreparedExpression(expr_str, options)
    result = expr.execute(parameters=params)
    print(f"{expr_str} = {result}")
```

---

## Custom Functions

### Creating a Custom Function

```python
from zetasql.api import FunctionBuilder, SignatureBuilder
from zetasql.types import TypeKind, FunctionMode

# Create function signature
signature = (
    SignatureBuilder()
    .add_argument(TypeKind.TYPE_INT64)
    .add_argument(TypeKind.TYPE_INT64)
    .set_result_type(TypeKind.TYPE_INT64)
    .build()
)

# Create function
add_func = (
    FunctionBuilder("custom_add", group="custom")
    .add_signature(signature)
    .set_mode(FunctionMode.FUNCTION_MODE_SCALAR)
    .build()
)

# Add to catalog
catalog = (
    CatalogBuilder("mydb")
    .add_function(add_func)
    .build()
)
```

### Aggregate Function

```python
from zetasql.api import FunctionBuilder, SignatureBuilder
from zetasql.types import TypeKind, FunctionMode

# Signature for aggregate function
signature = (
    SignatureBuilder()
    .add_argument(TypeKind.TYPE_DOUBLE)
    .set_result_type(TypeKind.TYPE_DOUBLE)
    .build()
)

avg_func = (
    FunctionBuilder("custom_avg")
    .add_signature(signature)
    .set_mode(FunctionMode.FUNCTION_MODE_AGGREGATE)
    .build()
)
```

### Table-Valued Function (TVF)

```python
from zetasql.api import TVFBuilder
from zetasql.types import TypeKind

# Create TVF that returns a table
range_tvf = (
    TVFBuilder("generate_series")
    .add_input_argument("start_val", TypeKind.TYPE_INT64)
    .add_input_argument("end_val", TypeKind.TYPE_INT64)
    .add_output_column("value", TypeKind.TYPE_INT64)
    .build()
)

catalog = CatalogBuilder("mydb").add_tvf(range_tvf).build()

# Can now use in queries:
# SELECT * FROM generate_series(1, 10)
```

---

## Script Analysis

### Extracting Table Names

```python
from zetasql.api import Analyzer

script = """
    SELECT c.name, COUNT(o.order_id)
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_date >= '2024-01-01'
    GROUP BY c.name;
    
    SELECT p.name, SUM(oi.quantity)
    FROM products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.name;
"""

analyzer = Analyzer(options, catalog)
metadata = analyzer.extract_table_names_from_script(script)

print(f"Tables referenced: {metadata.tables}")
# Output: {'customers', 'orders', 'products', 'order_items'}

print(f"Number of statements: {metadata.statement_count}")
# Output: 2
```

### Validating Scripts

```python
from zetasql.api import Analyzer

valid_script = """
    CREATE TEMP TABLE active_users AS
    SELECT * FROM users WHERE status = 'active';
    
    SELECT COUNT(*) FROM active_users;
"""

invalid_script = """
    SELECT * FROM nonexistent_table;
    SELECT invalid_column FROM users;
"""

analyzer = Analyzer(options, catalog)

# Validate valid script
result = analyzer.validate_script(valid_script)
assert result.is_valid
print("✓ Script is valid")

# Validate invalid script
result = analyzer.validate_script(invalid_script)
if not result.is_valid:
    print("✗ Script has errors:")
    for error in result.errors:
        print(f"  - {error}")
```

### Analyzing Script Statements One by One

```python
from zetasql.api import Analyzer
from zetasql.types import ParseResumeLocation

script = """
    SELECT 1;
    SELECT 2;
    SELECT 3;
"""

analyzer = Analyzer(options, catalog)
location = ParseResumeLocation(sql=script)

statements = []
while True:
    try:
        stmt, location = analyzer.analyze_next_statement(location, options, catalog)
        statements.append(stmt)
        
        if not location or location.byte_position >= len(script):
            break
    except Exception:
        break

print(f"Analyzed {len(statements)} statements")
```

---

## Working with Values

### Creating Different Value Types

```python
from zetasql.api import Value
from zetasql.types import TypeKind
import datetime

# Numeric values
int_val = Value.int64(42)
float_val = Value.double(3.14159)
bool_val = Value.bool(True)

# String and bytes
str_val = Value.string("Hello, ZetaSQL!")
bytes_val = Value.bytes(b"binary data")

# Date/Time values
date_val = Value.date(2024, 1, 15)
timestamp_val = Value.timestamp(datetime.datetime.now())

# NULL values
null_int = Value.null(TypeKind.TYPE_INT64)
null_str = Value.null(TypeKind.TYPE_STRING)

# Check types
print(f"int_val is INT64: {int_val.type_kind() == TypeKind.TYPE_INT64}")
print(f"null_int is NULL: {null_int.is_null()}")
```

### Working with Arrays

```python
from zetasql.api import Value

# Create array
numbers = Value.array([
    Value.int64(1),
    Value.int64(2),
    Value.int64(3),
    Value.int64(4),
    Value.int64(5),
])

print(f"Array size: {numbers.get_array_size()}")

# Access elements
for i in range(numbers.get_array_size()):
    element = numbers.get_array_element(i)
    print(f"  [{i}] = {element.get_int64()}")

# Iterate over array
for element in numbers:
    print(f"Value: {element.get_int64()}")
```

### Working with Structs

```python
from zetasql.api import Value

# Create struct
person = Value.struct({
    "id": Value.int64(1),
    "name": Value.string("Alice"),
    "email": Value.string("alice@example.com"),
    "age": Value.int64(30),
    "active": Value.bool(True),
})

# Access fields
print(f"Name: {person.get_field('name').get_string()}")
print(f"Age: {person.get_field('age').get_int64()}")
print(f"Active: {person.get_field('active').get_bool()}")

# Nested structs
address = Value.struct({
    "street": Value.string("123 Main St"),
    "city": Value.string("Springfield"),
    "zip": Value.string("12345"),
})

person_with_address = Value.struct({
    "id": Value.int64(1),
    "name": Value.string("Bob"),
    "address": address,
})

city = person_with_address.get_field("address").get_field("city").get_string()
print(f"City: {city}")
```

### Value Comparisons

```python
from zetasql.api import Value

val1 = Value.int64(42)
val2 = Value.int64(42)
val3 = Value.int64(100)

# Equality
print(f"val1 == val2: {val1.equals(val2)}")  # True
print(f"val1 == val3: {val1.equals(val3)}")  # False

# Comparison
print(f"val1 < val3: {val1.compare_to(val3) < 0}")   # True
print(f"val3 > val1: {val3.compare_to(val1) > 0}")   # True
print(f"val1 == val2: {val1.compare_to(val2) == 0}") # True
```

### Type Conversions

```python
from zetasql.api import Value
from zetasql.types import TypeKind

# Implicit conversion (coercion)
int_val = Value.int64(42)
double_val = int_val.coerce_to(TypeKind.TYPE_DOUBLE)
print(f"42 as double: {double_val.get_double()}")  # 42.0

# Explicit conversion (casting)
str_val = Value.string("123")
int_val = str_val.cast_to(TypeKind.TYPE_INT64)
print(f"'123' as int: {int_val.get_int64()}")  # 123

str_val = Value.string("3.14")
double_val = str_val.cast_to(TypeKind.TYPE_DOUBLE)
print(f"'3.14' as double: {double_val.get_double()}")  # 3.14

# Boolean from string
bool_str = Value.string("true")
bool_val = bool_str.cast_to(TypeKind.TYPE_BOOL)
print(f"'true' as bool: {bool_val.get_bool()}")  # True
```

### SQL Literal Representation

```python
from zetasql.api import Value

values = [
    Value.int64(42),
    Value.string("hello"),
    Value.bool(True),
    Value.array([Value.int64(1), Value.int64(2), Value.int64(3)]),
    Value.struct({"x": Value.int64(1), "y": Value.int64(2)}),
]

for val in values:
    print(f"{val} → SQL: {val.to_sql_literal()}")
```

---

## Error Handling

### Catching Analysis Errors

```python
from zetasql.api import Analyzer
from zetasql.core.exceptions import ZetaSQLError

analyzer = Analyzer(options, catalog)

queries = [
    "SELECT * FROM users",                    # Valid
    "SELECT * FROM nonexistent_table",        # Invalid - table not found
    "SELECT invalid_column FROM users",       # Invalid - column not found
    "SELECT",                                 # Invalid - syntax error
]

for sql in queries:
    try:
        stmt = analyzer.analyze_statement(sql)
        print(f"✓ {sql}")
    except ZetaSQLError as e:
        print(f"✗ {sql}")
        print(f"  Error: {e}")
```

### Handling Execution Errors

```python
from zetasql.api import PreparedQuery
from zetasql.core.exceptions import ZetaSQLError

try:
    query = PreparedQuery(sql, options, catalog)
    result = query.execute(
        parameters=parameters,
        table_content=table_content
    )
except ZetaSQLError as e:
    print(f"Query execution failed: {e}")
    # Handle error (log, retry, etc.)
```

### Graceful Error Handling

```python
from zetasql.api import Analyzer
from zetasql.core.exceptions import ZetaSQLError
from typing import Optional

def safe_analyze(sql: str, analyzer: Analyzer) -> Optional[str]:
    """Safely analyze SQL and return error message if invalid."""
    try:
        stmt = analyzer.analyze_statement(sql)
        return None  # Success
    except ZetaSQLError as e:
        return str(e)

# Use it
error = safe_analyze("SELECT * FROM invalid_table", analyzer)
if error:
    print(f"Analysis failed: {error}")
else:
    print("SQL is valid")
```

---

## Advanced Patterns

### Query Roundtrip (Analysis → SQL → Analysis)

```python
from zetasql.api import Analyzer

analyzer = Analyzer(options, catalog)

# Original SQL
original_sql = "SELECT name, email FROM users WHERE id > 100"

# Step 1: Analyze
stmt = analyzer.analyze_statement(original_sql)

# Step 2: Build SQL back from AST
rebuilt_sql = Analyzer.build_statement(stmt, catalog)

# Step 3: Re-analyze rebuilt SQL (should succeed)
stmt2 = analyzer.analyze_statement(rebuilt_sql)

# Verify output columns match
cols1 = [col.name for col in stmt.output_column_list]
cols2 = [col.name for col in stmt2.output_column_list]
assert cols1 == cols2

print(f"Original:  {original_sql}")
print(f"Rebuilt:   {rebuilt_sql}")
print(f"Columns:   {cols1}")
```

### Batch Analysis

```python
from zetasql.api import Analyzer
from typing import List, Tuple

def batch_analyze(
    queries: List[str],
    analyzer: Analyzer
) -> List[Tuple[str, bool, str]]:
    """
    Analyze multiple queries and return results.
    
    Returns: List of (query, is_valid, error_or_type)
    """
    results = []
    for sql in queries:
        try:
            stmt = analyzer.analyze_statement(sql)
            results.append((sql, True, type(stmt).__name__))
        except Exception as e:
            results.append((sql, False, str(e)))
    return results

# Use it
queries = [
    "SELECT * FROM users",
    "SELECT COUNT(*) FROM orders",
    "SELECT invalid FROM nowhere",
]

results = batch_analyze(queries, analyzer)
for sql, is_valid, info in results:
    status = "✓" if is_valid else "✗"
    print(f"{status} {sql}: {info}")
```

### Catalog Composition

```python
from zetasql.api import CatalogBuilder, TableBuilder
from zetasql.types import TypeKind

# Create separate domain-specific catalogs
def create_user_catalog():
    users = TableBuilder("users").add_column("id", TypeKind.TYPE_INT64).build()
    return CatalogBuilder("users_domain").add_table(users)

def create_product_catalog():
    products = TableBuilder("products").add_column("id", TypeKind.TYPE_INT64).build()
    return CatalogBuilder("products_domain").add_table(products)

# Compose into single catalog
full_catalog = (
    CatalogBuilder("full")
    .add_table(create_user_catalog().build().table[0])
    .add_table(create_product_catalog().build().table[0])
    .build()
)
```

### Conditional Table Building

```python
from zetasql.api import TableBuilder
from zetasql.types import TypeKind

def build_table_with_optional_columns(
    name: str,
    base_columns: dict,
    optional_columns: dict = None,
    include_timestamp: bool = True
):
    """Build table with optional columns."""
    builder = TableBuilder(name)
    
    # Add base columns
    for col_name, col_type in base_columns.items():
        builder.add_column(col_name, col_type)
    
    # Add optional columns
    if optional_columns:
        for col_name, col_type in optional_columns.items():
            builder.add_column(col_name, col_type)
    
    # Add timestamp if requested
    if include_timestamp:
        builder.add_column("created_at", TypeKind.TYPE_TIMESTAMP)
        builder.add_column("updated_at", TypeKind.TYPE_TIMESTAMP)
    
    return builder.build()

# Use it
table = build_table_with_optional_columns(
    "users",
    base_columns={
        "id": TypeKind.TYPE_INT64,
        "name": TypeKind.TYPE_STRING,
    },
    optional_columns={
        "email": TypeKind.TYPE_STRING,
        "phone": TypeKind.TYPE_STRING,
    },
    include_timestamp=True
)
```

---

## See Also

- [Getting Started Guide](GETTING_STARTED.md)
- [API Reference](API_REFERENCE.md)
- [Architecture](ARCHITECTURE.md)
