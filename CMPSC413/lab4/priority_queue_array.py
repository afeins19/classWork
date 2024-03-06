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
        2. In the worst case, describe the runtime to remove the target with highest priority.
        3. In the worst case, describe the runtime to change the priority of an target (find an target and
        change the priority of the target).
        Show an example for each.

Exercise-2:
    Write down the algorithm and implement a priority queue (both min and max) using a linked list of
    elements. Determine the runtime for each of the following:
        1. In the worst case, describe the runtime to insert an item into the priority queue.
        2. In the worst case, describe the runtime to remove the target with highest priority.
        3. In the worst case, describe the runtime to change the priority of an target.
        Show an example for each.


Exercise-3:
    Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based
    data structure (both min and max). Determine the runtime for each of the following:
    1. In the worst case, describe the runtime to insert an item into the priority queue.
    2. In the worst case, describe the runtime to remove the target with highest priority.
    3. In the worst case, describe the runtime to change the priority of an target.
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
from base_classes import Comparator, PriorityQueueElement


class priorityQueueArray():
    def __init__(self):
        self.pq = []
        self.is_min = True

        self.cp = Comparator(self.is_min)

    def is_empty(self):
        return True if self.pq is None else False

    def insert(self, priority, value):
        new_element = PriorityQueueElement(priority, value)

        if self.is_empty():
            self.pq.append(new_element)

        else:
            idx_found = False

            for i in range(len(self.pq)):   # iterate over elements
                if self.cp.compare(priority, self.pq[i].p): # compare using chose priority order of queue
                    self.pq.insert(i, new_element)
                    idx_found = True
                    break

            if idx_found == False:
                self.pq.append(new_element)

    def peek(self):
        if not self.is_empty():
            return self.pq[0]

    def delete(self):
        if not self.is_empty():
            del self.pq[0]

    def change_priority(self, new_priority, val):
        # finds target, deletes it and creates a new one with the updated priority
        element_idx = None

        for i in range(len(self.pq)):
            if sel.pq[i].val == val:
                element = self.pq[i]
                break

        if element_idx:
            del self.pq[element_idx]  # drop target from the list

        self.insert(new_priority, val) # add it back as a new target with different priority


a = priorityQueueArray()
a.insert(2,2)
a.insert(3,4)
a.insert(1,2)

print(a.peek())

