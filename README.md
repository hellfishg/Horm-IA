Nombre: Horm IA
Genero: Simulador de colonia de hormigas
Resolución de laberinto
IA

Mecanica:

	Incial: Una colonia de hormigas envía X n° de ellas a la vez, a recoger un recurso para dicha colonia. Para conseguirlo, deberán sortear un laberinto dividido en módulos (A, B, C, D). Cada una de las hormigas deberá resolver el laberinto en una determinada cantidad de ciclos de vida. Pasada dicha cantidad, la hormiga morirá. Cuando una hormiga muere, automáticamente comenzará otra nueva hormiga, siendo X n° de ellas las que estarán siempre presentes en el laberinto. La hormiga muerta portará información de la resolución del módulo que haya sorteado con éxito, información que podrá obtener cualquier hormiga que encuentre su cadáver. Pero no será sino la hormiga que pueda volver con el recurso, la que transmita el conocimiento a toda la colonia.

	Segunda parte: La colonia obtiene información de la hormiga que volvió con el recurso. Las próximas hormigas que envíe, realizarán el mismo camino, con una posibilidad del X% en cada módulo de resolverlo a nuevo, sin la información transmitida. Una vez eso ocurra en alguno de los módulos, la posibilidad se anula en los siguientes módulos, cuyo modo de realización seguirá siendo el de la información que aportó la hormiga a la colonia en primer lugar.

	Tercera parte: Esto da la posibilidad de que el laberinto se resuelva en más ciclos, en menos ciclos, o que no se resuelva.
		Más ciclos: Las hormigas seguirán haciendo el camino previo.
		Menos ciclos: Al llegar la hormiga con el recurso, las hormigas recibirán nueva información.
		No se resuelve: Se supone que tardó más ciclos, entonces ese cadaver desaparece.



Idea: 
Crea un programa que cree objetos que tengas que aprender a recorrer un la laberinto modular. llegar al final y regresar con un recurso.

Cada entidad tendra una canidad de ciclos de ejecucion de vida. pasado estos ciclos se moriria y alguien podra heredar lo aprendido de ella. (ver como heredar)

Cada vez que se complete un sector del laberito se dara como aprendido. tomando tambien la cantidad de ciclos que tomo completarlo. de forma tal que se puede mejorar los tiempos de resolucion.

Morir en un sector implica que no se aprendio como salir de dicho sector. incluso si superar un sector gaste el 97% de los cliclos y no queden ciclos para resolver el sector siguiente.

Cada ciclo sera estimado por el usuario para acelerar o relentizar los resultados del experimento.

Jugador interactivo: Antes de comenzar la "partida" el jugador resolvera el mismo el laberinto. La "victoria" será que la hormiga resuelva el laberinto con la duración del jugador o más corta.
----------------------------------------------------------------------------------------------------------

+Creacion de un laberinto modular.
	+laberintos compuesto por 4 sectores, cada sector

+Analizar el tiempo de resolucion del laberito y darle aproximadamente 3 a 4 veces mas ciclos.

+Herencia 1: Si se encuentra una hormiga muerta, la hormiga que pasa por el sector puede heredar el conocimiento de un sector aprendido. Analizar cuanto duran las hormigas muertas. o si solo duran si tiene el conocimiento.

+Herencia 2: Cada vez que una hormiga muere regresa al principio y e intenta cambiar todos los patrones aprendidos anteriormente del sector (osea hacer otra cosa distinta). (creo que la cantidad de probabilidades randoms seria muy grande para p
+Herencia 4: oder resolver el laberinto)

+Herencia 3: La hormiga luego de finalizar sus ciclos queda en el lugar hasta que alguien la hereda. Siempre y cuando termino un sector.

+Herencia 4: esquema lunis despues de encontrar de traer el recurso ida i vuelta.

+Cada vez que se aprende a pasar un sector, y se encuentra con una hormiga muerta se puede chequear la cantidad de ciclos que se tardo en completar el mismo sector , de esta forma se puede mejorar el tiempo de aprendisaje.

+Regresar con un recurso agregaria 5 hormigas mas a la colmena. Acelerando el proceso de optimizacion de apredizaje gral.

+Ver el truco de "mano derecha en la pared".

Esquema de simbolos y pantalla (un sector)
 _______________________
   |  |     |     |	    || Ant: a  
@--+--+--+--+--+--+     ||  sec 1 = Aprendido / 23 ciclos.
   |     |  |           ||  	+heredado de b =23 ciclos.
   |     +--+--+--+     ||		+heredado de c =40 ciclos.
   +     |  |     |     ||
   |--------+-----+--@  ||
   +--------+           ||
________________________||

