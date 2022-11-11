from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from ventana.vistas.VentanaVista import Vista
class VentanaPrincipal(MDApp):

    #Metodo que se ejecuta al iniciar la aplicacion
    def build(self):
        #Se crea una pantalla
        screen = Screen()
        #Se crea un layout de tipo BoxLayout
        box = BoxLayout(orientation='vertical')
        #Se crea un layout de tipo GridLayout
        grid = GridLayout(cols=2, size_hint_y=None)
        #Se asegura que el alto es suficiente para poder hacer scroll
        grid.bind(minimum_height=grid.setter('height'))

        #Se agrega un label en la primera celda
        grid.add_widget(Label(text='Ejecutar sentencia SQL:'))
        #Se agrega un TextInput en la segunda celda
        self.textinput = TextInput(multiline=False)
        grid.add_widget(self.textinput)
        #Se agrega un boton en la tercera celda
        button = Button(text='Ejecutar', on_press=self.abrir_ventana_consulta)
        grid.add_widget(button)
        #Se agrega el GridLayout al BoxLayout
        box.add_widget(grid)
        #Se agrega el BoxLayout a la pantalla
        screen.add_widget(box)
        return screen

    def abrir_ventana_consulta(self, obj):
        self.stop()
        Vista(self.textinput.text).run()
