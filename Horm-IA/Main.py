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
import MenuInicio

cgitb.enable(format="text")#llama la funcion para el manejo de exepcion no default.

setea=MenuInicio.pantalla()
print(setea)
log=Log.Log()
lab=Laberinto.Laberinto()
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

##########################################################################
