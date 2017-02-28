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
	<tr><td>rb</td><td>Solo lectura en modo binario </td><td></td></tr>
	<tr><td>r+</td><td>Lectura y escritura </td><td>Al inicio del archivo</td></tr>
	<tr><td>rb+</td><td>Lectura y escritura binario</td><td>Al inicio del archivo</td></tr>
	<tr><td>w</td><td>Solo escritura. Sobreescribe si existe. Crea el archivo si no existe.</td><td>Al inicio del archivo</td></tr>
	<tr><td>wb</td><td>Solo escritura en modo binario. Sobreescribe si existe. Crea el archivo si no existe.</td><td>Al inicio del archivo</td></tr>
	<tr><td>w+</td><td>Escritura y lectura. Sobreescribe si existe. Crea el archivo si no existe.</td><td>Al inicio del archivo</td></tr>
	<tr><td>wb+</td><td>Escritura y lectura binaria. Sobreescribe si existe. Crea el archivo si no existe.</td><td>Al inicio del archivo</td></tr>
	<tr><td>a</td><td>Añadido (agregar contenido). Crea el archivo si no existe.</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>ab</td>Añadido en modo binario. Crea si éste no existe<td></td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>a+</td><td>Añadido y lectura. Crea el archivo si no existe.</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	<tr><td>ab+</td><td>Añadido y lectura en binario. Crea el archivo si no existe</td><td>Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.</td></tr>
	
</table>

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

