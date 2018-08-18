
#---------------------
'''
Author: Isadora Salvetti
Descripcion:
Dibuja banderas hechas de bloques de lana en el suelo. Esta hecho para un mundo "super plano".
Veer abajo como usar.

'''
#---------------------

######################
# Código de las funciones - no cambiar!
######################

from mine import *
import time
mc = Minecraft()

#COLORES DE LANA 
red = block.WOOL_RED
white = block.WOOL_WHITE
blue = block.WOOL_BLUE
black = block.WOOL_BLACK
grass = block.GRASS
orange = block.WOOL_ORANGE
lightBlue = block.WOOL_CYAN
green = block.WOOL_GREEN
yellow = block.WOOL_YELLOW

def rect(ox, oz, dx, dz, color):
	block = color;
	pos = mc.player.getTilePos()
	posI = mc.player.getTilePos()
	posI.x = pos.x + ox - 3
	posI.z = pos.z + oz - 4
	pos.y = -1

	for x in range (0, dx):
		pos.x = posI.x + x
		for z in range (0, dz):
			pos.z = posI.z + z
			mc.setBlock(pos, block)

#Base: 6 x 9 white
rect(-12, -12, 33, 30, grass)
rect(-1, -1, 2, 2, block.REDSTONE_BLOCK)
rect(0, 0, 9, 6, white)

######################
# FIN
######################


"""
Codigo para crear las banderas.

La funcion "rect(1, 2, 3, 4, color)" crea una un rectangulo.
Los números y color dentro de la funcion son llamados de argumentos.
Puedes cambiarlos para cambiar el rectangulo creado.

Números:
1) distancia en sentido horizontal (x, en minecraft) del inicio del rectangulo al borde de la bandera. *
2) distancia en sentido vertical (z, en minecraft) del inicio del rectangulo al borde de la bandera. *
3) ancho del rectángulo.
4) altura del rectángulo
*La redstone marca este borde.

Colores: 
Las colores de lana estan listadas en #COLORES DE LANA (arriba).
Ej: red = block.WOOL_RED
	 ^ para lana roja, usar "red".

"""

#EJEMPLOS DE USO: (sacar los # para "activar" el código y veer los otros dos. Solo la última bandera "activa" estará visible).
#Italia
rect(0, 0, 3, 6, green)
rect(3, 0, 3, 6, white)
rect(6, 0, 3, 6, red)

#Alemania
#rect(0, 0, 9, 2, black)
#rect(0, 2, 9, 2, red)
#rect(0, 4, 9, 2, yellow)

#Dinamarca
#rect(0, 0, 9, 6, red)
#rect(0, 2, 9, 2, white)
#rect(2, 0, 2, 6, white)