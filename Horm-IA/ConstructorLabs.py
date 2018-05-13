#by hellfishg 13/05/2018

class ConstructorLabs:
    #clase padre para ser heredada por los constructores de laberintos.

    def __init__(self,largo,alto):
        self.X=largo
        self.Y=alto
        self.matriz=[[["bloq"for a in range(4)]for b in range(self.Y)]for c in range(self.X)]

###############################################################################
    def crearLaberinto(self):
    #funcion principal para implementar-override.
        pass
###############################################################################
    def cavarCamino(self,dire,posActual):
        #Crea un camino segun la eleccion, y regresa la proxima posicion
        direcciones=["ar","de","ab","iz"]

        x=posActual[0]
        y=posActual[1]
        z=direcciones.index(dire)

        self.matriz[x][y][z]=dire #Graba el cambio en el laberinto.

        #Necesita habilitar el camino tambien en la otra posicion:
        direSig=self.invertirDire(dire)
        xySig=self.siguientePosicion(dire,posActual)
        zSig=direcciones.index(direSig)

        self.matriz[xySig[0]][xySig[1]][zSig]=direSig #Graba la salida en la sig.posicion

        return xySig
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
    def chequearAglomeracion(self):
    	#Esta es la funcion de facu
    	pass
###############################################################################
###############################################################################
###############################################################################
