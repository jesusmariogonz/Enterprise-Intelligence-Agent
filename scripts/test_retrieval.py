"""
Ejercicio de cierre del Capítulo 5: verifica que retrieve_context()
recupere el documento correcto para consultas conocidas.

Requiere haber ejecutado antes scripts/build_index.py, y tener
configuradas ANTHROPIC_API_KEY y VOYAGE_API_KEY en .env.

Uso:
    python scripts/test_retrieval.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.cap_05.retrieval import retrieve_context

CONSULTAS_DE_PRUEBA = [
    ("cuántos días de anticipación necesito para pedir vacaciones", "politica_vacaciones.md"),
    ("reembolso pendiente de más de 30 días", "politica_reembolsos.md"),
    ("puede un agente de IA acceder a información confidencial", "politica_seguridad_informacion.md"),
]


def main():
    aciertos = 0
    for query, doc_esperado in CONSULTAS_DE_PRUEBA:
        resultados = retrieve_context(query, k=2)
        fuentes = [r["fuente"] for r in resultados]
        acierto = doc_esperado in fuentes
        aciertos += acierto
        estado = "OK" if acierto else "FALLÓ"
        print(f"[{estado}] \"{query}\"")
        print(f"       esperado: {doc_esperado} | recuperado: {fuentes}")

    print(f"\n{aciertos}/{len(CONSULTAS_DE_PRUEBA)} consultas recuperaron el documento correcto.")


if __name__ == "__main__":
    main()
