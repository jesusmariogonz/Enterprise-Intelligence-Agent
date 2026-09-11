"""
Capítulo 5, Listados 5.1 y 5.2 — Segmentación de documentos.

Dos estrategias de chunking: tamaño fijo con solapamiento (5.1), y
consciente de secciones Markdown, con respaldo de tamaño fijo (5.2).
"""
import re
from dataclasses import dataclass


@dataclass
class Chunk:
    id: str
    text: str
    source: str
    start_offset: int


def chunk_document(
    text: str,
    source: str,
    chunk_size: int = 500,
    overlap: int = 80,
) -> list[Chunk]:
    """Segmenta un documento en fragmentos con solapamiento."""
    chunks: list[Chunk] = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        fragment = text[start:end]
        chunk_id = f"{source}_{start}"
        chunks.append(Chunk(chunk_id, fragment, source, start))
        start += chunk_size - overlap
    return chunks


def chunk_by_section(text: str, source: str, max_size: int = 700) -> list[Chunk]:
    """Segmenta por encabezados Markdown; aplica chunk_document
    como respaldo si una sección excede max_size."""
    sections = re.split(r"\n(?=## )", text)
    chunks: list[Chunk] = []
    offset = 0
    for section in sections:
        if len(section) <= max_size:
            chunk_id = f"{source}_{offset}"
            chunks.append(Chunk(chunk_id, section, source, offset))
        else:
            chunks.extend(
                chunk_document(section, source, chunk_size=max_size, overlap=100)
            )
        offset += len(section)
    return chunks
