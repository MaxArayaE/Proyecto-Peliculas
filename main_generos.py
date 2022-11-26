from os_related import *
from files_related import *
from generos_related import *


def main():
    already_exists = False
    files_in_directory = directories()
    for file in files_in_directory:
        if (file == "generos.csv"):
            already_exists = True
            break
    if (already_exists):
        with open("generos.csv", 'r') as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0)    # Solo en caso de que quisiese usar
                                # el read() o readlines() despues.
        with open("generos.csv", 'a') as csv_file:
            if (original_csv_file[-1:] == "\n"):
                input_as_string = input_genre()
                csv_file.write(input_as_string)
            else:
                input_as_string = input_genre()
                csv_file.write(f"\n{input_as_string}")
    else:
        with open("generos.csv", 'w') as csv_file:
            input_as_string = input_genre()
            csv_file.write(input_as_string) 


if __name__ == "__main__":
    main()