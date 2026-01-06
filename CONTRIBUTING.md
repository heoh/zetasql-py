# Contributing to ZetaSQL Python

Thank you for your interest in contributing to ZetaSQL Python! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Code Generation](#code-generation)
- [Project Structure](#project-structure)
- [Reporting Issues](#reporting-issues)

## Getting Started

### Prerequisites

- **Python 3.10+** (required)
- **Git** for version control
- **pip** package manager
- **ruff** for linting/formatting (installed with dev dependencies)

### Development Setup

1. **Fork and clone the repository:**
```bash
git clone https://github.com/heoh/zetasql-py.git
cd zetasql-py
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in development mode:**
```bash
pip install -e ".[dev]"
```

This installs the package in editable mode along with development dependencies:
- pytest (testing framework)
- pytest-cov (coverage reporting)
- ruff (linter and formatter)
- grpcio-tools (proto compilation)

4. **Verify installation:**
```bash
python -c "import zetasql; print(zetasql.__version__)"
pytest --version
ruff --version
```

## Development Workflow

### Making Changes

1. **Create a new branch:**
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions/modifications

2. **Make your changes:**
   - Write clean, readable code
   - Add/update tests for your changes
   - Update documentation as needed
   - Follow the code style guidelines

3. **Run tests locally:**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_analyzer.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=zetasql --cov-report=html
```

4. **Check code style:**
```bash
# Check for issues
ruff check src/ tests/

# Format code
ruff format src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/
```

5. **Commit your changes:**
```bash
git add .
git commit -m "Short description of changes

Longer explanation if needed. Reference issues like #123.
"
```

**Commit Message Guidelines:**
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be ≤50 characters
- Reference issues and PRs when applicable
- Provide context in the body for complex changes

6. **Push to your fork:**
```bash
git push origin feature/your-feature-name
```

7. **Open a Pull Request on GitHub**

## Code Style

### Python Style Guidelines

We use **Ruff** for consistent code formatting and linting.

**Configuration:** See `pyproject.toml`:
- Line length: 120 characters
- Target Python: 3.10+
- Quote style: Double quotes
- Indent: 4 spaces

**Rules enforced:**
- `E` - pycodestyle errors
- `F` - pyflakes
- `B` - flake8-bugbear
- `SIM` - flake8-simplify
- `I` - isort (import sorting)
- `UP` - pyupgrade
- `C4` - flake8-comprehensions
- `RUF` - Ruff-specific rules

**Excluded paths:**
- `src/zetasql/wasi/` - Auto-generated protobuf code
- `src/zetasql/types/proto_model/generated.py` - Auto-generated ProtoModels

### Type Hints

**Required for all public APIs:**
```python
from typing import Optional
from zetasql.types import AnalyzerOptions, SimpleCatalog

def analyze_sql(
    sql: str,
    options: AnalyzerOptions,
    catalog: Optional[SimpleCatalog] = None
) -> ResolvedStatement:
    """Analyze SQL statement."""
    ...
```

### Docstrings

**Use Google-style docstrings:**
```python
def function_name(param1: int, param2: str) -> bool:
    """Short description.

    Longer description if needed, explaining the function's
    purpose, behavior, and usage.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ZetaSQLError: When analysis fails

    Example:
        >>> function_name(42, "hello")
        True
    """
```

### Code Organization

**Import Order:**
1. Standard library imports
2. Third-party imports
3. Local imports

```python
import datetime
from typing import Optional

import pytest

from zetasql.api import Analyzer
from zetasql.core import ZetaSqlLocalService
from zetasql.types import AnalyzerOptions
```

## Testing

### Test Structure

```
tests/
├── test_analyzer.py           # Analyzer API tests
├── test_script_analysis.py    # Script analysis tests
├── builders/                  # Builder pattern tests
├── catalog/                   # Catalog operations tests
├── core/                      # Core layer tests
├── execution/                 # Query execution tests
├── extensions/                # Extension feature tests
├── integration/               # Integration tests
└── types/                     # Type system tests
```

### Writing Tests

**Use pytest fixtures:**
```python
import pytest
from zetasql.api import Analyzer, CatalogBuilder
from zetasql.types import AnalyzerOptions

@pytest.fixture
def analyzer(options, catalog):
    """Create analyzer for testing."""
    return Analyzer(options, catalog)

def test_analyze_statement(analyzer):
    """Test statement analysis."""
    stmt = analyzer.analyze_statement("SELECT 1")
    assert stmt is not None
```

**Test naming conventions:**
- Test files: `test_*.py`
- Test classes: `Test*`
- Test functions: `test_*`

**Good test practices:**
1. One assertion per test (when practical)
2. Use descriptive test names
3. Test both success and failure cases
4. Include edge cases
5. Mock external dependencies when appropriate

### Running Tests

```bash
# All tests
pytest

# Specific module
pytest tests/test_analyzer.py

# Specific test
pytest tests/test_analyzer.py::TestAnalyzer::test_analyze_statement

# With coverage
pytest --cov=zetasql --cov-report=html

# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run only failed tests
pytest --lf
```

## Pull Request Guidelines

### Before Submitting

**Checklist:**
- [ ] Tests pass locally (`pytest`)
- [ ] Code follows style guidelines (`ruff check`)
- [ ] Code is formatted (`ruff format`)
- [ ] Documentation updated if needed
- [ ] CHANGELOG.md updated for notable changes
- [ ] Type hints added for new public APIs
- [ ] Docstrings added/updated

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Related Issues
Fixes #123
Related to #456

## Checklist
- [ ] Tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

### Review Process

1. **Automated checks** will run on your PR
2. **Maintainer review** will provide feedback
3. **Address feedback** by pushing new commits
4. **Approval** and merge once ready

## Code Generation

### ProtoModel Generation

After updating protobuf definitions:

```bash
python scripts/generate_proto_models.py \
    --proto-dir src/zetasql/wasi/_pb2 \
    --output src/zetasql/types/proto_model/generated.py
```

**What it does:**
- Scans all `_pb2.py` files
- Extracts message definitions and parent relationships
- Generates dataclass-based ProtoModel wrappers
- Creates inheritance hierarchies

**When to regenerate:**
- After updating WASM binary with new proto versions
- When proto definitions change
- When adding new message types

### Proto Compilation

If you need to recompile proto files:

```bash
./scripts/build_protos.sh
```

**Note:** Usually not needed unless working on WASM layer.

## Project Structure

Understanding the codebase:

```
src/zetasql/
├── __init__.py           # Package init
├── __version__.py        # Version info
├── wasi/                 # Layer 0: WASM & Protobuf
│   ├── *.wasm           # WebAssembly binary
│   ├── _pb2/            # Generated protobuf code
│   └── proto/           # Original .proto files
├── core/                 # Layer 1: Infrastructure
│   ├── local_service.py # WASM communication
│   ├── wasm_client.py   # WASM client
│   ├── exceptions.py    # Exception definitions
│   └── func_utils.py    # Utility functions
├── types/                # ProtoModel & Types
│   ├── __init__.py      # Type exports
│   └── proto_model/     # ProtoModel system
│       ├── generated.py # Auto-generated models
│       ├── proto_model.py # Base classes
│       └── extensions/  # Custom extensions
└── api/                  # Layer 2: User-facing API
    ├── analyzer.py      # Analyzer class
    ├── prepared_query.py # Query execution
    ├── prepared_expression.py # Expression evaluation
    ├── value.py         # Value API
    ├── type_factory.py  # Type creation
    ├── table_content.py # Table data
    └── builders/        # Builder patterns
        ├── catalog_builder.py
        ├── table_builder.py
        ├── function_builder.py
        └── ...
```

## Reporting Issues

### Bug Reports

Include:
- **Python version** (`python --version`)
- **Package version** (`pip show zetasql`)
- **Operating system**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Error messages** (full stack traces)
- **Minimal code example**

### Feature Requests

Include:
- **Use case** - Why is this feature needed?
- **Proposed API** - What should the interface look like?
- **Alternatives** - What alternatives have you considered?
- **Examples** - Code examples of how it would be used

### Questions

For questions:
- Check [documentation](docs/) first
- Search [existing issues](https://github.com/heoh/zetasql-py/issues)
- Open a new issue with "Question:" prefix

## Code of Conduct

### Our Standards

- **Be respectful and inclusive** of all contributors
- **Welcome newcomers** and help them get started
- **Provide constructive feedback** in code reviews
- **Accept criticism gracefully** and learn from it
- **Focus on what is best** for the community

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling, insulting comments, or personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## Getting Help

- **Documentation:** [docs/](docs/)
- **Examples:** [docs/EXAMPLES.md](docs/EXAMPLES.md)
- **Issues:** [GitHub Issues](https://github.com/heoh/zetasql-py/issues)

Thank you for contributing! 🎉
- Focus on constructive feedback
- Maintain a positive environment

## Questions?

Feel free to open an issue for questions or discussions about the project.

## License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.
