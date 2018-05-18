#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgitb
import os
import time
import random
import sys

import CreadorLab1
import CreadorLab2
import Laberinto
import Hormiga
import Colonia
import Interfaz
import Log
import MenuInicio

cgitb.enable(format="text")#llama la funcion para el manejo de exepcion no default.

from Menu import A_MenuPrincipal

arg=2
pepe= A_MenuPrincipal.MenuPrincipal(arg)

#time.sleep(10)



# setea=MenuInicio.pantalla()
# print(setea)
# log=Log.Log()
# #generar el laberinto aca:
#
# #creador= CreadorLab1.CreadorLab1(10,10,[0,0],"de",100)
# creador= CreadorLab2.CreadorLab2(10,10,[0,0],"de",600)
#
# creador.crearLaberinto()
# lab=Laberinto.Laberinto(creador.matriz,[0,0],creador.salidaCreada)
#
#
# colony=Colonia.Colonia(setea[3],setea[2],lab,log,setea[4])
# inter=Interfaz.Interfaz(lab,colony,setea[0])
#
# for i in range(setea[0]): #ciclos de vida de la colonia
#
#     os.system('clear')
#     colony.avanzarHormigas()
#     inter.graficarDescripcionHormigasVivas()
#     inter.graficarLaberinto()
#     inter.graficarHormigas()
#     time.sleep(setea[1])
#
# log.guardarEnArchivo()
# inter.devolverInforme(log.informe)
# print(creador.salidaCreada)

##########################################################################
