# Student Class - Primary Maths Program
# 05/07/21
# Wesley Key

class Student:
    def __init__(self, stn, yl, dif):
        self.student_name = stn
        self.year_level = yl
        self.difficulty = dif
    
    def year_l(self):
        if self.year_level not in ["1", "2", "3","4","5","6"]:
            return ["1", "2","3","4","5","6"]
    
    def range(self):
        if self.difficulty == "Easy":
            return (1,5)
        '''elif self.difficulty == "Medium":
            return (3,7)
        elif self.difficulty == "Hard":
            return (5, 9)
        else: 
            return (6,12)'''
        