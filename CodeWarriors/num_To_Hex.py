 
def to_hex( decimal ) :
	
	if decimal == 0 :
		
		return 0
	
	sig = False	
	if decimal < 0 :
		sig = True
		decimal = abs(decimal) 
		
	let = "a b c d e f".split()
	
	hexa = [ ]
	
	while decimal > 0 :
		
		cociente , resto = divmod(decimal, 16)
		
		if resto > 9 :
			v = let[resto - 10]
			
		else :
			v = resto
			
		decimal = cociente 
			
		hexa.append(str(v))
		
	hexa.reverse()
	
	return ("-" if sig else "") + "".join(hexa)
	
print(to_hex(7))