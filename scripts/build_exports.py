import json
from pathlib import Path

exports = Path("exports")
exports.mkdir(exist_ok=True)

lite = {
    "bundle": "lite",
    "status": "generated"
}

full = {
    "bundle": "full",
    "status": "generated"
}

rag = {
    "bundle": "rag",
    "status": "generated"
}

(exports / "bundle-lite.json").write_text(json.dumps(lite, indent=2))
(exports / "bundle-full.json").write_text(json.dumps(full, indent=2))
(exports / "bundle-rag.json").write_text(json.dumps(rag, indent=2))

print("export bundles built")