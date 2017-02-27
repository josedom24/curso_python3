# Tipo de datos secuencia: listas

Las listas (`list`) me permiten guardar un conjunto de datos que se pueden repetir y que pueden ser de distintos tipos. Es un tipo mutable.

## Construcción de una lista 

Para crear una lista puedo usar varias formas:

* Con los caracteres `[` y `]`:

		>>> lista1 = []
		>>> lista2 = ["a",1,True]

* Utilizando el constructor `list`, que toma como parámetro un dato de algún tipo secuencia.

		>>> lista3 = list()
		>>> lista4 = list("hola")
		>>> lista4
		['h', 'o', 'l', 'a']

## Operaciones básicas con listas

Como veíamos en el apartado "Tipo de datos secuencia" podemos realizar las siguientes operaciones:

* Las secuencias se pueden recorrer.
* Operadores de pertenencia: `in` y `not in`.
* Concatenación: `+` 
* Repetición: `*`
* Indexación: Cada elemento tiene un índice, empezamos a contar por el elemento en el índice 0. Si intento acceder a un índice que corresponda a un elemento que no existe obtenemos una excepción `IndexError`.

		>>> lista1[6]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module
		IndexError: list index out of range	

	Se pueden utilizar índices negativos:

		>>> lista[-1]
		6

* Slice: Veamos como se puede utilizar

	* `lista[start:end]` 	  # Elementos desde la posición start hasta end-1
	* `lista[start:]`    	  # Elementos desde la posición start hasta el final
	* `lista[:end]`      	  # Elementos desde el principio hata la posición end-1
	* `lista[:]` 		 	  # Todos Los elementos	    
	* `lista[start:end:step]` # Igual que el anterior pero dando step saltos.
 		
 	Se pueden utilizar también índices negativos, por ejemplo: `lista[::-1]`

## Funciones predefinidas que trabajan con listas

	>>> lista1 = [20,40,10,40,50]
	>>> len(lista1)
	5
	>>> max(lista1)
	50
	>>> min(lista1)
	10
	>>> sum(lista1)
	150
	>>> sorted(lista1)
	[10, 20, 30, 40, 50]
	>>> sorted(lista1,reverse=True)
	[50, 40, 30, 20, 10]

Veamos con más detenimiento la función `enumerate`: que recibe una secuencia y devuelve un objeto enumerado como tuplas:

	>>> seasons = ['Primavera', 'Verano', 'Otoño', 'Invierno']
	>>> list(enumerate(seasons))
	[(0, 'Primavera'), (1, 'Verano'), (2, 'Otoño'), (3, 'Invierno')]
	>>> list(enumerate(seasons, start=1))
	[(1, 'Primavera'), (2, 'Verano'), (3, 'Otoño'), (4, 'Invierno')]


## Las listas son mutables

Como hemos indicado anteriormente las listas es un tipo de datos mutable. Eso tiene para nostros varias consecuencias, por ejemplo podemos obtener resultados como se los que se muestran a continuación:

	>>> lista1 = [1,2,3]
	>>> lista1[2]=4
	>>> lista1
	[1, 2, 4]
	>>> del lista1[2]
	>>> lista1
	[1, 2]


	>>> lista1 = [1,2,3]
	>>> lista2 = lista1
	>>> lista1[1] = 10
	>>> lista2
	[1, 10, 3]

### ¿Cómo se copian las listas?

Por lo tanto si queremos copiar una lista en otra podemos hacerlo de varias formas:

	>>> lista1 = [1,2,3]
	>>> lista2=lista1[:]
	>>> lista1[1] = 10
	>>> lista2
	[1, 2, 3]

	>>> lista2 = list(lista1)	

	>>> lista2 = lista1.copy()

## Listas multidimensionales

A la hora de definir las listas hemos indicado que podemos guardar en ellas datos de cualquier tipo, y evidentemente podemos guardar listas dentro de listas. 

	>>> tabla = [[1,2,3],[4,5,6],[7,8,9]]
	>>> tabla[1][1]
	5

	>>> for fila in tabla:
	...   for elem in fila:
	...      print(elem,end="")
	...   print()
	 
	123
	456
	789
