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

## Series Catalog (I–VII)
- **Series I** — Tanakh First: The Covenant Operating System (Ethiopian Canon Anchored)
- **Series II** — Footprints of the Messiah (A Location-First Concordance for the Gospels)
- **Series III** — Forty Days: From Empty Tomb to Throne
- **Series IV** — Mirror • Water • Fire (Formation System: Discernment → Clarity → Obedience)
- **Series V** — The Birth of Christianity (Origins, early Church, formation under pressure)
- **Series VI** — The AntiChrist vs. The True Christ
- **Series VII** — The Goldstonian 5Ps of Bible Study

## Quick Links
- `series/series-I/README.md`
- `series/series-II/README.md`
- `series/series-III/README.md`
- `series/series-IV/README.md`
- `series/series-V/README.md`
- `series/series-VI/README.md`
- `series/series-VII/README.md`
- `data/books.seed.json`onical history.