#!/bin/bash
#
# org-to-post.sh - Convert org-mode file to Jekyll blog post
#
# Usage: ./scripts/org-to-post.sh blog/_org/my-post.org [--draft] [--force]
#        ./scripts/org-to-post.sh blog/_org/my-post/my-post.org [--draft] [--force]
#
# Features:
# - Extracts front matter from org keywords, emitted as safe YAML
# - Converts org to markdown via pandoc (org `*` becomes <h2>, so the post
#   layout's title stays the page's only <h1>)
# - Resolves citations from Zotero and FAILS if any citekey does not resolve
# - Generates a bibliography in Vancouver/NLM style
# - Copies images referenced relative to the org file ([[file:figures/a.png]])
#   into assets/images/blog/<slug>/ and rewrites the links, so a post can live
#   in its own folder next to the code and data that produced its figures
#
# Org file format:
# #+TITLE: My Post Title
# #+DATE: 2026-02-11            (or an org timestamp: <2026-02-11 Wed>)
# #+UPDATED: 2026-03-01         (optional; last substantive revision)
# #+DESCRIPTION: A brief description
# #+TAGS: tag1 tag2 tag3        (REQUIRED - at least one tag)
# #+BIBLIOGRAPHY: citekey1 citekey2 citekey3
#
# Citations in text: [cite:@citekey] or [cite:@key1;@key2]
#
# Quote posts (a passage from elsewhere, with attribution - the format
# simonwillison.net uses for its "quotations"):
# #+KIND: quote
# #+SOURCE: https://example.org/the-article      (REQUIRED for quotes)
# #+AUTHOR: Who said it                          (REQUIRED for quotes)
# #+CONTEXT: their role, or the publication      (optional)
# The body is the quoted passage itself; the layout wraps it in a
# <blockquote cite=...> and appends the attribution line. #+TITLE: may be
# omitted and defaults to "Quoting <author>". #+DESCRIPTION: defaults to the
# opening of the quote.
#
# Environment:
#   ZOTERO_EXPORT  Path to the Zotero BibTeX exporter.
#                  Default: $HOME/.pi/agent/skills/zotero/export-bibtex.sh

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
CSL_FILE="$REPO_DIR/_csl/vancouver.csl"
ZOTERO_EXPORT="${ZOTERO_EXPORT:-$HOME/.pi/agent/skills/zotero/export-bibtex.sh}"

# Colors for output (suppressed when stdout is not a terminal)
if [ -t 1 ]; then
    RED=$'\033[0;31m'
    GREEN=$'\033[0;32m'
    YELLOW=$'\033[1;33m'
    NC=$'\033[0m'
else
    RED=''
    GREEN=''
    YELLOW=''
    NC=''
fi

die() {
    printf '%sError: %s%s\n' "$RED" "$1" "$NC" >&2
    exit 1
}

usage() {
    cat <<'EOF'
Usage: org-to-post.sh <org-file> [--draft] [--force]

  org-file  Path to a .org file (e.g., blog/_org/my-post.org)
  --draft   Write to blog/_drafts instead of blog/_posts
  --force   Overwrite an existing post/draft with the same slug
EOF
}

# ---------------------------------------------------------------- arguments

ORG_FILE=""
IS_DRAFT=false
FORCE=false

while [ $# -gt 0 ]; do
    case "$1" in
        --draft) IS_DRAFT=true ;;
        --force) FORCE=true ;;
        -h|--help) usage; exit 0 ;;
        --*)
            usage >&2
            die "unknown option: $1"
            ;;
        *)
            if [ -n "$ORG_FILE" ]; then
                usage >&2
                die "more than one org file given ($ORG_FILE, $1)"
            fi
            ORG_FILE="$1"
            ;;
    esac
    shift
done

if [ -z "$ORG_FILE" ]; then
    usage >&2
    exit 1
fi

if [ ! -f "$ORG_FILE" ]; then
    die "file not found: $ORG_FILE"
fi

ORG_BASE=$(basename "$ORG_FILE")

printf '%sConverting: %s%s\n' "$GREEN" "$ORG_FILE" "$NC"

# ------------------------------------------------------------------ helpers

# Emit a value as a YAML single-quoted scalar: the only quoting style that
# needs no escaping beyond doubling an internal apostrophe. Survives double
# quotes, colons, hashes, leading dashes - everything a title may contain.
yaml_squote() {
    local escaped
    escaped=$(printf '%s' "$1" | sed "s/'/''/g")
    printf "'%s'" "$escaped"
}

