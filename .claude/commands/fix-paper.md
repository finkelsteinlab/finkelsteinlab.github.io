# Fix Paper Full-Text Markdown

Fix a paper-md full-text markdown file. The user will provide one or more paper directory names (e.g. `2019-07-04-adp-ribose-polymerase-1`). For each paper, the file is at `assets/md/<paper-name>/index.md`.

Use the sonnet model for subagents.

## What to fix

### 1. Figure order

Ensure figure blocks appear in sequential order in the document (Fig 1, Fig 2, Fig 3, ...). A figure block consists of:
- A caption line (usually starting with `***Figure N***` or `***Fig. N.***` or similar bold/italic pattern)
- An image line (usually `![Fig. N](filename.jpg)`)

If a figure is out of order, move its entire block (caption + image) to the correct sequential position.

### 2. Figure linking

Convert ALL in-text figure references to markdown anchor links so they navigate to the figure box on the page.

**Rules:**
- `Fig. 1a` becomes `[Fig. 1a](#fig1)`
- `(Fig. 2b, c)` becomes `([Fig. 2b, c](#fig2))`
- `Figure 3` becomes `[Figure 3](#fig3)`
- `(Fig. 1a and Fig. 2b)` becomes `([Fig. 1a](#fig1) and [Fig. 2b](#fig2))`
- The anchor is always `#figN` where N is the main figure number (ignore sub-panel letters like a, b, c)
- Leave references that are already wrapped in `[...]` alone
- Do NOT link Supplementary figures, Extended Data figures, Supporting Information figures, or Table references
- Inside figure captions, also link cross-references to other figures
- References to figures from other papers (e.g. "Fig. 1 of Smith et al.") should NOT be linked

### 3. References section

If the file does NOT already have a `## References` section (or `## REFERENCES`), fetch references from PMC and add them:
- The `pmcid` is in the YAML front matter
- Use WebFetch to get `https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`
- Extract the references/bibliography section from the page
- Add `## References` at the end of the markdown file (before any archive footer), followed by a numbered list
- Format: `1. Author names. Title. *Journal* year;volume:pages. [doi:10.xxx/yyy](https://doi.org/10.xxx/yyy)`

If the file already has a References section, leave it as-is unless it needs reformatting.

## How to run

For each paper provided by the user:
1. Read the file
2. Check all three criteria above
3. Make necessary fixes
4. Write the corrected file back
5. Report what was changed

Launch one sonnet subagent per paper for parallel processing (up to 5 at a time to avoid rate limits).

After all agents complete, commit the changes and push.

## Example usage

```
/fix-paper 2019-07-04-adp-ribose-polymerase-1 2020-07-16-HEDGES
```
