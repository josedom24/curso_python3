#!/usr/bin/env python
from persona import Persona
from notas import Notas
class Alumno(Persona,Notas):

	def __init__(self,dni,nombre,edad):
		Persona.__init__(self,dni,nombre,edad)
		Notas.__init__(self)

	def __str__(self):
		return Persona.__str__(self)+"\n"+Notas.__str__(self)