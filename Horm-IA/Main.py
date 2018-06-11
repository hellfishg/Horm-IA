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

arg=None
menuprincipal= A_MenuPrincipal.MenuPrincipal(arg)



##########################################################################
