import random

class CreadorLab2:
	def __init__(self,largo,alto,entrada,salida,separacion):
		self.X=largo
		self.Y=alto
		self.posicionActual=entrada
		self.salida=salida
		self.separacion=separacion
		self.direContraria=self.invertirDire(salida)#no esta bien hecho
		self.matriz=[[["bloq"for a in range(4)]for b in range(self.Y)]for c in range(self.X)]
###############################################################################
	def crearLaberinto(self):
		final=True
		while final:
			restricciones= self.controlarBordes(self.posicionActual)
			restricciones= self.comprobarDireccionContraria(restricciones,self.direContraria)
			direccionesACavar= self.decideCaminos(restricciones)
			final=self.avanzarCaminos(direccionesACavar)
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
	def comprobarDireccionContraria(self,restricciones,direCont):
	#comprueba si la direccion contraria esta o no en las restriccion y si no la agrega.
		try:
			restricciones.index(direCont)
		except:
			restricciones.append(direCont)

		return restricciones
###############################################################################
	def decideCaminos(self,restricciones):
	#Elije randomente cantidad de movimientos y eleccion en base menos las restricciones.
		dirAsignadas=list()
		direcciones=["ar","de","ab","iz"]
		#Aca borra las restricciones de las probabilidades
		if restricciones != None:#si hay restricciones
			for i in range(len(restricciones)):
				direcciones.remove(restricciones[i])

		cantDeCavadas=random.randint(1,len(direcciones))
		i=1
		for i in range(cantDeCavadas):
			aux=True
			while aux:
				i=random.randint(0,len(direcciones)-1)
				if direcciones[i] != None:
					dirAsignadas.append(direcciones[i])
					direcciones[i]= None
					aux=False
		return(dirAsignadas)
###############################################################################
	def chequearAglomeracion(self):
		#Esta es la funcion de facu
		return True
###############################################################################
	def avanzarCaminos(self,direACavar):
	#Crea las ramas del troco principal
		ultPosRamas=list()

		self.separacion
		for i in range(len(direACavar)):
			ultPos=self.cavarRama(direACavar[i],self.separacion,self.posicionActual)
			if ultPos == False:
				return False

			ultdir=direACavar[i]
			ultPosRamas.append([ultPos,ultdir])

		i= random.randint(0,len(ultPosRamas)-1)
		self.posicionActual=ultPosRamas[i][0]
		self.direContraria= self.invertirDire(ultPosRamas[i][1])

		return True
###############################################################################
	def cavarRama(self,dire,distancia,posActual):
	#cava en la matriz y gira un poco las ramas.
		for A in range(distancia-1):
			if self.noEstarEnLaSalida(posActual):
				posActual=False
				return posActual
			direcciones=["ar","de","ab","iz"]
			restricciones= self.controlarBordes(posActual)
			direContra= self.invertirDire(dire)
			restricciones= self.comprobarDireccionContraria(restricciones,direContra)
			if restricciones != None:#si hay restricciones
				for i in range(len(restricciones)):
					direcciones.remove(restricciones[i])

			i=random.randint(0,len(direcciones)-1)
			dire=direcciones[i]
			posActual=self.cavarCamino(dire,posActual)

		return posActual
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
	def noEstarEnLaSalida(self,posActual):
	#Regresa true o false si se esta en una pared de salida:
		respuesta=False
		if self.salida == "ar":
			if posActual[1] == 0:
				respuesta=True
		if self.salida == "de":
			if posActual[0] == self.X-1:
				respuesta=True
		if self.salida == "ab":
			if posActual[1] == self.Y-1:
				respuesta=True
		if self.salida == "iz":
			if posActual[0] == 0:
				respuesta=True

		return respuesta
###############################################################################
