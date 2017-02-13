# Tipo de datos numéricos

Python3 trabaja con tres tipos numéricos:

* Enteros (int): Representan todos los números enteros (positivos, negativos y 0), sin parte decimal. En python3 este tipo no tiene limitación de espacio. 
* Reales (float): Sirve para representar los números reales, tienen una parte decimal y otra  decimal. Normalmente se utiliza para su implementación un tipo `double` de C. 
* Complejos (complex): Nos sirven para representar números complejos, con una parte real y otra imaginaria.

Como hemos visto en la unidad anterior son tipos de datos inmutables.

*Ejemplos*

	>>> type(entero)
	<class 'int'>
	>>> real = 7.2
	>>> type (real)
	<class 'float'
	>>> complejo = 1+2j
	>>> type(complejo)
	<class 'complex'>

## Operadores aritméticos

* `+`: Suma dos números
* `-`: Resta dos números
* `*`: Multiplica dos números
* `/`: Divide dos números, el resultado es `float`.
* `//`: División entera
* `%`: Módulo o resto de la división
* `**`: Potencia
* `+`, `-`: Operadores unarios positivo y negativo

## Funciones predefinidas que trabajan con números:

* `abs(x)`: Devuelve al valor absoluto de un número.
* `divmod(x,y)`: Toma como parámetro dos números, y devuelve una tubla con dos valores, la división entera, y el módulo o resto de la división.
* `hex(x)`: Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro.
* `oct(x)`: Devuelve una cadena con la representación octal del número que recibe como parámetro.
* `pow(x,y): Devuelve la potencia de la base x elevedao al exponete y. Es similar al operador `**`.
* `round(x,[y])`: Devuelve un número real (float) que es el redondeo del número recibido como parámetro, podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.

*Ejemplos*

	>>> abs(-7)
	7
	>>> divmod(7,2)
	(3, 1)
	>>> hex(255)
	'0xff'
	>>> oct(255)
	'0o377'
	>>> pow(2,3)
	8
	>>> round(7.567,1)
	7.6


