# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Documentation

### Testing

## [0.1.3] - 2026-01-07

### Added

#### Core Features
- **Analyzer API**: High-level SQL analysis with both instance and static methods
  - `analyze_statement()` - Analyze SQL statements
  - `analyze_expression()` - Analyze SQL expressions
  - `analyze_next_statement()` - Parse multi-statement scripts
  - `build_statement()` - Build SQL from resolved AST
  - Statement type categorization (QUERY, DML, DDL, OTHER)
  
- **PreparedQuery**: Query execution with parameter binding
  - Builder pattern for fluent configuration
  - Context manager support
  - Parameter binding with type-safe Values
  - Table data injection via TableContent
  
- **PreparedExpression**: Expression evaluation
  - Builder pattern for configuration
  - Parameter and column binding
  - Type inference and validation
  
- **Value API**: Type-safe SQL value creation and manipulation
  - Factory methods for all SQL types (int64, string, array, struct, etc.)
  - Type-safe accessor methods
  - Comparison operations (equals, compare_to)
  - Type conversion (coerce_to, cast_to)
  - SQL literal generation
  
- **TypeFactory**: Complex type creation
  - Simple types
  - Array types
  - Struct types with named fields
  - Map types (key-value pairs)

#### Builder Patterns
- **CatalogBuilder**: Fluent API for building SimpleCatalog
  - Add tables, functions, constants, TVFs
  - Builtin function configuration
  
- **TableBuilder**: Fluent API for building SimpleTable
  - Add columns with types
  - Value table support
  - Anonymous column support
  
- **FunctionBuilder**: Custom function definition
  - Multiple signature support
  - Function mode configuration (SCALAR, AGGREGATE, ANALYTIC)
  
- **SignatureBuilder**: Function signature construction
  - Argument types and cardinality
  - Result type specification
  
- **TVFBuilder**: Table-valued function definition
  - Input arguments
  - Output columns
  
- **ConstantBuilder**: Constant definition

#### ProtoModel System
- Auto-generated dataclass-based wrappers for protobuf messages
- Real Python inheritance (no parent field chains)
- Bidirectional proto conversion (from_proto/to_proto)
- Full type hints and IDE support
- MRO-based automatic parent chain tracking
- 1000+ generated model classes covering all ZetaSQL protos

#### Script Analysis
- Extract table names from SQL scripts
- Multi-statement validation
- Script metadata extraction (tables, statement count)
- Statement-by-statement parsing with resume locations

#### Extensions
- `create_table_content()` - Factory for creating TableContent from row data
- Language options with maximum features support
- Builtin function configuration

### Changed
- Updated Python requirement to 3.10+ (from 3.9+)
- Improved error messages with better context
- Enhanced type hints throughout the API

### Documentation
- Comprehensive README with quick start guide
- Detailed Getting Started guide
- Complete API reference documentation
- Extensive examples covering all major features
- Architecture documentation explaining design decisions
- Updated contributing guidelines with code style and workflow

### Testing
- 100+ test cases covering all major features
- Integration tests for complete workflows
- Builder pattern tests
- Catalog operation tests
- Query execution tests
- Script analysis tests
- Value API tests
- Type system tests

## [0.1.0] - 2025-12-21

### Added
- Initial project structure
- Basic package setup with pyproject.toml
- Python 3.10+ support
- wasmtime dependency integration
- WebAssembly-based ZetaSQL integration
- Project documentation (README, CONTRIBUTING, LICENSE)
- Basic protobuf definitions
- WASM client infrastructure
- ZetaSqlLocalService singleton
- Core exception handling

[Unreleased]: https://github.com/heoh/zetasql-py/compare/v0.1.3...HEAD
[0.1.3]: https://github.com/heoh/zetasql-py/compare/v0.1.0...v0.1.3
[0.1.0]: https://github.com/heoh/zetasql-py/releases/tag/v0.1.0
