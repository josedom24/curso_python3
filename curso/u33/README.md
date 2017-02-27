# Tipo de datos mapa: diccionario

Los diccionarios son tipos de datos que nos permiten guardar valores, a los que se puede acceder por medio de una clave. Son tipos de datos mutables y los campos no tienen asignado orden.

## Definición de diccionarios. Constructor dict

	>>> a = dict(one=1, two=2, three=3)
	>>> b = {'one': 1, 'two': 2, 'three': 3}
	>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
	>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
	>>> e = dict({'three': 3, 'one': 1, 'two': 2})
	>>> a == b == c == d == e
	True

Si tenemos un diccionario vacío, al ser un objeto mutable, también podemos construir el diccionario de la siguiente manera.

	>>> dict1 = {}
	>>> dict1["one"]=1
	>>> dict1["two"]=2
	>>> dict1["three"]=3

## Operaciones básicas con diccionarios

	>>> a = dict(one=1, two=2, three=3)

* `len()`: Devuelve número de elementos del diccionario.

		>>> len(a)
		3

* Indexación: Podemos obtener el valor de un campo o cambiarlo (si no existe el campo nos da una excepción `KeyError`):

		>>> a["one"]
		1
		>>> a["one"]+=1
		>>> a
		{'three': 3, 'one': 2, 'two': 2}

* `del()`:Podemos eliminar un elemento, si no existe el campo nos da una excepción `KeyError`:
		
		>>> del(a["one"])
		>>> a
		{'three': 3, 'two': 2}

* Operadores de pertenencia: `key in d` y `key not in d`.

		>>> "two" in a
		True

* `iter()`: Nos devuelve un iterador de las claves. 

		>>> next(iter(a))
		'three'

## Los diccionarios son tipos mutables

Los diccionarios, al igual que las litas, son tipos de datos mutable. Por lo tanto podemos encontrar situaciones similares a las que explicamos en su momentos con las listas.

	>>> a = dict(one=1, two=2, three=3)
	>>> a["one"]=2
	>>> del(a["three"])
	>>> a
	{'one': 2, 'two': 2}	
	

	>>> a = dict(one=1, two=2, three=3)
	>>> b = a
	>>> del(a["one"])
	>>> b
	{'three': 3, 'two': 2}	

En este caso para copiar diccionarios vamos a usar el método `copy()`:

	>>> a = dict(one=1, two=2, three=3)
	>>> b = a.copy()
	>>> a["one"]=1000
	>>> b
	{'three': 3, 'one': 1, 'two': 2}







