
'''

Simple teleport script - introductory classes.
1) Write simple script that only teleports.
2) Add condition - only teleport if the target block is air.
3) Increment condition - only teleport if target block is air or water.


'''


#Import functions and connect to minecraft
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft()


#Get and change the player position to the new teleport position
playerPos = mc.player.getPos()
playerPos.x = playerPos.x + 1


#Get the target block
targetBlock = mc.getBlock(playerPos)
mc.postToChat(targetBlock)


# Find if the target block is air - if it is not, player should not be able to teleport
if targetBlock == 0:
	mc.player.setPos(playerPos)
else:
	mc.postToChat("Couldn't teleport: There is a block there!")



