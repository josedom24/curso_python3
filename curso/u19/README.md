# Tipo de datos secuencia

Los tipos de datos secuencia me permiten guardar una sucesión de datos de diferentes tipos. Los tipos de datos secuencias en python son: 

* Las listas (`list`): Me permiten guardar un conjunto de datos que se pueden repetir y que pueden ser de distintos tipos. Es un tipo mutable.
* Las tuplas (`tuple`): Sirven para los mismo que las listas, pero en este caso es un tipo inmutable. 
* Los rangos (`range`): Es un tipo de secuencias que nos permite crear secuencias de números. Es un tipo inmutable y se suelen utilizar para realizar bucles.
* Las cadenas de caracteres (`str`): Me permiten guardar secuencias de caracteres. Es un tipo inmutable. 
* Las secuencias de bytes (`byte`): Me permite guardar valores binarios representados por caracteres ASCII. Es un tipo inmutable.
* Las secuencias de bytes (`bytearray`): En este caso son iguales que las anteriores, pero son de tipo mutables.
* Los conjuntos (`set`): Me permiten guardar conjuntos de datos, en los que no se existen repeticiones. Es un tipo mutable.
* Los conjuntos (`frozenset`): Son igales que los anteriores, pero son tipos inmutables.


## Características principales de las secuencias

Vamos a ver distintos ejemplos partiendo de una lista, que es una secuencia mutable.

	lista = [1,2,3,4,5,6]

* Las secuencias se pueden recorrer
	
		>>> for num in lista:
		...   print(num,end="")
		123456

* Operadores de pertenencia: Se puede comprobar si un elemento pertenece o no a una secuencia con los operadores `in` y `not in`.

		>>> 2 in lista
		True
		>>> 8 not in lista
		True

* Concatenación: El operador `+` me permite unir datos de tipos secuenciales. No se pueden concatenar secuencias de tipo `range` y de tipo conjunto.

		>>> lista + [7,8,9]
		[1, 2, 3, 4, 5, 6, 7, 8, 9]

* Repetición: El operador `*` me permite repetir un dato de un tipo secuencial. No se pueden repetir secuencias de tipo `range` y de tipo conjunto.

		>>> lista * 2
		[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

* Indexación: Puedo obtener el dato de una secuencia indicando la posición en la secuencia. Los conjuntos no tienen implementado esta característica.

		>>> lista[3]
		4
	
* Slice (rebanada): Puedo obtener una subsecuencia de los datos de una secuencia. En los conjuntos no puedo obtener subconjuntos. Esta característica la estudiaremos más detenidamente en la unidad que estudiemos las listas.

		>>> lista[2:4]
		[3, 4]
		>>> lista[1:4:2]
		[2, 4]

* Con la función `len` puedo obtener el tamaño de la secuencia, es decir el número de elementos que contiene.

		>>> len(lista)
		6

* Con las funciones `max` y `min` puedo obtener el valor máximo y mínimo de una secuencia.

		>>> max(lista)
		6
		>>> min(lista)
		1
	
Además en los tipos mutables puedo realizar las siguientes operaciones:

* Puedo modificar un dato de la secuencia indicando su posición.

		>>> lista[2]=99
		>>> lista
		[1, 2, 99, 4, 5, 6]
		
* Puedo modificar un subconjunto de elementos de la secuencia haciendo slice.

		>>> lista[2:4]=[8,9,10]
		>>> lista
		[1, 2, 8, 9, 10, 5, 6]

* Puedo borrar un subconjunto de elementos con la instrucción `del`.

		>>> del lista[5:]
		>>> lista
		[1, 2, 8, 9, 10]

* Puedo actualizar la secuencia con el operador `*=`

		>>> lista*=2
		>>> lista
		[1, 2, 8, 9, 10, 1, 2, 8, 9, 10]
