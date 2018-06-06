import os

from Menu.Ventana import Ventana
from Menu.AAB_GeneradorDeLabs import GeneradorDeLabs
from CreadorLab1 import CreadorLab1
from CreadorLab2 import CreadorLab2

class CreadorLab (Ventana):
    def __init__(self,arg,menuAnterior):
        super().__init__(menuAnterior,arg)
        self.imprimirMenu()

##############################################################################
    def imprimirMenu(self):
        os.system("clear")
        for i in range(19):
            os.system("echo")

        self.imprimirMarquesina()
        self.imprimirDeArchivo(0,7,"Menu/menuCreadorLab.txt")

        aux=input(' Eleccion: ')

        if self.procesarEleccion(aux.upper()) == None:
            #Error de comando invalido
            self.comandoInvalido(self.imprimirMenu)

##############################################################################
    def procesarEleccion(self,elec):
        if elec == 'A':
            self.algoritmoLab1()
            return True
        if elec == 'B':
            self.algoritmoLab2()
            return True
        if elec == 'C':
            self.menuAnterior.imprimirMenu()
            return True

        return None
##############################################################################
    def algoritmoLab1(self):
        os.system("clear")
        #los ciclos de tiempo
        #las entradas y salidas.

        auxElec=list()

        #Mas adelante se podria implemetar setear la salida y la entra.
        print("Los ciclos representan cuando tiempo el algoritmo trabaja antes de forzarlo a llegar a la salida. RECOMENDADO 100")

        auxElec.append(input(' Cantidad de ciclos: '))

        algoritmo=CreadorLab1(10,10,[0,0],"de",auxElec[0])
        generadorDeLabs=GeneradorDeLabs(self.arg,self,algoritmo)
        #enviar a la ventana de vista de laberintos.

##############################################################################
    def algoritmoLab2(self):
        os.system("clear")
        auxElec=list()
        auxElec.append(input(' Cantidad de iteraciones de ramas: '))

        algoritmo=CreadorLab2(10,10,[0,0],"de",auxElec[0])
        generadorDeLabs=GeneradorDeLabs(self.arg,self,algoritmo)

##############################################################################
