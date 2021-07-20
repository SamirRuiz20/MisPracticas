import tkinter as tk





class VenTres(tk.Toplevel) :
	
	def __init__(self, parent, master = None) :
		
		self.parent = parent
		super().__init__(master)
		
		self.attributes("-fullscreen", True)
		
		self.label = tk.Label(self, text = "Tercera Ventana")
		
		self.btn = tk.Button(self, text = "← Inicio", activebackground = "skyblue", command = self.regre)
		
		self.label.pack(side = "top", pady = 100)
		self.btn.pack(side = "top")
		
		
	def regre(self) :
		
		self.master.deiconify()
		self.parent.destroy()
		self.destroy()
		
		
def main_(parent, master) :
	
	app = VenTres(parent, master)