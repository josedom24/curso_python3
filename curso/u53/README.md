# Polimorfismo, herencia y delegación
	
## Polimorfismo

El polimorfismo es la técnico que nos posibilita que al invocar un determinado método de un objeto, podrán obtenerse distintos resultados según la clase del objeto. Esto se debe a que distintos objetos pueden tener un método con un mismo nombre, pero que realice distintas operaciones.

Lo llevamos usando desde principio del curso, por ejemplo podemos recorrer con una estructura `for` distintas clases de objeto, debido a que el método especial `__iter__` está definida en cada una de las clases. Otro ejemplo sería que con la función `print` podemos imprimir distintas clases de objeto, en este caso, el método especial `__str__` está definido en todas las clases.

Además esto es posible a que python es dinámico, es decir en tiempo de ejecución es cuando se determina el tipo de un objeto. Veamos un ejemplo:

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

## Herencia

La herencia es un mecanismo de la programación orientada a objetos que sirve para crear clases nuevas a partir de clases preexistentes. Se toman (heredan) atributos y métodos de las clases viejas y se los modifica para modelar una nueva situación.

La clase vieja se llama clase base y la que se construye a partir de ella es una clase derivada.

