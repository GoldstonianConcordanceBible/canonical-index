import json
from pathlib import Path

errors = []

for path in Path(".").glob("**/*.json"):
    try:
        json.loads(path.read_text())
    except Exception as e:
        errors.append(f"{path}: {e}")

if errors:
    print("Validation failed:")
    for err in errors:
        print(err)
    raise SystemExit(1)

print("Corpus validation passed")