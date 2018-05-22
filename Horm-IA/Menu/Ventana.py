#by hellfishg 13/05/2018
import sys
import os

class Ventana:
    def __init__(self,menuAnterior,arg):
        self.matriz=None
        self.menuAnterior = menuAnterior
        self.arg=arg
##############################################################################
    def imprimirMenu(self):
        #Override
        pass
##############################################################################
    def procesarEleccion(self):
        #Override
        pass
##############################################################################
    def graficarAca(self,xy,text):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        sys.stdout.flush()
###############################################################################
    def color(self,color):
        #le pedis un color y te devuelve su ascci:
        #ver implementacion.
        pass
##############################################################################
    def graficarLaberinto(self,mLab,X,Y):
        #grafica el laberinto en base a la matriz y la posicion deseada.
        largo=len(mLab)#maximo tamano de eje x
        alto=len(mLab[0])#maximo tamano de eje y

        for y in range(alto):
            for x in range(largo):
                dibX="[  ]"
                dibY=" "

                if self.sinSalida(x,y,mLab):
                    dibX="    "

                if mLab[x][y][1] == "de":
                    dibX+="=="
                else:
                    dibX+="  "

                if mLab[x][y][2] == "ab":
                    dibY+="||"


                self.dibujaAca((x*6)+ X , (y*2)+ Y, dibX)
                self.dibujaAca((x*6)+ X , (y*2)+ Y+1 , dibY)
###############################################################################
    def sinSalida(self,x,y,matrix):
        bloq=0
        mLab=matrix

        for i in range(4):
            if mLab[x][y][i] == "bloq":
                bloq+=1

                if bloq == 4:
                    return True
            else:
                return False
##############################################################################
    def imprimirMarquesina(self):
        archivo=open("Menu/marquesina.txt", "r")
        y=0
        for nombre in archivo.readlines():
            y+=1
            self.dibujaAca(0,y,nombre)
        archivo.close()
###############################################################################
    def imprimirDeArchivo(self,x,y,path):
        archivo=open(str(path), "r")
        texto=""
        for linea in archivo.readlines():
            texto+=linea

        archivo.close()
        self.dibujaAca(x,y,texto)
###############################################################################
    def dibujaAca(self,x, y, text):
    #Dibuja un string en la posicion y,x
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        sys.stdout.flush()
###############################################################################
    def comandoInvalido(self,fun):
        os.system("clear")
        for i in range(10):
            os.system("echo")
        print("INGRESE UNA LETRA CORRECTA!")
        input('--OPRIMA ENTER PARA CONTINUAR--')
        fun()
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
