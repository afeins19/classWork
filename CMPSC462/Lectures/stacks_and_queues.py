"""
    Stacks and Queues
Stacks -  (Last In First Out)
    - push()
    - pop()

Queue  - (First in First Out)
    - enqueue() (add)
    - deque() (remove)

These are abstract data structures...functionality is defined, implementation is not.
"""

class Stack:
    def __init__(self):
        self.stack = list()
    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[self.size()-1]
        return None

class Queue:
    def __init__(self):
        self.queue = list()
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)



