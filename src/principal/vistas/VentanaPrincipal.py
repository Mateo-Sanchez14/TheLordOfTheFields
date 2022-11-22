from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from ventana.vistas.VentanaVista import Vista
class VentanaPrincipal(MDApp):

    #Metodo que se ejecuta al iniciar la aplicacion
    def build(self):
        #Se crea una pantalla
        screen = Screen()
        #Se ponen los colores de la aplicacion
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        #Se agrega una imagen
        image = AsyncImage(source='https://st.depositphotos.com/1526816/2017/v/600/depositphotos_20172553-stock-illustration-a-sack-of-potatoes.jpg')
        image.size_hint = (1, 0.7)
        #Se agrega una imagen al layout
        screen.add_widget(image)


        #Se crea un layout de tipo BoxLayout
        box = BoxLayout(orientation='vertical')
        #Se crea un layout de tipo GridLayout
        grid = GridLayout(cols=2, padding=dp(10), spacing=10, row_default_height=80, row_force_default=True, orientation='lr-tb')
        #Se asegura que el alto es suficiente para poder hacer scroll
        grid.bind(minimum_height=grid.setter('height'))


        #Se agrega una etiqueta en la izquierda de la pantalla
        grid.add_widget(Label(text='Consultas Rapidas:'))
        #Se agrega una etiqueta vacia en la derecha de la pantalla
        grid.add_widget(Label(text=''))


        #Se agrega un boton en la pantalla
        button = Button(text='Ingresos', on_press=self.abrir_ingresos)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Egresos del mes', on_press=self.abrir_egresos)
        grid.add_widget(button)
        # Se agrega un boton en la pantalla
        button = Button(text='Partes por Maquina', on_press=self.abrir_partes_maquina)
        grid.add_widget(button)
        # Se agrega un boton en la pantalla
        button = Button(text='Partes por Empleado', on_press=self.abrir_partes_empleado)
        grid.add_widget(button)
        # Se agrega un boton en la pantalla
        button = Button(text='Lotes por finca', on_press=self.abrir_lotes_finca)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Ayudantes por Empleado', on_press=self.abrir_ayudantes_empleado)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Cheques de la semana', on_press=self.abrir_cheques_semana)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Gastos en comida', on_press=self.abrir_gastos_comida)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Proovedores agroquímicos', on_press=self.abrir_proovedores_agroquimicos)
        grid.add_widget(button)
        #Se agrega un boton en la pantalla
        button = Button(text='Fincas con Limones', on_press=self.abrir_fincas_limones)
        grid.add_widget(button)


        #Se agrega el GridLayout al BoxLayout
        box.add_widget(grid, index=2)

        #Se agrega un boton en la pantalla
        button = Button(text='Agregar Ingreso', on_press=self.abrir_ventana_agregar, size_hint=(1, 0.1))
        box.add_widget(button, index=0)
        #Se agrega el BoxLayout a la pantalla
        button = Button(text='Agregar Egreso', on_press=self.abrir_ventana_agregar, size_hint=(1, 0.1))
        box.add_widget(button, index=0)
        screen.add_widget(box)
        return screen

    def abrir_ventana_agregar(self, obj):
        self.stop()
        #Vista(self.textinput.text).run()
        self.run()

    def abrir_partes_maquina(self, obj):
        self.stop()
        Vista("partesxmaquina").run()
        self.run()

    def abrir_ingresos(self, obj):
        self.stop()
        Vista("ingresos").run()
        self.run()

    def abrir_egresos(self, obj):
        self.stop()
        Vista("egresos_del_mes").run()
        self.run()

    def abrir_partes_empleado(self, obj):
        self.stop()
        Vista("partes_por_empleado").run()
        self.run()

    def abrir_lotes_finca(self, obj):
        self.stop()
        Vista("lotes_por_finca").run()
        self.run()

    def abrir_ayudantes_empleado(self, obj):
        self.stop()
        Vista("AyudantesxEmpleado").run()
        self.run()

    def abrir_cheques_semana(self, obj):
        self.stop()
        Vista("cheques_de_la_semana").run()
        self.run()

    def abrir_gastos_comida(self, obj):
        self.stop()
        Vista("gastos_en_comida").run()
        self.run()

    def abrir_proovedores_agroquimicos(self, obj):
        self.stop()
        Vista("proveedores_de_agroquimicos").run()
        self.run()
    def abrir_fincas_limones(self, obj):
        self.stop()
        Vista("fincas_con_limones").run()
        self.run()


