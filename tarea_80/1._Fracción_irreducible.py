print("Tras introducir un número entre 0,0001 y 0,9999 (no mas de 4 cifras decimales),\nse obtendrá y mostrará la correspondiente fracción irreducible.")
print()
print()
print()


entrada = True
intentos = 1

while entrada:
	
	numero = float(input("Introducir valor númerico que se desea fraccionar: "))

	if numero > 0 and numero < 1:
		numerador = int(numero * 10000)
		denominador = 10000
		i = 7
		while i > 1: 
			
			if numerador % i == 0 and denominador % i == 0:
				numerador = numerador/i
				denominador = denominador/i

			else:  
				i = i-1

		solucion = ("%d" % numerador + "/" + "%d" % denominador)

		print("La fracción irreducible de " + str(numero) + " es " + str(solucion))
		entrada = False

	if numero < 0 or numero > 1:
		print("El número no es válido, recuerda, introduce un valor entre 0,0001 y 0,9999.")
		intentos += 1
	

	if intentos >= 4:
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		entrada = False
	
	
	