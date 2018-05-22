import os

from Menu.Ventana import Ventana

class CatalogoLabs (Ventana):
    def __init__(self,arg,menuAnterior):
        super().__init__(menuAnterior,arg)
        self.imprimirMenu()
##############################################################################
