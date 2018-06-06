import os
import copy
import pickle

from Menu.Ventana import Ventana
import Menu.A_MenuPrincipal
# from CreadorLab1 import CreadorLab1
# from CreadorLab2 import CreadorLab2

class GeneradorDeLabs (Ventana):
    def __init__(self,arg,menuAnterior,algoritmo):
        super().__init__(menuAnterior,arg)
        self.algoritmo= algoritmo
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        rand=True

        while rand:
            os.system("clear")
            for i in range(32):
                os.system("echo")
            backupAlgoritmo= copy.deepcopy(self.algoritmo)

            self.imprimirDeArchivo(0,0,"Menu/labAlgoritmo.txt")
            backupAlgoritmo.crearLaberinto()

            #aca grafica lab
            mLab= backupAlgoritmo.matriz
            self.graficarLaberinto(mLab,3,3)

            elecc=input(' Eleccion: ')
            respuesta=self.procesarEleccion(elecc.upper(),mLab)

            if respuesta == None:
                #Error de comando invalido
                self.comandoInvalido(self.imprimirMenu)
            elif respuesta == True:
                pass
            elif respuesta == False:
                rand=False

##############################################################################
    def procesarEleccion(self,elec,mLab):
        if elec == 'A':
            return True
        if elec == 'B':
            self.copiarEnArchivo(mLab)
            #!salir al menu principal
            menuPrincipal=Menu.A_MenuPrincipal.MenuPrincipal(self.arg)
            return False
        if elec == 'C':
            self.menuAnterior.imprimirMenu()
            return False
        if elec == 'D':
            menuPrincipal=Menu.A_MenuPrincipal.MenuPrincipal(self.arg)
            return False

        return None
##############################################################################
    def copiarEnArchivo(self,mLab):
        os.system("clear")
        for i in range(34):
            os.system("echo")

        elecc=input('  Con que nombre quiere guardar el laberinto?: ')
        matrizDeLabs=list()

        try:
            pkl_file = open('BDLabs.pkl', 'rb')
            matrizDeLabs = pickle.load(pkl_file)
            pkl_file.close()
        except:
            pass

        pkl_file = open('BDLabs.pkl', 'wb')

        elemento= [str(elecc),mLab]
        matrizDeLabs.append(elemento)

        pickle.dump(matrizDeLabs, pkl_file)
        pkl_file.close()

        os.system("clear")
        print("ARCHIVO GUARDADO CON EXITO!")
        input('OPRIMA CUALQUIER TECLA PARA CONTINUAR')
##############################################################################
##############################################################################
