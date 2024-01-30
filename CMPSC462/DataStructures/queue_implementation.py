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

