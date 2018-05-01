import random

class CreadorLab3:

    def __init__(self,largo,alto,entrada,ciclos):
        self.X=largo
        self.Y=alto
        self.ciclos=ciclos
        self.salida="de" #hacer generico
        self.posicionActual=entrada

        self.treintaPorciento= int(self.ciclos * 0.30)
        self.diezPorciento= int(self.ciclos * 0.10)

        self.matriz=[[["bloq"for a in range(4)]for b in range(self.Y)]for c in range(self.X)]
        self.creaLaberinto() #solo para debug

###############################################################################
    def crearCaminoPrincipal(self):
        #Marca el camino principal por la matriz de laberinto.

        restricciones = self.controlarBordes(self.posicionActual)
        dirRand = self.aleatoriedadPorCiclos(restricciones)
        self.posicionActual = self.cavarCamino(dirRand)

###############################################################################
    def aleatoriedadPorCiclos(self,restricciones):
        #reduce la aleatoriedad segun se va quedando sin ciclos.
        direccionesRand=["ar","de","ab","iz"]

        if self.ciclos <= self.treintaPorciento:
            direccionesRand.append(self.salida)
        if self.ciclos <= self.diezPorciento:
            direccionesRand.append(self.salida)
            direccionesRand.append(self.salida)

        #Aca borra las restricciones de las probabilidades
        if len(restricciones) != 0:#si no hay restricciones
            for i in range(len(restricciones)):
                direccionesRand.remove(restricciones[i])

        i=random.randint(0,len(direccionesRand)-1)
        return direccionesRand[i]

###############################################################################
    def cavarCamino(self,dire):
        #Crea un camino segun la eleccion, y regresa la proxima posicion

        #!!ME QUEDE ACA!
        pass

###############################################################################
    def controlarBordes(self,posicionActual):
        #funcion dedicada a prohibir salirse de los bordes de la matriz
        #mina ya la tiene definida.
        pass
###############################################################################
    def ramificar(self):
        #crea aleatoriamente ramificaciones en el camino principal
        #!!balancear
        pass
###############################################################################
    def creaLaberinto(self):
        #funcion de debug.
        #00
        self.matriz[0][0][1]="de"
        #10
        self.matriz[1][0][2]="ab"
        self.matriz[1][0][3]="iz"
        #20
        self.matriz[2][0][1]="de"
        #30
        self.matriz[3][0][3]="iz"
        self.matriz[3][0][1]="de"
        #40
        self.matriz[4][0][3]="iz"
        self.matriz[4][0][2]="ab"
        #01
        self.matriz[0][1][1]="de"
        self.matriz[0][1][2]="ab"
        #11
        self.matriz[1][1][0]="ar"
        self.matriz[1][1][1]="de"
        self.matriz[1][1][2]="ab"
        self.matriz[1][1][3]="iz"
        #21
        self.matriz[2][1][3]="iz"
        #31
        self.matriz[3][1][1]="de"
        self.matriz[3][1][2]="ab"
        #41
        self.matriz[4][1][0]="ar"
        self.matriz[4][1][2]="ab"
        self.matriz[4][1][3]="iz"

        #02
        self.matriz[0][2][0]="ar"
        #12
        self.matriz[1][2][0]="ar"
        self.matriz[1][2][1]="de"
        #22
        self.matriz[2][2][1]="de"
        self.matriz[2][2][2]="ab"
        self.matriz[2][2][3]="iz"
        #32
        self.matriz[3][2][0]="ar"
        self.matriz[3][2][3]="iz"
        #42
        self.matriz[4][2][0]="ar"
        self.matriz[4][2][1]="de"
        self.matriz[4][2][2]="ab"
        #52
        self.matriz[5][2][1]="de"
        self.matriz[5][2][2]="ab"
        self.matriz[5][2][3]="iz"
        #62 -meta actual
        self.matriz[6][2][3]="iz"
        #23
        self.matriz[2][3][0]="ar"
        #33
        self.matriz[3][3][1]="de"
        #43
        self.matriz[4][3][0]="ar"
        self.matriz[4][3][1]="de"
        self.matriz[4][3][3]="iz"
        #53
        self.matriz[5][3][0]="ar"
        self.matriz[5][3][3]="iz"

###############################################################################
###############################################################################
###############################################################################
###############################################################################
