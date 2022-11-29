from os_related import *
from files_related import *
from peliculas_related import *


def main_peliculas(title, director, genre, year, score, root):
    already_exists = False
    files_in_directory = directories()
    for file in files_in_directory:
        if (file == "peliculas.csv"):
            already_exists = True
            break
    if (already_exists):
        with open("peliculas.csv", 'r', encoding="utf-8") as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0) # Solo en caso de...
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
           
