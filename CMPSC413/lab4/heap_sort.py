"""

Write down the algorithm and implement a heap sort (both ascending and descending) using heap data
structure. Determine the runtime for each of the following.

"""
import random

from base_classes import PriorityQueueElement, Comparator
from priority_queue_heap_array import PriorityQueueHeap

def heap_sort(arr=None, reverse=False):
    is_min = True

    # if we want to sort in descending order (reversed, we can set our heap to be a maxheap)
    if reverse:
        is_min = False

    heap = PriorityQueueHeap(is_min=is_min)
    sorted_array = []

    # add elements to the heap
    for element in arr:
        heap.insert(element[0], element[1])

    # root contains highest priority element -> pop into list
    while not heap.is_empty():
        root_element = heap.delete()

        if root_element is not None:
            sorted_array.append(root_element)

    return sorted_array

#test = [(random.randint(0,50), 'element') for i in range(5)]


#print(heap_sort(test,reverse=False))
#print(heap_sort(test,reverse=True))



