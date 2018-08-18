# Coordinates list:
# 175, 65, 335 -> House
# 177, 62, 332 -> Secret room (house)
# 346, 71, 774 -> Labyrinth

import mcpi.minecraft as minecraft
import time
import code
import sys

#---------------------
'''

Descripcion:
Pide una contrasena al jugador. Cuando el jugador entra la contrasena correcta, teleporta a un sitio especifico.
Cada contrasena es un funcion. Mirar abajo como adicionar / cambiar contrasenas.

'''
#---------------------

mc = minecraft.Minecraft() #Crear conneccino con minecraft

playerId = mc.getPlayerId()

def inputLine(prompt):
    mc.events.clearAll()
    while True:
        chats = mc.events.pollChatPosts()
        for c in chats:
            if c.entityId == playerId:
                print(c.message)
                if c.message == 'quit':
                    return 'quit()'
                elif c.message == ' ':
                    return ''
                elif "__" in c.message:
                    sys.exit();
                else:
                    return c.message
        time.sleep(0.2)

#################
# CONTRASENAS:
#################
def ohSecret(): # Nombre de funcion = contrasena
	coord = minecraft.Vec3(177, 62, 332) # Coordenada para el teleporte de esta contrasena
	mc.postToChat("Contraseña acceptada.") # Mensajes para el jugador
	mc.player.setTilePos(coord)
	time.sleep(0.5)
	mc.postToChat("Teleporte concluido. Has descubierto un secreto!")
	sys.exit() #Ya esta todo hecho. Quita el script

#Otros ejemplos:
def House(): #Nombre de funcion = contrasena
	coord = minecraft.Vec3(175, 65, 335) #!!!! Coordenada para el teleporte de esta contrasena
	mc.postToChat("Your password has been accepted.")
	mc.player.setTilePos(coord)
	time.sleep(0.5)
	mc.postToChat("Welcome home!")
	sys.exit() #Ya esta todo hecho. Quita el script

def ZigZag(): #Nombre de funcion = contrasena
	coord = minecraft.Vec3(346, 71, 774) #!!!! Coordenada para el teleporte de esta contrasena
	mc.postToChat("Your password has been accepted.")
	mc.player.setTilePos(coord)
	time.sleep(0.5)
	mc.postToChat("Welcome to the maze.")
	sys.exit() #Ya esta todo hecho. Quita el script

#################
# MENSAJE INICIAL
#################
# Las mensages que el jugador recibe antes de poner una contrasena
mc.postToChat("Escribir una contraseña.")
mc.postToChat("Hay muchas contraseñas posibles. Tu destino depende de la contra que eliges.")
mc.postToChat("Si no recibes respuesta, la contraseña no era correcta.")

################
i = code.interact(banner="", readfunc=inputLine, local=locals())
