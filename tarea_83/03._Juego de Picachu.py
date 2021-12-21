#Juego de Picachu

import random 
import time

picachu_ataque = 50
jigglypuff_ataque = 45

turno = [0, 1]

picachu_vida = 100
jigglypuff_vida = 100


print("*****  PICACHU Y JIGGLYUFF SE ENFRENTAN EN LA BATALLA  ****")
print()
time.sleep(2)
print()
print("*****   ¡¡¡COMIENZA LA BATALLA ENTRE POKEMONS!!!       ****")
time.sleep(2)
print()
print()


turno = random.choice(["0", "1"])
if turno == "0":
	print("Empieza la batalla atacando Picachu.")
if turno == "1":
	print("Empieza la batalla atanco Jigglypuff.")

time.sleep (3)

while picachu_vida > 0 and jigglypuff_vida > 0:

	if turno == "0":
		jigglypuff_vida = jigglypuff_vida - picachu_ataque
		print("Despues del ataque de Picachu, a Jigglypuff le quedan, ", jigglypuff_vida, "puntos de vida.")
		turno = "1"

		time.sleep (3)

	elif turno == "1":
		picachu_vida = picachu_vida - jigglypuff_ataque
		print("Despues del ataque de Jigglypuff, a picachu le quedan, ", picachu_vida, "puntos de vida.")
		turno = "0"

		time.sleep (3)


if picachu_vida <= 0:
	print("Jigglypuff gana el combate.")
else:
	print("Picachu gana el combate.")
