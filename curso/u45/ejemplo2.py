#!/usr/bin/env python
def operar(a,b):
	global suma
	suma = a + b
	resta = a - b
	print(suma,resta)

if __name__ == '__main__':
	operar(4,5)
	print(suma)
	print(resta)
	