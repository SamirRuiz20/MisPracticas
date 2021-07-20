
from doctest import testmod




''' Creacion De La Clase Matriz '''	


class Matriz :
	
	
	
	
	def __init__(self, lista) :
		
	    
	    valida = self.validaUna(lista)
	    
	    if valida == True :
	    	
	    	self.lista = lista
	    	self.value = True

	    	
	    else :
	    	
	    	#print(valida)
	    	self.value = False
	    
	    	
	    		
	
	 
		    			
	@classmethod
	def validaUna(cls, lista) :
		
		
		
		if type(lista) is list :
			
			
			if all([ type(i) is list for i in lista ]) and len(lista) > 0 :
				
				longs = [len(i) for i in lista]
				if len(longs) == longs.count(longs[0]) :
					
					
					if longs[0] > 0 :
						
						return True
					
					else :
						
						return "Las sublistas no deben estar vacias"
						
					
				else :
					
					return "Las Sublistas deben ser de misma Longitud"
				
				
			else :
				
				return "La lista debe contener Sublistas"
		
				
		else :
			
			return f"El Argumento lista debe ser de tipo list no {lista.__class__} "
			
	
	
	
	
	
	@classmethod
	def validaDos(cls, lista1, lista2) :
		
		
		
		if type(lista1) is list and type(lista2) is list :
			
			
			if (all([type(i) is list for i in lista1]) and len(lista1) > 0 )  and \
			(all([type(i) is list for i in lista2]) and len(lista2) > 0 ) :
				
				
				long_l1 = [len(i) for i in lista1]
				long_l2 = [len(i) for i in lista2]
				
				if len(long_l1) == long_l1.count(long_l1[0]) and len(long_l2) == long_l2.count(long_l2[0]) :
					
					if long_l1[0] > 0 and long_l2[0] :
						
						return True
						
					else :
						
						return "Por Favor no ingresar las listas con sublistas vacias"
					
					
				else :
					
					
					return "La longitud de las sublistas deben ser de igual tamaño"
				
				
			else :
						
				
				return "Ambos argumentos deben contener sublistas"
						
			
		else :
			
			
			return "Ambas argumentos deben ser de tipo lista"
			
			
	
	
	
		
	#metodo __str__ imprimira la matriz
	def __str__(self) :
		
		
		if self.value :
			
			
			for i in range(len(self.lista)) :
				
				print("[ ", end = "")
				
				for j in range(len(self.lista[0])) :
					
					print(f"{self.lista[i][j]:^5}", end = " ")
					
				print("]")
				
			return ""
			
			
		else :
			
			
			return "OUTPUT_ERROR.!"
			
	
	
	
	
	
	#metodo que se encargara de sumar las listas una vez validadas a matrices y retornando una matriz con la suma de las dos matrices 
	@classmethod
	def sumar(cls, lista1, lista2) :
		
		
		
		validar = cls.validaDos(lista1, lista2)
		
		if validar == True :
			
			
			if len(lista1) == len(lista2) and len(lista1[0]) == len(lista2[0]) :
				
				
				suma = [[lista1[j][i] + lista2[j][i] for i in range(len(lista1[0]))] for j in range(len(lista1))]
				
				return cls(suma)
				
				
			else :
				
				
				return "las matrices no se pueden sumar por que son de diferente tamaño"
			
			
		else :
			
			
			return validar
			
	
	
	
	
	
	#metodo que devuelve la multiplicacion de dos matrices
	@classmethod
	def producto(cls, lista1, lista2) :
		
		
		validar = cls.validaDos(lista1, lista2)
		
		if validar == True :
			
			
			if len(lista1[0]) == len(lista2) :
				
				
				producto = []
				
				for i in range(len(lista1)) :
					
					producto.append([])
					for j in range(len(lista2[0])) :
						
						producto[i].append(0)
				
				for i in range(len(producto)) :
					
					for j in range(len(producto[0])) :
						
						for k in range(len(lista1[0])) :
							
							producto[i][j] += lista1[i][k] * lista2[k][j]
							
						
				return cls(producto)		
				
				
				
			else :
				
				return "Las Matrices no pueden ser multiplicadas"
			
			
		else :
			
			
			return validar
			
	
	
	
	
	
	#metodo que devuelve la transpuesta de una matriz
	@classmethod
	def transpuezta(cls, lista) :
			
			
			validar = cls.validaUna(lista)
			
			if validar == True :
				
				
				transpuezta = [[lista[i][j] for i in range(len(lista))] for j in range(len(lista[0]))]
				
				return cls(transpuezta)
				
				
			else :
				
				
				return validar
				
	
	
	
	
	
	#metodo que rota una matriz a la direccion pasada al parametro side los argumentos validos son :               R -> para rotar a la derecha rotacion horaria                           L -> a la izquierda rotacion antihoraria
	@classmethod
	def rotar_matriz(cls, lista, * , side = "R") :
			
			
			side = side.upper()
			
			if side not in ("R", "L") :
				
				return "SIDE_ERROR.!"
				
				
				
			validar = cls.validaUna(lista)
			
			if validar == True :
				
				
				rotada = []
				
				for i in range(len(lista[0])) :
					
					rotada.append([])
					
					for j in range(len(lista)) :
						
						if side == "I" :
							
							value = lista[j][len(lista[0]) - 1 - i]
							
						else :
							
							value = lista[len(lista) -1 - j][i]
							
						rotada[i].append(value)
						
					
				return cls(rotada)
				
				
			else :
				
				
				return validar 



	@classmethod
	def equal(cls, lista1, lista2) :

		

		if ( (type(lista1) is Matriz and type(lista2) is Matriz) and (lista1.value == True and lista2.value == True ) ) :


			lista1 = lista1.lista
			lista2 = lista2.lista 
			validas = True
			

		else :

			validas = cls.validaDos(lista1, lista2) 

		if validas == True :

			if len(lista1) == len(lista2) and len(lista1[0]) == len(lista2[0]) :

				for i in range(len(lista1)) :
					for j in range(len(lista1[0])) :

						if lista1[i][j] != lista2[i][j] :

							return False

				return True 

			return False

			

		else :

			return "Los argumentos deben ser matrices"





	def potencia(cls, lista, exp = 0) :


		pass
			
			
			

		

				

def test() :
						
	'''
	>>>
	>>> test()
	False
	>>> 
	'''

						
	matriz = Matriz.equal( [[1, 2], [3, 4]], [[1, 2, 7], [3, 4, 5]])  
	
	print(matriz) 
								
						

testmod()  


'''
matriz = Matriz([[28281, 28288, 38282], [4, 5, 6], [7, 8, 9]])

print(matriz)
'''






#jeseabad@gmail.com


