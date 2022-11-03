import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
    
        # Configure Window
        self.title("Mi ventana principal")
        self.geometry("800x600")
        self.resizable(0,0)
        self.config(bg = "green")

        self.crear_gui()


    def crear_gui(self):
        self.etiqueta = ttk.Label(self, text = "Hola mundo")
        self.etiqueta.grid(column=0, row=0, padx=10, pady=10)

