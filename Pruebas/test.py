#Herencia en python
class Automotor :
    """Clase de la cual heredan las demas"""

    def __init__(self, ensambladora) :
        self.ensambladora = ensambladora

    def printEnsambladora(self) :
        print "La ensambladora es", self.ensambladora

class Carro(Automotor) :
    """Esta clase hereda de Automotor y sus metodos"""
    pass

auto = Carro("algo")
auto.printEnsambladora()
