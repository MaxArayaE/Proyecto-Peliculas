import os


def directories() -> None:
    """
    Imprime directorio actual y los archivos que posee, retorna lista de 
    los archivos en el directorio
    """
    files_list = os.listdir()
    for file in files_list:
        pass
    return files_list