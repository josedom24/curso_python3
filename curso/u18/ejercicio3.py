#!/usr/bin/env python
num=int(input("Número:"))
fact=1
for i in range(2,num+1):
	fact*=i
print("El resultado es %d" % fact)