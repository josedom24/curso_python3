# Tipo de datos: iterador y generador

## Iterador

Un objeto iterable es aquel que puede devolver un iterador. Normalmente las colecciones que hemos estudiados son iterables. Un iterador me permite recorrer los elementos del objeto iterable.

### Definición de iterador. Constructor iter

	>>> iter1 = iter([1,2,3])
	>>> type(iter1)
	<class 'list_iterator'>
	>>> iter2 = iter("hola")
	>>> type(iter2)
	<class 'str_iterator'>

## Función next(), reversed()

Para recorrer el iterador, itilizamos la función `next()`:

	>>> next(iter1)
	1
	>>> next(iter1)
	2
	>>> next(iter1)
	3
	>>> next(iter1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration

## El módulo itertools

El módulo (itertools)[https://docs.python.org/3.4/library/itertools.html] contine distintas funciones que nos devuelven iteradores.


