#!/usr/bin/env python

def guardar_agenda(l_agenda,**kwargs):
	l_agenda.append(kwargs)
	return l_agenda

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

if __name__ == '__main__':
	 main()