# Lowercase slug, matching Jekyll's `slugify` filter closely enough that a
# tag's own text and its /blog/tags/#anchor are the same string.
slugify() {
    printf '%s' "$1" \
        | tr '[:upper:]' '[:lower:]' \
        | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-*//; s/-*$//'
}

# Value of a `#+KEY:` line, whitespace-trimmed, empty when the key is absent.
# Only the `#+KEY:` prefix is removed, so a value containing colons survives.
org_keyword() {
    local key="$1" line
    line=$(grep -i -m1 "^#+$key:" "$ORG_FILE" || true)
    if [ -z "$line" ]; then
        return 0
    fi
    printf '%s' "${line:$(( ${#key} + 3 ))}" \
        | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

# Normalise an org timestamp to a bare YYYY-MM-DD.
#   2026-03-01
#   <2026-03-01 Sun>          [2026-03-01 Sun]
#   <2026-03-01 Sun 14:30>    <2026-03-01 Sun 14:30-15:30>
normalize_date() {
    local raw="$1" stripped
    stripped=$(printf '%s' "$raw" \
        | sed 's/^[[:space:]]*[<[]//; s/[]>][[:space:]]*$//; s/^[[:space:]]*//; s/[[:space:]]*$//')
    if ! printf '%s' "$stripped" \
        | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}([[:space:]]+[A-Za-z.]+)?([[:space:]]+[0-9]{1,2}:[0-9]{2}(-[0-9]{1,2}:[0-9]{2})?)?$'; then
        return 1
    fi
    printf '%s' "${stripped:0:10}"
}

# Is this a real calendar date? (2026-02-31 is not.)
valid_date() {
    local d="$1" out
    if out=$(date -j -f "%Y-%m-%d" "$d" "+%Y-%m-%d" 2>/dev/null); then
        [ "$out" = "$d" ]
        return $?
    fi
    if out=$(date -d "$d" "+%Y-%m-%d" 2>/dev/null); then
        [ "$out" = "$d" ]
        return $?
    fi
    # No usable `date`; the regex already proved the shape.
    return 0
}

# ----------------------------------------------------------------- metadata

TITLE=$(org_keyword TITLE)
DATE_RAW=$(org_keyword DATE)
UPDATED_RAW=$(org_keyword UPDATED)
DESCRIPTION=$(org_keyword DESCRIPTION)
TAGS_RAW=$(org_keyword TAGS)
CITEKEYS_RAW=$(org_keyword BIBLIOGRAPHY)
KIND=$(org_keyword KIND | tr '[:upper:]' '[:lower:]')
SOURCE_URL=$(org_keyword SOURCE)
SOURCE_AUTHOR=$(org_keyword AUTHOR)
SOURCE_CONTEXT=$(org_keyword CONTEXT)

# --- kind: an ordinary post, or a quote collected from elsewhere ---
case "$KIND" in
    ''|post)
        KIND=post
        ;;
    quote)
        if [ -z "$SOURCE_URL" ]; then
            die "#+KIND: quote in $ORG_BASE needs a #+SOURCE: URL - the attribution links to it."
        fi
        if ! printf '%s' "$SOURCE_URL" | grep -qE '^https?://[^[:space:]"<>]+$'; then
            die "#+SOURCE: '$SOURCE_URL' in $ORG_BASE is not an http(s) URL."
        fi
        if [ -z "$SOURCE_AUTHOR" ]; then
            die "#+KIND: quote in $ORG_BASE needs an #+AUTHOR: - who is being quoted."
        fi
        ;;
    *)
        die "unrecognised #+KIND: '$KIND' in $ORG_BASE. Use 'quote', or leave it out for a normal post."
        ;;
esac

if [ -z "$TITLE" ]; then
    if [ "$KIND" = quote ]; then
        TITLE="Quoting $SOURCE_AUTHOR"
    else
        die "no #+TITLE: found in $ORG_BASE - every post needs a title."
    fi
fi

# --- date ---
if [ -z "$DATE_RAW" ]; then
    DATE=$(date +%Y-%m-%d)
