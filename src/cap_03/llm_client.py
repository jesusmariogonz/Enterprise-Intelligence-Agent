"""
Capítulo 3, Listado 3.2 — Primera llamada al modelo del EIA.

Función base y reutilizable para enviar un mensaje al modelo y recibir
una respuesta de texto, controlando explícitamente la temperatura.
"""
import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def ask_llm(prompt: str, temperature: float = 0.2) -> str:
    """Envía un prompt al modelo y devuelve el texto de la respuesta."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


if __name__ == "__main__":
    print(ask_llm("Resume en una frase qué es RAG."))
