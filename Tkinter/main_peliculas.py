from os_related import *
from files_related import *
from peliculas_related import *


def main_peliculas(title: str, director: str, genre: str, year: str,
    score: str, root):
    """
    Recibe el título, director, género, año, valoración y la ventana del 
    tkinter. Abre el archivo peliculas.csv si existe, si no, lo crea, 
    luego ingresa la película que recibe de input_movie() en 
    peliculas.csv
    """
    already_exists = False
    files_in_directory = directories()
    for file in files_in_directory:
        if (file == "peliculas.csv"):
            already_exists = True
            break
    if (already_exists):
        with open("peliculas.csv", 'r', encoding="utf-8") as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0) 
        with open("peliculas.csv", 'a', encoding="utf-8") as csv_file:
            if (original_csv_file[-1:] == "\n"):
                input_as_string = input_movie(
                    title, director, genre, year, score, root)
                csv_file.write(input_as_string)
            else:
                input_as_string = input_movie(
                    title, director, genre, year, score, root)
                csv_file.write(f"\n{input_as_string}")
    else:
        with open("peliculas.csv", 'w', encoding="utf-8") as csv_file:    
            input_as_string = input_movie(
                title, director, genre, year, score, root)
            csv_file.write(input_as_string)
