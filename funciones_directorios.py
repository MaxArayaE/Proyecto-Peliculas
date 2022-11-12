import os


def directories() -> None:
    """
    Es solo una funcion con la que imprimo cosas relacionadas a
    directorios.
    """
    print("Verifica de estar en el directorio donde se encuentre "\
        "\"peliculas.csv\"\n"\
        f"Directorio Actual -> {os.getcwd()}\n"\
        "Archivos en directorio:")
    files_list = os.listdir()
    for file in files_list:
        print(f"\t> {file}")
