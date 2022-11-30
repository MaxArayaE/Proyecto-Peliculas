from tkinter import *
import tkinter as tk

def in_button(event):
    event.type.config(bg="grey")

    
def out_button(event):
    event.type.config(bg="white")


root = Tk()
root.geometry("1080x720")
root.config(bg="white")
root.title("joder")
root.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=10, weight=10)
    
#imagen
foto = PhotoImage(file="esto es cine2.png")
etiqueta = Label(root, image=foto).grid(row=5, column=3)

#botones 
button1 = tk.Button(root, text="si", cursor= "hand1")
button1.grid(row=8, column=4, columnspan=5, sticky="nsew" )

button2 = tk.Button(root, text="si", cursor= "hand1")
button2.grid(row=4, column=4, columnspan=5, sticky="nsew" )

#evento 
button1.bind("<Enter>", in_button)
button1.bind("<Leave>", out_button)

button2.bind("<Enter>", in_button)
button2.bind("<Leave>", out_button)



root.mainloop()