import json

def build_verse(book, chapter, verse, text):
    return {
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "id": f"{book}-{chapter:03d}-{verse:03d}",
        "text": text
    }

example = build_verse("genesis",1,1,"In the beginning God created the heaven and the earth.")

print(json.dumps(example, indent=2))