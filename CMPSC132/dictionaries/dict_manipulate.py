#dictionaries are unordered and familiar (for accesing)
#syntax: {key : value,}
myCat = {'size' : 'fat', 'color' : ' gray', 'disposition': 'loud'}
print('My cat is '+myCat['size'])

#compare to lists which are only equal when ordered:
list_a=[1,2,3,4]
list_b=[4,3,2,1]

print(list_a==list_b) #False

#car dict
toyota_matrix = {'make': 'Toyota', 'model': 'Matrix', 'color': 'black', 'engine': '1.8L'}

#print boolean val for item in dict
print('model' in toyota_matrix)
print('transmission' in toyota_matrix)
print('Toyota' in toyota_matrix.values())

#built-in methods for searching dicsts
#.keys() & .values() returns a *VEIW OBJECT*
#you must cast as list it to make it a list
print(list(toyota_matrix.keys()))
print(list(toyota_matrix.values()))

#iterate with loop through keys or values
print('\n')
for att in toyota_matrix.keys():
    print(att)

#ITEMS Method:
#returns a 2 elemet tuple
print(list(toyota_matrix.items()))

#multiple assignemnt in pyhton
print('\n')
for k, v in toyota_matrix.items():
    print(k+':',v)

#get method(key, defualt)
print(toyota_matrix.get('transmission','<Attribute Not Available>'))

#setdeuafult() method:
#if key does not exist, append a k-v pair
#if the k-v pair is already present, then this does not affect the dict
toyota_matrix.setdefault('transmission','automatic (cositionada)')
print(toyota_matrix)



