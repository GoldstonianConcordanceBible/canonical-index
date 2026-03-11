# Canon Books Authority Registry

This folder contains the GCB authority registry for canonical books.

## Purpose
`index.json` is the canonical registry that ties together:
- canon group membership
- file paths
- slug authority
- tradition visibility
- downstream graph and ontology references

## Source of truth
For book identity, prefer:
1. `canon/books/index.json`
2. the individual canonical book JSON file
3. alias maps only for discovery, never for identity

## Critical policy
Do not silently merge:
- Meqabyan with Maccabees
- Ethiopian-distinct books into Protestant or Catholic lists
- variant books without explicit tradition-aware labels

## Downstream consumers
This registry is intended for:
- `canon/graph/`
- `canon/ontology/`
- `canon/search/`
- `canon/agents/`
- LLM ingestion pipelines