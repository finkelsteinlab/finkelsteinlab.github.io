# Paper Full-Text Markdown Formatting Rules

These rules standardize the formatting of archived paper full-text files in `assets/md/<paper-slug>/index.md`. Apply all rules to every file.

**⚠️ CRITICAL: Use `edit` (find-and-replace) for all changes. Do NOT use `write` to rewrite the entire file — this risks truncation on large files. Work through the file section by section with surgical edits.**

---

## 1. Front Matter

Keep the existing YAML front matter unchanged. Do not modify `layout`, `title`, `paper_slug`, `source_url`, or `pmcid`.

---

## 2. Figures

### 2.1 Figure block format

Every figure must use this exact HTML structure:

```html
<figure class="paper-figure" id="figN">
<img src="FILENAME.jpg" alt="Figure N">
<figcaption><strong>Figure N. Title of figure.</strong> Rest of caption text...</figcaption>
</figure>
```

Rules:
- `id="figN"` where N is the figure number (e.g., `id="fig1"`, `id="fig2"`)
- `alt="Figure N"` — just the figure label, no panel letters
- Caption goes in `<figcaption>`, **below** the image
- The figure label and title are wrapped in `<strong>`: `<strong>Figure N. Title.</strong>`
- The rest of the caption follows after the `</strong>` tag within the same `<figcaption>`
- Do NOT put blank lines between the `<figure>`, `<img>`, `<figcaption>`, and `</figure>` tags
- Preserve any HTML within captions (e.g., `<em>`, `<sub>`, `<sup>`)

### 2.1a Formatting inside `<figcaption>`

Markdown syntax (`**bold**`, `_italic_`) does NOT render inside HTML tags. Use HTML equivalents:

- `**a**` → `<b>a</b>` (panel letters, labels)
- `_text_` → `<em>text</em>` (gene names, variables, species)
- Any literal asterisks must be escaped as HTML entities to prevent markdown interpretation:
  - Statistical significance: `**p < 0.01` → `&#42;&#42;p < 0.01`, `****p < 0.0001` → `&#42;&#42;&#42;&#42;p < 0.0001`
  - Scientific notation with footnote markers: `IP**` → `IP&#42;&#42;`
  - General rule: if `*` is not intended as bold/italic formatting, escape it as `&#42;`
- `(ref. [44](#ref44))` → `([44](#ref44))` — strip the `ref.` prefix

### 2.2 Converting from other formats

Replace ALL of the following legacy formats with the HTML structure above:

**Format A — bold-italic caption above image:**
```markdown
***[Figure 1](#fig1).*** Caption text...
![Figure 1](file.jpg)
```

**Format B — markdown heading with anchor:**
```markdown
#### Figure 1. {#fig1}
![Figure 1.](file.jpg)
Caption text in bold...
```

**Format C — caption below image as bold text:**
```markdown
![Figure 1](file.jpg)
**Figure 1. Caption text...**
```

**Format D — already using `<figure>` tags:**
Verify `id`, `alt`, and caption structure match the spec above. Fix if needed.

### 2.3 Figure placement

Figures should appear in sequential order (Fig 1, Fig 2, Fig 3, …) within the body text. Place each figure block near its first textual reference, between paragraphs. Do not place figures inside paragraphs.

### 2.4 Graphical abstracts

Graphical abstracts are NOT numbered figures. Leave them as simple markdown images:
```markdown
![Graphical Abstract](file.jpg)
```

---

## 3. Inline Figure References

### 3.1 Link all figure references to local anchors

Every mention of a main figure in the text must be a markdown link to its `#figN` anchor.

Examples:
- `Fig. 1A` → `[Fig. 1A](#fig1)`
- `(Fig. 2B, C)` → `([Fig. 2B, C](#fig2))`
- `Figure 3` → `[Figure 3](#fig3)`
- `(Figs. 1A and 2B)` → `([Figs. 1A](#fig1) and [2B](#fig2))`
- `(Fig. 1A–C)` → `([Fig. 1A–C](#fig1))`
- `Figures 1D–G` → `[Figures 1D–G](#fig1)`

### 3.2 Anchor format

The anchor is always `#figN` where N is the figure number only. Ignore panel letters (a, b, c) in the anchor.

### 3.3 What NOT to link

Do NOT link any of the following:
- Supplementary figures (e.g., "Figure S1", "Supplementary Fig. S2", "Extended Data Fig. 3")
- Supporting Information figures
- Table references
- Movie/Video references
- Figures from other papers (e.g., "Fig. 1 of Smith et al.")
- Scheme references

