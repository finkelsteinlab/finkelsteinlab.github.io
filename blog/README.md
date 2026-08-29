# Finkelstein Lab Blog

Posts are written in org-mode, converted to Jekyll markdown by a script, and
published from `master` like the rest of the site. Citations come from Zotero,
comments from GitHub Discussions, and search runs client-side in the browser.

This file is internal and excluded from the build. Everything below is
verified against the actual pipeline — where something does not work, it says
so rather than describing an intention.

**Start here:** copy `blog/_org/TEMPLATE.org`, which demonstrates every
construct that survives conversion and flags the traps inline.

## Quick Start

### Writing a New Post

1. **Copy the template** — `blog/_org/TEMPLATE.org` is a commented skeleton
   demonstrating every construct that survives conversion, with the traps
   called out inline. Start from it rather than a blank file:

```bash
cp blog/_org/TEMPLATE.org blog/_org/my-post.org
```

   The header block is all that is strictly required:

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
```

   Do **not** add a `* References` heading or `#+print_bibliography:` — the
   converter appends the bibliography itself, in Vancouver style.

2. **Convert to Jekyll post**:

```bash
./scripts/org-to-post.sh blog/_org/my-post.org
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
./scripts/org-to-post.sh blog/_org/my-post.org --draft
```

Drafts are named `YYYY-MM-DD-slug.md` just like posts, and `_config.yml`
gives them the same layout and permalink, so `jekyll serve --drafts`
previews exactly what publishing will produce.

`blog/_drafts/` is gitignored: a draft is a build artifact of its org
file, which is the thing under version control. Re-run the converter to
regenerate it on another machine.

### Overwriting an existing post

The converter refuses to overwrite a post or draft whose slug already
exists — including one filed under a different date, since two files with
the same slug would collide on the same `/blog/<slug>/` permalink. Pass
`--force` when you mean to replace it:

```bash
./scripts/org-to-post.sh blog/_org/my-post.org --force
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
ZOTERO_EXPORT=/path/to/export-bibtex.sh ./scripts/org-to-post.sh blog/_org/my-post.org
```

### Link previews

A link in a post can show a hover card (title, description, image) when
its URL is listed in `_data/link_previews.yml`. Write the link normally in
org; nothing changes in the post itself:

```org
The printer showed up via [[https://en.wikipedia.org/wiki/CUPS][CUPS]].
```

Draft the registry entry with the helper, check the text, and paste it in:

```bash
./scripts/fetch-link-preview.sh https://en.wikipedia.org/wiki/CUPS
./scripts/fetch-link-preview.sh https://example.org/post --image https://example.org/lead.jpg
```

It reads `og:title` / `og:description` / `og:image` (or Wikipedia's summary
API for Wikipedia URLs), saves the image to `assets/images/blog/previews/`
resized to 480px, and prints a YAML block. It never edits the data file,
because `og:` copy is often missing or marketing text. Entries take `url`,
`title`, `description`, `site`, `image`; only `url` and `title` are needed.

Everything is static and self-hosted. The CSP forbids fetching other
origins from the browser, so there is no live unfurling: the card is what
you put in the registry. Pieces: `_data/link_previews.yml` (registry),
`_includes/blog/link-previews.html` (embeds it as JSON on each post),
`assets/themes/lab/js/link-preview.js` (the card), `blog.css` (styling).
Cards show on hover and keyboard focus, and not at all on touch, where the
link just works as a link.

### Comments (Giscus)

- GitHub Discussions-based comments, one thread per post
- Appear at the bottom of each post; readers need a GitHub account
- Configured in `_includes/blog/giscus.html`; threads live in this repo's
  Discussions tab under the **Blog Comments** category
- The CSP allows `giscus.app` for `script-src`, `frame-src` and `style-src`,
  scoped to `/blog/` only. All three are required — miss one and comments
  fail silently, with nothing rendered and no error

### Search

- Full-text search at `/blog/search/`, entirely client-side
- Powered by Lunr, vendored at `assets/themes/lab/js/lunr.min.js` rather
  than loaded from a CDN: the CSP does not allow third-party script hosts,
  and an unpinned CDN URL would track upstream releases silently
- Searches title, tags, excerpt, and content, over `/blog/search.json`
- Direct link: `/blog/search/?q=query`. The query is escaped before display

### Tag Filtering

- Filter by tag on `/blog/` index
- Click tag buttons or use text filter
- Tag links and URL hashes use the slug: `/blog/tags/#gene-editing`
- Browse all tags: `/blog/tags/`

### RSS Feed

