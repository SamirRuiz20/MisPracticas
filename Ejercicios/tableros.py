



def tablero_per( long , t) :
	p = " "
	casilla = 0
	tab = 0
	if long == 3 :
		espa = 15
		spac = 8
		fill = 5
		
	elif long == 4 :
		espa = 10
		spac = 7
		fill = 4
		
	elif long == 5 :
		espa = 8
		spac = 6
		fill = 4
	
	
	
	for x in range(long) :
		
		for j in range(fill) :
			print(f"{p:>{espa}}", end = "")
			for i in range(long) :
				#casilla += 1
				
				if j == 0 :
					casilla += 1
					print(f"  {casilla:<{spac}}", end  = "|" if i != long-1 else "")
					
				elif j == 2 :
					
					print(f"{t[tab]:^{spac+2}}", end = "|" if i != long-1 else "")
					tab += 1
							
				else :
					print(f"  {p:<{spac}}", end = "|" if i != long-1 else "")
			print()
			
		
		if x != long-1 :
	
			g = "-"*(spac+2)
			print(f"{p:>{espa}}", end = "")	
			for k in range(long) :
				
				print(f"{g}", end = "±" if k != long-1 else "")
				
			print() 


		



def tablero_matriz(t) :
	'''
	devuelve un tablero
	'''
	long = len(t)
	
	p = " "
	casilla = 0
	tab = 0
	fila = 0
	
	
	if long == 3 :
		espa = 14
		spac = 8
		fill = 4
		
	elif long == 4 :
		espa = 10
		spac = 7
		fill = 4
		
	elif long == 5 :
		espa = 8
		spac = 6
		fill = 4
	
	
	def line() :
		g = "-"*(spac+2)
		print(f"{p:>{espa}}", end = "±")	
		for k in range(long) :
					
			print(f"{g}", end = "±" )
					
		print()
	print(f"{p:{espa}}" , end = " ")	
	for i in range(long) :
		casilla += 1
		print(f"{casilla:^{spac+2}}", end = " ")
				 	 	
	print()
	line() 
	casilla = 0					
	
	for x in range(long) :
		casilla += 1
		
		
		for j in range(fill) :
			print(f"{p:>{espa}}" if j != 2 else f"{casilla:{espa-1}} " , end = "|")
			row = 0
			for i in range(long) :
				 
					
				if j == 2 :
					
					print(f"{t[fila][row]:^{spac+2}}", end = "|")
					row += 1
							
				else :
					print(f"  {p:<{spac}}", end = "|")
			print()
			
		fila += 1
			
		

	
		line()					
												
t = [["^_^"] * 3] * 3
l = len(t)

tablero_matriz(t)