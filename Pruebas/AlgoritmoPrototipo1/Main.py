import CreaLaberinto
import DibujadorLabs

cosas=CreaLaberinto.CreaLaberinto()
#print(cosas)
cosas.Armar()
cosas.DecideCaminos()
if cosas.ChequearAglomeracion():
	cosas.Cava()
else:
	#Resolver que pasa si sale false en la funcion de facu
	pass

dibujito = DibujadorLabs.DibujadorLabs()
dibujito.graficarLaberinto(cosas.matriz)



