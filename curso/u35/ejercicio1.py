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
