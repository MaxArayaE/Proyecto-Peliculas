import tkinter as tk
from tkinter import ttk
from funciones import crea_lista_archivo
from peliculas_related import *
from main_peliculas import *
import sys


def root_generator():
    root = tk.Toplevel()
    root.geometry("1080x720") # Tamaño de la ventana
    root.config(bg="pink")
    root.config(cursor="heart")
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
    root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=5, weight=10)
    return root


def close(event=None):
    sys.exit()


def movies_menu(root_main):
    def temp_title(event):
        if event.type == tk.EventType.FocusIn and title_entry.get() == temp_title_text:
            title_entry.delete(0, "end")
            title_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if title_entry.get() == "":
                title_entry.config(fg="gray")
                title_entry.insert(0, temp_title_text)


    def temp_director(event):
        if event.type == tk.EventType.FocusIn and director_entry.get() == temp_director_text:
            director_entry.delete(0, "end")
            director_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if director_entry.get() == "":
                director_entry.config(fg="gray")
                director_entry.insert(0, temp_director_text)


    def temp_genre(event):
        if event.type == tk.EventType.FocusIn and genre_entry.get() == temp_genre_text:
            genre_entry.delete(0, "end")
            genre_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if genre_entry.get() == "":
                genre_entry.config(fg="gray")
                genre_entry.insert(0, temp_genre_text)


    def temp_year(event):
        if event.type == tk.EventType.FocusIn and year_entry.get() == temp_year_text:
            year_entry.delete(0, "end")
            year_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if year_entry.get() == "":
                year_entry.config(fg="gray")
                year_entry.insert(0, temp_year_text)


    def temp_score(event):
        if event.type == tk.EventType.FocusIn and score_entry.get() == temp_score_text:
            score_entry.delete(0, "end")
            score_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if score_entry.get() == "":
                score_entry.config(fg="gray")
                score_entry.insert(0, temp_score_text)


    def back_main(event):
        root_main.deiconify()
        root.destroy()


    def confirmar(event):
        if (title_entry.get() != "" and not title_entry.get().isspace() and
            title_entry.get() != temp_title_text
            and director_entry.get() != "" and
            director_entry.get() != temp_director_text and
            not director_entry.get().isspace() and
            genre_entry.get() != "" and not genre_entry.get().isspace() and
            genre_entry.get() != temp_genre_text and
            year_entry.get() != "" and not year_entry.get().isspace() and
            year_entry.get() != temp_year_text and
            score_entry.get() != "" and not score_entry.get().isspace() and
            score_entry.get() != temp_score_text):

            main_peliculas(title_entry.get(), director_entry.get(),
            genre_entry.get(), year_entry.get(), score_entry.get(), root)


        else:
            entry_error = tk.Toplevel(root) 
            entry_error.geometry("500x100")
            entry_error.title("Error!")
            tk.Label(entry_error, text= "Porfavor, ingrese todos los datos",
            font=(None, 15)).pack(padx=10, pady=20)




    root = root_generator()
    root.title("Ingresar películas")
    root_main.withdraw()
    
    # Titulo de la ventana
    tk.Label(root, text="Ingresar Películas", font=(None, 30), bg="pink",
    ).grid(row=0, column=3, columnspan=5, sticky="new")
    
    # Título
    title_entry = tk.Entry(root, width=40, font=(None, 25), fg="gray")
    title_entry.grid(row=1, column=1, columnspan=7, sticky="w")
    temp_title_text = "Ingrese el Título de la película aquí"
    title_entry.insert(0, temp_title_text)

    # Director
    director_entry = tk.Entry(root, width=40, font=(None, 25), fg="gray")
    director_entry.grid(row=3, column=1, columnspan=7, sticky="w")
    temp_director_text = "Ingrese el Director de la película aquí"
    director_entry.insert(0, temp_director_text)

    # Genero
    genre_entry = tk.Entry(root, width=40, font=(None, 25), fg="gray")
    genre_entry.grid(row=5, column=1, columnspan=7, rowspan=1, sticky="w")
    temp_genre_text = "Ingrese el Género de la película aquí"
    genre_entry.insert(0, temp_genre_text)

    # Año
    year_entry = tk.Entry(root, width=30, font=(None, 25), fg="gray")
    year_entry.grid(row=7, column=1, columnspan=4, rowspan=1, sticky="w")
    temp_year_text = "Ingrese el año de la película aquí"
    year_entry.insert(0, temp_year_text)

    # Valoracion
    score_entry = tk.Entry(root, width=30, font=(None, 25), fg="gray")
    score_entry.grid(row=7, column=5, columnspan=4, rowspan=1, sticky="e")
    temp_score_text = "Ingrese la valoración de la película aquí"
    score_entry.insert(0, temp_score_text)

    #  Botones
    button1 = tk.Button(root, text="Volver atrás", cursor="hand1", height=2)
    button1.grid(row=9, column=1, columnspan=2, sticky="sew")
    button2 = tk.Button(root, text="Confirmar", cursor="hand1", height=2)
    button2.grid(row=9, column=8, columnspan= 2, sticky="sew")

    # Eventos
    title_entry.bind("<FocusIn>", temp_title)
    title_entry.bind("<FocusOut>", temp_title)

    director_entry.bind("<FocusIn>", temp_director)
    director_entry.bind("<FocusOut>", temp_director)

    genre_entry.bind("<FocusIn>", temp_genre)
    genre_entry.bind("<FocusOut>", temp_genre)

    year_entry.bind("<FocusIn>", temp_year)
    year_entry.bind("<FocusOut>", temp_year)

    score_entry.bind("<FocusIn>", temp_score)
    score_entry.bind("<FocusOut>", temp_score)

    button1.bind("<Button-1>", back_main)
    button2.bind("<Button-1>", confirmar)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)
    
    root.mainloop()


