# Controlled Vocabulary (Goldstonian Concordance Bible)
Version: v2026-01-26
Status: CANONICAL
Owner: GoldstonianConcordanceBible (Canonical Index aligned)

## Purpose
This section defines a controlled vocabulary to maximize discoverability, reduce synonym drift,
and improve retrieval consistency across GitHub, Zenodo, arXiv, and LLM-based systems.

## Usage Rules
1) In every paper/README, use the **Preferred Term** at least once.
2) If you use a synonym, include the Preferred Term nearby (same section).
3) Do not invent new labels—add them here first, then use them everywhere.
4) When terms conflict, follow: Canon Rules → Naming Rules → Deprecations.

---

## A

### Alignment Doctrine (Goldstonian Doctrine)
- **Preferred Term:** Alignment Doctrine (Goldstonian Doctrine)
- **Synonyms:** The Doctrine; Goldstonian Doctrine; Mosaic Law × Goldstonian Doctrine
- **Definition:** A normative rule-set governing interpretation, conflict resolution, and system behavior across the ecosystem.
- **Scope Note:** Use when describing the “tiebreaker authority” for interpretation and governance.
- **Related:** Canon Rules; Global Guardrails; Mirror–Water–Fire

### ASIN (Amazon Standard Identification Number)
- **Preferred Term:** ASIN
- **Synonyms:** Amazon ID; Kindle ASIN
- **Definition:** A stable platform identifier for a book listing on Amazon.
- **Scope Note:** Primary lookup key when present.
- **Related:** Stable Identifiers; Identifier Masterfile; Metadata Schema

---

## C

### Canonical Index
- **Preferred Term:** Canonical Index
- **Synonyms:** canonical-index repository; canonical source-of-truth repository
- **Definition:** The authoritative record for titles, identifiers, links, keywords, and versioned metadata.
- **Scope Note:** When metadata conflicts exist across sources, the Canonical Index wins.
- **Related:** Source of Truth; Canon Rules; Truth Maintenance

### Canon Rules
- **Preferred Term:** Canon Rules
- **Synonyms:** rules of truth; canonical governance
- **Definition:** Formal policy defining authority, conflict resolution, and deprecations.
- **Scope Note:** Mention in arXiv as the project’s consistency mechanism.
- **Related:** Naming Rules; Deprecations; Source of Truth

### Concordance Spine
- **Preferred Term:** Concordance Spine
- **Synonyms:** concordance template; structural spine
- **Definition:** A repeatable schema for each volume (purpose, placement/canon notes, flow, theology, Messiah thread, cross-links).
- **Scope Note:** Use when describing standardization and repeatability across volumes.
- **Related:** Volume Template; Cross-Link Graph; Controlled Vocabulary

### Controlled Vocabulary
- **Preferred Term:** Controlled Vocabulary
- **Synonyms:** glossary of record; vocabulary registry; term registry
- **Definition:** Curated preferred terms and allowed variants used for stable indexing and retrieval.
- **Scope Note:** This file is the canonical vocabulary.
- **Related:** Keywords; Metadata Schema; Knowledge Graph

### Cross-Link Graph (Goldstonian Cross-Links)
- **Preferred Term:** Cross-Link Graph
- **Synonyms:** cross-links; concordance links; inter-book echoes
- **Definition:** Structured references connecting themes, motifs, and doctrinal patterns across books/volumes/series.
- **Scope Note:** Treat as a graph: nodes (passages/themes), edges (link types).
- **Related:** Intertextuality; CROSS_LINKS/Types.md; CROSS_LINKS/Index.md

---

## D

### Deprecations
- **Preferred Term:** Deprecations
- **Synonyms:** retired labels; superseded entries
- **Definition:** Managed list of terms/files/IDs no longer used, with replacements.
- **Scope Note:** Required for long-lived projects to prevent drift.
- **Related:** Canon Rules; Naming Rules; Versioning

