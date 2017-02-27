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

