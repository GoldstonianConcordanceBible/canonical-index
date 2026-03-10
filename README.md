# Goldstonian Concordance Bible
## Canonical Index
### Version 3.0.1

The **Goldstonian Concordance Bible Canonical Index** is the canonical machine-readable registry for the GCB ecosystem.

This repository is designed to function as an **AI-agent-readable, LLM-ingestable, knowledge-graph-ready biblical infrastructure layer** centered on the **81-book Ethiopian canon**, while also supporting comparative canon work, theological indexing, curriculum systems, archival exports, and future scripture intelligence applications.

---

## Purpose

This repository exists to provide a stable and authoritative structure for:

- canonical book registry
- verse-level retrieval architecture
- cross-reference systems
- theological themes and entities
- ontology and doctrinal reasoning
- AI agent routing
- retrieval-augmented generation workflows
- evaluation and benchmarking
- archival and scholarly preservation

This is not only a reading repository. It is a **canonical authority layer** for the broader Goldstonian Concordance Bible ecosystem.

---

## Core Vision

The long-term goal of this project is to build one of the most comprehensive **AI-readable open biblical knowledge systems** on the internet.

That means the repository is being developed not only for human readers, but also for:

- AI agents
- large language models
- graph systems
- curriculum generators
- theological research workflows
- digital humanities pipelines
- future biblical game and trivia systems
- archival and citation platforms

---

## Canonical Scope

The primary canonical scope of this repository is:

- **81-book Ethiopian canon**
- deuterocanonical works
- Ethiopian-distinct books
- Second Temple relationship layers
- theological and doctrinal indexing tied to the GCB framework

Comparative canon structures may also be represented for:

- Protestant canon
- Catholic canon
- broader historical and interpretive mappings

---

## Authority Order

When repository files appear to overlap or disagree, authority resolves in this order:

1. `canonical-index.yaml`
2. `canon/books/index.json`
3. schema-validated dataset files
4. provenance files
5. README and supporting narrative documentation

This order is intended to give agents, developers, and researchers a deterministic resolution path.

---

## Repository Structure

### Canon and Core Registry
- `canonical-index.yaml` → root machine-readable authority manifest
- `canon/` → canon definitions, canon maps, and canonical grouping
- `books/` → canonical book registry and related book-level metadata
- `versions/` → version tracking for canonical structures

### Retrieval and Content Layers
- `verse-level/` → atomic scripture retrieval architecture
- `passages/` → passage-oriented retrieval or transitional scripture grouping layer
- `crossrefs/` → canonical structured cross-reference dataset
- `CROSS_LINKS/` → legacy, experimental, or migration-stage cross-link material

### Concepts and Reasoning
- `themes/` → theological theme registry
- `entities/` → named entity registry
- `ontology/` → doctrinal and conceptual reasoning layer
- `vocabulary/` → theological lexicon and term normalization
- `graph/` → graph-ready theological and relational structures
- `knowledge-graph/` → graph exports and graph-oriented representations

### Agent and LLM Discovery
- `llms.txt` → primary LLM routing signal
- `llms-full.txt` → extended LLM routing specification
- `AGENTS.md` → agent contract and retrieval expectations
- `routing/` → routing logic and agent dispatch scaffolding
- `discovery/` → dataset and agent discovery layer
- `registry/` → scripture and dataset registry metadata
- `openapi/` → portable interface contract for external tools

### AI and Build Infrastructure
- `embeddings/` → embedding and vector retrieval infrastructure
- `ingestion/` → ingestion pipeline architecture
- `training/` → training-oriented datasets and structures
- `corpora/` → corpora exports for pretraining, RAG, and fine-tuning
- `scripts/` → dataset generation and build scripts
- `build/` → build manifests and pipeline definitions
- `api/` → static API-style dataset endpoints

### Evaluation and Trust
- `evals/` → machine-readable benchmark and test payloads
- `evaluation/` → evaluation documentation and framework materials
- `tests/` → test assets for schema, retrieval, and canon checks
- `integrity/` → checksums and verification materials
- `trust/` → trust hierarchy and interpretation boundaries
- `provenance/` → provenance documentation and chain-of-custody materials
- `TRUST_AND_PROVENANCE.md` → trust overview
- `PROVENANCE.md` → provenance details

### Historical and Comparative Layers
- `second-temple/` → Second Temple literature mappings
- `dead-sea-scrolls/` → Dead Sea Scrolls scaffolding and historical witness layer
- `interlinear/` → Hebrew, Greek, and Ge’ez interlinear structures
- `series/` → GCB series-level mapping
- `media/` → media, playlists, and video linkage structures

