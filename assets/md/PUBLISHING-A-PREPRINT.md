# When a preprint becomes a published paper

A preprint on this site is not just a set of metadata fields. It is a post in
`papers/_posts/`, a PDF in `assets/pdfs/`, and — usually — a full-text markdown
conversion in `assets/md/<slug>/` with its own extracted figures.

**Updating the metadata alone produces a page that lies.** The citation header
says *Science Advances*, the body is still the bioRxiv text, and the figures are
still the preprint's figures. Published versions are revised: wording changes,
figures get renumbered or replaced, references are renumbered, and data can be
added in review. This happened once already and is the reason this file exists.

Work through all six steps, in order.

## 1. Get the published PDF and supplement

Download from the publisher, not from a preprint server or an aggregator. Take
the article PDF and any **PDF** supplement. Do not mirror supplementary movies,
spreadsheets, or archives — a single paper's `.avi` set can exceed the whole
image budget of the site. If the only supplement is non-PDF, leave
`supplement:` empty.

Name them to match the library: `NNNN-YYYY-FirstAuthor et al-Journal.pdf`, with
supplements as the same stem plus `-supplement.pdf`. Keep the paper's existing
number and just change the year and journal, since the number tracks the paper,
not the version. Delete the old preprint PDF.

Then recompress, as every other PDF in the library has been:

```sh
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages=true \
   -sOutputFile=out.pdf "in.pdf"
```

Keep the result only if it is **both** smaller and the same page count. Check
the page count with
`gs -q -dNODISPLAY -dNOSAFER -dBATCH -c "(f.pdf) (r) file runpdfbegin pdfpagecount = quit"`.
For image-heavy papers (AFM, cryo-EM, microscopy), render one figure page to PNG
and look at it before accepting the compressed version.

## 2. Update the post front matter

`journal`, `year`, `volume`, `issue`, `pages`, `doi`, `pmid`, `pmcid`,
`shortref`, `pdf`, `supplement`. Replace the abstract in the body with the
published one — it is frequently reworded.

Take the author list from the publisher page, not from Google Scholar, which
truncates to "et al." The head template splits `authors:` on `", "`, `", and "`,
`" and "` and `" & "` to emit one `citation_author` tag per author, so
punctuation matters. Keep the `&#42;` / `&dagger;` convention for co-first and
corresponding authors.

## 3. Rename the post file, and redirect

Two separate things depend on the filename:

- **Sort order** on `/papers/` comes from the `YYYY-MM-DD-` prefix, so a paper
  keeping its preprint date sorts into the wrong year.
- **The Preprints section** of `papers/index.html` is selected by a `10.1101/`
  DOI prefix. Once the DOI is a real journal DOI the paper leaves that section
  automatically.

Renaming changes the URL, so add a `redirect_from:` entry with the **old URL**
or you break every existing link. Derive that URL from the old *filename slug*,
not from `nickname` — they are often different, and getting this wrong silently
produces a redirect from a page that never existed. Check the previous build or
the `paper_url:` in the full-text index to confirm what the old URL actually was.

Keep slugs distinct from every other slug by more than case: macOS's
case-insensitive filesystem collapses case-only differences and one page
disappears from local builds without warning.

## 4. Re-render the full text

This is the step that gets skipped. If `assets/md/<slug>/` exists, its body and
figures are from the preprint and must be regenerated from the published version.

**Scrape PMC — do not OCR the PDF.** Once a paper is in PubMed Central it has a
`pmcid`, and PMC gives structured HTML with real figure files. That is the
pipeline the rest of this corpus was built with (`## Full-Text Paper Markdown
(PMC Scraping)` in `AGENTS.md`), and it is both faster and far more accurate than
running an ML layout model over a PDF. `marker_single` on an 11-page article ran
13 minutes at 13% CPU without finishing; PMC scraping takes seconds. Reach for
marker only when there is no PMCID and the full text genuinely matters.

```sh
uv run scripts/pmc-to-md.py papers/_posts/<filename>
```

Replace `index.md` and the figure images in `assets/md/<slug>/`, then apply
`assets/md/FORMATTING-RULES.md` to the result. Keep the front matter, updating
`doi` and `paper_url`. Downsample the new figures to a 1600 px long edge.

A bioRxiv preprint has no PMCID, so a preprint entry normally has no full-text
conversion at all — which is another reason the conversion must be regenerated
rather than inherited when the paper is published.

If you are not going to re-render, **delete the full-text conversion and clear
the post's `markdown:` field** rather than leaving preprint prose under a
published citation. A missing full text is honest; a stale one is not.

## 5. Update the pointers

`paper_url:` in `assets/md/<slug>/index.md` must point at the new paper URL. Grep
for the old slug across `_data/news.yml`, `cv/`, and `papers/_posts/` — internal
links are plain strings and nothing catches them when they rot.

## 6. Build and verify

```sh
bundle exec jekyll build
```

Then confirm: the paper appears under the right year and no longer under
Preprints; its page has exactly one `<h1>` and it is the title; `citation_author`
count matches the real author list; `citation_pdf_url` resolves to a file that
exists; the old URL renders as a redirect stub pointing at the new page; and no
`pdf:`/`supplement:` field anywhere references a missing file.
