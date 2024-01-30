'''
Created on Dec 3, 2018

@author: aaronfeinberg
'''
class student:
    
    def __init__(self):
        self.name = raw_input("Name: ")
        self.age = raw_input("Age: ")
    
    def getGpa(self):
        self.gpa = float(raw_input("GPA: "))
        

        
        
freshman = student()
freshman.getGpa()
print(vars(freshman))
