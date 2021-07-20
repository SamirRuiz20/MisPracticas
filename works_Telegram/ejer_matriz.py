import os




class Matriz :
	
	
	
	def __init__(self, rows = 0 , columns = 0) :
		
		
		self.matriz = [[0 for i in range(columns)] for i in range(rows)]
		self.rows = rows
		self.columns = columns
		
	
		
	
		
	def __str__(self) :
		
		print()
				
		for i in range(self.rows) :
			
			print("[", end = "")
			
			for j in range(self.columns) :
				
				print(f"{self.matriz[i][j]:^3}", end = "")
				
			print("]")
			
			
		return ""
		
		
		
	
	
	
	def rellenar(self) :
		
		print("\n-------------------\n")
		
		fila = input(f" Ingrese la fila -> {range(1, self.rows+1)} ")
		columna = input(f" Ingrese la Columna -> {range(1, self.columns+1)}  ")
		valor = input(" Ingrese su nuevo valor ->  ")
		print("\n-------------------\n")
		
		
		fila = int(fila)-1
		columna = int(columna)-1
		
		if fila > self.rows or columna > self.columns :
			
			print("Los Indices Dados Han Pasado el rango de la matriz")
			return
		
		self.matriz[fila][columna] = valor
		
	
	
	
	
	#metodo que se encarga de rotar la matriz a la izquierda o la derecha
	def rotar_matriz(self, side = None) :
		
		
		side = side.upper()
		if side in ("D", "I") :
				
				
				
				rotada = []
				
				for i in range(self.columns) :
					
					rotada.append([])
					
					for j in range(self.rows) :
					
						value = self.matriz[j][self.columns-1-i] if side == "D" else self.matriz[self.rows-1-j][i]
							
						rotada[i].append(value)
						
				
				self.matriz = rotada
				self.rows = len(rotada)
				self.columns = len(rotada[0])
				
				return self.__str__()
						
		
										
		else :
			
			return "ingresa d para derecha o i para izquierda"
		

		
				
								
		
def menu() :
	
	while True :
		
		os.system("clear")
		print("\n     Menu\n")
		
		print(" 1 ->  Crear matriz")
		print(" 2 ->  Salir")
		print()
		
		op = input(" Cual Es Tu Opcion ->  ")
		
		if op in ("1", "2") :
			
			return op
			
		print()
		print("Opcion no valida")
		input("\n   Enter Para intentar otra vez\n")
		
		



def submenu() :
		
		
		while True :
			
			os.system("clear")
			
			print("\n    Submenu De La Matriz\n")
			
			print(" 1 ->  Rellenar Matriz .")
			print(" 2 ->  Mostrar Matriz")
			print(" 3 ->  Rotar Matriz.")
			print(" 4 ->  Volver")
			
			print()
			op = input("\n Cual Es Tu Opcion  ")
			
			if op in ("1", "2", "3", "4") :
				
				return op
				
			print()
			print("Opcion No Valida")
			input("\n  Enter Para intentar otra vez\n")
				
				
			
		
				
								
		
		
		

def main() :
	
		
		
	while True :
			
		os.system("clear")
		
		op = menu()
		
		if op == "2" :
			
			break
			
		elif op == "1" :
			os.system("clear")
		
			filas = input("\n De Cuantas Filas Quieres Que Sea La Matriz  ")
				
			columnas = input("\n De Cuantas Columnas Quieres Que Sea La Matriz  ")
				
			filas = int(filas)
			columnas = int(columnas)
				
			mt = Matriz(filas, columnas)
			
			while True :
					
				subOp = submenu() 
				os.system("clear")
			
				if subOp == "4" :
					
					break
					
				elif subOp == "1" :
					
					mt.rellenar()
					
				elif subOp == "2" :
					
					print(mt)
					
				elif subOp == "3" :
					
					side = input("\n A La Derecha (D) O Izquierda (I) - ").upper()
					
					print(mt.rotar_matriz(side)) 
				
				input("\n    |Enter| Para Continuar \n")
					
				
			
if __name__ == "__main__" :
		
					
								
	  main() 		
		
		
		
		
	