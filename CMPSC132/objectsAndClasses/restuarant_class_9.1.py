class Restuarant():

    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
        self.is_open = False

    def describe_restuarant(self):
        print(self.restuarant_name.title() + 'is serves '
              + self.cuisine_type.title() + ' food.')
    def openRestuarant(self):
        self.is_open=True

class bar(Restuarant):
    
    def __init__(self, barName,  bar_type='boozy dive bar'):

        self.bar_type=bar_type
        self.bar_name= barName

    def describe_bar(self):
        print('my bar is a '+self.bar_type)







my_res = Restuarant('kilt & wilt','scottish')
print(my_res.restuarant_name)
my_res.describe_restuarant()
my_res.openRestuarant()
print(my_res.is_open)

my_bar = bar("shoe")
my_bar.describe_bar()
print(my_bar.bar_name)
