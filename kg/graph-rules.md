# GCB Knowledge Graph Expansion Rules

## Canon authority
All books must inherit identity from:

canon/books/index.json

Graph nodes may extend metadata but may never override canonical identity.

## Doctrine alignment
Every book node must connect to:
- doctrine.mirror
- doctrine.water
- doctrine.fire

## Theme mapping
Books should connect to at least:
- 3 thematic nodes
- 1 canonical group

## Character mapping
Priority books should connect to at least:
- 1 major character
- 1 event where applicable

## Edge integrity
Edges must remain:
- directional
- non-duplicated
- canonical-order aware

## Ethiopian Canon protection
The following books must remain distinct:
- 1 Meqabyan
- 2 Meqabyan
- 3 Meqabyan
- Jubilees
- Enoch

These must never be merged with western canon equivalents.