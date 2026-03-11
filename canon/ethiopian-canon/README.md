# Ethiopian Canon Additions

This folder contains book-level canonical records for texts that are specific to or distinctively preserved within the 81-Book Ethiopian Canon tradition.

## Purpose
These records help the Goldstonian Concordance Bible canonical-index distinguish:
- books shared across multiple traditions
- books present in the Ethiopian canon but absent from Protestant canons
- books whose Ethiopian forms differ materially from similarly named books in other traditions

## Current scope
Included here:
- Enoch
- Jubilees
- 1 Meqabyan
- 2 Meqabyan
- 3 Meqabyan

## Canon policy
These files should be treated as:
- canonical in the Ethiopian tradition
- first-class records in the GCB canonical system
- distinct from similarly named books in Catholic or Protestant mappings where applicable

## Naming rule
Use lowercase kebab-case filenames.

Examples:
- `enoch.json`
- `jubilees.json`
- `1-meqabyan.json`

## Required fields
Each book file in this folder should include:
- `id`
- `slug`
- `title`
- `canon_group`
- `traditions`
- `canonical_status`
- `distinctives`
- `related_books`
- `notes`

## Distinction policy
The Meqabyan books are **not** the same as 1–3 Maccabees and must never be silently merged in maps, aliases, or graph references.

## Future expansion
This folder may later include:
- richer metadata
- chapter/section scaffolds
- doctrine links
- graph node mappings
- video/playlist bindings