def genres_menu(root_main):



    def temp_genre(event):
        if event.type == tk.EventType.FocusIn and genre_entry.get() == temp_genre_text:
            genre_entry.delete(0, "end")
            genre_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if genre_entry.get() == "":
                genre_entry.config(fg="gray")
                genre_entry.insert(0, temp_genre_text)


    def temp_year(event):
        if event.type == tk.EventType.FocusIn and year_entry.get() == temp_year_text:
            year_entry.delete(0, "end")
            year_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if year_entry.get() == "":
                year_entry.config(fg="gray")
                year_entry.insert(0, temp_year_text)


    def back_main(event):
        root_main.deiconify()
        root.destroy()



    
    root = root_generator()
    root.title("Ingresar películas")
    root_main.withdraw()
    
    # Titulo de la ventana
    tk.Label(root, text="Ingresar Géneros", font=(None, 30), bg="pink",
    ).grid(row=0, column=3, columnspan=5, sticky="new")
    
    # Título
    frame_movie = tk.Frame(root, bd="3", relief="groove")
    frame_movie.grid(row=2, column=2, columnspan=7, rowspan=1, sticky="nsew")
    scroll_v = tk.Scrollbar(frame_movie)
    scroll_v.pack(side="right", fill="y")
    text_area = tk.Text(
        frame_movie, wrape=None, yscrollcommand=scroll_v.set,
        font=(None, 20), height=10
    )
                #text_area.insert(tk.END, movies_text)
    text_area.pack(side="top", fill="x")
    scroll_v.config(command=text_area.yview)
    text_area.config(state="disabled")


    # Genero
    genre_entry = tk.Entry(root, width=50, font=(None, 25), fg="gray")
    genre_entry.grid(row=6, column=2, columnspan=7, rowspan=1, sticky="w")
    temp_genre_text = "Ingrese el Género aquí"
    genre_entry.insert(0, temp_genre_text)

    # Genero Padre
    year_entry = tk.Entry(root, width=50, font=(None, 25), fg="gray")
    year_entry.grid(row=7, column=2, columnspan=7, rowspan=1, sticky="w")
    temp_year_text = "(opcional) Ingrese el Género Padre"
    year_entry.insert(0, temp_year_text)


    #  Botones
    button1 = tk.Button(root, text="Volver atrás", cursor="hand1", height=2)
    button1.grid(row=9, column=1, columnspan=2, sticky="sew")
    button2 = tk.Button(root, text="Confirmar", cursor="hand1", height=2)
    button2.grid(row=9, column=8, columnspan= 2, sticky="sew")

    # Eventos

    genre_entry.bind("<FocusIn>", temp_genre)
    genre_entry.bind("<FocusOut>", temp_genre)

    year_entry.bind("<FocusIn>", temp_year)
    year_entry.bind("<FocusOut>", temp_year)


    button1.bind("<Button-1>", back_main)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)
    
    root.mainloop()


