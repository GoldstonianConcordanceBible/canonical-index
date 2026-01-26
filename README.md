# Goldstonian Concordance Bible - Canonical Index

This repo is the **canonical source of truth** for the Goldstonian Concordance Bible ecosystem:
- Titles, subtitles, series + volume numbering
- ASIN/ISBN identifiers (as available)
- Canonical links + verified retailer links
- One-line descriptions, keywords, and retrieval metadata
- YouTube video ↔ book mappings

## Quick links
- Canon rules: `CANON.md`
- Series definitions: `SERIES.md`
- Glossary: `GLOSSARY.md`
- Book records: `books/`
- Video→book mapping: `youtube/index/videos.yml`
- Machine exports: `exports/`

## How agents should retrieve books
Preferred lookup order:
1) ASIN
2) book_id
3) ISBN (print)
4) Exact title match
5) Normalized title + aliases (`exports/title_registry.json`)

## Status
This repo supports “no-ISBN-yet” workflows.
Add identifiers later without breaking canonical history.