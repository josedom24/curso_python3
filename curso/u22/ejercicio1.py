#!/usr/bin/env python
num=int(input("Número:"))
lista=[]
while num>0:
    lista.append(num)
    num=int(input("Número:"))		
print("Maáximo: %d" % max(lista))
for n in lista:
    if n % 2 ==0:
        print(n,end=" ")
print()
