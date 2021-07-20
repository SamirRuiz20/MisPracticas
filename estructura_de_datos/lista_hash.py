
class Nodo :
	
	
	
	def __init__(self, codigo = None, name = None) :
		
		self.codigo = codigo
		self.name = name
		self.next = None
		
		
		
		
		
class ListHash :
	
	
	
	def __init__(self) :
		
		
		self.start = None
		self.end = None
		self.size = 0
		
		
		
		
	def insert(self, codigo , name) :
		
		
		
		new_nodo = Nodo(codigo , name)
		
		if self.start is None :
			
			
			self.start = self.end = new_nodo
			
			
		else :
			
			
			self.end.next = new_nodo
			self.end = new_nodo
			
			
		self.size += 1
		
		
		
		
	def hash(self, codigo, size) :
		
		
		if type(codigo) is str :
			
			asciis = [ ]
			
			for i in codigo :
				
				asciis.append(ord(i))
				
			codigo = sum(asciis)
		
		
		return codigo % size
	
		
			
	
	
	def buscar(self, codigo) :
		
		
		if self.start is None :
			
			print("Error Lista Vacia")
			return False
			
			
		elif self.size > 1 :
			
			
			if self.start.codigo == codigo :
				
				print(self.start.name)
				return True
				
				
			
			aux = self.start.next
			
			while aux :
				
				if aux.codigo == codigo :
					
					print(aux.name)
					return True
					
				aux = aux.next
				
		
		
		
		
			
				
	
	def remove(self, codigo) :
		
		
		if self.start is None :
			
			print("Eror")
			return False
			
		
		elif self.size > 1 :
			
				
			if self.start.codigo == codigo :
				
				
				self.start = self.start.next
				self.size -= 1
				
				
			else :
				
				
				aux = self.start
				
				while aux.next :
					
					if aux.next.codigo == codigo :
						
						aux.next = aux.next.next
						self.size -= 1
						return True
						
					aux = aux.next
						
		
		
		else :
						
			
			if self.start.codigo == codigo :
				
				self.start = self.end = None
				self.size = 0
						
			
			
		
	
		
		
		
	
	
	def run(self) :
		
		
		aux = self.start
		
		while aux :
			
			
			print(f"{aux.codigo} : {aux.name} " , end = " -> ")
			aux = aux.next
			
			
			
			
			
hashs = [ListHash() for i in range(5)]


lista = ListHash()


while True :
	
	__import__("os").system("clear")
		
	for i in range(5) :
		
		print(f"ListaHash[{i}] = " , end = " ")
		hashs[i].run()
		
		print()
		
	print()	
	
	codigo = (input("Digite El Codigo  "))
	
	delete = (input("Desea Eliminar ese Codigo  "))
	
	
	if codigo.isdigit() :
		
		codigo = int(codigo)
	
	
	
	if delete == "s" :
		
		clave = lista.hash(codigo, len(hashs))
		hashs[clave].remove(codigo)
		
	else :
		
	
		name = input("Digite El Nombre  ")
		
		clave = lista.hash(codigo, len(hashs))
		hashs[clave].insert(codigo, name)
		
		print()
	
	contin = input("Desea Continuar  ")
	
	if contin != "s" :
		
		break
		
		
	