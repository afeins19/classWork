'''Implementation of the Queue data structure (last item in list is front)'''

class Queue():
    def __init__(self):
        self.items=list()

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop(0)

    def isEmpty(self):
        if len(self.items)==0:
            return True
        return False

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



