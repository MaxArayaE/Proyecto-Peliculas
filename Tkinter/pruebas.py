from tkinter import *
import tkinter as tk




root = Tk()
root.geometry("1080x720")
root.config(bg="white")
root.title("joder")
root.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=10, weight=10)
    
#imagen
foto = PhotoImage(file="omedeto.gif")
etiqueta = Label(root, image=foto).grid(row=5, column=3)





root.mainloop()