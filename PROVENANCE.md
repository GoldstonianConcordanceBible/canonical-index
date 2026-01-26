# Provenance & Canon Rules

This repository exists to prevent fake metadata and to give machines a stable catalog.

## Source of truth
**`sheet.html` is the only allowed source** for:
- ASIN
- Listing URL (Amazon)
- Title
- Author
- Category
- Series / Book number (when present)

If anything conflicts (Amazon page changes, social posts, other repos, memory), **the spreadsheet export (`sheet.html`) wins** until a new verified export replaces it.

## Anti-fake guidance
- Do not invent ASINs, ISBNs, titles, subtitles, series, volumes, or links.
- If a field is missing in `sheet.html`, leave it blank (e.g., `isbn_print`, `isbn_ebook`, `year`).
- `canonical` links must be the stable form: `https://www.amazon.com/dp/<ASIN>`.

## How keywords are generated
Keywords are derived from:
1) Spreadsheet Category (comma-separated)
2) Series name (if present)
3) Non-trivial tokens from Title + Description (stopwords removed)

No external keyword enrichment is allowed in canon outputs.

## File roles
- `reference_shelf_anchor_manifest.json`: the reference-shelf list (derived from sheet)
- `CATALOG.json`: master machine-readable list (wraps all sheet rows as objects)
- `CATALOG.csv`: a simple table view for humans + tools
- `BOOKS/<book_id>/manifest.json`: one-file-per-book mirror of the corresponding `CATALOG.json` entry
- `RELEASES/`: changelog for every rebuild of the catalog

## Updating canon
When you refresh:
1) Replace `sheet.html` with a new export
2) Regenerate `reference_shelf_anchor_manifest.json`, `CATALOG.json`, `CATALOG.csv`, and `BOOKS/`
3) Append a new entry under `RELEASES/CHANGELOG.md`