# Execute Query Demo - LocalService and Wrapper Usage Guide

This demo (`execute_query_demo.py`) provides comprehensive examples of using ZetaSQL's `LocalService` API and `Wrapper` classes to parse, analyze, and execute SQL queries. It implements functionality similar to ZetaSQL's `execute_query` command-line tool.

## Overview

The demo showcases four main operational modes:

1. **Parse Mode**: Convert SQL text to Abstract Syntax Tree (AST)
2. **Analyze Mode**: Perform semantic analysis with catalog resolution
3. **Execute Mode**: Run queries with sample data and display results
4. **Unanalyze Mode**: Convert resolved AST back to formatted SQL

Additionally, it demonstrates error handling for common SQL mistakes.

## Sample Database Schema

The demo uses a realistic e-commerce database with three tables:

### Customers Table
| Column | Type | Description |
|--------|------|-------------|
| customer_id | INT64 | Primary key |
| name | STRING | Customer full name |
| email | STRING | Email address |
| country | STRING | Country of residence |

**Sample Size**: 15 customers from various countries (USA, Canada, UK, Australia, Germany, South Korea, China, Spain)

### Products Table
| Column | Type | Description |
|--------|------|-------------|
| product_id | INT64 | Primary key |
| name | STRING | Product name |
| category | STRING | Product category |
| unit_price | DOUBLE | Price per unit |

**Sample Size**: 12 products across categories (Electronics, Furniture, Stationery, Appliances, Accessories)

### Orders Table
| Column | Type | Description |
|--------|------|-------------|
| order_id | INT64 | Primary key |
| customer_id | INT64 | Foreign key to Customers |
| product_id | INT64 | Foreign key to Products |
| quantity | INT64 | Number of items ordered |
| price | DOUBLE | Total order price |
| status | STRING | Order status (Delivered, Shipped, Processing, Cancelled) |

**Sample Size**: 20 orders with various statuses and values

## Examples Breakdown

### Example 1: Parse Mode - AST Traversal

**Purpose**: Demonstrates how to parse SQL and traverse the resulting Abstract Syntax Tree.

**APIs Used**:
- `LocalService.parse(sql)` - Parse SQL text to AST

**Techniques**:
- **Shallow Traversal** (depth=2): Quick overview of query structure
- **Deep Traversal** (full tree): Complete AST exploration with all fields

**Query Example**:
```sql
SELECT 
    c.name,
    c.country,
    COUNT(*) as order_count
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Delivered'
GROUP BY c.name, c.country
HAVING COUNT(*) > 1
ORDER BY order_count DESC
```

**What You'll Learn**:
- How to access parse tree nodes via protobuf messages
- Recursive traversal patterns for AST exploration
- Difference between shallow and deep inspection
- Handling parent references to avoid infinite loops

**Output**: Tree-structured view of AST nodes with field names and values

---

### Example 2: Analyze Mode - Semantic Analysis

**Purpose**: Shows semantic analysis with catalog resolution to produce a ResolvedAST.

**APIs Used**:
- `LocalService.analyze(sql, simple_catalog)` - Semantic analysis with catalog

**Wrapper Classes Demonstrated**:
- Base wrapper navigation through resolved nodes
- Node type identification using `DESCRIPTOR.name`

**Query Example**:
```sql
SELECT 
    c.name as customer_name,
    p.name as product_name,
    o.quantity,
    o.price
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Products p ON o.product_id = p.product_id
WHERE o.status = 'Delivered' AND o.quantity > 1
ORDER BY o.price DESC
LIMIT 10
```

**What You'll Learn**:
- How ResolvedAST differs from parse tree
- Extracting semantic information (tables, columns, joins, filters)
- Identifying scan types (TableScan, JoinScan, FilterScan, ProjectScan)
- Traversing resolved nodes with complete field inspection

**Output**: 
- Tree-structured resolved AST with all fields displayed
- Summary statistics (tables, columns, joins, filters, aggregates)

