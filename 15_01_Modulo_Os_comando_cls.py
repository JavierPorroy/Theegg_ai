#Modulo Os , comando cls.

#import os
#os.system("cls") #Nos limpia la pantalla.

#Programa dinamico con varias frases.

import os
import time


print("******************")
print("*                *")
print("*     ¡Hola!     *")
print("*                *")
print("******************")

time.sleep(2)
os.system("cls")

print("******************")
print("*                *")
print("*    ¡Qué tal!   *")
print("*                *")
print("******************")

time.sleep(2)
os.system("cls")


print("******************")
print("*                *")
print("*     ¡Adiós!    *")
print("*                *")
print("******************")

time.sleep(2)

#Movimiento de figuras.

espacios = " "

for i in range(20):				#Con este bucle nos ahorramos el tener que dibujar 20 monigotes y haremos q se repitan las figuras,
								# dejando un espacio en cada iterancion. Utilizamos las llaves para incorporarlo 
	time.sleep(0.3)				#y lo llamamos con el .format(espcaios).
	os.system("cls")

	print()
	print("{}   o   ".format(espacios))
	print("{}  /|\  ".format(espacios))
	print("{}  / |  ".format(espacios))

	espacios += " "

	time.sleep(0.3)
	os.system("cls")

	print()
	print("{}   o   ".format(espacios))
	print("{}  (|\  ".format(espacios))
	print("{}  | |  ".format(espacios))

	espacios += " "

	time.sleep(0.3)
	os.system("cls")

	print()
	print("{}   o   ".format(espacios))
	print("{}  /|\  ".format(espacios))
	print("{}  | \  ".format(espacios))

	espacios += " "

	time.sleep(0.3)
	os.system("cls")

	print()
	print("{}   o   ".format(espacios))
	print("{}  /|)  ".format(espacios))
	print("{}  | |  ".format(espacios))

	espacios += " "
