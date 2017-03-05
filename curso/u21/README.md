# Métodos principales de listas

Cuando creamos una lista estamos creando un objeto de la clase `list`, que tiene definido un conjunto de métodos:

	lista.append   lista.copy     lista.extend   lista.insert   lista.remove   lista.sort
	lista.clear    lista.count    lista.index    lista.pop      lista.reverse

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

	>>> lista=["hola","que","tal","Hola","Que","Tal"]
	>>> lista.sort()
	>>> lista
	['Hola', 'Que', 'Tal', 'hola', 'que', 'tal']
	>>> lista=["hola","que","tal","Hola","Que","Tal"]
	>>> lista.sort(key=str.lower)
	>>> lista
	['hola', 'Hola', 'que', 'Que', 'tal', 'Tal']


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