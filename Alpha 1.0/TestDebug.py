import os
import time
import random
import sys

import Laberinto
import Hormiga
import Colonia
import Interfaz

lab=Laberinto.Laberinto()


colony=Colonia.Colonia(10,20,lab)

for i in range(300):    
	colony.avanzarHormigas()
	inter=Interfaz.Interfaz(lab)

	for j in range(10):
		print colony.estadoHormiga(j)

	print ("------------------")	
	time.sleep(0.5)

	




