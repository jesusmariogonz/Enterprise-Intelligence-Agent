"""
Capítulo 5, Listado 5.3 — Generación de embeddings para el corpus.

Usa Voyage AI (socio de embeddings recomendado por Anthropic).
Requiere la variable de entorno VOYAGE_API_KEY.
"""
import os

import voyageai

from .chunking import Chunk

vo = voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


def embed_chunks(chunks: list[Chunk]) -> list[list[float]]:
    """Genera embeddings en lote para una lista de chunks."""
    textos = [c.text for c in chunks]
    resultado = vo.embed(
        textos,
        model="voyage-3",
        input_type="document",
    )
    return resultado.embeddings
