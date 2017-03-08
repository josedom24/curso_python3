# Conceptos avanzados de programación orientada a objetos II


## Propiedades: getters, setters, deleter

Para implementar la encapsulación y no permitir el acceso directo a los atributos, podemos poner los atributos ocultos y declarar métodos especificos para acceder y modificar los atributos (mutadores). Estos métodos se denominan getters y setters.

	class circulo():
		def __init__(self,radio):
			self.set_radio(radio)
		def set_radio(self,radio):
			if radio>=0:
				self._radio = radio
			else:
				raise ValueError("Radio positivo")
				self._radio=0
		def get_radio(self):
			print("Estoy dando el radio")
			return self._radio

	>>> c1=circulo(3)
	>>> c1.get_radio()
	Estoy dando el radio
	3
	>>> c1.set_radio(-1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/home/jose/github/curso_python3/curso/u51/circulo.py", line 8, in set_radio
	    raise ValueError("Radio positivo")
	ValueError: Radio positivo

En Python, las propiedades nos permiten implementar la funcionalidad exponiendo estos métodos como atributos.