class Calculadora():
	def __init__(self,nombre):
		self.nombre=nombre
	def modelo(self):
		return self.nombre
	
	@staticmethod
	def sumar(x,y):
		return x+y