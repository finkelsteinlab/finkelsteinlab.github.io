# Paper Full-Text Markdown Formatting Rules

These rules standardize the formatting of archived paper full-text files in `assets/md/<paper-slug>/index.md`. Apply all rules to every file.

**⚠️ CRITICAL: Use `edit` (find-and-replace) for all changes. Do NOT use `write` to rewrite the entire file — this risks truncation on large files. Work through the file section by section with surgical edits.**

---

## 1. Front Matter

Keep the existing YAML front matter unchanged. Do not modify `layout`, `title`, `paper_slug`, `source_url`, or `pmcid`.

---

## 1a. Common Scraper Artifacts

The PMC-to-markdown scraper introduces several systematic artifacts. Fix all of these early in processing:

### Double-space headers

The scraper produces `##  Title` (two spaces after `##`). Normalize to single space:
```
##  Abstract  →  ## Abstract
##  Results   →  ## Results
```
This applies to all heading levels (`##`, `###`, `####`).

### Broken image filenames

In Nature Communications and some other Springer Nature papers, the scraper embeds markdown link syntax inside `<img>` src filenames:
```html
<!-- BROKEN -->
<img src="41467_2024_47830_[Fig1](#fig1)_HTML.jpg" alt="Figure 1">

<!-- FIXED -->
<img src="41467_2024_47830_Fig1_HTML.jpg" alt="Figure 1">
```
Check actual filenames on disk with `ls assets/md/<slug>/*.jpg` and fix any `src` attributes that don't match.

### Supplementary figures incorrectly linked to main figure anchors

The scraper sometimes converts "Supplementary Fig. N" or "Supplementary [Fig. N]" into markdown links targeting the main figure anchors:
```markdown
<!-- BROKEN -->
Supplementary [Fig. 5](#fig5)
(Supplementary [Figs. 5 and 6](#fig5))

<!-- FIXED -->
Supplementary Fig. 5
(Supplementary Figs. 5 and 6)
```
Per §3.3, supplementary figures must NOT link to local anchors. Strip these links but keep the text.

### "Open in a new tab" artifacts

The scraper inserts `Open in a new tab` lines after tables. Delete these entirely:
```
Open in a new tab     ← delete this line
```

### Malformed mailto links

The scraper sometimes prepends `http://` to `mailto:` links in STAR Methods / contact sections:
```markdown
<!-- BROKEN -->
[email](http://mailto:user@example.edu)

<!-- FIXED -->
[email](mailto:user@example.edu)
```

### Plain-text superscripts and subscripts

The scraper strips all HTML `<sup>` and `<sub>` tags, producing plain text like `× 106 M−1 sec−1` instead of `× 10⁶ M⁻¹ sec⁻¹`, and `Mg2+` instead of `Mg²⁺`. See §6a for systematic fix procedures.

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

### 3.1a Panel letters must be inside the link text

Panel letters belong inside the linked text, not detached after it. Watch for two common scraper artifacts:

```markdown
<!-- BROKEN: space separates panel letter from link -->
[Fig. 2](#fig2) A

<!-- BROKEN: panel letter after closing bracket -->
([Figure 3](#fig3)D)

<!-- FIXED -->
[Fig. 2A](#fig2)
([Figure 3D](#fig3))
```

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

## 6a. Scientific Notation, Units, and Chemical Formatting

The PMC scraper strips superscripts and subscripts, producing plain text like `× 106 M−1 sec−1` instead of `× 10⁶ M⁻¹ sec⁻¹`. **Always verify against the PDF** — the PDF is ground truth.

### 6a.1 Exponents in scientific notation

Use Unicode superscripts for all exponents. Never leave plain-digit exponents after `× 10`:

| Wrong | Correct |
|-------|---------|
| `× 103` | `× 10³` |
| `× 105` | `× 10⁵` |
| `× 106` | `× 10⁶` |
| `× 107` | `× 10⁷` |
| `× 10−3` | `× 10⁻³` |
| `× 10−5` | `× 10⁻⁵` |
| `× 10−6` | `× 10⁻⁶` |

Unicode superscript digits: `⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺`

### 6a.2 Unit superscripts

Use Unicode superscripts in units. This applies in body text, figure legends, tables, and table headers:

