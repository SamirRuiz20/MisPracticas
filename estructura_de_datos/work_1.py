
class Nodo :
	
	
	def __init__(self, data) :
		
		self.data = data
		self.next = None
		
		
		
		




class ListCircSimple :
	
	
	
	def __init__(self) :
		
		self.start = None
		self.end = None
		self.dia = None
		
		
		
	def add_first(self, data) :
		
		if self.start is None :
			
			self.start = self.end = Nodo(data)
			self.end.next = self.start
			
		else :
			
			new_nodo = Nodo(data)
			new_nodo.next = self.start
			self.start = new_nodo
			self.end.next = self.start
		
		
	
	def search(self, data) :
		
		
		if self.start is None :
			
			print("Lista Vacia")
			return None
			
			
		else :
			
			aux = self.start
			
			while aux :
				
				if aux.data == data :
					
					self.dia = aux.next
					#self.dia.next = aux.next.next
					#aux.next = self.dia
					
					return True
					
				aux = aux.next
				
				if aux == self.start :
					
					return False
					
					
					
					
	def run(self) :
					
		aux = self.dia
		
		while aux :
					
			print(aux.data)
			
			aux = aux.next
			
			
			if aux == self.dia :
					
					return None
					
					
		

		
a = ListCircSimple()

a.add_first("Lunes")
a.add_first("Martes")
a.add_first("Miercoles")
a.add_first("Jueves")
a.add_first("Viernes")
a.add_first("Sabado")
a.add_first("Domingo")

a.search("Domingo")
a.run() 		