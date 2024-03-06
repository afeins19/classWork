"""CMPSC 462 – Assignment-2 (30 points)

Due date: 1 week
Note: attach screenshots of your program and results under each programming exercises. Please make
sure that the screenshot is readable. Don’t attach a very small screenshot image.

1. Create a Python program that asks the user to enter two sets of comma-separated values. Use the
string split() method to parse the line and then use the set() function to covert the lists to sets.
Demonstrate set theory for the two sets by displaying the two sets and their relationship to each
other as subset, superset, union, intersection, and difference. 8 points

2. How can the last target of a set be deleted? Justify your answer? 4 points

3. Write a Python function to find whether a given array of integers contains any duplicate target?
Your function should return true if any value appears more than once and return false if every
target is distinct. 7 points

4. Write a Python function which takes two int arrays as inputs and returns an array containing
common elements from those two arrays. 7 points

5. Answer the following? 4 points
    a. Is a set a subset of itself? Explain?
    b. What happens if you pass a dictionary to a set constructor? for example: set(dictionary1).
    Explain?

Deliverables:
    1. This assignment word file - program and Outputs with appropriate screenshots
"""
import CommandLineTools as clt
import array

"Exercise 1"

def makeSetOfInts(vals: list):
    return set([int(val) for val in vals])

a =  input("please input your first list of comma separated values: ").split(",")
b =  input("please input your second list of comma separated values: ").split(",")

set_a = makeSetOfInts(a)
set_b = makeSetOfInts(b)

clt.header("Set Operations")
clt.header("a is a subset of b?")
print(set_a.issubset(set_b))

clt.header("a is a superset of b?")
print(set_a.issuperset(set_b))

clt.header("Union")
print(set_a.union(set_b))

clt.header("intersection")
print(set_a.intersection(set_b))

clt.header("difference")
print(set_a.difference(set_b))

"Exercise 3"

def any_duplicates(arr: array.array):
    if len(set(arr)) == len(arr):
        return False
    return True

clt.header("Duplicates")
print(any_duplicates(array.array('i', [1,2,3,2])))

"Exercise 4"

def get_common_elements(arr1: array.array, arr2: array.array):
    return array.array('i', list(set(arr1).intersection(set(arr2))))

clt.header("Common Elements")
common_array=get_common_elements(array.array('i', [1,2,3,4]), array.array('i', [3,4]))
print(common_array)

clt.header("Passing dict to a set")
d={'a':1,'b':2,'c':3, 'c':4, 'd':3}
print(set(d))