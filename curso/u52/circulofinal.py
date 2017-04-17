class circulo():
	def __init__(self,radio):
		self.radio=radio  ## Este el setter
	
	@property
	def radio(self):
		print("Estoy dando el radio")
		return self._radio

	@radio.setter
	def radio(self,radio):
		if radio>=0:
			self._radio = radio
		else:
			raise ValueError("Radio positivo")
			self._radio=0
	
	@radio.deleter
	def radio(self):
		del self._radio

	def __str__(self):
		clase = type(self).__name__
		msg = "{0} de radio {1}"
		return msg.format(clase, self.radio)

	def __repr__(self):
		clase = type(self).__name__
		msg = "{0}({1})"
		return msg.format(clase, self.radio)

	def __eq__(self,otro):
		return self.radio==otro.radio

	def __add__(self,otro):
		self.radio+=otro.radio

	def __sub__(self,otro):
		if self.radio-otro.radio>=0:
			self.radio-=otro.radio
		else:
			raise ValueError("No se pueden restar")