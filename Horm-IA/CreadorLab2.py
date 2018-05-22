#by lakhezis and hellfishg -- 10/05/2018

import random
from ConstructorLabs import ConstructorLabs

class CreadorLab2(ConstructorLabs):
	def __init__(self,largo,alto,entrada,salida,separacion):
		super().__init__(largo,alto)
		self.posicionActual=entrada
		self.salida=salida
		self.separacion=int(separacion)
		self.direContraria=self.invertirDire(salida)#no esta bien hecho
		self.salidaCreada=None
###############################################################################
	def crearLaberinto(self):
		final=True
		while final:
			restricciones= self.controlarBordes(self.posicionActual)
			restricciones= self.comprobarDireccionContraria(restricciones,self.direContraria)
			direccionesACavar= self.decideCaminos(restricciones)
			final=self.avanzarCaminos(direccionesACavar)

		self.salidaCreada=self.posicionActual
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
