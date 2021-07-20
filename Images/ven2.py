import tkinter as tk

from ven3 import *



class VenDos(tk.Toplevel) :
	
	def __init__(self, master = None) :
		
		super().__init__(master)
		
		self.attributes("-fullscreen", True)
		
		self.label = tk.Label(self, text = "Segunda Ventana")
		
		self.btn = tk.Button(self, text = "Next →", activebackground = "skyblue", command = self.next)
		
		self.label.pack(side = "top", pady = 100)
		self.btn.pack(side = "top")
		
		
	def next(self) :
		
		main_(self, self.master)
		
		
def main(master) :
	
	app = VenDos(master)