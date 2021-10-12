
from copy import deepcopy

		
def adjunta(m , fila , column) :
	
	return  [ [ m[i][j] for j in range(len(m)) if j != column ] for i in range(len(m)) if i != fila ]
	

	
def determinante( m ) :
	
	if len(m) == 2 :
		
		return m[0][0] * m[1][1] - m[0][1] * m[1][0]
		
	else :
		
		fila = 0
		
		
		
		
		det = 0
		
		for j in range( len(m) ) :
			
			adj = adjunta(m, fila, j)
			
			det += (pow(-1, fila+j) * m[fila][j] ) * determinante(adj)
			
		return det
				
	
	
	
	
m = [
	[10, 2, 3, 4, 5],
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20],
	[25, 22, 23, 24, 20]
]

'''m = [
	[0, -4, -5],
	[0, -6, 2],
	[8, 3, -5]
]'''


print("\n".join([ str(i) for i in m ]))

print()

print(determinante( m ))


