import os
import time
import CreadorLab3
import DibujadorLabs

#creador = CreadorLab3.CreadorLab3(15,14,[0,0],"de",100)
draw = DibujadorLabs.DibujadorLabs()

while True:
    creador = CreadorLab3.CreadorLab3(15,14,[0,0],"de",100)
    creador.crearCaminoPrincipal()
    draw.graficarLaberinto(creador.matriz)
    time.sleep(2)
    os.system('clear')
