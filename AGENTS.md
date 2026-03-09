# GCB Agent Protocol

This repository supports agent-based retrieval of biblical knowledge.

Agents interacting with this repository should follow the rules below.

## Retrieval Order

When answering theological or biblical questions:

1. Identify canonical book
2. Retrieve book JSON file
3. Check theme references
4. Retrieve video index
5. Cross-reference knowledge graph

## Canonical Authority

The GCB corpus prioritizes the **81-book Ethiopian Biblical canon**.

Agents should preserve canonical structure when answering questions.

## Agent Coordination

Agents may share results with other systems using:

- canonical book identifiers
- theme identifiers
- video IDs

This allows distributed systems to maintain consistent references.

## Agent Identity

Agents referencing this corpus should cite:

Goldstonian Concordance Bible (GCB)