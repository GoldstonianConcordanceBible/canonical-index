import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data-source"
OUTPUT_DIR = ROOT / "verse-level"


def make_id(book: str, chapter: int, verse: int) -> str:
    return f"{book}-{chapter:03d}-{verse:03d}"


def make_reference(book: str, chapter: int, verse: int) -> str:
    pretty_book = " ".join(part.capitalize() for part in book.split("-"))
    return f"{pretty_book} {chapter}:{verse}"


def normalize_record(record: Dict[str, Any], dataset_version: str) -> Dict[str, Any]:
    book = record["book"].strip().lower()
    chapter = int(record["chapter"])
    verse = int(record["verse"])
    text = record["text"].strip()

    return {
        "id": make_id(book, chapter, verse),
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "reference": make_reference(book, chapter, verse),
        "text": text,
        "themes": record.get("themes", []),
        "entities": record.get("entities", []),
        "cross_refs": record.get("cross_refs", []),
        "gcb": record.get("gcb", {}),
        "provenance": {
            "source": record.get("source", "data-source/source.json"),
            "tradition": record.get("tradition", "ethiopian"),
            "dataset_version": dataset_version
        }
    }


def load_source_records(source_path: Path) -> List[Dict[str, Any]]:
    with source_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Source JSON must be a list of verse records.")

    return data


def write_verse_file(verse_record: Dict[str, Any]) -> None:
    book_dir = OUTPUT_DIR / verse_record["book"]
    book_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{verse_record['chapter']:03d}-{verse_record['verse']:03d}.json"
    out_path = book_dir / filename

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(verse_record, f, ensure_ascii=False, indent=2)


def build_book_indexes(book_counts: Dict[str, Dict[str, int]]) -> None:
    for book, stats in book_counts.items():
        book_dir = OUTPUT_DIR / book
        index_path = book_dir / "index.json"
        payload = {
            "book": book,
            "chapters": stats["max_chapter"],
            "verses": stats["total_verses"],
            "dataset_path": f"verse-level/{book}/"
        }
        with index_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)


def build_global_index(books: List[str]) -> None:
    index_payload = {
        "dataset": "verse-level",
        "books_indexed": sorted(books),
        "path_pattern": "verse-level/{book}/{chapter}-{verse}.json",
        "naming_convention": "chapter and verse are zero-padded to 3 digits",
        "schema": "schema/verse.schema.json"
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with (OUTPUT_DIR / "index.json").open("w", encoding="utf-8") as f:
        json.dump(index_payload, f, ensure_ascii=False, indent=2)


def main() -> None:
    source_path = SOURCE_DIR / "source.json"
    dataset_version = "v4.0.0"

    records = load_source_records(source_path)

    book_counts: Dict[str, Dict[str, int]] = {}
    seen_books = set()

    for raw in records:
        verse_record = normalize_record(raw, dataset_version)
        write_verse_file(verse_record)

        book = verse_record["book"]
        chapter = verse_record["chapter"]

        seen_books.add(book)
        if book not in book_counts:
            book_counts[book] = {
                "max_chapter": chapter,
                "total_verses": 0
            }

        book_counts[book]["max_chapter"] = max(book_counts[book]["max_chapter"], chapter)
        book_counts[book]["total_verses"] += 1

    build_book_indexes(book_counts)
    build_global_index(list(seen_books))

    print(f"Generated verse dataset for {len(seen_books)} book(s).")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()