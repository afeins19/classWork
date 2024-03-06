"""How do you implement a queue using 2 stacks"""
from Labs import Stack

class QueueFromStack:
    def __init__(self):
        self.main_stack = Stack.Stack()
        self.temp_stack = Stack.Stack()

    def enque(self, item):
        # items added to the end will simply be appended
        self.main_stack.push(item)

    def deque(self):
        # pops items to a temporary stack to reverse the order (now ordered as a list)
        for i in range(self.main_stack.size()):
            self.temp_stack.push(self.main_stack.pop())

        # saves the first target to be popped
        out = self.temp_stack.pop()

        # returns the elements back to the original stack to allow for safe enqueing
        for j in range(self.temp_stack.size()):
            self.main_stack.push(self.temp_stack.pop())

        return out

    def is_empty(self):
        return len(self.main_stack.stack) == 0

    def size(self):
        return self.main_stack.size()

#instantiating
myQueue = QueueFromStack()

#populating the queue
myQueue.enque(1)
myQueue.enque(2)
myQueue.enque(3)
myQueue.enque(4)
myQueue.enque(5)

#popping (FIFO order)
while not myQueue.is_empty():
    print(myQueue.deque())
