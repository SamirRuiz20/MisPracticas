
class Error(Exception) :
	
	pass
	
class InputError(Error) : 
	
	def __init__(self , expr, messa) :
		
		self.expr = expr
		self.messa = messa
		
		
class TransitionError(Error) :
	
	def __init__(self, *args, **kwargs) :
		
		self.arg = args
		self.k = kwargs
		
raise TransitionError("Un Error", a = "Error", b = "Other")

a = [1, 2, 3, 4]

print(*a)