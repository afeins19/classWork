'''Clossed for modificaition, open for extension - prof. hussain, 2019'''

'''A class is a blueprint for an object'''

#super class which holds all subclasses
class Animal():

    def __init__(self, kind):
        self.kind = kind

class Dog(Animal):
    '''a simple attempt to model a dog.'''
    def __init__(self,name, age, kind='dog'):
        super()
        self.name = name
        self.age = str(age)

    def sit(self):
        '''simulates a dog sitting'''
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        '''doggo will roll over'''
        print(self.name.title() + ' rolled over!')


myDog = Dog('Dog','Sparky','8')
print(myDog.kind)
myDog.roll_over()


