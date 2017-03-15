import os
import time
import random

import Laberinto
import Hormiga
import Colonia


lab=Laberinto.Laberinto()


colony=Colonia.Colonia(10,10,lab)

for i in range(1):
    colony.avanzarHormigas()


for i in range(10):
    print colony.estadoHormiga(i)
