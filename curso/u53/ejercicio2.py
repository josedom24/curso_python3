
class punto():

	def __init__(self,otro=None,x=0,y=0):
		if otro!=None:
			self.x=otro.x
			self.y=otro.y
		else:
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

class punto3d(punto):
	def __init__(self,otro=None,x=0,y=0,z=0):
		if otro!=None:
			super().x=otro.x
			super().y=otro.y
			self.z=otro.z
		else:
			super().__init__(x,y)
			self.z=z
	@property
	def z(self):
		return self._z

	@z.setter
	def z(self,z):
		self._z=z

	def __str__(self):
		return super().__str__+":"+str(self.z)

	def distancia(self,otro):
		dx = self.x - otro.x
		dy = self.y - otro.y
		dz = self.z - otro.z
		return (dx*dx + dy*dy + dz*dz)**0.5