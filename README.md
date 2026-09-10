# Enterprise Intelligence Agent (EIA)

Repositorio complementario del libro **"AI Solution Architect: De LLMs y RAG
a Agentes, Orquestación y Sistemas Inteligentes Empresariales"**.

## Qué es este proyecto

Este repositorio acompaña el proyecto transversal del libro: el
**Enterprise Intelligence Agent (EIA)**, un asistente empresarial en Python
que combina:

- **RAG** sobre documentos internos (políticas de una empresa ficticia,
  "EIA Corp").
- **Consultas SQL** sobre datos estructurados (una base de datos
  transaccional ficticia basada en Northwind).
- **Ejecución de herramientas controladas** (tool use / function calling).
- **Gobierno y seguridad** del agente (permisos, auditoría, límites de uso).

El código se construye de forma **incremental, capítulo a capítulo**, a
medida que el libro introduce nuevos conceptos: desde los fundamentos de
LLMs y RAG, hasta agentes, orquestación multiagente y despliegue de
sistemas inteligentes empresariales.

## Estructura del repositorio

```
.
├── src/
│   ├── cap_03/ ... cap_22/   # Código de cada capítulo (cap. 1 y 2 son teóricos, sin código)
├── data/
│   ├── structured/            # northwind.db + su licencia (sistema transaccional de EIA Corp)
│   └── documents/             # Documentos Markdown de políticas internas (corpus de RAG)
├── figures/                   # Diagramas fuente (Graphviz/Python) usados en el libro
├── scripts/                   # Utilidades compartidas entre capítulos (carga de datos, helpers)
├── requirements.txt
├── .env.example
└── LICENSE
```

Cada carpeta `src/cap_XX/` incluye un `README.md` que se irá reemplazando
por el código correspondiente a medida que avance el libro.

> **Nota sobre datos:** a diferencia de otros proyectos Python, `data/` **sí
> se versiona** en este repositorio (no está en `.gitignore`), ya que los
> datos de ejemplo (Northwind y las políticas de EIA Corp) son parte
> integral de los ejercicios del libro.

## Instalación

```bash
# 1. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp .env.example .env
# Editar .env y completar ANTHROPIC_API_KEY con tu clave real
```

Las dependencias del `requirements.txt` se irán ampliando capítulo a
capítulo (por ejemplo: un framework de RAG en el Capítulo 5, FastAPI en el
Capítulo 18, etc.).

## Licencias

- El **código** de este repositorio se distribuye bajo licencia MIT (ver
  [`LICENSE`](./LICENSE)).
- Los **datos de Northwind** (`data/structured/`) se distribuyen bajo su
  propia licencia (ver
  [`data/structured/LICENSE_NORTHWIND.txt`](./data/structured/LICENSE_NORTHWIND.txt)).
