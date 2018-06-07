#by hellfishg -- 14/05/2018
import os

from Menu.Ventana import Ventana
from Menu.AA_MenuCreadorLab import CreadorLab
from Menu.AB_CatalogoLabs import CatalogoLabs
from Menu.AC_ElegirLaberinto import ElegirLaberinto
from Menu.AD_Estadisticas import Estadisticas
from Menu.AE_Instrucciones import Instrucciones

class MenuPrincipal (Ventana):
    def __init__(self,arg):
        super().__init__(self,arg)
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        os.system("clear")
        for i in range(23):
            os.system("echo")

        self.imprimirMarquesina()
        self.imprimirDeArchivo(0,7,"Menu/menuPrincipal.txt")

        aux=input(' Eleccion: ')

        if self.procesarEleccion(aux.upper()) == None:
            #Error de comando invalido
            self.comandoInvalido(self.imprimirMenu)

##############################################################################
    def procesarEleccion(self,elec):

        if elec == 'A':
            creadorLab=CreadorLab(self.arg,self)
            return True
        if elec == 'B':
            catalogoLabs=CatalogoLabs(self.arg,self)
            return True
        if elec == 'C':
            comenzarColonia=ElegirLaberinto(self.arg,self)
            return True
        if elec == 'D':
            estadisticas=Estadisticas(self.arg,self)
            return True
        if elec == 'E':
            instrucciones=Instrucciones(self.arg,self)
            return True
        if elec == 'F':
            os._exit
            return True

        return None

##############################################################################
##############################################################################
