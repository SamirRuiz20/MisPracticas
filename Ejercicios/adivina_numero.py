
import random



lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

codigo = ""

for i in range(4) :
	
	num = random.choice(lista)
	
	while num in codigo :
		num = random.choice(lista)
		
	codigo += num
	

print(f"\n{'Adivina Las Cuatro Cifras':^59}\n")	

propuesta = ""

while codigo != propuesta :
	
	propuesta = (input(" Que Numero Propones  --  "))
	
	exis = [ i for i in propuesta if i in codigo ]
	
	if any(exis) :
		
		for i in exis :
			if propuesta.index(i) == codigo.index(i) :
				
				print(" Has Acertado Con El Numero ", i)
				
			elif i in codigo :
				print("Has Coincidido Con Un Numero Pero En Posicion Diferente ", i)
		
	else :
		
		print("No Has Acertado Ni Coincidido ")
	
print("Felicitaciones Has Acertado")	