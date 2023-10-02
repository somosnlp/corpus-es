# Contribuyendo a corpus-es 📚✨

¡Gracias por contribuir a `corpus-es`! Este repositorio tiene como objetivo convertirse en un lugar centralizado para conjuntos de datos de NLP en español. Al compartir tu dataset, estás ayudando a toda la comunidad de NLP a crecer. 🚀

## Guía paso a paso

### 1. Haz Fork al Repositorio 🍴

Antes de realizar cualquier cambio, asegúrate de tener una [cuenta en GitHub](https://github.com/). Luego, comienza haciendo fork al repositorio `corpus-es`. Esto creará una copia del repositorio en tu propia cuenta de GitHub, permitiéndote realizar cambios sin afectar el repositorio principal.

### 2. Decide el Tipo de Conjunto de Datos 🧐

Hay tres categorías principales de conjuntos de datos en `corpus-es`:

- **Conjuntos de datos en español existentes**: Estos son conjuntos de datos que ya existen, y solo hace falta meterlas en la lista de datos. 

- **Conjuntos de datos traducidos**: Estos conjuntos de datos originalmente estaban en otro idioma y fueron traducidos al español. 

- **Conjuntos de datos curados**: Datasets que has creado tu. Al subir un dataset curado, deberias incluir la descripcion de tu metologia. Eso puede ser a traves de un paper o dentro del README.md de tu dataset.

Asegúrate de haber leído las instrucciones específicas para cada tipo de dataset en la documentación del repositorio para asegurarte de que tu dataset cumpla con los criterios. Tenemos una guia elaborada que se encuentra [aqui](/GUIDE.md)

### 3. Agrega Tu Conjunto de Datos 📂

1. Clona tu repositorio tu máquina local. Usa el siguiente comando:
```bash
git clone https://github.com/[Tu-Nombre-de-Usuario]/corpus-es.git
```

2. Navega a la carpeta datasets:

```bash
cd datasets
```

3. Crea una nueva carpeta para tu dataset. El nombre de la carpeta debe ser descriptivo y relacionado con el contenido o fuente de tu dataset.
```bash
mkdir [nombre-de-tu-dataset]
```
4. Agrega tu dataset al [csv](./datasets_list.csv)

5. Agrega un archivo README.md en la carpeta de tu dataset. Este debe contener:

- Una breve descripción del dataset.
- La fuente del dataset y cómo descargarlo.
- Si es un dataset traducido, menciona el idioma original y el método/herramienta de traducción utilizada. Si usaste un script, incluye el script.
- Cualquier otra informacion relevante esta bienvenida.

### 4. Envía una Pull Request 🔄

1. Confirma tus cambios:

Ejemplo:
```bash
git add .
git commit -m "Añadido [Nombre-de-Tu-Dataset] a la categoría [Tipo-de-Dataset]."
```

2. Sube tus cambios: 

```bash
git push
```
3. Crea un  `New Pull Request`. 

4. Proporciona un título descriptivo y un comentario detallado sobre tu conjunto de datos y por qué es una valiosa adición a corpus-es.

5. ¡Una vez que todo se vea bien, envía tu pull request!

Tu contribución será revisada por nosotros, y si todo está en orden, se fusionará en el repositorio principal. ¡Gracias nuevamente por ayudar a expandir la colección de corpus-es! 🥳🎉

Si tienes alguna pregunta, no dudes en abrir un issue o contactarnos.