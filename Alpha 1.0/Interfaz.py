
import sys
import os

class Interfaz:

    def __init__(self,laberinto,colonia,ciclos):

        self.__laberinto=colonia.laberinto
        self.__colonia=colonia
        self.__ciclos=ciclos
        self.__ciclosRestantes=ciclos
        self.pos_Lab_X=50
        self.pos_Lab_Y=15
        self.graficarLaberinto()

###############################################################################
    def graficarLaberinto(self):
    #Dibuja una celda + sus caminos derecha y abajo:

        mLab=self.__laberinto.getMatriz()

        largo=len(mLab)#maximo tamano de eje x
        alto=len(mLab[0])#maximo tamano de eje y

        for y in range(alto):
            for x in range(largo):
                dibX="[  ]"
                dibY=" "

                if self.__sinSalida(x,y):
                    dibX="    "

                if mLab[x][y][1] == "de":
                    dibX+="=="

                else:
                    dibX+="  "

                if mLab[x][y][2] == "ab":
                    dibY+="||"

                X=self.pos_Lab_X
                Y=self.pos_Lab_Y

                self.__dibujaAca((x*6)+ X , (y*2)+ Y, dibX)

                self.__dibujaAca((x*6)+ X , (y*2)+ Y+1 , dibY)

###############################################################################
    def graficarHormigas(self):

        mHormigas= self.__colonia.getHormigasEnMatriz()

        X=self.pos_Lab_X
        Y=self.pos_Lab_Y

        for i in range(self.__colonia.getCantidad()):
            coordenadas = mHormigas[i].posicion
            x= (((coordenadas[0])*6)+ X+1)
            y= (((coordenadas[1])*2)+ Y)
            sprite= "H" + str(i)

            self.__dibujaAca(x, y, chr(27)+"[0;35m" + str(sprite))

###############################################################################
    def graficarDescripcionHormigasVivas(self):

        self.__ciclosRestantes -= 1
        cantHormigasVivas= len(self.__colonia.getHormigasEnMatriz())

        for i in range(cantHormigasVivas):
            descripcion=self.__colonia.estadoHormiga(i)
            self.__dibujaAca(10, 13+  i,chr(27)+"[1;32m"+ "H" + str(i)+ ":" + str(descripcion))
            #estado de los ciclos:
            ciclosTotal=self.__ciclos
            ciclosRestante=self.__ciclosRestantes
            self.__dibujaAca(10, 10, "CICLOS: " + str(ciclosRestante) + "/" + str(ciclosTotal) )

###############################################################################
    def __dibujaAca(self,x, y, text):
    #Dibuja un string en la posicion y,x

        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        sys.stdout.flush()

###############################################################################
    def __sinSalida(self,x,y):

        bloq=0
        mLab=self.__laberinto.getMatriz()


        for i in range(4):

            if mLab[x][y][i] == "bloq":

                bloq+=1

        if bloq == 4:

            return True

        else:

            return False

###############################################################################
    def devolverInforme(self,log):
        os.system('clear')
        for info in log:
            print(info)

###############################################################################

'''
El formato de los codigos es, como habreis podido observar:
[A;Bm

A es un digito que indica formato:
0 - normal
1 - negrita
2 - diluir
3 - cursiva
4 - subrayado
5 - parpadeo lento
6 - parpadeo rapido
7 - negativo (invertir)

B es un numero que indica el color:
30-39 - color de texto, intensidad normal
40-49 - color de fondo, intensidad normal
90-99 - color de texto, intensidad fuerte
100-109 - color de fondo, intensidad fuerte

Ejemplo:

>>>print chr(27)+"[0;36m"+"este texto sale azul"
>>>print chr(27)+"[0;46m"+"este texto sale con fondo azul"+chr(27)+"[0m"

Hay que tener en cuenta que la configuracion de color se queda fijada para las siguientes salidas de texto. Si quereis que vuelva a escribir con los colores por defecto, debeis ejecutar:

>>>print chr(27)+"[0m"

'''
###########################################################################
#print chr(27)+"[0;33m"+"este texto sale de color,depende del numero 30 a 39"
#print "tu culo"


#\033[cordenadas]+"string"



###############################################################################
