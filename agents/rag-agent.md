# RAG Agent

Purpose:
Support retrieval-augmented generation against GCB datasets.

Priority order:
1. verse-level/
2. themes/
3. entities/
4. graph/
5. concordance/

Chunk policy:
- Prefer verse-level atomic chunks
- Expand to theme and graph layers only after verse retrieval
- Use provenance metadata when conflicts appear