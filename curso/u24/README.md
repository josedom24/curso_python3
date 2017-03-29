# Tipo de datos secuencia: Tuplas

Las tuplas (`tuple`): Sirven para los mismo que las listas (me permiten guardar un conjunto de datos que se pueden repetir y que pueden ser de distintos tipos), pero en este caso es un tipo inmutable.

## Construcción de una tupla

Para crear una lista puedo usar varias formas:

* Con los caracteres ( y ):

    	>>> tupla1 = ()
    	>>> tupla2 = ("a",1,True)

* Utilizando el constructor tuple, que toma como parámetro un dato de algún tipo secuencia.

		>>> tupla3=tuple()
		>>> tuple4=tuple([1,2,3])

## Empaquetado y desempaquetado de tuplas

Si a una variable se le asigna una secuencia de valores separados por comas, el valor de esa variable será la tupla formada por todos los valores asignados. 

	>>> tuple = 1,2,3
	>>> tuple
	(1, 2, 3)

Si se tiene una tupla de longitud k, se puede asignar la tupla a k variables distintas y en cada variable quedará una de las componentes de la tupla. 

	>>> a,b,c=tuple
	>>> a
	1

## Operaciones básicas con tuplas

En las tuplas se pueden realizar las siguientes operaciones:

* Las tuplas se pueden recorrer.
* Operadores de pertenencia: `in` y `not in`.
* Concatenación: `+` 
* Repetición: `*`
* Indexación
* Slice

Entre las funciones definidas podemos usar: `len`, `max`, `min`, `sum`, `sorted`.

## Las tuplas son inmutables

	>>> tupla = (1,2,3)
	>>> tupla[1]=5
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

## Métodos principales

Métodos de búsqueda: `count`, `index`

	>>> tupla = (1,2,3,4,1,2,3)
	>>> tupla.count(1)
	2

	>>> tupla.index(2)
	1
	>>> tupla.index(2,2)
	5




