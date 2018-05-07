import random
class CreaLaberinto:
###############################################################################
	def __init__(self,entrada):

		self.x= random.randint(20,50)
		self.y= random.randint(30,70)
		#self.x=10
		#self.y=15
		self.posicionActual=entrada
		self.matriz= None		
		self.Armar()
###############################################################################
	def Armar(self):

		aux=4
		self.matriz=[[["bloq"for a in range(aux)]for b in range(self.y)]for c in range(self.x)]		
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
	#Esta es la funcion de facu que comprueba que las casillas aledañas esten disponibles
	#o no para cavar
	def ChequearAglomeracion(self):
		return True


###############################################################################
	def TraducirPosicion(self,dire,xy):
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
	def Cava(self):
		largo=self.x
		alto=self.y

		try:
			while True:
				for i in range(len(dirAsignadas))
				#self.TraducirPosicion(dire,xy)=dirAsignadas

		except:
			pass
		
		#for x in range():
			#for y in range(alto):
				#print(x,y,self.Regula(x,y))

		#print(self.x,self.y)
		#Modificacion: Hacer que se mueva a partir de la ultima posicion cavada.
		#Desde x posicion, hay 3 casillas alrededor que estan llenas?
		#Verdadero, falso
###################################################################################

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


		