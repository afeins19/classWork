import random

from base_classes import PriorityQueueElement, Comparator

from priority_queue_array import PriorityQueueArray
from priority_queue_linked_list import PriorityQueueLinkedList
from priority_queue_heap_array import PriorityQueueHeap
from heap_sort import heap_sort

    # Demonstration

    # min heap

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# test elements
elements = [(random.randint(0,100), alpha[i]) for i in range(5)]
print(f"Unordered Array of Elements: { elements }\n")

    # Exercise 1 - priority queue array
print("\nArray Implementation")
priority_queue_array = PriorityQueueArray(is_min=True)

# inserting elements
for element in elements:
    priority_queue_array.insert(element[0], element[1])

# Elements now in heap
print(priority_queue_array.pq)

# removing largest element
print(priority_queue_array.delete())

# changing an elements priority
target_v = priority_queue_array.pq[0].v
target_p = priority_queue_array.pq[0].p

print(f"Changing Priority of { target_p, target_v }")
priority_queue_array.change_priority(new_priority=100, val=target_v)
print(priority_queue_array.pq)


    # Exercise 2 - linked list
print("\nLinked List Implementation")
priority_queue_linked_list = PriorityQueueLinkedList()

# inserting elements
for element in elements:
    priority_queue_linked_list.insert(element[0], element[1])

# removing largest element
print(priority_queue_linked_list.delete())

# changing an elements priority
target_v = priority_queue_linked_list.head.element.v
target_p = priority_queue_linked_list.head.element.p

print(f"Changing Priority of { target_p, target_v }")
priority_queue_linked_list.change_priority(new_priority=100, val=target_v)

# checking the final element of the linked list
cur = priority_queue_linked_list.head

while cur.next:
    cur = cur.next

print(f"Now moved to the end of the priority Queue: {cur.element}")


    # Exercise 3 - Heap Tree (Array Based)
print("\nHeap Implementation")
priority_queue_heap = PriorityQueueHeap(is_min=True)

# inserting elements
for element in elements:
    priority_queue_heap.insert(element[0], element[1])

# printing elements in heap
print(priority_queue_heap.pq)

# changing elements priority
# changing an elements priority
target = priority_queue_heap.pq[0]
target_p = priority_queue_heap.pq[0].p

print(f"Changing Priority of { target.p, target.v }")
priority_queue_heap.change_priority(new_priority=100, element=target)
priority_queue_heap.bubble_down()
print(f"Last Element is now: {priority_queue_heap.pq}")

    # Exercise 4 - Heap Sort
print("\nHeap Sort")

print(f"unordered elements: {elements}")
print(f"sorted elements using heap-sort (normal order): { heap_sort(elements)}")
print(f"sorted elements using heap-sort (Reverse order): { heap_sort(elements, reverse=True)}")



    # Max Heap

# Exercise 1 - priority queue array
print("\nArray Implementation")
priority_queue_array = PriorityQueueArray(is_min=False)

# inserting elements
for element in elements:
    priority_queue_array.insert(element[0], element[1])

# Elements now in heap
print(priority_queue_array.pq)

# removing largest element
print(priority_queue_array.delete())

# changing an elements priority
target_v = priority_queue_array.pq[0].v
target_p = priority_queue_array.pq[0].p

print(f"Changing Priority of { target_p, target_v }")
priority_queue_array.change_priority(new_priority=100, val=target_v)
print(priority_queue_array.pq)


    # Exercise 2 - linked list
print("\nLinked List Implementation")
priority_queue_linked_list = PriorityQueueLinkedList(is_min=False)

# inserting elements
for element in elements:
    priority_queue_linked_list.insert(element[0], element[1])

# removing largest element
print(priority_queue_linked_list.delete())

# changing an elements priority
target_v = priority_queue_linked_list.head.element.v
target_p = priority_queue_linked_list.head.element.p

print(f"Changing Priority of { target_p, target_v }")
priority_queue_linked_list.change_priority(new_priority=100, val=target_v)

# checking the final element of the linked list
cur = priority_queue_linked_list.head

while cur.next:
    cur = cur.next

print(f"Now moved to the end of the priority Queue: {cur.element}")


    # Exercise 3 - Heap Tree (Array Based)
print("\nHeap Implementation")
priority_queue_heap = PriorityQueueHeap(is_min=False)

# inserting elements
for element in elements:
    priority_queue_heap.insert(element[0], element[1])

# printing elements in heap
print(priority_queue_heap.pq)

# changing elements priority
# changing an elements priority
target = priority_queue_heap.pq[0]
target_p = priority_queue_heap.pq[0].p

print(f"Changing Priority of { target.p, target.v }")
priority_queue_heap.change_priority(new_priority=100, element=target)
priority_queue_heap.bubble_down()
print(f"Last Element is now: {priority_queue_heap.pq}")

    # Exercise 4 - Heap Sort
print("\nHeap Sort")

print(f"unordered elements: {elements}")
print(f"sorted elements using heap-sort (normal order): { heap_sort(elements)}")
print(f"sorted elements using heap-sort (Reverse order): { heap_sort(elements, reverse=True)}")

