"""
Script de utilidad: indexa el corpus real de documentos de EIA Corp
(data/documents/) usando el pipeline del Capítulo 5.

Uso:
    python scripts/build_index.py

Requiere las variables de entorno ANTHROPIC_API_KEY y VOYAGE_API_KEY
configuradas en .env (ver .env.example).
"""
import glob
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.cap_05.chunking import chunk_by_section
from src.cap_05.embeddings import embed_chunks
from src.cap_05.vector_store import index_chunks

DOCS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "documents")


def main():
    doc_files = sorted(glob.glob(os.path.join(DOCS_PATH, "*.md")))
    doc_files = [f for f in doc_files if os.path.basename(f) != "README.md"]

    print(f"Documentos encontrados: {len(doc_files)}")
    total_chunks = 0
    for path in doc_files:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        source = os.path.basename(path)
        chunks = chunk_by_section(text, source)
        embeddings = embed_chunks(chunks)
        index_chunks(chunks, embeddings)
        total_chunks += len(chunks)
        print(f"  - {source}: {len(chunks)} chunks indexados")

    print(f"\nTotal de chunks indexados: {total_chunks}")
    print("Índice guardado en ./data/vector_store")


if __name__ == "__main__":
    main()
