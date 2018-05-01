import CreadorLab3
import DibujadorLabs



creador = CreadorLab3.CreadorLab3(10,15,[0,4],100)
draw = DibujadorLabs.DibujadorLabs()

restri=["de","ab"]

for i in range(20):
    print(creador.aleatoriedadPorCiclos(restri))
#draw.graficarLaberinto(creador.matriz)
