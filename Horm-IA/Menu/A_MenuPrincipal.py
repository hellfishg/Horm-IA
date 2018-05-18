#by hellfishg -- 14/05/2018
import os

from Menu.Ventana import Ventana
from Menu.B_MenuCreadorLab import CreadorLab
from Menu.C_ComenzarColonia import ComenzarColonia
from Menu.D_Estadisticas import Estadisticas
from Menu.E_Instrucciones import Instrucciones

class MenuPrincipal (Ventana):
    def __init__(self,arg):
        super().__init__(self,arg)
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        pass
##############################################################################
    def imprimirMenu(self):
        os.system("clear")
        for i in range(23):
            os.system("echo")

        self.imprimirMarquesina()
        self.imprimirDeArchivo(0,7,"Menu/menuPrincipal.txt")

        aux=input(' Eleccion: ')

        if self.procesarEleccion(aux.upper()) == False:
            #Error de comando invalido
            pass
##############################################################################
    def procesarEleccion(self,elec):

        if elec == 'A':
            creadorLab=CreadorLab(self.arg,self)
        if elec == 'B':
            catalogoLabs=CatalogoLabs(self.arg,self)
        if elec == 'C':
            comenzarColonia=ComenzarColonia(self.arg,self)
        if elec == 'D':
            estadisticas=Estadisticas(self.arg,self)
        if elec == 'E':
            instrucciones=Instrucciones(self.arg,self)
        if elec == 'F':
            os._exit

        return True

##############################################################################
##############################################################################