| Wrong | Correct |
|-------|---------|
| `M−1 sec−1` | `M⁻¹ sec⁻¹` |
| `M−1 s−1` | `M⁻¹ s⁻¹` |
| `sec−1` | `sec⁻¹` |
| `min−1` | `min⁻¹` |
| `nm2` | `nm²` |

### 6a.3 Ion charges

Use Unicode superscripts for ion charges:

| Wrong | Correct |
|-------|---------|
| `Mg2+` | `Mg²⁺` |
| `Ca2+` | `Ca²⁺` |
| `Mn2+` | `Mn²⁺` |
| `Zn2+` | `Zn²⁺` |

This applies everywhere: body text, section headings, figure legends, tables.

### 6a.4 Chemical formulas

Use Unicode subscripts for chemical formula subscripts:

| Wrong | Correct |
|-------|---------|
| `MgCl2` | `MgCl₂` |
| `CaCl2` | `CaCl₂` |
| `CO2` | `CO₂` |
| `H2O` | `H₂O` |
| `His6` (hexahistidine tag) | `His₆` |

Unicode subscript digits: `₀₁₂₃₄₅₆₇₈₉`

For radioactive isotopes, use Unicode superscripts:

| Wrong | Correct |
|-------|---------|
| `[γ-32P]` | `[γ-³²P]` |
| `γ−32P` | `γ-³²P` |
| `35S` | `³⁵S` |
| `14C` | `¹⁴C` |

### 6a.5 Kinetic parameters and thermodynamic variables

In **body text** (markdown context), use `*italic*` + `<sub>`:

