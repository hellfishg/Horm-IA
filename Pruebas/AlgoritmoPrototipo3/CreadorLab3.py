import random

class CreadorLab3:

    def __init__(self,largo,alto,entrada,salida,ciclos):
        self.X=largo
        self.Y=alto
        self.ciclos=ciclos
        self.salida=salida
        self.posicionActual=entrada

        self.treintaPorciento= int(ciclos * 0.30)
        self.diezPorciento= int(ciclos * 0.10)

        self.matriz=[[["bloq"for a in range(4)]for b in range(self.Y)]for c in range(self.X)]

###############################################################################
    def crearCaminoPrincipal(self):
        #Crea el camino principal por la matriz de laberinto.
        restricciones = self.controlarBordes(self.posicionActual)

        while self.noEstarEnLaSalida(restricciones):
            dirRand = self.aleatoriedadPorCiclos(restricciones)
            self.posicionActual = self.cavarCamino(dirRand)
            restricciones = self.controlarBordes(self.posicionActual)
            self.ciclos-=1

###############################################################################
    def noEstarEnLaSalida(self,restricciones):
        #Regresa true o false si se esta en una pared de salida:
        try:
            restricciones.index(self.salida)
            return False
        except ValueError:
            return True
###############################################################################
    def controlarBordes(self,pos):
        #funcion dedicada a prohibir salirse de los bordes de la matriz
        x=pos[0]
        y=pos[1]
        restricciones=list()

        if x == 0:
            restricciones.append("iz")
        if y == 0:
            restricciones.append("ar")
        if x ==(self.X)-1:
            restricciones.append("de")
        if y ==(self.Y)-1:
            restricciones.append("ab")

        return restricciones
###############################################################################
    def aleatoriedadPorCiclos(self,restricciones):
        #reduce la aleatoriedad segun se va quedando sin ciclos.
        direccionesRand=["ar","de","ab","iz"]

        if self.ciclos <= self.treintaPorciento:
            direccionesRand.append(self.salida)
        if self.ciclos <= self.diezPorciento:
            direccionesRand.append(self.salida)

        #Aca borra las restricciones de las probabilidades
        if restricciones != None:#si no hay restricciones
            for i in range(len(restricciones)):
                direccionesRand.remove(restricciones[i])

        i=random.randint(0,len(direccionesRand)-1)
        return direccionesRand[i]
###############################################################################
    def cavarCamino(self,dire):
        #Crea un camino segun la eleccion, y regresa la proxima posicion
        direcciones=["ar","de","ab","iz"]

        x=self.posicionActual[0]
        y=self.posicionActual[1]
        z=direcciones.index(dire)

        self.matriz[x][y][z]=dire #Graba el cambio en el laberinto.

        #Necesita habilitar el camino tambien en la otra posicion:
        direSig=self.invertirDire(dire)
        xySig=self.siguientePosicion(dire,self.posicionActual)
        zSig=direcciones.index(direSig)

        self.matriz[xySig[0]][xySig[1]][zSig]=direSig#Graba la salida en la sig.posicion

        return xySig
###############################################################################
    def siguientePosicion(self,dire,xy):
    	if dire =="ar":
    		xy[1]-=1
    	if dire =="de":
    		xy[0]+=1
    	if dire =="ab":
    		xy[1]+=1
    	if dire =="iz":
    		xy[0]-=1
    	return xy
###############################################################################
    def invertirDire(self,dire):
        if dire =="ar":
        	z="ab"
        if dire =="de":
        	z="iz"
        if dire =="ab":
        	z="ar"
        if dire =="iz":
        	z="de"
        return z
###############################################################################
    def ramificar(self):
        #crea aleatoriamente ramificaciones en el camino principal
        #!!balancear
        pass
###############################################################################
###############################################################################
###############################################################################
###############################################################################
