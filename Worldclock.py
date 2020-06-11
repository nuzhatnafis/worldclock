#importing module
from tkinter import *
from tkinter.ttk import *
from time import strftime

#creating tkinter window
root = Tk()
root.title("WorldClock")

#Display time on Label
def time():
	string = strftime("%H:%M:%S %p")
	lbl.config(text=string)
	lbl.after(1000, time)
	
#styling label
lbl = Label (root, font=("lucidia", 45, "bold"),
             background="Blue",
             foreground="White")
             
#center Placing
lbl.pack(anchor="center")
time()
mainloop()