If any of the above currently link to PMC URLs, **strip the link but keep the text**:
```markdown
<!-- BEFORE -->
[Figure S1A](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#SD1)
[Table S2](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#SD1)
[Movie S1](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#SD2)

<!-- AFTER -->
Figure S1A
Table S2
Movie S1
```

### 3.4 Convert PMC figure URLs to local anchors

Replace any figure references that link to PMC URLs:
```markdown
<!-- BEFORE -->
Figure [1A](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../F1)
(Figure [2B](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../F2))

<!-- AFTER -->
[Figure 1A](#fig1)
([Figure 2B](#fig2))
```

### 3.5 Inside figure captions

Also link cross-references to other figures within `<figcaption>` text. For example, if Figure 3's caption says "see also Figure 1A", link it: `see also <a href="#fig1">Figure 1A</a>` (use HTML links inside HTML tags).

### 3.6 Already-correct references

Leave references that already use `[Fig. N](#figN)` format alone. Do not double-link.

---

## 4. Inline Citations

### 4.1 Strip PMC links, add local reference anchors

Every inline citation currently links to a PMC URL. Convert these to local anchor links pointing to the References section.

**Numbered citation style:**
```markdown
<!-- BEFORE -->
([1](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#B1),[2](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#B2))

<!-- AFTER -->
([1](#ref1),[2](#ref2))
```

**Author-year citation style:**
```markdown
<!-- BEFORE -->
([Author et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#R25))

<!-- AFTER -->
([Author et al., 2020](#ref25))
```

### 4.2 Determining the correct reference number

- For **numbered citations**: the link text IS the reference number. `[1]` → `#ref1`.
- For **author-year citations**: extract the reference number from the PMC anchor. `#R25` or `#B25` → `#ref25`. The number in the PMC anchor matches the entry number in the References section.

### 4.3 Multiple citations in one parenthetical

Keep them together in the same parentheses, separated by semicolons or commas as in the original:
```markdown
([Author et al., 2020](#ref25); [Other et al., 2019](#ref57))
([1](#ref1),[2](#ref2))
([8–10](#ref8))
```

For ranges like `[8–10]`, link only to the first reference: `[8–10](#ref8)`.

### 4.4 Citations without PMC links

Some citations may already be plain text (no link). Leave them as-is unless you can match them to a reference number, in which case add the `#refN` anchor.

### 4.5 Structural PMC links (tables, supplements, key resources)

Some files contain non-citation PMC links to structural elements like Key Resources Tables, Supplementary Tables, or "Open in a new tab" links. **Strip these links but keep the text:**
```markdown
<!-- BEFORE -->
See [Key Resources Table](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#T1)
(see [Supplement](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../#SD1))
[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC.../)

<!-- AFTER -->
See Key Resources Table
(see Supplement)
Open in a new tab
```

---

## 5. References Section

### 5.1 Anchor IDs on each reference

Add an anchor ID to each numbered reference entry so inline citations can link to it. Use a span element at the start of each entry:

```markdown
<span id="ref1">1.</span> Author names. Title. *Journal* year;volume:pages. [doi:10.xxx/yyy](https://doi.org/10.xxx/yyy)

<span id="ref2">2.</span> Author names. Title. *Journal* year;volume:pages.
```

### 5.2 DOI links

- If a reference has a DOI, format it as a link: `[doi:10.xxx/yyy](https://doi.org/10.xxx/yyy)`
- If a reference already has `[DOI](https://doi.org/...)` or `[[DOI](https://doi.org/...)]`, keep that format — both are acceptable
- If no DOI is available, no link is needed
- **Do not include stray `"` characters** in DOI text or URLs: `doi:10.xxx"` → `doi:10.xxx`
- **Do not confuse PNAS supplement URLs with DOI links.** URLs like `https://www.pnas.org/lookup/suppl/doi:10.1073/...` are supplement links, not DOI references — leave them as-is or strip to plain text per §4.5

### 5.2a Strip PMC/PubMed/Google Scholar metadata links

Many reference entries contain metadata links scraped from PMC. **Strip all of these:**
```markdown
<!-- BEFORE -->
1. Author. Title. *Journal* year;vol:pages. [[DOI](https://doi.org/...)] [[PMC free article](https://pmc.ncbi.nlm.nih.gov/...)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/...)] [[Google Scholar](https://scholar.google.com/...)]

<!-- AFTER -->
1. Author. Title. *Journal* year;vol:pages. [[DOI](https://doi.org/...)]
```

- **Keep**: `[DOI](https://doi.org/...)` links (these are the permanent identifier)
- **Strip**: `[PMC free article](...)`, `[PubMed](...)`, `[Google Scholar](...)` — remove the entire `[[text](url)]` block including surrounding brackets

