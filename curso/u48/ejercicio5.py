#!/usr/bin/env python

def multiplicar(lista):
	if len(lista)==1:
		return lista[0]
	else:
		return lista.pop()*multiplicar(lista)

if __name__ == '__main__':
	print(multiplicar([3,4,5]))