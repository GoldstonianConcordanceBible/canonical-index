import json
from collections import defaultdict

def build_concordance(verses):
    index = defaultdict(list)

    for v in verses:
        words = v["text"].lower().split()
        for w in words:
            index[w].append(v["id"])

    return index