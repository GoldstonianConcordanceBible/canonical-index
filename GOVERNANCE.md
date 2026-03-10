# Governance

## Purpose

	•	release discipline
	•	authority order
	•	contribution rules

This repository is the canonical machine-readable index for the Goldstonian Concordance Bible (GCB).

Its purpose is to provide a stable, citable, AI-agent-readable authority layer for the 81-book Ethiopian canon and related theological datasets.

## Governance Model

Canonical changes must follow these rules:

1. All structural changes must be documented in `CHANGELOG.md`.
2. All schema-impacting changes must update the relevant files in `schema/`.
3. All canonical registry changes must preserve compatibility with:
   - `canonical-index.yaml`
   - `canon/books/index.json`
   - `ids/`
   - `registry/`
4. Provenance-sensitive updates must be reflected in:
   - `TRUST_AND_PROVENANCE.md`
   - `PROVENANCE.md`

## Release Discipline

Before tagging a release:

- validate JSON files
- confirm README version matches the release
- verify all quick links resolve
- confirm release notes match committed files
- update `VERSION.json`
- update `CHANGELOG.md`

## Authority Order

When files disagree, authority resolves in this order:

1. `canonical-index.yaml`
2. `canon/books/index.json`
3. schema-validated dataset files
4. provenance files
5. README and supporting narrative docs

## Maintainer

Goldstonian Concordance Bible Project