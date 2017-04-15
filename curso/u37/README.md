# Gestionar ficheros CSV

## Módulo CSV

El módulo [cvs](https://docs.python.org/3.4/library/csv.html) nos permite trabajar con ficheros CSV.
Un fichero CSV (comma-separated values)  son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas (o por otro carácter).

## Leer ficheros CSV

Para leer un fichero CSV utilizamos la función `reader()`:

	>>> import csv
	>>> fichero = open("ejemplo1.csv")
	>>> contenido = csv.reader(fichero)
	>>> list(contenido)
	[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
	>>> list(contenido)
	[]
	>>> fichero.close()

Podemos guardar la lista obtenida en una variable y acceder a ella indicando fila y columna.

	...
	>>> datos = list(contenido)
	>>> datos[0][0]
	'4/5/2015 13:34'
	>>> datos[1][1]
	'Cherries'
	>>> datos[2][2]
	'14'

Por supuesto podemos recorrer el resultado:

	...
	>>> for row in contenido:
		print("Fila "+str(contenido.line_num)+" "+str(row))	

	Fila 1 ['4/5/2015 13:34', 'Apples', '73']
	Fila 2 ['4/5/2015 3:41', 'Cherries', '85']
	Fila 3 ['4/6/2015 12:46', 'Pears', '14']
	Fila 4 ['4/8/2015 8:59', 'Oranges', '52']
	Fila 5 ['4/10/2015 2:07', 'Apples', '152']
	Fila 6 ['4/10/2015 18:10', 'Bananas', '23']
	Fila 7 ['4/10/2015 2:40', 'Strawberries', '98']

Veamos otro ejemplo un poco más complejo:

	>>> import csv
	>>> fichero = open("ejemplo2.csv")
	>>> contenido = csv.reader(fichero,quotechar='"')
	>>> for row in contenido:
	...   print(row)
	... 
	['Año', 'Marca', 'Modelo', 'Descripción', 'Precio']
	['1997', 'Ford', 'E350', 'ac, abs, moon', '3000.00']
	['1999', 'Chevy', 'Venture "Extended Edition"', '', '4900.00']
	['1999', 'Chevy', 'Venture "Extended Edition, Very Large"', '', '5000.00']
	['1996', 'Jeep', 'Grand Cherokee', 'MUST SELL!\nair, moon roof, loaded', '4799.00']

## Escribir ficheros CSV

	>>> import csv
	>>> fichero = open("ejemplo3.csv","w")
	>>> contenido = csv.writer(fichero)
	>>> contenido.writerow(['4/5/2015 13:34', 'Apples', '73'])
	>>> contenido.writerows(['4/5/2015 3:41', 'Cherries', '85'],['4/6/2015 12:46', 'Pears', '14'])
	>>> fichero.close()

	$ cat ejemplo3.csv
	4/5/2015 13:34,Apples,73
	4/5/2015 3:41,Cherries,85
	4/6/2015 12:46,Pears,14

