#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgitb
import os
import time
import random
import sys

import Laberinto
import Hormiga
import Colonia
import Interfaz

cgitb.enable(format="text")#llama la funcion para el manejo de exepcion no default.
lab=Laberinto.Laberinto()
colony=Colonia.Colonia(20,60,lab)
inter=Interfaz.Interfaz(lab,colony,5000)

for i in range(5000): #ciclos de vida de la colonia

    os.system('clear')
    colony.avanzarHormigas()
    inter.graficarDescripcionHormigasVivas()
    inter.graficarLaberinto()
    inter.graficarHormigas()
    time.sleep(0.1)


# hormigas=colony.getHormigasEnMatriz()
# print (hormigas[0].obtenerMemoria())
# print (hormigas[1].obtenerMemoria())
# hormigas[7].transferirFeromonas(hormigas[1].obtenerMemoria())

###################3
