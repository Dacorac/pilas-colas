from Pila import Pila

class Libro():
	def __init__(self, nombre, autor):
		self.nombre = nombre
		self.autor = autor

	def imprimirLibro(self):
		print self.nombre, "-" , self.autor

pila = Pila()
pilaAux = Pila() 
pilaAux2 = Pila()

def buscarLibrosAutor(pila, autor):
	for i in range(0, pila.longitudPila() ):
		if pila.getElementoPos(i).autor == autor:
			pilaAux.agregarElemento(pila.sacarElementoPos(i))
			buscarLibrosAutor(pila, autor)
			break
	return pilaAux		

def buscarLibrosNombre(pila, nombre):
	for i in range(0, pila.longitudPila()):
		if pila.getElementoPos(i).nombre == nombre:
			pilaAux2.agregarElemento(pila.sacarElementoPos(i))
			buscarLibrosNombre(pila, nombre)
			break
	return pilaAux2

pila.agregarElemento(Libro("It", "Stephen King"))
pila.agregarElemento(Libro("Cujo", "Stephen King"))
pila.agregarElemento(Libro("Matar a un Ruiseñor", "Harper Lee"))
pila.agregarElemento(Libro("Carrie", "Stephen King"))
pila.agregarElemento(Libro("Suave es la noche", "F. Scott Fitzgerald"))
pila.agregarElemento(Libro("1984", "George Orwell"))

pila2 = buscarLibrosAutor(pila, "Stephen King")
libro = pila2.getElementoPos(2)
libro.imprimirLibro()
pila3 = buscarLibrosNombre(pila2, "Carrie")
libro = pila3.getElementoPos(0)
libro.imprimirLibro()