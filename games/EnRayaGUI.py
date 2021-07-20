import tkinter as tk

from tkinter import messagebox as m

from tkinter.simpledialog import askstring

from functools import partial





 


def hay_Win(youficha) :
	
	if table[0] == table[1] == table[2] == youficha or \
	table[3] == table[4] == table[5] == youficha or table[6] == table[7] == table[8] == youficha or table[0] == table[3] == table[6] == youficha or table[1] == table[4] == table[7] == youficha or table[2] == table[5] == table[8] == youficha or table[0] == table[4] == table[8] == youficha or table[2] == table[4] == table[6] == youficha :
		return True

				
def isEmpate() :
	
	if not( " " in table) :
		
		return True
	



def lights() :
	
	#while True :
			
	color = __import__("random").choice(["skyblue", "#5CE79D", "#FF4500"])
		
	color1 = __import__("random").choice(["yellow", "red", "orange"])
		
		
	title.configure(bg = color)
	btn.configure(highlightbackground = color1)
	__import__("time").sleep(0.1)
		
	#root.update()
	root.after(100, lights)








def cambiar(index) :
	
		
	global turn , namePlay1, namePlay2, turnPlay

		
	
	def ganador(name, ficha) :
		
		if hay_Win(ficha) :
			
			turn = 0
			turnPlay.set("Ha Ganado " + name)
			return True
			
		elif isEmpate() :
			
			turn = 0
			turnPlay.set("Han Empatado")
			
			return True
	

	
	if table[index] == " " and turn == 0 :
		
		buttons[index].configure(text = "X", bg = "blue", fg = "white", font = "none 10 bold")
		table[index] = "X"
		turn = 1
		
		if ganador(namePlay1, "X") :
			
			bloquear()
			btn["state"] = "normal"
		
		
		else :	
			turnPlay.set("Turno De -> " + namePlay2.upper())
		
	
	elif table[index] == " " and turn == 1 :
		
		buttons[index].configure(text = "O", bg = "lightblue", fg = "white", font = "none 10 bold")
		table[index] = "O"
		turn = 0
		
		if ganador(namePlay2, "O") :
			
			bloquear()
			btn["state"] = "normal"
			
		else :
			turnPlay.set("Turno De -> " + namePlay1.upper())
		
	buttons[index].config(state = "disable")
		

		
	
def bloquear() :
	
	for i in buttons :
		
		i.configure(state = "disable")

				
		
def startGame() :
	
	global namePlay1, namePlay2, turnPlay, rondas
	
	
	turnPlay.set("")
	
	index = 0
	for i in buttons :
		i.configure(state = "normal", text = "", bg = "#AB942B", bd = 5)
		
		table[index] = " "
		index += 1
		
	namePlay1 = askstring("Jugador", "Nombre Del Jugador 1")
	namePlay2 = askstring("Jugador", "Nombre Del Jugador 2")
	
	
	if not(namePlay1 is None or namePlay2 is None) and len(namePlay1) != 0 and len(namePlay2) != 0 :
	
		turnPlay.set("Turno De -> " + namePlay1.upper() )
		tag.configure(font = "Verdana 10", fg = "green")
		
		rondas += 1
		round["text"] = "Ronda\n" + str(rondas)
		btn["state"] = "disable"
		
		
	else :
		m.showinfo("Error", "Ingresa Los Nombres \nPor Favor" )
		bloquear() 
		
		





root = tk.Tk()

turnPlay = tk.StringVar()


namePlay1 = ""
namePlay2 = ""
buttons = [ ]
turn = 0
table = [ " " ] * 9

x = 120
y = 280

for i in range(9) :

	
	BTN = tk.Button(root, width = 4, height = 3, activebackground = "#AB942B",font = "none 10 bold", bd = 8, command = partial(cambiar, i) )
	BTN.place(x = x, y = y)
	
	buttons.append(BTN)
	
	if i <= 2 :
		x += 180
		if i == 2 :
			x = 120
			y += 190
			
	elif i <= 5 :
		x += 180
		if i == 5 :
			x = 120
			y += 190
	else :
		x += 180




		
	
bloquear()

rondas = 0

round = tk.Label(root, text = "Ronda\n" + str(rondas), font = "Verdana 8", fg = "green" )
round.place(x = 10, y = 50)

#title = tk.Label(root, text = "Tres En Raya", font = "verdana 15 ", bg = "skyblue", fg = "#AB942B") 
#title.place(x = 200, y = 50)
#titulo()

tag = tk.Label(root, textvariable = turnPlay)
tag.place(x = 200, y= 200)

btn = tk.Button(root, text = "Iniciar Juego", bg = "#289173", fg = "white", font = "verdana 10 ", bd = 8, activebackground = "#289173", activeforeground = "white", command = startGame, highlightbackground = "red")
btn.place(x = 230, y= 900)



title = tk.Label(root, text = "Tres En Raya", font = "verdana 15 ", bg = "skyblue", fg = "#AB942B") 
title.place(x = 200, y = 50)
 


root.mainloop()