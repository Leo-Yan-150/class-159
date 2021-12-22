from tkinter import *

root=Tk()
root.geometry("600x400")

listt = ["Grapes","Peaches","Bananas"]
dictt = {"value1" : "ans1", "value2" : "ans2"}

try:
    print(listt[2])
    print(dictt["value3"])
except IndexError:
    messagebox.showinfo("Error", "The index number in line 10 is undefined.")
except KeyError:
    messagebox.showinfo("Error", "The key entered in line 11 does not exist.")

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school