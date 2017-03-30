#!/usr/bin/env python
letra=input("Letra:")		
if letra>="A" and letra<="Z":
	print("Mayuscula")
elif letra>="a" and letra<="z":
	print("Minúscula")
else:
	print("Otro carácter")