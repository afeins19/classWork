"""Sets
    - contain unique objects
    - every target is unique and immutable (no lists or dictionaries)
    - same as math sets
    - union, intersectoin, symmetric difference
"""

import CommandLineTools as clt

"creating a set"
set1 = {1, 2, 3} #integer data type
print(set1)

set2 = {1, 1.0, "hi", (1,2,3)} #1 and 1.0 are not unique (python treats them as the same)
print(set2)

set3 = set([1,2,3,2]) #as lists are immutable, the set() function takes each item in the list places it inside
print(set3)

print(set("python rocks"))
for each in set("python rocks"):
    print(each)

print("\n")
"adding elements to a set"
set4 = {1,2,3}
print(set4)

set4.add(5)
print(set4)

set4.update([2,3,4,6]) #will add elements if they are unique
print(set4)

set4.add((1,2,8)) #note that tuples are added as distinct objects
print(set4)

set4.update(['a','b'], ('a','c')) #update takes elements out of their containers and places them into the set if they are unique
print(set4)
print("\n")
"removing elements from a set" \
"- note that we must know the specific target we are accesing to remove it " \
"- discard(): works like remove but does not throw an error if the item being removed is not in the set" \
"- remove(): removes an target from a set but will throw an error if the target being removed doesnt exist"
print("\n")
set1 = {1, 3, 4, 5, 6}
print(set1)
set1.discard(4)
print(set1)
set1.remove(6)
print(set1)

print("\n")
A = {1,2,3,4,5}
B= {4,5,6,7,8}

#union...all are equal operations
print(A | B)
print(A.union(B))
print(B.union(A))

print("\n")

#intersetion...all are equal operations
print(A & B)
print(A.intersection(B))
print(B.intersection(A))

print("\n")

#difference A - B or B - A
print(A - B) #different
print(B - A) #different
print(A.difference(B))
print(B.difference(A))

print("\n")

#symmetric difference (removes elements that are shared)
print(A ^ B) #same
print(B ^ A) #same
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

"""More Useful builtin functions for sets"""
C = A  #C is  a set now equal to A

C.discard(1) #discarding an target from the set, if it doesnt exist, no  error is  thrown
print(C.isdisjoint(A)) #returns true if intersection with this set is the null set
print(C.issubset(A)) #if C is a subset of A, then this will return true
print(A.issuperset(C)) #if  A contains C, then this will return true
B.intersection_update(C) #udpates the set with the intersection of the argument set
print(B)

"""Frozen Sets - sets that have all the functionality of normal sets but are immutable"""
print("\nFrozen Sets:\n")
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A.isdisjoint(B))
print(A.difference(B))
print(A | B)


