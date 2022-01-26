'''3.- Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99:

Guarda en una variable el número introducido por el usuario. 
Añade un filtro que asegure que el número sea entre 0 y 99. 
Escribe la tabla multiplicando el valor introducido por valores entre 1 y 10.'''



comprobando = True

while comprobando:
	n1 = int(input("Introduce un valor entre 0 y 99: "))

	if n1 >= 0 and n1 <= 99:
		for i in range(1,11):
			print(str(n1), "x", str(i), "=", str(n1*i))
		comprobando = False
			
	else:
		print("El número no se encuentra dentro del rango determinado.")

	