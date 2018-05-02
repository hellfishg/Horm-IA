#
#	Funcion de prueba
#	Recorre la matriz casilla por casilla
#

def recorrerMatriz(nombreMatriz):

	for i in range(len(nombreMatriz)):
		for j in range(len(nombreMatriz[0])):
			if False==comprobarAdyacentes(nombreMatriz,i,j):
				print(str(i)+":"+str(j)+" = "+str(comprobarAdyacentes(nombreMatriz,i,j))+"\n")

###################################################################################################

#
#	Funcion que comprueba las casillas adyacentes a la posicion dada
#	Si algun cuadrante esta ocupado devuelve False de lo contrario 
#	devuelve True
#	No analiza los bordes
#

def comprobarAdyacentes(nombreMatriz,i,j):
	
			if i!=0 and j!=0 and i<len(nombreMatriz)-1 and j<len(nombreMatriz[0])-1:
				for x in range(2):
					for y in range(2):
						
						#	Seteo dos variable en falso
						#	Recorre las esquinas de cada cuadrante por iteracion 
						#	y comprueba que si son iguales cambie la variable a true

						a=False
						b=False

						#	comprueba las casillas de forma vertical

						if nombreMatriz[i-1+(x*2)][j-1+(y*2)]==nombreMatriz[i-1+(x*2)][j]:
							a=True

						#	comprueba las casillas de forma horizontal

						if nombreMatriz[i-1+(x*2)][j-1+(y*2)]==nombreMatriz[i][j-1+(y*2)]:
							b=True

						#	Si ambas son verdaderas entonces dicha casilla tiene al menos un
						#	un cuadrante ocupado y devuelve falso

						if a and b:
							#print(str(j+1)+":"+str(i+1)+" "+str(nombreMatriz[i][j]))
							#print("\n"+str(nombreMatriz[i-1+(x*2)][j-1+(y*2)])+"\t"+str(nombreMatriz[i][j-1+(y*2)])+"\n"+str(nombreMatriz[i-1+(x*2)][j])+"\n",end='')
							return False
				return True
			#return "Borde"
#				print("\n")

#		print("\n")

##################################################################################################

#
#	Imprime una matriz oredenada
#

def imprimirMatriz(nombreMatriz):
	for i in range(len(nombreMatriz)):
		for j in range(len(nombreMatriz[0])):
			if nombreMatriz[i][j]<10:
				print("0",end='')
			print(str(nombreMatriz[i][j])+"\t",end='')
		print("\n",end='')