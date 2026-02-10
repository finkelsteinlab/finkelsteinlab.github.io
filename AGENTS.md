# Lab Website Agent Instructions

This is a Jekyll site hosted on GitHub Pages at `finkelsteinlab.org`. Push to `master` triggers an automatic Jekyll build — no custom CI/Actions.

## Auto-commit on every file change

After every file edit or write in this project, immediately stage and commit the changed file(s). Do not batch changes — commit each logical change separately.

## Git Commit Format

Use Conventional Commits style: `<type>(<scope>): <summary>`

- `type` REQUIRED. Use `feat` for new features, `fix` for bug fixes. Other common types: `docs`, `refactor`, `chore`, `test`, `perf`.
- `scope` OPTIONAL. Short noun in parentheses for the affected area (e.g., `members`, `news`, `papers`, `research`, `css`).
- `summary` REQUIRED. Short, imperative, <= 72 chars, no trailing period.
- Body is OPTIONAL. Do NOT include breaking-change markers, footers, or sign-offs.
- Only commit; do NOT push.

---

## Key Files and Directories

| Path | Purpose |
|------|---------|
| `_data/members.yml` | All lab members (current + alumni) |
| `_data/news.yml` | News feed entries |
| `_data/jobtypes.yml` | Position type labels (do not edit unless adding a new role) |
| `papers/_posts/` | One markdown file per paper |
| `papers/template.md` | Blank template for new papers |
| `cv/cv.md` | Ilya's abridged CV |
| `research/research.md` | Research descriptions |
| `teaching/teaching.md` | Teaching page content |
| `join/join.md` | "Join the lab" page content |
| `contact/contact.md` | Contact info and map |
| `assets/images/members/` | Member photos |
| `assets/images/gallery/` | Homepage carousel images |
| `assets/images/research/` | Research page figures |
| `assets/pdfs/` | Paper PDFs and supplements |
| `index.html` | Homepage (shows latest 5 news + 4 papers) |

---

## Adding/Updating Lab Members

**File:** `_data/members.yml`

### Adding a new current member

Append a new YAML block. Required fields:

```yaml
- name: First Last
  position: gradstudent          # see _data/jobtypes.yml for valid values
  email: user@utexas.edu
  image: first_last_current.jpg  # place file in assets/images/members/
  young_image: first_last_young.jpg
  favorite_activities:
    - Activity one
    - Activity two
    - Activity three
  quote: "A memorable quote."
  quote_author: Attribution
  joined: 2025-01-15             # YYYY-MM-DD
```

Optional fields: `twitter`, `website`, `CV`, `ORCID`, `GScholar`, `GitHub`, `gitlab`, `linkedin`.

**Valid `position` values:** `pi`, `managerscientist`, `manager`, `postdoc`, `gradstudent`, `research_scientist`, `undergrad`, `assistant`, `rotation`, `visiting_professor`.

### Photo naming convention

- Current photo: `firstname_lastname_current.jpg`
- Young photo: `firstname_lastname_young.jpg`
- Place both in `assets/images/members/`

### Marking a member as departed (alumni)

Add two fields to their existing entry:

```yaml
  departed: 2025-08-01           # YYYY-MM-DD
  whereabouts: Description of where they went
```

Members with a `departed` date are hidden from the current members list and shown in the Alumni table. Members without `departed` appear as current.

### Notes

- The order in `members.yml` does not affect display — members are grouped by `position` type as defined in `jobtypes.yml`.
- The members page (`members/index.html`) iterates `jobtypes.yml` keys in order, so position display order is controlled there.
- The hover effect swaps `image` and `young_image` on mouseover.
- Alumni table columns: Name, Position, Dates (joined–departed), Last Whereabouts.

---

## Adding News

**File:** `_data/news.yml`

Add a new entry anywhere in the file (entries are sorted by date automatically):

```yaml
- date: 2025-10-17
  text: Jesse Buffington et al. publish a [Nature Biotechnology](https://doi.org/10.1038/...) paper on retron editors for precise genome editing.
```

### Conventions (based on existing entries)

