# Métodos principales de cadenas

Cuando creamos una cadena de caracteres estamos creando un objeto de la clase `str`, que tiene definido un conjunto de métodos:

	cadena.capitalize    cadena.isalnum       cadena.join          cadena.rsplit
	cadena.casefold      cadena.isalpha       cadena.ljust         cadena.rstrip
	cadena.center        cadena.isdecimal     cadena.lower         cadena.split
	cadena.count         cadena.isdigit       cadena.lstrip        cadena.splitlines
	cadena.encode        cadena.isidentifier  cadena.maketrans     cadena.startswith
	cadena.endswith      cadena.islower       cadena.partition     cadena.strip
	cadena.expandtabs    cadena.isnumeric     cadena.replace       cadena.swapcase
	cadena.find          cadena.isprintable   cadena.rfind         cadena.title
	cadena.format        cadena.isspace       cadena.rindex        cadena.translate
	cadena.format_map    cadena.istitle       cadena.rjust         cadena.upper
	cadena.index         cadena.isupper       cadena.rpartition    cadena.zfill


## Métodos de formato

	>>> cad = "hola, como estás?"
	>>> print(cad.capitalize())
	Hola, como estás?

	>>> cad = "Hola Mundo" 
	>>> print(cad.lower())
	hola mundo

	>>> cad = "hola mundo"
	>>> print(cad.upper())
	HOLA MUNDO

	>>> cad = "Hola Mundo"
	>>> print(cad.swapcase())
	hOLA mUNDO

	>>> cad = "hola mundo"
	>>> print(cad.title())
	Hola Mundo

	>>> print(cad.center(50))
	                    hola mundo                    
	>>> print(cad.center(50,"="))
	====================hola mundo====================

	>>> print(cad.ljust(50,"="))
	hola mundo========================================
	>>> print(cad.rjust(50,"="))
	========================================hola mundo

	>>> num = 123
	>>> print(str(num).zfill(12))
	000000000123

## Métodos de búsqueda

	>>> cad = "bienvenido a mi aplicación"
	>>> cad.count("a")
	3
	>>> cad.count("a",16)
	2
	>>> cad.count("a",10,16)
	1

	>>> cad.find("mi")
	13
	>>> cad.find("hola")
	-1

## Métodos de validación

	>>> cad.startswith("b")
	True
	>>> cad.startswith("m")
	False
	>>> cad.startswith("m",13)
	True

	>>> cad.endswith("ción")
	True
	>>> cad.endswith("ción",0,10)
	False
	>>> cad.endswith("nido",0,10)
	True

Otras funciones de validación: `isalnum()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`, `isspace()`, `istitle()`,...