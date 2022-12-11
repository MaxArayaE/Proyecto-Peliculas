def crea_lista_archivo(archivo: str, separador: str) -> list:
    """
    lee un archivo en formato 'txt' o 'csv' y lo retorna en forma de lista,
    separados por lineas y por un caracter
    """
    archivo = open(archivo, 'r', encoding="utf-8").read().split('\n')
    lista = []
    for i in archivo:
        if not i.isspace() and i != '':
            lista.append(i.split(separador))
    for i in lista:
        i[0] = i[0].strip('" ')
        i[1] = i[1].strip('" ')
        i[2] = i[2].strip('" ')

    
    return (lista)

