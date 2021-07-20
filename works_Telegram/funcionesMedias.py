
def run(l, n) :
	
	if len(l) < n :
		
		n = n - len(l)
	
	for i in range(-1, -n-1, -1) :
		
		new = l.pop()
		
		l.insert(0, new)
		
		
# funcion que aplana una lista qje tiene sublistas		
l = [[1, 2, [40, 50, [60, 70]]], 8, [3, 4, [7, 10]]]


def listaplana(l) :
	
	plana = []
	
	for el in l :
		
		if type(el) != list :
			
			plana.append(el)
			
		else :
			
			
			p = listaplana(el)
			plana += p
			
						
	return plana

	

			

									
																											

#Funcion Que borra los elementos repetidos de una lista			
def delRepeat(l) :
			
		for i in list(l) :
			
			while l.count(i) != 1 :
				
					l.remove(i)
						
			

			
									
									
def fun(n) :
	
	#global a
	#print(a)
	
	a = []
	
	for i in range(2) :
		#print(a)
	
		if n :
			
			a.append(i+n)
			
			
		else :
			a = a + fun(1)
			
		
		
	return a	
	



def a_matriz(l, sublist = 2) :	
	if sublist == 0 :
		
		return l
		
	subs = len(l) % sublist
	a = len(l) // sublist

	matriz = [ ]
	
	if (subs == 0) :
		
		for i in range(0, len(l), a) :
			
			matriz.append(l[i:i+a])
			
		return matriz
				
	else :
		
		return "No Pueden Haber sublustas de tal tamaño"
		
		
		
		
		
		
		
def types(l) :
		
		lista = [ ]
		
		for i in l :
			
			if str(type(i)) in lista :
				
				continue
				
			lista.append(str(type(i)))
		
		return lista, len(lista)
		
		

				
b = [1, 2, 1, 1, "A", "C", "D", "B", True, 2+0j]

s = "\n"
l = [3, 6, 3+0j, "A", 3.5, 8, True]
tipos, cant = types(l)
print(f"Hay {cant} tipos de datos y son :\n{s.join(tipos)}")
			
			