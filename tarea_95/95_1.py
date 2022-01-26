'''1.- Realiza un programa que lea 2 números por teclado y determine:
	Si los dos números son iguales
	Si los dos números son diferentes
	Si el primero es mayor que el segundo
	Si el segundo es mayor o igual que el primero'''

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un segundo número: "))

comprobando = True

while comprobando:
	if n1 != n2:
		print("Los dos numeros son diferentes.")
		if n1 > n2:
			print("El número, ",n1,"es mayor que el número ",n2,".")
		elif n2 > n1:
			print("El número, ",n2,"es mayor que el número ",n1,".")

	else:
		print("Los dos numeros son iguales.")

	comprobando = False