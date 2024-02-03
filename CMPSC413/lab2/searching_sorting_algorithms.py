""" CMPSC 412 - Lab 2: Searching and Sorting


1. Write and implement the algorithm for Linear search, Binary search, Insertion sort, Selection sort
and Bubble sort. Calculate the time complexity for these searching and sorting algorithms.
Table-1: tabulate the time complexity for these algorithms with best and worst time
complexities.

"""
import random

def linear_search(val, data=[]):
    for v in data:
        if v == val:
            return val

def binary_search(val, data=[]):
    if not data:
        return None


    # sort data first (use insertion since we might get a sorted list...insertion is faster)
    data = insertion_sort(data)

    mid = len(data)//2
    l,r = 0, len(data)-1

    while l <= r:
        mid = l + ((r - l) // 2) # find mid again based on l,r

        if val > data[mid]:
            l = mid + 1

        elif val < data[mid]:
            r = mid - 1

        elif val==data[mid]: # got it
            return (data[mid], f'idx={ mid }')

    return None

def selection_sort(data=[]):
    if not data:
        return None

    for i in range(len(data)):
        min_idx = i # store index of current min element

        for j in range(i + 1, len(data)):

            # find the minimum of the unsorted portion
            if data[j] < data[min_idx]:
                min_idx = j

        # swap
        temp = data[i]
        data[i] = data[min_idx]
        data[min_idx] = temp

    return data

def insertion_sort(data=[]):
    if not data:
        return None


    for i in range(1, len(data)):

        key = data[i] # value were comparing
        comp_idx = i - 1

        # shift elements until correct spot is found
        while key < data[comp_idx] and comp_idx > 0:
            data[comp_idx + 1] = data[comp_idx]
            comp_idx -= 1

        # putting the data in the right spot
        data[comp_idx + 1] = key


    return data

def bubble_sort(data=[]):
    if not data:
        return None

    for i in range(len(data)):
        for j in range(0, len(data) - i - 1): # sorted part at end of list
            if data[j] < data[i]:
                # swap
                temp = data[i]
                data[i] = data[j]
                data[j] = temp

    return data


print(binary_search(2, [random.randint(0,100) for i in range(1000)]))