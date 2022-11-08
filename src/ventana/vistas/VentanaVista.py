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
from kivymd.uix.datatables import MDDataTable
from conector.controlador.conector import Conector

class Vista(MDApp):
    def __init__(self,query):
        super().__init__()
        self.query = query
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        # Create a BoxLayout with default orientation
        box = BoxLayout(orientation='vertical')
        # Create a GridLayout with 2 columns
        grid = GridLayout(cols=2, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        grid.bind(minimum_height=grid.setter('height'))
        # Add a Label in the first cell
        grid.add_widget(Label(text='Ejecutar sentencia SQL:'))
        # Add a TextInput in the second cell
        self.textinput = TextInput(multiline=False)
        grid.add_widget(self.textinput)

        # Add a Button in the third cell
        button = Button(text='Ejecutar', on_press=self.show_data)
        grid.add_widget(button)

        # Add the GridLayout to the BoxLayout
        box.add_widget(grid)
        # Add the BoxLayout to the screen
        screen.add_widget(box)

        self.conector = Conector()
        self.data = self.conector.select(self.query)
        columnas = self.conector.columnas
        columnitas = [(x, dp(30)) for x in columnas]

        self.table = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            column_data= columnitas,
            row_data= self.data,
        )
        screen.add_widget(self.table)
        return screen

    def show_data(self, obj):
        # conector = Conector()
        # data = conector.select(self.textinput.text)
        # columnas = conector.columnas
        # columnitas = [(x,dp(30)) for x in columnas]
        # print(columnitas)
        # self.table.row_data = data
        self.data = self.conector.select(self.textinput.text)
        self.table.row_data = self.data
