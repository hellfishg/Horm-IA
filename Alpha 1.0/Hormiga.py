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
        self.llego=False
        self.feroPosition=None

###############################################################################
    def __chequearMeta(self):

        if self.posicion == self.__metaActual:
            if len(self.__feromonas) < 1:#llego a al recurso:
                self.__feromonas = self.__memoria
                self.__memoria=list()
                self.__metaActual= self.laberinto.getEntrada()
                return True
            else:#llego a la colonia ida y vuelta:
                #comparar si la memoria es menor a las feromonas mejora el algoritmo:
                if len(self.__memoria) < len(self.__feromonas):
                    self.__feromonas= self.__memoriaReversa(self.__memoria)

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

            return True
        else:
            return False

###############################################################################
    def explorarConFeromonas(self):
        #1)chequer hacia donde va.
        #2)avanzar usando las feromonas.
        #3)chequear cuando se llego a la meta.
        #4)volver de forma normal.
        if self.posicion != self.__metaActual:

            i=self.feroPosition
            aux=self.laberinto.permitePaso(self.posicion, self.__feromonas[i])
            self.posicion=aux

            self.ciclo-=1
            self.feroPosition+=1
            self.__memoria.append(self.__feromonas[i])

        else:
            self.feroPosition=None
            self.__feromonas=list()

###############################################################################
    def __eleccion(self):
        matrizDireciones = ["ar","de","ab","iz"]
        aux= random.randint(0,3)

        return matrizDireciones[aux]

###############################################################################
    def __memoriaReversa(self,memo):
        #invierte el las desiciones tomadas en memoria tanto de direccion como de orden.
        memoria=memo
        memoria.reverse()
        aux=""
        for i in range(len(memoria)):
            if memoria[i] == "de":
                aux="iz"
            if memoria[i] == "iz":
                aux="de"
            if memoria[i] == "ar":
                aux="ab"
            if memoria[i] == "ab":
                aux="ar"

            memoria[i]=aux

        return memoria

###############################################################################
    def obtenerMemoria(self):
        return self.__memoria

###############################################################################
    def transferirFeromonas(self):
        return self.__feromonas

###############################################################################
    def recibirFeromonas(self,fero):
        self.__feromonas=fero
        self.feroPosition=0

###############################################################################
    def __repr__(self):
        return "+Hormiga: {} en {} /Vida restante: {}'\n' |->Feromona: {}'\n'".format(self.nombre,self.posicion,self.ciclo,self.__feromonas)

###############################################################################
