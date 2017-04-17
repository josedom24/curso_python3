#!/usr/bin/env python
def sumar(n,*args):
	resultado=n
	for i in args:
		resultado+=i
	return resultado