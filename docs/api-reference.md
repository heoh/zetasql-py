# API Reference

Complete API documentation for ZetaSQL Python.

## Table of Contents

- [zetasql.api](#zetasqlapi)
  - [Analyzer](#analyzer)
  - [PreparedQuery](#preparedquery)
  - [PreparedExpression](#preparedexpression)
  - [Value](#value)
  - [TypeFactory](#typefactory)
  - [Builders](#builders)
- [zetasql.types](#zetasqltypes)
  - [ProtoModel Classes](#protomodel-classes)
  - [Enums](#enums)
- [zetasql.core](#zetasqlcore)
  - [ZetaSqlLocalService](#zetasqllocalservice)

---

## zetasql.api

High-level convenience API for SQL analysis and execution.

### Analyzer

**Class:** `zetasql.api.Analyzer`

SQL analyzer for parsing and analyzing SQL statements and expressions.

#### Constructor

```python
Analyzer(
    options: AnalyzerOptions,
    catalog: SimpleCatalog | None = None,
    service: ZetaSqlLocalService | None = None
)
```

**Parameters:**
- `options`: Analyzer configuration options
- `catalog`: Optional catalog for name resolution
- `service`: Optional LocalService instance (uses singleton if not provided)

**Example:**
```python
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions

analyzer = Analyzer(AnalyzerOptions(), catalog)
```

#### Instance Methods

##### `analyze_statement(sql: str) -> ResolvedStatement`

Analyze SQL statement and return resolved AST.

**Parameters:**
- `sql`: SQL statement to analyze

**Returns:** `ResolvedStatement` (union type - actual type determined at runtime)

**Raises:** `ZetaSQLError` if analysis fails

**Example:**
```python
stmt = analyzer.analyze_statement("SELECT * FROM users")
print(f"Output columns: {len(stmt.output_column_list)}")
```

##### `analyze_expression(expression: str) -> ResolvedExpr`

Analyze SQL expression and return resolved AST.

**Parameters:**
- `expression`: SQL expression to analyze

**Returns:** `ResolvedExpr`

**Example:**
```python
expr = analyzer.analyze_expression("price * quantity")
print(f"Expression type: {expr.type.type_kind}")
```

##### `analyze_next_statement(...) -> Tuple[ResolvedStatement, ParseResumeLocation]`

Analyze next statement in a script.

**Parameters:**
- `location`: Resume location from previous parse
- Additional options...

**Returns:** Tuple of (resolved statement, next resume location)

##### `extract_table_names_from_script(script: str) -> ScriptMetadata`

Extract metadata from SQL script.

**Returns:** `ScriptMetadata` with tables and statement count

**Example:**
```python
metadata = analyzer.extract_table_names_from_script(script)
print(f"Tables: {metadata.tables}")
print(f"Statements: {metadata.statement_count}")
```

##### `validate_script(script: str) -> ValidationResult`

Validate SQL script for errors.

**Returns:** `ValidationResult` with validation status and errors

**Example:**
```python
result = analyzer.validate_script(script)
if not result.is_valid:
    for error in result.errors:
        print(f"Error: {error}")
```

#### Static Methods

##### `analyze_statement_static(sql: str, options: AnalyzerOptions, catalog: SimpleCatalog) -> ResolvedStatement`

Static version of `analyze_statement`.

##### `analyze_expression_static(expression: str, options: AnalyzerOptions, catalog: SimpleCatalog) -> ResolvedExpr`

Static version of `analyze_expression`.

##### `build_statement(stmt: ResolvedStatement, catalog: SimpleCatalog) -> str`

Build SQL string from resolved statement AST.

**Example:**
```python
sql = Analyzer.build_statement(resolved_stmt, catalog)
```

#### Helper Functions

##### `get_statement_type(stmt: ResolvedStatement) -> StatementType`

Categorize statement into QUERY, DML, DDL, or OTHER.

**Example:**
```python
from zetasql.api import get_statement_type

stmt_type = get_statement_type(stmt)
print(stmt_type)  # StatementType.QUERY
```

---

### PreparedQuery

**Class:** `zetasql.api.PreparedQuery`

Prepared query for execution with parameter binding and table data.

#### Constructor

```python
PreparedQuery(
    sql: str,
    options: AnalyzerOptions,
    catalog: SimpleCatalog | None = None,
    service: ZetaSqlLocalService | None = None
)
```

**Example:**
```python
from zetasql.api import PreparedQuery

query = PreparedQuery(
    "SELECT * FROM users WHERE id = @user_id",
    options,
    catalog
)
```

#### Methods

##### `execute(parameters: dict = None, table_content: dict = None) -> EvaluateResponse`

Execute the query with parameters and table data.

**Parameters:**
- `parameters`: Dict mapping parameter names to values
- `table_content`: Dict mapping table names to TableContent

**Returns:** `EvaluateResponse` with query results

**Example:**
```python
from zetasql.api import create_table_content

data = create_table_content([[1, "Alice"], [2, "Bob"]])
result = query.execute(
    parameters={"user_id": 1},
    table_content={"users": data}
)
```

##### `with_parameters(params: dict) -> PreparedQuery`

Set query parameters (returns self for chaining).

##### `with_table_content(content: dict) -> PreparedQuery`

Set table data (returns self for chaining).

##### `close()`

Release resources (or use as context manager).

#### Builder Pattern

```python
from zetasql.api import PreparedQuery

query = (
    PreparedQuery.builder()
    .sql("SELECT * FROM users WHERE id > @min_id")
    .options(options)
    .catalog(catalog)
    .build()
)
```

#### Context Manager

```python
with PreparedQuery(sql, options, catalog) as query:
    result = query.execute(parameters={...})
```

---

### PreparedExpression

**Class:** `zetasql.api.PreparedExpression`

Prepared expression for evaluation with column binding.

#### Constructor

```python
PreparedExpression(
    expression: str,
    options: AnalyzerOptions,
    catalog: SimpleCatalog | None = None,
    service: ZetaSqlLocalService | None = None
)
```

#### Methods

##### `execute(parameters: dict = None, columns: dict = None) -> Value`

Evaluate expression and return result.

**Parameters:**
- `parameters`: Query parameters
- `columns`: Column values for expression evaluation

**Returns:** `Value` object with result

**Example:**
```python
from zetasql.api import PreparedExpression, Value

expr = PreparedExpression("@x + @y", options)
result = expr.execute(parameters={
    "x": Value.int64(10),
    "y": Value.int64(20)
})
print(result.get_int64())  # 30
```

##### `get_expression_type() -> Type`

Get the type of the expression result.

#### Builder Pattern

```python
expr = (
    PreparedExpression.builder()
    .expression("price * quantity")
    .options(options)
    .catalog(catalog)
    .column("price", TypeKind.TYPE_DOUBLE)
    .column("quantity", TypeKind.TYPE_INT64)
    .build()
)
```

---

### Value

**Class:** `zetasql.api.Value`

Represents a typed SQL value with type-safe constructors and accessors.

#### Static Constructors

##### Primitive Types

```python
Value.int64(value: int) -> Value
Value.int32(value: int) -> Value
Value.uint64(value: int) -> Value
Value.uint32(value: int) -> Value
Value.bool(value: bool) -> Value
Value.float_value(value: float) -> Value
Value.double(value: float) -> Value
Value.string(value: str) -> Value
Value.bytes(value: bytes) -> Value
```

##### Date/Time Types

```python
Value.date(year: int, month: int, day: int) -> Value
Value.timestamp(dt: datetime) -> Value
Value.time(hour: int, minute: int, second: int, microsecond: int = 0) -> Value
Value.datetime(dt: datetime) -> Value
```

##### Complex Types

```python
Value.array(elements: list[Value]) -> Value
Value.struct(fields: dict[str, Value]) -> Value
Value.null(type_kind: TypeKind) -> Value
```

**Examples:**
```python
from zetasql.api import Value
import datetime

# Primitives
num = Value.int64(42)
text = Value.string("hello")
flag = Value.bool(True)

# Date/Time
date_val = Value.date(2024, 1, 15)
ts_val = Value.timestamp(datetime.datetime.now())

# Arrays
arr = Value.array([Value.int64(1), Value.int64(2), Value.int64(3)])

# Structs
person = Value.struct({
    "id": Value.int64(1),
    "name": Value.string("Alice"),
    "active": Value.bool(True)
})

# NULL
null_int = Value.null(TypeKind.TYPE_INT64)
```

#### Accessor Methods

```python
get_int64() -> int
get_int32() -> int
get_string() -> str
get_bool() -> bool
get_double() -> float
get_float() -> float
get_date() -> datetime.date
get_timestamp() -> datetime.datetime

get_array_size() -> int
get_array_element(index: int) -> Value
get_field(field_name: str) -> Value
```

#### Utility Methods

```python
is_null() -> bool
type_kind() -> TypeKind
get_type() -> Type
to_proto() -> types.Value
to_sql_literal() -> str

equals(other: Value) -> bool
compare_to(other: Value) -> int  # -1, 0, 1

coerce_to(target_type: TypeKind) -> Value  # Implicit conversion
cast_to(target_type: TypeKind) -> Value     # Explicit conversion
```

**Examples:**
```python
# Check type
if value.type_kind() == TypeKind.TYPE_INT64:
    print(value.get_int64())

# Check null
if value.is_null():
    print("Value is NULL")

# Comparison
if val1.equals(val2):
    print("Values are equal")

# Conversion
int_val = Value.int64(42)
double_val = int_val.coerce_to(TypeKind.TYPE_DOUBLE)

str_val = Value.string("123")
parsed_int = str_val.cast_to(TypeKind.TYPE_INT64)
```

---

### TypeFactory

**Class:** `zetasql.api.TypeFactory`

Factory for creating ZetaSQL type objects.

#### Static Methods

##### `create_simple_type(type_kind: TypeKind | int) -> Type`

Create a simple (primitive) type.

**Example:**
```python
from zetasql.api import TypeFactory
from zetasql.types import TypeKind

int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
string_type = TypeFactory.create_simple_type(TypeKind.TYPE_STRING)
```

##### `create_array_type(element_type: Type) -> Type`

Create an array type with given element type.

**Example:**
```python
int_type = TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
int_array_type = TypeFactory.create_array_type(int_type)
```

##### `create_struct_type(fields: list[tuple[str, Type]]) -> Type`

Create a struct type with named fields.

**Example:**
```python
struct_type = TypeFactory.create_struct_type([
    ("id", TypeFactory.create_simple_type(TypeKind.TYPE_INT64)),
    ("name", TypeFactory.create_simple_type(TypeKind.TYPE_STRING)),
])
```

##### `create_map_type(key_type: Type, value_type: Type) -> Type`

Create a map type with key and value types.

**Example:**
```python
map_type = TypeFactory.create_map_type(
    TypeFactory.create_simple_type(TypeKind.TYPE_STRING),
    TypeFactory.create_simple_type(TypeKind.TYPE_INT64)
)
```

---

### Builders

#### CatalogBuilder

**Class:** `zetasql.api.CatalogBuilder`

Fluent builder for creating `SimpleCatalog` objects.

```python
CatalogBuilder(name: str)
```

**Methods:**
- `add_table(table: SimpleTable) -> Self`
- `add_function(func: Function) -> Self`
- `add_constant(const: SimpleConstant) -> Self`
- `add_tvf(tvf: TableValuedFunction) -> Self`
- `with_builtin_functions(options: ZetaSQLBuiltinFunctionOptions) -> Self`
- `build() -> SimpleCatalog`

**Example:**
```python
from zetasql.api import CatalogBuilder
from zetasql.types import LanguageOptions, ZetaSQLBuiltinFunctionOptions

catalog = (
    CatalogBuilder("mydb")
    .add_table(users_table)
    .add_table(orders_table)
    .with_builtin_functions(
        ZetaSQLBuiltinFunctionOptions(
            language_options=LanguageOptions.maximum_features()
        )
    )
    .build()
)
```

#### TableBuilder

**Class:** `zetasql.api.TableBuilder`

Fluent builder for creating `SimpleTable` objects.

```python
TableBuilder(name: str)
```

**Methods:**
- `add_column(name: str, type_or_kind: Type | TypeKind | int, is_pseudo: bool = False) -> Self`
- `set_full_name(full_name: str) -> Self`
- `set_is_value_table(is_value: bool) -> Self`
- `allow_anonymous_columns() -> Self`
- `build() -> SimpleTable`

**Example:**
```python
from zetasql.api import TableBuilder
from zetasql.types import TypeKind

table = (
    TableBuilder("users")
    .add_column("id", TypeKind.TYPE_INT64)
    .add_column("name", TypeKind.TYPE_STRING)
    .add_column("email", TypeKind.TYPE_STRING)
    .add_column("created_at", TypeKind.TYPE_TIMESTAMP)
    .build()
)
```

#### FunctionBuilder

**Class:** `zetasql.api.FunctionBuilder`

Fluent builder for creating `Function` objects.

```python
FunctionBuilder(name: str, group: str = "")
```

**Methods:**
- `add_signature(signature: FunctionSignature) -> Self`
- `set_mode(mode: FunctionMode) -> Self`
- `build() -> Function`

**Example:**
```python
from zetasql.api import FunctionBuilder, SignatureBuilder
from zetasql.types import TypeKind, FunctionMode

signature = (
    SignatureBuilder()
    .add_argument(TypeKind.TYPE_INT64)
    .add_argument(TypeKind.TYPE_INT64)
    .set_result_type(TypeKind.TYPE_INT64)
    .build()
)

func = (
    FunctionBuilder("add_numbers")
    .add_signature(signature)
    .set_mode(FunctionMode.FUNCTION_MODE_SCALAR)
    .build()
)
```

#### SignatureBuilder

**Class:** `zetasql.api.SignatureBuilder`

Fluent builder for creating `FunctionSignature` objects.

**Methods:**
- `add_argument(type_or_kind: Type | TypeKind, cardinality: FunctionArgumentTypeCardinality = REQUIRED) -> Self`
- `set_result_type(type_or_kind: Type | TypeKind) -> Self`
- `build() -> FunctionSignature`

#### TVFBuilder

**Class:** `zetasql.api.TVFBuilder`

Fluent builder for Table-Valued Functions.

```python
TVFBuilder(name: str)
```

**Methods:**
- `add_input_argument(name: str, type_or_kind: Type | TypeKind) -> Self`
- `add_output_column(name: str, type_or_kind: Type | TypeKind) -> Self`
- `build() -> TableValuedFunction`

#### ConstantBuilder

**Class:** `zetasql.api.ConstantBuilder`

Fluent builder for creating constants.

```python
ConstantBuilder(name: str)
```

**Methods:**
- `set_type(type_or_kind: Type | TypeKind | int) -> Self`
- `build() -> SimpleConstant`

---

### Utility Functions

#### `create_table_content(rows_data: list[list[Any]]) -> TableContent`

Create TableContent from row data for query execution.

**Example:**
```python
from zetasql.api import create_table_content

data = create_table_content([
    [1, "Alice", "alice@example.com"],
    [2, "Bob", "bob@example.com"],
    [3, "Charlie", "charlie@example.com"]
])
```

---

## zetasql.types

ProtoModel classes and type definitions.

### ProtoModel Classes

Auto-generated dataclass-based models with protobuf conversion.

#### Key Classes

**Analyzer Types:**
- `AnalyzerOptions`: Configuration for SQL analysis
- `LanguageOptions`: Language feature flags
- `SimpleCatalog`: Catalog with tables, functions, constants
- `SimpleTable`: Table definition with columns
- `SimpleColumn`: Column definition
- `Type`: Type information
- `Function`: Function definition
- `FunctionSignature`: Function signature
- `TableValuedFunction`: TVF definition

**Resolved AST:**
- `ResolvedStatement`: Base for all statements
  - `ResolvedQueryStmt`: SELECT statements
  - `ResolvedInsertStmt`: INSERT statements
  - `ResolvedUpdateStmt`: UPDATE statements
  - etc.
- `ResolvedExpr`: Base for expressions
  - `ResolvedLiteral`: Literal values
  - `ResolvedColumnRef`: Column references
  - `ResolvedFunctionCall`: Function calls
  - etc.

**Parse Tree:**
- `ASTNode`: Base for all parse tree nodes
- `ASTStatement`: Parsed statement nodes
- `ASTExpression`: Parsed expression nodes

**Service Types:**
- `AnalyzeRequest`: Request for analysis
- `AnalyzeResponse`: Analysis result
- `EvaluateRequest`: Query execution request
- `EvaluateResponse`: Execution result

#### ProtoModel Features

All ProtoModel classes support:

```python
# Create from proto
model = ModelClass.from_proto(proto_obj)

# Convert to proto
proto = model.to_proto()

# Direct instantiation
model = ModelClass(field1=value1, field2=value2)

# Access fields
print(model.field_name)

# MRO-based inheritance
isinstance(resolved_literal, ResolvedExpr)  # True
```

### Enums

All enums are IntEnum compatible with protobuf values.

#### TypeKind

```python
from zetasql.types import TypeKind

TypeKind.TYPE_UNKNOWN
TypeKind.TYPE_INT32
TypeKind.TYPE_INT64
TypeKind.TYPE_UINT32
TypeKind.TYPE_UINT64
TypeKind.TYPE_BOOL
TypeKind.TYPE_FLOAT
TypeKind.TYPE_DOUBLE
TypeKind.TYPE_STRING
TypeKind.TYPE_BYTES
TypeKind.TYPE_DATE
TypeKind.TYPE_TIMESTAMP
TypeKind.TYPE_TIME
TypeKind.TYPE_DATETIME
TypeKind.TYPE_GEOGRAPHY
TypeKind.TYPE_NUMERIC
TypeKind.TYPE_BIGNUMERIC
TypeKind.TYPE_JSON
TypeKind.TYPE_ARRAY
TypeKind.TYPE_STRUCT
TypeKind.TYPE_PROTO
TypeKind.TYPE_ENUM
# ... and more
```

#### Other Important Enums

- `FunctionMode`: SCALAR, AGGREGATE, ANALYTIC
- `JoinType`: INNER, LEFT, RIGHT, FULL
- `SetOperationType`: UNION, INTERSECT, EXCEPT
- `LanguageFeature`: Feature flags for language options
- `ProductMode`: INTERNAL, EXTERNAL

---

## zetasql.core

Core layer for WASM communication and ProtoModel infrastructure.

### ZetaSqlLocalService

**Class:** `zetasql.core.ZetaSqlLocalService`

Singleton service for communication with ZetaSQL WASM layer.

#### Getting Instance

```python
from zetasql.core import ZetaSqlLocalService

service = ZetaSqlLocalService.get_instance()
```

#### Key Methods

##### `analyze(request: AnalyzeRequest) -> AnalyzeResponse`

Low-level SQL analysis.

##### `evaluate(request: EvaluateRequest) -> EvaluateResponse`

Low-level query execution.

##### `get_language_options(maximum_features: bool = False) -> LanguageOptions`

Get language options with optional all features enabled.

##### `get_builtin_functions(options: ZetaSQLBuiltinFunctionOptions) -> list[Function]`

Get list of builtin functions.

**Note:** Most users should use the high-level API (`zetasql.api`) instead of calling service methods directly.

---

## Error Handling

### ZetaSQLError

**Class:** `zetasql.core.exceptions.ZetaSQLError`

Base exception for all ZetaSQL errors.

```python
from zetasql.core.exceptions import ZetaSQLError

try:
    stmt = analyzer.analyze_statement(sql)
except ZetaSQLError as e:
    print(f"Analysis failed: {e}")
```

---

## Type Hints

All APIs include comprehensive type hints for IDE support:

```python
from zetasql.api import Analyzer
from zetasql.types import AnalyzerOptions, SimpleCatalog, ResolvedStatement

def analyze_sql(sql: str, catalog: SimpleCatalog) -> ResolvedStatement:
    analyzer = Analyzer(AnalyzerOptions(), catalog)
    return analyzer.analyze_statement(sql)
```

---

## See Also

- [Getting Started Guide](getting-started.md)
- [Architecture](architecture.md)
