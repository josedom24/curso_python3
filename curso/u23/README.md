# Ejercicios de listas

Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.

Solución

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
	# con list comprehension
	for n in [x for x in lista if x % 2 == 0]:
		print(n)

Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

Solución

	#!/usr/bin/env python
	lista=['Di', 'buen', 'dia', 'a', 'papa']
	print(lista[::-1])

Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas veces aparece en la lista,  lee otra cadena y sustituye la primera por la segunda en la lista, y por último borra la cadena de la lista

Solución

	#!/usr/bin/env python
	lista=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]	

	cadena=input("Cadena:")
	if cadena in lista:
		print("La cadena está en la lista")
	else:
		print("La cadena no está en la lista")	

	print(lista.count(cadena))	

	cadena2=input("Cadena a reemplazar:")
	apariciones=lista.count(cadena)
	pos=0
	for i in range(0,apariciones):
		pos=lista.index(cadena,pos)
		lista[pos]=cadena2
	print(lista)

Dado una lista, hacer un programa que indique si está ordenada o no.

Solución

	#!/usr/bin/env python
	lista=[2,3,4,1]
	lista2=lista[:]
	lista.sort()
	if lista==lista2:
		print("Lista ordenada")
	else:
		print("Lista no ordenada")
