# Mi primer programa en python3

La documentación de este curso esta escrita usando la distribución GNU/Linux Debian Jessie. Algunas particularidades pueden cambiar en otras versiones, distribuciones o sistemas operativos.

## Uso del interprete

Al instalar python3 el ejecutable del interprete lo podemos encontrar en `/usr/bin/python3`. Este directorio por defecto está en el PATH, por lo tanto lo podemos ejecutar directamente en el terminal. Por lo tanto para entrar en el modo interactivo, donde podemos ejecutar instrucción por instrucción interactivamente, ejecutamos:

	$ python3
	Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
	[GCC 4.9.1] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 

En el modo interactivo, la última expresión impresa es asignada a la variable _.

	>>> 4 +3
	7
	>>> 3 + _
	10


Si tenemos nuestro programa en un fichero fuente (suele tener extensión `py`), por ejemplo `programa.py`,lo ejecutaríamos de la siguiente manera.
	
	$ python3 programa.py

Por defecto la codificación de nuestro código fuente es UTF-8, por lo que no debemos tener ningún problema con los caracteres utilizados en nuestro programaos. Si por cualquier motivo necesitamos cambiar la codificación de los caracteres, en la primera línea de nuestro programa necesitaríamos poner:

	# -*- coding: encoding -

Por ejemplo:

	# -*- coding: cp-1252 -*-

## Escribimos un programa

Un ejemplo de nuestro primer programa, podría ser este "hola mundo" un poco modificado:

	numero = 5
	if numero == 5:
		print ("Hola mundo!!!")

La indentación de la última línea es importante (se puede hacer con espacios o con tabulador), en python se utiliza para indicar bloques de instrucciones definidas por las estructuras de control (if, while, for, ...). 

Para ejecutar este programa (guardado en `hola.py`):

	$ python3 hola.py
	$ Hola mundo!!!

## Ejecución de programas usando [shebang](https://es.wikipedia.org/wiki/Shebang)

Podemos ejecutar directamente el fichero utilizando en la primera línea el shebang, donde se indica el ejecutable que vamos a utilizar.

	#!/usr/bin/python3

También podemos usar el programa `env` para preguntar al sistema por la ruta el interprete de python:

	#!/usr/bin/env python

Por supuesto tenemos que dar permisos de ejecución al fichero.

	$ chmod +x hola.py

 	$ ./hola.py
	$ Hola mundo!!!

## Guía de estilo

Puede encontrar la guía de estilos para escribir código python en [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).