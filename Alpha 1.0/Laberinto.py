# -*- coding: utf-8 -*-
class Laberinto:

    def __init__(self):

        x=7
        y=4
        aux=4
        self.__matriz=[[["bloq"for a in range(aux)]for b in range(y)]for c in range(x)]
        self.__creaLaberinto()

        self.__entrada="0,0"
        self.__salida="6,2"

    def getEntrada(self):
        return self.__entrada
    def getSalida(self):
        return self.__salida

    def imprimir(self):
        print(self.__matriz)

    def __creaLaberinto(self):
#00
        self.__matriz[0][0][1]="de"
#10
        self.__matriz[1][0][2]="ab"
        self.__matriz[1][0][3]="iz"
#20
        self.__matriz[2][0][1]="de"
#30
        self.__matriz[3][0][3]="iz"
        self.__matriz[3][0][1]="de"
#40
        self.__matriz[4][0][3]="iz"
        self.__matriz[4][0][2]="ab"
#01
        self.__matriz[0][1][1]="de"
        self.__matriz[0][1][2]="ab"
#11
        self.__matriz[1][1][0]="ar"
        self.__matriz[1][1][1]="de"
        self.__matriz[1][1][2]="ab"
        self.__matriz[1][1][3]="iz"
#21
        self.__matriz[2][1][3]="iz"
#31
        self.__matriz[3][1][1]="de"
        self.__matriz[3][1][2]="ab"
#41
        self.__matriz[4][1][0]="ar"
        self.__matriz[4][1][2]="ab"
        self.__matriz[4][1][3]="iz"

        #02
        self.__matriz[0][2][0]="ar"
        #12
        self.__matriz[1][2][0]="ar"
        self.__matriz[1][2][3]="de"
        #22
        self.__matriz[2][2][1]="de"
        self.__matriz[2][2][2]="ab"
        self.__matriz[2][2][3]="iz"
        #32
        self.__matriz[3][2][0]="ar"
        self.__matriz[3][2][3]="iz"
        #42
        self.__matriz[4][2][0]="ar"
        self.__matriz[4][2][1]="de"
        self.__matriz[4][2][2]="ab"
        #52
        self.__matriz[5][2][1]="de"
        self.__matriz[5][2][2]="ab"
        self.__matriz[5][2][3]="iz"
        #62
        self.__matriz[6][2][3]="iz"
        #23
        self.__matriz[2][3][0]="ar"
        #33
        self.__matriz[3][3][1]="de"
        #43
        self.__matriz[4][3][0]="ar"
        self.__matriz[4][3][1]="de"
        self.__matriz[4][3][3]="iz"
        #53
        self.__matriz[5][3][0]="ar"
        self.__matriz[5][3][3]="iz"

