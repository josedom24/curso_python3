# Módulos y paquetes

* Módulo: Cada uno de los ficheros `.py` que nosotros creamos se llama módulo. Los elementos creados en un módulo (funciones, clases, ...) se pueden importar para ser utilizados en otro módulo. El nombre que vamos a utilizar para importar un módulo es el nombre del fichero.

* Paquete: Para estructurar nuestros módulos podemos crear paquetes. Un paquete, es una carpeta que contiene archivos `.py`. Pero, para que una carpeta pueda ser considerada un paquete, debe contener un archivo de inicio llamado `__init__.py`. Este archivo, no necesita contener ninguna instrucción. Los paquetes, a la vez, también pueden contener otros sub-paquetes.

## Ejecutando módulos como scripts

Si hemos creado un módulo, donde hemos definido dos funciones y hemos hecho un programa principal donde se utilizan dichas funciones, tenemos dos opciones: ejecutar ese módulo como un script o importar ese módulo desde otro, para utilizar sus funciones. Por ejemplo, si tenemos un fichero llamado `potencias.py`:

	#!/usr/bin/env python	

	def cuadrado(n):
		return(n**2)
	def cubo(n):
		return(n**3)
	if __name__ == "__main__":
		print(cuadrado(3))
		print(cubo(3))

En este caso, cuando lo ejecuto como un script:

	$ python3 potencias.py

El nombre que tiene el módulo es `__main__`, por lo tanto se ejecutará el programa principal.

Además este módulo se podrá importar (como veremos en el siguiente apartado) y el programa principal no se tendrá en cuenta.

## Importando módulos: import, from

Para importar un módulo completo tenemos que utilizar las instrucción `import`. lo podemos importar de la siguiente manera:

	>>> import potencias
	>>> potencias.cuadrado(3)
	9
	>>> potencias.cubo(3)
	27

## Namespace y alias

Para acceder (desde el módulo donde se realizó la importación), a cualquier elemento del módulo importado, se realiza mediante el **namespace**, seguido de un punto (.) y el nombre del elemento que se desee obtener. En Python, un **namespace**, es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo.

Es posible también, abreviar los **namespaces** mediante un **alias**. Para ello, durante la importación, se asigna la palabra clave `as` seguida del alias con el cuál nos referiremos en el futuro a ese namespace importado:

	>>> import potencias as p
	>>> p.cuadrado(3)
	9

## Importando elementos de un módulo: from...import

Para no utilizar el **namespace** podemos indicar los elementos concretos que queremos importar de un módulo:

	>>> from potencias import cubo
	>>> cubo(3)
	27

Podemos importar varios elementos separándolos con comas:

	>>> from potencias import cubo,cuadrado

Podemos tener un problema al importar dos elementos de dos módulos que se llamen igual. En este caso tengo que utilizar **alias**:

	>>> from potencias import cuadrado as pc
	>>> from dibujos import cuadrado as dc
	>>> pc(3)
	9
	>>> dc()
	Esto es un cuadrado

## Importando módulos desde paquetes

Si tenemos un módulo dentro de un paquete la importación se haría de forma similar. tenemos un paquete llamado `operaciones`:

	$ cd operaciones
	$ ls
	__init.py__  potencias.py

Para importarlo:

	>>> import operaciones.potencias
	>>> operaciones.potencias.cubo(3)
	27

	>>> from operaciones.potencias import cubo
	>>> cubo(3)
	27

## Función dir()

La función `dir()` nos permite averiguar los elementos definidos en un módulo:

	>>> import potencias
	>>> dir(potencias)
	['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cuadrado', 'cubo']


## ¿Donde se encuentran los módulos?
	
Los módulos estandar (como `math` o `sys` por motivos de eficiencia están escrito en C e incorporados en el interprete (builtins).

Para obtener la lista de módulos builtins:

	>>> import sys
	>>> sys.builtin_module_names
	('_ast', '_bisect', '_codecs', '_collections', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha512', '_socket', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'signal', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zipimport', 'zlib')

Los demás módulos que podemos importar se encuentran guardados en ficheros, que se encuentra en los path indicados en el interprete:

	>>> sys.path
	['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']

