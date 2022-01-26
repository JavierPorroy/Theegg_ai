'''2.- Determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10.'''

cadena = str(input("Introduce un texto: "))

comprobando = True

while comprobando:
	if len(cadena) >= 5 and len(cadena) < 10:
		print("La longitud de la cadena es mayor o igual que 5 y menor que 10.")
	elif len(cadena) > 10:
		print("La longitud de la cadena es mayor que 10.")
	elif len(cadena) < 5:
		print("La longitud de la cadena es menor que 5.")
	comprobando = False