#!/usr/bin/env python
import csv
def LeerPartidos():
	"""Función que lee el fichero CSV y devuelve los datos del mismo en una 
	lista de diccionarios con los datos de la liga."""
	datos=[]
	keys=["fecha","equipo1","equipo2","final","mitad"]
	fichero = open("liga.csv")
	contenido = csv.reader(fichero)
	for row in list(contenido)[1:]:
		partido=dict(zip(keys,row))
		datos.append(partido)
	fichero.close()
	return datos

def Equipos(liga):
	"""Función que recibe la lista de diccionarios con los datos de la liga y devuelve un
	 conjunto con los equipos de la liga."""
	return(tuple(set([partido["equipo1"] for partido in liga])))


def QuienGana(resultado):
	"""Función que recibe un resultado y devuelve un 0 si es un empate, un 1 si
	 gana el equipo de casa y -1 si gana el equipo visitante."""
	golescasa=int(resultado.split("-")[0])
	golesvisitante=int(resultado.split("-")[1])
	if golescasa==golesvisitante:
		return 0
	elif golescasa>golesvisitante:
		return 1
	else:
		return -1

def Puntos(info):
	"""* `Puntos(info)`: Función que recibe una lista con los partidos ganados,
	 empatados y perdidos y devuelve los puntos obtenidos."""
	return 3*info[0]+info[2]

def InfoEquipos(liga,*equipos):
	"""Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de
	 equipos y devuelve una lista de tuplas, en cada tupla se guarda un equipo
	  con los partidos ganados, empatados y perdidos y los puntos obtenidos."""
	resultados=[]
	for equipo in equipos:
		resultado = [0,0,0]
		for partido in liga:
			#Equipo es local
			# Gana
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==1:
				resultado[0]+=1
			# Pierde
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==-1:
				resultado[1]+=1
			# Empata
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
			

			# Equipo es visitante
			# Gana
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==-1:
				resultado[0]+=1
			# Pierde
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==1:
				resultado[1]+=1
			# Empata
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
		resultado.append(Puntos(resultado))
		resultado.insert(0,equipo)
			
		resultados.append(tuple(resultado))
	return resultados

	
def Clasificacion(datos):
	"""Recibe la lista generada con la función anterior y la ordena según 
	el número de puntos."""
	datos_ordenados=datos[:]
	datos_ordenados.sort(key=lambda datos: datos[4],reverse=True)
	return datos_ordenados

def impClasificacion(liga):
	"""recibe la lista de diccionarios con losnerado a parir del fichero csv, genera los datos
	 de la clasificación y los imprime por pantalla"""
	datos=InfoEquipos(liga,*Equipos(liga))
	contador=1
	line = '-' * 61
	print(line)
	print("|   №    |     Equipo      |   PG   |   PP  |  PE   |Puntos |")
	print(line)
	for dato in Clasificacion(datos):
		print('| {0:^6} | {1:^15} | {2:^6} |{3:^6} |{4:^6} |{5:^6} |'.format(contador,dato[0],dato[1],dato[2],dato[3],dato[4]))
		contador+=1
	print(line)


if __name__ == '__main__':
	liga=LeerPartidos()
	impClasificacion(liga)






