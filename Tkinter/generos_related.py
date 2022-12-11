from files_related import *
import tkinter as tk


def validate_father_genre(genero_padre: str) -> bool:  
    """
    Recibe el género padre y valida si existe en el archivo generos.csv
    """
    genero_padre = genero_padre.lower()
    genres_as_list = obtain_list("generos.csv", True)
    for i in range(len(genres_as_list)):
        genres_as_list[i] = genres_as_list[i].lower()
    if (genero_padre in genres_as_list):
        return True
    return False


def check_if_genre_exists(genero_a_ingresar: str) -> bool:
    """
    Recibe string de genero a ingresar y retorna un valor booleano
    correspondiente a si la string ya existe o no en generos.csv
    """
    genero_a_ingresar = genero_a_ingresar.lower()
    actual_genre = genero_a_ingresar.split(',')
    genres_as_list = obtain_list("generos.csv", True)
    for i in range(len(genres_as_list)):
        genres_as_list[i] = genres_as_list[i].lower()
    if (actual_genre[0] in genres_as_list):
        return True
    return False


def input_genre(genre: str, genre_father: str, root) -> str:
    """
    Esta función recibe el género, género padre y la ventana  
    del tkinter. Luego hace las validaciones de cada uno, si estas son 
    correctas retorna un string de estos separados por una coma.
    """
    entry_error = tk.Toplevel(root)
    entry_error.geometry("500x100")
    entry_error.title("Error!")

    genre = genre.capitalize()
    if (genre_father == ""):
        genre_father = "General"
    
    else:  
        if not validate_father_genre(f"\"{genre_father}\""):
            tk.Label(entry_error, text= ("El género padre no se encuentra en"
                "\nnuestra base de datos, ingrese uno que ya esté."),
        font=(None, 15)).pack(padx=10, pady=20)
            return ""
            
        genre_father = genre_father.capitalize()
    
    string_to_return = f"\"{genre}\", \"{genre_father}\""
    if (check_if_genre_exists(string_to_return)):
        tk.Label(entry_error, text= ("El género con el género padre ingresado "
            "\nya se enceuentra en la base de datos"),
        font=(None, 15)).pack(padx=10, pady=20)

        return ""
    entry_error.title("Omedeto")   
    tk.Label(entry_error, text= ("El género se ha ingresado correctamente."),
        font=(None, 15)).pack(padx=10, pady=20)
            
    return string_to_return
