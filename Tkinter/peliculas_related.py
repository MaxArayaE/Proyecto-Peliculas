from files_related import *
import tkinter as tk


def equal_movie_and_director_exists(list_to_validate: list) -> bool:
    """
    Recibe lista dispuesta de esta forma ["Pelicula", "Director"], retorna 
    valor booleano que corresponderá a sí ya existe o no este par en 
    "peliculas.csv".
    """
    movies_matrix = obtain_matrix("peliculas.csv")
    lowered_list_to_validate = [x.lower() for x in list_to_validate]
    for i in range(len(movies_matrix)):
        values_of_interest = movies_matrix[i][:2]
        values_of_interest = [x.lower() for x in values_of_interest]
        if (values_of_interest
            == lowered_list_to_validate):
            return True
    return False


def input_movie(title, director, genre, year, score, root) -> str:

    entry_error = tk.Toplevel(root) 
    entry_error.geometry("500x100")
    entry_error.title("Error!")

    all_user_input = ""
    list_to_validate = []
    genres_list = obtain_list("generos.csv", True)

    all_user_input = f'"{title}", "{director}", "{genre}", {year}, {score}'
    list_to_validate = [f'"{title}"', f'"{director}"']
    
    if genre not in genres_list:
        tk.Label(entry_error, text= ("El género no se encuentra en nuestra"
            " base de datos,\ndebe agregarlos previamente"),
        font=(None, 15)).pack(padx=10, pady=20)
        return ""

    if int(year) < 1895:
        tk.Label(entry_error, text= ("El año debe ser mayor o igual a 1895"),
        font=(None, 15)).pack(padx=10, pady=20)
        return ""

    if int(score) < 1 or int(score) > 5:
        tk.Label(entry_error, text= ("La valoración debe ser entre 1 y 5"),
        font=(None, 15)).pack(padx=10, pady=20)
        return ""

    if (equal_movie_and_director_exists(list_to_validate)):
        tk.Label(entry_error, text= "El par de películas y director ya están",
        font=(None, 20)).pack(padx=10, pady=20)
        return ""

    return all_user_input


# La verdad este código me deja medio esceptico, siento que si bien ayuda en
# que se puedan añadir aun más preguntas en un futuro, no es demasiado optimo
# y hace muchas validaciones totalmente innecesarias al estar entero dentro de
# un for.
