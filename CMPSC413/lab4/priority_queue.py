""""
Lab Exercises:
The priority queue is an abstract data type that contains the following methods:

insert(item, priorityValue)
Inserts item into the priority queue with priority value priorityValue.

peek()
Returns (but does not remove) the item with highest priority in the priority queue.

delete()
Removes and returns the item with highest priority in the priority queue.

changePriority(item, newPriority)
Changes the priority of an item to a new priority value.

Exercise-1:
Write down the algorithm and implement a priority queue (both min and max) using an array of
elements. Determine the runtime for each of the following:
1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element (find an element and
change the priority of the element).
Show an example for each.

Exercise-2:
Write down the algorithm and implement a priority queue (both min and max) using a linked list of
elements. Determine the runtime for each of the following:
1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element.
Show an example for each.

Exercise-3:
Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based
data structure (both min and max). Determine the runtime for each of the following:
1. In the worst case, describe the runtime to insert an item into the priority queue.
2. In the worst case, describe the runtime to remove the element with highest priority.
3. In the worst case, describe the runtime to change the priority of an element.
Show an example for each.

Exercise-4:
Write down the algorithm and implement a heap sort (both ascending and descending) using heap data
structure. Determine the runtime for each of the following.

1. In the worst case, describe the runtime to sort in ascending order.
2. In the worst case, describe the runtime to sort in descending order.

Exercise-5:
Tabulate to compare the time complexity of insert, remove and change priority operations for array/linked
list/ heap priority queues.

Exercise-6: Conclusion
Write a paragraph about what have you learnt from this lab exercises?

Deliverables:
 Codes
 Report with algorithms, screenshots of results for each exercise and conclusion (exercise-6).
 Attach the codes as appendix in your report.
 Recorded video of demonstration (~5 minutes)

"""

# will be an element in the priority queue, contains the value and the priority
class priorityQueueElement():
    def __init__(self, priority, value):
        self.p = priority
        self.v = value
    def __repr__(self):
        return f"[{self.p} , {self.v}]"

class priorityQueueArray():
    def __init__(self):
        self.pq = []

    def insert(self, priority, value):
        self.pq.append(priorityQueueElement(priority, value))