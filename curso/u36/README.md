# Lectura y escritura de ficheros de textos

## Función open()

La función [open()](https://docs.python.org/3.4/library/functions.html#open) se utiliza normalmente con dos parámetros (fichero con el que vamos a trabajar y modo de acceso) y nos devuelve un objeto de tipo `file`.

	>>> f = open("ejemplo.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

### Modos de acceso

Los modos que podemos indicar son los siguientes:

<table>
	<tr>
		<td>Modo</td>
		<td>Comportamiento</td>
		<td>Puntero</td>
	</tr>
	<tr><td>r</td><td>Solo lectura</td><td>Al inicio del archivo</td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	<tr><td></td><td></td><td></td></tr>
	



 		 					
rb 		Solo lectura en modo binario 	Al inicio del archivo
r+ 		Lectura y escritura 			Al inicio del archivo
rb+ 	Lectura y escritura binario 	Al inicio del archivo
w 		Solo escritura. 				Al inicio del archivo
		Sobreescribe si existe. 
		Crea el archivo si no existe 	
wb 		Solo escritura en modo binario. Al inicio del archivo
		Sobreescribe si existe. 
		Crea el archivo si no existe 	
w+ 		Escritura y lectura. 			Al inicio del archivo
		Sobreescribe si existe. 
		Crea el archivo si no existe 	
wb+ 	Escritura y lectura binario. 	Al inicio del archivo
		Sobreescribe si existe. 
		Crea el archivo si no existe 	
a 		Añadido (agregar contenido).	Si el archivo existe, al final de éste. 
		Crea el archivo si no existe 	Si el archivo no existe, al comienzo 
ab 		Añadido en modo binario 		Si el archivo existe, al final de éste. 
		Crea si éste no existe 			Si el archivo no existe, al comienzo
a+ 		Añadido y lectura. 				Si el archivo existe, al final de éste.
		Crea el archivo si no existe. 	Si el archivo no existe, al comienzo
ab+ 	Añadido y lectura en binario. 	Si el archivo existe, al final de éste.
		Crea el archivo si no existe 	Si el archivo no existe, al comienzo

Como podemos comprobar podemos trabajar con ficheros binarios y con ficheros de textos.

### Codificación de caracteres

Si trabajamos con fichero de textos podemos indicar también el parámetro `encoding` que será la codificación de caracteres utilizadas al trabajar con el fichero, por defecto se usa la indicada en el sistema:

	>>> import locale
	>>> locale.getpreferredencoding()
	'UTF-8'

Y por último también podemos indicar el parámetro `errors` que controla el comportamiento cuando se encuentra con algún error al codificar o decodificar caracteres.

## Objeto file

Al abrir un fichero con un determinado modo de acceso con la función `open()` se nos devuelve un objeto fichero. El fichero abierto siempre hay que cerrarlo con el método `close()`:

	>>> f = open("ejemplo.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

Podemos abrirlo y cerrarlo en la misma instrucción con la siguiente estructura:

