"""This is a program to collect information"""

from tkinter import *

class InfoCollectorGUI:
    def __init__(self, parent):
        """ Constructor function"""
        self.lb1 = Label(parent, text = "Label 1")
        self.lb1.pack()



if __name__=="__main__":
    root = Tk()
    buttons = InfoCollectorGUI(root)
    root.mainloop()