import os

class Log:

    def __init__(self):
        self.informe=list()
        self.archivo=open("Informe.txt", "w")
        self.archivo.close()

###############################################################################
    def agregarInforme(self,info):
        self.informe.append(info)

###############################################################################
    def guardarEnArchivo(self):
        archivo=open("Informe.txt", "a")
        for log in self.informe:
            archivo.writelines(str(log)+'\n')

        archivo.close()

###############################################################################
