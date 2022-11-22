from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker

from conector.controlador.conector import Conector
from kivy.uix.screenmanager import Screen

class VentanaEgreso(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
        self.title = "Ventana Egresos"
        self.screen = Screen()
        self.box = BoxLayout(orientation='vertical')
        self.grid = GridLayout(cols=2, padding=dp(10), spacing=10, row_default_height=80, row_force_default=True, orientation='lr-tb')
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.grid.add_widget(Label(text='Monto:'))
        self.monto = TextInput(multiline=False)
        self.grid.add_widget(self.monto)
        self.grid.add_widget(Label(text='Descripcion:'))
        self.descripcion = TextInput(multiline=False)
        self.grid.add_widget(self.descripcion)
        self.grid.add_widget(Label(text='Fecha:'))
        botonFecha = Button(text='Seleccionar', on_press=self.show_date_picker)
        self.grid.add_widget(botonFecha)
        self.grid.add_widget(Label(text='Tipo:'))
        self.tipo = TextInput(multiline=False)
        self.grid.add_widget(self.tipo)
        self.grid.add_widget(Label(text='Nombre Maquina: '))
        self.idMaquina = TextInput(multiline=False)
        self.grid.add_widget(self.idMaquina)
        self.grid.add_widget(Label(text='Cuenta: '))
        self.idCuenta = TextInput(multiline=False)
        self.grid.add_widget(self.idCuenta)


        self.box.add_widget(self.grid, index=10)
        self.button = Button(text='Guardar', on_press=self.guardar, size_hint_y=None, height=dp(50))
        self.box.add_widget(self.button, index=0)
        self.button = Button(text='Volver', on_press=self.volver, size_hint_y=None, height=dp(50))
        self.box.add_widget(self.button, index=1)
        self.screen.add_widget(self.box)
        return self.screen


    def guardar(self, *args):
        #Conector().insert("INSERT INTO EGRESO (Monto, Descripcion, Fecha, Tipo) VALUES ('{}', '{}', '{}', '{}')".format(self.monto.text, self.descripcion.text, self.fecha, self.tipo.text))
        idCuenta = Conector().select("SELECT idCuenta FROM CUENTA WHERE Nombre = '{}'".format(self.idCuenta.text))
        idEgreso = Conector().select("SELECT idEgreso FROM EGRESO ORDER BY idEgreso DESC LIMIT 1")

        if idEgreso == []:
            idEgreso = 1
        else:
            idEgreso = idEgreso[0][0] + 1
        if idCuenta == []:
            idCuenta = 1
        else:
            idCuenta = idCuenta[0][0]
        fecha = self.fecha.strftime("%Y-%m-%d")

        condition = Conector().insert("INSERT INTO EGRESO (idEgreso, Monto, Detalle, Fecha, idCuenta, idMaquina, Nro_Orden) VALUES ({}, {}, '{}', '{}', {}, {}, {})".format(idEgreso, self.monto.text, self.descripcion.text, fecha, idCuenta, self.idMaquina.text, 1))

        if condition:
            dialog = MDDialog(title='Egreso', text='Egreso guardado correctamente', size_hint=(0.7, 1), buttons=[MDFlatButton(text='Aceptar', on_press=self.volver)])
            dialog.open()
        else:
            dialog = MDDialog(title='Egreso', text='Egreso no guardado', size_hint=(0.7, 1), buttons=[MDFlatButton(text='Aceptar', on_press=self.volver)])
            dialog.open()

        self.monto.text = ''
        self.descripcion.text = ''
        self.tipo.text = ''
        self.idMaquina.text = ''
        self.idCuenta.text = ''

    def volver(self, *args):
        self.stop()


    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.fecha = value
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self, *args):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


