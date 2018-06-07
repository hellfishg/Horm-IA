import os
import pickle

from Menu.Ventana import Ventana
from Menu.ACA_ComenzarColonia import ComenzarColonia

class ElegirLaberinto (Ventana):
    def __init__(self,arg,menuAnterior):
        super().__init__(menuAnterior,arg)
        self.matrizDeLabs=list()
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        rand= True
        i=0
        maximo=0
        self.cargarBDLabs()
        if self.matrizDeLabs == None:
            rand = False
        else:
            maximo = len(self.matrizDeLabs)-1

        while rand:
            if i>maximo:
                i=i-1
            if i<0:
                i=0

            os.system("clear")
            mLab=self.matrizDeLabs[i]
            self.imprimirDeArchivo(0,0,"Menu/elegirLabs.txt")

            for saltosDeLineas in range(23):
                os.system("echo")
            print("|                      "+str(mLab[0]))


            self.graficarLaberinto(mLab[1],3,3)

            for saltosDeLineas in range(10):
                os.system("echo")

            elecc=input(' Eleccion: ')
            respuesta=self.procesarEleccion(elecc.upper(),i)

            if respuesta == None:
                #Error de comando invalido
                self.comandoInvalido(self.imprimirMenu)
            if respuesta == "False":
                rand=False
            else:
                i=respuesta

##############################################################################
    def cargarBDLabs(self):
        try:
            pkl_file = open('BDLabs.pkl', 'rb')
            self.matrizDeLabs = pickle.load(pkl_file)
            pkl_file.close()
        except:
            os.system("clear")
            print("NO HAT LABERINTOS GUADADOS!")
            input('OPRIMA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL')
            self.menuAnterior.imprimirMenu()
            return False

        return True

##############################################################################
    def procesarEleccion(self,elec,i):
        if elec == 'A':
            i=i+1
            return i
        if elec == 'B':
            i=i-1
            return i
        if elec == 'C':
            laberinto=self.matrizDeLabs[i]
            comenzarColonia=ComenzarColonia(self.arg,self.menuAnterior,laberinto)
            return "False"
        if elec == 'D':
            self.menuAnterior.imprimirMenu()
            return "False"

        return None

##############################################################################

##############################################################################
