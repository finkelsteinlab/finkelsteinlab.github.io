# Paper Full-Text Markdown Formatting Rules

These rules standardize the formatting of archived paper full-text files in `assets/md/<paper-slug>/index.md`. Apply all rules to every file.

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
- If a reference already has `[DOI](https://doi.org/...)`, keep that format — both are acceptable
- If no DOI is available, no link is needed

### 5.3 Placeholder references

Some files have a placeholder instead of actual references:
```markdown
For the complete references list, please see the [full text on PMC](...)
```

For these files:
- Keep the placeholder as a fallback
- Inline citations in these files should still use `#refN` anchors even though the targets won't resolve — this is acceptable and will work once references are added later
- If the file ALSO has a numbered reference list below the placeholder, remove the placeholder and keep only the numbered list

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

## 7. Processing Checklist

For each `assets/md/<paper-slug>/index.md` file:

1. **Inventory figures**: List all figure image files and their current format (A/B/C/D)
2. **Convert all figures** to the standard `<figure>` HTML block (§2)
3. **Verify figure order** is sequential in the document
4. **Convert inline figure references** to `[Fig. N](#figN)` local anchors (§3)
5. **Convert inline citations** from PMC links to `#refN` local anchors (§4)
6. **Add `<span id="refN">` anchors** to each entry in the References section (§5)
7. **Verify DOI links** in the References section are present where available (§5.2)
8. **Verify** no PMC URLs remain in inline citations or figure references
9. **Verify** no content was accidentally modified

---

## 8. Verification

After processing, confirm:
- `rg 'https://pmc' <file>` returns zero matches for inline citations and figure refs (PMC URLs may remain in the front matter `source_url` and in archive footer — those are OK)
- Every `<figure>` has a matching `id="figN"`
- Every `<span id="refN">` in References has at least one corresponding `(#refN)` in the text (or the citation is unused — that's OK too)
- The file renders without broken markdown (no unclosed tags, no malformed links)
