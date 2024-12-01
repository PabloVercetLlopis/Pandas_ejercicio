# Pandas_ejercicio
# Ejercicio de Análisis Avanzado de Datos con Pandas en Python

Este repositorio contiene una serie de ejercicios prácticos diseñados para trabajar con la librería **Pandas** en Python, con el objetivo de analizar datos de películas utilizando dos archivos CSV: **`imdb_titulos.csv`** y **`imdb_elenco.csv`**.

## Requisitos

Para ejecutar este proyecto, necesitarás tener **Python 3.8 o superior** instalado y las siguientes librerías:

- pandas
- matplotlib

## Archivos
imdb_titulos.csv: Contiene información sobre los títulos de películas, incluyendo el año de lanzamiento y otros detalles.

imdb_elenco.csv: Contiene información sobre los elencos de las películas, incluyendo los actores, roles y años de participación.
                El archivo CSV necesario para este proyecto es demasiado grande para ser subido directamente al repositorio. Puedes descargarlo desde el siguiente enlace:

- **[imdb_elenco.csv (Dropbox)](https://www.dropbox.com/scl/fi/4tq8nc5jwld02k0r7kw7x/imdb_elenco.zip?rlkey=4g8vb59fxuhevy5g5sus8utfe&st=60fzczr6&dl=0)**

### Cómo descargar los datos

Los archivos CSV están disponibles en formato RAW. Para descargarlos:
imdb_titulos.csv:
1. Haz clic en el archivo.
2. Haz clic en el botón **"RAW"**.

enlace_imdb_elenco.csv
1. Haz clic en el enlace y descarga el archivo ZIP.
2. Descomprime el archivo.
3. Asegúrate de que el archivo descomprimido se llame **`imdb_elenco.csv`** para que sea compatible con los scripts.


## Ejercicios
A continuación se describen los ejercicios que resuelve el script:

1&2. Cargar los archivos CSV (imdb_titulos.csv y imdb_elenco.csv) como dataframes de pandas y mostrar las primeras 5 filas.

3. Mostrar el número de registros en cada dataframe.
4. Mostrar las 5 películas más antiguas basadas en el año de lanzamiento.
5. Filtrar las películas que contienen "Dracula" en el título y contar el número total de coincidencias.
6. Mostrar los 10 títulos más comunes (aquellos que más se repiten en el listado).
7. Buscar la primera película titulada "Romeo and Juliet".
8. Listar todas las películas que contienen "Exorcist" en el título, ordenadas de la más vieja a la más reciente.
9. Contar cuántas películas fueron hechas en el año 1950.
10. Contar cuántas películas fueron hechas entre 1950 y 1959.
11. Mostrar todos los roles o papeles en la película "The Godfather".
12. Ordenar por la clasificación "n" de los roles de la película "Dracula" (1958).
13. Contar cuántos papeles de "Bruce Wayne" han sido realizados en la historia del cine.
14. Contar cuántos papeles ha hecho "Robert De Niro" en su carrera.
15. Mostrar los papeles como protagonista (n=1) de "Charlton Heston" en la década de los 60's, ordenados por año de forma descendente.
16. Contar cuántos papeles para actores y actrices hubo en la década de los 50's.

## Estructura del repositorio

Pandas_ejercicio/
- **`Código fuente`**
  - **`pandas_analisis.py`**:    # Código fuente con las soluciones del ejercicio
- **`Datos`**
  - **`imdb_titulos.csv`**:            # Archivo CSV con los títulos de las películas
  - **`enlace_imdb_elenco.csv`**:      # Enlace a dropbox para descargar CSV con el elenco de las películas 
- **`Results`**:                 # Resultados generados
  - **`5 peliculas mas antiguas.PNG`**
  - **`5 primeras filas elenco.PNG`**
  - **`5 primeras filas titulo.PNG`**
  - **`Output_textuales`**
  - **`elenco de dracula 1958 ordenados por n.PNG`**
  - **`papeles como protagonista por Charles Heston.PNG`**
  - **`papeles de actor en los 50.PNG`**
  - **`papeles de actriz en los 50.PNG`**
  - **`papeles hechos por Bruce Wayne.PNG`**
  - **`papeles hechos por Robert de Niro.PNG`**
  - **`peliculas hechas en 1950.PNG`**
  - **`peliculas hechas entre 1950-1959.PNG`**
  - **`peliculas que contengan -Exorcist- y ordenadas de mas vieja a mas nueva.PNG`**
  - **`peliculas que contienen el nombre de Dracula.PNG`**
  - **`todos los papeles que hubo en The GodFather.PNG`** 
- **`README.md`**          #Descripcion del proyecto y como ejecutarlo
