import json
from pathlib import Path

root = Path(".")
output = {"books": [], "themes": [], "entities": []}

for path in root.glob("canon/**/*.json"):
    data = json.loads(path.read_text())
    output["books"].append({
        "title": data.get("book", ""),
        "slug": path.stem,
        "path": str(path),
        "summary": data.get("summary", ""),
        "themes": data.get("major_themes", [])
    })

public_dir = root / "public"
public_dir.mkdir(exist_ok=True)

(public_dir / "search-index.json").write_text(json.dumps(output, indent=2))
print("search-index.json built")