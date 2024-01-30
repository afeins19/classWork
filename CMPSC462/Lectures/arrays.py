"""Arrays are not builtin data structures in python, they are built using lists.
We will import a module to create arrays
    - note that as arrays are modeled  using lists, they can be sized dynamicallly
    - we can accomodate basically every data type  in python (signed, unsigned, longs, shorts, chars, str...)
"""

import array
import CommandLineTools as clt
clt.header("Arrays")
a = array.array('i', [1,2,3,4,5])  #i (signed int) is the type, then we pass in a list of values)
d = array.array('d', [i*1.0 for i in range(1,6)])
print(a)
print(d)


"""Accessing Elements & Slicing"""
clt.subsection("Accessing Elements & Slicing")
print(a[0])
print(a[:]) #no delimeter
print(a[:-2]) #ignore n values from the right (ignore the values 4,5)


"""Adding and Changing Items"""
clt.subsection("Adding and Changing Items")
a[0] = 10
print(a)

a[:2] = array.array('i', [2,4]) #we can pass in multiple values
print(a)

a.extend([7,8,9]) #appending these items to the array
print(a)

"""concatenating two arrays"""
clt.subsection("concatenating two arrays")
c = array.array('i', [65,900,21340])
concats = c+a
print(concats)

"""deleting elements"""
clt.subsection("deleting elements")
del c[0] #normal  delete keyword  (will throw error if item doesnt exst)
a.pop(2) #removes  and returns item
print(a)

"""important functions"""
clt.subsection("important functions")
print(a.itemsize) #returns the number of bytes allocated for this array
print(a.index(4))  #returns the index of the first occurance of this item
a.insert(5, 123454)
a.reverse()
print(a)




