#!/usr/bin/env bash
#
# fetch-link-preview.sh - draft a _data/link_previews.yml entry for a URL
#
# Usage: ./scripts/fetch-link-preview.sh URL [--image IMAGE_URL]
#
# Reads the page's <title>, og:title, og:description / description and
# og:image, downloads the image into assets/images/blog/previews/ (resized
# to 480px wide), and prints a YAML block to paste into
# _data/link_previews.yml. It never writes the data file itself: check the
# text, since og: tags are often marketing copy or missing entirely, and
# hand-write the description when they are.
#
# For a Wikipedia article, the REST summary endpoint gives a better
# extract than og:description; this script uses it automatically.

set -euo pipefail

URL=""
IMAGE_URL=""
while [ $# -gt 0 ]; do
    case "$1" in
        --image) IMAGE_URL="$2"; shift 2 ;;
        -h|--help) sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) URL="$1"; shift ;;
    esac
done
[ -n "$URL" ] || { echo "usage: $0 URL [--image IMAGE_URL]" >&2; exit 1; }

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT/assets/images/blog/previews"
mkdir -p "$OUT_DIR"

UA="Mozilla/5.0 (finkelsteinlab.org link-preview fetch)"

meta() {  # meta NAME HTMLFILE -> content of <meta property|name=NAME>
    python3 - "$1" "$2" <<'PY'
import html, re, sys
name, path = sys.argv[1], sys.argv[2]
s = open(path, encoding="utf-8", errors="replace").read()
for m in re.finditer(r"<meta\s+[^>]*>", s, re.I):
    tag = m.group(0)
    if re.search(r'(property|name)\s*=\s*["\']%s["\']' % re.escape(name), tag, re.I):
        c = re.search(r'content\s*=\s*["\']([^"\']*)["\']', tag, re.I)
        if c:
            print(html.unescape(c.group(1)).strip()); break
PY
}

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

TITLE=""; DESC=""; SITE=""
case "$URL" in
    *wikipedia.org/wiki/*)
        ARTICLE="${URL##*/wiki/}"
        curl -sL -A "$UA" "https://en.wikipedia.org/api/rest_v1/page/summary/$ARTICLE" > "$TMP"
        TITLE=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["title"])' "$TMP")
        DESC=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("extract",""))' "$TMP")
        [ -n "$IMAGE_URL" ] || IMAGE_URL=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("thumbnail",{}).get("source",""))' "$TMP")
        SITE="Wikipedia"
        ;;
    *)
        curl -sL -A "$UA" "$URL" > "$TMP"
        TITLE=$(meta og:title "$TMP")
        [ -n "$TITLE" ] || TITLE=$(python3 -c 'import html,re,sys;s=open(sys.argv[1],encoding="utf-8",errors="replace").read();m=re.search(r"<title[^>]*>(.*?)</title>",s,re.I|re.S);print(html.unescape(m.group(1)).strip() if m else "")' "$TMP")
        DESC=$(meta og:description "$TMP")
        [ -n "$DESC" ] || DESC=$(meta description "$TMP")
        SITE=$(meta og:site_name "$TMP")
        [ -n "$IMAGE_URL" ] || IMAGE_URL=$(meta og:image "$TMP")
        ;;
esac
[ -n "$SITE" ] || SITE=$(printf '%s' "$URL" | sed -E 's#^https?://(www\.)?([^/]+).*#\2#')

IMAGE_PATH=""
if [ -n "$IMAGE_URL" ]; then
    SLUG=$(printf '%s' "$URL" | sed -E 's#^https?://(www\.)?##; s#[^A-Za-z0-9]+#-#g; s#-+$##' | tr 'A-Z' 'a-z' | cut -c1-60)
    IMG_TMP=$(mktemp)
    if curl -sL -A "$UA" -o "$IMG_TMP" "$IMAGE_URL" && [ -s "$IMG_TMP" ]; then
        if magick "$IMG_TMP" -background white -flatten -resize '480x>' -quality 85 "$OUT_DIR/$SLUG.jpg" 2>/dev/null; then
            IMAGE_PATH="/assets/images/blog/previews/$SLUG.jpg"
        else
            echo "warning: could not convert image $IMAGE_URL" >&2
        fi
    else
        echo "warning: could not download image $IMAGE_URL" >&2
    fi
    rm -f "$IMG_TMP"
fi

yq() { python3 -c 'import json,sys;print(json.dumps(sys.argv[1]))' "$1"; }

echo "# Paste into _data/link_previews.yml (check the text first):"
echo "- url: $(yq "$URL")"
echo "  title: $(yq "$TITLE")"
echo "  description: $(yq "$DESC")"
echo "  site: $(yq "$SITE")"
[ -n "$IMAGE_PATH" ] && echo "  image: $IMAGE_PATH"
exit 0
