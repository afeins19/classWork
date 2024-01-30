class person:

    #class variables (global to all objects from this class
    is_sexy_boi = True

    def __init__(self, name='-' , age='-'):
    #initialises the objects in the class (like constructor?)
    #these are INSTANCE variables (belong to each object and can reference different values)
        self.name = name.title()
        self.age = str(age)

    def display(self):
        print('Name: '+self.name)
        print('age: '+self.age)

    def get_info(self):
        self.name = input('Please input your name: ')
        self.age = input('Please input your age: ')

    def greet(self):
        print(self.name+' says Hello!')


student_list= [person(age=19),person('jake',19)]
student_list[0].get_info()
print(student_list[0].display())