else
    if ! DATE=$(normalize_date "$DATE_RAW"); then
        die "unrecognised #+DATE: '$DATE_RAW' in $ORG_BASE.
  Accepted: YYYY-MM-DD, <YYYY-MM-DD Day>, [YYYY-MM-DD Day], with an optional time."
    fi
    if ! valid_date "$DATE"; then
        die "#+DATE: '$DATE_RAW' in $ORG_BASE is not a real calendar date."
    fi
fi

# --- updated (optional): the date of the last substantive revision ---
UPDATED=""
if [ -n "$UPDATED_RAW" ]; then
    if ! UPDATED=$(normalize_date "$UPDATED_RAW"); then
        die "unrecognised #+UPDATED: '$UPDATED_RAW' in $ORG_BASE.
  Accepted: YYYY-MM-DD, <YYYY-MM-DD Day>, [YYYY-MM-DD Day], with an optional time."
    fi
    if ! valid_date "$UPDATED"; then
        die "#+UPDATED: '$UPDATED_RAW' in $ORG_BASE is not a real calendar date."
    fi
    # ISO dates compare correctly as strings.
    if [[ "$UPDATED" < "$DATE" ]]; then
        die "#+UPDATED: $UPDATED in $ORG_BASE is before #+DATE: $DATE."
    fi
    # Updated on the day it was published is not an update.
    if [ "$UPDATED" = "$DATE" ]; then
        UPDATED=""
    fi
fi

# --- tags (mandatory) ---
if [ -z "$TAGS_RAW" ]; then
    die "no #+TAGS: found in $ORG_BASE - every post needs at least one tag."
fi

# Commas let a tag contain spaces ('Gene Editing'); org's :a:b: filetag
# syntax is accepted too; otherwise split on whitespace.
TAGS_LIST=()
if printf '%s' "$TAGS_RAW" | grep -q ','; then
    TAG_SEP=','
elif printf '%s' "$TAGS_RAW" | grep -qE '^:.*:$'; then
    TAG_SEP=':'
else
    TAG_SEP=' '
fi
OLD_IFS="$IFS"
IFS="$TAG_SEP"
for raw_tag in $TAGS_RAW; do
    slug_tag=$(slugify "$raw_tag")
    if [ -z "$slug_tag" ]; then
        continue
    fi
    dup=false
    for existing in ${TAGS_LIST[@]+"${TAGS_LIST[@]}"}; do
        if [ "$existing" = "$slug_tag" ]; then
            dup=true
        fi
    done
    if [ "$dup" = false ]; then
        TAGS_LIST+=("$slug_tag")
    fi
done
IFS="$OLD_IFS"

