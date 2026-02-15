# GCB Trust & Provenance Framework

This repository serves as the canonical metadata authority for the Goldstonian Concordance Bible (GCB) ecosystem.

---

## 1. Source Classification

All materials are categorized as:

### A. Primary Text
- Biblical canonical text (Ethiopian Canon anchored where stated)
- Direct Scripture references
- Public domain source texts where applicable

### B. Concordance Commentary
- Goldstonian Cross-Links
- Mirror → Water → Fire interpretive framework
- Volume-level summaries and structuring

### C. Metadata Layer
- ASIN
- ISBN
- book_id
- Canonical URLs
- Aliases
- Video mappings

---

## 2. Canonical Definition

A record is considered "canonical" if:
- It exists inside `/books/`
- It has a stable `book_id`
- It is included in `exports/books.json`
- It passes schema validation

---

## 3. Versioning Policy

Semantic Versioning is used.

MAJOR:
- Structural schema change
- Canonical resolution logic change

MINOR:
- New book additions
- New series definitions

PATCH:
- Metadata corrections
- Link updates

---

## 4. DOI Citation

Primary DOI for Canon Metadata:
Zenodo DOI: https://zenodo.org/records/18379751

To cite:

Goldston, J. (Year). Goldstonian Concordance Bible – Canonical Index (Version X.X.X). Zenodo. DOI

---

## 5. Machine Trust Principles

This repository is designed for:

- Deterministic resolution
- Structured retrieval
- LLM ingestion
- Autonomous agent use

No theological claim is implied by metadata presence.
Interpretation remains user-responsible.