"""
Exercise-3:
    Write down the algorithm and implement a priority queue (both min and max) using a heap tree-based
    data structure (both min and max). Determine the runtime for each of the following:
    1. In the worst case, describe the runtime to insert an item into the priority queue.
    2. In the worst case, describe the runtime to remove the target with highest priority.
    3. In the worst case, describe the runtime to change the priority of an target.
    Show an example for each.

"""

from base_classes import PriorityQueueElement, Comparator

class PriorityQueueHeap():
    def __init__(self, is_min=True):
        self.is_min = is_min # priority ordering set to min by default
        self.pq = [] # list based implementation
        self.cp = Comparator(is_min).compare

    def is_empty(self):
        return len(self.pq) == 0

    def get_r_child_idx(self, parent_idx):
        r_child_idx = (2 * parent_idx) + 2

        if r_child_idx < len(self.pq):
            return r_child_idx
        return None

    def get_l_child_idx(self, parent_idx):
        l_child_idx = (2 * parent_idx) + 1

        if l_child_idx < len(self.pq):
            return l_child_idx
        return None

    def get_parent_idx(self, element_idx): # using O(logn) time to find element (best case)
        return (element_idx - 1) // 2

    # finds the index of a target
    def get_element_idx(self, target):
        for i, element in enumerate(self.pq): # unpacks the element object
            if element == target:
                return i
        return None  # Element not found

    def insert(self, priority, value):
        element = PriorityQueueElement(priority=priority, value=value) # make a new element object
        self.pq.append(element) # throw it in the array
        self.bubble_up(len(self.pq) - 1) # bubble it up to the correct position

    def bubble_up(self, start_idx=0):
        # start bubbling up from the specified index
        cur_idx = start_idx

        while cur_idx > 0:  # stop if node is at the root
            parent_idx = self.get_parent_idx(cur_idx)

            # check if the heap property is violated and swap if it is
            if self.cp(self.pq[cur_idx].p, self.pq[parent_idx].p):
                self.pq[cur_idx], self.pq[parent_idx] = self.pq[parent_idx], self.pq[cur_idx]
                cur_idx = parent_idx  # move up to the parent index
            else:
                break  # stop if the heap property is not violated

    def bubble_down(self, cur_idx=0):
        # keep within bounds of array
        while cur_idx < len(self.pq):
            l_idx = self.get_l_child_idx(cur_idx)
            r_idx = self.get_r_child_idx(cur_idx)
            swap_idx = None

            # find which child to swap with
            if l_idx is not None and (r_idx is None or self.cp(self.pq[l_idx].p, self.pq[r_idx].p)): # max priority left
                swap_idx = l_idx
            elif r_idx is not None: # max priority right
                swap_idx = r_idx

            # do the swap if we need to
            if swap_idx is not None and not self.cp(self.pq[cur_idx].p, self.pq[swap_idx].p):
                self.pq[cur_idx], self.pq[swap_idx] = self.pq[swap_idx], self.pq[cur_idx]
                cur_idx = swap_idx
            else:
                break # don't need to swap so we're done

    def get_root(self):
        return self.pq[0]

    def peek(self):
        # will return the element at the root position
        if not self.is_empty():
            return self.pq[0]

    def delete(self): # functions like pop() on the heap
        if self.is_empty():
            return None

        root = self.get_root()
        last_element = self.pq.pop()  # remove the last element

        if not self.is_empty():  # check if the heap is not empty after removing the last element
            self.pq[0] = last_element  # place the last element at the root
            self.bubble_down(0)  # heapify the heap

        return root

    def change_priority(self, element, new_priority):
        element_idx = self.get_element_idx(element) # finding the element in the pq
        self.pq[element_idx].p = new_priority # updating the priority in place

        if element_idx: # if element exists
            # see if we need to bubble up or down
            # bubble up - new priority is higher than old
            # true when new_priority > cur_priority and we have max or new_priority < cur_priority and we have min
            if self.is_min and new_priority < element.p:
                self.bubble_up(start_idx=element_idx)
            elif not self.is_min and new_priority > element.p:
                self.bubble_up(start_idx=element_idx)
            else:
                self.bubble_down()


