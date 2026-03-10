# Goldstonian Concordance Bible
## Canonical Index
### Version 3.0.1

The canonical machine-readable index for the Goldstonian Concordance Bible (GCB).

This repository is designed for:

- AI agents
- LLM retrieval pipelines
- biblical knowledge graphs
- digital humanities workflows
- curriculum systems
- archival and scholarly citation

It serves as the canonical routing and authority layer for the 81-book Ethiopian canon within the GCB ecosystem.
The canonical machine-readable index for the Goldstonian Concordance Bible (GCB).

Purpose:
Provide the authoritative structured registry for:

• The 81-book Ethiopian biblical canon
• GCB theological frameworks
• AI and LLM agent retrieval
• Knowledge graph construction
• Cross-platform biblical indexing

This repository functions as the **canonical routing layer** for the GCB ecosystem.

It is designed to support:

• AI agents
• Large language models
• researchers
• theological education
• knowledge graph systems
• scripture retrieval pipelines

---

## Canon Scope

The canonical dataset includes:

• 81-book Ethiopian Biblical Canon  
• Deuterocanonical literature  
• Second Temple literature connections  
• GCB theological commentary  
• cross-reference graph  
• verse-level metadata

---

## Directory Roles

The following directories have distinct purposes and should not be treated as duplicates.

### Canonical Retrieval
- `crossrefs/` → canonical structured cross-reference dataset
- `verse-level/` → atomic scripture retrieval layer
- `themes/` → theological theme registry
- `entities/` → named entity registry

### Legacy / Supplemental / Transitional
- `CROSS_LINKS/` → legacy or experimental cross-link materials retained for compatibility or migration support

### Evaluation
- `evals/` → machine-readable benchmark and test payloads
- `evaluation/` → evaluation documentation, notes, or higher-level framework materials

If overlap exists between directories, the structured canonical source should take precedence over legacy or narrative materials.

# CROSS_LINKS

This directory is retained for compatibility, legacy cross-link materials, migration staging, or experimental relationship files.

Canonical cross-reference data should live in:

`crossrefs/`

If duplicate content exists, `crossrefs/` is authoritative.

# evaluation

This directory contains higher-level evaluation framework materials, narrative benchmarking notes, and supporting evaluation documentation.

Machine-readable benchmark payloads and test fixtures should live in:

`evals/`

If a benchmark exists in both places, `evals/` is the canonical machine-readable source.