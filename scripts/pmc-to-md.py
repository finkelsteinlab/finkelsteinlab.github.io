#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "beautifulsoup4>=4.12",
#   "lxml>=5.1",
#   "requests>=2.32",
#   "PyYAML>=6.0",
# ]
# ///
"""
pmc-to-md.py — scrape a PubMed Central article into the site's archived
full-text markdown format.

Usage
-----
    uv run scripts/pmc-to-md.py papers/_posts/2026-05-18-Hna-antiphage-defense.MD

Reads the paper post's YAML front matter (`pmcid`, `title`, `doi`, `nickname`,
`authors`, `journal`, `volume`, `issue`, `pages`, `year`), fetches the PMC
article HTML, and writes:

    assets/md/<slug>/index.md      -- the archived full text
    assets/md/<slug>/figN.jpg      -- one JPEG per main figure

The slug defaults to the post's filename stem; override with --slug.

Figures are downsampled to a 1600 px long edge and re-encoded as JPEG q82 via
`sips` (macOS). If the re-encode ends up larger than the original *and* the
original is already a JPEG at or below 1600 px, the original is kept.

The output is meant to be ~95% of the way to the house style documented in
`assets/md/FORMATTING-RULES.md`; always read the result and fix the residue by
hand (units, kinetic parameters, italics for species/Latin terms, etc.).

Options
-------
    --slug SLUG        output directory name under assets/md/ (default: post stem)
    --outdir DIR       repo root (default: parent of this script's directory)
    --no-figures       skip figure download
    --no-toc           omit the Table of Contents block
    --footer           append the "Archived from PubMed Central" footer
    --force            overwrite an existing index.md
    --cache DIR        HTML cache directory (default: <tmp>/pmc-cache)
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 "
    "(finkelsteinlab.org site archiver; ilya@finkelsteinlab.org)"
)
REQUEST_DELAY = 2.0  # seconds between requests to NCBI

SUP_MAP = str.maketrans("0123456789+-−=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿ")
SUB_MAP = str.maketrans("0123456789+-−=()", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎")

CIT_OPEN = "\x01"
CIT_CLOSE = "\x02"

# words that stay lowercase when down-casing a SHOUTED journal heading
SMALL_WORDS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "of",
    "on", "or", "the", "to", "via", "with",
}


def normalize_heading(title: str) -> str:
    """Trim trailing punctuation and title-case ALL-CAPS journal headings."""
    title = title.strip().rstrip(":").strip()
    title = re.sub(r"\.\s*$", "", title)
    letters = [c for c in title if c.isalpha()]
    if letters and all(c.isupper() for c in letters) and len(letters) > 3:
        words = title.split()
        out = []
        for i, w in enumerate(words):
            lower = w.lower()
            if i and lower in SMALL_WORDS:
                out.append(lower)
            else:
                out.append(lower[:1].upper() + lower[1:])
        title = " ".join(out)
    return title


# --------------------------------------------------------------------------
# front matter
# --------------------------------------------------------------------------


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        sys.exit(f"no YAML front matter in {path}")
    return yaml.safe_load(m.group(1)) or {}


def unescape_entities(s: str) -> str:
    import html as _html

    return _html.unescape(s or "")


# --------------------------------------------------------------------------
# fetching
# --------------------------------------------------------------------------

_last_request = [0.0]


def polite_get(session: requests.Session, url: str, **kw) -> requests.Response:
    wait = REQUEST_DELAY - (time.time() - _last_request[0])
    if wait > 0:
        time.sleep(wait)
    resp = session.get(url, timeout=60, **kw)
    _last_request[0] = time.time()
    if resp.status_code in (403, 429, 503):
        sys.exit(
            f"PMC returned {resp.status_code} for {url}. "
            "Stopping rather than retrying — try again later."
        )
    resp.raise_for_status()
    return resp


def fetch_article(session: requests.Session, pmcid: str, cache: Path) -> str:
    cache.mkdir(parents=True, exist_ok=True)
    cached = cache / f"{pmcid}.html"
    if cached.exists():
        return cached.read_text(encoding="utf-8")
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    resp = polite_get(session, url)
    cached.write_text(resp.text, encoding="utf-8")
    return resp.text


# --------------------------------------------------------------------------
# converter
# --------------------------------------------------------------------------


class Converter:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup
        self.body = soup.find("section", class_="main-article-body")
        if self.body is None:
            sys.exit("could not find <section class='body main-article-body'>")
        self.fig_ids: dict[str, int] = {}      # html anchor id -> figure number
        self.fig_files: dict[int, str] = {}    # figure number -> source image URL
        self.ref_ids: dict[str, int] = {}      # html anchor id -> reference number
        self._scan_figures()
        self._scan_references()

    # -- discovery ---------------------------------------------------------

    def _scan_figures(self) -> None:
        n = 0
        for fig in self.body.find_all("figure"):
            classes = fig.get("class") or []
            if "fig" not in classes:
                continue
            img = fig.find("img")
            if img is None or not img.get("src"):
                continue
            n += 1
            head = fig.find(class_="obj_head")
            label = head.get_text(" ", strip=True) if head else ""
            m = re.match(r"\s*(?:Fig(?:ure)?\.?)\s*(\d+)", label, re.I)
            num = int(m.group(1)) if m else n
            fid = fig.get("id")
            if fid:
                self.fig_ids[fid] = num
            self.fig_files[num] = img["src"]

    def _scan_references(self) -> None:
        for sec in self.soup.find_all("section", class_="ref-list"):
            n = 0
            for li in sec.find_all("li"):
                if not li.get("id"):
                    continue
                n += 1
                label = li.find("span", class_="label")
                num = n
                if label:
                    m = re.search(r"(\d+)", label.get_text())
                    if m:
                        num = int(m.group(1))
                self.ref_ids[li["id"]] = num

    # -- inline ------------------------------------------------------------

    def inline(self, node, html_ctx: bool = False) -> str:
        out: list[str] = []
        for child in getattr(node, "children", []):
            out.append(self._inline_node(child, html_ctx))
        return self._join(out)

    @staticmethod
    def _join(parts: list[str]) -> str:
        buf = ""
        for p in parts:
            if not p:
                continue
            # keep adjacent markdown emphasis runs from fusing ("*Journal***12**")
            if buf.endswith("*") and p.startswith("*"):
                buf += " "
            buf += p
        return buf

    def _inline_node(self, node, html_ctx: bool) -> str:
        if isinstance(node, NavigableString):
            text = re.sub(r"\s+", " ", str(node))
            if html_ctx:
                text = text.replace("*", "&#42;")
            return text
        if not isinstance(node, Tag):
            return ""

        name = node.name.lower()

        if name in ("script", "style"):
            return ""
        if name == "br":
            return " "
        if name in ("em", "i"):
            inner = self.inline(node, html_ctx).strip()
            if not inner:
                return ""
            return f"<em>{inner}</em>" if html_ctx else f"*{inner}*"
        if name in ("strong", "b"):
            inner = self.inline(node, html_ctx).strip()
            if not inner:
                return ""
            return f"<strong>{inner}</strong>" if html_ctx else f"**{inner}**"
        if name == "sup":
            return self._sup(node, html_ctx)
        if name == "sub":
            inner_text = node.get_text("", strip=True)
            if re.fullmatch(r"[0-9+\-−=()]+", inner_text):
                return inner_text.translate(SUB_MAP)
            return f"<sub>{self.inline(node, html_ctx).strip()}</sub>"
        if name == "a":
            return self._anchor(node, html_ctx)
        if name in ("math", "mml:math"):
            return node.get_text("", strip=True)
        if name in ("table", "thead", "tbody", "tr", "td", "th"):
            return self.inline(node, html_ctx)
        return self.inline(node, html_ctx)

    def _sup(self, node: Tag, html_ctx: bool) -> str:
        links = node.find_all("a")
        if links and all(self._is_ref_link(a) for a in links):
            return self._citation_run(node)
        inner_text = node.get_text("", strip=True)
        if re.fullmatch(r"[0-9+\-−=()n]+", inner_text):
            return inner_text.translate(SUP_MAP)
        return f"<sup>{self.inline(node, html_ctx).strip()}</sup>"

    def _is_ref_link(self, a: Tag) -> bool:
        href = a.get("href", "")
        return href.startswith("#") and href[1:] in self.ref_ids

    def _citation_run(self, node: Tag) -> str:
        """Collapse a <sup> full of reference links into one marker group."""
        parts: list[str] = []
        first = None
        for child in node.children:
            if isinstance(child, NavigableString):
                parts.append(re.sub(r"\s+", " ", str(child)))
            elif isinstance(child, Tag) and child.name == "a":
                num = self.ref_ids.get(child.get("href", "")[1:])
                if num is None:
                    parts.append(child.get_text("", strip=True))
                    continue
                if first is None:
                    first = num
                parts.append(child.get_text("", strip=True))
            else:
                parts.append(child.get_text("", strip=True))
        text = "".join(parts).strip()
        if first is None:
            return text
        return f"{CIT_OPEN}{first}|{text}{CIT_CLOSE}"

    def _anchor(self, node: Tag, html_ctx: bool) -> str:
        href = node.get("href", "") or ""
        text = self.inline(node, html_ctx).strip()
        if not text:
            return ""

        if href.startswith("#"):
            target = href[1:]
            if target in self.fig_ids:
                num = self.fig_ids[target]
                if html_ctx:
                    return f'<a href="#fig{num}">{text}</a>'
                return f"[{text}](#fig{num})"
            if target in self.ref_ids:
                num = self.ref_ids[target]
                # reference numbers are often italicised by the journal; the
                # emphasis is decoration, not content
                plain = node.get_text(" ", strip=True)
                if html_ctx:
                    return f'<a href="#ref{num}">{plain}</a>'
                return f"{CIT_OPEN}{num}|{plain}{CIT_CLOSE}"
            # tables, supplementary material, movies, schemes: strip the link
            return text

        if href.startswith("mailto:"):
            return f"[{text}]({href})" if not html_ctx else f'<a href="{href}">{text}</a>'

        if href.startswith("http"):
            if re.search(r"(scholar\.google|pubmed\.ncbi|/articles/PMC)", href):
                return text
            return f"[{text}]({href})" if not html_ctx else f'<a href="{href}">{text}</a>'

        # relative PMC links (figure/F1/, /articles/instance/...): strip
        return text

    # -- blocks ------------------------------------------------------------

    def render_body(self) -> list[str]:
        chunks: list[str] = []
        abstract_seen = False
        for child in self.body.children:
            if not isinstance(child, Tag):
                continue
            classes = child.get("class") or []
            if child.name == "hr":
                continue
            if "abstract" in classes:
                if abstract_seen:
                    continue  # editors' summary / one-sentence blurb
                abstract_seen = True
                chunks.extend(self._abstract(child))
                chunks.append("---")
                continue
            if child.name == "section":
                chunks.extend(self._section(child, level=2))
            else:
                chunks.extend(self._block(child, level=2))
        return chunks

    def _abstract(self, sec: Tag) -> list[str]:
        out = ["## Abstract"]
        for el in sec.children:
            if not isinstance(el, Tag):
                continue
            if el.name in ("h1", "h2", "h3", "h4"):
                continue
            if "kwd-group" in (el.get("class") or []):
                for p in el.find_all("p"):
                    out.append(self.inline(p).strip())
                continue
            out.extend(self._block(el, level=3))
        return out

    def _section(self, sec: Tag, level: int) -> list[str]:
        classes = sec.get("class") or []
        sid = sec.get("id", "") or ""
        if "ref-list" in classes:
            return []  # rendered separately
        if sid.startswith("_ad") or "associated-data" in classes:
            return []
        out: list[str] = []
        head = sec.find(["h2", "h3", "h4", "h5"], recursive=False)
        if head is not None and "obj_head" not in (head.get("class") or []):
            title = normalize_heading(self.inline(head).strip())
            hlevel = min(max(level, 2), 5)
            out.append(f"{'#' * hlevel}{' '}{title}")
        for el in sec.children:
            if not isinstance(el, Tag) or el is head:
                continue
            if el.name in ("h1", "h2", "h3", "h4", "h5"):
                continue
            if el.name == "section":
                out.extend(self._section(el, level + 1))
            else:
                out.extend(self._block(el, level + 1))
        return out

    def _block(self, el: Tag, level: int) -> list[str]:
        classes = el.get("class") or []
        name = el.name.lower()

        if name == "hr":
            return []
        if name == "figure" and "fig" in classes:
            return [self._figure(el)]
        if name == "figure":
            return []
        if name in ("p", "div"):
            if "text-right" in classes:
                return []  # "Open in a new tab"
            if name == "div" and el.find(["p", "section", "figure", "table"]):
                out: list[str] = []
                for sub in el.children:
                    if isinstance(sub, Tag):
                        out.extend(self._block(sub, level))
                return out
            text = self.inline(el).strip()
            return [text] if text else []
        if name in ("ul", "ol"):
            return [self._list(el, ordered=(name == "ol"))]
        if name == "table":
            return [self._table(el)]
        if name == "section":
            return self._section(el, level)
        if name == "blockquote":
            text = self.inline(el).strip()
            return [f"> {text}"] if text else []
        text = self.inline(el).strip()
        return [text] if text else []

    def _list(self, el: Tag, ordered: bool) -> str:
        lines = []
        for i, li in enumerate(el.find_all("li", recursive=False), start=1):
            marker = f"{i}." if ordered else "-"
            lines.append(f"{marker} {self.inline(li).strip()}")
        return "\n".join(lines)

    def _table(self, el: Tag) -> str:
        rows: list[list[str]] = []
        header: list[str] | None = None
        for tr in el.find_all("tr"):
            cells = tr.find_all(["th", "td"])
            vals = [self.inline(c).strip().replace("|", "\\|") for c in cells]
            if header is None and all(c.name == "th" for c in cells) and cells:
                header = vals
            else:
                rows.append(vals)
        if header is None and rows:
            header, rows = rows[0], rows[1:]
        if not header:
            return ""
        width = max([len(header)] + [len(r) for r in rows] or [0])
        header += [""] * (width - len(header))
        lines = ["| " + " | ".join(header) + " |",
                 "|" + "|".join([" --- "] * width) + "|"]
        for r in rows:
            r = r + [""] * (width - len(r))
            lines.append("| " + " | ".join(r) + " |")
        return "\n".join(lines)

    def _figure(self, fig: Tag) -> str:
        img = fig.find("img")
        fid = fig.get("id")
        num = self.fig_ids.get(fid) if fid else None
        if num is None:
            num = 0
        head = fig.find(class_="obj_head")
        label = head.get_text(" ", strip=True) if head else f"Figure {num}."
        label = re.sub(r"^\s*Fig(?:ure)?\.?\s*(\d+)\s*[.:]?\s*",
                       lambda m: f"Figure {m.group(1)}. ", label)
        label = label.strip()
        if not label.endswith((".", "?", "!")):
            label += "."
        cap_el = fig.find("figcaption")
        caption = self.inline(cap_el, html_ctx=True).strip() if cap_el else ""
        caption = re.sub(r"\s+", " ", caption)
        body = f"<strong>{label}</strong>"
        if caption:
            body += f" {caption}"
        return (
            f'<figure class="paper-figure" id="fig{num}">\n'
            f'<img src="fig{num}.jpg" alt="Figure {num}">\n'
            f"<figcaption>{body}</figcaption>\n"
            f"</figure>"
        )

    # -- references --------------------------------------------------------

    def render_references(self) -> list[str]:
        sec = self.soup.find("section", class_="ref-list")
        if sec is None:
            return []
        out = ["## References", ""]
        entries = []
        for li in sec.find_all("li"):
            if not li.get("id"):
                continue
            num = self.ref_ids.get(li["id"])
            if num is None:
                continue
            doi = None
            for a in li.find_all("a"):
                href = a.get("href", "")
                if "doi.org/" in href:
                    doi = href
                    break
            cite = li.find("cite") or li
            for a in cite.find_all("a"):
                a.replace_with(a.get_text("", strip=True))
            # PMC separates author list / title / journal with bare newlines;
            # restore the sentence period that some journal styles rely on
            for s in list(cite.find_all(string=True)):
                txt = str(s)
                if "\n" not in txt:
                    continue
                txt = re.sub(r"(?<=[A-Za-z0-9])\s*\n\s*(?=[A-Z])", ". ", txt)
                txt = re.sub(r"\s*\n\s*", " ", txt)
                s.replace_with(txt)
            text = self.inline(cite).strip()
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"^\(?\d+\)?\.\s*", "", text)
            text = text.strip()
            if doi:
                doi_id = doi.split("doi.org/", 1)[1]
                # some entries already carry a plain "DOI: 10.x" tail
                text = re.sub(r"\s*DOI:\s*" + re.escape(doi_id) + r"\s*$", "", text)
                if not text.endswith("."):
                    text += "."
                text += f" [doi:{doi_id}]({doi})"
            entries.append(f'<span id="ref{num}">{num}.</span> {text}')
        out.append("\n\n".join(entries))
        return out


# --------------------------------------------------------------------------
# post-processing
# --------------------------------------------------------------------------


def postprocess(text: str) -> str:
    # 1. expand citation markers, collapsing adjacent runs
    def cit(m: re.Match) -> str:
        return f"[[{m.group(2)}]](#ref{m.group(1)})"

    pattern = re.compile(
        re.escape(CIT_OPEN) + r"(\d+)\|(.*?)" + re.escape(CIT_CLOSE), re.S
    )

    def collapse(text: str) -> str:
        # merge "⟦a|1⟧, ⟦b|2⟧" style runs into one bracketed group
        run = re.compile(
            "(?:" + re.escape(CIT_OPEN) + r"\d+\|[^\x02]*" + re.escape(CIT_CLOSE)
            + r")(?:\s*(?:,|–|—|-|, and|and)?\s*(?:" + re.escape(CIT_OPEN)
            + r"\d+\|[^\x02]*" + re.escape(CIT_CLOSE) + r"))*"
        )

        def repl(m: re.Match) -> str:
            s = m.group(0)
            nums = re.findall(re.escape(CIT_OPEN) + r"(\d+)\|", s)
            disp = pattern.sub(lambda mm: mm.group(2), s)
            disp = re.sub(r"\s+", " ", disp).strip()
            disp = disp.strip(" ,;")
            return f"[[{disp}](#ref{nums[0]})]"

        return run.sub(repl, text)

    text = collapse(text)
    # any stragglers
    text = pattern.sub(lambda m: f"[[{m.group(2)}](#ref{m.group(1)})]", text)

    # 2. parenthesis-only citation groups: "([[1, 2](#ref1)])" -> "[[1, 2](#ref1)]"
    text = re.sub(r"\(\s*(\[\[[^\]]*\]\(#ref\d+\)\])\s*\)", r"\1", text)

    # 3. a space must precede an opening citation bracket
    text = re.sub(r"(?<=[^\s(\[])(\[\[)", r" \1", text)

    # 4. orphaned "Fig. [1a](#fig1)" -> "[Fig. 1a](#fig1)"
    text = re.sub(
        r"\b(Figs?\.?|Figures?)\s*\[([^\]\n]{1,40})\]\(#fig(\d+)\)",
        r"[\1 \2](#fig\3)",
        text,
    )
    # 5. merge adjacent links to the same figure, keeping the original separator:
    #    "[Fig. 2](#fig2)C and [E](#fig2)" -> "[Fig. 2C and E](#fig2)"
    #    "[Fig. 5A](#fig5)&[B](#fig5)-[i](#fig5)" -> "[Fig. 5A&B-i](#fig5)"
    merge = re.compile(
        r"\[([^\]\n]+)\]\(#fig(\d+)\)([A-Za-z0-9,&\-–—\s]{0,10}?)\[([^\]\n]+)\]\(#fig\2\)"
    )
    for _ in range(12):
        new = merge.sub(r"[\1\3\4](#fig\2)", text)
        if new == text:
            break
        text = new
    # 5b. a lone trailing panel letter belongs inside the link text
    text = re.sub(
        r"\[((?:Figs?\.|Figures?)\s*\d+)\]\(#fig(\d+)\)([A-Za-z](?=[\s,;.)\]]))",
        r"[\1\3](#fig\2)",
        text,
    )
    # 6. supplementary figures must never link to local anchors
    text = re.sub(
        r"(Supplementary|Extended Data|Supporting Information)\s*"
        r"\[((?:Figs?\.?|Figures?)[^\]\n]*)\]\(#fig\d+\)",
        r"\1 \2",
        text,
    )

    # 7. supplementary-file size markers are not superscripts
    text = re.sub(
        r"\s*<sup>\s*\((\d+(?:\.\d+)?\s*[KMG]B),\s*([A-Za-z0-9]+)\)\s*</sup>",
        r" (\1, \2)",
        text,
    )

    # 8. tidy spacing
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def slugify_heading(h: str) -> str:
    s = re.sub(r"[^\w\s-]", "", h.lower())
    return re.sub(r"\s+", "-", s.strip())


def build_toc(chunks: list[str]) -> list[str]:
    heads = [c[3:].strip() for c in chunks if c.startswith("## ")]
    if len(heads) < 3:
        return []
    out = ["## Table of Contents", ""]
    out.append("\n".join(f"- [{h}](#{slugify_heading(h)})" for h in heads))
    return out


# --------------------------------------------------------------------------
# figures
# --------------------------------------------------------------------------


def download_figures(
    session: requests.Session, conv: Converter, outdir: Path
) -> tuple[int, int]:
    outdir.mkdir(parents=True, exist_ok=True)
    total = 0
    count = 0
    tmp = Path(tempfile.mkdtemp(prefix="pmcfig-"))
    try:
        for num in sorted(conv.fig_files):
            url = conv.fig_files[num]
            ext = os.path.splitext(url)[1].lower() or ".jpg"
            raw = tmp / f"fig{num}{ext}"
            resp = polite_get(session, url)
            raw.write_bytes(resp.content)
            dest = outdir / f"fig{num}.jpg"
            small = tmp / f"fig{num}-small.jpg"
            subprocess.run(
                ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                 "-Z", "1600", str(raw), "--out", str(small)],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            use = small
            if ext in (".jpg", ".jpeg") and raw.stat().st_size < small.stat().st_size:
                # original JPEG already smaller (and <=1600px after sips no-op)
                w = subprocess.run(
                    ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(raw)],
                    capture_output=True, text=True,
                ).stdout
                dims = [int(x) for x in re.findall(r":\s*(\d+)", w)]
                if dims and max(dims) <= 1600:
                    use = raw
            shutil.copyfile(use, dest)
            total += dest.stat().st_size
            count += 1
            print(f"  fig{num}.jpg  {dest.stat().st_size:>9,} bytes  <- {url.rsplit('/', 1)[-1]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return count, total


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def build_header(fm: dict) -> list[str]:
    authors = unescape_entities(str(fm.get("authors", ""))).strip()
    journal = unescape_entities(str(fm.get("journal", ""))).strip()
    vol = str(fm.get("volume") or "").strip()
    issue = str(fm.get("issue") or "").strip()
    pages = str(fm.get("pages") or "").strip()
    year = str(fm.get("year") or "").strip()
    doi = str(fm.get("doi") or "").strip()

    cite = f"*{journal}*" if journal else ""
    if vol:
        cite += f", {vol}"
        if issue:
            cite += f"({issue})"
    if pages:
        cite += f": {pages}"
    if year:
        cite += f", {year}"

    out = []
    if authors:
        out.append(f"**{authors}**")
    if cite:
        out.append(cite)
    if doi:
        out.append(f"DOI: [{doi}](https://doi.org/{doi})")
    out.append("---")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post", type=Path, help="path to papers/_posts/<file>.MD")
    ap.add_argument("--slug", help="output directory name under assets/md/")
    ap.add_argument("--root", type=Path, help="repo root (default: script's parent dir)")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--footer", action="store_true",
                    help="append the 'Archived from PubMed Central' footer")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--cache", type=Path,
                    default=Path(tempfile.gettempdir()) / "pmc-cache")
    args = ap.parse_args()

    root = args.root or Path(__file__).resolve().parent.parent
    post = args.post if args.post.is_absolute() else (root / args.post)
    if not post.exists():
        sys.exit(f"no such post: {post}")

    fm = read_front_matter(post)
    pmcid = str(fm.get("pmcid") or "").strip()
    if not pmcid:
        sys.exit(f"{post.name} has no pmcid — PMC full text is unavailable")

    slug = args.slug or post.stem
    outdir = root / "assets" / "md" / slug
    index = outdir / "index.md"
    if index.exists() and not args.force:
        sys.exit(f"{index} already exists (use --force to overwrite)")

    session = requests.Session()
    session.headers["User-Agent"] = UA

    print(f"fetching {pmcid} ...")
    html = fetch_article(session, pmcid, args.cache)
    soup = BeautifulSoup(html, "lxml")
    conv = Converter(soup)
    print(f"  {len(conv.fig_files)} figures, {len(conv.ref_ids)} references")

    chunks = conv.render_body()
    chunks += conv.render_references()

    if not args.no_toc:
        toc = build_toc(chunks)
        if toc:
            chunks = toc + ["---"] + chunks

    source_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    if args.footer:
        chunks += ["---",
                   f"*Archived from [PubMed Central]({source_url}) "
                   f"on {date.today().isoformat()}.*"]

    title = unescape_entities(str(fm.get("title", ""))).replace('"', '\\"')
    front = [
        "---",
        "layout: paper-md",
        f'title: "{title}"',
        f"paper_slug: {slug}",
        f"paper_url: /papers/paper/{fm.get('nickname', '')}",
        f"doi: {fm.get('doi', '')}",
        f"source_url: {source_url}",
        f"pmcid: {pmcid}",
        "---",
    ]

    body = "\n\n".join(build_header(fm) + chunks)
    text = "\n".join(front) + "\n\n" + postprocess(body).strip() + "\n"

    outdir.mkdir(parents=True, exist_ok=True)
    index.write_text(text, encoding="utf-8")
    print(f"wrote {index} ({len(text):,} bytes)")

    if not args.no_figures:
        count, total = download_figures(session, conv, outdir)
        print(f"{count} figures, {total:,} bytes")

    print(f"\nNow add to {post.name} front matter:  markdown: {slug}")


if __name__ == "__main__":
    main()
