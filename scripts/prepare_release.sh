#!/bin/bash
set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  ZetaSQL-py Release Preparation${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ] || [ ! -f "CHANGELOG.md" ]; then
    echo -e "${RED}Error: Must be run from the project root directory${NC}"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
echo -e "${YELLOW}Current version: ${CURRENT_VERSION}${NC}"
echo ""

# Prompt for new version
read -p "Enter new version (e.g., 0.1.3): " NEW_VERSION

if [ -z "$NEW_VERSION" ]; then
    echo -e "${RED}Error: Version cannot be empty${NC}"
    exit 1
fi

# Validate version format (basic semver check)
if ! [[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo -e "${RED}Error: Invalid version format. Use semantic versioning (e.g., 0.1.3)${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}Preparing release for version: ${NEW_VERSION}${NC}"
echo ""

# Check for [Unreleased] section in CHANGELOG
if ! grep -q "## \[Unreleased\]" CHANGELOG.md; then
    echo -e "${RED}Error: No [Unreleased] section found in CHANGELOG.md${NC}"
    exit 1
fi

# Show unreleased changes
echo -e "${GREEN}📋 Unreleased changes in CHANGELOG.md:${NC}"
echo -e "${YELLOW}----------------------------------------${NC}"

# Extract content between [Unreleased] and the next version section
awk '/## \[Unreleased\]/,/## \[[0-9]/' CHANGELOG.md | grep -v "## \[[0-9]" | sed '1d'

echo -e "${YELLOW}----------------------------------------${NC}"
echo ""

# Confirm
read -p "Do you want to create release v${NEW_VERSION}? (y/N): " CONFIRM

if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo -e "${YELLOW}Release preparation cancelled${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}Creating and pushing tag v${NEW_VERSION}...${NC}"

# Create tag
TAG_NAME="v${NEW_VERSION}"
git tag "$TAG_NAME"

if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to create tag${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Created tag: ${TAG_NAME}${NC}"

# Push tag
git push origin "$TAG_NAME"

if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to push tag. You may need to delete the local tag:${NC}"
    echo -e "${RED}  git tag -d ${TAG_NAME}${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Pushed tag to origin${NC}"
echo ""

# Instructions
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ Tag created successfully!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Go to: https://github.com/heoh/zetasql-py/releases/new?tag=${TAG_NAME}"
echo "2. Create a GitHub Release from the tag"
echo "3. The GitHub Actions workflow will automatically:"
echo "   - Update CHANGELOG.md"
echo "   - Update version in pyproject.toml and __version__.py"
echo "   - Build the package"
echo "   - Upload wheel and sdist to the release"
echo "   - Publish to PyPI"
echo ""
echo -e "${BLUE}Note: Make sure you have set the PYPI_API_TOKEN secret in your repository!${NC}"
