#!/usr/bin/env python
cad =  input("Dame un número:")
try:
	i = int(cad)
except ValueError as error:
	print(type(error))
	print(error.args)
	print(error)