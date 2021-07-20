
''' funcion De Calcular La potencia De Un Numero Optimizada '''
def poten(a, b, count = 0) :
	
	
	
	if b <= 0 :
		
		return 1
		
	elif (b % 2 == 0) :
		
		pot = poten(a, b//2, count)
		return pot * pot
		
	else :
		
		pot = poten(a, (b-1)//2, count)
		
		return pot * pot * a
		




		

def poten(a, b) :
						
	pila = [ ]
	
	while b :
						
		if b % 2 == 0 :
				
			pila.append(True)
			b //= 2
			
		else :
			
			pila.append(False)
			b = (b-1) // 2
	
	pot = 1		
	
	while pila :
						
		esPar = pila.pop()
		if esPar :
			
			pot = pot * pot
			
			
		else :
			
			pot = pot * pot * a
			
			
			
			
	return pot
			
						
						

		
		