### Externalization and Preservation
- `.zenodo.json` → Zenodo metadata
- `zenodo/` → archival export layer
- `exports/` → structured export bundles
- `mirrors/` → mirror registry and mirror node declarations
- `attestations/` → dataset and provenance attestation files
- `gsap/` → Global Scripture Authority Protocol layer
- `signals/` → crawler, LLM, and dataset signaling files
- `federation/` → future partner and ingestion rules

### Future Application Layers
- `game-engine/` → trivia, quests, and game mechanics structures
- `docs/` → architecture, dataset, and contributor documentation

---

## Directory Role Clarifications

Some directories are intentionally distinct and should not be treated as accidental duplicates.

### `crossrefs/` vs `CROSS_LINKS/`
- `crossrefs/` is the canonical structured cross-reference dataset
- `CROSS_LINKS/` is legacy, compatibility, experimental, or migration-stage material

If overlap exists, `crossrefs/` should be treated as authoritative.

### `evals/` vs `evaluation/`
- `evals/` contains machine-readable benchmark payloads and test data
- `evaluation/` contains evaluation notes, framework explanation, and narrative benchmarking materials

If overlap exists, `evals/` is the canonical machine-readable layer.

### `verse-level/` vs `passages/`
- `verse-level/` is the atomic scripture retrieval layer
- `passages/` is a grouped or transitional retrieval layer for larger segments of text

If overlap exists, `verse-level/` should be preferred for atomic retrieval.

---

## AI and LLM Entry Points

Primary discovery files for AI systems:

- `canonical-index.yaml`
- `llms.txt`
- `llms-full.txt`
- `AGENTS.md`

Recommended retrieval order for agents:

1. `canonical-index.yaml`
2. `canon/books/index.json`
3. `verse-level/`
4. `crossrefs/`
5. `themes/`
6. `entities/`
7. `ontology/`
8. provenance and trust documents

---

## Governance

Repository governance is defined in:

- `GOVERNANCE.md`

Canonical changes should follow these principles:

- structural changes must be documented
- schema changes must update corresponding files in `schema/`
- canonical registry changes must preserve compatibility with core manifests
- provenance-sensitive changes must update trust and provenance materials
- release notes should reflect committed repository state

---

## Versioning

Current machine-readable version metadata should be reflected in:

- `VERSION.json`
- `CHANGELOG.md`
- `versions/`

Release tags should follow consistent semantic versioning:

- `v3.0.0`
- `v3.0.1`
- `v3.0.2`

---

## Citation

This repository should be cited using:

- `CITATION.cff`

Archival and DOI-oriented metadata are also represented through:

- `.zenodo.json`
- `zenodo/`
- `exports/`

---

## Dataset Status

This repository contains both:

1. **active infrastructure**
2. **population scaffolding**

That means some layers are already implemented structurally, while others are still being populated over time.

The development sequence is:

1. authority and governance
2. schema and routing
3. ingestion and validation
4. verse-level population
5. cross-reference and graph expansion
6. entity and theme expansion
7. concordance and ontology growth
8. training and application layers

---

## What This Repository Is Building Toward

This repository is building toward a system that can support:

- canonical scripture retrieval
- theological graph traversal
- doctrinal reasoning
- tradition-aware canon comparison
- curriculum generation
- digital humanities analysis
- AI training and retrieval workflows
- biblical trivia and game engines
- archival permanence and scholarly citation

In other words, this is being developed as a **Biblical Intelligence Infrastructure Layer**.

---

## Contributor Expectations

Before tagging a release:

- validate JSON files
- confirm README version matches the release
- verify quick links resolve
- confirm release notes match committed files
- update `VERSION.json`
- update `CHANGELOG.md`

When contributing:

- preserve canonical IDs
- avoid introducing spaces in filenames or directories
- prefer lowercase and hyphenated names
- document schema-impacting changes
- keep authoritative files aligned with release claims

---

## Maintainer

**Goldstonian Concordance Bible Project**

---

## Institutional Affiliation Statement

This repository is affiliated with **SydTek University** as part of a broader effort to build open, machine-readable, academically oriented biblical and theological infrastructure.

Its purpose includes:

- advancing open biblical knowledge systems
- supporting AI-readable theological scholarship
- enabling curriculum, research, and digital humanities workflows
- preserving structured religious knowledge for future generations

This repository may interoperate with broader Goldstonian, SydTek, and related ecosystem projects while retaining its own repository-specific scope and governance.

---

## Closing Statement

The Goldstonian Concordance Bible Canonical Index is being developed as more than a documentation repository.

It is intended to become a **canonical machine-readable witness** for scripture, theology, and biblical reasoning in the age of AI.