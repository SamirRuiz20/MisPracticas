
import sys
import time



def torre(n, * , side = "C", rows = 1) :
	
	if side == "C" :
		separ = 29
	elif side == "L" :	
		separ = n*2-1
		
	''' esto es solo un adorno en la cima '''
	print(" "*(separ-1)+"|")
	print(" "*(separ-3)+"-----")
	print(" "*(separ-1)+"|")
	''' ------------------ '''
	
	return "\n".join([" "*(separ-(i+1+i)
	) + "."*(i+1+i*3) for i in range(n) for j in range(rows)])
	
	
print(torre(10, rows = 1, side = "C"))
	
			
	

def crespas(n) :
	
	return "\n".join( [
	(" "*(6-i+1) + "*"*(i+1+i) + " "*(n-i+1))*n for i in range(5)
	] )
	
	







print()


def crespas(n, *, rows = 6 ) :
	
	if n <= 0 :
		return ""
	
	e = " "
	x = rows-1
	
	return  "\n".join(
	     [
	    f"{e:>{x}}*{e:>{x}}"*n if i == 0 \
	     else f"{e*(x-(i))}*{e*(1+(i+i-2))}*{e*(x-(i))}"*n for i in range(rows)
	
	     ]
	     	)              	










def crespas(n) :
	
	
	rows = 6
	sep = (rows-1)*2
	
	lista = [" "]
	lista.extend([" "]* sep * n )
	
	listaR = [ ]
	
	for i in range(rows) :
		print(lista, lista.__len__())
		input()
		
		lista = [ " " if x == "*" else x for x in lista ]
	
		
		for j in range(n) :
			
			__import__("os").system("clear")
		
			
			pos = (sep//2)*(2*j+1)
			lista[pos-i] = "*"
			lista[pos+i] = "*"
			
			print(lista, pos, i)
			input() 
			
		print("Salio")
		print("".join(lista))
		listaR.append("[" + "".join(lista) + "]")
		
	
	return listaR