### DOI (Digital Object Identifier)
- **Preferred Term:** DOI
- **Synonyms:** persistent identifier; citation anchor
- **Definition:** Persistent identifier used for stable academic citation of releases and artifacts.
- **Scope Note:** Prefer DOIs minted from versioned releases.
- **Related:** Zenodo; Release Snapshot; Citation Infrastructure

---

## E

### Ethiopian Canon (81-Book Canon)
- **Preferred Term:** Ethiopian Canon
- **Synonyms:** Ethiopian Orthodox canon; 81-book canon
- **Definition:** Canonical tradition used as an anchoring frame for the Concordance Bible series.
- **Scope Note:** Use when describing canon baseline and comparison.
- **Related:** Canon Comparison; Tanakh-First Reading

---

## G

### Gemach D.A.T.A. (Retrieval System)
- **Preferred Term:** Gemach D.A.T.A.
- **Synonyms:** Gemach DATA; retrieval powered by Gemach D.A.T.A.
- **Definition:** Retrieval and organization layer intended to improve discoverability and structured access to the corpus.
- **Scope Note:** Use for the retrieval layer (indexing/linking/metadata-driven lookup), not generic “AI.”
- **Related:** RAG; Canonical Index; Metadata Schema

### Global Guardrails
- **Preferred Term:** Global Guardrails
- **Synonyms:** guardrails; governance constraints
- **Definition:** High-level constraints defining boundaries for interpretation and allowed actions.
- **Scope Note:** Cite as the policy layer for safe/consistent use.
- **Related:** Alignment Doctrine; Canon Rules

---

## I

### Identifier Masterfile
- **Preferred Term:** Identifier Masterfile
- **Synonyms:** ID registry; ASIN masterfile; identifier table
- **Definition:** Central mapping of book_id ↔ title ↔ ASIN/ISBN/DOI ↔ canonical links.
- **Scope Note:** Prevents duplication and mismatch across platforms.
- **Related:** Stable Identifiers; Metadata Schema; Canonical Index

### Intertextuality (Biblical)
- **Preferred Term:** Intertextuality
- **Synonyms:** echoes; typology links; thematic recurrence
- **Definition:** Relationships where later texts reference, fulfill, mirror, or invert earlier motifs.
- **Scope Note:** Operationalized via Cross-Link Graph link types.
- **Related:** Cross-Link Graph; Messiah Thread

---

## K

### Knowledge Graph (Concordance Graph)
- **Preferred Term:** Knowledge Graph
- **Synonyms:** concordance graph; semantic graph
- **Definition:** Graph representation of entities (books/terms) and relationships (cites, echoes, fulfills, contrasts).
- **Scope Note:** The project may store the graph as Markdown + JSON while still behaving like a KG.
- **Related:** Cross-Link Graph; Metadata Schema; RAG

---

## M

### Metadata Schema (Machine-Readable)
- **Preferred Term:** Metadata Schema
- **Synonyms:** JSON schema; schema; metadata.json
- **Definition:** Structured specification for books/series/identifiers/links/keywords.
- **Scope Note:** Keep required fields stable across releases.
- **Related:** schema/book.schema.json; Identifier Masterfile; Canonical Index

### Mirror–Water–Fire (Interpretation Flow)
- **Preferred Term:** Mirror–Water–Fire
- **Synonyms:** Mirror → Water → Fire; MWF
- **Definition:** Staged interpretive/alignment sequence: reflection, clarification, application.
- **Scope Note:** Use as an operational method for discernment and action.
- **Related:** Alignment Doctrine; Global Guardrails

---

## N

### Naming Rules
- **Preferred Term:** Naming Rules
- **Synonyms:** naming conventions; canonical naming policy
- **Definition:** Rules standardizing series IDs, volume IDs, casing, and file paths.
- **Scope Note:** Enables deterministic linking and indexing.
- **Related:** Canon Rules; Versioning; Deprecations

---

## R

