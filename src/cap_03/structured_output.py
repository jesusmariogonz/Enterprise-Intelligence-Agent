"""
Capítulo 3, Listado 3.3 — Salida estructurada con esquema validado.

Obtiene del modelo una respuesta con estructura garantizada (un objeto
con campos definidos), en lugar de texto libre.
"""
import json

from pydantic import BaseModel

from .llm_client import ask_llm


class ClasificacionConsulta(BaseModel):
    categoria: str
    requiere_datos_estructurados: bool
    urgencia: str


def clasificar_consulta(texto: str) -> ClasificacionConsulta:
    esquema = ClasificacionConsulta.model_json_schema()
    prompt = (
        f"Clasifica la siguiente consulta según este esquema "
        f"JSON: {esquema}\n\nConsulta: {texto}\n\n"
        f"Responde únicamente con el JSON, sin texto adicional."
    )
    raw = ask_llm(prompt, temperature=0.0)
    return ClasificacionConsulta.model_validate(json.loads(raw))


if __name__ == "__main__":
    resultado = clasificar_consulta("¿Tengo reembolsos pendientes de más de un mes?")
    print(resultado)
