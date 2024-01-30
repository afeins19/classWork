#this program will all users to register thier pets into a registry
#this registry stores pets in a list, with each element bein a dictionary
#which itself has 3 elements (name, pet-type, age)

#global registry
pet_registry = list()

def register_pet(pet_name, animal_type, age=0):
    '''Function recieves and stores pet attributes in dictionary'''
    pet_attributes = {'Name':pet_name,'Type':animal_type,'Age':age}
    pet_registry.append((pet_attributes))


register_pet('Gary','Snail',10)
register_pet('Lary','Kale',10)
register_pet('Mary','Whale',10)


for pet in pet_registry:
    for atr in pet:
        print(atr+': '+ str(pet[atr]),end=', ')
    print('\n')







