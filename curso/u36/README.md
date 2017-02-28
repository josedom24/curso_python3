# Lectura y escritura de ficheros de textos

## Función open()

La función [open()](https://docs.python.org/3.4/library/functions.html#open) se utiliza normalmente con dos parámetros (fichero con el que vamos a trabajar y modo de acceso) y nos devuelve un objeto de tipo `file`.

	>>> f = open("ejemplo.txt","w")
	>>> type(f)
	<class '_io.TextIOWrapper'>
	>>> f.close()

Los modos que podemos indicar son los siguientes:

`r`: lectura (por defecto)
`w`: escritura, si el fichero no existe lo crea, si exite lo sobreeescribe. 	open for writing, truncating the file first
`x`: Abrir para crearlo, si exite devuelve un error
`a`: escritura, añadiendo al final del fichero
`b`: modo binario
`t`: modo texto (por defecto)
`+`: Modo lectura/escritura

Como podemos comprobar podemos trabajar con ficheros binarios y con ficheros de textos.

Si trabajamos con fichero de textos podemos indicar también el parámetro `encoding` que será la codificación de caracteres utilizadas al trabajar con el fichero, por defecto se usa la indicada en el sistema:

	>>> import locale
	>>> locale.getpreferredencoding()
	'UTF-8'

Y por último también podemos indicar el parámetro `errors`
