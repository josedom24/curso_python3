#!/usr/bin/env python

def calcular_segundos(horas,minutos,segundos):
	return horas*3600+minutos*60+segundos

def calcular_horas(segundos):
	horas = segundos // 3600
	segundos-=horas*3600
	minutos = segundos // 60
	segundos-=minutos*60
	return horas,minutos,segundos

if __name__ == '__main__':
	print(calcular_segundos(4,12,23))
	hora=map(str,calcular_horas(12345))
	print(":".join(hora))

