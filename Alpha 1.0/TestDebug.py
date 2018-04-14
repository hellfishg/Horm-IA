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
import Log

cgitb.enable(format="text")#llama la funcion para el manejo de exepcion no default.
log=Log.Log()
lab=Laberinto.Laberinto()
colony=Colonia.Colonia(20,60,lab,log)
inter=Interfaz.Interfaz(lab,colony,5000)

for i in range(5000): #ciclos de vida de la colonia

    os.system('clear')
    colony.avanzarHormigas()
    inter.graficarDescripcionHormigasVivas()
    inter.graficarLaberinto()
    inter.graficarHormigas()
    time.sleep(0.0)

log.guardarEnArchivo()
inter.devolverInforme(log.informe)



###################3
