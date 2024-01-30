names = ['Bob', 'mel', 'val', 'Ab', 'mia']

for i in range(0,len(names),2):
    print(names[i])

alt_names = [names[n] for n in range(1,len(names),2)]
print(alt_names)

#------------------
myList = [0,1,2,3,4,5,6,7,8,9]
print(myList[::2])

#------------------
books=['Calculus','Agebra','art history','word','history']
books.sort(key=str.lower)
print(books)

print(list(range(0,10)))

#---------
a=set([1,2,3,1])
print(a)