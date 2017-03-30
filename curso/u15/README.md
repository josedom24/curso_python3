# Estructura de control: Alternativas

Si al evaluar la expresión lógica obtenermos el resultado True ejecuta un bloque de instrucciones, en otro caso ejecuta otro bloque.

## Alternativas simples

	if numero<0:
		print("Número es negativo")

## Alternativas dobles

	if numero<0:
		print("Número es negativo")	
	else:
		print("Número es positivo")

## Alternativas múltiples

	if numero>0:
		print("Número es negativo")	
	elif numero<0:
		print("Número es positivo")
	else:
		print("Número es cero")

## Expresión reducida del if

	>>> lang="es"
	>>> saludo = 'HOLA' if lang=='es' else 'HI'
	>>> saludo
	'HOLA'
