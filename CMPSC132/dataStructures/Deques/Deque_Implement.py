'''Deque (deck): FIFO and LIFO Data Strucutre front of deque is end of list'''

from Data_Structures.Queues.Queue_Implement import Queue

class Deque(Queue):
    def __init__(self):
        super().__init__()

    def addFront(self,item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    