import tkinter as tk

from ven2 import *




class VenUno(tk.Tk) :
	
	def __init__(self) :
		
		super().__init__()
		#self.pack()
		
		self.label = tk.Label(self, text = "Primera Ventana")
		
		self.btn = tk.Button(self, text = "Next →", activebackground = "skyblue", command = self.next)
		
		self.label.pack(side = "top", pady = 100)
		self.btn.pack(side = "top")
		
		
	def next(self) :
		
		main(self)



#root = tk.Tk()


app = VenUno()



app.mainloop() 

