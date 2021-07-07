# Primary Maths Interface
# 05/07/21
# Wesley Key

# Imports
from tkinter import *
from student_class import *

root = Tk()

'''Colours
# yellow (check button, new student btn) - #ffd639
# dark blue (text box bg, restart button) - #007cbe
# green (next button, ticks) - #4cbb17
# light blue (bg) - #add8e6
# red (red crosses, done button)- #ed1c24'''

# Define Class
class Interface:
    def __init__(self, main_window):
        self.main_window = main_window
        self.restart = False
        self.notvalid = False
    
    # First Frame
    def welcome_frame(self):
        self.main = Frame(self.main_window, bg='#add8e6')
        self.main.grid()
        
        # Header
        Label(self.main, text="         ",bg='#add8e6').grid(column=1,row=0)
        self.heading = Label(self.main, font=("Arial 28 bold"), text="PRIMARY MATHEMATICS", fg="black",bg='#add8e6')
        self.heading.grid(row=1, column=2)
        
        # Logo
        
        # Asking User for their input using input boxes
        Label(self.main, text="         ",bg='#add8e6').grid(column=1,row=2)
        # Student Name
        Label(self.main,font=("Arial 14 bold"),text="Student Name: ",bg='#add8e6').grid(row=3,column=2, sticky=W)
        self.stn=Entry(self.main)
        self.stn.grid(row=3,column=2, sticky=E)
        
        # Student Year Level
        Label(self.main, font="Arial 15 bold", text="Year Level: ",bg='#add8e6').grid(row=4,column=2,sticky=W)
        self.yl = Entry(self.main)
        self.yl.grid(row=4, column=2, sticky=E)
       
        

        
