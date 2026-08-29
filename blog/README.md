# Finkelstein Lab Blog

A Jekyll-based blog with org-mode authoring, Zotero citations, and GitHub Discussions comments.

## Quick Start

### Writing a New Post

1. **Create an org file** in `_org/blog/`:

```org
#+TITLE: My Post Title
#+DATE: <2026-02-15 Sun>
#+DESCRIPTION: A brief description for previews
#+TAGS: crispr, gene editing, methods
#+BIBLIOGRAPHY: citekey1 citekey2
#+OPTIONS: ^:{}

* Introduction

Your content here. Use [cite:@citekey1] for citations.

* Another Section

More content with another citation [cite:@citekey2].

* References

#+print_bibliography:
```

2. **Convert to Jekyll post**:

```bash
./scripts/org-to-post.sh _org/blog/my-post.org
```

3. **Preview locally**:

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle exec jekyll serve --drafts
# Visit http://localhost:4000/blog/
```

4. **Commit and push** to publish.

### Draft Posts

Use the `--draft` flag to save to `blog/_drafts/` instead of `blog/_posts/`:

```bash
./scripts/org-to-post.sh _org/blog/my-post.org --draft
```

Drafts are named `YYYY-MM-DD-slug.md` just like posts, and `_config.yml`
gives them the same layout and permalink, so `jekyll serve --drafts`
previews exactly what publishing will produce.

### Overwriting an existing post

The converter refuses to overwrite a post or draft whose slug already
exists — including one filed under a different date, since two files with
the same slug would collide on the same `/blog/<slug>/` permalink. Pass
`--force` when you mean to replace it:

```bash
./scripts/org-to-post.sh _org/blog/my-post.org --force
```

### When conversion fails

The converter exits non-zero and writes nothing if anything is wrong. It
does not produce a half-correct post. The cases it stops on:

| Failure | What to do |
|---------|------------|
| No `#+TITLE:` | Add one. |
| No `#+TAGS:` | Add at least one tag — see below. |
| `#+DATE:` it cannot parse, or a date that does not exist | Use one of the accepted forms below. |
| A citekey that does not resolve, or resolves to an entry under a different key | Check Zotero is running; check the key. |
| The slug already exists | Pass `--force`. |
| The Zotero exporter is missing | Set `ZOTERO_EXPORT` (see below). |

## Post Metadata

### `#+TITLE:` — required

Becomes the post title, the page's only `<h1>`, and the slug. Quotes,
colons and apostrophes are all safe: the front matter is emitted as
single-quoted YAML scalars.

### `#+DATE:` — optional, defaults to today

Both plain dates and org timestamps are accepted, with or without a day
name and with or without a time:

```org
#+DATE: 2026-03-01
#+DATE: <2026-03-01 Sun>
#+DATE: [2026-03-01 Sun]
#+DATE: <2026-03-01 Sun 14:30>
#+DATE: <2026-03-01 Sun 14:30-15:30>
```

`C-c .` in Emacs inserts the `<2026-03-01 Sun>` form, which is what you
will normally have. All of these normalise to `2026-03-01` in both the
filename and the front matter. Anything else — or a date that does not
exist, like `2026-02-31` — is an error.

### `#+TAGS:` — required

**Every post must carry at least one tag.** An untagged post never
appears in the tag cloud, the tag filter on `/blog/`, or `/blog/tags/`,
so it is effectively invisible. A missing or empty `#+TAGS:` line is a
hard error.

Tags are lowercased and slugified, so they match the `#anchor` links and
the exact-match tag filter the site uses:

```org
#+TAGS: crispr methods gene-editing     -> crispr, methods, gene-editing
#+TAGS: Gene Editing, CRISPR-Cas9       -> gene-editing, crispr-cas9
```

Separate tags with **commas** when a tag contains a space; with spaces
alone, each word becomes its own tag. Org's `:tag1:tag2:` filetag syntax
works too.

### `#+BIBLIOGRAPHY:` — optional

Space-separated citekeys. Keys cited in the body but omitted here are
picked up automatically.

### `#+OPTIONS: ^:{}` — recommended

Org treats `A_B` as a subscript, which quietly mangles gene and variable
names (`Cas9_v2`, `ATTR_HTML`) into `Cas9<sub>v2</sub>`. `^:{}` limits
subscripts to the explicit `H_{2}O` form and leaves bare underscores
alone.

## Features

### Citations from Zotero

