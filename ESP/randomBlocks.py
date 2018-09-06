#---------------------
'''
Author: Isadora Salvetti
Descripcion:
Random Blocks!

'''
#---------------------

from mine import *
import time
import random
mc = Minecraft()

def randomBlock():
	while(True):
		time.sleep(.2)
		pos = mc.player.getTilePos()
		pos.y -= 1
		block = random.randint(1, 90)
		mc.setBlock(pos.x, pos.y, pos.z, block)

def randomCube(size):
	x, y, z = 0, 0, 0
	pos = mc.player.getTilePos()
	while (z < size):

		block = random.randint(1, 90)
		mc.setBlock(pos.x + x, pos.y + y, pos.z + z, block)

		x+=1 #Una dimension

		if (x >= size): #Dos dimensiones
			x -= size
			y += 1

		if (y >= size): #Tres dimensiones
			y -= size
			z += 1

#randomBlock()
randomCube(5)