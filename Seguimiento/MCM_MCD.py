def MCD(a, b) :
	
	while b :
		
		a, b = b, a%b
		
	return a
	
	
	
def MCM(a, b) :
	
	return (a*b) // MCD(a, b)
	
print(MCM(172771, 17824))


