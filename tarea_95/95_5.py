'''5.- Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
 el proceso debe repetirse hasta que lo introduzca correctamente.'''



comprobando = True

while comprobando:
	n1 = int(input("Introduce un número impar: "))

	if n1 % 2 == 0:
		print("El número introducido no es impar, vuelve a intentarlo.")
	else:
		print("Correcto el número", n1,", es impar.")