---

### Example 3: Execute Mode - Query Execution

**Purpose**: Demonstrates executing queries with sample data and formatting results.

**APIs Used**:
- `LocalService.prepare_query(sql, simple_catalog)` - Prepare query for execution
- `LocalService.evaluate_query(prepared_query_id, table_content)` - Execute with data
- `LocalService.unprepare_query(prepared_query_id)` - Cleanup resources

**Helper Functions**:
- `create_table_content(rows_data)` - Build TableContent protobuf from Python lists
- `print_table_result(columns, rows)` - Format results as ASCII table

**Query Example**:
```sql
SELECT 
    c.name as customer_name,
    c.country,
    p.name as product_name,
    p.category,
    o.quantity,
    o.price,
    o.status
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Products p ON o.product_id = p.product_id
WHERE o.status IN ('Delivered', 'Shipped')
ORDER BY o.price DESC
LIMIT 15
```

**What You'll Learn**:
- How to structure table data for query execution
- Type mapping between Python values and protobuf cells
- Extracting and formatting query results
- Proper resource cleanup with unprepare_query

**Output**: ASCII table with columns, separators, and 15 result rows

---

### Example 4: Error Handling

**Purpose**: Shows proper error handling for common SQL mistakes.

**Error Cases**:
1. **Non-existent Table**: References a table not in the catalog
2. **Type Mismatch**: Invalid operations between incompatible types

**Queries**:
```sql
-- Error 1: Table not found
SELECT * FROM NonExistentTable

-- Error 2: Type mismatch (adding INT + STRING)
SELECT customer_id + name FROM Customers
```

**What You'll Learn**:
- Exception types thrown by ZetaSQL
- Error message format and information
- Proper try-except patterns for ZetaSQL operations

**Output**: Caught exceptions with error type and descriptive messages

---

### Example 5: Unanalyze & Format Mode

**Purpose**: Demonstrates converting ResolvedAST back to SQL and formatting.

**APIs Used**:
- `LocalService.analyze(sql, simple_catalog)` - Create ResolvedAST
- `LocalService.build_sql(resolved_statement)` - Convert ResolvedAST to SQL (unanalyze)
- `LocalService.format_sql(sql)` - Pretty-print SQL

**Query Example**:
```sql
SELECT c.country, COUNT(*) as customer_count, 
SUM(o.price) as total_revenue
FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Delivered'
GROUP BY c.country HAVING SUM(o.price) > 500
ORDER BY total_revenue DESC
```

**What You'll Learn**:
- How to regenerate SQL from analyzed queries
- SQL formatting and pretty-printing
- Comparing original vs regenerated SQL
- Use cases for SQL transformation pipelines

**Output**: 
- Original SQL (unformatted)
- Regenerated SQL from ResolvedAST
- Formatted version for readability

---

## Running the Demo

### Prerequisites

Ensure zetasql-py is installed:

```bash
pip install -e .
```

### Execute All Examples

```bash
cd examples
python execute_query_demo.py
```

### Expected Output Structure

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    Execute Query Demo - LocalService                       ║
║                       and Wrapper Usage Examples                           ║
╚════════════════════════════════════════════════════════════════════════════╝

Initializing ZetaSQL LocalService...
Setting up catalog with 3 tables: Customers, Products, Orders...
✓ Catalog ready with sample data

================================================================================
  Example 1: Parse Mode - AST Traversal
================================================================================

SQL Query:
...

--- Shallow AST Traversal (depth=2) ---
...

--- Deep AST Traversal (full tree) ---
...

================================================================================
  Example 2: Analyze Mode - Semantic Analysis
================================================================================
...

