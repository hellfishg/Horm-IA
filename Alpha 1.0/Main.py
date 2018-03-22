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
inter=Interfaz.Interfaz(lab)

for i in range(600):

    colony.avanzarHormigas()

    for i in range(10):
        print (colony.estadoHormiga(i))

    print ("------------------------------")

    inter.graficarLaberinto()
    inter.graficarHormigas( colony.getHormigasEnMatriz())
    time.sleep(3)
