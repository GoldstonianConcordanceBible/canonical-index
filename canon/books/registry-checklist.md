# Registry Checklist

## Required checks
- [ ] Every book in `canon/books/index.json` has a unique slug
- [ ] Every book in `canon/books/index.json` has a unique path
- [ ] Every path points to a grouped canonical file
- [ ] No active root-level duplicate files remain
- [ ] `canon-index.json` group counts match registry counts
- [ ] `canon-map.json` relationships only reference valid slugs
- [ ] Ethiopian-distinct books remain distinct
- [ ] Meqabyan is never aliased to Maccabees

## High-priority manual review
- [ ] confirm actual filenames in `canon/torah/`
- [ ] confirm `Historical_Books` filenames align with registry paths
- [ ] confirm `New_Testament` filenames align with registry paths
- [ ] confirm grouped folder naming remains stable even if folder casing is mixed