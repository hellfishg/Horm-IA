import os
import time

from Menu.Ventana import Ventana
import Log
import Hormiga
import Colonia
import Laberinto
import Interfaz

class ComenzarColonia (Ventana):
    def __init__(self,arg,menuAnterior,laberinto):
        super().__init__(menuAnterior,arg)
        self.laberinto=laberinto[1]
        self.nombreLab=laberinto[0]
        self.salidaLab=laberinto[2]
        self.imprimirMenu()
##############################################################################
    def imprimirMenu(self):
        os.system("clear")

        aux=None
        verificar=True
        setea=list()

        while verificar:
        	aux=input('Introduce la cantidad de ciclos que durara el programa: ')
        	try:
        		int(aux)
        		verificar=False
        	except:
        		print("Tiene que ser en numeros enteros!")
        setea.append(int(aux))
        verificar=True
    ############################################################################
        while verificar:
        	aux=input('Introduce el tiempo que dura un movimiento de hormiga por pantalla (Recomendado 1): ')
        	try:
        		float(aux)
        		verificar=False
        	except:
        		print("Tiene que ser en numeros enteros!")
        setea.append(float(aux))
    ############################################################################
        verificar=True
        while verificar:
        	aux=input('Introduce la cantidad de ciclos de cada hormiga: ')
        	try:
        		int(aux)
        		verificar=False
        	except:
        		print("Tiene que ser en numeros enteros!")
        setea.append(int (aux))
    ############################################################################
        verificar=True
        while verificar:
        	aux=input('Introduce cuantas hormigas vivas habra al mismo tiempo: ')
        	try:
        		int(aux)
        		verificar=False
        	except:
        		print("¡Tiene que ser en numeros enteros!")
        setea.append(int (aux))
    ############################################################################
        verificar=True
        while verificar:
        	aux=input('¿Las hormigas que llegan a la meta quedaran en la lista?(s/n): ')
        	if aux== 's' or aux== 'n':
        		verificar=False
        	else:
        		print("¡Tiene que ser s o n!")
        setea.append(aux)

        #iniciar la beta con los parametros.

##############################################################################
        log=Log.Log()
        lab=Laberinto.Laberinto(self.laberinto,[0,0],self.salidaLab)

        colony=Colonia.Colonia(setea[3],setea[2],lab,log,setea[4])
        inter=Interfaz.Interfaz(lab,colony,setea[0])

        for i in range(setea[0]): #ciclos de vida de la colonia

            os.system('clear')
            colony.avanzarHormigas()
            inter.graficarDescripcionHormigasVivas()
            inter.graficarLaberinto()
            inter.graficarHormigas()
            time.sleep(setea[1])

        log.guardarEnArchivo()
        inter.devolverInforme(log.informe)

##############################################################################
##############################################################################
##############################################################################
