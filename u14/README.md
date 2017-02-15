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



	* Las listas son mutables
	* Indexación y recorrido de una lista
	* Funciones predefinidas: len, sum, max, min, sorted
	* Concatenación de listas
	* Operadores in, not in, +, *
	* Slice 
	* Función enumerate()
	* Listas multidimensionales
	* ¿Cómo se copian las listas?