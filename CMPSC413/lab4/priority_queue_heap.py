"""
Exercise-3:
    Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based
    data structure (both min and max). Determine the runtime for each of the following:
    1. In the worst case, describe the runtime to insert an item into the priority queue.
    2. In the worst case, describe the runtime to remove the target with highest priority.
    3. In the worst case, describe the runtime to change the priority of an target.
    Show an example for each.
"""

from base_classes import Comparator, PriorityQueueElement

# the node of our tree
class Node():
    def __init__(self, element, l_child = None, r_child = None):
        self.element = element
        self.l_child = l_child
        self.r_child = r_child

class priorityQueueTree():
    def __init__(self, root=None, is_min=True):
        self.root = root
        self.is_min = is_min
        self.cp = Comparator.compare(is_min)

    def insert(self, priority, val):
        element = Node(PriorityQueueElement(priority=priority, value=val))

        cur = self.root

        while cur and not self.cp(element.p, cur.p):
            pass

    def make_insertion(self, node_to_insert, node_cur):
        # if tree is empty or we recursed to a leaf node return
        if not node_cur.element:
            return

        # compare nodes value to current node, if the current nodes position is out of place, recurse down
        if not self.cp(node_to_insert.element.p, node_to_insert.element.p):
            self.make_insertion(node_to_insert.element.p, node_cur.l_child)
            self.make_insertion(node_to_insert.element.p, node_cur.r_child)

        # node is in correct position, insert it
        else:
            # save a temp copy of the target in the cur position
            temp_node = node_cur

            # replace node in current position with node we're inserting
            node_cur.element = node_to_insert.element

            # insert the temp node back in
            self.make_insertion(temp_node, self.root)






