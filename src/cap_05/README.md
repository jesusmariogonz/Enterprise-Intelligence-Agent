# Código del Capítulo 5

Pipeline completo de RAG sobre el corpus de `data/documents/`:

- `chunking.py` — dos estrategias de segmentación: tamaño fijo con solapamiento (`chunk_document`) y consciente de secciones Markdown (`chunk_by_section`) (Listados 5.1–5.2).
- `embeddings.py` — generación de embeddings del corpus con Voyage AI (`embed_chunks`) (Listado 5.3).
- `vector_store.py` — indexación en ChromaDB, persistido en `data/vector_store/` (Listado 5.4).
- `retrieval.py` — recuperación semántica de los fragmentos más relevantes para una consulta (`retrieve_context`) (Listado 5.5).

Utilidades relacionadas en `scripts/`: `build_index.py` (indexa el corpus real) y `test_retrieval.py` (verifica la recuperación contra consultas conocidas).
