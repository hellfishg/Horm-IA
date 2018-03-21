import sys

class Interfaz:

    def __init__(self,laberinto):

        self.__laberinto=laberinto
        self.graficarLaberinto()


###############################################################################
    def graficarLaberinto(self):
    #Dibuja uns celda + sus caminoas derecha y abajo:

        mLab=self.__laberinto.getMatriz()

        largo=len(mLab)

        for y in range(len(mLab[0])):


            for x in range(largo):
                dibX="[  ]"
                dibY=" "

                if self.__sinSalida(x,y):
                    dibX="[xx]"


                if mLab[x][y][1] == "de":
                    dibX+="=="

                else:
                    dibX+="  "


                if mLab[x][y][2] == "ab":
                    dibY+="||"

                
                self.__dibujaAca(x*6, (y*2)+1, dibX)

                self.__dibujaAca(x*6, (y*2)+2 , dibY)



###############################################################################
    def __dibujaAca(self,y, x, text):
    #Dibuja algo en la posicion y,x

        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        #sys.stdout.flush()

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
