#!/bin/bash
set -e

# Protocol Buffer compilation script for ZetaSQL
# This script compiles .proto files to Python _pb2.py and _pb2_grpc.py files

SCRIPT_DIR=$(dirname "${BASH_SOURCE[0]}")
PROJECT_ROOT=$(realpath "${SCRIPT_DIR}/..")
PROTO_SRC="$PROJECT_ROOT/src/zetasql/wasi/proto"
PROTO_OUT="$PROJECT_ROOT/src/zetasql/wasi/_pb2"

echo "========================================"
echo "Building ZetaSQL Protocol Buffers"
echo "========================================"
echo "Source: $PROTO_SRC"
echo "Output: $PROTO_OUT"
echo ""

# Check if proto source directory exists
if [ ! -d "$PROTO_SRC" ]; then
    echo "Error: Proto source directory not found: $PROTO_SRC"
    echo "Please extract proto files to $PROTO_SRC first"
    exit 1
fi

# Check if grpcio-tools is installed
if ! python -c "import grpc_tools" 2>/dev/null; then
    echo "Error: grpcio-tools is not installed"
    echo "Please install with: pip install grpcio-tools"
    exit 1
fi

# Clear old generated files
echo "Cleaning old generated files..."
rm -rf "$PROTO_OUT"
mkdir -p "$PROTO_OUT"

# Find all .proto files, excluding test files with intentional errors
PROTO_FILES=$(find "$PROTO_SRC" -name "*.proto" ! -path "*/testdata/*" ! -path "*/test_*")
if [ -z "$PROTO_FILES" ]; then
    echo "Warning: No .proto files found in $PROTO_SRC"
    exit 0
fi

echo "Found proto files (excluding testdata):"
echo "$PROTO_FILES" | while read -r file; do
    echo "  - ${file#$PROTO_SRC/}"
done
echo ""

# Generate Python protobuf files
echo "Generating Python files..."
python -m grpc_tools.protoc \
    --proto_path="$PROTO_SRC" \
    --python_out="$PROTO_OUT" \
    --pyi_out="$PROTO_OUT" \
    $PROTO_FILES

# Fix imports in generated files (convert absolute imports to package-relative)
echo "Fixing imports in generated files..."
find "$PROTO_OUT" -name "*_pb2*.py" -type f | while read -r file; do
    # Convert "from zetasql.X import Y" to "from zetasql.wasi._pb2.zetasql.X import Y"
    sed -i.bak 's|from zetasql\.|from zetasql.wasi._pb2.zetasql.|g' "$file"
    
    # Convert "import foo_pb2" to "from . import foo_pb2" for same-directory imports
    sed -i.bak 's/^import \([a-zA-Z0-9_]*\)_pb2 as \([a-zA-Z0-9_]*\)$/from . import \1_pb2 as \2/g' "$file"
    sed -i.bak 's/^import \([a-zA-Z0-9_]*\)_pb2$/from . import \1_pb2/g' "$file"
    rm -f "${file}.bak"
done

# Also fix .pyi stub files
find "$PROTO_OUT" -name "*_pb2.pyi" -type f | while read -r file; do
    # Convert "from zetasql.X import Y" to "from zetasql.wasi._pb2.zetasql.X import Y"
    sed -i.bak 's|from zetasql\.|from zetasql.wasi._pb2.zetasql.|g' "$file"
    rm -f "${file}.bak"
done

# Create __init__.py files in all directories
echo "Creating __init__.py files..."
find "$PROTO_OUT" -type d -exec touch {}/__init__.py \;

# Create root __init__.py with docstring
cat > "$PROTO_OUT/__init__.py" << 'EOF'
"""Generated protocol buffer Python modules.

This package contains auto-generated code from .proto files.
Do not edit these files manually - they will be overwritten.

To regenerate:
    ./scripts/build_protos.sh
"""
EOF

echo ""
echo "========================================"
echo "Proto compilation complete!"
echo "========================================"
echo "Generated files are in: $PROTO_OUT"
echo ""
echo "Note: Remember to commit the generated files to version control"
echo "      for reproducible builds and user convenience."
