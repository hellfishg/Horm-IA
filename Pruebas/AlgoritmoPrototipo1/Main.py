import os
import cgitb
import CreadorLab2
import DibujadorLabs

cgitb.enable(format="text")#llama la funcion para el manejo de exepcion no default.
#(int-largo,int-alto,[1,0]-entrada,"de"-salida,int-separacion)
lab=CreadorLab2.CreadorLab2(10,10,[3,3],"de",600)

os.system('clear')
lab.crearLaberinto()

dibujito = DibujadorLabs.DibujadorLabs()
dibujito.graficarLaberinto(lab.matriz)



# cosas=CreaLaberinto.CreaLaberinto()
# #print(cosas)
# cosas.Armar()
# cosas.DecideCaminos()
# if cosas.ChequearAglomeracion():
# 	cosas.Cava()
# else:
# 	#Resolver que pasa si sale false en la funcion de facu
# 	pass
#
