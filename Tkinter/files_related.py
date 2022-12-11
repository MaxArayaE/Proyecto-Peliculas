def obtain_matrix(file_to_read: str) -> list:
    """
    Recibe el archivo a leer de, retorna la salida de readlines sobre el 
    archivo csv en forma de matriz dispuesta asi:
    ['"Genero0"', '"Genero Padre0"'], (...)
    En caso de usarse sobre "peliculas.csv" sería distinto.
    """
    with open(file_to_read, 'r', encoding="utf-8") as csv_file:
        original_csv_file = csv_file.readlines()
        csv_file.seek(0) 
    for i, lista in enumerate(original_csv_file):
        original_csv_file[i] = lista.split(',')
        for j, elemento in enumerate(original_csv_file[i]):
            original_csv_file[i][j] = elemento.strip()
            
    return original_csv_file


def obtain_list(file_to_read: str, no_repeated_values = False, 
            only_father_genres = False) -> list:
    """
    Recibe el archivo a leer de y dos valores booleanos, el primero de 
    estos corresponde a si se quiere retornar una lista sin valores 
    repetidos, el segundo si se quiere que la lista a retorna contenga 
    solo a los generos padres (Solo usar sobre "generos.csv").
    """
    matrix = obtain_matrix(file_to_read)
    list_to_return = []
    if (only_father_genres):
        for lista in matrix:
            list_to_return.append(lista[1])
    else:
        for lista in matrix:
            list_to_return.extend(lista)
    if (no_repeated_values):
        return list(set(list_to_return))
    return list_to_return


def list_strip_double_quotes(any_list: list) -> None:
    for i, elemento in enumerate(any_list):
        any_list[i] = elemento.strip('\"')