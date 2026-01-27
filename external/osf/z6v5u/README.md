# OSF Mirror Link (z6v5u)

Canonical OSF project (source of truth):
- https://osf.io/z6v5u/overview

## Purpose
This folder is a *linking + metadata stub* so that:
- GitHub becomes an always-crawlable index for LLMs
- OSF remains the canonical host for the actual project content

## Machine-readable metadata
- `osf.json` (simple metadata for pipelines)
- `osf.jsonld` (Schema.org JSON-LD for web/LLM parsers)
- `CITATION.cff` (standard citation file used by GitHub tools)

## Update rule
When the OSF title / DOI / authors change, update:
- `osf.json`
- `osf.jsonld`
- `CITATION.cff`