import tkinter as tk
from tkinter import ttk

from window_2 import main as main_





#Inicio de la clase WindowFirst
class WindowFirst(tk.Frame) :
	
	
	
	
	def __init__(self, master = None, **kw) :
		
		
		super().__init__(master, cnf = {}, **kw)
		
		self.gamers = None
		self.rayas = None
		self.master = master
		
		
		self.configure(relief = "raised", bd = 10)
		self.master["bg"] = "orange"
		self.pack(side = "top", fill = "both", expand = True, padx = 30, pady = 30)
		
		
		self.varStr = tk.StringVar(value = "1")
		self.varInt = tk.IntVar(value = 3) 		

				
		self.title = tk.Label(    self,      text = "Tic Tac Toc",     fg = "orange",        font = "none 15 bold",       highlightthickness = 5,       bd = 10,       relief= "sunken",      highlightbackground = "yellow" 
		)
				
		self.opcion1 = tk.Label(    self,      text = "Elige Una Opcion ↓",       relief = "ridge",        bd = 8,      fg = "yellow",         bg = "black"
		)
		
		self.opcion2 = tk.Label(    self,       text = "Elige Una Opcion ↓",        relief = "ridge",       bd = 8,      fg = "yellow",         bg = "black"
		)
		
		self._player1 = ttk.Radiobutton(     self, text= "1 Jugador" ,       variable = self.varStr,       value = "1",    underline = 0
		)
		self._player2 = ttk.Radiobutton(self,     text = "2 Jugadores",      value = "2",      variable = self.varStr,       underline = 0
		)
		
		self.separ = ttk.Separator(self, orient = tk.HORIZONTAL)
		
		self.raya3 = ttk.Radiobutton(self,      text = " 3 En Raya",      value = 3,        variable = self.varInt
		)
		self.raya4 = ttk.Radiobutton(self,     text = " 4 En Raya",     value = 4,         variable = self.varInt
		)
		self.raya5 = ttk.Radiobutton(self,     text = " 5 En Raya",     value = 5,         variable = self.varInt
		)
		
		self.inicio = tk.Button(self,   text = "Iniciar Juego",             bg = "#289173",     fg = "white",     font = "verdana 10 ",     bd = 8,     activebackground = "#289173",         activeforeground = "white" , highlightbackground = "limegreen", highlightthickness = 3,        command = lambda : ( self.UpdateVars(), self.start()), highlightcolor = "yellow"
		)
		
		self.salir = tk.Button(self ,     text = "Salir",               font = "courier 10",     bg = "red",      fg = "white",      activeforeground = "white",      activebackground = "red",       relief = "ridge",      bd = 8, command = self.master.destroy
		)
		
				
		#posicionamiento de widgets con pack
		self.title.pack(side = "top",      fill = "both",      padx = 50,      expand = True,      pady = 50
		)
		
		''' --- '''		
		self.opcion1.pack(side = "top",     fill = "y",          expand = True,      pady = 20,    ipadx = 30,     padx = 50
		)		
		self._player1.pack(side = "top",      fill = "both",       padx = 70,      expand = True
		)
		self._player2.pack(side = "top",     fill = "both",      padx = 70,      expand = True
		)
		''' ----- '''
		
		self.separ.pack(side = "top", fill = "x", padx = 70, expand = True, pady = 30)
		
		''' --- '''
		self.opcion2.pack(side = "top",     fill = "y",     padx = 50,     pady = 20,     ipadx = 30,    expand = True
		)		
		self.raya3.pack(side = "top",     fill = "both",     padx = 70,     expand = True
		)
		self.raya4.pack(side = "top",     fill = "both",     padx = 70,     expand = True
		)
		self.raya5.pack(side = "top" ,     fill = "both",      padx = 70,      expand = True
		)
		''' ---- '''
		
		
		self.salir.pack(side = "left",     fill = "both",     padx = 20,     expand = True,     pady = 40,   ipadx = 40
		)
		
		self.inicio.pack(side = "right",       fill = "both",     padx = 20,      expand = True,     pady = 40,      ipadx = 40
		)
		
		
		self.inicio.focus()
		
	

	
	
	#metodo que actualiza los valores de los atributos gamers y rayas con los valores seleccionados en los Radiobuttons .
	def UpdateVars(self) :
		
		
		self.gamers = self.varStr.get()
		self.rayas = self.varInt.get()
		


	
	
	#metodo que es llamado al presionar el boton iniciar juego y llama a la funcion main que crea la segunda ventana desde el modulo window_2.py .
	def start(self) :
		
		
		main_(self.master, self.gamers, self.rayas)
		
		
		
	
	
	#.......		
	def __del__(self) :
		
		pass 
		
		

''' ------ Fin De La Clase ------ '''
								
		
		
		
#funcion principal que crea la primera ventana del juego .		
def main() :
	
					
	root = tk.Tk()
	app = WindowFirst(root)
	
	app.mainloop()		
				
		
		

if __name__ == "__main__" :
		
		main()
		
#CuEnTa2021ViRtUaL
		
		
		
		 