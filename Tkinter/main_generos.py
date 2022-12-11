from os_related import *
from files_related import *
from generos_related import *


def main_generos(genre: str, genre_father: str, root):
    """
    Recibe el género, el género padre y la ventana. Abre el archivo csv  
    de generos si existe, si no, lo crea, luego ingresa el género que 
    recibe de la función input_genre() en generos.csv.
    """
    already_exists = False
    files_in_directory = directories()
    for file in files_in_directory:
        if (file == "generos.csv"):
            already_exists = True
            break
    if (already_exists):
        with open("generos.csv", 'r', encoding="utf-8") as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0)    
        with open("generos.csv", 'a', encoding="utf-8") as csv_file:
            if (original_csv_file[-1:] == "\n"):
                input_as_string = input_genre(genre, genre_father, root)
                csv_file.write(input_as_string)
            else:
                input_as_string = input_genre(genre, genre_father, root)
                csv_file.write(f"\n{input_as_string}")
    else:
        with open("generos.csv", 'w', encoding="utf-8") as csv_file:
            input_as_string = input_genre(genre, genre_father, root)
            csv_file.write(input_as_string) 
