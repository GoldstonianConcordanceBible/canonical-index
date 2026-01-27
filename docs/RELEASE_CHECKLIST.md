# Release Checklist (canonical-index)

1. Update exports (JSON/YAML/CSV) and validate schema locally.
2. Update CHANGELOG.md with what changed.
3. Bump version references in README if present.
4. Ensure `main` is clean and all PRs are merged.
5. Create signed tag: `vX.Y.Z`
6. Push tag to GitHub.
7. Create GitHub Release from the tag:
   - Title: `vX.Y.Z — Canonical Index`
   - Notes: paste changelog section
8. Verify release commit shows "Verified".
9. (Optional) Update Zenodo / DOI integration if you use it.
