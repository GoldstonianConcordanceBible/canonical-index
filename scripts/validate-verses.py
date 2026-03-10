import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "verse.schema.json"
VERSE_DIR = ROOT / "verse-level"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    files_checked = 0

    for path in VERSE_DIR.rglob("*.json"):
        if path.name == "index.json":
            continue
        data = load_json(path)
        jsonschema.validate(instance=data, schema=schema)
        files_checked += 1

    print(f"Validated {files_checked} verse file(s) successfully.")


if __name__ == "__main__":
    main()