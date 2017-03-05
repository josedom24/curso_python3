#!/usr/bin/env python
import math
class punto():
	""" Representación de un punto en el plano, los atributos son x e y
	que representan los valores de las coordenadas cartesianas."""

	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	
	def distancia(self, otro):
		""" Devuelve la distancia entre ambos puntos. """
		dx = self.x - otro.x
		dy = self.y - otro.y
		return math.sqrt((dx*dx + dy*dy))

if __name__ == '__main__':
	
	punto1=punto()
	punto2=punto(4,5)
	print(punto1.distancia(punto2))
