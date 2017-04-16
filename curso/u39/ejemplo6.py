
def nivel(numero):
	if numero<0:
		raise ValueError("El número debe ser positivo:"+str(numero))
	else:
		return numero

print(nivel(5))
print(nivel(-1))