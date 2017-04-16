#!/usr/bin/env python
x =  input("Dame un número:")
y =  input("Dame otro número:")

try:
	result = int(x) / int(y)
except ValueError:
	print("Algún número no se puede convertir a entero")
except ZeroDivisionError:
	print("División por cero!")
else:
	print("El resultado es", result)
finally:
	print("Terminamos el programa")