print("Tras introducir un número entre 0,0001 y 0,9999 (no mas de 4 cifras decimales),\nse obtendrá y mostrará la correspondiente fracción irreducible.")
print()
print()
print()	


entrada = True						# Se le asigna a "entrada" el  valor booleano True para poder realizar el búcle posterior.
intentos = 1

while entrada:						# Se implementa un búcle que mientras "entrada" sea True se ejecute una y otra vez hasta que su valor sea False.
	
	numero = float(input("Introducir valor númerico que se desea fraccionar: "))

	if numero > 0 and numero < 1:					# De cumplirse la condición de haber introducido el valor númerico correctamente entre...
		numerador = int(numero * 10000)				#...los valores indicados, se desarrollará el cálculo de la fracción irreducible.
		denominador = 10000							# Multiplicaremos el num. y denom. por 10000 para pasar el número decimal a fracción.

		i = 7										# Le daremos un valor inicial de 7 a partir del cual irá dividiendo el num. como el denom.
		while i > 1: 											# Mientras el parametro i se encuentre por encima del valor 1, el búcle irá dividiendo...
			if numerador % i == 0 and denominador % i == 0:		#...aquellos valores de i que sean divisibles, tanto por el numerador como por el ...
				numerador = numerador/i 						#...denominador, con resto 0, hasta encontrar la fracción irreducible del valor introducido.
				denominador = denominador/i

			else:  
				i = i-1											# El parametro i comenzará desde el valor 7 e irá disminuyendo su valor de 1 en 1.

		solucion = ("%d" % numerador + "/" + "%d" % denominador)

		print("La fracción irreducible de " + str(numero) + " es " + str(solucion))
		entrada = False											# Cambiaremos el valor booleano de "entrada" a False para finalizar el programa.

	if numero < 0 or numero > 1:																# Se implementa un código para que en caso de...
		print("El número no es válido, recuerda, introduce un valor entre 0,0001 y 0,9999.")	#...introducir mal el valor numérico que se...
		intentos += 1																			#...desea fraccionar (que no se encuentre entre los...
																								#... valores indicados), el programa lo indique.

	if intentos >= 4:																			# Se implementa un código para que en caso de...
		print("Has consumido demasiados intentos. El programa ha finalizado.")					#...introducir 3 veces mal el valor numérico que se...
		entrada = False																			#...desea fraccionar (que no se encuentre entre los...
																								#... valores indicados), el programa se finalice.
		# Cambiaremos el valor booleano de "entrada" a False para finalizar el programa.
	