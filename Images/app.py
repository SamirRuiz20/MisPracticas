import tkinter as tk

from fx2 import Fx2

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "Open"
        self.button["command"] = self.open
        self.button.pack()

    def open(self):
        Fx2(self.master)
        
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
