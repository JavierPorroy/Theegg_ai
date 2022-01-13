#Juego de Picachu

import random 			# Importamos la librería random para poder utilizar el módulo .choice más adelante.
import time				# Importamos la librería time para poder utilizar el módulo .sleep más adelante.

picachu_ataque = 50		#Se le asigana a cada pokemon los puntos de vida que quitarán al rival con su ataque (especificados).
jigglypuff_ataque = 45

turno = [0, 1]

picachu_vida = 100		#Se le asigna a cada pokemon unos punto de vida especificados.
jigglypuff_vida = 100


print("*****  PICACHU Y JIGGLYUFF SE ENFRENTAN EN LA BATALLA  ****")
print()
time.sleep(2)			# Utilizamos el módulo .sleep para hacer una pausa de determinada duración entre textos de presentación... 
print()					#...y posteriormente entre ataques.

print("*****   ¡¡¡COMIENZA LA BATALLA ENTRE POKEMONS!!!       ****")
time.sleep(2)
print()
print()


turno = random.choice(["0", "1"])		# Utilizamos el módulo .choice para que el programa seleccione aleatoriamente quién comienza la batalla.
if turno == "0":
	print("Empieza la batalla atacando Picachu.")
if turno == "1":
	print("Empieza la batalla atanco Jigglypuff.")

time.sleep (3)

while picachu_vida > 0 and jigglypuff_vida > 0:		# Mediante un bucle while y siempre y cuando los dos pokemon tengan vida ira generando ... 
													# ... ataques y descontando puntos de vida a uno y a otro según los turnos asignados.
	if turno == "0":
		jigglypuff_vida = jigglypuff_vida - picachu_ataque
		print("Despues del ataque de Picachu, a Jigglypuff le quedan, ", jigglypuff_vida, "puntos de vida.")
		turno = "1"								# Esto hará que cambie el turno y se ejecute el siguiente condicionante en la próxima...
												#...  vuelta de búcle.
		time.sleep (3)

	elif turno == "1":
		picachu_vida = picachu_vida - jigglypuff_ataque
		print("Despues del ataque de Jigglypuff, a picachu le quedan, ", picachu_vida, "puntos de vida.")
		turno = "0"

		time.sleep (3)							#El búcle se repetirá una y otra vez cambiando el turno hasta que uno de los dos tenga 0 puntos...
												#... de vida o menos.

if picachu_vida <= 0:							# En el caso en el que picachu llegue a tener 0 o menos puntos de vida. Jigglypuff gana.
	print("Jigglypuff gana el combate.")
else:											# Sino ganara Picachu.
	print("Picachu gana el combate.")
