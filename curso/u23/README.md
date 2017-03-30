# Operaciones avanzadas con secuencias

Las funciones que vamos a estudiar en esta unidad nos acercan al paradigna de la programación funcional que también nos ofrece python. La programación funcional es un paradigma de programación declarativa basado en el uso de funciones matemáticas, en contraste con la programación imperativa, que enfatiza los cambios de estado mediante la mutación de variables.

## Función map

`map(funcion,secuencia)`: Ejecuta la función enviada por parámetro sobre cada uno de los elementos de la secuencia.

*Ejemplo*

	>>> items = [1, 2, 3, 4, 5]
	>>> def sqr(x): return x ** 2
	>>> list(map(sqr, items))
	[1, 4, 9, 16, 25]

## Función filter

`filter(funcion,secuencia)`: Devuelve una secuencia con los elementos de la secuencia envíada por parámetro que devuelvan `True` al aplicarle la función envíada también como parámetro.

*Ejemplo*

	>>> lista = [1,2,3,4,5]
	>>> def par(x): return x % 2==0 
	>>> list(filter(par,lista))

## Función reduce

`reduce(funcion,secuencia)`: Devuelve un único valor que es el resultado de aplicar la función á los lementos de la secuencia.
	
*Ejemplo*

	>>> from functools import reduce
	>>> lista = [1,2,3,4,5]
	>>> def add(x,y): return x + y
	>>> reduce(add,lista)
	15

# list comprehension

`list comprehension` nos propociona una alternativa para la creación de listas. Es parecida a la función `map`, pero mientras `map` ejecuta una función por cada elemento de la secuencia, con esta técnica se aplica una expresión.

*Ejemplo*

	>>> [x ** 3 for x in [1,2,3,4,5]]
	[1, 8, 27, 64, 125]

	>>> [x for x in range(10) if x % 2 == 0]
	[0, 2, 4, 6, 8] 

	>>> [x + y for x in [1,2,3] for y in [4,5,6]]
	[5, 6, 7, 6, 7, 8, 7, 8, 9]
