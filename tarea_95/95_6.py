'''6.- Realiza un programa que sume todos los números enteros impares desde el 0 hasta el 115.'''

impares =[]
suma_impares = 0

for i in range (1,116,2):
	impares.append(i)
	print(i)
for j in impares:
	suma_impares = sum(impares)
print("La suma de todos los impares del 0 al 115 es, ", suma_impares, ".")
