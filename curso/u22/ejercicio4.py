#!/usr/bin/env python
lista=[1,2,3,4]
lista2=lista[:]
lista.sort()
if lista==lista2:
	print("Lista ordenada")
else:
	print("Lista no ordenada")
