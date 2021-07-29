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
        if self.year_level == 1:
            return [0,1,2,3,4,5]
        elif self.year_level == 2:
            return [0,2,3,4,5,6,7]
        elif self.year_level == 3:
            return [0,3,4,5,6,7,8,9]
        elif self.year_level == 4:
            return [0,4,5,6,7,8,9,10]
        elif self.year_level == 5:
            return [1,4,5,6,7,8,10,11,12]
        else:
            return[0,5,8,9,10,11,12,13,14,15]
        
        
        