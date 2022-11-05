from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class VentanaPrincipal(App):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.window = None

    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.add_widget(Label(text="Nombre:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Apellido:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Edad:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Sexo:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Email:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Telefono:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Direccion:"))
        self.window.add_widget(TextInput(multiline=False))
        self.window.add_widget(Label(text="Ciudad:"))
        self.window.add_widget(TextInput(multiline=False))

        self.window.add_widget(Button(text="Guardar"))
        self.window.add_widget(Button(text="Cancelar"))

        # add widgets to window

        return self.window

