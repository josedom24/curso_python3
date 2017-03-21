# Tipos de datos

Podemos concreatar aún más los tipos de datos (o clases) de los objetos que manejamos en el lenguaje:

* Tipos númericos
	* Tipo entero (int)
	* Tipo real (float)
	* Tipo numérico (complex)
* Tipos booleanos (bool)
* Tipo de datos secuencia
	* Tipo lista (list)
	* Tipo tuplas (tuple)
	* Tipo rango (range)
* Tipo de datos cadenas de caracteres
	* Tipo cadena (str)
* Tipo de datos binarios
	* Tipo byte (bytes)
	* tipo bytearray (bytearray)
* Tipo de datos conjuntos
	* Tipo conjunto (set)
	* Tipo conjunto inmutable (frozenset)
* Tipo de datos iterador y generador (iter)
* Tipo de datos mapas o diccionario (dict)

En realidad todo tiene definido su tipo o clase:

* Ficheros
* Módulos
* Funciones
* Excepciones
* Clases 

## Función type() 

La función `type` nos devuelve el tipo de dato de un objeto dado. Por ejemplo:

	>>> type(5)
	<class 'int'>
	>>> type(5.5)
	<class 'float'>
	>>> type([1,2])
	<class 'list'>
	>>> type(int)
	<class 'type'>

## Función isinstance()

Esta función devuelve True si el objeto indicado es del tipo indicado, en caso cntrario devuelve False.

	>>> isinstance(5,int)
	True
	>>> isinstance(5.5,float)
	True
	>>> isinstance(5,list)
	False
