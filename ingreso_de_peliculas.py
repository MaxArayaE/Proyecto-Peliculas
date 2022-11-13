from lectura_de_archivos import *


def movie_and_director_validation(list_to_validate: list) -> bool:
    movies_matrix = obtain_movies_matrix()
    for i in range(len(movies_matrix)):
        values_of_interest = movies_matrix[i][:2]
        values_of_interest = [x.lower() for x in values_of_interest]
        if (values_of_interest
            == list_to_validate):
            return False
    return True


def input_movie(genres_list: list) -> str:
    """
    Recibe diccionario con generos, retorna una str con:
    \t  (1) -> Nombre de la pelicula (str)
    \t  (2) -> Nombre del director (str)
    \t  (3) -> Genero (str)
    \t  (4) -> Año (int)
    \t  (5) -> Valoracion (int)
    Siendo el numero que les antecede el orden en el que estan dentro de
    esta str.
    Las validaciones se hacen en la misma funcion debido a ser demasiado
    especificas acorde al input pedido al usuario, estas son:
    \t  (!) Año tiene que ser mayor o igual a 1895
    \t  (!) Valoracion de 1 a 5, ambos valores incluidos
    \t  (!) Que el genero ingresado ya exista en el programa
    \t  (!) El par ordenado de la pelicula y director no puede ya haber
            existido.
    """
    input_questions = {
        "Nombre de la pelicula\n> " : "str",
        "Nombre del director\n> " : "str",
        "Genero\n> " : "str",
        "Año\n> " : "int",
        "Valoracion\n> ": "int"
    }
    all_user_input = ""
    list_to_validate = []
    while True:
        for i, question in enumerate(input_questions, start=1):
            if (input_questions[question] == "str"):
                if (question == "Genero\n> "):
                    user_input = f"\"{input(question).capitalize()}\""
                    while (user_input not in genres_list):
                        print("Ese genero no esta en nuestra lista, ingresa uno "\
                                "que ya este.")                    
                        user_input = f"\"{input(question).capitalize()}\""
                    user_input = f"\"{user_input}\""
                else:
                    user_input = f"\"{input(question)}\""
                    list_to_validate.append(user_input.lower())
            else:
                if (question == "Año\n> "):
                    while True:
                        try:
                            user_input = int(input(question))
                            while (user_input < 1895):
                                print("¿Enserio?, ingresa fecha valida.")
                                user_input = int(input(question))
                            user_input = str(user_input)
                            break
                        except:
                            print("Me rompiste... Recuerda que un año no puede "\
                                    "ser un numero no entero...")            
                else:
                    while True:    
                        try:
                            user_input = int(input(question))
                            while (user_input < 1
                                    or user_input > 5):
                                print("¿Enserio?, ingresa valoracion valida.")
                                user_input = int(input(question))
                            user_input = str(user_input)
                            break
                        except:
                            print("Me rompiste... Recuerda que una valoracion "\
                                    "debe de ser un numero entero...") 
        if (movie_and_director_validation(list_to_validate)):
            break
        else:
            print("\n- ESTA PELICULA YA HA SIDO INGRESADA... -\n")
    if (i == len(input_questions)):
        all_user_input += user_input
    else:
        all_user_input += f"{user_input}, "
    return all_user_input
