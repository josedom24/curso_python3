#!/usr/bin/env python
cad =  input("Dame un número:")
try:
	print (10/int(cad))
except ValueError:
	print("No se puede converir a entero")
except ZeroDivisionError:
	print("No se puede divir por cero")
except:
	print("Otro error")