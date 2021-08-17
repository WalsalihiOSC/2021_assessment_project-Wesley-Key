# Student Class - Primary Maths Program
# 05/07/21
# Wesley Key

class Student:
    
    def __init__(self, name, year_level, num, difficulty):
        self.student_name = name
        self.year_level = year_level
        self.difficulty = difficulty
        self.range = num
        
    def year_l(self):
        if self.year_level not in ["1","2","3","4","5","6"]:
            return ["1","2","3","4","5","6"]  
            
    def ranges(self):
        if self.range == "1" or self.range == "2":
            return [0,1,2,3,4]
        elif self.range == "3" or self.range == "4":
            return [1,2,3,4,5]
        else:
            return [3,4,5,6,7]
            
    def confirm(self):
        results_file = open("math_results.text", "a")
        results_file.write("-------------------------\n")
        results_file.write(f"Student Name: {self.student_name} \n"
                            f"Year Level: {self.year_level} \n"
                            f"Operation: {self.difficulty}")
        
        results_file.write("-------------------------\n")
        results_file.close()
        
    
        
        