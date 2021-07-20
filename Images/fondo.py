import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1280x720")
root.update()

background_img = Image.open("Beach.jpg")
background_img = background_img.resize((root.winfo_width(),root.winfo_height()), Image.ANTIALIAS)
background_tkimg = ImageTk.PhotoImage(background_img)

canvas = tk.Canvas(root, highlightthickness=35)
canvas.pack(expand = True, fill = "both")
canvas.create_image(0,0, image = background_tkimg, anchor = "nw")

root.update()
canvas_height = canvas.winfo_height()
canvas_width = canvas.winfo_width()

title_label = canvas.create_text((canvas_width//2), (canvas_height//2) - 25, fill = "white", text="TITLE")
button1 = tk.Button(canvas, text="button 1", highlightthickness = 10, highlightbackground = "yellow")
button2 = tk.Button(canvas, text="button 2")
button3 = tk.Button(canvas, text="button 3")

canvas.create_window((canvas_width//2) - 75, (canvas_height//2) + 25 , window = button1)
canvas.create_window((canvas_width//2), (canvas_height//2) + 25, window = button2)
canvas.create_window((canvas_width//2) + 75, (canvas_height//2) + 25, window = button3)

root.mainloop()