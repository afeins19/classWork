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