if [ ${#TAGS_LIST[@]} -eq 0 ]; then
    die "no usable #+TAGS: in $ORG_BASE - every post needs at least one tag."
fi

# --- citekeys: the #+BIBLIOGRAPHY: line, plus anything cited in the body ---
CITEKEYS=()
add_citekey() {
    local k="${1#@}" existing
    if [ -z "$k" ]; then
        return 0
    fi
    for existing in ${CITEKEYS[@]+"${CITEKEYS[@]}"}; do
        if [ "$existing" = "$k" ]; then
            return 0
        fi
    done
    CITEKEYS+=("$k")
}
for k in $CITEKEYS_RAW; do
    add_citekey "$k"
done
while IFS= read -r k; do
    add_citekey "$k"
done < <(grep -oE '\[cite[^]]*\]' "$ORG_FILE" 2>/dev/null \
    | grep -oE '@[A-Za-z0-9_][A-Za-z0-9_:.+/-]*' || true)

SLUG=$(slugify "$TITLE")
if [ -z "$SLUG" ]; then
    die "could not derive a slug from #+TITLE: '$TITLE'."
fi

echo "  Title: $TITLE"
echo "  Date: $DATE"
echo "  Slug: $SLUG"
echo "  Tags: ${TAGS_LIST[*]}"
if [ "$KIND" = quote ]; then
    echo "  Kind: quote"
    echo "  Quoting: $SOURCE_AUTHOR${SOURCE_CONTEXT:+, $SOURCE_CONTEXT}"
    echo "  Source: $SOURCE_URL"
fi
if [ ${#CITEKEYS[@]} -gt 0 ]; then
    echo "  Citations: ${CITEKEYS[*]}"
fi

# -------------------------------------------------------------- output path

if [ "$IS_DRAFT" = true ]; then
    OUTPUT_DIR="$REPO_DIR/blog/_drafts"
else
    OUTPUT_DIR="$REPO_DIR/blog/_posts"
fi
OUTPUT_FILE="$OUTPUT_DIR/$DATE-$SLUG.md"

# Refuse to clobber. Any date prefix counts: two files sharing a slug are the
# same post, and Jekyll would serve them at the same /blog/<slug>/ permalink.
if [ "$FORCE" != true ]; then
    for existing in "$OUTPUT_DIR"/*-"$SLUG".md; do
        if [ -e "$existing" ]; then
            die "$existing already exists.
  Pass --force to overwrite it."
        fi
    done
fi

# ----------------------------------------------------------------- temp dir

TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_BIB="$TMP_DIR/references.bib"
TMP_ERR="$TMP_DIR/zotero.err"
TMP_MD="$TMP_DIR/content.md"

# ---------------------------------------------------------------- citations

if [ ${#CITEKEYS[@]} -gt 0 ]; then
    printf '%sFetching citations from Zotero...%s\n' "$YELLOW" "$NC"

    if [ ! -x "$ZOTERO_EXPORT" ]; then
        die "Zotero BibTeX exporter not found or not executable:
    $ZOTERO_EXPORT
  $ORG_BASE cites ${#CITEKEYS[@]} key(s), so it cannot be converted without it.
  Set ZOTERO_EXPORT=/path/to/export-bibtex.sh to point at yours."
    fi

    : > "$TMP_BIB"
    FAILED=()

    for citekey in "${CITEKEYS[@]}"; do
        echo "  Fetching: $citekey"
        entry=""
        if ! entry=$("$ZOTERO_EXPORT" "$citekey" 2>"$TMP_ERR"); then
            printf '%s  %s: exporter failed%s\n' "$RED" "$citekey" "$NC" >&2
            if [ -s "$TMP_ERR" ]; then
                sed 's/^/    /' "$TMP_ERR" >&2
            fi
            if [ -n "$entry" ]; then
                printf '%s\n' "$entry" | sed 's/^/    /' >&2
            fi
            FAILED+=("$citekey")
            continue
        fi
        # The exporter prints its own failure text on stdout, so a zero exit
        # is not proof of success: require real BibTeX whose entry key is the
        # key we asked for, or citeproc silently renders `**citekey?**`.
        key_re=$(printf '%s' "$citekey" | sed 's/[][\.*^$+?(){}|\\\/]/\\&/g')
        if ! printf '%s\n' "$entry" \
            | grep -qE "^[[:space:]]*@[A-Za-z]+[[:space:]]*\{[[:space:]]*$key_re[[:space:]]*,"; then
            printf '%s  %s: no BibTeX entry with that key came back%s\n' "$RED" "$citekey" "$NC" >&2
            if [ -n "$entry" ]; then
                printf '%s\n' "$entry" | head -5 | sed 's/^/    /' >&2
            fi
            FAILED+=("$citekey")
            continue
        fi
        printf '%s\n\n' "$entry" >> "$TMP_BIB"
    done

    if [ ${#FAILED[@]} -gt 0 ]; then
        die "${#FAILED[@]} citekey(s) did not resolve: ${FAILED[*]}
  No post was written. Check that Zotero is running with Better BibTeX, and
  that each key exists:  $ZOTERO_EXPORT <citekey>"
    fi

    BIB_ENTRIES=$(grep -c '^[[:space:]]*@' "$TMP_BIB" || true)
    printf '%s  Fetched %s citation(s)%s\n' "$GREEN" "$BIB_ENTRIES" "$NC"

    if [ ! -f "$CSL_FILE" ]; then
        die "citation style not found: $CSL_FILE"
    fi
fi

# ------------------------------------------------------------------- pandoc

printf '%sConverting org to markdown...%s\n' "$YELLOW" "$NC"

PANDOC_ARGS=(
    "$ORG_FILE"
    -f org
    -t gfm
    --wrap=none
    # The layout already renders the title as the page's <h1>. Push org's
    # top-level `*` headings down to <h2> so each post has exactly one <h1>.
    --shift-heading-level-by=1
)

if [ -s "$TMP_BIB" ]; then
    PANDOC_ARGS+=(
        --citeproc
        --bibliography="$TMP_BIB"
        --csl="$CSL_FILE"
        -M link-citations=true
    )
fi

pandoc "${PANDOC_ARGS[@]}" -o "$TMP_MD"

# Belt and braces: citeproc renders an unresolved key as `[**key?**](#ref-key)`
# rather than failing. Never let that reach a post.
if grep -qE '\?\*\*\]\(#ref-' "$TMP_MD"; then
    die "pandoc could not resolve one or more citations in $ORG_BASE:
$(grep -oE '\*\*[^*]+\?\*\*' "$TMP_MD" | sort -u | sed 's/^/    /')
  No post was written."
fi

# Pandoc marks an org link it cannot classify as a "spurious link", which
# renders as literal text. The usual cause is a relative image written without
# the file: prefix - [[figures/a.png]] instead of [[file:figures/a.png]].
if grep -q 'class="spurious-link"' "$TMP_MD"; then
    die "pandoc could not make sense of these links in $ORG_BASE:
$(grep -oE 'class="spurious-link" target="[^"]*"' "$TMP_MD" | sed -E 's/.*target="([^"]*)"/    [[\1]]/' | sort -u)
  A relative image needs the file: prefix: [[file:figures/a.png]].
  No post was written."
fi

# ------------------------------------------------------- relative images
#
# A post that lives in its own folder (blog/_org/<name>/<name>.org) may point
# at figures relative to itself - [[file:figures/fig1.png]] - so Emacs can
# preview them inline and the analysis that made them sits next to the prose.
# The site cannot serve anything under _org, so each referenced file is copied
# to assets/images/blog/<slug>/ and the target rewritten to that URL. Only the
# files the post actually references are copied; supplementary figures in the
# folder stay out of the build. Nothing is copied until every target resolves.

ORG_DIR="$(cd "$(dirname "$ORG_FILE")" && pwd)"
IMG_DIR_REL="assets/images/blog/$SLUG"
IMG_DIR="$REPO_DIR/$IMG_DIR_REL"

REL_IMAGES=()
while IFS= read -r target; do
    [ -n "$target" ] && REL_IMAGES+=("$target")
done < <( { grep -oE '\]\([^)"[:space:]]+\)' "$TMP_MD" | sed -E 's/^\]\(//; s/\)$//'
            grep -oiE '(src|poster)="[^"]+"' "$TMP_MD" | sed -E 's/^[^=]*="//; s/"$//'
            grep -oiE "(src|poster)='[^']+'" "$TMP_MD" | sed -E "s/^[^=]*='//; s/'$//"
          } | grep -iE '\.(png|jpe?g|gif|svg|webp)$' \
            | grep -vE '^(/|#|[A-Za-z][A-Za-z0-9+.-]*:)' \
            | sort -u )

# Escape a literal for use inside a sed regex delimited by #.
sed_escape() {
    printf '%s' "$1" | sed 's/[][\.*^$+?(){}|\\\/#]/\\&/g'
}

IMG_REWRITE=()
IMG_SOURCES=()
IMG_BASENAMES=()
if [ ${#REL_IMAGES[@]} -gt 0 ]; then
    for target in "${REL_IMAGES[@]}"; do
        src="$ORG_DIR/$target"
        if [ ! -f "$src" ]; then
            die "$ORG_BASE references '$target', but there is no such file at
    $src
  Relative image paths are resolved against the org file's own folder.
  No post was written."
        fi
        base=$(basename "$target")
        i=0
        for existing in ${IMG_BASENAMES[@]+"${IMG_BASENAMES[@]}"}; do
            if [ "$existing" = "$base" ]; then
                die "two images in $ORG_BASE share the file name '$base':
    ${IMG_SOURCES[$i]#"$ORG_DIR/"}
    $target
  They would collide in $IMG_DIR_REL/. Rename one.
  No post was written."
            fi
            i=$((i + 1))
        done
        IMG_SOURCES+=("$src")
        IMG_BASENAMES+=("$base")
        IMG_REWRITE+=(-e "s#\]\($(sed_escape "$target")\)#](/$IMG_DIR_REL/$(sed_escape "$base"))#g")
        IMG_REWRITE+=(-e "s#(src|poster)=\"$(sed_escape "$target")\"#\1=\"/$IMG_DIR_REL/$(sed_escape "$base")\"#gI")
        IMG_REWRITE+=(-e "s#(src|poster)='$(sed_escape "$target")'#\1='/$IMG_DIR_REL/$(sed_escape "$base")'#gI")
    done
    sed -E "${IMG_REWRITE[@]}" "$TMP_MD" > "$TMP_MD.rewritten"
    mv "$TMP_MD.rewritten" "$TMP_MD"
fi

# A quote post's description doubles as its og:description and its index
# blurb. Default it to the opening of the quote, the way a feed reader would.
if [ "$KIND" = quote ] && [ -z "$DESCRIPTION" ]; then
    DESCRIPTION=$(pandoc "$ORG_FILE" -f org -t plain --wrap=none \
        | grep -v '^[[:space:]]*$' | grep -v '^#+' | head -1 \
        | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
    if [ ${#DESCRIPTION} -gt 200 ]; then
        DESCRIPTION="${DESCRIPTION:0:200}"
        DESCRIPTION="${DESCRIPTION% *}…"
    fi
fi

# -------------------------------------------------------------------- write

mkdir -p "$OUTPUT_DIR"

if [ ${#IMG_SOURCES[@]} -gt 0 ]; then
    mkdir -p "$IMG_DIR"
    i=0
    for src in "${IMG_SOURCES[@]}"; do
        cp -f "$src" "$IMG_DIR/${IMG_BASENAMES[$i]}"
        echo "  Image: ${src#"$REPO_DIR/"} -> $IMG_DIR_REL/${IMG_BASENAMES[$i]}"
        i=$((i + 1))
    done
fi

{
    echo "---"
    echo "title: $(yaml_squote "$TITLE")"
    echo "date: $DATE"
    if [ -n "$UPDATED" ]; then
        echo "updated: $UPDATED"
    fi
    if [ -n "$DESCRIPTION" ]; then
        echo "description: $(yaml_squote "$DESCRIPTION")"
    fi
    if [ "$KIND" = quote ]; then
        # Read by _includes/blog/quote.html. `kind` rather than `type`:
        # Jekyll reserves `type` on documents for the collection name.
        echo "kind: quote"
        echo "source_url: $(yaml_squote "$SOURCE_URL")"
        echo "source_author: $(yaml_squote "$SOURCE_AUTHOR")"
        if [ -n "$SOURCE_CONTEXT" ]; then
            echo "source_context: $(yaml_squote "$SOURCE_CONTEXT")"
        fi
    fi
    echo "tags:"
    for t in "${TAGS_LIST[@]}"; do
        echo "  - $(yaml_squote "$t")"
    done
    echo "---"
    echo ""
    # The pipeline below does four things to pandoc's markdown:
    #
    # 1. Strips leftover org metadata lines and pandoc's raw-org artifacts.
    # 2. Un-file://s image and link targets. Pandoc's org reader treats a
    #    site-absolute target as a local file, so [[/assets/images/blog/fig.jpg]]
    #    comes out as file:///assets/... and 404s on the site. Only the
    #    triple-slash form in a link target or an HTML src/href/poster is
    #    touched, so an external URL that merely contains "file://" - or a
    #    genuine file://host/share URL - is left alone.
    # 3. Repairs the bibliography. kramdown does not parse markdown inside a
    #    block-level <div>, so inside the refs block pandoc's GFM escapes
    #    (\[Internet\]) and autolinks (<https://...>) would reach the browser
    #    verbatim.
    # 4. Collapses runs of blank lines.
    sed -e '/^#+[A-Za-z_]*:/d' \
        -e '/^```{=org}$/,/^```$/d' \
        -e 's/^:::.*//' "$TMP_MD" \
        | sed -E -e 's#\]\(file:///#](/#g' \
                 -e 's#(src|href|poster)="file:///#\1="/#g' \
                 -e "s#(src|href|poster)='file:///#\1='/#g" \
        | sed -e '/^<div id="refs"/,$ {
                    s/\\\[/[/g
                    s/\\\]/]/g
                    s|<\(https\{0,1\}://[^ <>]*\)>|<a href="\1">\1</a>|g
                  }' \
        | sed '/^$/N;/^\n$/d'
} > "$OUTPUT_FILE"

printf '%s%s Created: %s%s\n' "$GREEN" "✓" "$OUTPUT_FILE" "$NC"
if [ ${#IMG_SOURCES[@]} -gt 0 ]; then
    echo "  Remember to git add $IMG_DIR_REL/ along with the post."
fi
echo ""
echo "Preview URL: http://localhost:4000/blog/$SLUG/"
