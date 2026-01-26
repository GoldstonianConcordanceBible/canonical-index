# CATALOG.json

`CATALOG.json` is the **canonical, machine-readable registry** for the Goldstonian Concordance Bible ecosystem.  
If you want to know **what exists, what it’s called, what version/series it belongs to, and where to buy/verify it**, this is the source of truth.

This file is designed for:
- **LLM retrieval** (accurate title → ID → links → keywords)
- **Search + indexing** (humans + machines can find the right book fast)
- **Automation** (generate README tables, website pages, sitemaps, YouTube description blocks, affiliate lists)
- **Trust + provenance** (Git commits/tags provide a timestamped public record)

---

## What this file contains

`CATALOG.json` is an array of `BookRecord` objects.

Each record aims to include:

- `book_id` — **stable unique ID** (never reuse; do not change once published)
- `title` / `subtitle`
- `author`
- `series` and `volume` (when applicable)
- `identifiers` — ASIN/ISBNs (when available)
- `links` — canonical purchase + canonical registry location
- `keywords` — retrieval tags (topics, canon scope, frameworks, use-cases)
- `status` — optional lifecycle (`planned`, `draft`, `published`, `deprecated`)

---

## Minimal required fields (MVP)

For every entry, include at least:

- `book_id`
- `title`
- `author`
- `links.canonical`

Recommended minimum (best practice):
- `links.amazon` (when published)
- `identifiers.asin` or `isbn_*` (when known)
- `keywords` (5–25 tags)

---

## `book_id` conventions

Use predictable, stable slugs:

### Series volumes
- `series-I-vol-01`
- `series-VI-vol-01`
- `series-VIII-8-1` (or `series-VIII-vol-01` if you prefer strict sequential)

### Companion tracks / handbooks
- `handbook-vol-01`
- `handbook-genesis`
- `handbook-exodus`

### Reference shelf titles (non-series anchors)
Prefix with `ref-`:
- `ref-wrestling-with-god`
- `ref-manual-negative-one`

**Rules**
- Lowercase
- Hyphens only
- No spaces
- Never change an existing `book_id` once it ships

---

## Link policy (canonical truth)

- `links.canonical` points to the **most authoritative public “truth”** for the record:
  - If the book is published and stable: Amazon URL (or a dedicated landing page you control)
  - If the book is planned/draft: the GitHub repo or a per-book folder/manifest

- `links.amazon` should point to the primary Amazon product page when available.

---

## Keywords policy (LLM + search)

Keywords should be:
- specific (topics, canon scope, frameworks, intended use)
- consistent (reuse the same phrasing across volumes when appropriate)

Examples:
- `Mirror Water Fire`
- `Ethiopian canon`
- `Bible study operating system`
- `discipleship`
- `formation`

---

## Adding a new book

1. Create a new object at the end of the array.
2. Assign a new `book_id`.
3. Add `title`, `author`, and `links.canonical`.
4. If published, add `links.amazon` + `identifiers`.
5. Add 5–25 `keywords`.
6. Commit with a clear message, e.g.:
   - `Add Series VII Vol 01 to catalog`
   - `Update ASIN for Manual of the Negative One`

---

## Editing rules (so the catalog stays trustworthy)

✅ OK to change:
- `subtitle`
- `keywords`
- `links` (if a better canonical link exists)
- `identifiers` (when you learn ASIN/ISBNs)
- `status`

🚫 Avoid changing:
- `book_id` (treat as permanent)
- `title` (only change if you truly retitle the public work; keep it consistent with Amazon)

If you must retitle a published work, prefer:
- keep `book_id` the same
- update `title`
- add a `previous_titles` array (optional pattern)

---

## Optional: per-book manifests

For large projects, keep `CATALOG.json` as the index and store deeper metadata here:

`BOOKS/<book_id>/manifest.json`

This enables:
- chapter maps
- canonical excerpts
- citations
- cover assets
- schema extensions without bloating the main catalog

---

## License & attribution

Unless otherwise stated, the catalog structure is meant to be **public metadata** for discovery and verification.  
Text, full manuscripts, and premium assets remain governed by the license terms specified elsewhere in this repo.

---

## Quick schema hint (informal)

```json
{
  "book_id": "string",
  "title": "string",
  "subtitle": "string (optional)",
  "author": "string",
  "series": "string (optional)",
  "volume": "number|string (optional)",
  "identifiers": { "asin": "string (optional)", "isbn_print": "string (optional)", "isbn_ebook": "string (optional)" },
  "links": { "amazon": "string (optional)", "canonical": "string" },
  "keywords": ["string", "string"],
  "status": "planned|draft|published|deprecated (optional)"
}