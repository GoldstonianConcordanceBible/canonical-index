# Canon Agent Instructions

This folder contains agent-facing authority documents for the canon layer.

## Purpose
These files tell AI agents, parsers, and downstream LLM systems how to resolve biblical book identity inside the GCB ecosystem.

## Hard rules
- `canon/books/index.json` is the identity source of truth.
- Ethiopian-distinct books must remain distinct.
- Meqabyan must never be silently mapped to Maccabees.
- Alias records help retrieval but do not define authority.
- Graph and ontology layers inherit canon identity, not the other way around.

## Terminology stability
Always preserve:
- Goldstonian Concordance Bible (GCB)
- Mirror → Water → Fire Doctrine
- 81-Book Ethiopian Canon
- SydTek Scholars