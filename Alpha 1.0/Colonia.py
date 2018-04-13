import random
import Hormiga

class Colonia:

    def __init__(self,cantidad,ciclos,laberinto):

        self.__cantidad=cantidad
        self.ciclos=ciclos
        self.laberinto=laberinto
        self.hormigas=list()
        #self.__nomNum=1
        self.__crearColonia()


###############################################################################
    def avanzarHormigas(self):
        #Avanza un ciclo a todas las hormigas recibiendo un timpo de delay del sistema.
        self.__comprobarEstadoDeColonia()#busca hormigas muertas y remplaza.

        for i in range(self.__cantidad):
            self.hormigas[i].explorar()

###############################################################################
    def __crearColonia(self):
        #Crea inicialmente una camada de hormigas.
        for i in range(self.__cantidad):
            nombre=self.nombrarHormiga()
            self.hormigas.append(Hormiga.Hormiga(nombre,self.ciclos,[0,0],self.laberinto))

            #self.__nomNum+=1
###############################################################################
    def nombrarHormiga(self):
        matrizNom=list()
        archivo=open("../Textos/NomHormiga.txt", "r")

        for nombre in archivo.readlines():
            matrizNom.append(nombre.rstrip('\n'))
            archivo.close()
            num=random.randint(0,len(matrizNom)-1)

        return matrizNom[num]

###############################################################################
    def __comprobarEstadoDeColonia(self):
        #Chequea el estado de vida de las colonias.y si estan muertas las remplaza.
        for i in range(self.__cantidad):

            if self.hormigas[i].ciclo <= 0:
                self.__procrearHormiga(i)

###############################################################################
    def __procrearHormiga(self,i):
        #Crea una homiga nueva.
        nombre=self.nombrarHormiga()
        self.hormigas[i]=Hormiga.Hormiga(nombre,self.ciclos,[0,0],self.laberinto)

        #self.__nomNum+=1

###############################################################################
    def estadoHormiga(self,i):
        estado=(self.hormigas[i].nombre,self.hormigas[i].posicion)
        return estado

###############################################################################
    def getHormigasEnMatriz(self):
        return self.hormigas

###############################################################################
    def getCantidad(self):
        return self.__cantidad
###############################################################################
