# Contribuir a corpus-es 📚✨

¡Gracias por contribuir a `corpus-es`! Este repositorio tiene como objetivo convertirse en un lugar centralizado para conjuntos de datos de PLN en español y lenguas cercanas (e.g., catalán, quechua). Al compartir tu dataset, estás ayudando a toda la comunidad de PLN a crecer. 🚀

## Guía paso a paso

### 1. Haz Fork al Repositorio 🍴

Antes de realizar cualquier cambio, asegúrate de tener una [cuenta en GitHub](https://github.com/). Luego, comienza haciendo fork al repositorio `corpus-es`. Esto creará una copia del repositorio en tu propia cuenta de GitHub, permitiéndote realizar cambios sin modificar el repositorio principal.

### 2. Decide el Tipo de Conjunto de Datos 🧐

Hay tres categorías principales de conjuntos de datos en `corpus-es`:

| Tipo de Dataset  | Descripción                                                                                                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Corpus Existente | Conjuntos de datos que ya existen, simplemente hace falta añadirlos a la lista de corpus. Intenta incluir toda la información que encuentres sobre el corpus.                                                                                      |
| Corpus Traducido | Conjuntos de datos originalmente en otro idioma y traducidos al español. Se pueden usar herramientas como Google Translate, DeepL, OpenAI, etc. En la carpeta de [scripts](./scripts/) se pueden encontrar ejemplos de scripts para la traducción. |
| Corpus Original  | Conjuntos de datos creados por ti desde cero. En este caso deberás describir la metodología utilizada y proveer los scripts.                                                                                                                       |

Si has traducido un corpus o creado uno desde cero, súbelo a https://huggingface.co/hacktoberfest-corpus-es. También te animamos a subir datasets ya existentes que estén en otras plataformas (siempre y cuando la licencia lo permita!). Para subir un dataset al hub, puedes seguir estas [instrucciones](https://huggingface.co/docs/datasets/create_dataset)

### 3. Agrega tu Corpus 📂

1. Clona tu repositorio en tu máquina local. Usa el siguiente comando:

```bash
git clone https://github.com/<tu_nombre_de_usuario>/corpus-es.git
```

2. Navega a la carpeta datasets:

```bash
cd datasets
```

3. Crea una nueva carpeta para tu dataset. El nombre de la carpeta debe ser descriptivo y relacionado con el contenido o fuente de tu dataset.

```bash
mkdir <nombre_de_tu_dataset>
```

4. Incluye en la carpeta los scripts de creación, limpieza y/o traducción de tu corpus.

5. Agrega un archivo `README.md` en la carpeta de tu dataset:

- Copia la [plantilla](./datasets/nuevo_dataset.md) y rellena la información
- Incluye una breve descripción del dataset
- La evaluación del dataset se premiará con puntos extra:
  - Calcula la distribución perplejidad del dataset
  - Evalúa los sesgos en el dataset
- Incluye toda la información que consideres relevante

### 4. Agrega tu corpus a la tabla [datasets.csv](./datasets.csv)

Añade una nueva línea a la tabla y rellena la información correspondiente.

Si usas VS Code, te recomendamos utilizar extensiones como Rainbow CSV o un editor de CSV para falicitar esta tarea.

### 5. Envía una Pull Request 🔄

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
