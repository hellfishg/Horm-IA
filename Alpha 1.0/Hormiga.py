import random


class Hormiga:

    def __init__(self,nombre,ciclo,posicion,iDLab):
        self.nombre=nombre
        self.ciclo=ciclo
        self.posicion=posicion
        self.iDLab=iDLab
        self.memoria=list()


###############################################################################




###############################################################################

    def explorar(self):

        aux=False
        while aux == False:
            randElecc=self.__eleccion()
            aux=self.iDLab.permitePaso(self.posicion,randElecc)

        self.posicion=aux
        self.ciclo=self.ciclo-1
        self.memoria.append(randElecc)


###############################################################################

    def __eleccion(self):
        aux= random.randint(0,3)

        if aux == 0:
            dire= "ar"
        if aux == 1:
            dire= "de"
        if aux == 2:
            dire= "ab"
        if aux == 3:
            dire= "iz"

        return dire


###############################################################################





###############################################################################



###############################################################################



###############################################################################