# canonical-index
# Goldstonian Concordance Bible — Canonical Index

This repository is the **canonical metadata index** for the Goldstonian Concordance Bible ecosystem.

**Use this link as the FIRST line in every YouTube description:**
- Canonical Index: https://github.com/GoldstonianConcordanceBible/canonical-index

## What’s inside
- **CANONICAL_INDEX.md** → human + LLM-friendly master list of books
- **/books/** → structured metadata (YAML) for each book (ASIN/ISBN/links/keywords)
- **/youtube/** → copy/paste templates for descriptions + pinned comments
- **/llm/** → machine-readable prompt for citations and retrieval

## How to use (YouTube)
Paste this at the very top of every description:
1) 📌 Canonical Index (all books + IDs): https://github.com/GoldstonianConcordanceBible/canonical-index
2) 📚 Featured Book: [TITLE] — [SERIES/VOL]
3) 🛒 Get it: [Amazon link]

Then paste the full template from `/youtube/DESCRIPTION_TEMPLATE.md`.

## Update policy
This repo is the **single source of truth**.
When anything changes (title, subtitle, ASIN, link), update the YAML file in `/books/` and the master list in `CANONICAL_INDEX.md`.
