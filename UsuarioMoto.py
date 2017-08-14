from Cola import Cola

class UsuarioMoto():
	def __init__(self, nombre, apellido, placa):
		self.nombre = nombre
		self.apellido = apellido
		self.placa = placa

cola = Cola()
colaAux = Cola()
colaAux2 = Cola()

def ImprimirCola(cola):
	for i in range(0, cola.longitudCola()):
		print "Nombre: ", cola.getElementoPosCola(i).nombre, " Apellido: ", cola.getElementoPosCola(i).apellido, " Placa: " , cola.getElementoPosCola(i).placa

print(cola.colaVacia())
cola.agregarElementoCola(UsuarioMoto("Daniela", "Cordoba", "AB123"))
cola.agregarElementoCola(UsuarioMoto("Andrea", "Acosta", "CD456"))
cola.agregarElementoCola(UsuarioMoto("Santiago", "Jimenez", "EF789"))
cola.agregarElementoCola(UsuarioMoto("Camilo", "Bonilla", "GH321"))
print(cola.colaVacia())

usuario = cola.sacarElementoCola() #Aqui sacamos uno
print "Nombre: ", usuario.nombre, " Apellido: ", usuario.apellido, " Placa: " , usuario.placa

cola.sacarNumElementosCola(2) #Aqui dos mas
ImprimirCola(cola) # imprie solo uno, el ultimo
