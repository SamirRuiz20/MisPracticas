

'''

pedir un numero de 4 digitos
adivinar el resultado final y mostrarlo
pedir otro numero de 4 digitos
agregar un numero de 4 cifras que sume 9 con cada cifra del numero anterior 
ejem 
 user = 2345
 pc   = 7654
 ...
 
pedir otro numero al usuario
agregar otro numero
a la suma

comprobar la adivinanza
mostrarlo ...

'''


first = (input("Primer Numero  "))

if first in ("0000", "0001") :
	
	result = "19998" if first == "0000" else "19999"
	
else :	
	
	aux = int(first) - 2
	aux = str(aux).zfill(4)
	
	result = "2" + str(aux)
	

print("El Resultado Sera " ,result)

print("Comprobemoslo")
print()

first = [int(first)]

for i in range(4) :
	
	if i % 2 == 0 :
		
		num = (input("Ingresa Otro Numero  "))
		
		first.append(int(num))
		
	else :
		
		num = 9999 - first[-1]
		first.append(num)
		print(num)
		
print()

 

print(sum(first)) 
		
		
	
	
	