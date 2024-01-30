
#Program by Aaron Feinberg
#this program instructs the user to enter 3 values: a,b,c
#the user then inputs max and min values for a variable x
#the program will check all possible solutions to an
#inequality of the form ax + b < c  between the given ranges of x

#!/usr/bin/env python

var_list=['a','b','c','x_min','x_max']
solution_set=[]
lrg=0

for i in range(len(var_list)):
        var_list[i] = int(input('Please input value for '+var_list[i]+': '))


#min/max are stored in positions 3,4 in var_list
for x in range(var_list[3],var_list[4]):
    if var_list[0] * x + var_list[1] < var_list[2]:
        solution_set.append(x)


