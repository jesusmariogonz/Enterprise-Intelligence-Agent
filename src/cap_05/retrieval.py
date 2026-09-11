"""
Capítulo 5, Listado 5.5 — Recuperación semántica de fragmentos relevantes.
"""
from .embeddings import vo
from .vector_store import collection

MIN_RELEVANCE = 0.65


def retrieve_context(query: str, k: int = 5) -> list[dict]:
    """Recupera los k fragmentos más relevantes para una consulta."""
    query_embedding = vo.embed(
        [query], model="voyage-3", input_type="query"
    ).embeddings[0]
    resultados = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
    )
    relevantes = []
    for doc, meta, dist in zip(
        resultados["documents"][0],
        resultados["metadatas"][0],
        resultados["distances"][0],
    ):
        score = 1 - dist
        if score >= MIN_RELEVANCE:
            relevantes.append({"texto": doc, "fuente": meta["source"], "score": score})
    return relevantes
