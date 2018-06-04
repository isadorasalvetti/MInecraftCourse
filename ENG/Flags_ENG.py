# !!!! Do not change the code bellow
from mine import *
import time
mc = Minecraft()
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

#END




#Write your code bellow:
#Colors: red, white, blue, black.

#Italy
rect(0, 0, 3, 6, green)
rect(3, 0, 3, 6, white)
rect(6, 0, 3, 6, red)

#German
rect(0, 0, 9, 2, black)
rect(0, 2, 9, 2, red)
rect(0, 4, 9, 2, yellow)

#Denmark
rect(0, 0, 9, 6, red)
rect(0, 2, 9, 2, white)
rect(2, 0, 2, 6, white)

#Who knows
rect(0, 0, 9, 3, white)
rect(0, 3, 9, 3, red)
