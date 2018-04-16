import random
import Hormiga

class Colonia:

    def __init__(self,cantidad,ciclos,laberinto,log):

        self.__cantidad=cantidad
        self.ciclos=ciclos
        self.laberinto=laberinto
        self.log=log
        self.hormigas=list()
        self.feromonasColonia=list()
        self.feromonaNueva=None
        self.__crearColonia()


###############################################################################
    def avanzarHormigas(self):
        #Avanza un ciclo a todas las hormigas recibiendo un timpo de delay del sistema.
        self.__comprobarEstadoDeColonia()#busca hormigas muertas y remplaza.

        for i in range(self.__cantidad):
            if self.hormigas[i].feroPosition == None:#explorar sin feromonas.

                if self.hormigas[i].explorar() == False and self.hormigas[i].llego == False:#si llego a la colonia ida y vuelta.
                    self.log.agregarInforme(self.hormigas[i])
                    self.hormigas[i].llego=True
                    self.feromonaNueva = self.hormigas[i].transferirFeromonas()
                    self.__elegirMejorFeromona()
                    self.hormigas[i].ciclo=0#sacar esto para guardar la hormiga o dejarlo, la mata y remplaza

            else:#explorar con feromonas.
                self.hormigas[i].explorarConFeromonas()


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
        #Chequea el estado de vida de las colonias.y si estan muertas las remplaza.ademas crea la nueva camada con las feromonas recibidas.
        for i in range(self.__cantidad):

            if self.hormigas[i].ciclo <= 0:
                if len(self.feromonasColonia) != 0:#camada con feromonas.
                    self.__procrearHormiga(i)
                    I= len(self.feromonasColonia)-1#obtiene la ultima feromona
                    self.hormigas[i].recibirFeromonas(self.feromonasColonia[I])

                else:#camada nueva.
                    self.__procrearHormiga(i)

###############################################################################
    def __crearColonia(self):
        #Crea inicialmente una camada de hormigas.
        for i in range(self.__cantidad):
            nombre=self.nombrarHormiga()
            self.hormigas.append(Hormiga.Hormiga(nombre,self.ciclos,[0,0],self.laberinto))

###############################################################################
    def __procrearHormiga(self,i):
        #Crea una homiga nueva.
        nombre=self.nombrarHormiga()
        self.hormigas[i]=Hormiga.Hormiga(nombre,self.ciclos,[0,0],self.laberinto)

###############################################################################
    def estadoHormiga(self,i):
        #DEPRECADO?
        estado=(self.hormigas[i].nombre,self.hormigas[i].posicion)
        return estado

###############################################################################
    def __elegirMejorFeromona(self):
        #se encarga de comparar la nueva feromona obtenida vs la de la colonia en uso.
        i=len(self.feromonasColonia)-1

        if len(self.feromonasColonia) < 1:
            self.feromonasColonia.append(self.feromonaNueva)

        else:
            if len(self.feromonaNueva) < len(self.feromonasColonia[i]):
                self.feromonasColonia.append(self.feromonaNueva)


###############################################################################
    def getHormigasEnMatriz(self):
        return self.hormigas
###############################################################################
    def getCantidad(self):
        return self.__cantidad
###############################################################################
