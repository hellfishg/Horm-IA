import random


class Hormiga:

    def __init__(self,nombre,ciclo,posicion,iDLab):
        self.__nombre=nombre
        self.__ciclo=ciclo
        self.__posicion=posicion
        self.iDLab=iDLab
        self.__memoria=list()


###############################################################################

    def estado(self):
        return self.__ciclo

###############################################################################

    def explorar(self):

        aux=False
        while aux == False:
            randElecc=self.__eleccion()
            aux=self.iDLab.permitePaso(self.__posicion,randElecc)

        self.__posicion=aux
        self.__ciclo=self.__ciclo-1
        self.__memoria.append(randElecc)


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
