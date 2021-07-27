# Student Class - Primary Maths Program
# 05/07/21
# Wesley Key

class Student:
    def __init__(self, stn, yl, tkvar):
        self.student_name = stn
        self.year_level = yl
        self.difficulty = tkvar
    
    def year_l(self):
        if self.year_level not in ["1", "2", "3","4","5","6"]:
            return ["1", "2","3","4","5","6"]
        
    def range(self):
        if self.difficulty == "Addition":
            return (1,12)
        elif self.difficulty == "Subtraction":
            return (1,12)
        elif self.difficulty == "Multiplication":
            return (1,10)
        else: 
            return (1,12)
        
        