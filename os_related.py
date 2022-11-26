import os


def directories() -> None:
    """
    Imprime directorio actual y los archivos que posee, retorna lista de 
    los archivos en el directorio
    """
    print("Verifica de estar en el directorio donde se encuentre "\
        "\"peliculas.csv\"\n"\
        f"Directorio Actual -> {os.getcwd()}\n"\
        "Archivos en directorio:")
    files_list = os.listdir()
    for file in files_list:
        print(f"\t> {file}")
    return files_list