import tkinter as tk

from PIL import ImageTk
from PIL import Image





class WindowThree(tk.Toplevel) :
	
	
	def __init__(self, master = None, master2 = None, message = "", img = None) :
		

			self.master = master
			self.master2 = master2
			self.message = message
			self.imagen = Image.open(img)
			self.imagen = self.imagen.resize((600, 500), Image.ANTIALIAS)
			self.imagen = ImageTk.PhotoImage(self.imagen)
		
			super().__init__(master)
			
			self.attributes("-fullscreen", True)

						
			
			self.rowconfigure(0, weight = 1)
			self.columnconfigure(0, weight = 1)
			self.rowconfigure(4, weight = 1)
			self.columnconfigure(2, weight = 1)
			
			
			self.img = tk.Label(self, image = self.imagen, anchor = "center", highlightthickness = 7, highlightbackground = "limegreen")
			self.final = tk.Label(self, text = self.message, font = "courier 13", fg = "blue" )
			
			self.inicio = tk.Button(self, text = "Inicio", command = self.start, relief = "ridge" , bd = 10, font = "Verdana 12", activeforeground = "white", activebackground = "green", bg = "green", fg = "white")
			
			
			
			self.img.grid(row = 1, column = 1, pady = 70)
			self.final.grid(row = 2, column = 1, pady = 50)
			self.inicio.grid(row = 3, column = 1)	
			
					
	
	def start(self) :
		
			self.master.deiconify()
			self.master2.destroy()
			self.destroy()
			


def main(parent) :
	
	app = WindowThree(parent)
	
	app.grab_set()
	parent.wait_window(app)
									
				
if __name__ == "__main__" :
	
		root = tk.Tk()
		
		tk.Button(root, text = "click", command = lambda : main(root)).pack()
		
		root.mainloop()
		
			