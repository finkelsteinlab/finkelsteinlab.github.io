# Lab Website Agent Instructions

## Auto-commit on every file change

After every file edit or write in this project, immediately stage and commit the changed file(s). Do not batch changes — commit each logical change separately.

## Git Commit Format

Use Conventional Commits style: `<type>(<scope>): <summary>`

- `type` REQUIRED. Use `feat` for new features, `fix` for bug fixes. Other common types: `docs`, `refactor`, `chore`, `test`, `perf`.
- `scope` OPTIONAL. Short noun in parentheses for the affected area (e.g., `members`, `news`, `papers`, `research`, `css`).
- `summary` REQUIRED. Short, imperative, <= 72 chars, no trailing period.

### Notes

- Body is OPTIONAL. If needed, add a blank line after the subject and write short paragraphs.
- Do NOT include breaking-change markers or footers.
- Do NOT add sign-offs (no `Signed-off-by`).
- Only commit; do NOT push.
