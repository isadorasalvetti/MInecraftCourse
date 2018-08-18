import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import sys

mc = minecraft.Minecraft() #Crear conneccion con minecraft

#!!!!!!!!!!!!!!IMPORTANTE!!!!!!!!!!!!!!!!!!

#Antes de usar el script, usa el comando: /setworldspawn 0 0 0.
#Si no, las coordenadas no funcionan correctamente.

#!!!!!!!!!!!!!!IMPORTANTE!!!!!!!!!!!!!!!!!!

#Crea una pared desde x1, y1, z1 hasta x2, y2, z2, con un boque especifico:
#mc.setBlocks(x1, y1, z1, x2, y2, z2, material)

#Ejemplo: crea una casa simple desde el bloque 100, 4, 34

"""
ESQUEMA de COORDENADAS:
las coordenadas de los cantos son necessárias para crear las paredes:

b: 0, 0 + z -------- c: 0 + x, 0 + z
    /                            /
    /                            /
    /                            / 
    /                            /
    /                            /
a: 0, 0    ---------- d: 0 + x, 0

(La diferencia de altura es siempre igual para todas las paredes!)

Paredes:
a -> b
b -> c
c -> d
d -> a

"""


#Construir la casa desde posicion 0, 0, 0
h = 0 + 4 # y inicial + altura
x = 10 # tamano x
z = 4 # tamano z

#PAREDES
mc.setBlocks(0    , 0, 0    , 0    , h, 0 + z, block.DIAMOND_BLOCK)
mc.setBlocks(0    , 0, 0 + z, 0 + x, h, 0 + z, block.DIAMOND_BLOCK)
mc.setBlocks(0 + x, 0, 0 + z, 0 + x, h, 0    , block.DIAMOND_BLOCK)
mc.setBlocks(0 + x, 0, 0    , 0    , h, 0    , block.DIAMOND_BLOCK)

#TECHO
mc.setBlocks(0-1, h+1, 0-1, 0+x+1, h+2, 0+z+1, block.DIAMOND_BLOCK)

#Construir la casa desde posicion "i" (Mas facil de cambiar)
i = minecraft.Vec3(-72, 20, -14)
material = block.DIAMOND_BLOCK
h = i.y + 4 # y inicial + altura
x = 10 # tamano x
z = 22 # tamano z

#PARED
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

#TECHO
mc.setBlocks(i.x-1, h+1, i.z-1, i.x+x+1, h+1, i.z+z+1, material)


"""  <- eso es para crear comentarios de multiplas lineas.
        (hay siempre un par, un en el inicio del comentario y otro al final)
        puedes quitarlos para acceder el codigo seguinte, pero recuerdate de quitar
        el segundo al final de todo!

#Construir casa con materiales diferentes:
i = minecraft.Vec3(-32, 4, -14)
material = block.ICE 
h = i.y
x = 10 # tamano x
z = 22 # tamano z
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

i.y = i.y + 1
h = i.y
material = block.GLASS
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

i.y = i.y + 1
h = i.y
material = block.ICE 
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

i.y = i.y + 1
h = i.y
material = block.GLASS
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

i.y = i.y + 1
h = i.y
material = block.ICE 
mc.setBlocks(i.x    , i.y, i.z    , i.x    , h, i.z + z, material)
mc.setBlocks(i.x    , i.y, i.z + z, i.x + x, h, i.z + z, material)
mc.setBlocks(i.x + x, i.y, i.z + z, i.x + x, h, i.z    , material)
mc.setBlocks(i.x + x, i.y, i.z    , i.x    , h, i.z    , material)

#TECHO
mc.setBlocks(i.x-1, h+1, i.z-1, i.x+x+1, h+1, i.z+z+1, material)


#FIN DEL COMENTARION -> """