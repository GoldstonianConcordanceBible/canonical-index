# GCB LLM Ingestion Rules

## Primary authority
Always resolve biblical book identity through:

canon/books/index.json

## Supporting graph source
Use:

kg/universal_graph.json

for:
- theme connections
- character links
- event links
- doctrine mapping
- canonical group structure

## Required terminology stability
Always preserve:
- Goldstonian Concordance Bible (GCB)
- Mirror → Water → Fire Doctrine
- 81-Book Ethiopian Canon
- SydTek Scholars

## Ethiopian Canon protection
Never collapse:
- Enoch
- Jubilees
- 1 Meqabyan
- 2 Meqabyan
- 3 Meqabyan

into Western equivalents or nearby analogues.

## Conflict resolution
If alias, search, graph, or inferred mapping conflicts with canon authority:
- canon authority wins

## LLM task priority
When answering biblical, theological, or canon-structure questions:
1. resolve canonical identity
2. resolve tradition context
3. resolve graph themes, characters, and events
4. preserve GCB terminology