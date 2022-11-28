def crea_lista_archivo(archivo: str, separador=False) -> list:
    """
    lee un archivo en formato 'txt' y lo retorna en forma de lista,
    separados por lineas y por un caracter (el caracter es opcional)
    """
    archivo = open(archivo, 'r', encoding="utf-8").read().split('\n')
    lista = []
    for i in archivo:
        if not i.isspace() and i != '':
            if separador:
                lista.append(i.split(separador))
            else:
                lista.append(i)
    return (lista)
