'''stack data structure'''
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[len(self.stack)-1]
        else:
            return None

    def isEmpty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


