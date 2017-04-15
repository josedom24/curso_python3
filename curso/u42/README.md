# Módulos estándares: módulos matemáticos

## Módulo math

El módulo [math](https://docs.python.org/3.4/library/math.html) nos proporciones distintas funciones y operaciones matemáticas.

	>>> import math
	>>> math.factorial(5)
	120
	>>> math.pow(2,3)
	8.0
	>>> math.sqrt(7)
	2.6457513110645907
	>>> math.cos(1)
	0.5403023058681398
	>>> math.pi
	3.141592653589793
	>>> math.log(10)
	2.302585092994046

## Módulo fractions

El módulo [fractions](https://docs.python.org/3.4/library/fractions.html) nos permite trabajar con fracciones.

	>>> from fractions import Fraction
	>>> a=Fraction(2,3)
	>>> b=Fraction(1.5)
	>>> b
	Fraction(3, 2)
	>>> c=a+b
	>>> c
	Fraction(13, 6)

## Módulo statistics

El módulo [statistics](https://docs.python.org/3.4/library/statistics.html) nos proporciona funciones para hacer operaciones estadísticas.

	>>> import statistics
	>>> statistics.mean([1,4,5,2,6])
	3.6

	>>> statistics.median([1,4,5,2,6])
	4

## Módulo random

El módulo [random](https://docs.python.org/3.4/library/random.html) nos permite generar datos pseudo-aleatorios.

	>>> import random
	>>> random.randint(10,100)
	34
	
	>>> random.choice(["hola","que","tal"])
	'que'
	
	>>> frutas=["manzanas","platanos","naranjas"]
	>>> random.shuffle(frutas)
	>>> frutas
	['naranjas', 'manzanas', 'platanos']

	>>> lista = [1,3,5,2,7,4,9]
	>>> numeros=random.sample(lista,3)
	>>> numeros
	[1, 2, 4]

	



