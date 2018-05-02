import sys
import os

class DibujadorLabs:

    def __init__(self):
        self.pos_Lab_X=6 #50  #debug:80
        self.pos_Lab_Y=6 #15  #debug:10
        os.system('clear')

###############################################################################
    def graficarLaberinto(self,matriz):
        mLab=matriz
        largo=len(mLab)#maximo tamano de eje x
        alto=len(mLab[0])#maximo tamano de eje y

        for y in range(alto):
            for x in range(largo):
                dibX="[  ]"
                dibY=" "

                if self.sinSalida(x,y,matriz):
                    dibX="    "

                if mLab[x][y][1] == "de":
                    dibX+="=="
                else:
                    dibX+="  "

                if mLab[x][y][2] == "ab":
                    dibY+="||"

                X=self.pos_Lab_X
                Y=self.pos_Lab_Y
                self.dibujaAca((x*6)+ X , (y*2)+ Y, dibX)
                self.dibujaAca((x*6)+ X , (y*2)+ Y+1 , dibY)

###############################################################################
    def dibujaAca(self,x, y, text):
    #Dibuja un string en la posicion y,x
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
        sys.stdout.flush()

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

###############################################################################

###############################################################################
###############################################################################
###############################################################################
###############################################################################