- **Paper published:** "Author et al. publish a [Journal](URL) paper on TOPIC."
- **PhD defense:** "Dr. First Last defends their PhD! Congrats!"
- **Member joins:** "First Last joins the Finkelstein lab as a POSITION!"
- **Member departs:** "Dr. First Last departs the lab to DESTINATION. Congratulations!"
- **Award:** "First Last is awarded AWARD_NAME."
- **Fellowship:** "First Last is awarded an F31/F32/K99 DESCRIPTION."
- Use markdown links `[text](url)` for papers, programs, etc.
- Dates use `YYYY-MM-DD` format.
- The homepage (`index.html`) shows the 5 most recent entries.
- The news page (`news/index.html`) shows all entries grouped by year, newest first.
- Future-dated entries are hidden (filtered by `event_timestamp <= current_unix_timestamp`).

---

## Adding Papers

### Step 1: Create the post file

**Directory:** `papers/_posts/`

**Filename:** `YYYY-MM-DD-Short-Descriptive-Name.md` (or `.MD`)

The date in the filename determines sort order. Use the publication date.

### Step 2: Fill in front matter

Use `papers/template.md` as a starting point:

```yaml
---
layout: paper
title: "Full Paper Title"
volume: 15
issue: 1
pages: 100-110
year: "2025"
shortref: "LastName et al. Journal (2025)"
nickname: "short-nickname"
journal: "Nature Biotechnology"
authors: "First Author&#42;;, Second Author;, ... Ilya J. Finkelstein &dagger; (&#42; co-first authors) (&dagger; co-corresponding)"
pdf: NNNN-YYYY-Author et al.pdf
supplement: NNNN-YYYY-Author et al-supplement.pdf
doi: 10.1038/s41587-025-02879-3
pmcid:
pmid: 12345678
extra_text: ''
category: paper
tags: keyword1, keyword2
---
{% include JB/setup %}

# Abstract
Paste abstract text here.
```

### Field notes

- `doi`: If starts with `10.1101/`, the paper is listed under **Preprints**. All other DOIs go under the year-grouped **Published** section.
- `journal`: Use "Submitted" or "Under review" for unpublished work.
- `pdf` / `supplement`: Filename only (no path). Place files in `assets/pdfs/`. Naming convention: `NNNN-YYYY-Author et al.pdf` where NNNN is a zero-padded sequential number.
- `volume`, `issue`, `pages`: Optional. If all three are present, the citation line reads "Journal. Vol (Issue): Pages". Otherwise just "Journal."
- `authors`: Use `&#42;` for asterisk (co-first), `&dagger;` for dagger (co-corresponding). Separate authors with `;,`.
- `category: paper` is REQUIRED (this is how Jekyll finds papers).
- `shortref`: Used in the homepage "Recent Papers" widget.

### Step 3: Add PDF files

Place in `assets/pdfs/` with naming convention: `NNNN-YYYY-Author et al.pdf`

Check the highest existing number:
```bash
ls assets/pdfs/ | sort -r | head -3
```

### Updating a paper from preprint/submitted to published

Edit the existing post file:
1. Update `doi` from bioRxiv to the published DOI
2. Update `journal` from "Submitted"/"Under review" to the journal name
3. Fill in `volume`, `issue`, `pages`, `pmid`
4. Add `pdf` and `supplement` if available
5. Optionally rename the file to reflect the publication date

---

## Updating the CV

**File:** `cv/cv.md`

This is a plain markdown file rendered via `cv/index.html`. Sections:

1. **Contact info** (top)
2. **Education**
3. **Professional Experience** — update title/dates for promotions
4. **Awards and Honors** — add new awards as bullet points
5. **Five Significant Publications** — update if desired
6. **Recent Professional Activities** — add new service roles

Update the `_Updated DATE_` line at the bottom when editing.

### Common updates

- **Promotion:** Edit the Professional Experience section (e.g., change "Associate Professor (2019- )" to add Professor)
- **New award:** Add a bullet to Awards and Honors
- **New service:** Add a bullet to Recent Professional Activities

---

## Updating Research Page

**File:** `research/research.md`

Markdown with HTML image containers. Sections use `{#anchor}` IDs linked from the homepage:
- `{#CRISPR}` — CRISPR-Cas Adaptive Immunity
- `{#DNA-repair}` — Eukaryotic Genome Maintenance
- `{#tools}` — High-throughput tools