- Add citekeys to the `#+BIBLIOGRAPHY:` header (space-separated)
- Use `[cite:@citekey]` in text for inline citations
- Requires Zotero desktop running with Better BibTeX
- Citations rendered in Vancouver/NLM (PubMed) style

**A citekey that does not resolve aborts the conversion.** The converter
validates that Zotero actually returned BibTeX keyed by the key it asked
for, so an unreachable Zotero, a typo'd key, or a key that maps to a
different entry all fail loudly instead of producing a post whose
citations render as `[**citekey?**]` with an empty bibliography.

The exporter is found at `~/.pi/agent/skills/zotero/export-bibtex.sh` by
default. Override it with the `ZOTERO_EXPORT` environment variable:

```bash
ZOTERO_EXPORT=/path/to/export-bibtex.sh ./scripts/org-to-post.sh _org/blog/my-post.org
```

### Comments (Giscus)

- GitHub Discussions-based comments
- Appear at bottom of each post
- Configured in `_includes/blog/giscus.html`
- Comments stored in repo's Discussions tab

### Search

- Full-text search at `/blog/search/`
- Powered by Lunr.js (client-side)
- Searches title, tags, excerpt, and content
- Direct link: `/blog/search/?q=query`

### Tag Filtering

- Filter by tag on `/blog/` index
- Click tag buttons or use text filter
- Tag links and URL hashes use the slug: `/blog/tags/#gene-editing`
- Browse all tags: `/blog/tags/`

### RSS Feed

- Atom feed at `/blog/feed.xml`
- Auto-discovered by browsers/readers

## Directory Structure

```
blog/
├── _posts/           # Published posts (YYYY-MM-DD-slug.md)
├── _drafts/          # Draft posts (YYYY-MM-DD-slug.md, not published)
├── index.html        # Blog listing with tag filtering
├── tags/index.html   # Tag browse page
├── search/index.html # Search page
├── search.json       # Search index (generated)
├── feed.xml          # RSS feed (generated by jekyll-feed)
└── README.md         # This file

_org/blog/            # Org source files
_csl/                 # Citation styles
  ├── vancouver.csl   # Vancouver (in use)
  └── nlm.csl         # NLM/Vancouver, Citing Medicine 2nd ed.
scripts/
  └── org-to-post.sh  # Org → Markdown converter
_includes/blog/
  └── giscus.html     # Comments configuration
```

## Configuration

### _config.yml Settings

```yaml
# Blog post defaults
defaults:
  - scope:
      path: "blog/_posts"
      type: "posts"
    values:
      layout: "blog-post"
      category: "blog"
      author: "Ilya Finkelstein"
      permalink: /blog/:slug/

# RSS feed
plugins:
  - jekyll-feed

feed:
  categories:
    - blog
```

`blog/_drafts` has a matching `defaults` block, so drafts preview at the
same permalink they will publish at.

### Citation Style

Vancouver (`_csl/vancouver.csl`) is what the converter uses. `_csl/nlm.csl`
is the NLM/Vancouver *Citing Medicine* 2nd-edition style, kept as an
alternative. To switch, or to add another style:

1. Download a CSL file from https://www.zotero.org/styles (or
   https://github.com/citation-style-language/styles)
2. Save it to `_csl/` and check it with `xmllint --noout _csl/<file>.csl`
3. Update `CSL_FILE` in `scripts/org-to-post.sh`

## Local Development

### Requirements

- **Ruby 3.3** (via Homebrew: `brew install ruby@3.3`). Ruby 4.x makes
  bundler backtrack to `github-pages 15` and fail on `yajl-ruby`; macOS
  system Ruby is far too old. See `AGENTS.md`.
- Bundler (`gem install bundler:2.6.9`)
- Pandoc (`brew install pandoc`)
- Zotero with Better BibTeX (for citations)

### Setup

```bash
# Use Homebrew Ruby
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve --drafts
```

### Testing Posts

```bash
# Convert and preview
./scripts/org-to-post.sh _org/blog/test-post.org --draft
bundle exec jekyll serve --drafts
# Visit http://localhost:4000/blog/test-post/
```

Before pushing, run the same checks the rest of the site uses:

```bash
bundle exec jekyll build
xmllint --noout _site/atom.xml _site/rss.xml _site/sitemap.xml _site/blog/feed.xml
```

## Org-mode Syntax Reference

### Headers