[continues with all examples]
```

## Key Components

### Helper Functions

#### `create_table_content(rows_data)`
Converts Python lists to ZetaSQL's TableContent protobuf format. Automatically handles type detection for:
- `None` → NULL
- `bool` → bool_value
- `int` → int64_value
- `float` → double_value
- `str` → string_value

**Usage**:
```python
data = [
    [1, "Alice", True],
    [2, "Bob", False],
]
table_content = create_table_content(data)
```

#### `print_table_result(columns, rows)`
Formats query results as ASCII tables with:
- Automatic column width calculation
- Header row with column names
- Separator line
- Aligned data rows
- Row count summary

**Usage**:
```python
columns = ["id", "name", "active"]
rows = [[1, "Alice", True], [2, "Bob", False]]
print_table_result(columns, rows)
```

Output:
```
id | name  | active
---+-------+-------
1  | Alice | True
2  | Bob   | False

(2 rows)
```

### Catalog Setup

The `setup_catalog_and_data()` function demonstrates:
- Creating `SimpleCatalogProto` with multiple tables
- Defining table schemas with typed columns
- Populating realistic sample data
- Returning both catalog and table content

## Learning Path

### For Beginners
1. Start with **Example 1** (Parse) to understand AST basics
2. Move to **Example 3** (Execute) to see end-to-end query execution
3. Review helper functions to understand data preparation

### For Intermediate Users
1. Study **Example 2** (Analyze) for semantic analysis patterns
2. Explore **Example 5** (Unanalyze) for SQL transformation
3. Examine error handling patterns in **Example 4**

### For Advanced Users
1. Modify traversal functions to extract specific information
2. Add custom wrapper classes for type-safe node access
3. Extend catalog with user-defined functions or types
4. Implement query optimization analysis

## Comparison to basic_usage.py

While `basic_usage.py` demonstrates 10 incremental examples focusing on individual features, `execute_query_demo.py` provides:

- **Real-world scenarios**: Multi-table joins, aggregations, filtering
- **Complete workflows**: End-to-end parse → analyze → execute pipelines
- **Production patterns**: Error handling, resource cleanup, result formatting
- **Deeper exploration**: Full AST/ResolvedAST traversal with all fields
- **Practical utilities**: Reusable helper functions for common tasks

Both examples complement each other:
- Use `basic_usage.py` to learn individual API calls
- Use `execute_query_demo.py` to see how they combine in real applications

## API Reference Quick Links

### LocalService Methods
- `parse(sql)` - Parse SQL to AST
- `analyze(sql, simple_catalog)` - Semantic analysis
- `prepare_query(sql, simple_catalog)` - Prepare for execution
- `evaluate_query(prepared_query_id, table_content)` - Execute query
- `unprepare_query(prepared_query_id)` - Cleanup prepared query
- `build_sql(resolved_statement)` - ResolvedAST to SQL
- `format_sql(sql)` - Format SQL for readability

### Protobuf Messages
- `SimpleCatalogProto` - Catalog definition
- `TableContent` - Table data for execution
- `ParseResponse` - Contains parsed AST
- `AnalyzeResponse` - Contains ResolvedAST
- `EvaluateQueryResponse` - Contains query results

## Troubleshooting

### Common Issues

**Issue**: `ImportError: No module named zetasql`
**Solution**: Install the package: `pip install -e .` from project root

**Issue**: Infinite recursion in AST traversal
**Solution**: Always maintain a `visited` set and skip `parent` fields

**Issue**: Type errors when creating table content
**Solution**: Ensure Python types match expected SQL types (use `int` for INT64, not numpy types)

**Issue**: Queries fail with "Table not found"
**Solution**: Verify table names in catalog match exactly (case-sensitive)

## Next Steps

After understanding this demo:

1. **Experiment**: Modify queries and see how AST/ResolvedAST changes
2. **Extend**: Add more tables and complex joins
3. **Analyze**: Extract query statistics (join count, filter complexity)
4. **Transform**: Build query rewriting tools using parse → modify → build_sql
5. **Optimize**: Analyze execution plans (future: explain mode)

## Contributing

Found issues or have improvements? See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

This demo is part of zetasql-py and follows the same license. See [LICENSE](../LICENSE).
