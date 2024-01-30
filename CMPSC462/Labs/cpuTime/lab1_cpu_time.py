"""thisprogramwillgenerateaspecifiedquantityofintegers (minimum of 1000) using the rand function in range [1,10000]"""
import random
import time

def getDuration(start: time.time(), end: time.time()):
    return end - start

def getUniqueRandomNumbers(count: int, min:int, max:int):
    vals = []
    r = random.randint(min, max)
    for i in range(count):
        while r in vals:
            r = random.randint(min, max)
        vals.append(r)
    return vals

def getUniqueRandomDictKeys(count: int, d: dict):
    vals = []
    r = random.randint(0,len(d.keys()))
    for c in range(count):
        while r in vals or r not in d.keys():
            r = random.randint(0,len(d.keys()))
        vals.append(list(d.keys())[r])
    return vals
def printResults(title: str, list_times: [], dict_times: []):
    avg_list = sum(list_times)/len(list_times)
    avg_dict = sum(dict_times)/len(dict_times)
    print("\n"+title)
    print("\tList Times: "+str(list_times) + " | Average: "+str(avg_list))
    print("\tDict  Times: " + str(dict_times) + " | Average: "+str(avg_dict))

    if  avg_list < avg_dict:
        print("\t\tFastest: List")
    else:
        print("\t\tFastest: Dictionary")

test_dict = dict()
test_list=[]

for i in range(1000000):
    x=random.randint(1,100000)
    test_dict[i] = x
    test_list.append(x)

#test_list = [random.randint(1,100000) for i in range(1000000)]

"Print Testing"
list_print_times = []
dict_print_times = []

for i in range(3):
    start = time.time()
    print(test_list)
    end = time.time()
    list_print_times.append(getDuration(start,end))

    start = time.time()
    print(test_dict)
    end = time.time()
    dict_print_times.append(getDuration(start, end))


"""Retrieval Testing"""
list_retrieval_times = []
dict_retrieval_times = []

for i in range(3):
    r = random.randint(0,len(test_list))
    start=time.time()
    exists = r in test_list #performs a retrival and stores existance of the object in the list as a boolean
    end=time.time()

    list_retrieval_times.append(getDuration(start, end))
    start = time.time()
    exists = r in test_dict  # performs a retrival and stores existance of the object in the list as a boolean
    end = time.time()
    dict_retrieval_times.append(getDuration(start, end))

"""Insertion"""
list_insertion_times  = []
dict_inssertion_times = []


for i in range(3):
    r = random.randint(0,len(test_list))
    start=time.time()
    test_list.insert(r,r)
    end=time.time()
    list_insertion_times.append(getDuration(start,end))

    start = time.time()
    test_dict[r] = r
    end = time.time()
    dict_inssertion_times.append(getDuration(start, end))

#generating 3 unique random numbers to avoid removing items more than once
list_remove_indecies = getUniqueRandomNumbers(3, 1, len(test_list))
dict_remove_keys = list_remove_indecies
print(list_remove_indecies)

list_remove_times = []
dict_remove_times = []

"Deletion"

for j in list_remove_indecies:
    start=time.time()
    del test_list[j]
    end=time.time()
    list_remove_times.append(getDuration(start,end))

    start = time.time()
    test_dict.__delitem__(j)
    end = time.time()
    dict_remove_times.append(getDuration(start, end))

"output  section"
print("\n-------------------------------------- Results ---------------------------------------")
printResults("Printing", list_print_times, dict_print_times)
printResults("Retrieval", list_print_times, dict_print_times)
printResults("Insertion", list_insertion_times, dict_inssertion_times)
printResults("Deletion", list_remove_times, dict_remove_times)



