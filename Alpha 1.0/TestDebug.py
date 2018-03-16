import os
import time
import random

import Laberinto
import Hormiga
import Colonia
import Interfaz

lab=Laberinto.Laberinto()


colony=Colonia.Colonia(10,20,lab)

for i in range(300):
    colony.avanzarHormigas()


for i in range(10):
    print colony.estadoHormiga(i)

#inter=Interfaz.Interfaz(lab)
