import sys

class Interfaz:

    def __init__(self,laberinto,colonia):

        self.__laberinto=laberinto
        self.__colonia=colonia



###############################################################################
    def dibujar(self):
        print "algo"
        #Dibuja por pantalla todo.

###############################################################################
    def __print_there(y, x, text):
         sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
         sys.stdout.flush()

###############################################################################



###############################################################################

'''
El formato de los códigos es, como habréis podido observar:
[A;Bm

A es un dígito que indica formato:
0 - normal
1 - negrita
2 - diluir
3 - cursiva
4 - subrayado
5 - parpadeo lento
6 - parpadeo rápido
7 - negativo (invertir)

B es un número que indica el color:
30-39 - color de texto, intensidad normal
40-49 - color de fondo, intensidad normal
90-99 - color de texto, intensidad fuerte
100-109 - color de fondo, intensidad fuerte

Ejemplo:

>>>print chr(27)+"[0;36m"+"este texto sale azul"
>>>print chr(27)+"[0;46m"+"este texto sale con fondo azul"+chr(27)+"[0m"

Hay que tener en cuenta que la configuración de color se queda fijada para las siguientes salidas de texto. Si queréis que vuelva a escribir con los colores por defecto, debéis ejecutar:

>>>print chr(27)+"[0m"

'''
###########################################################################
#print chr(27)+"[0;33m"+"este texto sale de color,depende del numero 30 a 39"
#print "tu culo"


#\033[cordenadas]+"string"



###############################################################################
