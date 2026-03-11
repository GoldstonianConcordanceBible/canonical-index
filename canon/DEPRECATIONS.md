# Deprecations

## Canon identity deprecations

### Root-level duplicate files
The following pattern is deprecated:
- `canon/<book>.json`

Grouped canonical files must be used instead.

### Example
Deprecated:
- `canon/genesis.json`

Preferred:
- `canon/torah/genesis.json`

## Naming deprecations
Deprecated:
- mixed-case filenames
- inconsistent separator styles
- duplicate canonical slugs across folders
- implicit tradition collapse

Preferred:
- lowercase kebab-case filenames
- one authoritative grouped file per canonical slug
- explicit tradition-aware distinctions

## Canonical distinction deprecations
Never silently merge:
- `1-meqabyan` with `1-maccabees`
- `2-meqabyan` with `2-maccabees`
- `3-meqabyan` with `3-maccabees`

## Compatibility policy
Deprecated files may remain temporarily as forwarding stubs, but must include:
- `deprecated: true`
- `replacement_path`
- `replacement_slug`
- `replacement_id`