| Parameter | Markdown |
|-----------|----------|
| *k*<sub>cat</sub> | `*k*<sub>cat</sub>` |
| *K*<sub>M</sub> | `*K*<sub>M</sub>` |
| *k*<sub>on</sub> | `*k*<sub>on</sub>` |
| *k*<sub>off</sub> | `*k*<sub>off</sub>` |
| *K*<sub>d</sub> | `*K*<sub>d</sub>` |
| *k*<sub>max</sub> | `*k*<sub>max</sub>` |
| *k*<sub>obs</sub> | `*k*<sub>obs</sub>` |
| *t*<sub>1/2</sub> | `*t*<sub>1/2</sub>` |
| *k*<sub>cat</sub>/*K*<sub>M</sub> | `*k*<sub>cat</sub>/*K*<sub>M</sub>` |
| IC₅₀ | `IC₅₀` |

The PMC scraper often produces `_k_ cat/_K_ M` (underscores with spaces). Replace these systematically:
- `_k_ cat/_K_ M` → `*k*<sub>cat</sub>/*K*<sub>M</sub>`
- `_k_ on` → `*k*<sub>on</sub>`
- `_k_ off` → `*k*<sub>off</sub>`
- `_K_ d` → `*K*<sub>d</sub>`
- `_t_ 1/2` → `*t*<sub>1/2</sub>`
- `_k_ max` → `*k*<sub>max</sub>`
- `_k_ obs` → `*k*<sub>obs</sub>`
- `_k_ raw` → `*k*<sub>raw</sub>`

In **`<figcaption>` and other HTML contexts** (where markdown doesn't render), use HTML tags:

| Parameter | HTML |
|-----------|------|
| *k*<sub>on</sub> | `<i>k</i><sub>on</sub>` |
| *k*<sub>off</sub> | `<i>k</i><sub>off</sub>` |
| *K*<sub>d</sub> | `<i>K</i><sub>d</sub>` |

The scraper often produces plain `k on`, `k off` inside `<figcaption>` — these need to be found by context (e.g., "value of k on", "Values of k on and k off", "give k on values") and replaced with the HTML form.

### 6a.6 Table footnote superscripts

Table footnote markers should use `<sup>` tags:

**In table rows:**
```markdown
crRNA(−18:+24)*<sup>a</sup> | 1.4 (±0.3) × 10⁷ | ...
```

**In footnote text:**
```markdown
<sup>a</sup>For crRNA variants, the asterisk indicates...
<sup>b</sup>For the determination of...
<sup>c</sup>Measured using excess...
```

### 6a.7 Bulk replacement strategy

These fixes are pervasive (dozens of instances per file). Use `sed` for systematic replacement, then targeted `edit` for edge cases:

```bash
FILE="assets/md/<slug>/index.md"

# 1. Scientific notation exponents
sed -i '' 's/× 103 /× 10³ /g' "$FILE"
sed -i '' 's/× 105 /× 10⁵ /g' "$FILE"
sed -i '' 's/× 106 /× 10⁶ /g' "$FILE"
sed -i '' 's/× 107 /× 10⁷ /g' "$FILE"
sed -i '' 's/× 10−3 /× 10⁻³ /g' "$FILE"
sed -i '' 's/× 10−5 /× 10⁻⁵ /g' "$FILE"
sed -i '' 's/× 10−6 /× 10⁻⁶ /g' "$FILE"

# 2. Unit superscripts
sed -i '' 's/M−1 sec−1/M⁻¹ sec⁻¹/g' "$FILE"
sed -i '' 's/sec−1/sec⁻¹/g' "$FILE"

# 3. Ion charges
sed -i '' 's/Mg2+/Mg²⁺/g' "$FILE"

# 4. Chemical formulas
sed -i '' 's/MgCl2/MgCl₂/g' "$FILE"
sed -i '' 's/CaCl2/CaCl₂/g' "$FILE"
sed -i '' 's/His6/His₆/g' "$FILE"
sed -i '' 's/OD600/OD₆₀₀/g' "$FILE"

# 5. Additional unit superscripts (methods sections)
sed -i '' 's/μg μl−1/μg μl⁻¹/g' "$FILE"
sed -i '' 's/mg ml−1/mg ml⁻¹/g' "$FILE"
sed -i '' 's/μm2 s−1/μm² s⁻¹/g' "$FILE"

# 6. Verify no remaining plain exponents or unformatted ions
rg '× 10[0-9−]' "$FILE"
rg 'Mg2\+|Ca2\+|Mn2\+' "$FILE"
rg 'MgCl2|CaCl2' "$FILE"
```

**Caution with sed:** Always check that the replacements don't clobber other text. For example, `His6` → `His₆` is safe because "His6" only appears as the hexahistidine tag in biochemistry papers. But watch for false positives with short patterns.

### 6a.8 Additional common formatting issues

These issues appear frequently across verified papers:

#### Spectroscopic and optical measurements

| Wrong | Correct | Context |
|-------|---------|---------|
| `OD600` | `OD₆₀₀` | Optical density at 600 nm |
| `A260` | `A₂₆₀` | Absorbance at 260 nm |
| `λex` / `λem` | `λ<sub>ex</sub>` / `λ<sub>em</sub>` | Excitation/emission wavelengths |

#### Complex chemical names with subscripts

Fluorescent reporters and labeled probes often have numeric subscripts:

| Wrong | Correct |
|-------|---------|
| `FQ-C5` | `FQ-C₅` |
| `FQ-C10` | `FQ-C₁₀` |
| `FQ-T5` | `FQ-T₅` |
| `FAM2-T5-Biotin2` | `FAM₂-T₅-Biotin₂` |
| `Dig-Sp18-FAM-T5-Biotin2` | `Dig-Sp₁₈-FAM-T₅-Biotin₂` |

#### Protein structural motifs

| Wrong | Correct |
|-------|---------|
| `(βα)6-barrel` | `(βα)₆-barrel` |
| `p202p102` (caspase stoichiometry) | `p20₂p10₂` |

#### Concentration and physical units

Extended unit superscripts commonly found in methods sections:

| Wrong | Correct |
|-------|---------|
| `μm2 s−1` | `μm² s⁻¹` |
| `μg μl−1` | `μg μl⁻¹` |
| `mg ml−1` | `mg ml⁻¹` |
| `ng μl−1` | `ng μl⁻¹` |
| `μM−1` | `μM⁻¹` |
| `mL−1` | `mL⁻¹` |
| `L−1` | `L⁻¹` |
| `W cm−2` | `W cm⁻²` |

#### p-value asterisks in figcaptions

Inside `<figcaption>` (HTML context), literal asterisks for statistical significance must be HTML-encoded to prevent markdown interpretation:

| Wrong | Correct |
|-------|---------|
| `*P < 0.05` | `&#42;P < 0.05` |
| `**P < 0.01` | `&#42;&#42;P < 0.01` |
| `***P < 0.001` | `&#42;&#42;&#42;P < 0.001` |
| `****P < 0.0001` | `&#42;&#42;&#42;&#42;P < 0.0001` |

#### Species abbreviations in CRISPR papers

Cas9/Cas12a ortholog papers use italicized species abbreviations:

| Wrong | Correct |
|-------|---------|
| `SaCas9` or `Sa Cas9` | `_Sa_ Cas9` (body) or `<em>Sa</em> Cas9` (HTML) |
| `SpCas9` | `_Sp_ Cas9` |
| `FnCas9` | `_Fn_ Cas9` |
| `NmeCas9` | `_Nme_ Cas9` |
| `LbCas12a` | `_Lb_ Cas12a` |
| `AsCas12a` | `_As_ Cas12a` |

Note: Some papers use `dSaCas9` for dead/nuclease-dead variants — keep the `d` prefix non-italic: `d_Sa_ Cas9`.

#### Latin terms

Always italicize:
- `*in vitro*`, `*in vivo*`, `*in situ*`
- `*cis*`, `*trans*` (especially in Cas12a *trans*-cleavage papers)
- `*de novo*`, `*et al.*`

---

## 6b. PDF Verification

After formatting a paper's `index.md`, verify the markdown against the published PDF. **The PDF is always ground truth.**

### 6b.1 Convert PDF to images

```bash
mkdir -p /tmp/<slug>-pdf
pdftoppm -png -r 200 "assets/pdfs/<pdf-file>.pdf" /tmp/<slug>-pdf/page
```

### 6b.2 Verification checklist

Image each PDF page and compare against the markdown:

| Check | What to verify |
|-------|----------------|
| **Title** | Exact match including en-dashes, special chars |
| **Authors** | All names present, correct corresponding-author markers |
| **Abstract** | Verbatim text, *K*<sub>d</sub> and other symbols correct |
| **Body text** | Spot-check superscripts, subscripts, ion charges, rate constants |
| **Table values** | Every cell value matches PDF; exponents are superscripted |
| **Table headers** | Column names with correct sub/superscripts |
| **Table footnotes** | Footnote markers are superscripted, text matches |
| **Figure legends** | Full caption text matches PDF; kinetic parameters formatted |
| **Equations** | All terms correct (if any) |
| **Chemical formulas** | MgCl₂, His₆, ³²P, etc. |
| **References** | Count matches PDF; spot-check a few entries |

### 6b.3 Document results

After verification, add a note to `FORMATTING-STATUS.org` in the `:PROPERTIES:` block:

```org
:VERIFIED: YYYY-MM-DD
:VERIFIED_NOTES: Title ✓, authors ✓, abstract ✓, Table 1 (8 rows) ✓, Figs 1-7 ✓, 22 refs ✓. Formatting fixes applied: superscripts, Mg²⁺, kinetic params, table footnotes.
```

---

## 7. Processing Strategy

**⚠️ Use `edit` (surgical find-and-replace) for ALL changes. NEVER use `write` to output the entire file.**

Large files (200+ lines) will be truncated if you try to rewrite them in a single `write` call. Instead:

1. **Read the entire file** using `read` with `offset`/`limit` to get all sections.
2. **Work section by section** using `edit` to make surgical replacements.
3. **For figure conversions**: find the exact old figure block text and replace with the new `<figure>` HTML.
4. **For inline citations**: find each paragraph containing PMC links and replace the whole paragraph with the corrected version.
5. **For reference anchors**: find each reference line and replace with the anchored version.

### Agent reliability note

When running as a background `pi -p` agent, the process may terminate before committing. This is expected — edits persist in the git working tree. After an agent batch completes, check `git status` for uncommitted changes and commit them manually. If a file has 0 ref anchors or many remaining PMC URLs, relaunch a dedicated agent for that file.

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
# IMPORTANT: chain separate filters — do NOT use rg -v 'a\|b' (backslash-pipe is literal in rg)
rg -n 'https://pmc' <file> | rg -v 'source_url' | rg -v 'Archived from'
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
