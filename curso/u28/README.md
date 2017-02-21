# Métodos principales de cadenas

Cuando creamos una cadena de caracteres estamos creando un objeto de la clase `str`, que tiene definido un conjunto de métodos:

	cadena.capitalize    cadena.isalnum       cadena.join          cadena.rsplit
	cadena.casefold      cadena.isalpha       cadena.ljust         cadena.rstrip
	cadena.center        cadena.isdecimal     cadena.lower         cadena.split
	cadena.count         cadena.isdigit       cadena.lstrip        cadena.splitlines
	cadena.encode        cadena.isidentifier  cadena.maketrans     cadena.startswith
	cadena.endswith      cadena.islower       cadena.partition     cadena.strip
	cadena.expandtabs    cadena.isnumeric     cadena.replace       cadena.swapcase
	cadena.find          cadena.isprintable   cadena.rfind         cadena.title
	cadena.format        cadena.isspace       cadena.rindex        cadena.translate
	cadena.format_map    cadena.istitle       cadena.rjust         cadena.upper
	cadena.index         cadena.isupper       cadena.rpartition    cadena.zfill


## Métodos de inserción: append, extend, insert

	>>> lista = [1,2,3]
	>>> lista.append(4)
	>>> lista
	[1, 2, 3, 4]

	>>> lista2 = [5,6]
	>>> lista.extend(lista2)
	>>> lista
	[1, 2, 3, 4, 5, 6]	

	>>> lista.insert(1,100)
	>>> lista
	[1, 100, 2, 3, 4, 5, 6]

## Métodos de eliminación: pop, remove

	>>> lista.pop()
	6
	>>> lista
	[1, 100, 2, 3, 4, 5]

	>>> lista.pop(1)
	100
	>>> lista
	[1, 2, 3, 4, 5]

	>>> lista.remove(3)
	>>> lista
	[1, 2, 4, 5]

## Métodos de ordenación: reverse, sort, 

	>>> lista.reverse()
	>>> lista
	[5, 4, 2, 1]

	>>> lista.sort()
	>>> lista
	[1, 2, 4, 5]

	>>> lista.sort(reverse=True)
	>>> lista
	[5, 4, 2, 1]

## Métodos de búsqueda: count, index

	>>> lista.count(5)
	1

	>>> lista.append(5)
	>>> lista
	[5, 4, 2, 1, 5]
	>>> lista.index(5)
	0
	>>> lista.index(5,1)
	4
	>>> lista.index(5,1,4)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: 5 is not in list

## Método de copia: copy

	>>> lista2 = lista1.copy()