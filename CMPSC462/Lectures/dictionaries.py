"""dictionaries: a python builtin mapping type
    - not linear data structures
    - data may only be accessed via keys which correspond to values

    - the key of a dictionary must be immutable
    """

"""creating a dictionary"""
#defining a dictionary
d = {'a':10, 'b':20}

#assignment
d['a'] = 10
d['a'] = 7 * 5

#adding values to a dict involves simply passing in a new key (note that values may not be duplicates)
d['c'] = 30
d['c'] = 40 #replaces the value at key 'c'

"""deleting values from a dictionary"""
del d['c'] #deleting with del keyword

d.clear() #clear() completely removes all values from a dict()

"""dictionary functions"""
d = {"user": "aaron", "id": "123", "password" : "abc"}
print(d.keys())
print(d.values())

print(d.items()) #this returns a TUPLE. tuples are like lists but tuples are IMMUTABLE

"Example: tuples as keys" \
"   - as tuples are immutable objects, they are valid keys"
numberGames = dict()

numberGames[(1,2,4)] = 8
numberGames[(4,2,1)] = 10
numberGames[(1,2)] = 12
print(numberGames)

"Example: crates"
boxes = dict()
jars = dict()
crates = dict()
boxes['cereal'] = 1
boxes['candy'] = 2
jars['honey'] = 4
crates['boxes'] = boxes
crates['jars'] = jars

print((crates['boxes']))








