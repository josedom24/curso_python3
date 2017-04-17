class Alumno():
	contador=0
	def __init__(self,nombre=""):
		self.nombre=nombre
		Alumno.contador+=1