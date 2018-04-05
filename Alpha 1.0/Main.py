#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import random
import sys

import Laberinto
import Hormiga
import Colonia
import Interfaz

os.system('clear')
lab=Laberinto.Laberinto()
colony=Colonia.Colonia(10,20,lab)
inter=Interfaz.Interfaz(lab,colony)

for i in range(600): #ciclos de vida de la colonia

    colony.avanzarHormigas()
    inter.graficarDescripcionHormigasVivas()
    inter.graficarLaberinto()
    inter.graficarHormigas()
    time.sleep(3)
