# Importar pandas
import pandas as pd

# cargar dataframes
ruta_csv1 = "./05_05_imdb_titulos.csv"
ruta_csv2 = "./05_05_imdb_elenco.csv"
df_titulos = pd.read_csv(ruta_csv1, delimiter = ",")
df_elenco = pd.read_csv(ruta_csv2, delimiter = ",")

# 5 primeras filas de titulos
df_titulos.head()

# 5 primeras filas de elenco
df_elenco.head()

# Registros de titulos y elenco
print("Este fichero de titulos tiene: ", len(df_titulos), "registros")
print("Este fichero de elenco tiene: ", len(df_elenco), "registros")

# 5 ultimas peliculos mas antiguas
df_antiguas_titulos = df_titulos.sort_values(by = ["year"], ascending = False)
df_antiguas_titulos.tail()

# Peliculas que tienen "Dracula" en el titulo. Numero de peliculas que contienen esta condicion
df_titulos_dracula = df_titulos.loc[df_titulos["title"] == "Dracula", ["title"]]
print("Hay 6 peliculas con el nombre Dracula. Son las siguientes:")
df_titulos_dracula

# 10 titulos que mas se repiten
df_titulos_repetido = df_titulos.groupby("title")
df_titulos_repetido = df_titulos_repetido.size()
df_titulos_repetido = df_titulos_repetido.sort_values(ascending = False)
print("Estos son los 10 titulos que mas se repiten:")
df_titulos_repetido.head(10)

# 1a pelicula de romeo y julieta
df_titulos_romeo_juliet = df_titulos.loc [(df_titulos["title"] == "Romeo and Juliet"), :]
df_titulos_romeo_juliet = df_titulos_romeo_juliet.sort_values(by = ["year"], ascending = True)
df_titulos_romeo_juliet_1pelicula = df_titulos_romeo_juliet.iloc[0]
df_titulos_romeo_juliet_1pelicula

# Peliculas que tengan en el titulo "Exorcist" y ordenada de mas vieja a mas nueva
df_titulos_ordenadas_año = df_titulos.sort_values(by = ["year"], ascending = True)
df_titulos_ordenadas_año = df_titulos_ordenadas_año.dropna()
df_titulos_ordenadas_año = df_titulos_ordenadas_año.loc[df_titulos_ordenadas_año["title"].str.contains("exorcist", case = False), :]
df_titulos_ordenadas_año

# Peliculas hechas en 1950
df_titulos_1950 = df_titulos.loc[df_titulos["year"]==1950, :]
print("El numero de pelculas hechas en 1950 es de : ", len(df_titulos_1950))
df_titulos_1950

# Peliculas hechas entre 1950 y 1959
df_titulos_50s = df_titulos.loc[(df_titulos["year"] >= 1950) & (df_titulos["year"] < 1960), :]
df_titulos_50s = df_titulos_50s.sort_values(by = ["year"], ascending = False)
print("El numero de peliculas hechas durante los años 1950 y 1959 es de:", len(df_titulos_50s), ", y son las siguientes:")
df_titulos_50s

# Todos los papeles que hubo en The Godfather. Numero de coincidencias
df_elenco_godfather = df_elenco.loc[df_elenco["title"] == "The Godfather", : ]
print("El total de los roles que hubo en la pelicula The Godfather es de: ", len(df_elenco_godfather), "y son los siguientes:")
df_elenco_godfather

# Elenco de Dracula 1958 ordenado por la clasificacion n
df_elenco_dracula_1958 = df_elenco.loc[(df_elenco["title"]=="Dracula") & (df_elenco["year"]==1958), :]
df_elenco_dracula_1958_ordenado = df_elenco_dracula_1958.sort_values(by = ["n"], ascending = False)
df_elenco_dracula_1958_ordenado

# Papeles hechos de Bruce Wayne en la historia
df_elenco_Bruce = df_elenco.loc[df_elenco["character"]=="Bruce Wayne", :]
print("En toda la historia del cine se han hecho", len(df_elenco_Bruce), "papeles de Bruce Wayne")
df_elenco_Bruce

# Papeles hechos por Robert de Niro en la historia
df_elenco_Robert = df_elenco.loc[df_elenco["name"]=="Robert De Niro", :]
print("El actor Robert De Niro ha hecho un total de:", len(df_elenco_Robert), "papeles durante su carrera")
df_elenco_Robert

# Papeles como protagonista (n=1) que tuvo Charlton Heston en los 60s ordenado de forma descendente
df_elenco_Charlton = df_elenco.loc[(df_elenco["name"] == "Charlton Heston") & (df_elenco["n"] == 1 ), :]
df_elenco_Charlton = df_elenco_Charlton.loc[(df_elenco_Charlton["year"] >=1960) & (df_elenco_Charlton["year"] < 1970), :]
df_elenco_Charlton = df_elenco_Charlton.sort_values(by = ["year"], ascending = False)
df_elenco_Charlton

# Papeles de actor en los 50
df_elenco_actores = df_elenco.loc [(df_elenco["year"] >= 1950) & (df_elenco["year"] < 1960), : ]
df_elenco_actores = df_elenco_actores.groupby("type")
df_elenco_actores = df_elenco_actores.get_group("actor")
print("El numero de papeles de ACTOR durante la decada de los 50 fue de:", len(df_elenco_actores))
print("Son los siguientes:")
df_elenco_actores

# Papeles de actress en los 50
df_elenco_actress = df_elenco.loc[(df_elenco["year"] >= 1950) & (df_elenco["year"] < 1960), :]
df_elenco_actress = df_elenco_actress.groupby("type")
df_elenco_actress = df_elenco_actress.get_group("actress")
print("El numero de papeles de ACTRICES durante la decada de los 50 fue de:", len(df_elenco_actress))
print("Son los siguientes:")
df_elenco_actress
