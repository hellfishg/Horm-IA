import random

class Hormiga:

    def __init__(self,nombre,ciclo,posicion,laberinto):
        self.nombre=nombre
        self.ciclo=ciclo
        self.posicion=posicion
        self.laberinto=laberinto
        self.memoria=list()


###############################################################################
    def __chequearMeta__(self):
        meta=[6,2]
        if meta==self.posicion:
            return False
        else:
            return True

###############################################################################
    def explorar(self):

        if self.__chequearMeta__():

            aux=False
            while aux == False:
                randElecc=self.__eleccion()
                aux=self.laberinto.permitePaso(self.posicion,randElecc)

            self.posicion=aux
            self.ciclo-=1
            self.memoria.append(randElecc)

###############################################################################
    def __eleccion(self):
        matrizDireciones = ["ar","de","ab","iz"]
        aux= random.randint(0,3)

        return matrizDireciones[aux]

###############################################################################



###############################################################################



###############################################################################



###############################################################################
