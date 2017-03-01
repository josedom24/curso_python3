# Gestionar ficheros json

El módulo [json](https://docs.python.org/3.4/library/json.html) nos permite gestionar ficheros con formato [JSON (JavaScript Object Notation)](http://json.org/).

La correspondecia entre JSON y Python la podemos resumir en la siguiente tabla:
<table>
	<tr><td>JSON</td><td>Python</td></tr>
	<tr><td>object</td><td>dict</td></tr>
	<tr><td>array</td><td>list</td></tr>
	<tr><td>string</td><td>str</td></tr>
	<tr><td>number (int)</td><td>int</td></tr>
	<tr><td>number (real)</td><td>float</td></tr>
	<tr><td>true</td><td>True</td></tr>
	<tr><td>false</td><td>False</td></tr>
	<tr><td>null</td><td>None</td></tr>
</table>

## Leer ficheros json

Desde una cadena de caracteres:

	>>> import json
	>>> datos_json='{"nombre":"carlos","edad":23}'
	>>> datos = json.loads(datos_json)
	>>> type(datos)
	<class 'dict'>
	>>> print(datos)
	{'nombre': 'carlos', 'edad': 23}

Desde un fichero:

	>>> with open("ejemplo1.json") as fichero:
	...   datos=json.load(fichero)
	>>> type(datos)
	<class 'dict'>
	>>> datos
	{'bookstore': {'book': [{'_category': 'COOKING', 'price': '30.00', 'author': 'Giada De Laurentiis', 'title': {'__text': 'Everyday Italian', '_lang': 'en'}, 'year': '2005'}, {'_category': 'CHILDREN', 'price': '29.99', 'author': 'J K. Rowling', 'title': {'__text': 'Harry Potter', '_lang': 'en'}, 'year': '2005'}, {'_category': 'WEB', 'price': '49.99', 'author': ['James McGovern', 'Per Bothner', 'Kurt Cagle', 'James Linn', 'Vaidyanathan Nagarajan'], 'title': {'__text': 'XQuery Kick Start', '_lang': 'en'}, 'year': '2003'}, {'_category': 'WEB', 'price': '39.95', 'author': 'Erik T. Ray', 'title': {'__text': 'Learning XML', '_lang': 'en'}, 'year': '2003'}]}}
	
## Escribir ficheros json

	>>> datos = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
	>>> fichero = open("ejemplo2.json","w")
	>>> json.dump(datos,fichero)
	>>> fichero.close()

	cat ejemplo2.json 
	{"miceCaught": 0, "name": "Zophie", "felineIQ": null, "isCat": true}

