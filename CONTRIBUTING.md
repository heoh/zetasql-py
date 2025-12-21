# Contributing to ZetaSQL Python

Thank you for your interest in contributing to ZetaSQL Python! This document provides guidelines and instructions for contributing.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- pip

### Development Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/heoh/zetasql-py.git
cd zetasql-py
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e ".[dev]"
```

## Development Workflow

### Running Tests

```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=zetasql --cov-report=html
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions focused and small

### Making Changes

1. Create a new branch for your feature or bugfix:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and write tests

3. Ensure all tests pass:
```bash
pytest
```

4. Commit your changes:
```bash
git add .
git commit -m "Description of your changes"
```

5. Push to your fork:
```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request on GitHub

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Update documentation as needed
- Add entries to CHANGELOG.md for notable changes

## Reporting Issues

When reporting issues, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or stack traces

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Maintain a positive environment

## Questions?

Feel free to open an issue for questions or discussions about the project.

## License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.
