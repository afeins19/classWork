"""CMPSC 462 Data Structures and Algorithms Project 2"""
import copy
import math
import random
import timeit

from prettytable import PrettyTable

from SearchClass import SearchClass as searcher
from SortingClass import SortingClass as sorter

# Generating 10000 random numbers
pool = [random.randint(1,100000) for i in range(100000)]
s_pool = sorted(pool)

# getting the number at a random index in pool, then using that as our search target
ind=random.randint(0,len(pool)-1)
target = pool[ind]
print(f"Target: {target} @ Index {ind}")

# Instantiating our search class
search = searcher()

# Performing Linear Search
linear_search_time = timeit.timeit(lambda: search.linear_search(pool, target), number=5) / 5
print(f"Linear Search: {linear_search_time}\n")

# Performing Binary Search (we will pass in a sorted copy of pool)
binary_search_time = timeit.timeit(lambda: search.binary_search(s_pool, target), number=5) / 5
print(f"Binary Search: {binary_search_time}\n")

print(f"Binary Search is {round(linear_search_time/binary_search_time)} times faster than linear Search\n")

# Determining if List is unique and if not getting duplicate values
unique_values_time = timeit.timeit(lambda: search.unique_values(pool), number=5) / 5
print(f"\nUnique Values time: {unique_values_time}")


#min/max finding
min_search_time = timeit.timeit(lambda: search.min(pool), number=5) / 5
print(f"min value Search: {min_search_time}\n")

max_search_time = timeit.timeit(lambda: search.max(pool), number=5) / 5
print(f"max value Search: {max_search_time}\n")

print(pool)
print("\n")
# SORTING

sort = sorter()



sort_times = {"Merge": [], "Insertion": [], "Selection": [], "bubble": []}



for i in range(3):

    merge_time = timeit.timeit(lambda: sort.merge_sort(pool), number=1)

    insertion_time = timeit.timeit(lambda: sort.insertion_sort(pool), number=1)

    selection_time = timeit.timeit(lambda: sort.selection_sort(pool), number=1)

    bubble_time = timeit.timeit(lambda: sort.bubble_sort(pool), number=1)

    sort_times["Merge"].append(merge_time)
    sort_times['Insertion'].append(insertion_time)
    sort_times['Selection'].append(selection_time)
    sort_times['bubble'].append(bubble_time)

print(sort_times)
print(pool)
table = PrettyTable()

# Add columns
table.field_names = ['Algorithm', 'Run 1', 'Run 2', 'Run 3']
for key, values in sort_times.items():
    table.add_row([key] + values)

print(table)