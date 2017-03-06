#!/usr/bin/env python

def guardar_agenda(l_agenda,**kwargs):
	l_agenda.append(kwargs)
	return l_agenda

def buscar(l_agenda,**kwargs):
	lista_aciertos=[]
	for contacto in l_agenda:
		aciertos=0
		for campo,valor in kwargs.items():
			if campo in contacto and contacto[campo]==valor:
				aciertos+=1
		if aciertos==len(kwargs):
			lista_aciertos.append(contacto)
	return lista_aciertos

def main():
	agenda=[]
	cantidad = int(input("¿Cuántos contactos vas a introducir?"))
	for i in range(cantidad):
		contacto={}
		contacto["nombre"]=input("Indica el nombre:")
		contacto["telefono"]=input("Indica el teléfono:")
		campo=input("Introuzca otro campo:")
		while campo!="*":
			contacto[campo]=input("Introuzca valor:")
			campo=input("Introuzca otro campo:")
		agenda=guardar_agenda(agenda,**contacto)
	print(agenda)
	
	## Búsqueda
	filtro={}
	campo=input("Introuzca un campo para buscar:")
	while campo!="*":
		filtro[campo]=input("Introuzca valor a buscar:")
		campo=input("Introuzca otro campo a buscar:")
	print(buscar(agenda,**filtro))

if __name__ == '__main__':
	 main()