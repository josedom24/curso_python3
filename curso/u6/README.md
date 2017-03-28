# Estructura del programa

* Un programa python está formado por instrucciones que acaban en un caracter de "salto de línea". 
* El punto y coma “;” se puede usar para separar varias sentencias en una misma línea, pero no se aconseja su uso.
* Una línea empiza en la primera posición, si tenemos instrucciones dentro de un bloque de una estrucura de control de flujo habra que hacer una identación.
* La identación se puede hacer con espacios y tabulaciones pero ambos tipos no se pueden mezclar. Se recomienda usar 4 espacios.
* La barra invertida "\\" al final de línea se emplea para dividir una línea muy larga en dos o más líneas.
* Las expresiones entre paréntesis "()", llaves "{}" y corchetes "[]" separadas por comas "," se pueden escribir ocupando varias líneas.
* Cuando el bloque a sangrar sólo ocupa una línea ésta puede escribirse después de los dos punto.

## Comentarios

Se utiliza el caracter `#` para indicar los comentarios.

## Palabras reservadas

	False      class      finally    is         return
	None       continue   for        lambda     try
	True       def        from       nonlocal   while
	and        del        global     not        with
	as         elif       if         or         yield
	assert     else       import     pass
	break      except     in         raise

## Ejemplo

	#!/usr/bin/env python	

	# Sangrado con 4 espacios	

	edad = 23
	if edad > =18:
	   print('Es mayor de edad')  
	else:
	   print('Es menor de edad')	

	# Cada bloque de instrucciones dentro de una estructura de control
	# debe estar tabulada	

	if num >=0:
		while num<10:
			print (num)
			num = num +1	

	# El punto y coma “;” se puede usar para separar varias sentencias 
	# en una misma línea, pero no se aconseja su uso.	

	edad = 15; print(edad)	

	# Cuando el bloque a sangrar sólo ocupa una línea ésta puede
	# escribirse después de los dos puntos:   	

	if azul: print('Cielo')	

	# La barra invertida “\” permite escribir una línea de
	# código demasiado extensa en varias líneas:	

	if condicion1 and condicion2 and condicion3 and \  
	    condicion4 and condicion5:	

	# Las expresiones entre paréntesis, llaves o corchetes pueden 
	# ocupar varias líneas:	

	dias = ['lunes', 'martes', 'miércoles', 'jueves',
	        'viernes', 'sábado', 'domingo'] 
