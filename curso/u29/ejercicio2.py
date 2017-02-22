#!/usr/bin/env python
cadena=input("Cadena:")
caracter=input("Carácter:")
for i in range(10):
	cadena=cadena.replace(str(i),caracter)
print(cadena)