import os
import time
import random
import sys

matrizNom=list()

archivo=open("../Textos/NomHormiga.txt", "r")
for nombre in archivo.readlines():
	matrizNom.append(nombre.rstrip('\n'))
archivo.close()


#print(matrizNom[])

for i in range(len(matrizNom)):
	num=random.randint(0,137)
	print(matrizNom[num])
#Estaba imprimiendo los nombres de hormigas de manera random. Problema: Se repiten. Posible solucion
#agregarle un espacio a cada nombre por el que haya pasado el for y la proxima vez que pase,
#reemplazar ese espacio por un numero, que se vaya reemplazando por el siguiente numero cada vez
#que el for pase por ahi. 
