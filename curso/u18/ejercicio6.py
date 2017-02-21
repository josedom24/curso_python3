#!/usr/bin/env python
num=int(input("Número:"))
primo = True
for cont in range(2,num):
    if num%cont==0:
        primo=False
        break
if primo:
    print("Es primo")
else:
    print("No es primo")