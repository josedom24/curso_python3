# Tipo de datos secuencia: Listas

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

Como veíamos en el apartado de [Tipo de datos secuencia](../u13) podemos realizar las siguientes operaciones:

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
	* `lista[start:end:step]` # Igual que el anterior pero dantos step saltos.
 		
 	Se pueden utilizar también índices negativos, por ejemplo: `lista[::-1]`



## Las listas son mutables

Como hemos indicado anteriormente las listas es un tipo de datos mutable. Eso tiene para nostros varias consecuencias, por ejemplo podemos obtener resultados como se los que se muestran a continuación:

	>>> lista1 = [1,2,3]
	>>> lista2 = lista1
	>>> lista1[1] = 10
	>>> lista2
	[1, 10, 3]

### ¿Cómo se copian las listas?

Por lo tanto si queremos cpoiar una lista en otra podemos hacerlo de la siguiente manera:

	>>> lista1 = [1,2,3]
	>>> lista2=lista1[:]
	>>> lista1[1] = 10
	>>> lista2
	[1, 2, 3]



	
	* Funciones predefinidas: len, sum, max, min, sorted
	* Concatenación de listas
	* Operadores in, not in, +, *
	* Slice 
	* Función enumerate()
	* Listas multidimensionales
	* 