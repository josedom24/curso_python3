#!/usr/bin/env python
import csv
def LeerPartidos():
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
	return(list(set([partido["equipo1"] for partido in liga])))

def InfoEquipos(equipo,liga):
	if equipo in Equipos(liga):
		resultado = [0,0,0]
		for partido in liga:
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==1:
				resultado[0]+=1
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==-1:
				resultado[1]+=1
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==-1:
				resultado[0]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==1:
				resultado[1]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
		return resultado
	else:
		return []

def QuienGana(resultado):
	golescasa=int(resultado.split("-")[0])
	golesvisitante=int(resultado.split("-")[1])
	if golescasa==golesvisitante:
		return 0
	elif golescasa>golesvisitante:
		return 1
	else:
		return -1

def Puntos(info):
	return 3*info[0]+info[2]


liga=LeerPartidos()
print(Equipos(liga))
print(InfoEquipos("Barcelona",liga))

for e in Equipos(liga):
	print(e,Puntos(InfoEquipos(e,liga)))

