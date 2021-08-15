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


# Window
root = Tk()
root.title("Ormiston Primary Mathematics")
root.geometry("580x300+500+250")

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
        self.heading.grid(row=0, column=2, pady=20, padx=(30,30))
        
        # Asking User for their input using input boxes
        Label(self.main, text="             ",bg='#add8e6').grid(column=1,row=2)
        
        # Student Name
        self.student_name = Label(self.main,font=("Arial 14 bold"),text=" Student Name: ",bg='#add8e6', relief=SOLID, bd=1)
        self.student_name.grid(row=3,column=2, sticky=W)
        self.stn=Entry(self.main, bg='#add8e6')
        self.stn.grid(row=3,column=2, sticky=E)
        
        # Student Year Level
        self.year = Label(self.main, font="Arial 15 bold", text="    Year Level:    ",bg='#add8e6', relief=SOLID, bd=1)
        self.year.grid(row=4,column=2,sticky=W, pady=5)
        self.yl = Entry(self.main,bg='#add8e6')
        self.yl.grid(row=4, column=2, sticky=E)
        
        # operations
        # Drop down box for the different mathematical operations
        # Create Tkinter Variable
        self.tkvar = StringVar(root)
        
        # Set options
        self.choices = ['     Addition    ', ' Subtraction  ', 'Multiplication', '     Division    ']
        self.tkvar.set('Choose')
        self.dropdown = OptionMenu(self.main, self.tkvar, *self.choices)
        
        # Create Label
        self.difficulty = Label(self.main, font="Arial 15 bold", text="      Difficulty:    ",bg='#add8e6', relief=SOLID, bd=1)
        self.difficulty.grid(row=5, column=2, sticky=W)
        self.dif = self.dropdown.grid(row=5, column=2, sticky=E, pady=3)
        
        def change_dropdown(*args):
            self.method = (self.tkvar.get())
        self.tkvar.trace('w', change_dropdown)
        
        # Save Button
        self.save_btn = Button(self.main,text="Save",fg="black",highlightbackground="#007cbe",font="arial 14 bold",height="2",width="10",command=self.check_input)
        self.save_btn.grid(row=7,column=3, padx=20, pady=50)
    
        # Creating instance of students class with users input
        self.student = Student(self.stn, self.yl, self.tkvar) 
        self.range = self.student.range()
        self.year = self.student.year_l()   
    
    def check_input(self):
        # Get users input
        self.stname = (self.stn.get().capitalize())
        self.ylvl = self.yl.get()
        self.diff = self.tkvar.get()
        
        # Creating instance of students class with users input
        self.student = Student(self.stn, self.yl, self.tkvar) 
        self.range = self.student.range()
        self.year = self.student.year_l()
    
        # If entry boxes are empty or year level is not between 1 and 6, error message is set
        if len(self.stname)==0:
            self.notvalid = True
            messagebox.showerror("ERROR", "Please enter your name")
        elif len(self.ylvl)==0:
            self.notvalid = True
            messagebox.showerror("ERROR","Please enter your year level")    
        elif self.ylvl not in self.year:
            self.notvalid = True
            messagebox.showerror("ERROR", "You have to be in Year 1, 2, 3, 4, 5 or 6!!")
        
        # If the user has not picked an operation
        elif self.diff == "Choose":
            self.notvalid = True
            messagebox.showerror("ERROR", "Please pick a difficulty! ")
        else:
            self.notvalid = False
            
            # Destroying widgets from first window and replacing with new
            self.save_btn.destroy()
            
            self.next = Button(self.main,text="Next",fg="black",highlightbackground="#4cbb17",font="arial 14 bold",height="2",width="10",command=self.questions_win)
            self.next.grid(row=7,column=3, padx=20, pady=50)
        
    def questions_win(self):
        # destroy all widgets in first frame
        for widget in self.main.winfo_children():
            widget.destroy()

        # New widgets (labels, entry boxes and buttons)
        # Title
        self.title = Label(self.main, font="Arial 28 bold", text=f"{self.method}", fg="black", bg="#add8e6")
        self.title.grid(row=0, column=2, pady=20, padx=(30,30))
        Label(self.main, text="             ",bg='#add8e6').grid(column=1,row=2, padx=50)
        
        # set a sign to the method to display in questions
        if self.method == "     Addition    ":
            self.sign = "+"
        elif self.method == " Subtraction  ":
            self.sign = "-"
        elif self.method == "Multiplication":
            self.sign = "x"
        else:
            self.sign = "÷"
            
        # randomising numbers for questions
        self.x = random.choice(self.range)
        self.y = random.choice(self.range)
        
        # Display question and entry box
        Label(self.main, font="arial 30", text=f"{self.x} {self.sign} {self.y}", bg="#add8e6").grid(column=2, row=2,pady=(20,0))
        self.question = Entry(self.main, width=12,bg="#007cbe", fg="white", justify="center", font="arial 20")
        self.question.grid(column=2, row=3,pady=(20,0))
        
        # Check Button 
        self.check_btn = Button(self.main,text="Check ✓",fg="#ffd639",highlightbackground="#ffd639",font="arial 14 bold",height="2", width="10",command=lambda: self.checkb(self.question))
        self.check_btn.grid(row=4,column=3, padx=(50,40), pady=(35,60))
              
    # Function for the check button, return correct or wrong label
    def checkb(self, var1):
        if var1.get() == str(self.correct_answer()):
            correct = Label(self.main, text="✓", fg="green", font="arial 40 bold", bg="#add8e6")
            correct.grid(column=3, row=3, sticky=W)
            
            # Destroy Check Button
            self.check_btn.destroy()
            
            # Replace with next button
            self.next_btn = Button(self.main,text="Next ⮕",fg="black",highlightbackground="#4cbb17",font="arial 14 bold",height="2", width="10", command=self.questions_win)
            self.next_btn.grid(row=4,column=3, padx=(50,40), pady=(35,60))
            
        else:
            wrong = Label(self.main, text="✘", fg="red", font="arial 40 bold", bg="#add8e6")
            wrong.grid(column=3, row=3, sticky=W)
            self.score -= 1
            self.count_ten += 1
    
    # Function to return correct answer
    def correct_answer(self):
        self.questions_win
        
        if self.method == "     Addition    ":
            return self.x + self.y
        elif self.method == " Subtraction  ":
            return self.x - self.y
        elif self.method == "Multiplication":
            return self.x * self.y
        else:
            return self.x / self.y
        
    # Quit program function 
    def quit(self):
        self.main_window.destroy()       

Interface(root).welcome_frame()
root.mainloop()