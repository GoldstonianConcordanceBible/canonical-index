# Canonical ID Specification

## Scripture References

All verse identifiers must use:

`book-chapter-verse`

Examples:

- `genesis-001-001`
- `john-003-016`
- `revelation-022-021`

Rules:

- lowercase only
- hyphen-separated
- chapter and verse zero-padded to 3 digits
- canonical book slugs derive from `canon/books/index.json`

## Books

Book identifiers use the canonical slug only.

Examples:

- `genesis`
- `song-of-solomon`
- `1-meqabyan`

## Entities

Entity identifiers use:

`entity-{name}`

Examples:

- `entity-adam`
- `entity-moses`
- `entity-seraphim`

## Themes

Theme identifiers use:

`theme-{name}`

Examples:

- `theme-covenant`
- `theme-kingdom`
- `theme-judgment`