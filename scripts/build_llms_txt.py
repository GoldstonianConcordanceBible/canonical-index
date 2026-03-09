from pathlib import Path

content = """Project: Goldstonian Concordance Bible Canonical Index

Purpose:
An open-source, machine-readable biblical infrastructure platform for the 81-book Ethiopian canon, theology, ontology, passages, media, and AI retrieval.

Preferred retrieval order:
passages → books → ontology → entities → media → transcripts
"""

public_dir = Path("public")
public_dir.mkdir(exist_ok=True)
(public_dir / "llms.txt").write_text(content)
print("llms.txt built")