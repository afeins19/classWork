import random
import timeit


def selection_sort(data):
    """uses the selection sort algorithm to sort the data in the db based on a given attribute"""


    """Selection sort:
        1. traverse array
        2. find smallest element
        3. swap element with the lowest position
        4. reduce the search size of the array from the left by 1 
        5. repeat until search range is 0
    """
    for sorted_line in range((len(data))):
        mindex = sorted_line

        # this traverses the unsorted portion of the list and tries to find the index of the smallest element
        for i in range(sorted_line, len(data)):
            if data[i] < data[mindex]:  # we are comparing the attribute of each dictionary object
                mindex = i

        # after the traversal, mindex holds the index of the smallest item
        # so perform a swap
        data[sorted_line], data[mindex] = data[mindex], data[sorted_line]


    return data


def insertion_sort( data):
    """uses the insertion sort algorithm to sort the data in the db based on a given attribute"""


    """Insertion sort: 
        1. traverse array
        2. if 2 elements being compared are not in order, swap the smaller element
        with those in the sorted part ot the list until its place is found
        3. expand the sorted line by 1
        4. continue until we have traversed the array
    """

    for sorted_line in range(1, len(data)):
        j = sorted_line
        while j > 0 and data[j - 1] > data[j]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1


    return data

def bubble_sort(data):
    """uses the bubble sort algorithm to sort the data in the db based on a given attribute"""


    """bubble sort:
        1. traverse the list until the len(data) - sorted_line 
        2. compare adjacent elements
        3. if n-1 item is greater than n item perform swap
        4. continue until we hit the sorted line
        5. increment sorted line by 1           
    """

    # iterate over array...sorted area is formed at the end
    for sorted_line in range(len(data)):
        for i in range(0, len(data) - sorted_line - 1):
            if data[i] > data[i + 1]:
                data[i + 1], data[i] = data[i], data[i + 1]

    return data

def merge_sort(data):

    sorted_data = merge_sorter(data)

    return sorted_data


def merge_sorter(data):
    """Recursive function to split the lists"""

    """Merge sort:
        1. continously divide the list into 2 equal sublists l,r until each sublist of length 1
        2. sort the sublists and recombine with its partner and call a sort function to merge those 2 lists back into one
        3. repeat util we have reassembled list back (done automatically through recursion)
    """
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    l_sorted = merge_sorter(left)
    r_sorted = merge_sorter(right)

    return make_merge(l_sorted, r_sorted)


def make_merge(left_sublist, right_sublist):
    """helper function...recieves subarrays down from the merging function and sorts them"""
    merged = []

    # indicie tracking
    l, r = 0, 0

    # first we compare elements from the sublists and select items to be placed into our fully merged output
    while l < len(left_sublist) and r < len(right_sublist):
        if left_sublist[l] < right_sublist[r]:
            merged.append(left_sublist[l])
            l += 1
        else:
            merged.append(right_sublist[r])
            r += 1

    # if items remain in any of these sublists, add them to the merged list
    while l < len(left_sublist):
        merged.append(left_sublist[l])
        l += 1

    # ...emptying right sublist
    while r < len(right_sublist):
        merged.append(right_sublist[r])
        r += 1

    return merged

def make_stats(function_to_call, *args, num=1):
    """takes in a function and can run it num-times"""
    time = timeit.timeit(lambda: function_to_call(*args), number=num)
    return str(time / num)

fixed = [random.randint(0, 10000) for _ in range(2000)]

test_data = fixed.copy()
print("Merge:"+make_stats(merge_sorter, test_data))
test_data = fixed.copy()
print("Buble:"+make_stats(bubble_sort, test_data))
test_data = fixed.copy()
print("Insertion: "+make_stats(insertion_sort, test_data))
test_data = fixed.copy()
print("Selection: "+make_stats(selection_sort, test_data))

