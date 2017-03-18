import os
import time
import random


import Laberinto
import Hormiga
import Colonia


'''lab=Laberinto.Laberinto()


colony=Colonia.Colonia(10,20,lab)

for i in range(300):
    colony.avanzarHormigas()


for i in range(10):
    print colony.estadoHormiga(i)'''

################################################################################
#Testeo para dibujar con print()

#print "Esto es \nuna cadena",
#print "Esto es otra cadenas"

import sys

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()


#print chr(27)+"[0;36m"+"este texto sale azul"


print "[  ]==[  ]"
print "_______||____________ "
print "[  ]==[  ]==[  ]  [  ]"
print "_||____||__________||_"
print "[  ]  [  ]==[  ]==[  ]"


print_there(3, 8, chr(27)+"[0;35m"+"H1")
print_there(5, 14, chr(27)+"[0;36m"+"H2")