def main():
    fuente_texto = "Courier"


    def genres_window(event):
        #root.destroy()
        genres_menu(root)
    

    def movies_window(event):
        movies_menu(root)
        
    

    def buscador_peliculas(event):
        texto_buscado = buscador.get().lower()
        if (texto_buscado != "" and not texto_buscado.isspace()
            and buscador_combo.get() != combo_normal):
            text_area.config(state="normal")
            text_area.delete(1.0, tk.END)
            if buscador_combo.get() == combo_title:
                for i in movies_list:
                    if (i[0].lower().find(texto_buscado) != -1 or
                        i[1].lower().find(texto_buscado) != -1):
                        text_area.insert(tk.END, f"{','.join(i)}\n")

            elif buscador_combo.get() == combo_genre:
                for i in movies_list:
                    if (i[2].lower().find(texto_buscado) != -1 and
                        texto_buscado != "" and not texto_buscado.isspace()):
                        text_area.insert(tk.END, f"{','.join(i)}\n")
            elif buscador_combo.get() == combo_score:
                for i in movies_list:
                    print(i)
                    if (i[4].find(texto_buscado) != -1 and
                        texto_buscado != "" and not texto_buscado.isspace()):
                        text_area.insert(tk.END, f"{','.join(i)}\n")
            text_area.config(state="disable")
        else:
            text_area.config(state="normal")
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, movies_text)

    # Ventana Principal
    

    root = tk.Tk()
    root.geometry("1080x720") # Tamaño de la ventana
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    root.title("Fvck this is cine")
    root.config(bg="pink")
    root.config(cursor="heart")
    root.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
    root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=10, weight=10)

    with open("peliculas.csv", mode="r", encoding="utf-8") as movies_file:
        movies_text = movies_file.read() #  lee archivo
    movies_list = crea_lista_archivo("peliculas.csv", ",")

    #  Titulo
    tk.Label(
        root,
        text="Bienvenido a Fvck this is cine\nLa aplicacion para buscar, "
        "clasificar y puntuar\n tus películas favoritas\na continuacion haz "
        "click en tu opción deseada",
        bg="white",
        font=("Arial", 20, "bold", "roman"), relief="groove", bd=3
    ).grid(row=1, column=2, rowspan=1, columnspan=7, sticky="nsew")
    
    #  Buscador
    frame_search = tk.Frame(
        root, bd=3, height="40", relief="groove")
    frame_search.grid(row=3, column=2, columnspan=7, sticky="we")

    buscador = tk.Entry(frame_search, font=(fuente_texto, 20), width=45)
    buscador.grid(row=0, column=1, sticky="ns")
    combo_title = "Título o director"
    combo_genre = "Género"
    combo_score = "Valoración"
    combo_normal = "Buscar película por:"
    buscador_combo = ttk.Combobox(frame_search, state="readonly",
        values=[combo_normal, combo_title, combo_genre, combo_score]
    )
    buscador_combo.current(0)
    buscador_combo.grid(row=0, column=0, sticky="w")
    button_search = tk.Button(frame_search, text="buscar", cursor="hand1")
    #owo
    button_search.grid(row=0, column=2, sticky="e")

    #  Peliculas
    frame_movie = tk.Frame(root, bd="3", relief="groove")
    frame_movie.grid(row=6, column=2, columnspan=7, rowspan=1, sticky="nsew")
    scroll_v = tk.Scrollbar(frame_movie)
    scroll_v.pack(side="right", fill="y")
    text_area = tk.Text(
        frame_movie, wrape=None, yscrollcommand=scroll_v.set,
        font=(fuente_texto, 20), height=15
    )
    text_area.insert(tk.END, movies_text)
    text_area.pack(side="top", fill="x")
    scroll_v.config(command=text_area.yview)
    text_area.config(state="disabled")

    #  Botones
    button2 = tk.Button(root, text="Ingresar Películas", cursor="hand1")
    button2.grid(row=9, column=8, columnspan= 2, sticky="nsew")
    button1 = tk.Button(root, text="Ingresar Género", cursor="hand1", height=1)
    button1.grid(row=9, column=1, columnspan=2, sticky="nsew")

    #  Eventos
    button_search.bind("<Button-1>", buscador_peliculas)
    buscador.bind("<Return>", buscador_peliculas)
    button1.bind("<Button-1>", genres_window)
    button2.bind("<Button-1>", movies_window)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)
    

    root.mainloop()


if __name__ == "__main__":
    main()