Images are in `assets/images/research/`. Use this format:
```html
<div class="research-image-container">
  <img src="/assets/images/research/filename.png" class="research-image" width="800px" alt="description">
</div>
***Figure N. Caption.***
```

---

## Updating Teaching Page

**File:** `teaching/teaching.md`

Plain markdown. Currently describes FRI stream and BCH 339M course.

---

## Updating Join Page

**File:** `join/join.md`

Plain markdown. Lists open positions (Postdoc, Grad Student, Undergrad) with fellowship links.

---

## Updating Contact Page

**File:** `contact/contact.md`

Update title, address, phone, email as needed. Contains an embedded Google Maps iframe.

---

## Homepage

**File:** `index.html`

All content updates are done via YAML and markdown files — you should never need to edit HTML templates. The one exception is the homepage carousel, which has hardcoded image slides.

- **Carousel (only reason to edit `index.html`):** Manually defined image slides from `assets/images/gallery/`. Each slide needs a `<li>` indicator and a `<div class="item">` block.
- **News widget:** Auto-populated from the 5 most recent `_data/news.yml` entries.
- **Papers widget:** Auto-populated from the 4 most recent `papers/_posts/` entries.
- **Description text** at the top links to research page anchors.

---

## Full-Text Paper Markdown (PMC Scraping)

Papers with a `pmcid` field can have full-text HTML scraped from PubMed Central and saved as local markdown with figures.

### How it works

- **Script:** `/tmp/pmc-to-md.py` (or recreate — it crawls PMC, downloads figures, strips chrome)
- **Output:** `assets/md/<paper-slug>/index.md` + figure JPGs in same directory
- **Linking:** Add `markdown: <paper-slug>` to the paper's front matter (the slug is the filename stem, e.g., `2023-06-22-PAMless-DNA-SpRY-Cas9`)
- **Templates:** `papers/loop.html` shows `[MD]` badge; `_includes/themes/lab/paper.html` shows `Full text (md)` link
- **Layouts:** `_layouts/paper-md.html` renders the archived markdown with back-navigation

### Critical: the `markdown` field stores ONLY the slug

The templates prepend `/assets/md/` and append `/` to build the URL:
```
markdown: 2023-06-22-PAMless-DNA-SpRY-Cas9
→ href="/assets/md/2023-06-22-PAMless-DNA-SpRY-Cas9/"
→ serves assets/md/2023-06-22-PAMless-DNA-SpRY-Cas9/index.md
```

Do NOT put a full path or `/assets/md/` prefix in the `markdown` field — the templates add it.

### Adding full-text for a new paper

1. Ensure the paper post has a `pmcid` field
2. Run: `uv run /tmp/pmc-to-md.py papers/_posts/<filename>`
3. Add `markdown: <slug>` to the paper's front matter (before `extra_text:` or `category:`)
4. Commit both the `assets/md/<slug>/` directory and the updated paper post

### Notes

- 83 papers currently have PMC full-text archives (82 with `markdown:` field + 1 IgG/Science with no figures on PMC)
- Figure naming varies by journal — the script uses a catch-all approach (keeps all PMC CDN blob images except UI icons)
- The `paper-md` layout uses `paper_slug` from the archive's front matter to link back to the paper post
- Papers without `pmcid` (preprints, older papers not in PMC) need PDF→MD conversion via `marker_single` instead

---

## News and Press Archives

External links from `_data/news.yml` and paper press coverage can be archived as local markdown.

### News archives

- **Location:** `assets/md/news/<date-domain-slug>/index.md`
- **Layout:** `_layouts/news-md.html`
- **Linking:** Add `([md](/assets/md/news/<slug>/))` after the external link in `news.yml`
- Links must NOT include `.md` extension — Jekyll converts `.md` files to `.html`

### Paper press archives

- **Location:** `assets/md/papers/<paper-post-slug>/press/<outlet-slug>.md`
- **Linking:** Added to paper post's `extra_text` field under `**Press:**` header
- Format: `[Title (Outlet)](url) ([md](/assets/md/papers/.../press/slug))`
- Links must NOT include `.md` extension

---

## Deployment

1. Make edits and commit.
2. `git push origin master` — GitHub Pages rebuilds the site automatically.
3. Site is live at `finkelsteinlab.org` (CNAME configured).
