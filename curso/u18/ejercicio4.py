#!/usr/bin/env python
secreto=int(input("Número secreto:"))
num=int(input("Número:"))
while num!=secreto:
    if num>secreto:
        print("El número es menor")
    else:
        print("El número es mayor")
    num=int(input("Número:"))
print ("Has acertado")