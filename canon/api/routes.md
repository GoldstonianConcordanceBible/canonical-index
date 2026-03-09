# GCB API Routes

## GET /books
Returns all canonical books with metadata.

## GET /books/{slug}
Returns a single canonical book entry.

## GET /themes/{slug}
Returns a theological theme object.

## GET /entities/{slug}
Returns a person, being, place, or doctrine entity.

## POST /search
Performs lexical + semantic search over the corpus.

## POST /ask
Runs retrieval pipeline and returns:
- top sources
- suggested answer skeleton
- related books
- related themes
- graph neighbors

## GET /stats
Returns corpus statistics and completion metrics.