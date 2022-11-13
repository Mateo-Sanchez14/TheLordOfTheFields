from __future__ import annotations
from typing import TYPE_CHECKING

import principal

if TYPE_CHECKING:
    from principal.vistas.VentanaPrincipal import VentanaPrincipal
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from conector.controlador.conector import Conector
from kivy.uix.screenmanager import Screen
#from ventana.controladores.VentanaAgregar import Agregar
#import VentanaPrincipal

#from principal.vistas.VentanaPrincipal import VentanaPrincipal as VentanaP


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
        grid.add_widget(Label(text='Vista de la consulta:'))
        # Add a TextInput in the second cell


        # Add a Button in the third cell
        buttonUpdate = Button(text='Actualizar', on_press=self.show_data)
        grid.add_widget(buttonUpdate)
        buttonAdd=Button(text='Agregar')
        grid.add_widget(buttonAdd)
        buttonBack = Button(text='Volver', on_press=self.back)
        grid.add_widget(buttonBack)

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
            column_data=columnitas,
            row_data=self.data,
        )
        screen.add_widget(self.table)
        return screen

    def show_data(self, obj):
        self.data = self.conector.select(self.query)
        self.table.row_data = self.data

    def back(self, obj):
        self.stop()
        #principal.vistas.VentanaPrincipal.root_window()
    #def add(self, obj):
    #    self.stop()
    #    Agregar().run()

