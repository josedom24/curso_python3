# Polimorfismo, herencia y delegación
	
## Polimorfismo

El polimorfismo es la técnica que nos posibilita que al invocar un determinado método de un objeto, podrán obtenerse distintos resultados según la clase del objeto. Esto se debe a que distintos objetos pueden tener un método con un mismo nombre, pero que realice distintas operaciones.

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

La clase desde la que se hereda se llama clase base y la que se construye a partir de ella es una clase derivada.

Si nuestra clase base es la clase `punto` estudiadas en unidades anteriores, puedo crear una nueva clase de la siguiente manera:

	class punto3d(punto):
		def __init__(self,x=0,y=0,z=0):
			super().__init__(x,y)
			self.z=z
		@property
		def z(self):
			return self._z	

		@z.setter
		def z(self,z):
			self._z=z	

		def __str__(self):
			return super().__str__()+":"+str(self.z)	

		def distancia(self,otro):
			dx = self.x - otro.x
			dy = self.y - otro.y
			dz = self.z - otro.z
			return (dx*dx + dy*dy + dz*dz)**0.5	

Creemos dos objetos de cada clase y veamos los atributos y métodos que tienen definido:

	>>> p=punto(1,2)
	>>> dir(p)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', '_y', 'distancia', 'x', 'y']
	>>> p3d=punto3d(1,2,3)
	>>> dir(p3d)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', '_y', '_z', 'distancia', 'x', 'y', 'z']

## La función super()

La función `super()` me proporciona una referencia a la clase base. Y podemos observar también que hemos reescrito el método `distancia` y `__str__`.

	>>> p.distancia(punto(5,6))
	5.656854249492381
	>>> p3d.distancia(punto3d(2,3,4))
	1.7320508075688772
	>>> print(p)
	1:2
	>>> print(p3d)
	1:2:3

## Herencia múltiple

La herencia múltiple se refiere a la posibilidad de crear una clase a partir de múltiples clases superiores. Es importante nombrar adecuadamente los atributos y los métodos en cada clase para no crear conflictos.

	class Telefono:
	    "Clase teléfono"
	    def __init__(self,numero):
	        self.numero=numero
	    def telefonear(self):
	        print('llamando')
	    def colgar(self):
	        print('colgando') 
	    def __str__(self):
	        return self.numero	

	class Camara:
	    "Clase camara fotográfica"
	    def __init__(self,mpx):
	        self.mpx=mpx
	    def fotografiar(self):
	        print('fotografiando')        
	    def __str__(self):
	        return self.mpx
	class Reproductor:
	    "Clase Reproductor Mp3"
	    def __init__(self,capcidad):
	        self.capacidad=capcidad
	    def reproducirmp3(self):
	        print('reproduciendo mp3')                  
	    def reproducirvideo(self):
	        print('reproduciendo video')                  
	    def __str__(self):
	        return self.capacidad	

	class Movil(Telefono, Camara, Reproductor):
	    def __init__(self,numero,mpx,capacidad):
	        Telefono.__init__(self,numero)
	        Camara.__init__(self,mpx)
	        Reproductor.__init__(self,capacidad)
	    def __str__(self):
	        return "Número: {0}, Cámara: {1},Capacidad: {2}".format(Telefono.__str__(self),Camara.__str__(self),Reproductor.__str__(self))

Veamos los atributos y métodos de un objeto `Movil`:

	>>> mimovil=Movil("645234567","5Mpx","1G")
	>>> dir(mimovil)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'capacidad', 'colgar', 'fotografiar', 'mpx', 'numero', 'reproducirmp3', 'reproducirvideo', 'telefonear']
	>>> print(mimovil)
	Número: 645234567, Cámara: 5Mpx,Capacidad: 1G

## Funciones issubclass() y isinstance() 

La función `issubclass(SubClase, ClaseSup)` se utiliza para comprobar si una clase (SubClase) es hija de otra superior (ClaseSup), devolviendo True o False según sea el caso. 

	>>> issubclass(Movil,Telefono)
	True

La función booleana `isinstance(Objeto, Clase)` se utiliza para comprobar si un objeto pertenece a una clase o clase superior. 

	>>> isinstance(mimovil,Movil)
	True

## Delegación

Llamamos delegación a la situación en la que una clase contiene (como atributos) una o más instancias de otra clase, a las que delegará parte de sus funcionalidades.

A partir de la clase `punto`, podemos crear la clase `circulo` de esta forma:

	class circulo():	

		def __init__(self,centro,radio):
			self.centro=centro
			self.radio=radio	

		def __str__(self):
			return "Centro:{0}-Radio:{1}".format(self.centro.__str__(),self.radio)	

Y creamos un objeto `circulo`:

	>>> c1=circulo(punto(2,3),5)
	>>> print(c1)
	Centro:2:3-Radio:5
