class Cola():
	def __init__(self):
		self.cola = []

	def agregarElementoCola(self, elemento):
		self.cola.append(elemento)

	def sacarElementoCola(self):
		try:
			return self.cola.pop(0)
		except IndexError:
			return 

	def sacarNumElementosCola(self, cantidad):
		if cantidad <= len(self.cola) and cantidad > 0:
			self.cola.pop(0)
			self.sacarNumElementosCola(cantidad-1)
			

	def colaVacia(self):
		return self.cola == []

	def getElementoPosCola(self, pos):
		return self.cola[pos]

	def longitudCola(self):
		return len(self.cola)
