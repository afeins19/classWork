"""
Exercise-2:
Write down the algorithm and implement a priority queue (both min and max) using a linked list of
elements. Determine the runtime for each of the following:
    1. In the worst case, describe the runtime to insert an item into the priority queue.
    2. In the worst case, describe the runtime to remove the target with highest priority.
    3. In the worst case, describe the runtime to change the priority of an target.
    Show an example for each.

insert(item, priorityValue)
    Inserts item into the priority queue with priority value priorityValue.

peek()
    Returns (but does not remove) the item with highest priority in the priority queue.

delete()
    Removes and returns the item with highest priority in the priority queue.

changePriority(item, newPriority)
    Changes the priority of an item to a new priority value.

"""
from base_classes import Comparator, PriorityQueueElement

# takes in elements of type PriorityQueueElement
class Node():
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class priorityQueueLinkedList():
    def __init__(self, head=None, is_min = True):
        self.head = head
        self.is_min = is_min
        self.cp = Comparator(self.is_min)

    def is_empty(self):
        return self.head == None

    def insert(self, priority, val):
        new_node = Node(PriorityQueueElement(priority, val))

        # if ll is empty or new node will replace the current head...
        if self.is_empty() or self.cp.compare(priority, self.head.element.p):
            new_node.next = self.head
            self.head = new_node

        # other wise, follow normal insertion procedure
        else:
            cur = self.head # set cur to loop over ll starting from head
            while cur.next and not self.cp.compare(priority, cur.next.element.p): # find correct position
                cur = cur.next

            # perform insertion
            new_node.next = cur.next
            cur.next = new_node


    def peek(self):
        # gets the first target in the linked list
        if self.head:
            return self.head.element


    def delete(self):
        # removes the target with the highest priority (the current head)
        if self.head:
            self.head = self.head.next


    def change_priority(self, new_priority, val):
        # remove the old node first
        cur = self.head
        prev = None

        while cur and cur.element.v != val:
            prev = cur
            cur = cur.next

        if cur:
            if prev:
                prev.next = cur.next
            else:
                self.head = cur.next

            #  insert the new node with updated priority
            self.insert(new_priority, val)

test_ll = priorityQueueLinkedList()
test_ll.insert(1,'a')
test_ll.insert(2,'b')
test_ll.delete()
print(test_ll.peek())
