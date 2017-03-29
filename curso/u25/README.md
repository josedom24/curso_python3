# Tipo de datos secuencia: Rangos

Los rangos (`range`): Es un tipo de secuencias que nos permite crear secuencias de números. Es un tipo inmutable y se suelen utilizar para realizar bucles.

## Definición de un rango. Constructor range

Al crear un rango (secuencia de números) obtenemos un objeto que es de la clase `range`:

	>>> rango = range(0,10,2)
	>>> type(rango)
	<class 'range'>

Veamos algunos ejemplos, convirtirndo el rango en lista para ver la secuencia:

	>>> list(range(10))
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> list(range(1, 11))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> list(range(0, 30, 5))
	[0, 5, 10, 15, 20, 25]
	>>> list(range(0, 10, 3))
	[0, 3, 6, 9]
	>>> list(range(0, -10, -1))
	[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

## Recorrido de un rango

Los rangos se suelen usar para ser recorrido, cuando tengo que crear un bucle cuyo número de iteraciones lo se de antemanos puedo usar una estructura como esta:

	>>> for i in range(11):
	...    print(i,end=" ")
	0 1 2 3 4 5 6 7 8 9 10  

## Operaciones básicas con range

En las tuplas se pueden realizar las siguientes operaciones:

* Los rangos se pueden recorrer.
* Operadores de pertenencia: `in` y `not in`.
* Indexación
* Slice

Entre las funciones definidas podemos usar: `len`, `max`, `min`,  `sum`, `sorted`.

Ademas un objeto `range` posee tres atributos que nos almacenan el comienzo, final e intervalo del rango:

	>>> rango = range(1,11,2)
	>>> rango.start
	1
	>>> rango.stop
	11
	>>> rango.step
	2
