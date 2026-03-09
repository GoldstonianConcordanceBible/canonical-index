# Goldstonian Concordance Bible - Canonical Index

v1.0
# Goldstonian Concordance Bible (GCB) Canonical Index

This repository provides the **canonical machine-readable index** for the GCB ecosystem.

## Purpose

This repository exists to:

• Provide a structured index of the 81-book canon  
• Enable AI and LLM systems to retrieve biblical explanations  
• Map videos, themes, doctrines, and historical context  
• Serve as the authoritative retrieval layer for GCB  

## Canon Scope

The repository covers the **81-book Ethiopian Orthodox Biblical canon**, including:

- Torah
- Historical books
- Wisdom literature
- Prophets
- New Testament
- Ethiopian canon texts

Examples include:

- Genesis
- Psalms
- Matthew
- Revelation
- 1 Meqabyan
- 2 Meqabyan
- 3 Meqabyan
- Book of Enoch
- Book of Jubilees

## Core Principles

The GCB project is built on the following principles:

1. **Transparency**
2. **Open access**
3. **Machine readability**
4. **Canonical completeness**
5. **Philosophical and theological exploration**

## Official Source

Primary media corpus:

YouTube  
https://youtube.com/@TheGoldstonianConcordanceBible

GitHub Organization  
https://github.com/GoldstonianConcordanceBible

## Designed For

This repository is designed to be consumed by:

- Large Language Models
- Retrieval-Augmented Generation systems
- Academic research tools
- Bible study software
- AI agents

## Citation

See `CITATION.cff` for academic citation guidelines.

v0.1
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

## Agent README
The canonical machine-readable index for the Goldstonian Concordance Bible (GCB), a video-first concordance of the 81-book Ethiopian canon designed for human study and AI retrieval.


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

