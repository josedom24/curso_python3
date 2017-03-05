# Conceptos avanzados sobre funciones

## Tipos de argumentos: posicionales o keyword

Tenemos dos tipos de parámetros: los posiciónales donde el parámetro real debe coincidir en posición con el parámetro formal:

	>>> def sumar(n1,n2):
	...   return n1+n2
	... 
	>>> sumar(5,7)
	12
	>>> sumar(4)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: sumar() missing 1 required positional argument: 'n2'

Además podemos tener parámetros con valores por defecto:

	>>> def operar(n1,n2,operador='+',respuesta='El resultado es '):
	...   if operador=="+":
	...     return respuesta+str(n1+n2)
	...   elif operador=="-":
	...     return respuesta+str(n1-n2)
	...   else:
	...     return "Error"
	... 
	>>> operar(5,7)
	'El resultado es 12'
	>>> operar(5,7,"-")
	'El resultado es -2'
	>>> operar(5,7,"-","La resta es ")
	'La resta es -2'


Los parámetros keyword donde se indican el nombre del parámetro formal y su valor, por lo tanto no es necesario que tengan la misma posición. Al definir una función o al llamarla, hay que indicar primero los argumentos posicionales y a continuación los argumentos con valor por defecto (keyword). 

	>>> operar(5,7)										# dos parámetros posicionales
	>>> operar(n1=4,n2=6)								# dos parámetros keyword
	>>> operar(4,6,respuesta="La suma es")				# dos parámetros posicionales y uno keyword
	>>> operar(4,6,respuesta="La resta es",operador="-")# dos parámetros posicionales y dos keyword




## Argumentos arbitrarios (*args y **kwargs)

## Desempaquetar argumentos: pasar listas y diccionarios

## Parametro *

## Devolver múltiples resultados