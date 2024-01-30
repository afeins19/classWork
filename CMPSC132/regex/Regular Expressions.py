'''You can use regular expressions to find a patterns
in a huge string file for example

Definition: A regular expression, regex or regexp is a sequence of characters that define a search pattern.
Usually such patterns are used by string searching algorithms
for "find" or "find and replace"
operations on strings, or for input validation.
'''

#from https://www.w3schools.com/python/python_regex.asp

import re

#findall(): returns list with all occurences of 'ai'
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

#search: returns a matchobject of the first occurence

str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())


#test for hw:

#needs to seart by id
str='@article{id'
print(re.split('1',str,maxsplit=1))
