import os

from Menu.Ventana import Ventana

class Instrucciones (Ventana):
    def __init__(self,arg,menuAnterior):
        super().__init__(menuAnterior,arg)
        self.imprimirMenu()
##############################################################################
        def imprimirMenu(self):
            os.system("clear")
            for saltosDeLineas in range(10):
                os.system("echo")
            print("Aca van las instrucciones del programa...")
            input('OPRIMA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL')
            self.menuAnterior.imprimirMenu()
            
##############################################################################
##############################################################################
##############################################################################
