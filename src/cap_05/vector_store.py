"""
Capítulo 5, Listado 5.4 — Indexación en el vector store (ChromaDB).
"""
import chromadb

from .chunking import Chunk

client_db = chromadb.PersistentClient(path="./data/vector_store")
collection = client_db.get_or_create_collection("eia_corp_docs")


def index_chunks(chunks: list[Chunk], embeddings: list[list[float]]) -> None:
    """Indexa los chunks en el vector store, con sus metadatos."""
    collection.add(
        ids=[c.id for c in chunks],
        embeddings=embeddings,
        documents=[c.text for c in chunks],
        metadatas=[{"source": c.source, "offset": c.start_offset} for c in chunks],
    )
