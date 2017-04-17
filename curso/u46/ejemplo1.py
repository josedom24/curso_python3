#!/usr/bin/env python
def operar(n1,n2,operador='+',respuesta='El resultado es '):
	if operador=="+":
		return respuesta+str(n1+n2)
	elif operador=="-":
		return respuesta+str(n1-n2)
	else:
		return "Error"