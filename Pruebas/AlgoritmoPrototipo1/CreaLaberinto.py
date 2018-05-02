import random
class CreaLaberinto:
###############################################################################
	def __init__(self):

		#self.x= random.randint(20,50)
		#self.y= random.randint(30,70)
		self.x=10
		self.y=15
		self.auxEntrada= random.randint(0,self.y)		
		self.matriz= None		
		self.Armar()
###############################################################################
	def Armar(self):

		aux=4
		self.matriz=[[["bloq"for a in range(aux)]for b in range(self.y)]for c in range(self.x)]		
		self.entrada=[0,self.auxEntrada]
		#print(self.matriz)
		
###############################################################################
	def DecideCaminos(self):
		cantDeCavadas=random.randint(1,4)
		#print(cantDeCavadas)
		direcciones=["ar","de","ab","iz"]
		dirAsignadas=list()
		for i in range(cantDeCavadas):			
			aux=True			
			while aux:
				i=random.randint(0,cantDeCavadas-1)
				if direcciones[i] != None:					
					dirAsignadas.append(direcciones[i])
					direcciones[i]=None
					aux=False
		return(dirAsignadas)		

###############################################################################
	def Cava(self):
		largo=self.x
		alto=self.y

		for x in range(largo):
			for y in range(alto):
				print(x,y,self.Regula(x,y))

		print(self.x,self.y)
##############################################################################
	def Regula(self,x,y):
		restricciones=list()
		if x ==0:
			restricciones.append("iz")
		if y ==0:
			restricciones.append("ar")
		if x ==(self.x)-1:
			restricciones.append("de")
		if y ==(self.y)-1:
			restricciones.append("ab")

		return(restricciones)


		