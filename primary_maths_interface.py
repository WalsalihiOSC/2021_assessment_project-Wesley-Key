# Primary Maths Interface
# 05/07/21
# Wesley Key

# Imports
from tkinter import *
from student_class import *
from tkinter import messagebox
from random import *


root = Tk()
root.title("Ormiston Primary Mathematics")
root.geometry("500x270")

#Colour of bg - #add8e6ff

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
        self.heading = Label(self.main, font=("Arial 28 bold"), text="PRIMARY MATHEMATICS", fg="black",bg='#add8e6')
        self.heading.grid(row=0, column=2, pady=10, sticky=E)
        
        # Logo
        
        # Asking User for their input using input boxes
        Label(self.main, text="         ",bg='#add8e6').grid(column=1,row=2)
        # Student Name
        Label(self.main,font=("Arial 14 bold"),text=" Student Name: ",bg='#add8e6', relief=SOLID, bd=1).grid(row=3,column=2, sticky=W)
        self.stn=Entry(self.main, bg='#add8e6')
        self.stn.grid(row=3,column=2, sticky=E)
        
        # Student Year Level
        Label(self.main, font="Arial 15 bold", text="    Year Level:    ",bg='#add8e6', relief=SOLID, bd=1).grid(row=4,column=2,sticky=W, pady=5)
        self.yl = Entry(self.main,bg='#add8e6')
        self.yl.grid(row=4, column=2, sticky=E)
        
        # Difficulty
        # Drop down box for the different difficulty types
        # Create Tkinter Variable
        self.tkvar = StringVar(root)
        # Set options
        self.choices = ['Level 1', 'Level 2', 'Level 3']
        self.tkvar.set('Choose')
        
        self.dropdown = OptionMenu(self.main, self.tkvar, *self.choices)
        Label(self.main, font="Arial 15 bold", text="      Difficulty:    ",bg='#add8e6', relief=SOLID, bd=1).grid(row=5, column=2, sticky=W)
        self.dif = self.dropdown.grid(row=5, column=2, sticky=E, pady=3)
        
        def change_dropdown(*args):
            print(self.tkvar.get())
        
        self.tkvar.trace('w', change_dropdown)
        
        # Next Button
        next_btn = Button(self.main,text="Next",fg="black",highlightbackground="#4cbb17",font="arial 14 bold",height="2", width="10", command=self.questions_win)
        next_btn.grid(row=7,column=3, padx=10, pady=50)
        
    def questions_win(self):
        # Get users input
        self.stname = (self.stn.get().capitalize())
        self.ylvl = self.yl.get()
        self.diff = self.tkvar.get()
        
        # Creating instance of students class with users input
        self.student = Student(self.stn, self.yl, self.tkvar) 
        self.range = self.student.range()
        self.year = self.student.year_l()
        
        # If entry boxes are empty or year level is not between 1 and 6, error message is set
        if len(self.stname)==0 or len(self.ylvl)==0 or len(self.diff)==0:
            self.notvalid = True
            messagebox.showerror("ERROR", "No empty boxes please!")
        elif self.ylvl not in self.year:
            self.notvalid = True
            messagebox.showerror("ERROR", "You have to be in Year 1, 2, 3, 4, 5 or 6!!")
        else:
            self.notvalid = False
            self.q = []
        
            # Destroying widgets from first window and replacing with new
            for widget in self.main.winfo_children():
                widget.destroy()
            
            # Interface
            # New Widgets (labels, buttons, math questions and entry boxes)
            
            # Title
            # Header
            Label(self.main, text="         ",bg='#add8e6').grid(column=1,row=0)
            Label(self.main, font=("Arial 28 bold"), text="Addition", fg="black",bg='#add8e6').grid(row=1, column=2)

            # Layout for the questions (5 columns)
            
            
            

Interface(root).welcome_frame()
root.mainloop()