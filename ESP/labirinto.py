#---------------------
'''
Author: Isadora Salvetti
Descripcion:
Construe un labirinto. Veer descripcion de las funciones para detalles

'''
#---------------------

from mine import *
import time
import random
mc = Minecraft()

######################
# Variables
######################

MyMaze = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
          [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
          [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]

######################
# Código de las funciones
######################

def Build(lList, pos):
	#Construie el labirinto descrito por lista en LIST en la posicion POS.
	#El bock que se pone tiene el ID del block en la lista.

	x = 0
	z = 0
	xSize = len(MyMaze)
	zSize = len(MyMaze[0])

	while (z < zSize): #Loop principal - lee todos los valores en la lista, pone el block de mismo valor.	
		mc.setBlock(pos.x + x, pos.y + y, pos.z + z, lList[x][z]) #Pone un block con el ID en la lista.
		
		#Cambia los valores de la lista/ posicion del block
		x += 1
		if (x >= xSize):
			x -= xSize
			z += 1


def BuildHeight(lList, pos, h):
	#Construe el labirinto descrito por lista en LIST en la posicion POS.
	#El bock que se pone tiene el ID del block en la lista.
	#Adicinado altura (h) del labirinto

	x = 0
	y = 0
	z = 0
	xSize = len(MyMaze)
	zSize = len(MyMaze[0])

	while (z < zSize): #Loop principal - lee todos los valores en la lista, pone el block de mismo valor.	
		y -= 1
		
		while (y < h):
			pos.y += 1
			y += 1
			mc.setBlock(pos.x + x, pos.y + y, pos.z + z, lList[x][z]) #Pone un block con el ID en la lista.

		y -= h

		#Cambia los valores de la lista/ posicion del block
		x += 1
		if (x >= xSize):
			x -= xSize
			z += 1

#FUN/ Random:
def BuildHeightRandom(lList, pos, h):
	#Construe el labirinto descrito por lista en LIST en la posicion POS.
	#El bock que se pone es aleatorio
	#Adicinado altura (h) del labirinto

	x = 0
	y = 0
	z = 0
	xSize = len(MyMaze)
	zSize = len(MyMaze[0])

	while (z < zSize): #Loop principal - lee todos los valores en la lista, pone el block de mismo valor.	
		pos.y -= 1
		y -= 1
		
		while (y < h):
			pos.y += 1
			y += 1
			if (lList[x][z] > 0):
				mc.setBlock(pos.x, pos.y, pos.z, random.randint(1, 90)) #Pone un block con el ID en la lista.

		y -= h
		pos.y -= h

		#Cambia los valores de la lista/ posicion del block
		x += 1
		pos.x += 1
		if (x >= xSize):
			x -= xSize
			pos.x -= xSize
			z += 1
			pos.z += 1



#---------------------------------------------------------------------------------------
#-Llamar funcciones:--------------------------------------------------------------------

pos = mc.player.getTilePos()
#Build(MyMaze, pos)
#BuildHeight(MyMaze, pos, 3)
BuildHeightRandom(MyMaze, pos, 3)
