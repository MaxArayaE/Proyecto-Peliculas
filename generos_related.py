from files_related import *


def validate_father_genre(genero_padre: str) -> bool:
    """
    ¡RECUERDA AÑADIR EN LA STRING \" TANTO EN EL INICIO COMO FIN DE 
    ESTA, SINO SE RETORNARA UN VALOR QUIZÁ ERRONEO!
    Recibe una str, retorna un valor booleano correspondiente a si esa
    str existe en generos.csv como posible genero padre o no.
    """
    genres_as_list = obtain_list("generos.csv", True)
    if (genero_padre in genres_as_list):
        return True
    return False


def check_if_genre_exists(genero_a_ingresar: str) -> bool:
    """
    Recibe string de genero a ingresar y retorna un valor booleano
    correspondiente a si la string ya existe o no en generos.csv
    """
    actual_genre = genero_a_ingresar.split(',')
    genres_as_list = obtain_list("generos.csv", True)
    if (actual_genre[0] in genres_as_list):
        return True
    return False


# Podria haber juntado ambas funciones arriba pero creo que seria algo
# no óptimo, añadiria mucho "if" innecesario y seria menos legible, de
# hecho en "files_related.py" ya estoy medio esceptico de lo que hice
# con obtain_list().


def input_genre() -> str:
    """
    No recibe nada, retorna un str lista para escribir sobre "generos.csv".
    """
    while True:
        genre = input("Nombre del genero a añadir\n> ").capitalize()
        father_of_genre = input("Nombre de genero padre de "\
                                f"{genre}\n> ").capitalize()
        if (father_of_genre == ""):
            father_of_genre = "General"
        else:
            while (validate_father_genre(f"\"{father_of_genre}\"") == False):
                print("Ese genero padre no esta en nuestra lista, ingresa uno"\
                    " que ya este.")
                father_of_genre = input("Nombre de genero padre de "\
                                        f"\"{genre}\"\n> ").capitalize
        string_to_return = f"\"{genre}\", \"{father_of_genre}\""
        if (check_if_genre_exists(string_to_return)):
            print("----------------------------------------\n" \
                "Genero ya se encuentra en \"generos.csv\"" \
                "\n----------------------------------------")
        else:
            return string_to_return
