def input_movie(generos_peliculas: dict) -> str:
    """
    Recibe diccionario con generos, retorna una str con:
    \t  (1) -> Nombre de la pelicula (str)  \n
    \t  (2) -> Nombre del director (str)    \n
    \t  (3) -> Genero (str)                 \n
    \t  (4) -> Año (int)                    \n
    \t  (5) -> Valoracion (int)
    Siendo el numero que les antecede el orden en el que estan dentro de
    esta str.
    Las validaciones se hacen en la misma funcion debido a ser demasiado
    especificas acorde al input pedido al usuario, estas son:
    \t  (!) Año tiene que ser mayor o igual a 1895              \n
    \t  (!) Valoracion de 1 a 5, ambos valores incluidos        \n
    \t  (!) Que el genero ingresado ya exista en el programa    \n
    """
    input_questions = {
        "Nombre de la pelicula\n> " : "str",
        "Nombre del director\n> " : "str",
        "Genero\n> " : "str",
        "Año\n> " : "int",
        "Valoracion\n> ": "int"
    }
    all_user_input = ""
    for i, question in enumerate(input_questions, start=1):
        if (input_questions[question] == "str"):
            if (question == "Genero\n> "):
                user_input = input(question).capitalize()
                while (user_input not in generos_peliculas):
#
#   OJITO CON ESTA LINEA Y EL DE DONDE SACA LOS GENEROS, ESTO VA A
#   CAMBIAR SI O SI.
#
                    print("Ese genero no esta en nuestra lista, ingresa uno "\
                            "ya este.")                    
                    user_input = input(question).capitalize()
                user_input = f"\"{user_input}\""
            else:
                user_input = f"\"{input(question)}\""
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
        if (i == len(input_questions)):
            all_user_input += user_input
        else:
            all_user_input += f"{user_input}, "
    return all_user_input
