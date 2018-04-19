#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def pantalla():
	os.system('clear')
	
	
	aux=None
	verificar=True
	setea=list()

	while verificar:	
		aux=input('Introduce la cantidad de ciclos que durara el programa:')
		try:
			int(aux)
			verificar=False
		except:
			print("Tiene que ser en numeros enteros!")
	setea.append(int(aux))
		
	verificar=True
	while verificar:
		aux=input('Introduce la cantidad de ciclos de cada hormiga:')
		try:
			int(aux)
			verificar=False
		except:
			print("Tiene que ser en numeros enteros!")
	setea.append(int (aux))

	verificar=True
	while verificar:
		aux=input('Introduce cuantas hormigas vivas habra al mismo tiempo:')
		try:
			int(aux)
			verificar=False
		except:
			print("¡Tiene que ser en numeros enteros!")
	setea.append(int (aux))

	verificar=True
	while verificar:
		aux=input('¿Las hormigas que llegan a la meta quedaran en la lista?(S/N):')
		if aux== 'S' or aux== 'N':
			verificar=False
		else:
			print("¡Tiene que ser S o N!")
	setea.append(aux)

	#print(setea)
	return setea 