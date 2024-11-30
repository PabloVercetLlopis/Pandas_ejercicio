# Pandas_ejercicio
# Ejercicio de Análisis Avanzado de Datos con Pandas en Python

Este repositorio contiene una serie de ejercicios prácticos diseñados para trabajar con la librería **Pandas** en Python, con el objetivo de analizar datos de películas utilizando dos archivos CSV: **`imdb_titulos.csv`** y **`imdb_elenco.csv`**.

## Requisitos

Para ejecutar este proyecto, necesitarás tener **Python 3.8 o superior** instalado y las siguientes librerías:

- pandas
- matplotlib (para gráficas, si se requieren)

## Archivos
imdb_titulos.csv: Contiene información sobre los títulos de películas, incluyendo el año de lanzamiento y otros detalles.

imdb_elenco.csv: Contiene información sobre los elencos de las películas, incluyendo los actores, roles y años de participación.

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

pandas_exercise/

├── README.md              # Descripción del proyecto y cómo ejecutarlo
├── imdb_titulos.csv       # Archivo CSV con los títulos de las películas
├── imdb_elenco.csv        # Archivo CSV con el elenco de las películas
├── pandas_analysis.py     # Código fuente con las soluciones del ejercicio
├── results/               # Resultados generados (si aplican)
│   ├── logs/              # Archivos de logs generados (si aplican)
│   ├── graphs/            # Gráficas generadas durante el análisis (si aplican)
│   ├── tables/            # Tablas generadas (si aplican)
