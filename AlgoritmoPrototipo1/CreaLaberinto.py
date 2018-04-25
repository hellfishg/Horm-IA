class CreaLaberinto
###############################################################################
	def __init__(self):

		x= 50
		y= 70
		aux=4
		auxEntrada= random.randint(0,69)		
		self.__matriz=[[["bloq"for a in range(aux)]for b in range(y)]for c in range(x)]
		self.__creaLaberinto()
		self.__entrada=[0,auxEntrada]

###############################################################################
	def __definirCuadrantes(self,coord):
		coord= [x,y]
		