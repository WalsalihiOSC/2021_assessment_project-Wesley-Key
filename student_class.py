# Student Class - Primary Maths Program
# 05/07/21
# Wesley Key

class Student:
    def __init__(self, stn, yl, tkvar):
        self.student_name = stn
        self.year_level = yl
        self.difficulty = tkvar
    
    def year_l(self):
        if self.year_level not in ["1","2","3","4","5","6"]:
            return ["1","2","3","4","5","6"]
        
    def range(self):
        if self.year_level == 1 or self.year_level == 2:
            return [1,2,3,4]
        elif self.year_level == 3 or self.year_level == 4:
            return [2,3,4,5,6]
        else:
            return [4,5,6,7,8]
    
   # def leaderboard(self):
        
        
        