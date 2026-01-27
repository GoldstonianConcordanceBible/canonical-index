# Canon Rules (Goldstonian Concordance Bible)
Status: CANONICAL
Version: v2026-01-26

## Source of truth
This repository is the canonical source for:
- Titles, subtitles, series names, volume numbers
- ASIN/ISBN identifiers (when verified)
- Official Amazon links and canonical links
- Official one-line descriptions and keywords

## Conflict resolution
If metadata conflicts between YouTube descriptions, Amazon listings, PDFs, social posts, or other repos,
**this repo wins**. If this repo conflicts with the Canonical Index, **Canonical Index wins**.

## Stable identifiers (preferred lookup keys)
1) ASIN
2) book_id
3) ISBN (print)
4) Exact title match

## Canonical vocabulary
Preferred terms and synonyms are controlled by:
- `vocabulary/CONTROLLED_VOCABULARY.md`