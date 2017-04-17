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

	