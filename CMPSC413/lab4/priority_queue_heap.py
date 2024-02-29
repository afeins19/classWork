"""
Exercise-3:
    Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based
    data structure (both min and max). Determine the runtime for each of the following:
    1. In the worst case, describe the runtime to insert an item into the priority queue.
    2. In the worst case, describe the runtime to remove the element with highest priority.
    3. In the worst case, describe the runtime to change the priority of an element.
    Show an example for each.
"""

from base_classes import comparator, priorityQueueElement

# the node of our tree
class Node():
    def __init__(self, element, l_child = None, r_child = None):
        self.element = element
        self.l_child = l_child
        self.r_child = r_child

class priorityQueueTree():
    def __init__(self, root=None):
        self.root = root

    def insert(self, priority, val):
        # create new node to insert element
        node = Node(priorityQueueElement(priority, val))

        # case - tree has no root
        if not self.root:
            self.root = node

        """@TODO: write code to implement insertion of new nodes into heap"""
