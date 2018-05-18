#by hellfishg -- 10/05/2018

import random
from ConstructorLabs import ConstructorLabs

class CreadorLab1 (ConstructorLabs):

    def __init__(self,largo,alto,entrada,salida,ciclos):
        super().__init__(largo,alto)
        self.ciclos=ciclos
        self.salida=salida
        self.posicionActual=entrada

        self.treintaPorciento= int(ciclos * 0.30)
        self.diezPorciento= int(ciclos * 0.10)

        self.salidaCreada=None

###############################################################################
    def crearLaberinto(self):
        #Crea el camino principal por la matriz de laberinto.
        restricciones = self.controlarBordes(self.posicionActual)
        while self.noEstarEnLaSalida(restricciones):
            dirRand = self.aleatoriedadPorCiclos(restricciones)
            self.posicionActual = self.cavarCamino(dirRand,self.posicionActual)
            restricciones = self.controlarBordes(self.posicionActual)
            self.ciclos-=1

        self.salidaCreada=self.posicionActual
###############################################################################
    def noEstarEnLaSalida(self,restricciones):
        #Regresa true o false si se esta en una pared de salida:
        try:
            restricciones.index(self.salida)
            return False
        except ValueError:
            return True
###############################################################################
    def aleatoriedadPorCiclos(self,restricciones):
        #reduce la aleatoriedad segun se va quedando sin ciclos.
        direccionesRand=["ar","de","ab","iz"]

        if self.ciclos <= self.treintaPorciento:
            direccionesRand.append(self.salida)
        if self.ciclos <= self.diezPorciento:
            direccionesRand.append(self.salida)

        #Aca borra las restricciones de las probabilidades
        if restricciones != None:#si hay restricciones
            for i in range(len(restricciones)):
                direccionesRand.remove(restricciones[i])

        i=random.randint(0,len(direccionesRand)-1)
        return direccionesRand[i]
###############################################################################
###############################################################################
