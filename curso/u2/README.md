# Python2 us Python3

## python 2.x y python 3.x

La ultima versión 2.x fue la 2.7 de 2010, contando con soporte hasta el final de su vida útil. No está en desarrollo.
La versión 3.x está bajo desarrollo activo, la última versión 3.6 salió el 23 de diciembre de 2016. Las modificaciones que se han incluido en python 3.x en sintaxis y módulos claves han hecho que no sea compatible con python 2.x.

En el [post: What’s New In Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html) escrito por Guido van Rossum podemos encontrar los cambios introducidos en la versión 3.x. En la documentación podéis encontrar la página [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) donde podéis estudiar las mejoras de cada una de las versión que van saliendo.

## Entonces, ¿Qué versión debería utilizar? 

Te debes asegurar si las bibliotecas que vas a utilizar son compatibles con la versión que vas a utilizar. El problema en los últimos años ha sido que no todas las librerías se habían exportado a la versión 3. En los últimos tiempo la versión 3 es suficientemente madura para se utilizada y muchos de las librerías y software más utilizado ya está exportado. Puedes ver la lista de los paquetes exportados a la versión 3 en la página [http://python3wos.appspot.com/](http://python3wos.appspot.com/).

Si es totalmente necesario, porque la librería que necesito no está portada tendríamos que usar la versión 2, pero hay que tener en cuenta que python 2.x es un lenguaje antiguo con errores, por lo tanto merece la pena hacer un esfuerzo y buscad alternativas para usar la versión 3. Si tienes código en la antigua versión, también existen herramientas para realizar la portabilidad: [Porting Python Code to 3.x](https://wiki.python.org/moin/PortingPythonToPy3k).

## Las principales difreencia entre python 2.x y 3.x

## Print es una función en python3

En python2:

	print "hola mundo"

En python3:

	print ("Hola mundo")

### División de números enteros

En python 2 al dividir enteros, siempre el resultado era un entero, en python3 el resultado es un número real.

En python2:

	>>> 4/3
	1

En python3:

	>>> 3/2
	1.5

	>>> num = 3/2
	>>> type(num)
	<class 'float'>
	>>> num = 4/2
	>>> type(num)
	<class 'float'>

### Las "cadenas" (strings) son Unicode de forma predeterminada en python 3

En python2 existe dos tipos diferenciados de cadenas: str (ascii) y unicode, en python 3 todas las cadenas son unicodes.

En python2:

	>>> cad = "piña"
	>>> cad
	'pi\xc3\xb1a'


En python3: 

	>>> cad = "piña"
	>>> cad
	'piña'

### Generación de listas de número

En python2 teníamos dos funciones parecidas: range que generaba una lista de números, y xrange que era una función que devolvía un objeto de tipo xrange. La diferencia entre ambas era que utilizar esta última era mucho más eficiente. E python3 sólo tenemos range que ha pasado a ser un tipo de datos.

En python2:

	>>> range(1,10)
	[1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> xrange(1,10)
	xrange(1, 10)
	>>> type(xrange(1,10))
	<type 'xrange'>

En pyton3:

	>>> range(1,10)
	range(1, 10)
	>>> type(range(1,10))
	<class 'range'>

### Input es una cadena de texto en python 3

En python 2 habían dos funciones para ingresar datos por un teclado raw_input() en que lo ingresado se trataba como una cadena de texto e input() en lo que se ingresaba se evaluaba y se trataba por su tipo. En python 3, se eliminó el input() de python 2 quedando el raw_input() como el nuevo input(). O sea el input() de python 3 siempre devuelve una cadena de texto.

En python2:

	>>> cad=raw_input()
	123
	>>> type(cad)
	<type 'str'>
	>>> num=input()
	123
	>>> type(num)
	<type 'int'>

En python3:

	>>> num=input()
	123
	>>> type(num)
	<class 'str'>

### Comparando tipos

Python 3 nos indica un error cuando intentamos comparar tipos de datos diferentes.

En python2:

	>>> [1,2] > "hola"
	False

En python3:

	>>> [1,2] > "hola"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unorderable types: list() > str()




