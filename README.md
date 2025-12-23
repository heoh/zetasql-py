# ZetaSQL

Python port of Google's ZetaSQL - SQL analysis and parsing library.

## About

This is a Python implementation of [ZetaSQL](https://github.com/google/zetasql), Google's SQL analyzer and parser. ZetaSQL provides SQL analysis capabilities including parsing, name resolution, type checking, and more.

This Python port aims to bring ZetaSQL's powerful SQL analysis features to the Python ecosystem.

## Installation

Install via pip:

```bash
pip install zetasql
```

## Requirements

- Python 3.9 or higher
- wasmtime

## Quick Start

```python
import zetasql

# (Example usage will be added)
```

## Features

### ResolvedAST Wrapper Classes

ZetaSQL proto messages use parent field chains for inheritance. This library provides convenient Python wrapper classes with real inheritance for better IDE support and cleaner code.

**Problem:** Proto messages have deep parent chains
```python
# Proto way - cumbersome parent chain access
literal_proto = resolved_ast_pb2.ResolvedLiteralProto()
type_kind = literal_proto.parent.type.type_kind  # 😞 Deep nesting
parse_loc = literal_proto.parent.parent.parse_location_range  # 😞 Even deeper
```

**Solution:** Python wrappers with real inheritance
```python
from zetasql.resolved_ast_wrapper import ResolvedLiteral

# Wrapper way - clean and IDE-friendly
literal = ResolvedLiteral(literal_proto)
type_kind = literal.type.type_kind  # ✨ Direct access
parse_loc = literal.parse_location_range  # ✨ Inherited properties work!
```

**Type checking works too:**
```python
isinstance(literal, ResolvedLiteral)  # True
isinstance(literal, ResolvedExpr)     # True - real inheritance!
isinstance(literal, ResolvedNode)     # True
```

**IDE Autocompletion:** All properties have proper type hints, so your IDE can autocomplete fields from parent classes.

### Regenerating Wrappers

After proto file changes, regenerate the wrapper classes:

```bash
python scripts/generate_wrappers.py
```

This will scan all `_pb2.py` files and generate wrapper classes with proper inheritance chains based on proto parent fields.

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/heoh/zetasql-py.git
cd zetasql-py

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Building the Package

```bash
python -m build
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

This is a Python port of Google's ZetaSQL, which is also licensed under Apache 2.0.

## Acknowledgments

- Original ZetaSQL project: https://github.com/google/zetasql
- This is an unofficial Python port and is not affiliated with Google
