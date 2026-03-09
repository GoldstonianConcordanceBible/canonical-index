from pathlib import Path

base = "https://goldstonianconcordancebible.github.io/gcb-canonical-index/"
pages = [
    "",
    "books.html",
    "themes.html",
    "entities.html",
    "passages.html",
    "media.html",
    "benchmarks.html",
    "api.html"
]

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for page in pages:
    xml.append("  <url>")
    xml.append(f"    <loc>{base}{page}</loc>")
    xml.append("  </url>")

xml.append("</urlset>")

public_dir = Path("public")
public_dir.mkdir(exist_ok=True)
(public_dir / "sitemap.xml").write_text("\n".join(xml))
print("sitemap.xml built")