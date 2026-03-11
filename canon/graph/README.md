# Canon Graph Bindings

This folder links canonical identity to graph-ready node references.

## Purpose
The graph layer must not invent book identity. It inherits identity from:
- `canon/books/index.json`

## Binding policy
- one canonical slug -> one graph node
- one canonical book id -> one graph identity
- graph nodes may extend metadata, but not override canonical identity

## Downstream target
Primary downstream output:
- `kg/books/*.json`
- `kg/edges/*.json`
- `kg/universal_graph.json`