'''Implementing the que data strucutre using only stacks:

example: we have a line of customers waiting to order, can you serve them in FIFO order?
'''

from Data_Structures.Stacks.Stack_Implement import Stack

class stackQueue():
    def __init__(self):
        self.stuff = Stack()
        self.dump=Stack()

    def isEmpty(self):
        return self.stuff.isEmpty()

    def enqueue(self,item):
        if self.dump.isEmpty():
            self.dump.push(item)
        else:
            for i in self.dump.items:
                self.stuff.push(self.dump.pop())
            self.dump.push(item)
        for i in self.stuff.items:
            self.dump.push(self.stuff.pop())

    def dequeue(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)

a = stackQueue()
a.enqueue(1)
a.enqueue(2)
print(a.stuff.items)

print(a.isEmpty())



