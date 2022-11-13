from lectura_de_archivos import *


def validate_genre(genero_padre: str) -> bool:
    """
    Recibe una str, retorna un valor booleano correspondiente a si esa
    str existe en generos.csv como posible genero padre o no.
    """
    genres_as_list = obtain_genres_list(True)
    if (genero_padre in genres_as_list):
        return True
    return False


def input_genre() -> str:
    """
    No recibe nada, retorna un str lista para escribir en "generos.csv".
    """
    genre = input("Nombre del genero a añadir\n> ").capitalize()
    father_of_genre = input(f"Nombre de genero padre de \"{genre}\"\n> ")
    if (father_of_genre == ""):
        father_of_genre = "General"
    else:
        while (validate_genre(f"\"{father_of_genre}\"") == False):
            print("Ese genero no esta en nuestra lista, ingresa uno que ya este.")
            father_of_genre = input("Nombre de genero padre de "\
                                        f"\"{genre}\"\n> ")
    return f"\"{genre}\", \"{father_of_genre}\""
