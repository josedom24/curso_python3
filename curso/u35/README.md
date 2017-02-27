# Ejercicios de diccionarios

Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1

Solución

	#!/usr/bin/env python
	dict = {}
	frase = input("Frase:")
	lista_palabras=frase.split(" ")
	for palabra in lista_palabras:
		if palabra in dict:
			dict[palabra]+=1
		else:
			dict[palabra]=1	

	for campo,valor in dict.items():
		print (campo,"->",valor)