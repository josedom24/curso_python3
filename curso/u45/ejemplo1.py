#!/usr/bin/env python
def factorial(n):
	"""Calcula el factorial de un número"""
	resultado = 1
	for i in range(1,n+1):
		resultado*=i
	return resultado

if __name__ == '__main__':
	print(factorial(6))