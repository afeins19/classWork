"""This program will generate a list of 1000 integers. The User will select a number from 1 to 1000. The program will
then try to find the number that the user has selected. This Implementation will feature binary search."""

import math
import sys

def memory_stats(objects):
    """returns sizes of a list of objects thats passed in"""
    return [(sys.getsizeof(o)) for o in objects]

# ORDERED List of of values
vals = [i for i in range(1,1001)]

#initial setup
low = 0
mid = 0
hi = len(vals) - 1

def iterative_binary_seach(vals, low, hi):
    while True:

        #starting guess for our range of numbers
        mid = vals[math.floor((low+hi) / 2)]
        print(memory_stats([vals, low, hi]))
        #present guess to user and await input
        response = input(f"is {vals[mid]} your number (l=lower, h=higher, y=yes): ").lower()

        #we guessed it
        if response == "y":
            print("yay!")
            break

        #value is lower (set highest possible guess to values after the current mid point)
        elif response == "l":
            hi = mid - 1

        #value is higher (set lowest possible guess to values before the current midpoint)
        elif response == "h":
            low = mid + 1

        else: #invalid input...
            print("INVALID INPUT\n")


def recursive_binary_search(vals, l, h):

    #mid point is recalculated based on reduced bounderies for our list
    mid = math.floor((l+h)/2)

    response = input(f"(l={vals[l]}, m={vals[mid]}, h={vals[h]}) | is {vals[mid]} your number (l=lower, h=higher, y=yes): ").lower()

    #printing our memory stats
    stats = memory_stats([vals, low, hi])
    print(f"Memory: vals = {stats[0]} | low = {stats[1]} | hi = {stats[2]}\n")

    # base case
    if response == "y":
        return "yay!"

    # if users guess is lower, consider everything from low to current guess - 1
    elif response == "l":
        return recursive_binary_search(vals, l, mid-1)

    # if users guess is higher, consider everything from 1 more than current guess to the high
    elif response == "h":
        return recursive_binary_search(vals, mid+1, h)

    # otherwise input invalid and let user repeat the same entry instruction
    else:
        print("INVALID INPUT\n")
        return recursive_binary_search(vals, l, h)


def iterative_binary_seach_reducing_list(vals, low, hi):
    while True:
        # starting guess for our range of numbers
        mid = math.floor(len(vals)/2)

        # print memory stats
        stats=memory_stats([vals, low, hi])
        print(f"Memory: vals = {stats[0]} | low = {stats[1]} | hi = {stats[2]}\n")


        response = input(f"is {vals[mid]} your number (l=lower, h=higher, y=yes): ").lower()

        # we guessed it
        if response == "y":
            print("yay!")
            break

        # value is lower (set highest possible guess to values after the current mid point)
        elif response == "l":
            hi = mid - 1
            vals = vals[:mid]

        # value is higher (set lowest possible guess to values before the current midpoint)
        elif response == "h":
            low = mid + 1
            vals = vals[mid + 1:]

        else:  # invalid input...
            print("INVALID INPUT\n")



#recursive_binary_search(vals, 0, len(vals)-1)
iterative_binary_seach_reducing_list(vals, low, hi)