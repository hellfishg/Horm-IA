import random

class Hormiga:

    def __init__(self,nombre,ciclo,posicion,laberinto):
        self.nombre=nombre
        self.ciclo=ciclo
        self.posicion=posicion
        self.laberinto=laberinto
        self.__metaActual=laberinto.getSalida()
        self.__memoria=list()
        self.__feromonas=list()

###############################################################################
    def __chequearMeta(self):

        if self.__metaActual == self.posicion and self.__metaActual == self.laberinto.getSalida():

            self.transferirFeromonas(self.obtenerMemoria())

            return False
        else:
            return True

###############################################################################
    def explorar(self):
        if self.__chequearMeta():
            aux=False
            while aux == False:
                randElecc=self.__eleccion()
                aux=self.laberinto.permitePaso(self.posicion,randElecc)

            self.posicion=aux
            self.ciclo-=1
            self.__memoria.append(randElecc)

###############################################################################
    def __eleccion(self):
        matrizDireciones = ["ar","de","ab","iz"]
        aux= random.randint(0,3)

        return matrizDireciones[aux]

###############################################################################
    def explorarConFeromonas(self):
        #no esta terminado
        if self.__chequearMeta__():


            self.posicion=aux
            self.ciclo-=1
            self.__memoria.append(randElecc)

###############################################################################
    def obtenerMemoria(self):
        return self.__memoria

###############################################################################
    def transferirFeromonas(self,memoria):
        self.__feromonas = memoria
        self.__feromonas.reverse()

###############################################################################


###############################################################################
