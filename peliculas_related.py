from files_related import *


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


def input_movie() -> str:
    """
    No recibe nada, retorna una str con nombre de la pelicula, director de 
    esta, genero, año y valoración, en ese orden.
    """
    genres_list = obtain_list("generos.csv", True)
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
                        print("Ese genero no esta en nuestra lista, ingresa "\
                            "uno que ya este.")                    
                        user_input = f"\"{input(question).capitalize()}\""
                else:
                    user_input = f"\"{input(question)}\""
                    list_to_validate.append(user_input)
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
                            print("Me rompiste... Recuerda que un año no "\
                                "puede ser un numero no entero...")            
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
                            print("Me rompiste... Recuerda que una "\
                                "valoracion debe de ser un numero entero...")
            if (i == len(input_questions)):
                all_user_input += user_input
            else:
                all_user_input += f"{user_input}, "
        if (equal_movie_and_director_exists(list_to_validate)):
            print("--------------------------------------------\n" \
                "El par de pelicula y director ya se encuentran" \
                "en \"peliculas.csv\"" \
                "\n--------------------------------------------")
            all_user_input = ""
            list_to_validate = []
        else:
            break
    return all_user_input


# La verdad este código me deja medio esceptico, siento que si bien ayuda en
# que se puedan añadir aun más preguntas en un futuro, no es demasiado optimo
# y hace muchas validaciones totalmente innecesarias al estar entero dentro de
# un for.
