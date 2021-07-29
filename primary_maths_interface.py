# Primary Maths Interface
# 05/07/21
# Wesley Key

# Imports
from tkinter import *
from student_class import *

from tkinter import Image 
from tkinter import messagebox
from math import *
import random
import operator

# Window
root = Tk()
root.title("Ormiston Primary Mathematics")
root.geometry("580x300+500+250")

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
        self.heading.grid(row=0, column=2, pady=20, padx=(30,30))
        
        # Asking User for their input using input boxes
        Label(self.main, text="             ",bg='#add8e6').grid(column=1,row=2)
        
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
        self.choices = ['     Addition    ', ' Subtraction  ', 'Multiplication', '     Division    ']
        self.tkvar.set('Choose')
        self.dropdown = OptionMenu(self.main, self.tkvar, *self.choices)
        
        # Create Label
        Label(self.main, font="Arial 15 bold", text="      Difficulty:    ",bg='#add8e6', relief=SOLID, bd=1).grid(row=5, column=2, sticky=W)
        self.dif = self.dropdown.grid(row=5, column=2, sticky=E, pady=3)
        
        def change_dropdown(*args):
            self.method = (self.tkvar.get())
        self.tkvar.trace('w', change_dropdown)
        
        # Next Button
        next_btn = Button(self.main,text="Next",fg="black",highlightbackground="#4cbb17",font="arial 14 bold",height="2", width="10", command=self.questions_win)
        next_btn.grid(row=7,column=3, padx=20, pady=50)
        
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
        elif self.diff == "Choose":
            self.notvalid = True
            messagebox.showerror("ERROR", "Please pick a level! ")
        else:
            self.notvalid = False
            
            # Destroying widgets from first window and replacing with new
            for widget in self.main.winfo_children():
                widget.destroy()
            
            # Using dictionary for the different signs
            self.operators = {
                "+":operator.add,
                "-":operator.sub,
                "*":operator.mul,
                "/":operator.truediv
            }
            if self.method == "     Addition    ":
                sign = "+"
                self.operation = list(self.operators.keys())
                self.x = random.randint(1,12)
                self.y = random.randint(1,12)
            elif self.method == " Subtraction  ":
                sign = "-"
                self.x = random.randint(1,15)
                self.y = random.randint(1,15)
            elif self.method == "Multiplication":
                sign = "x"
                self.x = random.randint(0,12)
                self.y = random.randint(0,12)
            else:
                sign = "÷"
                self.x = random.randrange(0,15,2)
                self.y = random.randint(0,10)

             
            
            # New widgets (labels, entry boxes and buttons)
            # Title
            Label(self.main, font="Arial 28 bold", text=f"{self.method}", fg="black", bg="#add8e6").grid(row=0, column=2, pady=20, padx=(30,30))
            Label(self.main, text="             ",bg='#add8e6').grid(column=1,row=2, padx=50)
            
            # Questions
            # Create 5 columns for the questions
            # Row 1 of questions
            Label(self.main, font="arial 30", text=f"{self.x} {sign} {self.y}", bg="#add8e6").grid(column=2, row=2,pady=(20,0))
            self.question = Entry(self.main, width=12,bg="#007cbe", fg="white", justify="center", font="arial 20").grid(column=2, row=3,pady=(20,0))
            
            # Check Button 
            self.check_btn = Button(self.main,text="Check ✓",fg="black",highlightbackground="#ffd639",font="arial 14 bold",height="2", width="10", command=self.check)
            self.check_btn.grid(row=4,column=3, padx=(50,40), pady=(35,60))
            
            self.back_btn = Button(self.main, )
            
    def check(self):
        self.user_answer = self.question
        
        if self.user_answer == self.correct_answer:
            self.check_btn.destroy() # Destroy check button
            
            # Replace check button with next button
            self.next = Button(self.main,text="Next",fg="black",highlightbackground="#4cbb17",font="arial 14 bold",height="2", width="10")
            self.next.grid(row=4,column=3, padx=(50,40), pady=(35,60))
            
            
        
        
                
        

Interface(root).welcome_frame()
root.mainloop()