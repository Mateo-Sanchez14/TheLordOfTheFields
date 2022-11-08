import sys
from principal.vistas.VentanaPrincipal import VentanaPrincipal
from principal.vistas.VentanaPrincipalKiviMD import DemoApp
from conector.controlador.conector import Conector


def __main__():
    # VentanaPrincipal().run()
    lista = Conector().select("SELECT * FROM CLIENTE")
    print(lista)
    VentanaPrincipal().run()
    #DemoApp().run()



if __name__ == "__main__":
    __main__()
