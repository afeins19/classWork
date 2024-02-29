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

class comparator():
    # returns a function to be used in lambda based on the ordering scheme of the priority queue
    def __init__(self, is_min=True): # by default sorts by min priority first
        self.is_min = is_min

    def compare(self, a,b):
        if self.is_min:
            return a < b
        return a > b
class priorityQueueArray():
    def __init__(self):
        self.pq = []
        self.is_min = True

        self.cp = comparator(self.is_min)

    def is_empty(self):
        return True if self.pq is None else False

    def insert(self, priority, value):
        new_element = priorityQueueElement(priority, value)

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


a = priorityQueueArray()
a.insert(2,2)
a.insert(3,4)
a.insert(1,2)

print(a.peek())
