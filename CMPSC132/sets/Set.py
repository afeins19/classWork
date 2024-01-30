#declare our set here
mySet=set()

mySet.add(1)
mySet.add(2)

#adding true to the set will not add anything
#python consciders True as 1
mySet.add(True)

print(mySet)
print(len(mySet))

#discard wont incure errors if item is not in set
mySet.discard(55)

#dictionaries must have unique keys
myDict={} # empty dictionary

myDict['US']='Washington DC'
myDict['China']='Beinjing'

#fetching from dict
print(myDict.get(1))
print(list(myDict.values()))

#looping through dict
print('\n')
for k,v in myDict.items():
    print(k +' - '+ v)

