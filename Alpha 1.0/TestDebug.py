import os
import time
import random
import sys

import Laberinto
import Hormiga
import Colonia
import Interfaz

lab=Laberinto.Laberinto()
'''

'''
colony=Colonia.Colonia(10,20,lab)

for i in range(300):
    colony.avanzarHormigas()


for i in range(10):
    print colony.estadoHormiga(i)
'''
<<<<<<< HEAD

inter=Interfaz.Interfaz(lab)
=======

inter=Interfaz.Interfaz(lab)

>>>>>>> d71e2420dc9a830626e20a8034e0845f42e5e496
