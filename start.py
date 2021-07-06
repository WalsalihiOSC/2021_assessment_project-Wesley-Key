# Main routine - Primary Mathematics Program
# 05/07/21
# Wesley Key

# Imports
from tkinter import *
from primary_maths_interface import *

root = Tk()
root.title("Ormiston Primary Mathematics")
root.geometry("500x290")

#Colour of bg - #add8e6ff

gui = Interface(root)
gui.welcome_frame()
