import os
from ingreso_de_peliculas import *
# Usar archivo .csv de generos en -ingreso_de_peliculas-
from funciones_directorios import *


generos_peliculas = obtain_genres_list(True)


def main():
    directories()
    already_exists = False
    files_in_directory = os.listdir()
    for file in files_in_directory:
        if (file == "peliculas.csv"):
            already_exists = True
            break
    if (already_exists):
        with open("peliculas.csv", 'r') as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0)
        with open("peliculas.csv", 'a') as csv_file:
            if (original_csv_file[-1:] == "\n"):
                input_as_string = input_movie(generos_peliculas)
                csv_file.write(input_as_string)
            else:
                input_as_string = input_movie(generos_peliculas)
                csv_file.write(f"\n{input_as_string}")
    else:
        with open("peliculas.csv", 'w') as csv_file:    
            input_as_string = input_movie(generos_peliculas)
            csv_file.write(input_as_string)
           

if __name__ == "__main__":
    main()
