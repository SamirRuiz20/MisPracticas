import tkinter as tk
from tkinter import ttk

def change(t) :
		global what
		what = t
		


def Dialog() :
	
	
		
		
	
	dialogo = tk.Toplevel()
	#dialogo.overrideredirect(True)
	dialogo.geometry("400x300+150+350")
	#dialogo.title("Jugador")
	
	dialogo.configure(bg = "skyblue")
	dialogo.resizable(0, 0)
	
	var = tk.StringVar()
	
	tk.Label(dialogo, text = "Nombre Del Jugador ".upper() , font = "Verdana 8 normal", fg = "blue", bg = "skyblue").pack( pady = 30)
	
	entry = tk.Entry(dialogo, width = 30, textvariable = var, bg = "limegreen", fg = "red", bd = 8, relief = "raised", justify = tk.CENTER )
	entry.pack()
	
	ttk.Separator(dialogo, orient = tk.HORIZONTAL, style = None).place( x = 5, y = 170, width = 390, height = 5 , bordermode = tk.INSIDE)
	
	
	
	
	btn = tk.Button(dialogo, text = "Ok",  bg = "blue", fg = "white", bd = 10, relief = "raised", highlightbackground = "red", activeforeground = "white", activebackground = "blue"  ,command = lambda : ( change(entry.get()), dialogo.destroy() ))
	btn.pack( side = tk.BOTTOM)
	
	
	entry.bind("<Return>", lambda event :( change(entry.get()), dialogo.destroy()))
	
	entry.focus_set()
	
	dialogo.transient(master = root)
	
	dialogo.grab_set()
	
	
	root.wait_window(dialogo)
	


def askstring() :
			
	a = Dialog()
	
	return what
			
	

		
def Testear() :
	
	name1 = askstring()
	name2 = askstring()
	
	tk.Label(root, text = name1+name2).pack()
	
	

		
what = " "
names = [ ]


root = tk.Tk()


btn = tk.Button(root, text = "Test", command = Testear)

btn.pack()




root.mainloop()


#https://r.honeygain.me/SAMIR0D5F1