- Atom feed at `/blog/feed.xml`, advertised in every page's `<head>`
- Hand-written (`blog/feed.xml`), matching `atom.xml` and `rss.xml`. It
  carries only `category: blog` posts; the paper feeds exclude them.

## Directory Structure

```
blog/
├── _posts/           # Published posts (YYYY-MM-DD-slug.md)
├── _drafts/          # Draft posts (YYYY-MM-DD-slug.md, not published)
├── index.html        # Blog listing with tag filtering
├── tags/index.html   # Tag browse page
├── search/index.html # Search page
├── search.json       # Search index (generated)
├── feed.xml          # Atom feed (hand-written, like atom.xml and rss.xml)
├── README.md         # This file (excluded from the build)
└── _org/             # Org source files (underscore dir, ignored by Jekyll)
    └── TEMPLATE.org  # Commented skeleton — copy this to start a post
_csl/                 # Citation styles
  ├── vancouver.csl   # Vancouver (in use)
  └── nlm.csl         # NLM/Vancouver, Citing Medicine 2nd ed.
scripts/
  └── org-to-post.sh  # Org → Markdown converter
_includes/blog/
  └── giscus.html     # Comments configuration
assets/themes/lab/
  ├── css/blog.css    # Blog styles, loaded only under /blog/
  └── js/lunr.min.js  # Search index library, vendored (not a CDN)
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

# blog/README.md is excluded so it is not served at /blog/README.md
exclude: [..., "README.md", "blog/README.md", ...]
```

`blog/_drafts` has a matching `defaults` block, so drafts preview at the
same permalink they will publish at.

There is deliberately **no `jekyll-feed`**. It was tried and removed: its
`path` option renames the site-wide feed rather than adding one, its
`categories` option takes a list rather than the hash that was configured,
and it always emits an extra site-wide `/feed.xml` mixing papers and posts
with no way to suppress it. `blog/feed.xml` is a hand-written Liquid
template instead, matching `atom.xml` and `rss.xml`.

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
./scripts/org-to-post.sh blog/_org/test-post.org --draft
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

Keep images in a per-post folder, `assets/images/blog/<slug>/`, resized to
about 800px on the long edge; nothing resizes them for you.

### Side-by-side figures

Wrap several captioned images in a `figures` special block:

```org
#+BEGIN_figures
#+CAPTION: Figure 1a. The printer.
[[/assets/images/blog/my-post/printer.jpg]]

#+CAPTION: Figure 1b. A tank.
[[/assets/images/blog/my-post/tank.jpg]]
#+END_figures
```

Pandoc turns the block into `<div class="figures">` holding one `<figure>`
per image, and `blog.css` lays those out on a CSS grid: equal columns,
images cropped square with `object-fit: cover` so mismatched sources still
line up, stacking on narrow screens. Two or three images per row works;
more gets cramped. Any other `#+BEGIN_name` block becomes
`<div class="name">` the same way, so new layouts are a CSS rule away.

### Video and audio

Org has no native syntax for media, so drop to raw HTML. Everything between
the export markers is passed through untouched:

```org
#+BEGIN_EXPORT html
<video controls preload="metadata" width="100%"
       poster="/assets/images/blog/poster.jpg">
  <source src="/assets/video/example.mp4" type="video/mp4">
  Your browser cannot play this video.
</video>
#+END_EXPORT
```

Audio is the same, with `<audio controls src="...">`.

Media must be **self-hosted under `/assets/`**. The site's
Content-Security-Policy sets `media-src 'self'`, so a file hosted anywhere
else is refused before the request is made — Chrome reports
`MEDIA_ELEMENT_ERROR: Media load rejected by URL safety check`, which looks
like a corrupt file rather than a policy block. Always give a `poster` image
and fallback text.

The same escape hatch embeds anything else HTML can express.

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

Two things need care:

- **Definition lists** (`- term :: definition`) have no GFM equivalent
  and come out as plain lines with a hard break, not a `<dl>`. Use a
  two-column table instead.
- **Third-party embeds.** The CSP allows frames from Google and YouTube
  only, and media from this origin only. Anything else needs a CSP change
  in `_includes/themes/lab/default.html` first, or it is blocked with no
  visible error.

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

### Video or audio does not play

The CSP sets `media-src 'self'`, so media must be self-hosted under
`/assets/`. A file hosted elsewhere is refused before any request is made and
Chrome reports `MEDIA_ELEMENT_ERROR: Media load rejected by URL safety check`
— which reads like a corrupt file, not a policy block. Check the browser
console for a CSP violation before suspecting the file itself.

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
