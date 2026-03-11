# GCB Knowledge Graph

This folder contains the production knowledge graph layer for the Goldstonian Concordance Bible (GCB).

## Purpose
The knowledge graph translates canonical book identity into machine-readable graph objects for:
- LLM ingestion
- ontology alignment
- search enrichment
- doctrinal cross-linking
- playlist and video mapping
- future agent reasoning

## Identity rule
Canonical identity comes from:
- `canon/books/index.json`

The graph layer may extend metadata, but may not override canonical identity.

## Core folders
- `kg/books/` — book graph nodes
- `kg/edges/` — graph edges
- `kg/themes/` — theme nodes
- `kg/characters/` — character nodes
- `kg/doctrine/` — doctrine nodes
- `kg/events/` — event nodes
- `kg/universal_graph.json` — compiled graph artifact

## Hard rules
- one canonical slug -> one graph book node
- Meqabyan must remain distinct from Maccabees
- Ethiopian distinct books must retain explicit distinction
- graph bindings inherit from canon, not the reverse