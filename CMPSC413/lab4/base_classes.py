"""
Comparater()
    takes in the ordering scheme of the priority queue and compares elements
    based on if the invoking priority queue is a max or min queue.

"""

class comparator():
    # returns a function to be used in lambda based on the ordering scheme of the priority queue
    def __init__(self, is_min=True): # by default sorts by min priority first
        self.is_min = is_min

    def compare(self, a,b):
        if self.is_min:
            return a < b
        return a > b

class priorityQueueElement():
    def __init__(self, priority, value):
        self.p = priority
        self.v = value
    def __repr__(self):
        return f"[{self.p} , {self.v}]"