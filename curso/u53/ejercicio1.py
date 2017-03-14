
class gato():
	def hablar(self):
		print("MIAU")

class perro():
	def hablar(self):
		print("GUAU")

def escucharMascota(animal):
	animal.hablar()

if __name__ == '__main__':
	g = gato()
	p = perro()
	escucharMascota(g)
	escucharMascota(p)
