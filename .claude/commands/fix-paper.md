# Fix Paper Full-Text Markdown

Fix a paper-md full-text markdown file. The user will provide one or more paper directory names (e.g. `2019-07-04-adp-ribose-polymerase-1`). For each paper, the file is at `assets/md/<paper-name>/index.md`.

Use the haiku model for subagents. Work in batches of 2.

## What to fix

### 1. Figure order

Ensure figure blocks appear in sequential order in the document (Fig 1, Fig 2, Fig 3, ...). If a figure is out of order, move its entire block to the correct sequential position.

### 2. Figure heading format and anchors

Convert all figure headings to: `#### Figure N. {#figN}`
Update image alt text to: `![Figure N](filename.jpg)`
Make caption text bold: `**caption text**`

### 3. Figure linking

Convert ALL in-text figure references to markdown anchor links so they navigate to the figure box on the page.

**Rules:**
- `Fig. 1a` becomes `[Fig. 1a](#fig1)`
- `(Fig. 2b, c)` becomes `([Fig. 2b, c](#fig2))`
- `Figure 3` becomes `[Figure 3](#fig3)`
- `(Fig. 1a and Fig. 2b)` becomes `([Fig. 1a](#fig1) and [Fig. 2b](#fig2))`
- The anchor is always `#figN` where N is the main figure number (ignore sub-panel letters like a, b, c)
- Leave references that are already wrapped in `[...]` with `#fig` anchors alone
- Do NOT link Supplementary figures, Extended Data figures, Supporting Information figures, or Table references
- Inside figure captions, also link cross-references to other figures
- References to figures from other papers (e.g. "Fig. 1 of Smith et al.") should NOT be linked

### 4. References section

If the file does NOT already have a `## References` section (or `## REFERENCES`), fetch references from PMC and add them:
- The `pmcid` is in the YAML front matter
- Use WebFetch to get `https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`
- Extract the references/bibliography section from the page
- Add `## References` at the end of the markdown file (before any archive footer), followed by a numbered list
- Format: `1. Author names. Title. *Journal* year;volume:pages. [doi:10.xxx/yyy](https://doi.org/10.xxx/yyy)`

If the file already has a References section, leave it as-is unless it needs reformatting.

## Subagent prompt

Use this exact prompt for each subagent (replacing `<PAPER-NAME>` with the directory name):

```
Fix the paper markdown file at `/Users/ilya/Work/50 lab/finkelsteinlab.github.io/assets/md/<PAPER-NAME>/index.md`.

Follow these rules:

### 1. Figure order
Ensure figure blocks appear in sequential order (Fig 1, Fig 2, Fig 3, ...). If out of order, move the entire block.

### 2. Figure heading format and anchors
Convert all figure headings to: `#### Figure N. {#figN}`
Update image alt text to: `![Figure N](filename.jpg)`
Make caption text bold: `**caption text**`

### 3. Figure linking
Convert ALL in-text figure references to markdown anchor links:
- `Fig. 1a` → `[Fig. 1a](#fig1)`
- `(Fig. 2b, c)` → `([Fig. 2b, c](#fig2))`
- `Figure 3` → `[Figure 3](#fig3)`
- Already linked `[Fig. N](#figN)` → leave alone
- Do NOT link Supplementary/Supporting figures, Extended Data figures, or Tables
- Do NOT link figures from other papers
- Anchor is always `#figN` (number only, no panel letters)

### 4. References section
If there is NO `## References` section, fetch from PMC using pmcid from YAML front matter.
Use WebFetch to get `https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`, extract references,
add `## References` before archive footer.
Format: `1. Author names. Title. *Journal* year;volume:pages. [doi:10.xxx/yyy](https://doi.org/10.xxx/yyy)`
If references already exist, leave as-is.

Read the file, apply all fixes, write it back. Preserve all existing content.
```

## How to run

For each paper provided by the user:
1. Read the file
2. Check all four criteria above
3. Make necessary fixes
4. Write the corrected file back
5. Report what was changed

Launch one haiku subagent per paper for parallel processing (up to 2 at a time).

After all agents complete, commit the changes and push.

## Example usage

```
/fix-paper 2019-07-04-adp-ribose-polymerase-1 2020-07-16-HEDGES
```
