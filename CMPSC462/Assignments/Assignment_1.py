"""CMPSC 462 – Assignment-1 (30 points)
Lists and Dictionaries
Due date: 8/29/2023
Note: attach screenshots of your program and results under each programming exercises. Please make
sure that the screenshot is readable. Don’t attach a very small screenshot image.
Exercise:(1-5) - 6 points each
"""

"""Exercise-1:
Write a function called is_sorted (without using inbuilt sort function) that takes a list as a parameter and
returns True if the list is sorted in ascending order and False otherwise. You can assume (as a
precondition) that the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
--- your screenshots of program and results here --
"""


# uses the ascii function to compare adjacent items
def is_sorted(data: []):
    if data is None or len(data) == 0:  #empty argument handling
        return
    if len(data) == 1:  #if data is a single element, it is sorted
        return True
    else:
        for i in range(len(data) - 1):
            if ascii(data[i]) > ascii(data[i + 1]): #compare adjacent ascii values
                return False
        return True


print("Exercise 1: ")
print("\t[1,2,2] is sorted: " + str(is_sorted([1, 2, 2])))
print("\t['b','a'] is sorted: " + str(is_sorted(['b', 'a'])))

"""Exercise-2:
What command you would use to do the following for this dictionary:
dict1 = {'a': 10, 'b': 20, 'c': 30, ‘d’:20}
1. Update an entry in dict1
2. Show how to remove the duplicate values from dict1"""

print("\nExercise 2: ")
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 20}

# deleting a duplicate
"""Algorithm
(1) get keys and values of our dict
(2) iterate over the lists
(3) check to see if the our currently observed value at index i 
exists in the list with range [0:i]
"""

keys = list(dict1.keys())
vals = list(dict1.values())

for i in range(len(keys)):
    if dict1[keys[i]] in vals[0:i]:
        del dict1[keys[i]]

# updating a value
print("\t(original): " + str(dict1['c']))
dict1.update({'c': 500})  # pass in a new dict to specify the updated value
print("\t(updated):  " + str(dict1['c']))
print("\tduplicates now removed: " + str(dict1))

"""Exercise 3: Write a function called remove keys(mydict, keylist) that accepts two parameters: a dictionary called
mydict and a list called keylist. remove keys(mydict, keylist) should remove all the keys contained in
keylist from mydict and return the dictionary:
d = { "key1" : "value1", "key2" : "value2", "key3" : "value3", "key4"
: "value4" }
keys = ["key1", "key3", "key5"]"""



print("\nExercise 3: ")

d = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
keys = ["key1", "key3", "key5"]
def remove_keys(d: dict, keys: []):
    data = d
    if d is None or len(d) == 0:
        return
    else:
        for k in keys:
            if k in data.keys():
                del data[k]
    return data


print("\toriginal: " + str(dict1))
print("\tRemoved:  " + str(remove_keys(d, keys)))

"""Exercise-4:
Write a function called word frequencies(mylist) that accepts a strings of words and returns a dictionary
where the keys are the words from the string of words and the values are the number of times that
word appears in mylist:
S = “Fred fed Ted bread, and Ted fed Fred bread”
word_freq = {’Fred’:2, ’fed’:2, ’Ted’:2, ’bread’:2, ’and’:1}"""

print("\nExercise 4:")
S = "Fred fed Ted bread, and Ted fed Fred bread"
def word_freq(s):
    freq = dict()
    words = s.replace(',', '').split() #remove punctuation from our string and add each word to a list

    for w in words:
        if w not in freq.keys(): #if the word isnt in our dict, add it
            freq[w] = 1
        else:
            freq[w] += 1    #if the word is in our dict, append its frequency
    return freq


print("\tword frequencies: " + str(word_freq(S)))

"""Exercise-5:
Write a Python program to combine two dictionaries, adding values for common keys.
"""
d1 = {'x': 100, 'y': 200, 'm':100}
d2 = {'x': 200, 'n': 100, 'y':200}

def combine_dicts(d1:dict, d2: dict):
    #create a new dict afor temporary storage
    out = dict()
    #create combined lists of keys for d1 and d2
    all_keys = list(d1.keys())
    all_keys += d2.keys()

    for k in all_keys:
        if k in d1.keys() and k in d2.keys():
            out.update({k: d1[k] + d2[k]})
        elif k in d1.keys() and k not in d2.keys():
            out.update({k: d1[k]})
        elif k in d2.keys() and k not in d1.keys():
            out.update({k: d2[k]})
    return out


print("\nExercise 5")
print("\td1: " + str(d1))
print("\td2: " + str(d2))
print("\tcombined: "+str(combine_dicts(d1,d2)))

