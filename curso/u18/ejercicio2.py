#!/usr/bin/env python
numero = int(input("Número:"))
for cont in range(1,11):
	print ("%2d * %d = %2d" % (cont, numero, cont * numero))