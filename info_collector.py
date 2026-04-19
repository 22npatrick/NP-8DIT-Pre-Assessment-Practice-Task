"""This is a program to collect information"""

from tkinter import *

class Person:
    def __init__(self, name, age, phone_status):
        self.name = name
        self.age = age
        self.phone_status = phone_status


class InfoCollectorGUI:
    def __init__(self, parent):
        """ Constructor function"""
        self.f1 = Frame(parent)
        self.f2 = Frame(parent)

        self.v = IntVar()
        self.v.set(0)

        self.list_all_people = []

        #Frame 1
        self.lb1 = Label(self.f1, text = "Collecting Person Data", bg="pink")
        self.lb1.grid(row = 0, column = 0)

        self.bt1 = Button(self.f1, text = "Show all",  command=lambda: self.switch_frame(1))
        self.bt1.grid(row = 0, column = 2)

        self.lb2 = Label(self.f1, text = "First Name")
        self.lb2.grid(row = 2, column = 0)

        self.e1 = Entry(self.f1)
        self.e1.grid(row = 2, column = 2)

        self.lb3 = Label(self.f1, text = "Age")
        self.lb3.grid(row = 4, column = 0)

        self.e2 = Entry(self.f1)
        self.e2.grid(row = 4, column = 2)

        self.lb4 = Label(self.f1, text = "Do you have a mobile phone")
        self.lb4.grid(row = 6, column = 0)
        
        self.rb1 = Radiobutton(self.f1, variable = self.v, value = 0, text = "no")
        self.rb1.grid(row = 6, column = 2)
        
        self.rb2 = Radiobutton(self.f1, variable = self.v, value = 1, text = "yes")
        self.rb2.grid(row = 8, column = 2)

        self.bt2 = Button(self.f1, text = "Enter Data",  command=self.data_collecter)
        self.bt2.grid(row = 0, column = 2)


        #Frame 2

        self.lb5 = Label(self.f2, text = "Displaying Person Data", bg="pink" )
        self.lb5.grid(row = 0, column = 0)

        self.bt3 = Button(self.f2, text = "Add New Person", command=lambda: self.switch_frame(0))
        self.bt3.grid(row = 0, column = 2)

        self.lb6 = Label(self.f2, text = "First Name")
        self.lb6.grid(row = 2, column = 0)

        self.lb7 = Label(self.f2, text = "First Name of persom")
        self.lb7.grid(row = 2, column = 2)

        self.lb8 = Label(self.f2, text = "Age")
        self.lb8.grid(row = 4, column = 0)

        self.lb9 = Label(self.f2, text = "Age of person")
        self.lb9.grid(row = 4, column = 2)

        self.lb10 = Label(self.f2, text = 'Person (has)/(does not has) a mobile phone')
        self.lb10.grid(row = 6, column = 0, columnspan = 3)

        self.bt4 = Button(self.f2, text = "Previous")
        self.bt4.grid(row = 8, column = 0)
        
        self.bt5 = Button(self.f2, text = "Next")
        self.bt5.grid(row = 8, column = 2)

        #grid f1
        self.f1.grid()
    def switch_frame(self, amount):
        """" Switches between the 2 frames"""
        if amount == 1:
            self.f1.grid_forget()
            self.f2.grid()
        else:
            self.f2.grid_forget()
            self.f1.grid()

    def data_collecter(self):
        """" Creates a Person object using the data entered and adds it into the 
        list of all people"""
        self.list_all_people.append(Person(self.e1.get(),self.e2.get(), self.v.get()))






if __name__=="__main__":
    root = Tk()
    buttons = InfoCollectorGUI(root)
    root.mainloop()