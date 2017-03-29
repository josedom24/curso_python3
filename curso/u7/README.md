# Funciones y constantes predefinidas

## Funciones predefinidas

Tenemos una serie de funciones predefinidas en python3:

	abs() 		  dict() 		help()		 min() 		setattr()
	all() 		  dir() 		hex() 		 next() 	slice()
	any() 		  divmod() 		id() 		 object() 	sorted()
	ascii() 	  enumerate()		input() 	 oct() 		staticmethod()
	bin() 		  eval() 		int() 		 open() 	str()
	bool()		  exec() 		isinstance() 	ord() 		sum()
	bytearray()	  filter() 		issubclass() 	pow() 		super()
	bytes() 	  float() 		iter() 	 	 print() 	tuple()
	callable() 	  format() 		len() 		 property() 	type()
	chr() 		  frozenset() 		list() 		 range() 	vars()
	classmethod()	  getattr() 		locals() 	 repr() 	zip()
	compile() 	  globals() 		map() 		 reversed()		__import__()
	complex() 	  hasattr() 		max() 		 round() 	 
	delattr() 	  hash() 		memoryview() 	set() 	 

Todas estas funciones y algunos elmentos comunes del lenguaje están definidas en el módulo [builtins](https://docs.python.org/3/library/builtins.html).

### Algunos ejemplos de funciones

* La entrada y salida de información se hacen con la función `print` y la función `input`:
* Tenemos algunas funciones matemáticas como: `abs`, `divmod`, `hex`, `max`, `min`,...
* Hay funciones que trabajan con caracteres y cadenas: `ascii`, `chr`, `format`, `repr`,...
* Además tenemos funciones que crean o convierten a determinados tipos de datos: `int`, `float`, `str`, `bool`, `range`, `dict`, `list`, ...

Iremos estudianda cada una de las funciones en las unidades correspondientes.

## Constantes predefinidas

En el módulo [builtins](https://docs.python.org/3/library/builtins.html) se definen las siguientes constantes:

* `True` y `False`: Valores booleans
* `None` especifica que alguna variables u objeto no tiene asignado ningún tipo.

Hay alguna constante más que veremos a los largo del curso si es necesario.

## Ayuda en python

Un función fundamental cuando queremos obtener información sobre los distintos aspectos del lenguaje es `help`. Podemos usarla entrar en una sesión interactiva:

	>>> help()	

	Welcome to Python 3.4's help utility!	

	If this is your first time using Python, you should definitely check out
	the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.	

	Enter the name of any module, keyword, or topic to get help on writing
	Python programs and using Python modules.  To quit this help utility and
	return to the interpreter, just type "quit".	

	To get a list of available modules, keywords, symbols, or topics, type
	"modules", "keywords", "symbols", or "topics".  Each module also comes
	with a one-line summary of what it does; to list the modules whose name
	or summary contain a given string such as "spam", type "modules spam".

	help>

O pidiendo ayuda de una termino determinado, por ejemplo:

	>>> help(print)
