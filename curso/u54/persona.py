#!/usr/bin/env python

class Persona():

	def __init__(self,dni,nombre,edad):
		self.dni=dni
		self.nombre=nombre
		self.edad=edad

	@property
	def dni(self):
		return self._dni

	@dni.setter
	def dni(self,dni):
		self._dni=dni

	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self,nombre):
		self._nombre=nombre	

	@property
	def edad(self):
		return self._edad

	@edad.setter
	def edad(self,edad):
		if edad>0:
			self._edad=edad	
		else:
			raise ValueError("Edad incorrecta")

	def __str__(self):
		return self.dni.__str__()+" "+self.nombre+" ("+str(self.edad)+")"


