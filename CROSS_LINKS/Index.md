# Cross-Links Index (Goldstonian Concordance Bible)
Status: CANONICAL (scaffold)
Version: v2026-01-26

## Purpose
This index is the entry point to the Cross-Link Graph: a standardized system for connecting
themes, motifs, and doctrinal patterns across series and volumes.

## Files
- `CROSS_LINKS/Types.md` — allowed link types and meanings
- `CROSS_LINKS/Rules.md` — creation rules + quality standards
- `CROSS_LINKS/Index.md` — this table of cross-link sets (human navigable)

## Cross-Link Sets
| Set ID | Title | Scope | Primary Nodes | Status |
|---|---|---|---|---|
| CL-0001 | Covenant Operating System | Series I (vols 01–06) | covenant, law, mercy, holiness | draft |
| CL-0002 | Canon Comparison Anchors | All series | canon lists, placement notes, tradition markers | draft |
| CL-0003 | Messiah Thread Map | All series | prophecy → pattern → fulfillment | draft |
| CL-0004 | Truth Maintenance | Repo-wide | canon rules, naming, deprecations | draft |

## Node/Edge Convention
- Nodes: `NODE:<book_id>:<anchor>`
- Edges: `EDGE:<type>:<from_node> -> <to_node>`
- Every edge must cite a short justification (1–3 sentences) and a retrieval tag list.

Example:
- NODE:series-I-vol-01:purpose-thesis
- EDGE:echoes:NODE:series-I-vol-01:purpose-thesis -> NODE:series-I-vol-02:core-theology