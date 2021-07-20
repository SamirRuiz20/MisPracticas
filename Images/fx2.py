import tkinter as tk

class Fx2(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.attributes("-fullscreen", True)
        self.master = master
        self.create_widgets()
        
        self.grab_set()
        self.master.wait_window(self)
        
    
    def create_widgets(self):
        self.message = tk.Message(self, text="Hello")
        self.message.pack() 