### 5.3 Placeholder references

Some files have a placeholder instead of actual references:
```markdown
For the complete references list, please see the [full text on PMC](...)
```

For these files:
- Keep the placeholder as a fallback
- Inline citations in these files should still use `#refN` anchors even though the targets won't resolve — this is acceptable and will work once references are added later
- If the file ALSO has a numbered reference list below the placeholder, remove the placeholder and keep only the numbered list

### 5.3a Fetching missing references from PMC

If the file has inline `#refN` citations but no numbered reference list (only a placeholder), fetch the references from PMC:

1. Get the `pmcid` from the YAML front matter
2. Fetch `https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`
3. Extract references from the HTML — note that different journals use different markup:
   - Most journals: `<li>` elements with `id="RN"` or `id="BN"`
   - eLife and some others: `<li>` elements inside a `<ul class="ref-list">` without predictable IDs
4. Format each reference as: `<span id="refN">N.</span> Author. Title. *Journal* year;vol:pages. [doi:10.xxx](https://doi.org/10.xxx)`
5. Strip `[PMC free article]`, `[PubMed]`, `[Google Scholar]` metadata
6. Replace the placeholder with the full numbered list

### 5.4 Reference format

Do not change the citation format of existing references. They may use different journal styles (e.g., "Journal year;vol:pages" vs "Journal vol, pages (year)"). Preserve whatever format is present. Only add `<span id="refN">` anchors and DOI links.

---

## 6. Content Preservation

### 6.1 Do not modify

- Paper text content (do not rewrite, rephrase, or correct the scientific text)
- Section structure and headings
- Tables
- Equations
- Supplementary material references
- Acknowledgments, funding, author contributions
- Archive footer lines
- Front matter YAML

### 6.2 Preserve existing good formatting

- Italics for species names, gene names, Latin terms (*in vitro*, *E. coli*, etc.)
- Unicode superscripts/subscripts (10⁸, *k*<sub>cat</sub>, etc.)
- Horizontal rules between major sections
- Blank lines between paragraphs

---

## 7. Processing Strategy

**⚠️ Use `edit` (surgical find-and-replace) for ALL changes. NEVER use `write` to output the entire file.**

Large files (200+ lines) will be truncated if you try to rewrite them in a single `write` call. Instead:

1. **Read the entire file** using `read` with `offset`/`limit` to get all sections.
2. **Work section by section** using `edit` to make surgical replacements.
3. **For figure conversions**: find the exact old figure block text and replace with the new `<figure>` HTML.
4. **For inline citations**: find each paragraph containing PMC links and replace the whole paragraph with the corrected version.
5. **For reference anchors**: find each reference line and replace with the anchored version.

### Processing Checklist

For each `assets/md/<paper-slug>/index.md` file:

1. **Read the complete file** (use offset/limit — keep reading until you reach the end)
2. **Inventory figures**: List all figure image files and their current format (A/B/C/D)
3. **Convert all figures** to the standard `<figure>` HTML block (§2) — use `edit` per figure
4. **Verify figure order** is sequential in the document
5. **Convert inline figure references** to `[Fig. N](#figN)` local anchors (§3)
6. **Convert inline citations** from PMC links to `#refN` local anchors (§4)
7. **Strip structural PMC links** for tables, supplements, movies (§3.3, §4.5)
8. **Add `<span id="refN">` anchors** to each entry in the References section (§5)
9. **Verify DOI links** in the References section are present where available (§5.2)
10. **Run verification** (§8) to confirm no PMC URLs remain in citations/figure refs

---

## 8. Verification

After processing, run these checks and report results:

```bash
# 1. Count remaining PMC URLs — should ONLY be source_url in front matter and archive footer
rg -c 'https://pmc' <file>
# Expected: 1 (source_url) or 2 (source_url + archive footer)

# 2. Show any remaining PMC URLs that are NOT in front matter or archive footer
rg -n 'https://pmc' <file> | grep -v 'source_url' | grep -v 'Archived from'
# Expected: empty (no output)

# 3. Count figure blocks
rg -c '<figure class="paper-figure"' <file>

# 4. Count reference anchors
rg -c '<span id="ref' <file>

# 5. Verify file length wasn't truncated
wc -l <file>
```

**Acceptable PMC URLs** (do NOT strip these):
- `source_url:` in YAML front matter
- Archive footer: `*Archived from [PubMed Central](https://pmc.ncbi.nlm.nih.gov/...) on YYYY-MM-DD.*`

**Everything else** with `https://pmc` must be converted or stripped.
