class punto():

	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self,x):
		self._x=x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self,y):
		self._y=y

	def __str__(self):
		return "{0}:{1}".format(self.x,self.y)

	def distancia(self,otro):
		dx = self.x - otro.x
		dy = self.y - otro.y
		return (dx*dx + dy*dy)**0.5


class circulo():

	def __init__(self,centro,radio):
		self.centro=centro
		self.radio=radio

	def __str__(self):
		return "Centro:{0}-Radio:{1}".format(self.centro.__str__(),self.radio)


