def obtain_genres_matrix() -> list:
    """
    No recibe nada, retorna la salida de readlines sobre el archivo csv
    en forma de matriz.
    La forma de esta matriz es:
    \t  ['"Genero0"', '"Genero Padre0"'],
    \t  ['"Genero1"', '"Genero Padre1"'],
    \t  ['"Genero2"', '"Genero Padre2"']...
    """
    with open("generos.csv", 'r') as csv_file:
        original_csv_file = csv_file.readlines()
        csv_file.seek(0)
    original_csv_file = [x.split(',') for x in original_csv_file]
    for i, list in enumerate(original_csv_file):
        for j, element in enumerate(list):
            original_csv_file[i][j] = element.strip()
    return original_csv_file


def obtain_genres_list(no_repeated_values: bool) -> list:
    """
    Recibe un valor booleano, el retorno que tendra dependera de este.
    Si el valor booleano recibido es True:
    \t  Obtiene en forma de matriz la salida del readlines sobre el
    \t  archivo csv usando la funcion obtain_genres_matrix() y
    \t  retorna la matriz extendida de tal forma que ahora sera una
    \t  lista, PERO, recibiendo el valor booleano la pasara a set y
    \t  luego a lista, detal forma no hay elementos repetidos     
    Si el valor booleano recibido es False:
    \t  El unico cambio sera que la lista a retornar tendra los 
    \t  elementos repetidos y en "orden"
    """
    genres_matrix = obtain_genres_matrix()
    list_to_return = []
    for lista in genres_matrix:
        list_to_return.extend(lista)
    if (no_repeated_values):
        return list(set(list_to_return))
    return list_to_return

def strip_genres_list(genres_list: list) -> None:
    """
    Basicamente el map(func(), iterable) pero con .strip(\").
    """
    for i, element in enumerate(genres_list):
        genres_list[i] = element.strip("\"")

def obtain_movies_matrix() -> list:
    """
    No recibe nada, retorna la salida de readlines sobre el archivo csv
    en forma de matriz.
    La forma de esta matriz es:
    \t  ['"NombrePelicula0"', '"NombreDirector0"', '"NombreGenero0"',
    '"Año"', '"Valoracion"'],
    \t  ['"NombrePelicula0"', '"NombreDirector0"', '"NombreGenero0"',
    '"Año"', '"Valoracion"'],
    \t  ['"NombrePelicula0"', '"NombreDirector0"', '"NombreGenero0"',
    '"Año"', '"Valoracion"']...
    """
    with open("peliculas.csv", 'r') as csv_file:
        original_csv_file = csv_file.readlines()
        csv_file.seek(0)
    original_csv_file = [x.split(',') for x in original_csv_file]
    for i, list in enumerate(original_csv_file):
        for j, element in enumerate(list):
            original_csv_file[i][j] = element.strip()
            # Falta añadir alguna forma de que no se arruinen los ',
            # Child's Play -> Child\'s Play o traducirlo despues cuando
            # se muestre en la GUI.
    return original_csv_file
    
def obtain_movies_list(no_repeated_values: bool) -> list:
    """
    Recibe un valor booleano, el retorno que tendra dependera de este.
    Si el valor booleano recibido es True:
    \t  Obtiene en forma de matriz la salida del readlines sobre el
    \t  archivo csv usando la funcion obtain_genres_movies() y
    \t  retorna la matriz extendida de tal forma que ahora sera una
    \t  lista, PERO, recibiendo el valor booleano la pasara a set y
    \t  luego a lista, detal forma no hay elementos repetidos     
    Si el valor booleano recibido es False:
    \t  El unico cambio sera que la lista a retornar tendra los 
    \t  elementos repetidos y en "orden"
    """
    movies_matrix = obtain_movies_matrix()
    list_to_return = []
    for lista in movies_matrix:
        list_to_return.extend(lista)
    if (no_repeated_values):
        return list(set(list_to_return))
    return list_to_return

    