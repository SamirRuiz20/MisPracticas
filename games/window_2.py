import tkinter as tk
from tkinter.simpledialog import askstring as asking
from random import choice
from functools import partial
from tkinter import messagebox as message
from copy import deepcopy	
from time import sleep


from window_3 import WindowThree






def final(parent, parent2, mensaje, img) :
	
	app = WindowThree(parent, parent2, mensaje, img)
	
	app.grab_set()
	parent.wait_window(app)	




 

# inicio de la clase WindowSecond
class WindowSecond(tk.Toplevel) :
	
	
	
	
	def __init__(self, parent, gamers, rayas, **kw) :
		
		
		self.gamers = gamers
		self.rayas = rayas
		
		super().__init__(parent, cnf = {}, **kw)
		
		self.attributes("-fullscreen", True)
		
		
		self.master = parent
		
		# configuraciones.
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)		
		self.rowconfigure(3, weight = 4)		
		self.columnconfigure(1, weight = 1)
		self.columnconfigure(2, weight = 1)
		self.columnconfigure(3, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		
		
		
				
		#variables del juego
		self.var = tk.StringVar()
		self.player1 = None
		self.player2 = None
		self.turno = 0		
		self.buttons = []		
		self.tablero = [[" " for j in range(self.rayas)] for i in range(self.rayas)] 		
		self.rounds = 0
		
		
		self.volver = tk.Button(    self, text = "← Volver",    font = "courier 8",    bg = "blue",    fg = "white",    activebackground = "blue",    activeforeground = "white",     relief = "ridge",    bd = 8,    command = self.retorno
		)
		
		self.ronda = tk.Label(    self,    text = "Ronda\n" + str(self.rounds),     font = "Verdana 8",    fg = "green",    relief = "raised",    bg = "lightgray",     highlightthickness = 10,    highlightbackground = "yellow"
		)
		
		self.title = tk.Label(    self,    text = "Tic\nTac\nToe",     font = "verdana 15 ",    bg = "skyblue",    fg = "#AB942B",    relief = "raised",    bd = 8,    highlightthickness = 7,     highlightbackground = "yellow"
		)
				
		self.turn = tk.Label(     self,     textvariable = self.var,     bg = "skyblue",    relief = "sunken",    bd = 15,    font = "courier 10",    fg = "green",    width = 30,    highlightthickness = 4,     highlightbackground = "yellow"
		)
		
		#se crean los botones
		self.crea_buttons()
		self._buttons()
		
		
		#posicionamiento de widgets
		self.volver.grid(row = 0, column = 1, sticky = "w")
		
		self.ronda.grid(row = 1, column = 1, sticky = "ew", padx = 50)
		
		self.title.grid(row = 0, column = 2, sticky = "ew", padx = 50, rowspan = 2)
		
		self.turn.grid(row =2, column = 1, sticky = "ew", columnspan = 2, padx = 30, ipady = 10, pady = 10)
		
		
		#empieza el juego realizando el primer movimiento el primer jugador
		self.empezar()
		
		
		
		
		
	#metodo que crea los botones dentro de un frame	
	def crea_buttons(self) :
		
		
		self.frame = tk.Frame(    self,     bd = 10,    relief = "sunken",    bg = "lightgray",    width = 100,    height = 100
		)
		
		self.frame.grid(    row = 3,      column = 1,     sticky = "nsew",     columnspan = 2,     padx = 20,     rowspan = 2,     pady = 10
		)
	
		
		for i in range(self.rayas) :
			
			self.frame.rowconfigure(i, weight = 1)
			self.buttons.append([])

			for j in range(self.rayas) :
								
				self.frame.columnconfigure(j, weight = 1)
				
				BTN = tk.Button(	    self.frame ,    bg = "#D4D4D4",     width = 3,     height = 2,									 activebackground = "#AB942B", activeforeground = "white",         font = "courier 13",									   bd = 8,      relief = "sunken",   highlightbackground = "yellow",
									command = partial(self.mov, i, j) 
							)
			
				BTN.grid(row = i, column = j, sticky = "nsew")
	
				self.buttons[i].append(BTN)
				
				
		
				
				
	#metodo que bloquea todos los botones creados .			
	def bloquear(self) :
			
			
			for x in self.buttons :
				for i in x :
					i["state"] = "disable" 

	
	
	
	
	#metodo que desbloquea los botones que aun no han sido usados .
	def desbloquear(self) :
			
			for i in self.buttons :
					for x in i :
						if len(x["text"]) == 0 :
							
							x["state"] = "normal"
						



	
	#metodo que es llamado al presionar un boton del tablero para realizar su movimiento .	
	def mov(self, x, y, bloqueo = False) :
		
		
		if bloqueo :
			
			self.desbloquear()
		
				
		''' ------------------- '''
				
		if self.tablero[x][y] == " " and self.turno == 0 :
					   	
		   
		   self.tablero[x][y] = "X"
		   self.buttons[x][y].config( text = "X",            bg = "#3A88D4",fg ="orange",                     font = "courier 13 bold",     disabledforeground = "orange"
			)
			
		   self.turno = 1
		   
		   self.buttons[x][y]["state"] = "disable"
		   
		   fin = self.final("" if self.gamers == "1"\
		    else self.player1.upper() , 
		                        "X" )
		   
		   if fin :
		   	
		   	 self.bloquear() 
		   	 
		   	 self.after(800, lambda : final(self.master, self, self.var.get(), fin[1] ))
		   	 return
		   
		   else :
		   	
		   	self.var.set("Turno De La Maquina" if self.gamers == "1" else "Turno De " + self.player2.upper())
		   
		   
			   
		   if self.gamers == "1" :
			   
			   ind = self.mov_pc()
			   self.bloquear()
			   self.after(1000, lambda : self.mov(ind[0], ind[1], bloqueo = True))
			   
		   		 	
			
			
		elif self.gamers == "1" and self.turno == 1 :
		
		   
		   self.tablero[x][y] = "O"
		   self.buttons[x][y].config(  text = "O",     bg = "#00FF1A",    fg = "#3A88D4",                    font = "courier 13 bold", disabledforeground = "#3A88D4"
		   )
		   
		   self.turno = 0 
		   
		   fin = self.final("La Maquina", "O", "pc")
		   
		   if fin :
		   	
		   	self.bloquear()
		   	self.after(800, lambda : final(self.master, self, self.var.get(), fin[1]))
		   	return
		   	
		   else :
		   	
		   	self.var.set("Es Tu Turno")
			
			
						
		elif self.tablero[x][y] == " " and self.turno == 1 :
		  
		   
		   self.tablero[x][y] = "O"
		   self.buttons[x][y].config( text = "O",     bg = "limegreen",   fg = "white",                     font = "courier 13 bold", disabledforeground = "white"
		   )
		
		   self.turno = 0
		   
		   fin = self.final(self.player2.upper(), "O")
		   
		   if fin :
		   	
		   	self.bloquear()
		   	self.after(800, lambda : final(self.master, self, self.var.get(), fin[1]))
		   	return
		   	
		   	
		   else :
		   	
		   	self.var.set("Turno De " + self.player1.upper())
		
		
		
		#deshabilita el boton usado
		self.buttons[x][y]["state"] = "disable"
		


		
				
	#metodo que se llama al inicio del juego y verifica si el modo es de 1 jugador o dos jugadores .		
	def empezar(self) :
				
				
			if self.gamers == "1" :
				
				self.var.set("Es Tu Turno")
				
			else :
				
				self.player1 = asking("Nombre Del Jugador 1", "Escribe Aqui El Nombre")
				self.player2 = asking("Nombre Del Jugador 2", "Escribe Aqui El Nombre")
				self.var.set("ES tURNO De " + self.player1) 
				

	
	
	
	#metodo que actualiza el atributo self._rayas_ con todas las rayas del tablero [horizontales, veericales, diagonales]
	def _rayas(self, table) :
		
		
		self._rayas_ = [ ]
		
		for i in table :
			self._rayas_.append(i)
			
			
		for j in zip(*table) :	
			self._rayas_.append(list(j))
			
		
		diagonals = [[], []]		
		for diag in range(len(table)) :			
			diagonals[0].append(table[diag][diag])		
			diagonals[1].append(table[diag][-diag-1])
			
			
		for i in diagonals :
			self._rayas_.append(i)
			
		

				
							
	#metodo que realiza la jugada del pc devolviendo los indices de la celda que escogio comprobando antes si puede ganar o bloquear de lo contrario escoge una celda vacia al azar .
	def mov_pc(self) :
		
		
		copia = deepcopy(self.tablero)		
		for i in range(len(copia)) :
			for j in range(len(copia)) :
				
				 if copia[i][j] == " " :
				 	copia[i][j] = "O"
				 	if self.winner(copia, "O")[1] :
				 			return i, j
				 	copia[i][j] = " "
		
				 			 	
		for i in range(len(copia)) :
				for j in range(len(copia)) :
									
					if copia[i][j] == " " :
						copia[i][j] = "X"
						if self.winner(copia,"X")[1] :
							return i, j
						copia[i][j] = " "
		
									
		vacias = []
		for i in range(len(copia)) :
								
			for j in range(len(copia)) :
				if copia[i][j] == " " :
						vacias.append((i,j))
						
						
		return choice(vacias)		
									
				
	
	
									
	#metodo que comprueba si alguien ha ganado de ser asi devuelve True de lo contrario False .
	def winner(self,table, ficha) :
			
			
		self._rayas(table)		
		for x, i in enumerate(self._rayas_) :
			if i.count(ficha) == len(i) :
				return x, True
				
				
				
		return None, False				





	#
	def _buttons(self) :
		
		
		self._buttons_ = [ ]
		
		for i in self.buttons :
			self._buttons_.append(i)
			
			
		for j in zip(*self.buttons) :	
			self._buttons_.append(list(j))
			
		
		diagonals = [[], []]		
		for diag in range(len(self.buttons)) :			
			diagonals[0].append(self.buttons[diag][diag])		
			diagonals[1].append(self.buttons[diag][-diag-1])
			
			
		for i in diagonals :
			self._buttons_.append(i)
			
									
	
					
	
				
	#metodo que que es llamado al presiona el boton Volver y regresa a la ventana anterior .				
	def retorno(self) :
			
			
			self.master.deiconify()
			self.destroy()
			
	
	
	

	#
	def final(self, name, ficha, tipo = "usr") :
			
			raya, win = self.winner(self.tablero, ficha)
			
			
			if win :
				
				img = "../Images/win.png" if tipo == "usr" else "../Images/loss.jpg"
				
				
				self.var.set("Has Ganado " + name)
				
				for i in self._buttons_[raya] :					
			
					i.configure( fg = "red", font = "none 15 bold", relief = "raised", bd = 8, disabledforeground = "red", highlightthickness = 5, highlightbackground = "red")
				
				return True, img
				
				
			elif self.isEmpate() :
				
				img = "../Images/empate.jpg"
				
				
				self.var.set("Han Empatado")
				return True, img
			
			
			
			

						
	#metodo que comprueba si aun hay espacios vacios en el tablero
	def isEmpate(self) :
		
		return True if not(any([" " in i for i in self.tablero])) else False
		
		
		

''' ------ Fin De La Clase ----- '''


def ask() :
	
	na1 = asking("Jugador", "Escri")
	na2 = asking("Oyro", "Escron")
	
	return na1, na2

									
									
''' funcion principal que crea ka segunda ventana '''
def main(parent, gamers, rayas) :
	
	
	app = WindowSecond(parent, gamers, rayas , bg = "#B4FFFF")
	
	app.grab_set()
	parent.wait_window(app)	 	
	
	
	
	
		
if __name__ == "__main__" :
	
	root = tk.Tk()
	
	tk.Button(root, text = "click", command = lambda : main(root, "1", 3)).pack()
	
	root.mainloop()
	
			
		