#!/bin/bash
#
# org-to-post.sh - Convert org-mode file to Jekyll blog post
#
# Usage: ./scripts/org-to-post.sh _org/blog/my-post.org [--draft]
#
# Features:
# - Extracts front matter from org properties
# - Converts org to markdown via pandoc
# - Resolves citations from Zotero via Better BibTeX
# - Generates bibliography in Vancouver/NLM style
#
# Org file format:
# #+TITLE: My Post Title
# #+DATE: 2026-02-11
# #+DESCRIPTION: A brief description
# #+TAGS: tag1 tag2 tag3
# #+BIBLIOGRAPHY: citekey1 citekey2 citekey3
#
# Citations in text: [cite:@citekey] or [cite:@key1;@key2]

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
CSL_FILE="$REPO_DIR/_csl/vancouver.csl"
ZOTERO_EXPORT="$HOME/.pi/agent/skills/zotero/export-bibtex.sh"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check arguments
if [ -z "$1" ]; then
    echo -e "${RED}Usage: $0 <org-file> [--draft]${NC}"
    echo "  org-file: Path to .org file (e.g., _org/blog/my-post.org)"
    echo "  --draft:  Save to _drafts instead of _posts"
    exit 1
fi

ORG_FILE="$1"
IS_DRAFT=false
[ "$2" = "--draft" ] && IS_DRAFT=true

if [ ! -f "$ORG_FILE" ]; then
    echo -e "${RED}Error: File not found: $ORG_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}Converting: $ORG_FILE${NC}"

# Extract metadata from org file (trim leading/trailing whitespace)
TITLE=$(grep -i "^#+TITLE:" "$ORG_FILE" | sed 's/^#+TITLE:\s*//' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | head -1)
DATE=$(grep -i "^#+DATE:" "$ORG_FILE" | sed 's/^#+DATE:\s*//' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | head -1)
DESCRIPTION=$(grep -i "^#+DESCRIPTION:" "$ORG_FILE" | sed 's/^#+DESCRIPTION:\s*//' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | head -1)
TAGS=$(grep -i "^#+TAGS:" "$ORG_FILE" | sed 's/^#+TAGS:\s*//' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | head -1)
CITEKEYS=$(grep -i "^#+BIBLIOGRAPHY:" "$ORG_FILE" | sed 's/^#+BIBLIOGRAPHY:\s*//' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//' | head -1)

# Default date to today if not specified
[ -z "$DATE" ] && DATE=$(date +%Y-%m-%d)

# Generate slug from title
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')

echo "  Title: $TITLE"
echo "  Date: $DATE"
echo "  Slug: $SLUG"
[ -n "$TAGS" ] && echo "  Tags: $TAGS"
[ -n "$CITEKEYS" ] && echo "  Citations: $CITEKEYS"

# Create temporary files
TMP_DIR=$(mktemp -d)
TMP_BIB="$TMP_DIR/references.bib"
TMP_MD="$TMP_DIR/content.md"

# Export BibTeX for each citekey from Zotero
if [ -n "$CITEKEYS" ]; then
    echo -e "${YELLOW}Fetching citations from Zotero...${NC}"
    > "$TMP_BIB"  # Clear/create bib file
    
    for citekey in $CITEKEYS; do
        echo "  Fetching: $citekey"
        if [ -x "$ZOTERO_EXPORT" ]; then
            "$ZOTERO_EXPORT" "$citekey" >> "$TMP_BIB" 2>/dev/null || \
                echo -e "${YELLOW}  Warning: Could not fetch $citekey${NC}"
        else
            echo -e "${YELLOW}  Warning: Zotero export script not found${NC}"
        fi
    done
    
    # Check if we got any citations
    if [ -s "$TMP_BIB" ]; then
        BIB_ENTRIES=$(grep -c "^@" "$TMP_BIB" || echo 0)
        echo -e "${GREEN}  Fetched $BIB_ENTRIES citation(s)${NC}"
    fi
fi

# Convert org to markdown with pandoc
echo -e "${YELLOW}Converting org to markdown...${NC}"

PANDOC_ARGS=(
    "$ORG_FILE"
    -f org
    -t gfm
    --wrap=none
)

# Add citation processing if we have a bibliography
if [ -s "$TMP_BIB" ]; then
    PANDOC_ARGS+=(
        --citeproc
        --bibliography="$TMP_BIB"
        --csl="$CSL_FILE"
        -M link-citations=true
    )
fi

pandoc "${PANDOC_ARGS[@]}" -o "$TMP_MD"

# Determine output path
if [ "$IS_DRAFT" = true ]; then
    OUTPUT_DIR="$REPO_DIR/blog/_drafts"
    OUTPUT_FILE="$OUTPUT_DIR/$SLUG.md"
else
    OUTPUT_DIR="$REPO_DIR/blog/_posts"
    OUTPUT_FILE="$OUTPUT_DIR/$DATE-$SLUG.md"
fi

mkdir -p "$OUTPUT_DIR"

# Build front matter and clean up content
{
    echo "---"
    echo "title: \"$TITLE\""
    echo "date: $DATE"
    [ -n "$DESCRIPTION" ] && echo "description: \"$DESCRIPTION\""
    if [ -n "$TAGS" ]; then
        # Convert space-separated tags to YAML array
        TAGS_YAML=$(echo "$TAGS" | sed 's/ /, /g')
        echo "tags: [$TAGS_YAML]"
    fi
    echo "---"
    echo ""
    # Process content: remove org metadata and clean up pandoc artifacts
    cat "$TMP_MD" | \
        grep -v "^#+\(TITLE\|DATE\|DESCRIPTION\|TAGS\|BIBLIOGRAPHY\):" | \
        sed '/^```{=org}$/,/^```$/d' | \
        sed 's/^:::.*//g' | \
        sed '/^$/N;/^\n$/d'  # Remove multiple blank lines
} > "$OUTPUT_FILE"

# Clean up
rm -rf "$TMP_DIR"

echo -e "${GREEN}✓ Created: $OUTPUT_FILE${NC}"
echo ""
echo "Preview URL: http://localhost:4000/blog/$SLUG/"
