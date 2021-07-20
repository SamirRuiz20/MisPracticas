'''   Determinante de matrices   '''
from copy import deepcopy









def mul_diag(m) :
	
	mul = 1
	for i in range(len(m)) :
		mul *= m[i][i]
	return mul


def is_triangular( m ) :
	
	for i in range(len(m)) :
		for j in range(len(m)) :
			if i > j :
				if m[i][j] != 0 :
					return False
	return True 
					



def Determinante( m ) :
	
	for i in range(len(m)) :
		if 0 in m[i] :
			if m[i].count(0) == len(m) :
				return 0
				
	
	cont = 0
	for i in range(len(m)) :
		for j in range(len(m)) :
			if m[j][i] == 0 :
				cont += 1
				
		if cont == len(m) :
			return 0
		else :
			cont = 0
		
	
	m = deepcopy(m) 
	column = 0
	signo = 1
					
	for i in range(1, len(m)) :
		
		
		if is_triangular(m) :
				return signo * round(mul_diag(m), 5)
		
			
		if m[i-1][i-1] == 0 :
			for k in range(i, len(m)) :
				if m[k][i-1] != 0 :
					m[i-1], m[k] = m[k], m[i-1]
					signo *= -1 
					
			
		
						
		for j in range(i, len(m)) :
			
			if m[j][column] == 0 :
				
				continue 	
			
			
			div = round(m[j][column] / m[column][column], 8) 
			

			for k in range(column, len(m)) :
									
				re = round(m[j][k]- (m[column][k] * div), 5)
				m[j][k] = re	
		
			
		column += 1
		
		
	return signo * round(mul_diag(m), 5)


				
								
	
									
			
														
												
		
		
m = [
	[0, 5, 8, 7],	
	[0, 6, 0, 0],
	[8, 4, 8, 0],
	[0, 5, 0, 0] 	

] 

