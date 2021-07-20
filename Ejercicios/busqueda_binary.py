
def busqueda_binaria( lista, x ) :
	
	izq = 0
	der = len(lista) - 1
	comp = 0
	
	while izq <= der :
		
		medio = (der + izq) // 2
		comp += 1
		
		if lista[medio] == x :
			return medio, comp
			
		elif lista[medio] > x :
			der = medio - 1
			
		else :
			izq = medio + 1
			
	return -1, comp 

 
	
def busqueda_binaria(l, n, izq, der, medio) :
	
		if l[medio] == n  :
			return medio
			
		elif izq > der :
			return -1
			
		else :
			
			if l[medio] > n :
				der = medio-1
			else :
				izq = medio + 1
				
			medio = (izq + der)//2
			
			return busqueda_binaria(l, n, izq, der, medio)			

					

lista = [ 1, 3, 5, 7, 9 , 13, 15, 17, 19 , 19, 21, 23 ]

der = len(lista)-1
izq = 0
medio = len(lista) // 2

print(busqueda_binaria( lista, 5 , izq , der, medio ))