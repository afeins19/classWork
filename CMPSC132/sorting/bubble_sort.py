import random

def bubble_sort(iter): #temp = iter[j+1]
    for i in range(len(iter)):
        for j in range(len(iter)-i-1):
            if iter[j]>iter[j+1]:
                temp = iter[j+1]
                iter[j+1]=iter[j]
                iter[j]=temp
                print(i,j,iter, sep=':')
    return iter


gen_list = [random.randint(0,100) for i in range(10)]
print(bubble_sort(gen_list))