```org
#+TITLE: Required - becomes the post title and the slug
#+DATE: Optional - plain date or org timestamp; defaults to today
#+DESCRIPTION: Optional - for previews and meta tags
#+TAGS: REQUIRED - at least one; comma- or space-separated
#+BIBLIOGRAPHY: citekey1 citekey2 citekey3
#+OPTIONS: ^:{}
```

### Headings

Use `*` for the top level. The converter shifts every heading down one
level so `*` becomes `<h2>`: the layout already renders the post title as
the page's `<h1>`, and a page must have exactly one.

### Citations

```org
Single citation [cite:@smith_paper_2024]
Multiple citations [cite:@smith_paper_2024;@jones_study_2023]
```

### Images

Site-absolute paths work in all three forms — the converter strips the
`file://` prefix pandoc's org reader adds to them:

```org
[[/assets/images/blog/fig.jpg]]

#+ATTR_HTML: :alt A diagram of the delivery workflow
[[/assets/images/blog/fig.jpg]]

#+CAPTION: Figure 1. A diagram of the delivery workflow.
[[/assets/images/blog/fig.jpg]]
```

`#+CAPTION:` produces a `<figure>` with a `<figcaption>`. Note that
`#+ATTR_HTML:` and `#+CAPTION:` on the *same* image put the attributes on
the `<figure>`, not the `<img>`, so the `alt` is lost — use one or the
other.

`[[/path][description]]` makes a **link** with that text, not an image
with alt text. For alt text, use `#+ATTR_HTML: :alt ...`.

### Other blocks

All of these survive conversion and render correctly:

| Org | Result |
|-----|--------|
| `#+BEGIN_QUOTE` … `#+END_QUOTE` | `<blockquote>`; a `--- Attribution` line becomes a final paragraph |
| `#+BEGIN_SRC python` … `#+END_SRC` | fenced block; Rouge syntax-highlights it |
| `#+BEGIN_EXAMPLE` … `#+END_EXAMPLE` | plain `<pre><code>` |
| `#+BEGIN_EXPORT html` … `#+END_EXPORT` | raw HTML, passed straight through |
| `\| a \| b \|` tables | `<table>` |
| nested `-` / `1.` lists | nested `<ul>` / `<ol>` |
| `[fn:1]` footnotes | numbered footnotes with backlinks |
| `-----` | `<hr>` |
| `*bold*` `/italic/` `=code=` `~verbatim~` | `<strong>` `<em>` `<code>` `<code>` |

Two things do **not** survive:

- **Definition lists** (`- term :: definition`) have no GFM equivalent
  and come out as plain lines with a hard break, not a `<dl>`. Use a
  two-column table instead.
- **`<video>` elements** embed fine via `#+BEGIN_EXPORT html`, but the
  site's Content-Security-Policy has no `media-src` directive and
  `default-src 'none'`, so the browser blocks the media. Adding
  `media-src 'self';` to the CSP in `_includes/themes/lab/default.html`
  is a prerequisite for video.

One org gotcha, not a converter bug: a footnote definition absorbs
everything that follows it until the next heading or footnote definition.
Put footnote definitions last in their section, or at the end of the file.

### Find Citekeys

```bash
# Search Zotero by keyword
~/.pi/agent/skills/zotero/search.sh "CRISPR"

# Export BibTeX for a citekey
~/.pi/agent/skills/zotero/export-bibtex.sh "smith_paper_2024"
```

## Troubleshooting

### Conversion fails on a citekey

1. Ensure Zotero is running with Better BibTeX
2. Check the key exists: `~/.pi/agent/skills/zotero/export-bibtex.sh "citekey"`
3. If the exporter lives elsewhere, set `ZOTERO_EXPORT`

Note that the exporter prints its failure message to stdout and exits 1.
The converter separates the two and checks that what came back is really
BibTeX for the key requested, so it will not be fooled by that.

### Jekyll won't start

```bash
# Use correct Ruby version
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# Reinstall dependencies
bundle install
```

Do **not** delete `Gemfile.lock`. It pins `github-pages 232` / `jekyll
3.10.0`, the same stack GitHub Pages runs; removing it lets bundler
resolve a different set and what builds locally stops matching what
deploys.

### A post does not appear anywhere

Check it has tags. An untagged post is missing from the tag cloud, the
`/blog/` tag filter and `/blog/tags/`. The converter now refuses to
produce one, but posts predating that check may exist.

### Search not working

- Ensure `blog/search.json` is being generated
- Check browser console for JavaScript errors
- Search index loads asynchronously; wait a moment after page load
