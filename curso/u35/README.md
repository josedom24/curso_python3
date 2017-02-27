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

Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. Escribir un programa que lea una palabra y la muestre usando el código morse.

Solución

	#!/usr/bin/env pytho
	codigo = {
	    'A': '.-',     'B': '-...',    'C': '-.-.',
	    'D': '-..',    'E': '.',       'F': '..-.',
	    'G': '--.',    'H': '....',    'I': '..',
	    'J': '.---',   'K': '-.-',     'L': '.-..',
	    'M': '--',     'N': '-.',      'O': '---',
	    'P': '.--.',   'Q': '--.-',    'R': '.-.',
	    'S': '...',    'T': '-',       'U': '..-',
	    'V': '...-',   'W': '.--',     'X': '-..-',
	    'Y': '-.--',   'Z': '--..',    '1': '.----',
	    '2': '..---',  '3': '...--',   '4': '....-',
	    '5': '.....',  '6': '-....',   '7': '--...',
	    '8': '---..',  '9': '----.',   '0': '-----',
	    '.': '.-.-.-', ',': '--..--',  ':': '---...',
	    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
	    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
	    '-': '-....-', '/': '-..-.',   '=': '-...-',
	    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
	    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
	}	

	palabra = input("Palabra:")
	lista_codigos = []
	for caracter in palabra:
		if caracter.islower():
			caracter=caracter.upper()
		lista_codigos.append(codigo[caracter])	
	print (" ".join(lista_codigos))
		
Continuar el programa: ahora nos pide un cóigo morse donde cada letra esta separada por espacios y nos da la cadena correspondiente.

Solución

	morse=input("Morse:")
	lista_morse=morse.split(" ")
	palabra = ""
	for cod in lista_morse:
	    letra=[key for key,valor in codigo.items() if valor==cod][0]
	    palabra=palabra+letra
	print (palabra)


Suponga un diccionario que contiene como clave el nombre de una persona y como valor una lista con todas sus "gustos". Desarrolle un programa que agregue "gustos" a la persona:
* Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
* Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
* Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.

Se deja de pedir personas cuando introducimos el carácter "*".

Solución

	#!/usr/bin/env python
	gustos={}
	nombre = input("Nombre:")
	while nombre!="*":
		gusto=input("Gusto:")
		lista_gustos=gustos.setdefault(nombre,[gusto])
		if lista_gustos!=[gusto]:
			gustos[nombre].append(gusto)
		nombre = input("Nombre:")
	print(gustos)