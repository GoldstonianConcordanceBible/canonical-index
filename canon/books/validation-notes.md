# Validation Notes

## Required checks
- Every slug in `canon/books/index.json` must appear only once.
- Every `path` must point to one authoritative book file.
- Every book must belong to exactly one primary group.
- Ethiopian-distinct books must not be aliased to Maccabees.
- Root duplicates like `canon/genesis.json` should be deprecated in favor of grouped canonical paths if both exist.

## Recommended next validation pass
- confirm actual filenames match lowercase kebab-case
- remove mixed-case drift where present
- align all group folders to one naming convention
- ensure `canon-index.json`, `canon-map.json`, and `canon/books/index.json` agree on counts