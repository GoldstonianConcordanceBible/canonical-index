# Canon Normalization Plan

## Objective
Normalize the canon folder so that:
- each canonical book has one authoritative grouped file
- each canonical slug exists once in the authority registry
- root-level duplicates are deprecated
- downstream graph, ontology, search, and agent systems can resolve books deterministically

## Authority model
1. `canon/books/index.json` = identity authority
2. grouped canonical book files = content authority
3. alias files = discovery layer only
4. deprecated root files = temporary compatibility layer only

## Immediate normalization targets
- remove root-level ambiguity such as `canon/genesis.json`
- align file naming to lowercase kebab-case
- preserve Ethiopian-distinct identity
- prevent Meqabyan/Maccabees drift

## Folder role definitions
- `canon/torah/` and grouped folders: authoritative book content
- `canon/books/`: registry and schema
- `canon/aliases/`: alias resolution only
- `canon/graph/`: canonical graph bindings
- `canon/ontology/`: canonical concept layer
- `canon/search/`: retrieval layer
- `canon/agents/`: agent-facing authority instructions

## Completion condition
Normalization is complete when:
- no root-level canonical duplicates remain active
- all grouped book files follow one naming convention
- registry paths resolve cleanly
- all counts match across canon control files