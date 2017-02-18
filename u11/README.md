# Entrada y salida estándar

## Función input

No permite leer por teclado información. Devuelve una cadena de caracteres y puede tener como argumento una cadena que se muestra en pantalla.

*Ejemplos*

	>>> nombre=input("Nombre:")
	Nombre:jose
	>>> nombre
	'jose'
	>>> edad=int(input("Edad:"))
	Edad:23
	>>> edad
	23
	
## Función print

No permite escribir en la salida estándar. Podemos indicar varios datos a imprimir, que por defecto serán separado por un espacio (se puede indicar el separador) y por defecto se termina con un carácter salto de línea `\n` (también podemos indicar el carácter final). Podemos también imprimir varias cadenas de texto utilizando la concatenación.

*Ejemplos*

	>>> print(1,2,3)
	1 2 3
	>>> print(1,2,3,sep="-")
	1-2-3
	>>> print(1,2,3,sep="-",end=".")
	1-2-3.>>> 

	>>> print("Hola son las",6,"de la tarde")
	Hola son las 6 de la tarde
	>>> print("Hola son las "+str(6)+" de la tarde")
	Hola son las 6 de la tarde

## Formateando la salida¶
	
Existe dos formas de indicar el formato de impresión de las cadenas. En la documentación encontramos el [estilo antiguo](https://docs.python.org/2/library/stdtypes.html#string-formatting) y el [estilo nuevo](https://docs.python.org/3/library/string.html#string-formatting).

Para utilizar el nuevo estilo en python3 tenemos una función `format` y un método `format` en la clase `str`.



	* Función format()