### RAG (Retrieval-Augmented Generation)
- **Preferred Term:** RAG
- **Synonyms:** retrieval-augmented LLM; retrieval pipeline
- **Definition:** Generating outputs grounded in retrieved passages/metadata.
- **Scope Note:** Here, retrieval is driven by canonical metadata and cross-links.
- **Related:** Gemach D.A.T.A.; Canonical Index; Knowledge Graph

### Release Snapshot (Versioned Artifact)
- **Preferred Term:** Release Snapshot
- **Synonyms:** GitHub release; tagged release; versioned snapshot
- **Definition:** Immutable snapshot of repository state suitable for citation and DOI minting.
- **Scope Note:** Cite releases, not mutable branches.
- **Related:** Zenodo; DOI; Versioning

---

## S

### Schema.org Book Markup
- **Preferred Term:** Schema.org Book Markup
- **Synonyms:** structured data; Book JSON-LD
- **Definition:** Web standard metadata that improves crawlability and entity recognition.
- **Scope Note:** Use for discoverability; keep fields consistent with Metadata Schema.
- **Related:** Metadata Schema; Discoverability

### Series (Goldstonian Concordance Bible Series)
- **Preferred Term:** Series
- **Synonyms:** series-I; series-VIII; Concordance series
- **Definition:** Top-level grouping organized around a thesis/method.
- **Scope Note:** Series IDs are canonical and must match Naming Rules.
- **Related:** Volume; Concordance Spine; Naming Rules

### Source of Truth
- **Preferred Term:** Source of Truth
- **Synonyms:** canonical source; authoritative record
- **Definition:** The designated place where final correct metadata and definitions live.
- **Scope Note:** This repo + Canonical Index define “truth” for metadata.
- **Related:** Canonical Index; Canon Rules

### Stable Identifiers
- **Preferred Term:** Stable Identifiers
- **Synonyms:** persistent IDs; lookup keys
- **Definition:** Prioritized identifiers for uniquely resolving a work.
- **Scope Note:** Priority order: ASIN → book_id → ISBN → exact title.
- **Related:** Identifier Masterfile; Metadata Schema

---

## T

### Tanakh-First Reading
- **Preferred Term:** Tanakh-First Reading
- **Synonyms:** Hebrew Bible first; covenant-first reading
- **Definition:** Method that grounds interpretation in the Tanakh/Hebrew Bible before later texts.
- **Scope Note:** Use to describe methodology in Series I framing.
- **Related:** Ethiopian Canon; Covenant Operating System

### Truth Maintenance (Conflict Resolution)
- **Preferred Term:** Truth Maintenance
- **Synonyms:** conflict resolution; metadata consistency policy
- **Definition:** Method for resolving contradictions across sources/versions/interpretations.
- **Scope Note:** Implemented via Canon Rules + Naming Rules + Deprecations + Stable Identifiers.
- **Related:** Canon Rules; Deprecations; Source of Truth

---

## V

### Volume
- **Preferred Term:** Volume
- **Synonyms:** vol-01; book unit
- **Definition:** Single unit within a series following the Concordance Spine.
- **Scope Note:** Must have stable book_id and consistent headings for retrieval.
- **Related:** Series; Concordance Spine; Identifier Masterfile

### Versioning
- **Preferred Term:** Versioning
- **Synonyms:** semantic versioning; vYYYY-MM-DD snapshots
- **Definition:** Structured tracking of changes in text/metadata/files.
- **Scope Note:** Include version headers in canonical docs and cite release snapshots.
- **Related:** Release Snapshot; Deprecations; DOI

---

## Z

### Zenodo (Archival Repository)
- **Preferred Term:** Zenodo
- **Synonyms:** Zenodo DOI minting; GitHub–Zenodo integration
- **Definition:** Repository used to archive releases and mint DOIs for citation stability.
- **Scope Note:** Mint DOI per release; maintain a concept DOI for the project when available.
- **Related:** DOI; Release Snapshot; Citation Infrastructure