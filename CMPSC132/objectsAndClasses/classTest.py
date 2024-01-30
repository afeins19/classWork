class car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def displayCar(self):
        print(self.make, self.model)

class ev(car):
    def __init__(self, make, model, range):
        super().__init__(self, make, model)
        self.range = range

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

a = Student('joe','swie','132')
b=ev('1','2','3')