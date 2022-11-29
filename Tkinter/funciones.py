def crea_lista_archivo(archivo: str, separador) -> list:
    """
    lee un archivo en formato 'txt' y lo retorna en forma de lista,
    separados por lineas y por un caracter (el caracter es opcional)
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

