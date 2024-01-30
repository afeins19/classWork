#global list
#-----------------------------------------------------
with open(r'fuction_list_modification.py') as fobj:
    for code in fobj.readlines():
        print(code,end='')

a=[100,101,102]

add_one = lambda x: x+1

def now_add_one(x):
    x[0]+=1

print('\n')

#our original list
print(a)

#the lambda opertaion on the elemet
print(add_one(a[0]))

#lambda does NOT assign so list is unchanged
print(a)

#calling the method which DOES modify the list
now_add_one(a)

#output proves list was indeed modified
print(a)

#--------------------------------------------------------