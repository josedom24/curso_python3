#!/usr/bin/env python
import os
secreto=int(input("Número secreto:"))
os.system("clear")
cont=1
num=int(input("Número:"))
while num!=secreto:
    if num>secreto:
        print("El número es menor")
    else:
        print("El número es mayor")
    cont+=1
    num=int(input("Número:"))
print ("Has acertado, en %d veces"%cont)