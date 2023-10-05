# 📚✨ Contribuir a corpus-es

¡Gracias por contribuir a `corpus-es`! Este repositorio tiene como objetivo convertirse en un lugar centralizado para conjuntos de datos de PLN en español y lenguas cercanas (e.g., catalán, quechua). Al compartir tu dataset, estás ayudando a toda la comunidad de PLN a crecer. 🚀

## Guía paso a paso

### 1. 🍴 Haz fork al repositorio

Antes de realizar cualquier cambio, asegúrate de tener una [cuenta en GitHub](https://github.com/). Luego, comienza haciendo fork al repositorio `corpus-es`. Esto creará una copia del repositorio en tu propia cuenta de GitHub, permitiéndote realizar cambios sin modificar el repositorio principal.

### 2. 🧐 Decide el tipo de corpus que quieres añadir

Puedes aportar cualquier corpus que te parezca interesante para la comunidad siempre y cuando esté relacionado con el español, LATAM o España.

Echa un vistazo a la lista de [issues](https://github.com/somosnlp/corpus-es/issues). Si quieres añadir un corpus que no está en la lista, abre un nuevo issue. Una vez hayas elegido qué corpus vas a añadir, comenta en el issue correspondiente para que todo el mundo sepa que estás trabajando en él y evitar duplicar esfuerzos.

Hay tres tipos de contribuciones a la lista `corpus-es`:

| Tipo de Dataset  | Descripción                                                                                                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Corpus Existente | Conjuntos de datos que ya existen, simplemente hace falta añadirlos a la lista de corpus. Además del enlace, intenta incluir toda la información que encuentres sobre el corpus en el README.md.                                                   |
| Corpus Traducido | Conjuntos de datos originalmente en otro idioma y traducidos al español. Se pueden usar herramientas como Google Translate, DeepL, OpenAI, etc. En la carpeta de [scripts](./scripts/) se pueden encontrar ejemplos de scripts para la traducción. |
| Corpus Original  | Conjuntos de datos creados por ti desde cero. En este caso deberás describir la metodología utilizada y proveer los scripts.                                                                                                                       |

Si has traducido un corpus o creado uno desde cero, únete a https://huggingface.co/hacktoberfest-corpus-es (clic en "request to join this org") y súbelo. También te animamos a subir datasets ya existentes que estén en otras plataformas (siempre y cuando la licencia lo permita!). Para subir un dataset al hub, puedes seguir estas [instrucciones](https://huggingface.co/docs/datasets/create_dataset)

### 3. 📂 Agrega tu corpus al repo

1. Clona tu repositorio en tu máquina local. Usa el siguiente comando:

```bash
git clone https://github.com/<tu_nombre_de_usuario>/corpus-es.git
```

2. Navega a la carpeta datasets:

```bash
cd datasets
```

3. Crea una nueva carpeta para tu dataset. El nombre de la carpeta debe ser el nombre de tu dataset. Si es un dataset original, elige un nombre descriptivo relacionado con el contenido u origen del dataset.

```bash
mkdir <nombre_de_tu_dataset>
```

4. Incluye en la carpeta los scripts de creación, limpieza y/o traducción que hayas utilizado para tu corpus.

5. Agrega un archivo `README.md` en la carpeta con la información sobre tu dataset. Cada README se divide en dos secciones: un encabezado YAML y un cuerpo.

- Copia la [plantilla para el encabezado](./datasets/nuevo_dataset.md) y rellena la información correspondiente
- El equipo de Hugging Face ya ha diseñado unas Dataset Cards muy completas así que vamos a aprovechar su trabajo y utilizar la misma [plantilla para el cuerpo](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md).
- Queremos prestar especial atención a la evaluación de los corpus, la cual se premiará con puntos extra:
  - Calcula la distribución perplejidad del dataset
  - Incluye una descripción del tamaño más específica que "GB" o "número de tokens", por ejemplo, distribución de la longitud de las frases o documentos
  - Evalúa los sesgos en el dataset
  - Cuantos más detalles mejor!

### 4. 📄 Agrega tu corpus a la tabla [datasets.csv](./datasets.csv)

Añade una nueva línea a la tabla y rellena la información correspondiente.

Si usas VS Code, te recomendamos utilizar extensiones como Rainbow CSV o un editor de CSV para facilitar esta tarea.

### 5. 🔄 Envía una Pull Request

1. Confirma tus cambios:

```bash
git add .
git commit -m "añadir <nombre_de_tu_dataset> <existente/traducido/original>."
```

2. Sube tus cambios:

```bash
git push
```

3. Crea una `New Pull Request` con un título descriptivo: **"Añadir corpus existente/traducido/original: NombreDelCorpus"** explicando por qué tu corpus es una valiosa adición a `corpus-es`. ¡Una vez que todo se vea bien, envía tu pull request!

4. Tu contribución será revisada por el equipo, presta atención a posibles comentarios o sugerencias de cambios.

5. Una vez todo esté bien, se fusionará en el repositorio principal. ¡Gracias nuevamente por ayudar a expandir la colección de corpus-es! 🥳🎉

Si tienes alguna pregunta, no dudes en abrir un issue o contactarnos en [Discord](https://discord.com/invite/my8w7JUxZR).
