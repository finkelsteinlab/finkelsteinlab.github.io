#!/usr/bin/env bash
#
# Convert all paper PDFs to LLM-friendly markdown using marker-pdf.
#
# Output structure:
#   assets/md/<nickname>/          — one folder per paper
#   assets/md/<nickname>/paper.md  — the markdown
#   assets/md/<nickname>/images/   — extracted figures
#
# Run from the repo root:
#   bash scripts/convert-pdfs-to-md.sh
#
# Prerequisites:
#   uv tool install marker-pdf --with psutil
#
# Options:
#   --force    Re-convert even if paper.md already exists
#   --dry-run  Just list what would be converted

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
POSTS_DIR="${REPO_ROOT}/papers/_posts"
PDF_DIR="${REPO_ROOT}/assets/pdfs"
MD_DIR="${REPO_ROOT}/assets/md"
TMPDIR_BASE="${TMPDIR:-/tmp}/marker-convert"

FORCE=false
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --force)   FORCE=true ;;
    --dry-run) DRY_RUN=true ;;
  esac
done

mkdir -p "$MD_DIR" "$TMPDIR_BASE"

# Counters
total=0
skipped=0
converted=0
failed=0

echo "=== PDF → Markdown conversion ==="
echo "Posts:  $POSTS_DIR"
echo "PDFs:   $PDF_DIR"
echo "Output: $MD_DIR"
echo ""

for post in "$POSTS_DIR"/*.md "$POSTS_DIR"/*.MD; do
  [[ "$(basename "$post")" == "template.md" ]] && continue
  [[ ! -f "$post" ]] && continue

  # Extract nickname and pdf filename from front matter
  nickname=$(grep '^nickname:' "$post" | head -1 | sed 's/nickname: *"*//;s/"*$//' | xargs)
  pdf_file=$(grep '^pdf:' "$post" | head -1 | sed 's/pdf: *"*//;s/"*$//' | xargs)

  # Skip if no pdf
  if [[ -z "$pdf_file" ]]; then
    echo "SKIP (no pdf): $(basename "$post")"
    ((skipped++)) || true
    continue
  fi

  # Skip if no nickname
  if [[ -z "$nickname" ]]; then
    echo "SKIP (no nickname): $(basename "$post")"
    ((skipped++)) || true
    continue
  fi

  pdf_path="${PDF_DIR}/${pdf_file}"
  out_dir="${MD_DIR}/${nickname}"
  out_md="${out_dir}/paper.md"

  ((total++)) || true

  # Skip if already converted (unless --force)
  if [[ -f "$out_md" && "$FORCE" != "true" ]]; then
    echo "EXISTS: ${nickname}"
    ((skipped++)) || true
    continue
  fi

  # Check PDF exists
  if [[ ! -f "$pdf_path" ]]; then
    echo "MISSING PDF: ${pdf_file} (${nickname})"
    ((failed++)) || true
    continue
  fi

  if [[ "$DRY_RUN" == "true" ]]; then
    echo "WOULD CONVERT: ${pdf_file} → ${nickname}/"
    continue
  fi

  echo -n "CONVERTING: ${nickname} ... "

  # Create output dir
  mkdir -p "$out_dir"

  # Run marker_single to a temp directory, then move files
  tmp_out="${TMPDIR_BASE}/${nickname}"
  rm -rf "$tmp_out"

  if marker_single "$pdf_path" \
      --output_dir "$tmp_out" \
      --output_format markdown \
      --disable_multiprocessing \
      2>/dev/null; then

    # marker creates a subfolder named after the PDF (without extension)
    # Find the .md file it produced
    md_result=$(find "$tmp_out" -name "*.md" -type f | head -1)

    if [[ -n "$md_result" ]]; then
      # Move markdown
      cp "$md_result" "$out_md"

      # Move images if any
      img_src=$(dirname "$md_result")/images
      if [[ -d "$img_src" ]] && [[ "$(ls -A "$img_src" 2>/dev/null)" ]]; then
        mkdir -p "${out_dir}/images"
        cp -r "$img_src"/* "${out_dir}/images/"
        img_count=$(ls "${out_dir}/images/" | wc -l | xargs)

        # Rewrite image paths in MD to be relative
        # marker uses paths like images/filename.png — keep as-is since
        # we preserve the same relative structure
        echo "OK (${img_count} images)"
      else
        echo "OK (no images)"
      fi

      ((converted++)) || true
    else
      echo "FAIL (no md output)"
      ((failed++)) || true
    fi

    rm -rf "$tmp_out"
  else
    echo "FAIL (marker error)"
    ((failed++)) || true
    rm -rf "$tmp_out"
  fi
done

echo ""
echo "=== Done ==="
echo "Total:     $total"
echo "Converted: $converted"
echo "Skipped:   $skipped"
echo "Failed:    $failed"
