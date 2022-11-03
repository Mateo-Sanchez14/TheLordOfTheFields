import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Mi ventana principal")
ventana.geometry("800x600")
ventana.resizable(0,0)
ventana.config(bg = "green")

etiqueta = ttk.Label(ventana, text = "Hola mundo")
etiqueta.pack()

ventana.mainloop()