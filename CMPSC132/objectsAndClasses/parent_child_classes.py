from classes.class_example import person

#This is an example of a child class which inherits methods from the 'person' class
class student(person):

    def __init__(self, status, major):
        super(person)
        self.is_student=status
        self.major=major

    def student_status(self, sBool):
        self.is_student=sBool
        return '\nIs Student?: '+str(self.is_student)

    def set_major(self, user_major):
        self.major=user_major.title()



p1 = student(True, 'compsci')
print(p1.major)





