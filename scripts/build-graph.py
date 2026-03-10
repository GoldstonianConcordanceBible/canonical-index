import json

def build_edge(source,target,relationship):
    return {
        "source": source,
        "target": target,
        "relationship": relationship
    }

edge = build_edge("genesis-001-001","john-001-001","creation-parallel")

print(json.dumps(edge, indent=2))