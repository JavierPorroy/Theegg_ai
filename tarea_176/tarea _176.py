#1.Programa que diga el maximo de 3 numeros dados.

print("Vamos a calcular cual es el numero mayor")
print()
print()
print()

 
a = float(input("Introduce el primer número: "))
b = float(input("Introduce un segundo número: "))
c = float(input("Introduce un tercer número: "))

if a > b > c:
	print (a, "es el mayor.")
elif a < b > c:
	print (b, "es el mayor.")
elif b < a < c:
	print (c, "es el mayor.")
elif a < c > b:
	print (c, "es el mayor.")
elif a == b > c:
	print (a, " y ", b,",son iguales y son el número mayor.")
elif a < b == c:
	print (b, " y ", c,",son iguales y son el número mayor.")
elif a > b == c:
	print (a, "es el mayor.")
elif a == c > b:
	print (a, " y ", c,",son iguales y son el número mayor.")
else:
	print("Los 3 numreros son iguales.")

print()
print("********************************************************************************************************************************.")
print()


#2.Programa que diga la longitud de una frase.

print()
print()
print()
print("Vamos a calcular la longitud de una frase.")
print()
print()
print()


frase = str(input("Introduce una frase: "))

y = len(frase)
print("La frase tiene",y," caracteres.")

n = 0
longitud =len(frase)
veces = 0
while n <= longitud -1:
	if frase [n] == " ":
		veces += 1
	n += 1
x = veces + 1
print("La frase tiene ",x, " palabras.")


print()
print("********************************************************************************************************************************.")
print()


#3.Programa que determine si un caracter previamente dado  es vocal o no.


print()
print()
print()
print("Vamos a determinar si un caracter previamente dado es vocal o no.")
print()
print()
print()


vocales = ("a","e","i","o","u")
caracter = str(input("Introduce una caracter: "))
caracter = caracter.lower() 


if caracter in vocales:
	print ("El caracter ", caracter ,", es una vocal.")
else:
	print ("El caracter ", caracter ,", no es una vocal.")


print()
print("********************************************************************************************************************************.")
print()


#4.Programa que sume los valores de una lista.

import math

def sumar(lista):
	if lista == []:
		suma = 0
	else:
		suma = lista[0] + sumar(lista[1:])
	return suma


print()
print()
print()
print("Vamos a determinar la suma de los valores de una lista.")
print()
print()
print()

cantidad_valores = int(input("Introduce el número de valores que desea en su lista: "))

lista =[]


while len(lista) < cantidad_valores:
	lista_valores = float(input("Introduce un valor: "))
	lista.append(lista_valores)
	

operacion = sumar(lista)
print("El resultado de la suma es: ", operacion, " .")


print()
print("********************************************************************************************************************************.")
print()


#5.Programa que diga si una palabra dada es palíndromo.

print()
print()
print()
print("Vamos a determinar si una palabra dada es palíndromo.")
print()
print()
print()

def palindromo(palabra):
    palabra = palabra.replace(' ', '')      #Para reemplazar por todo seguido los espacios entre palabras de la frase para q la maquina pueda leer todo seguido.
    palabra = palabra.lower()               #Pasar la palabra a minusculas.
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():                  #run, es como funcion principal
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':      #Esta linea es el punto de entrada de un programa de python.
    run()
    
print()
print("********************************************************************************************************************************.")
print()

#6.Programa que compare dos listas y encuentre si hay algún valor coincidente.

print()
print()
print()
print("Vamos a comparar dos listas y encontrar algún valor coincidente, si es que lo hubiera.")
print()
print()
print()

cantidad_valores_1 = int(input("Introduce el número de valores que desea en su primera lista: "))
cantidad_valores_2 = int(input("Introduce el número de valores que desea en su segunda lista: "))

lista1 = []
lista2 = []
lista_coincidente = []


while len(lista1) < cantidad_valores_1:
	lista_valores_1 = float(input("Introduce un valor de la primera lista: "))
	lista1.append(lista_valores_1)

while len(lista2) < cantidad_valores_2:
	lista_valores_2 = float(input("Introduce un valor de la segunda lista: "))
	lista2.append(lista_valores_2)
	if lista_valores_2 in lista1 :
		lista_coincidente.append(lista_valores_2)

if lista_coincidente == []:
	print("Ningun valor de las listas coincide.")
else:
	print("De la lista de valores introducidos en ambas listas, estos son los valores coincidente: ", lista_coincidente,)

