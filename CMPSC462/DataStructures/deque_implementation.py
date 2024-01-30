from Queue import Queue

class deque:
    def __init__(self):
        self.deque = Queue()

    def enqueue(self, item):
        self.deque.enqueue(item)

    def deque(self):
        self.deque.dequeue()

    def isEmpty(self):
        return self.deque.size() == 0

    def size(self):
        return self.deque.size()