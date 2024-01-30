'''This program will take a latex file as input, sort the entries (by ID) and return
a sorted version of the file as output.

This program makes use of regular expressions in order to find specific strings

store entries in dict in form {Id : entry}
then writes

Use of RegEx to search for key:
              ^@=starts with '@',
              .*=has zero or more occurances of any char
              {=last charectar before id is given
Program by Aaron Feinberg
'''

#todo: implement removal of leading empty lines

import re

#writes sorted version of latex file to a new file called 'sorted_file'
def sortById(file_address):
    idDict = dict()
    with open(file_address, 'r+') as fObj:

        for line in fObj.readlines():

            #split() returns a list with a white space in [0] and the string after the regex in [1]
            #if split doesnt find the regex it returns a list with our RegEx at [1]
            idRegex = re.split('^@.*{', line)
            #checks to see if split returns 2 values (if yes then it has found our RegEx in the line)
            if len(idRegex)==2:
                #storying the key in a temporary variable as we need to lock it in place to append strings to the value
                x = idRegex[1]
                idDict[x]=''
            #keeps adding lines from the file until idRegex returns another list of len 2 and the key changes
            idDict[x]+=line
    #goes through dict with keys in sorted order and writes the vals to file
    with open('sorted_file', 'w') as fObj:
        for id in sorted(idDict.keys()):
            fObj.write(idDict[id])

#please replace with a locatoin on your machine
file_address=r'/Users/aaronfeinberg/PycharmProjects/Playground/CMPSC_132_2019/related.bib'
sortById(file_address)
