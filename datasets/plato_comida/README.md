# Platos de comida
## Descripción
El siguiente dataset son imagenes con platos de comidas y su titulo. El dataset se creó haciendo scrapy a la siguiente página web <a href="https://www.recetasgratis.net/">Recetas gratis</a>, la metodología es la siguiente:
1. Se obtiene el link de la página principal de la categoría de comida.
2. Se obtiene el link de la página de cada receta.
3. Se obtiene el link de la imagen de la receta.
4. Se obtiene el titulo de la receta.
## Imagenes
Las imagenes tienen un tamaño de 300x300 pixeles y se encuentran en formato jpg.
## Metadatos
Los metadatos que se encuentran en el dataset son los siguientes:
+ **prompt**: Titulo de la receta.
+ **source**: path de la imagen.
+ **uuid**: Identificador único de la imagen.
  
Nota 1: El dataset se encuentra en formato csv.
Nota 2: El nombre de las imagenes tambien va el titulo

## Directorio
```bash
|-- README.md - Este archivo
|-- dataset.csv - Dataset
|-- images - Imagenes
|-- src - Código fuente, en especial el script de scrapy
```
