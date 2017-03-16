#!/usr/bin/env python

class Dni():

	def __init__(self,numero):
		self.numero=numero

	def __calcular_letra(self):
		letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
		return letras[int(self.numero)%23]

	@property
	def numero(self):
		return self._numero

	@numero.setter
	def numero(self,numero):
		if len(numero)==8 and numero.isdigit():
			self._numero = numero
			self._letra = self.__calcular_letra()
		else: 
			raise ValueError("DNI incorecto")


	@property
	def letra(self):
		return self._letra

	def __str__(self):
		return "{0}-{1}".format(self.numero,self.letra)