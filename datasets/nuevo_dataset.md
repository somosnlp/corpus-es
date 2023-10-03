---
- `name`: 
- `corpus_link`: 
- `languages`: 
- `countries`: 
- `tasks`:
  - language modeling
  - translation
  - summarization
  - classification
  - named entity recognition
  - question answering
  - textual inference
  - paraphrasis
  - other (specify)
- `subtasks`: 
- `domains`: 
  - clinic
  - legal
  - academic or technic
  - literature or music
  - social media or forums
  - news or articles
  - dialogue
  - general
  - other (specify)
- `license_link`: 
- `license_type`: 
- `contributor_name`:
- `contributor_affiliation`:
- `download_script`:
- `creation_script`: 
- `cleaning_script`: 
- `translation_script`:
---

# < Nombre del Dataset >

Descripción...

## Evaluación del dataset

### Distribución de perplejidad

### Evaluación de sesgos

### Other

---

# Cómo rellenar esta plantilla

Si el corpus ya está subido al hub de Hugging Face, puedes reutilizar la misma Dataset Card (README.md) y añadir este encabezado YAML al principio del documento.

A continuación están explicados los campos del encabezado:

- `name`: Acrónimo o nombre del corpus
- `corpus_link`: Enlace al corpus
- `languages`: Idioma(s) presentes en el corpus
- `countries`: País(es) de origen de los datos, también se puede especificar la región
- `tasks`: Una o varias de las siguientes tareas:
  - Modelado de lenguaje
  - Traducción de texto
  - Resumen de texto
  - Clasificación de texto
  - Reconocimiento de entidades nombradas
  - Respuesta a preguntas
  - Inferencia textual
  - Desambiguación de palabras por contexto
  - Paráfrasis
  - Otro (especificar)
- `subtasks`: Por ejemplo, subtareas de "clasificación de texto" pueden ser "análisis de sentimiento" o "detección de discurso de odio"
- `domains`: Uno o varios de los siguientes dominios:
  - Clínico
  - Legal
  - Académico o técnico
  - Literatura o música
  - Redes sociales o foros
  - Noticias o artículos
  - Diálogos
  - General
  - Otro (especificar)
- `license_link`: Enlace a la licencia
- `license_type`: Elegir solo una:
  - commercial
  - non_commercial
- `contributor_name`: (opcional) Tu nombre
- `contributor_affiliation`: (opcional) Tu afiliación
- `download_script`: Enlace al script para descargar el corpus
- `creation_script`: Enlace al script de creación
- `cleaning_script`: Enlace al script de limpieza
- `translation_script`: Enlace al script de traducción
