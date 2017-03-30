# Ejercicios de cadenas

Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Solución

	#!/usr/bin/env python
	cadena=input("Cadena:")
	caracter=input("Carácter:")
	print(caracter.join(cadena))

Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX

Solución

	#!/usr/bin/env python
	cadena=input("Cadena:")
	caracter=input("Carácter:")
	for i in range(10):
		cadena=cadena.replace(str(i),caracter)
	print(cadena)

Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

* La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
* Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república
 argentina debe devolver República Argentina.
* Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

Solución

	#!/usr/bin/env python
	cad=input("Cadena:")				

	# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
	lista=cad.split(" ")
	for palabra in lista:
	    print (palabra[0],end="")
	print()
	# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
	for palabra in lista:
	    print (palabra.capitalize(),end=" ")
	print()			
	# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
	for palabra in lista:
	    if palabra.startswith("a") or palabra.startswith("A"):
	        print (palabra,end=",")
	print()

Escribir funciones que dadas dos cadenas de caracteres:

* Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
* Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.

Solución

	#!/usr/bin/env python
	cad1=input("Cadena 1:")
	cad2=input("Cadena 2:")	
	if cad1.find(cad2)>-1:
		print ("cad2 es subcadena de cad1")
	else:
		print ("cad2 no es subcadena de cad1")			

	print(cad1 if cad1<cad2 else cad2)

scribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer

Solución

	#!/usr/bin/env python
	cad1=input("Cadena:")	
	if cad1.lower()==cad1[::-1].lower():
    		print("palindromo")
	else:
    		print("no palindromo")
