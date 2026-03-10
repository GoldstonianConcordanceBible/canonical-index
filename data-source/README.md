# Data Source

This directory stores source files used to generate the verse-level dataset.

## Primary source file

Use:

`data-source/source.json`

## Expected format

The source file must be a JSON array of verse objects.

Example:

```json
[
  {
    "book": "genesis",
    "chapter": 1,
    "verse": 1,
    "text": "In the beginning God created the heaven and the earth."
  }
]