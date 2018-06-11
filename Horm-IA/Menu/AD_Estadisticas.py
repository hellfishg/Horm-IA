import os

from Menu.Ventana import Ventana

class Estadisticas (Ventana):
    def __init__(self,arg,menuAnterior):
        super().__init__(menuAnterior,arg)
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        os.system("clear")
        try:
            archivo=open("Informe.txt", "r")
            for log in archivo.readlines():
                print(log)
            archivo.close()
            input('OPRIMA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL')
            self.menuAnterior.imprimirMenu()
        except:
            for saltosDeLineas in range(15):
                os.system("echo")
            print("NO HAY LOGS GUARDADOS!")
            input('OPRIMA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL')
            self.menuAnterior.imprimirMenu()

##############################################################################
##############################################################################
##############################################################################
