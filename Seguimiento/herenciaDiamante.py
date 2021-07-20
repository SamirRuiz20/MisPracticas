
''' Problema de Diamante
            A
           / \
          B   C
          \   /
            D
            '''

class A :
	
	
	def __init__(self) :
		
		pass
		
	def __str__(self) :
		
		return f"<class {self.__class__.__qualname__!r}>..."
		
		
	def __repr__(self) :
		
		return f"<class {self.__class__.__qualname__!r}>"
		
		

		
				
								
class B(A) :
	
	
	def __init__(self) :
		
		pass
		
		
	def foo(self) :
		
		print("Hola Desde B")
		
		
		
class C(A) :
	
	
	def __init__(self) :
		
		pass
		
		
		
		
class D(B, C) :
	
	def __init__(self) :
		
		pass
		
	def bar(self) :
		
		super().foo()



''' ---_--_---_----_--'''



class Mapping :
	
	def __init__(self) :
		
		pass
		
	def update(self, m) :
		
		return f"Hola {m}"
		
		
	__update = update
	

	
			
	
class SubMapp(Mapping) :
	
	def __init__(self) :
		
		pass
		
	
	def update(self, n1, n2) :
		
		return f"Hola {n1} - {n2}"
		
		
	__update = update
		
		
		
a = SubMapp()
b = a._SubMapp__update


''' __iter__     __next__ '''



class Reverse :
	
	def __init__(self, data) :
		
		self.data = data
		self.index = len(data)
		
	
			
	def __next__(self) :
		
		
		
		if len(self.data) == 0 :
			
			raise StopIteration
			
			
		v = self.data[-1]
		self.data = self.data[:len(self.data)-1]
		
		return v
		
	
		
				
	def __iter__(self) :
		
		return self
		
		
		
a = Reverse("Hola")
b = iter(a)

for i in a :
	
	print(i)
	